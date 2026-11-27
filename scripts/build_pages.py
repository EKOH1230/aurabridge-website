#!/usr/bin/env python3
"""Generate the AuraBridge static preview pages in five languages."""
from __future__ import annotations

import html as html_lib
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ekoh1230.github.io/aurabridge-website"
TODO = '<mark class="todo-gap">【待补】</mark>'
LANGS = ("en", "zh", "fr", "de", "es")
HREFLANG = {"en": "en", "zh": "zh-Hans", "fr": "fr", "de": "de", "es": "es"}
HTML_LANG = {"en": "en", "zh": "zh-Hans", "fr": "fr", "de": "de", "es": "es"}
LANG_DIR = {"en": "", "zh": "zh", "fr": "fr", "de": "de", "es": "es"}
LANG_LABEL = {"en": "EN", "zh": "中文", "fr": "FR", "de": "DE", "es": "ES"}

# Small inline SVG flags for the language switcher (not emoji). EN uses the
# GB flag, ZH the CN flag, as specified. Decorative; labels stay on the codes.
_FLAG_SVG = {
    "en": (
        '<svg class="lang-flag__svg" viewBox="0 0 24 16" focusable="false" aria-hidden="true">'
        '<rect width="24" height="16" fill="#012169"/>'
        '<path d="M0 0l24 16M24 0L0 16" stroke="#fff" stroke-width="3.2"/>'
        '<path d="M0 0l24 16M24 0L0 16" stroke="#C8102E" stroke-width="1.6"/>'
        '<path d="M12 0v16M0 8h24" stroke="#fff" stroke-width="5.2"/>'
        '<path d="M12 0v16M0 8h24" stroke="#C8102E" stroke-width="3.2"/>'
        '</svg>'
    ),
    "fr": (
        '<svg class="lang-flag__svg" viewBox="0 0 24 16" focusable="false" aria-hidden="true">'
        '<rect width="8" height="16" fill="#002654"/>'
        '<rect x="8" width="8" height="16" fill="#fff"/>'
        '<rect x="16" width="8" height="16" fill="#ED2939"/>'
        '</svg>'
    ),
    "de": (
        '<svg class="lang-flag__svg" viewBox="0 0 24 16" focusable="false" aria-hidden="true">'
        '<rect width="24" height="5.34" fill="#000"/>'
        '<rect y="5.33" width="24" height="5.34" fill="#DD0000"/>'
        '<rect y="10.66" width="24" height="5.34" fill="#FFCE00"/>'
        '</svg>'
    ),
    "es": (
        '<svg class="lang-flag__svg" viewBox="0 0 24 16" focusable="false" aria-hidden="true">'
        '<rect width="24" height="16" fill="#AA151B"/>'
        '<rect y="4" width="24" height="8" fill="#F1BF00"/>'
        '</svg>'
    ),
    "zh": (
        '<svg class="lang-flag__svg" viewBox="0 0 24 16" focusable="false" aria-hidden="true">'
        '<rect width="24" height="16" fill="#DE2910"/>'
        '<polygon fill="#FFDE00" points="4.00,1.60 4.54,3.26 6.28,3.26 4.87,4.28 5.41,5.94 4.00,4.92 2.59,5.94 3.13,4.28 1.72,3.26 3.46,3.26"/>'
        '<polygon fill="#FFDE00" points="7.31,2.01 7.70,1.57 7.40,1.07 7.93,1.30 8.31,0.86 8.26,1.44 8.80,1.67 8.23,1.80 8.18,2.38 7.88,1.88"/>'
        '<polygon fill="#FFDE00" points="8.81,3.31 9.33,3.06 9.25,2.48 9.65,2.90 10.17,2.64 9.90,3.16 10.31,3.57 9.73,3.47 9.46,3.99 9.38,3.41"/>'
        '<polygon fill="#FFDE00" points="8.83,5.38 9.41,5.36 9.57,4.80 9.77,5.35 10.35,5.33 9.89,5.68 10.09,6.23 9.61,5.91 9.15,6.26 9.31,5.70"/>'
        '<polygon fill="#FFDE00" points="7.38,6.70 7.92,6.91 8.28,6.45 8.26,7.03 8.80,7.24 8.24,7.39 8.21,7.97 7.89,7.49 7.33,7.64 7.69,7.19"/>'
        '</svg>'
    ),
}


def lang_flag_label(code: str) -> str:
    return (
        f'<span class="lang-flag" aria-hidden="true">{_FLAG_SVG[code]}</span>'
        f'<span class="lang-switch__code">{html_lib.escape(LANG_LABEL[code])}</span>'
    )




def esc(s: str) -> str:
    return html_lib.escape(s, quote=True)


def current_dir(lang: str, nested: bool) -> str:
    parts = []
    if lang != "en":
        parts.append(lang)
    if nested:
        parts.append("products")
    return "/".join(parts)


def rel(from_dir: str, to_path: str) -> str:
    start = from_dir if from_dir else "."
    return os.path.relpath(to_path, start).replace("\\", "/")


def root_path(lang: str, filename: str) -> str:
    folder = LANG_DIR[lang]
    return f"{folder}/{filename}" if folder else filename


def page_url(lang: str, filename: str) -> str:
    return f"{SITE}/{root_path(lang, filename)}"


def here(lang: str, filename: str, nested: bool) -> str:
    return rel(current_dir(lang, nested), root_path(lang, filename))


def asset(lang: str, path: str, nested: bool) -> str:
    return rel(current_dir(lang, nested), path)

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import UI, PAGES
from legal import legal_body, privacy_body
from range_products import MODELS as RANGE_MODELS, DESC_SUFFIX, by_group

KH2406 = [
    ("assets/products/kh-2406/kh-2406-1.jpg", 1141, 1600, "front"),
    ("assets/products/kh-2406/kh-2406-2.jpg", 1141, 1600, "apart"),
    ("assets/products/kh-2406/kh-2406-3.jpg", 1141, 1600, "heads"),
    ("assets/products/kh-2406/kh-2406-4.jpg", 1600, 1436, "studio"),
    ("assets/products/kh-2406/kh-2406-5.jpg", 1425, 1600, "side"),
    ("assets/products/kh-2406/kh-2406-6.jpg", 900, 1600, "use"),
]
KH2307 = [
    ("assets/product-images/kh-2307-1.jpg", 800, 800, "main"),
    ("assets/product-images/kh-2307-2.jpg", 800, 800, "reservoir"),
    ("assets/product-images/kh-2307-3.jpg", 800, 800, "apply"),
    ("assets/product-images/kh-2307-4.jpg", 800, 800, "side"),
]
OB1600 = [
    ("assets/product-images/ob-1600.jpg", 1200, 900, "main"),
]

# Homepage and listing card thumbnails only. Same crop as files[0], with the
# background recolored to the card field (#f3f7f9) so object-fit:contain
# letterboxing does not show a mismatched band. Product detail galleries
# keep the original studio photos. OB-1600 stays on its existing cutout.
KH2406_CARD = "assets/products/kh-2406/kh-2406-1-card.jpg"
KH2307_CARD = "assets/product-images/kh-2307-1-card.jpg"
OB1600_CARD = "assets/product-images/ob-1600-card.jpg"


def card_files(files, card_path: str):
    path, w, h, _key = files[0]
    return [(card_path, w, h, "card")] + list(files[1:])


def alts(lang: str):
    c = PAGES[lang]
    # Keep English descriptive alts as the base; other langs use translated short alts already in PAGES for heroes,
    # plus specific gallery alts below.
    gallery = {
        "en": {
            "kh2406": [
                "KH-2406 precision scalp serum applicator, front view",
                "KH-2406 scalp serum applicator taken apart, showing the comb head, body, and cap",
                "KH-2406 applicator heads, a comb head and a roller-ball tip",
                "KH-2406 scalp serum applicator, studio photo on white",
                "KH-2406 scalp serum applicator on its side, studio photo on white",
                "KH-2406 scalp serum applicator held against the scalp",
            ],
            "kh2307": [
                "KH-2307 scalp roller with serum reservoir",
                "KH-2307 scalp roller, reservoir view",
                "KH-2307 scalp roller for serum application",
                "KH-2307 scalp roller, side view",
            ],
            "ob1600": ["OB-1600 alternating-pressure air mattress"],
        },
        "zh": {
            "kh2406": [
                "KH-2406 精密头皮精华涂抹器，正面",
                "KH-2406 头皮精华涂抹器拆开，显示梳齿头、主体和盖帽",
                "KH-2406 涂抹器头：梳齿头和滚珠头",
                "KH-2406 头皮精华涂抹器，白底照片",
                "KH-2406 头皮精华涂抹器侧放，白底照片",
                "KH-2406 头皮精华涂抹器贴在头皮上使用",
            ],
            "kh2307": [
                "KH-2307 带精华储液的头皮滚轮",
                "KH-2307 头皮滚轮，储液视角",
                "KH-2307 用于涂抹精华的头皮滚轮",
                "KH-2307 头皮滚轮，侧面",
            ],
            "ob1600": ["OB-1600 交替压力气垫"],
        },
        "fr": {
            "kh2406": [
                "Applicateur de précision KH-2406 pour sérum capillaire, vue de face",
                "Applicateur KH-2406 démonté, montrant la tête peigne, le corps et le bouchon",
                "Têtes de l’applicateur KH-2406 : tête peigne et embout à bille",
                "Applicateur KH-2406, photo studio sur fond blanc",
                "Applicateur KH-2406 posé sur le côté, photo studio sur fond blanc",
                "Applicateur KH-2406 tenu contre le cuir chevelu",
            ],
            "kh2307": [
                "Rouleau KH-2307 pour cuir chevelu avec réservoir de sérum",
                "Rouleau KH-2307, vue du réservoir",
                "Rouleau KH-2307 pour l’application de sérum",
                "Rouleau KH-2307, vue de côté",
            ],
            "ob1600": ["Matelas à air à pression alternée OB-1600"],
        },
        "de": {
            "kh2406": [
                "Präzisionsapplikator KH-2406 für Kopfhautserum, Vorderansicht",
                "Applikator KH-2406 zerlegt, mit Kammkopf, Gehäuse und Kappe",
                "Applikatorköpfe KH-2406: Kammkopf und Rollkugelspitze",
                "Applikator KH-2406, Studiofoto auf Weiß",
                "Applikator KH-2406 seitlich liegend, Studiofoto auf Weiß",
                "Applikator KH-2406 an die Kopfhaut gehalten",
            ],
            "kh2307": [
                "Kopfhautroller KH-2307 mit Serumreservoir",
                "Kopfhautroller KH-2307, Reservoiransicht",
                "Kopfhautroller KH-2307 zum Auftragen von Serum",
                "Kopfhautroller KH-2307, Seitenansicht",
            ],
            "ob1600": ["Luftmatratze mit Wechseldruck OB-1600"],
        },
        "es": {
            "kh2406": [
                "Aplicador de precisión KH-2406 para sérum del cuero cabelludo, vista frontal",
                "Aplicador KH-2406 desmontado, con el cabezal de peine, el cuerpo y el tapón",
                "Cabezales del aplicador KH-2406: cabezal de peine y punta de bola",
                "Aplicador KH-2406, foto de estudio sobre fondo blanco",
                "Aplicador KH-2406 de lado, foto de estudio sobre fondo blanco",
                "Aplicador KH-2406 aplicado sobre el cuero cabelludo",
            ],
            "kh2307": [
                "Rodillo KH-2307 para el cuero cabelludo con depósito de sérum",
                "Rodillo KH-2307, vista del depósito",
                "Rodillo KH-2307 para aplicar sérum",
                "Rodillo KH-2307, vista lateral",
            ],
            "ob1600": ["Colchón de aire de presión alterna OB-1600"],
        },
    }
    return gallery[lang]


def hreflang_tags(filename: str) -> str:
    parts = []
    for lang in LANGS:
        parts.append(
            f'<link rel="alternate" hreflang="{HREFLANG[lang]}" href="{page_url(lang, filename)}">'
        )
    parts.append(f'<link rel="alternate" hreflang="x-default" href="{page_url("en", filename)}">')
    return "".join(parts)


def header(lang: str, filename: str, nested: bool = False) -> str:
    u = UI[lang]
    cur = current_dir(lang, nested)
    logo = asset(lang, "assets/aurabridge-logo.png", nested)
    css = asset(lang, "assets/site.css", nested)
    js = asset(lang, "assets/site.js", nested)
    fav = asset(lang, "assets/favicon.svg", nested)
    home = here(lang, "index.html", nested)
    products = here(lang, "products.html", nested)
    about = here(lang, "about.html", nested)
    partnerships = here(lang, "partnerships.html", nested)
    contact = here(lang, "contact.html", nested)

    def cur_attr(page: str) -> str:
        if filename == page:
            return ' aria-current="page"'
        if page == "products.html" and filename.startswith("products/"):
            return ' aria-current="page"'
        return ""

    nav_pages = [
        (home, "home", "index.html"),
        (products, "products", "products.html"),
        (about, "about", "about.html"),
        (partnerships, "partnerships", "partnerships.html"),
    ]
    links = "".join(
        f'<a href="{href}"{cur_attr(page)}>{esc(u[key])}</a>'
        for href, key, page in nav_pages
    )
    contact_cur = ' aria-current="page"' if filename == "contact.html" else ""
    links += f'<a class="nav-contact" href="{contact}"{contact_cur}>{esc(u["contact"])} <span aria-hidden="true">↗</span></a>'

    lang_items = []
    for other in LANGS:
        href = rel(cur, root_path(other, filename))
        current = " aria-current=\"true\"" if other == lang else ""
        lang_items.append(
            f'<li><a href="{href}" hreflang="{HREFLANG[other]}" lang="{HTML_LANG[other]}"{current}>{lang_flag_label(other)}</a></li>'
        )
    return f'''  <a class="skip-link" href="#main">{esc(u["skip"])}</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{home}" aria-label="{esc(u["home"])} — AuraBridge"><img src="{logo}" alt="AuraBridge" width="1319" height="400"></a>
      <div class="header-end">
        <nav class="site-nav" id="site-nav" aria-label="{esc(u["nav_aria"])}" data-site-nav>{links}</nav>
        <div class="lang-switch" data-lang-switch>
          <button class="lang-switch__button" type="button" aria-expanded="false" aria-controls="lang-menu" aria-label="{esc(u["lang_aria"])}: {esc(LANG_LABEL[lang])}">{lang_flag_label(lang)}</button>
          <ul class="lang-switch__menu" id="lang-menu" hidden>{''.join(lang_items)}</ul>
        </div>
        <button class="menu-button" type="button" aria-label="{esc(u["menu_open"])}" aria-expanded="false" aria-controls="site-nav" data-menu-button><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
      </div>
    </div>
  </header>'''


def footer(lang: str, nested: bool = False) -> str:
    u = UI[lang]
    about = here(lang, "about.html", nested)
    partnerships = here(lang, "partnerships.html", nested)
    products = here(lang, "products.html", nested)
    contact = here(lang, "contact.html", nested)
    legal = here(lang, "legal.html", nested)
    privacy = here(lang, "privacy.html", nested)
    home = here(lang, "index.html", nested)
    return f'''  <footer class="site-footer"><div class="container footer-main"><div><a class="footer-brand" href="{home}">AuraBridge</a><p>{esc(u["footer_brand"])}</p><p class="footer-parent"><a href="https://www.brightbridgegroup.com" target="_blank" rel="noopener noreferrer">{esc(u["footer_parent"])}<span class="visually-hidden">{esc(u["new_tab"])}</span></a></p><p class="footer-address"><span class="address-label">{esc(u["addr_mainland"])}</span>{esc(u["mainland"])}</p><p class="footer-address"><span class="address-label">{esc(u["addr_holding"])}</span>{esc(u["holding"])}</p><div class="footer-links footer-contact"><a href="mailto:ohashi@brightbridgegroup.com">ohashi@brightbridgegroup.com</a><a href="tel:+8676989399795">+86 769 8939 9795</a></div></div><div><h3>{esc(u["explore"])}</h3><div class="footer-links"><a href="{about}">{esc(u["about"])}</a><a href="{partnerships}">{esc(u["partnerships"])}</a><a href="{products}">{esc(u["products"])}</a></div></div><div><h3>{esc(u["information"])}</h3><div class="footer-links"><a href="{contact}">{esc(u["contact"])}</a><a href="{legal}">{esc(u["legal"])}</a><a href="{privacy}">{esc(u["privacy"])}</a></div></div></div><div class="container footer-bottom"><span>© 2026 AuraBridge</span><span>Hong Kong Bright Bridge Group Co., Limited</span></div></footer>
<button class="back-to-top" type="button" data-back-to-top hidden aria-label="{esc(u["back_top"])}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 14l6-6 6 6"/></svg></button>'''


def quote_form(lang: str, nested: bool = False, selected: str | None = None) -> str:
    u = UI[lang]
    privacy = here(lang, "privacy.html", nested)
    link = f'<a href="{privacy}">{esc(u["privacy_link"])}</a>'
    notice = u["quote_privacy"].replace("{link}", link)
    options = [
        ("", u["select_product"]),
        ("KH-2406", u["p_kh2406"]),
        ("KH-2307", u["p_kh2307"]),
    ] + [(m["model"], f'{m["model"]} {m["copy"][lang]["name"]}') for m in RANGE_MODELS] + [
        ("OB-1600", u["p_ob1600"]),
        ("Other", u["other"]),
    ]
    option_html = []
    for value, label in options:
        sel = " selected" if selected and value == selected else ""
        option_html.append(f'<option value="{esc(value)}"{sel}>{esc(label)}</option>')
    return f'''    <section class="quote-band" id="request-a-quote" aria-labelledby="quote-title">
    <div class="container quote-layout">
      <div class="quote-intro">
        <div class="eyebrow">{esc(u["quote_eyebrow"])}</div>
        <h2 id="quote-title">{esc(u["quote_title"])}</h2>
        <p>{esc(u["quote_lead"])}</p>
      </div>
      <form class="quote-form" data-quote-form novalidate data-quote-subject="{esc(u["quote_subject"])}" data-label-name="{esc(u["label_name"])}" data-label-email="{esc(u["label_email"])}" data-label-company="{esc(u["label_company"])}" data-label-product="{esc(u["label_product"])}" data-sample-text="{esc(u["sample_text"])}" data-error-name="{esc(u["err_name"])}" data-error-email="{esc(u["err_email"])}" data-error-email-invalid="{esc(u["err_email_inv"])}" data-error-product="{esc(u["err_product"])}" data-error-message="{esc(u["err_message"])}">
        <div class="quote-field">
          <label for="quote-name">{esc(u["label_name"])}</label>
          <input id="quote-name" name="name" type="text" autocomplete="name" required aria-required="true" aria-describedby="quote-name-error">
          <p class="quote-error" id="quote-name-error" data-error-for="name"></p>
        </div>
        <div class="quote-field">
          <label for="quote-email">{esc(u["label_email"])}</label>
          <input id="quote-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-required="true" aria-describedby="quote-email-error">
          <p class="quote-error" id="quote-email-error" data-error-for="email"></p>
        </div>
        <div class="quote-field">
          <label for="quote-company">{esc(u["label_company"])} <span class="optional">{esc(u["optional"])}</span></label>
          <input id="quote-company" name="company" type="text" autocomplete="organization">
        </div>
        <div class="quote-field">
          <label for="quote-product">{esc(u["label_product"])}</label>
          <select id="quote-product" name="product" required aria-required="true" aria-describedby="quote-product-error">
            {''.join(option_html)}
          </select>
          <p class="quote-error" id="quote-product-error" data-error-for="product"></p>
        </div>
        <div class="quote-field quote-field--wide">
          <label for="quote-message">{esc(u["label_message"])}</label>
          <textarea id="quote-message" name="message" rows="5" required aria-required="true" aria-describedby="quote-message-error"></textarea>
          <p class="quote-error" id="quote-message-error" data-error-for="message"></p>
        </div>
        <div class="quote-actions">
          <button class="button primary" type="submit">{esc(u["send"])}</button>
          <p class="quote-note">{esc(u["quote_note"])}</p>
          <p class="quote-privacy">{notice}</p>
        </div>
      </form>
    </div>
  </section>'''


def shell(lang: str, filename: str, title: str, description: str, body: str, nested: bool = False, extra_css: bool = False, body_attr: str = "") -> str:
    css = asset(lang, "assets/site.css", nested)
    js = asset(lang, "assets/site.js", nested)
    fav = asset(lang, "assets/favicon.svg", nested)
    prod_css = f'<link rel="stylesheet" href="{asset(lang, "assets/products.css", nested)}">' if extra_css else ""
    return f'''<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#123f61">{hreflang_tags(filename)}
  <title>{esc(title)}</title>
  <link rel="icon" type="image/svg+xml" href="{fav}">
  <link rel="stylesheet" href="{css}">
  {prod_css}
  <script src="{js}" defer></script>
</head>
<body{body_attr}>
{header(lang, filename, nested)}
  <main id="main">
{body}
  </main>
{footer(lang, nested)}
</body>
</html>
'''


def write(lang: str, filename: str, html: str, nested: bool = False) -> None:
    dest = ROOT / root_path(lang, filename)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")


def work_list(items) -> str:
    rows = []
    for num, title, text in items:
        rows.append(f'<div class="work-item"><span class="number">{esc(num)}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></div>')
    return f'<div class="work-list">{"".join(rows)}</div>'


def callout(lang: str, eyebrow: str, title: str, href: str, label: str) -> str:
    return f'''<div class="callout"><div><div class="eyebrow light">{esc(eyebrow)}</div><h2>{esc(title)}</h2></div><a class="button light" href="{href}">{esc(label)} <span aria-hidden="true">↗</span></a></div>'''


def breadcrumb(lang: str, nested: bool, *trail) -> str:
    u = UI[lang]
    home = here(lang, "index.html", nested)
    parts = [f'<a href="{home}">{esc(u["home"])}</a>']
    for i, (href, label) in enumerate(trail):
        parts.append('<span>/</span>')
        if href and i < len(trail) - 1:
            parts.append(f'<a href="{href}">{esc(label)}</a>')
        else:
            parts.append(esc(label))
    return f'<div class="breadcrumb">{"".join(parts)}</div>'


def build_home(lang: str) -> None:
    c, u = PAGES[lang], UI[lang]
    a = alts(lang)
    nested = False
    p2406 = here(lang, "products/kh-2406.html", nested)
    p2307 = here(lang, "products/kh-2307.html", nested)
    p1600 = here(lang, "products/ob-1600.html", nested)
    products = here(lang, "products.html", nested)
    about = here(lang, "about.html", nested)
    partnerships = here(lang, "partnerships.html", nested)
    contact = here(lang, "contact.html", nested)
    img2406 = asset(lang, KH2406[0][0], nested)
    # Graded still-life of kh-2406-4.jpg for the homepage hero only. Separate
    # desktop and mobile frames keep the full product in view (no crop).
    img2406_hero = asset(lang, "assets/products/kh-2406/kh-2406-4-hero-desktop.jpg", nested)
    img2406_hero_m = asset(lang, "assets/products/kh-2406/kh-2406-4-hero-mobile.jpg", nested)
    img2406_card = asset(lang, KH2406_CARD, nested)
    img2307_card = asset(lang, KH2307_CARD, nested)
    img1600_card = asset(lang, OB1600_CARD, nested)
    body = f'''    <section class="hero">
      <div class="hero-media">
        <picture>
          <source media="(max-width: 900px)" srcset="{img2406_hero_m} 780w" sizes="100vw" width="780" height="700">
          <img src="{img2406_hero}" srcset="{img2406_hero} 2880w" sizes="100vw" alt="{esc(c["alt_kh2406_hero"])}" width="2880" height="1620">
        </picture>
      </div>
      <div class="container hero-inner">
        <div class="hero-copy">
          <div class="eyebrow">{esc(c["home_eyebrow"])}</div>
          <h1>{esc(c["home_h1"])}</h1>
          <p class="hero-lead">{esc(c["home_lead"])}</p>
          <div class="hero-actions"><a class="button light" href="{contact}#request-a-quote">{esc(c["cta_quote"])}</a></div>
        </div>
      </div>
    </section>
    <div class="preview-strip"><div class="container"><strong>{esc(c["strip_kicker"])}</strong><i aria-hidden="true"></i><span>{esc(c["strip_home"])}</span></div></div>
    <section class="section section-band-sky" aria-labelledby="portfolio-title"><div class="container"><div class="section-heading"><div class="eyebrow">{esc(c["range_eyebrow"])}</div><h2 id="portfolio-title">{esc(c["range_h2"])}</h2><p>{esc(c["range_p"])}</p><a class="text-link" href="{products}">{esc(c["browse_range"])} <span aria-hidden="true">→</span></a></div>
        <div class="highlight-grid">
          <a class="highlight" href="{p2406}"><img src="{img2406_card}" srcset="{img2406_card} 1141w" sizes="(min-width: 1000px) 30vw, (min-width: 640px) 45vw, 92vw" alt="{esc(a["kh2406"][0])}" width="1141" height="1600"><span>KH-2406</span><strong>{esc(u["name_kh2406"])}</strong></a>
          <a class="highlight" href="{p2307}"><img src="{img2307_card}" srcset="{img2307_card} 800w" sizes="(min-width: 1000px) 30vw, (min-width: 640px) 45vw, 92vw" alt="{esc(a["kh2307"][0])}" width="800" height="800"><span>KH-2307</span><strong>{esc(u["name_kh2307"])}</strong></a>
          <a class="highlight" href="{p1600}"><img src="{img1600_card}" srcset="{img1600_card} 1200w" sizes="(min-width: 1000px) 30vw, (min-width: 640px) 45vw, 92vw" alt="{esc(a["ob1600"][0])}" width="1200" height="900"><span>OB-1600</span><strong>{esc(u["name_ob1600"])}</strong></a>
        </div>
        {callout(lang, c["callout_eyebrow"], c["callout_h2"], contact + "#request-a-quote", c["cta_quote"])}
    </div></section>
    <section class="section section-band-soft" aria-labelledby="intro-title">
      <div class="container intro-grid">
        <div><div class="eyebrow">{esc(c["why_eyebrow"])}</div><h2 id="intro-title">{esc(c["why_h2"])}</h2></div>
        <div class="small-copy"><p class="large-copy">{esc(c["why_large"])}</p><p>{esc(c["why_p"])}</p><a class="text-link" href="{about}">{esc(c["more_about"])} <span aria-hidden="true">→</span></a></div>
      </div>
    </section>
    <section class="section tinted" aria-labelledby="focus-title">
      <div class="container"><div class="section-heading"><div class="eyebrow">{esc(c["work_eyebrow"])}</div><h2 id="focus-title">{esc(c["work_h2"])}</h2><p>{esc(c["work_p"])}</p></div>
        {work_list(c["work"])}
      </div>
    </section>
    <section class="section section-band-sky" aria-labelledby="connection-title"><div class="container split-panel"><div class="panel-photo"><img src="{img2406}" srcset="{img2406} 1141w" sizes="(min-width: 900px) 36vw, 92vw" alt="{esc(a["kh2406"][0])}" width="1141" height="1600"></div><div class="panel-copy"><div class="eyebrow">{esc(c["connect_eyebrow"])}</div><h2 id="connection-title">{esc(c["connect_h2"])}</h2><p>{esc(c["connect_p"])}</p><a class="text-link" href="{partnerships}">{esc(c["connect_link"])} <span aria-hidden="true">→</span></a></div></div></section>'''
    write(lang, "index.html", shell(lang, "index.html", c["home_title"], c["home_desc"], body, body_attr=' class="home"'))


def build_about(lang: str) -> None:
    c, u = PAGES[lang], UI[lang]
    products = here(lang, "products.html", False)
    body = f'''    <section class="page-hero"><div class="container">{breadcrumb(lang, False, (None, u["about"]))}<h1>{esc(c["about_h1"])}</h1><p>{esc(c["about_lead"])}</p></div></section>
    <div class="preview-strip"><div class="container"><strong>AuraBridge</strong><i aria-hidden="true"></i><span>{esc(c["about_strip"])}</span></div></div>
    <section class="section section-band-sky"><div class="container content-grid"><div><div class="eyebrow">{esc(c["about_eye"])}</div><h2>{esc(c["about_h2"])}</h2></div><div><p class="large-copy">{esc(c["about_large"])}</p><p>{esc(c["about_p1"])}</p><p>{esc(c["about_p2"])}</p></div></div></section>
    <section class="section section-band-navy"><div class="container content-grid"><div><div class="eyebrow">{esc(c["about_bb_eye"])}</div><h2>{esc(c["about_bb_h2"])}</h2></div><div><p class="large-copy">{esc(c["about_bb_large"])}</p><p>{esc(c["about_bb_p"])}</p><p><a class="text-link" href="https://www.brightbridgegroup.com" target="_blank" rel="noopener noreferrer">{esc(c["about_bb_link"])}<span class="visually-hidden">{esc(u["new_tab"])}</span></a></p></div></div></section>
    <section class="section"><div class="container"><div class="section-heading"><div class="eyebrow">{esc(c["work_eyebrow"])}</div><h2>{esc(c["work_h2"])}</h2><p>{esc(c["work_p"])}</p></div>{work_list(c["work"])}</div></section>
    <section class="section"><div class="container">{callout(lang, c["about_cta_eye"], c["about_cta"], products, c["cta_products"])}</div></section>'''
    write(lang, "about.html", shell(lang, "about.html", c["about_title"], c["about_desc"], body))


def build_partnerships(lang: str) -> None:
    c, u = PAGES[lang], UI[lang]
    contact = here(lang, "contact.html", False)
    body = f'''    <section class="page-hero"><div class="container">{breadcrumb(lang, False, (None, u["partnerships"]))}<h1>{esc(c["part_h1"])}</h1><p>{esc(c["part_lead"])}</p></div></section>
    <div class="preview-strip"><div class="container"><strong>{esc(u["partnerships"])}</strong><i aria-hidden="true"></i><span>{esc(c["part_strip"])}</span></div></div>
    <section class="section section-band-sky"><div class="container content-grid"><div><div class="eyebrow">{esc(c["part_eye"])}</div><h2>{esc(c["part_h2"])}</h2></div><div><p>{esc(c["part_p"])}</p><div class="note-box">{esc(c["part_note"])}</div></div></div></section>
    <section class="section tinted"><div class="container"><div class="section-heading"><div class="eyebrow">{esc(c["part_how_eye"])}</div><h2>{esc(c["part_how_h2"])}</h2><p>{esc(c["part_how_p"])}</p></div>{work_list(c["part_steps"])}</div></section>
    <section class="section"><div class="container">{callout(lang, c["part_cta_eye"], c["part_cta"], contact, c["contact_page"])}</div></section>'''
    write(lang, "partnerships.html", shell(lang, "partnerships.html", c["part_title"], c["part_desc"], body))


def thumbs(lang: str, files, alt_list, nested: bool, model: str, sizes: str) -> str:
    c = PAGES[lang]
    buttons = []
    for i, ((path, w, h, _key), alt) in enumerate(zip(files, alt_list), start=1):
        src = asset(lang, path, nested)
        pressed = "true" if i == 1 else "false"
        label = c["show_photo"].format(n=i, total=len(files))
        buttons.append(
            f'<button type="button" aria-pressed="{pressed}" aria-label="{esc(label)}" data-gallery-thumb data-src="{src}" data-srcset="{src} {w}w" data-width="{w}" data-height="{h}" data-alt="{esc(alt)}"><img src="{src}" srcset="{src} {w}w" sizes="{sizes}" alt="" width="{w}" height="{h}"></button>'
        )
    return "".join(buttons)


def product_card(lang: str, model: str, name_key: str, vendor: str, para: str, specs: list[str], files, alt_list, pid: str, css_class: str, name: str | None = None) -> str:
    u, c = UI[lang], PAGES[lang]
    name = name if name is not None else u[name_key]
    nested = False
    href = here(lang, f"products/{model.lower()}.html", nested)
    main = files[0]
    src = asset(lang, main[0], nested)
    w, h = main[1], main[2]
    thumb_html = thumbs(lang, files, alt_list, nested, model, "48px")
    specs_html = "".join(f"<li>{esc(s)}</li>" for s in specs)
    hidden = esc(f"{model} {name}")
    return f'''          <article class="product-card {css_class}" id="{model.lower()}" data-product-id="{model}">
            <a class="product-card__cover" href="{href}"><span class="visually-hidden">{hidden}</span></a>
            <div class="product-card__art" data-gallery>
              <div class="product-card__photo-wrap">
                <img class="product-card__photo" src="{src}" srcset="{src} {w}w" sizes="(min-width: 1000px) 30vw, (min-width: 640px) 45vw, 92vw" alt="{esc(alt_list[0])}" width="{w}" height="{h}" data-gallery-main>
                <small>{model}</small>
              </div>
              <div class="product-card__thumbs" role="group" aria-label="{esc(c["photos_of"].format(model=model))}">{thumb_html}</div>
            </div>
            <div class="product-card__body">
              <p class="product-card__vendor">{esc(vendor)}</p>
              <h3>{esc(name)}</h3>
              <p class="product-card__model">{model}</p>
              <p>{esc(para)}</p>
              <ul class="product-card__specs">{specs_html}</ul>
              <a class="product-card__action" href="{href}#request-a-quote">{esc(u["req_quote"])} <span aria-hidden="true">→</span></a>
            </div>
          </article>'''


def range_card(lang: str, m: dict, vendor: str, css_class: str) -> str:
    cp = m["copy"][lang]
    return product_card(lang, m["model"], "", vendor, cp["card_p"], cp["card_specs"], m["files"], [cp["alt"]] * len(m["files"]), m["model"], css_class, name=cp["name"])


def build_products(lang: str) -> None:
    c, u = PAGES[lang], UI[lang]
    a = alts(lang)
    contact = here(lang, "contact.html", False)
    scalp_cards = "\n".join(range_card(lang, m, c["vendor_scalp"], "scalp") for m in by_group("scalp"))
    face_cards = "\n".join(range_card(lang, m, c["vendor_face"], "scalp") for m in by_group("face"))
    body = f'''    <section class="page-hero product-hero">
      <div class="container">
        {breadcrumb(lang, False, (None, u["products"]))}
        <div class="eyebrow">{esc(u["range"])}</div>
        <h1>{esc(c["prod_h1"])}</h1>
        <p>{esc(c["prod_lead"])}</p>
        <div class="product-hero__summary" aria-label="{esc(c["prod_groups"])}">
          <span><strong>01</strong> {esc(c["prod_n_beauty"])}</span>
          <span><strong>02</strong> {esc(c["prod_n_face"])}</span>
          <span><strong>03</strong> {esc(c["prod_n_mattress"])}</span>
        </div>
      </div>
    </section>
    <div class="preview-strip"><div class="container"><strong>{esc(c["strip_kicker"])}</strong><i aria-hidden="true"></i><span>{esc(c["prod_strip"])}</span></div></div>
    <section class="product-intro" aria-label="{esc(c["prod_groups"])}">
      <div class="container product-intro__inner">
        <p>{esc(c["prod_intro"])}</p>
        <nav class="category-links" aria-label="{esc(c["prod_groups"])}"><a href="#beauty">{esc(c["cat_beauty"])} <span>01</span></a><a href="#facial">{esc(c["cat_face"])} <span>02</span></a><a href="#mattresses">{esc(c["cat_mattress"])} <span>03</span></a></nav>
      </div>
    </section>
    <section class="product-section" id="beauty" aria-labelledby="beauty-title">
      <div class="container">
        <div class="product-section__heading"><div><div class="eyebrow">{esc(c["sec_beauty_eye"])}</div><h2 id="beauty-title">{esc(c["sec_beauty_h2"])}</h2><p>{esc(c["sec_beauty_p"])}</p></div><span class="product-section__count">{esc(c["sec_beauty_count"])}</span></div>
        <div class="product-grid">
{product_card(lang, "KH-2406", "name_kh2406", c["vendor_scalp"], c["card_kh2406_p"], [c["card_kh2406_s1"], c["card_kh2406_s2"], c["card_kh2406_s3"]], card_files(KH2406, KH2406_CARD), a["kh2406"], "KH-2406", "scalp")}
{product_card(lang, "KH-2307", "name_kh2307", c["vendor_scalp"], c["card_kh2307_p"], [c["card_kh2307_s1"], c["card_kh2307_s2"], c["card_kh2307_s3"], c["card_kh2307_s4"]], card_files(KH2307, KH2307_CARD), a["kh2307"], "KH-2307", "scalp")}
{scalp_cards}
        </div>
      </div>
    </section>
    <section class="product-section" id="facial" aria-labelledby="facial-title">
      <div class="container">
        <div class="product-section__heading"><div><div class="eyebrow">{esc(c["sec_face_eye"])}</div><h2 id="facial-title">{esc(c["sec_face_h2"])}</h2><p>{esc(c["sec_face_p"])}</p></div><span class="product-section__count">{esc(c["sec_face_count"])}</span></div>
        <div class="product-grid">
{face_cards}
        </div>
      </div>
    </section>
    <section class="product-section product-section--tinted" id="mattresses" aria-labelledby="mattress-title">
      <div class="container">
        <div class="product-section__heading"><div><div class="eyebrow">{esc(c["sec_matt_eye"])}</div><h2 id="mattress-title">{esc(c["sec_matt_h2"])}</h2><p>{esc(c["sec_matt_p"])}</p></div><span class="product-section__count">{esc(c["sec_matt_count"])}</span></div>
        <div class="product-grid">
{product_card(lang, "OB-1600", "name_ob1600", c["vendor_care"], c["card_ob1600_p"], [], card_files(OB1600, OB1600_CARD), a["ob1600"], "OB-1600", "care")}
        </div>
      </div>
    </section>
    <section class="product-footnote"><div class="container"><div class="product-footnote__box"><div class="eyebrow">{esc(c["foot_eye"])}</div><h2>{esc(c["foot_h2"])}</h2><p>{esc(c["foot_p"])}</p><a class="text-link" href="{contact}#request-a-quote">{esc(u["req_quote"])} <span aria-hidden="true">→</span></a></div></div></section>
{quote_form(lang)}'''
    write(lang, "products.html", shell(lang, "products.html", c["prod_title"], c["prod_desc"], body, extra_css=True))


def build_contact(lang: str) -> None:
    c, u = PAGES[lang], UI[lang]
    products = here(lang, "products.html", False)
    body = f'''    <section class="page-hero"><div class="container">{breadcrumb(lang, False, (None, u["contact"]))}<h1>{esc(c["contact_h1"])}</h1><p>{esc(c["contact_lead"])}</p></div></section>
    <div class="preview-strip"><div class="container"><strong>{esc(u["contact"])}</strong><i aria-hidden="true"></i><span>{esc(c["contact_strip"])}</span></div></div>
    <section class="section"><div class="container contact-grid"><div class="contact-card dark"><div class="eyebrow light">{esc(c["contact_company_eye"])}</div><h2 class="company-name">{esc(u["footer_brand"])}</h2><p><span class="address-label">{esc(u["addr_mainland"])}</span>{esc(u["mainland"])}</p><p><span class="address-label">{esc(u["addr_holding"])}</span>{esc(u["holding"])}</p></div><div class="contact-card"><div class="eyebrow">{esc(c["contact_write_eye"])}</div><h2>{esc(c["contact_write_h2"])}</h2><div class="contact-facts"><a href="mailto:ohashi@brightbridgegroup.com">ohashi@brightbridgegroup.com</a><a href="tel:+8676989399795">+86 769 8939 9795</a></div><a class="button primary" href="#request-a-quote">{esc(u["req_quote"])} <span aria-hidden="true">↗</span></a></div></div></section>
    <section class="section tinted"><div class="container content-grid"><div><div class="eyebrow">{esc(c["contact_range_eye"])}</div><h2>{esc(c["contact_range_h2"])}</h2></div><div><p>{esc(c["contact_range_p"])}</p><a class="text-link" href="{products}">{esc(c["browse_range"] if "browse_range" in c else u["browse"])} <span aria-hidden="true">→</span></a></div></div></section>
{quote_form(lang)}'''
    write(lang, "contact.html", shell(lang, "contact.html", c["contact_title"], c["contact_desc"], body))


def gallery_block(lang: str, files, alt_list, model: str) -> str:
    c = PAGES[lang]
    main = files[0]
    src = asset(lang, main[0], True)
    w, h = main[1], main[2]
    thumbs_html = thumbs(lang, files, alt_list, True, model, "72px")
    return f'''        <div class="detail-gallery" data-gallery>
          <div class="detail-gallery__stage" tabindex="-1">
            <img class="detail-gallery__main" src="{src}" srcset="{src} {w}w" sizes="(min-width: 1000px) 42vw, min(92vw, 520px)" alt="{esc(alt_list[0])}" width="{w}" height="{h}" data-gallery-main>
            <button class="detail-gallery__nav detail-gallery__nav--prev" type="button" data-gallery-prev aria-label="{esc(c["prev_photo"])}" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button>
            <button class="detail-gallery__nav detail-gallery__nav--next" type="button" data-gallery-next aria-label="{esc(c["next_photo"])}" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>
          </div>
          <div class="detail-gallery__thumbs" role="group" aria-label="{esc(c["photos_of"].format(model=model))}">{thumbs_html}</div>
        </div>'''


def build_detail(lang: str, model: str, files, alt_list, title: str, desc: str, name: str, lead: str, spec_pairs, step_list, note: str, suit_list) -> str:
    c, u = PAGES[lang], UI[lang]
    products = here(lang, "products.html", True)
    filename = f"products/{model.lower()}.html"
    specs = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in spec_pairs)
    steps = "".join(f"<li>{esc(s)}</li>" for s in step_list)
    suit = "".join(f"<li>{esc(s)}</li>" for s in suit_list)
    order = "".join(f"<li>{esc(c[k])}</li>" for k in ("order_1", "order_2", "order_3"))
    body = f'''    <section class="page-hero product-detail-hero">
      <div class="container">
        {breadcrumb(lang, True, (products, u["products"]), (None, model))}
        <div class="eyebrow">{esc(u["range"])}</div>
        <h1>{esc(name)}</h1>
        <p>{esc(lead)}</p>
      </div>
    </section>
    <section class="section product-detail">
      <div class="container detail-layout">
        {gallery_block(lang, files, alt_list, model)}
        <div class="detail-copy">
          <p class="detail-model">{model}</p>
          <div class="detail-block">
            <h2>{esc(c["key_specs"])}</h2>
            <dl class="detail-specs">{specs}</dl>
          </div>
        <div class="detail-block">
          <h2>{esc(c["how_to"])}</h2>
          <ol class="detail-list">{steps}</ol>
          <p class="detail-note">{esc(note)}</p>
        </div>
        <div class="detail-block">
          <h2>{esc(c["suitable"])}</h2>
          <ul class="detail-list">{suit}</ul>
        </div>
        <div class="detail-block">
          <h2>{esc(c["ordering"])}</h2>
          <ul class="detail-list">{order}</ul>
        </div>
        <div class="detail-block">
          <h2>{esc(c["compliance"])}</h2>
          <p>{esc(c["compliance_p"])}</p>
        </div>
        <div class="detail-actions">
          <a class="button primary" href="#request-a-quote" data-quote-open data-product="{model}">{esc(u["req_quote"])}</a>
          <a class="button outline" href="#request-a-quote" data-quote-open data-product="{model}" data-quote-intent="sample">{esc(u["req_sample"])}</a>
        </div>
        </div>
      </div>
    </section>
{quote_form(lang, nested=True, selected=model)}'''
    return shell(lang, filename, title, desc, body, nested=True, extra_css=True, body_attr=f' data-product="{model}"')


def build_details(lang: str) -> None:
    mapping = [
        ("KH-2406", KH2406, "kh2406", "d2406_title", "d2406_desc", "d2406_lead", "d2406_specs", "d2406_steps", "d2406_note", "suit_beauty"),
        ("KH-2307", KH2307, "kh2307", "d2307_title", "d2307_desc", "d2307_lead", "d2307_specs", "d2307_steps", "d2307_note", "suit_beauty"),
        ("OB-1600", OB1600, "ob1600", "d1600_title", "d1600_desc", "d1600_lead", "d1600_specs", "d1600_steps", "d1600_note", "suit_mattress"),
    ]
    c, u = PAGES[lang], UI[lang]
    a = alts(lang)
    name_key = {"KH-2406": "name_kh2406", "KH-2307": "name_kh2307", "OB-1600": "name_ob1600"}
    for model, files, alt_key, title_key, desc_key, lead_key, specs_key, steps_key, note_key, suit_key in mapping:
        html = build_detail(lang, model, files, a[alt_key], c[title_key], c[desc_key], u[name_key[model]], c[lead_key], c[specs_key], c[steps_key], c[note_key], c[suit_key])
        write(lang, f"products/{model.lower()}.html", html, nested=True)
    for m in RANGE_MODELS:
        cp = m["copy"][lang]
        model = m["model"]
        html = build_detail(lang, model, m["files"], [cp["alt"]] * len(m["files"]), f"{model} — AuraBridge", f"{model}: {cp['card_p']} {DESC_SUFFIX[lang]}", cp["name"], cp["card_p"], cp["specs"], cp["steps"], cp["note"], c[m["suit"]])
        write(lang, f"products/{model.lower()}.html", html, nested=True)


def build_legalish(lang: str, kind: str) -> None:
    c, u = PAGES[lang], UI[lang]
    if kind == "legal":
        filename, title, desc, h1, updated, inner = "legal.html", c["legal_title"], c["legal_desc"], c["legal_h1"], c["legal_updated"], legal_body(lang)
        crumb = u["legal"]
    else:
        filename, title, desc, h1, updated, inner = "privacy.html", c["privacy_title"], c["privacy_desc"], c["privacy_h1"], c["privacy_updated"], privacy_body(lang)
        crumb = u["privacy"]
    body = f'''    <section class="page-hero"><div class="container">{breadcrumb(lang, False, (None, crumb))}<h1>{esc(h1)}</h1><p>{esc(updated)}</p></div></section>
    <section class="section"><div class="container legal-prose">{inner}<p class="font-note">{esc(c["font_note"])}</p></div></section>'''
    write(lang, filename, shell(lang, filename, title, desc, body))


def main() -> None:
    for lang in LANGS:
        build_home(lang)
        build_about(lang)
        build_partnerships(lang)
        build_products(lang)
        build_contact(lang)
        build_details(lang)
        build_legalish(lang, "legal")
        build_legalish(lang, "privacy")
        print("built", lang)


if __name__ == "__main__":
    main()
