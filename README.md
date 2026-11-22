# AuraBridge website

A static B2B website for AuraBridge, a brand of Hong Kong Bright Bridge Group Co., Limited. It introduces the company and shows three products in the range: two scalp-care devices (KH-2406 and KH-2307) and one alternating-pressure air mattress (OB-1600).

**View the website:** https://ekoh1230.github.io/aurabridge-website/

## View locally

Open `index.html` in a browser, or serve the folder with any static file server. The site uses plain HTML, CSS, and a small JavaScript file, with no build step required to view it. To regenerate pages after editing copy, run `python3 scripts/build_pages.py`.

## Pages

- `index.html` — home
- `products.html` — the three models, with scalp-care devices first and the air mattress last
- `about.html` — what AuraBridge does
- `partnerships.html` — how a wholesale conversation can start
- `contact.html` — addresses, email, phone, and the quote form
- `legal.html` — legal notice
- `privacy.html` — privacy policy
- `products/kh-2406.html`, `products/kh-2307.html`, `products/ob-1600.html` — product detail pages

English is at the site root. Simplified Chinese, French, German, and Spanish copies are under `zh/`, `fr/`, `de/`, and `es/`. Shared assets live in `assets/`. The header mark is `assets/aurabridge-logo.png`, the original bridge drawing with heavier strokes.

## Fonts

Headings use Source Serif 4 and body text uses Source Sans 3, both designed by Adobe and licensed under the SIL Open Font License, Version 1.1. The font files are hosted in `assets/fonts/`; licence texts are in those folders. The site does not load fonts from a third-party CDN.

## Privacy and forms

The site does not set cookies, does not use local storage, and does not load analytics or other third-party scripts. The quote form opens the visitor’s email application with a pre-filled message to ohashi@brightbridgegroup.com (copy to ikkei@brightbridgegroup.com). Nothing is stored on the website itself. See `privacy.html`.

Prices, certification marks, and treatment claims are not shown. No payment or account system is connected.

Publishing this repository with GitHub Pages makes the site publicly accessible to anyone with the URL. Keep internal source documents out of this repository.
