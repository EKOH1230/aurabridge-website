"""Check the static preview before publishing it."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
# Terms assembled at runtime; do not store supplier names in plaintext on the published tree.
FORBIDDEN = re.compile(
    "|".join(
        [
            "Obbo" + "Med",
            "obbo" + "med",
            "Jing" + "Mei" + "Rui",
            "景" + "美" + "瑞",
            "Kimai" + "ray",
            "szbeti" + "co",
            "Foun" + "der",
            "foun" + "der",
        ]
    ),
    re.I,
)
ALLOWED_EXTERNAL = (
    "https://ekoh1230.github.io/",
    "https://www.brightbridgegroup.com",
    "https://github.com",
    "https://pages.github.com",
    "https://docs.github.com/",
    "https://www.cnil.fr",
    "mailto:",
    "tel:",
    "#",
)
# Storage / tracking APIs should not appear in first-party JS.
STORAGE = re.compile(r"localStorage|sessionStorage|document\.cookie|googleapis|gstatic|gtag|analytics|hotjar|facebook\.net|unpkg|jsdelivr|fonts\.google", re.I)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hreflang = []
        self.hrefs = []
        self.srcs = []
        self.h1 = 0
        self.title = 0
        self.missing_alt = 0
        self.empty_content_alt = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title += 1
        if tag in {"a", "link"} and a.get("href"):
            self.hrefs.append(a["href"])
            if a.get("hreflang"):
                self.hreflang.append(a["href"])
        if tag in {"img", "script", "source"} and a.get("src"):
            self.srcs.append(a["src"])
        if tag == "img":
            if "alt" not in a:
                self.missing_alt += 1
            elif a.get("alt") == "" and "data-gallery-thumb" not in str(attrs):
                # thumbnails inside buttons may be empty; main/hero images must not
                src = a.get("src", "")
                if "data-gallery-thumb" not in a and not src.endswith("aurabridge-logo.png"):
                    # empty alt on thumbs is OK; detect thumbs by sizes=48px or 72px later
                    if a.get("sizes") in {"48px", "72px"}:
                        return
                    if a.get("alt") == "" and ("kh-" in src or "ob-1600" in src) and "product-card__thumbs" not in src:
                        # still could be a thumb; record only if width is large? skip thumbs via parent is hard.
                        pass


def iter_html():
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        yield path


def resolve(page: Path, link: str) -> Path | None:
    if not link or link.startswith(("#", "mailto:", "tel:", "http://", "https:")):
        return None
    return (page.parent / link.split("#", 1)[0]).resolve()


def main() -> int:
    errors = []
    pages = list(iter_html())
    if len(pages) < 40:
        errors.append(f"expected around 45 HTML pages, found {len(pages)}")

    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(ROOT)
        if FORBIDDEN.search(text):
            errors.append(f"{rel}: forbidden supplier or role term")
        parser = PageParser()
        parser.feed(text)
        if parser.h1 != 1:
            errors.append(f"{rel}: expected one h1, found {parser.h1}")
        if parser.title != 1:
            errors.append(f"{rel}: expected one title, found {parser.title}")
        if parser.missing_alt:
            errors.append(f"{rel}: image without alt attribute")
        # content images: hero, highlight, gallery main, logo
        for m in re.finditer(r"<img\b[^>]*>", text):
            tag = m.group(0)
            if 'alt="' not in tag and "alt='" not in tag:
                errors.append(f"{rel}: img missing alt: {tag[:80]}")
                continue
            alt_m = re.search(r'alt="([^"]*)"', tag)
            src_m = re.search(r'src="([^"]+)"', tag)
            alt = alt_m.group(1) if alt_m else None
            src = src_m.group(1) if src_m else ""
            is_thumb = "sizes=\"48px\"" in tag or "sizes=\"72px\"" in tag or "sizes='48px'" in tag
            is_logo = src.endswith("aurabridge-logo.png")
            if alt == "" and not is_thumb and not is_logo:
                errors.append(f"{rel}: empty alt on content image {src}")
        for link in parser.hrefs + parser.srcs:
            if not link or link.startswith("#"):
                continue
            if link.startswith(("http://", "https://", "mailto:", "tel:")):
                if not any(link.startswith(allow) or allow.rstrip("/") in link for allow in ALLOWED_EXTERNAL):
                    # x-default and hreflang use the preview host, already allowed
                    errors.append(f"{rel}: unexpected external URL {link}")
                continue
            target = resolve(page, link)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{rel}: missing target {link}")

        # required legal links in footer
        if "legal.html" not in text or "privacy.html" not in text:
            if page.name not in {"legal.html", "privacy.html"}:
                # legal pages link to themselves via nav? footer should still have both
                if "legal.html" not in text:
                    errors.append(f"{rel}: missing legal.html link")
                if "privacy.html" not in text:
                    errors.append(f"{rel}: missing privacy.html link")

    for path in [ROOT / "assets" / "site.js", ROOT / "assets" / "site.css"]:
        text = path.read_text(encoding="utf-8")
        if STORAGE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: tracking or third-party pattern")
        if FORBIDDEN.search(text):
            errors.append(f"{path.relative_to(ROOT)}: forbidden term")

    # required pages
    for name in ("legal.html", "privacy.html", "zh/legal.html", "fr/privacy.html", "de/legal.html", "es/privacy.html"):
        if not (ROOT / name).exists():
            errors.append(f"missing {name}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(pages)} pages: links, alt text, titles, headings, allowed URLs, and forbidden terms are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
