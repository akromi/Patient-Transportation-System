#!/usr/bin/env python3
"""Render the published study pages to print-ready PDFs.

The docs/*.html files are Artifact *fragments* — they carry a <title>, <style>
and body content, but no document skeleton, because the Artifact runtime supplies
one. This wraps each fragment in a real document, forces the light theme, layers
a print stylesheet over it, and drives headless Chromium to produce a PDF.

Usage:  python3 scripts/build-pdfs.py
Output: pdf/*.pdf
"""
import pathlib, subprocess, shutil, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS, OUT = ROOT / "docs", ROOT / "pdf"

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]

PAGES = [
    ("ontario-transport-gap.html", "ontario-transport-gap.pdf"),
    ("ottawa-business-case.html", "ottawa-business-case.pdf"),
]

PRINT_CSS = """
@page { size: Letter; margin: 15mm 14mm 16mm; }
html, body { background: #fff !important; }
* { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
.wrap { max-width: none !important; padding: 0 !important; }
/* Tables must not be clipped or forced wider than the page */
.tw { overflow: visible !important; border-radius: 0; }
table { min-width: 0 !important; width: 100% !important; font-size: 10.5pt; }
th, td { padding: 7px 9px !important; }
body { font-size: 10.5pt; line-height: 1.5; }
h1 { font-size: 30pt !important; }
h2 { font-size: 17pt !important; }
h3 { font-size: 11.5pt !important; }
.deck { font-size: 12pt !important; }
.stat .v { font-size: 19pt !important; }
/* Keep logical units together */
.block, .callout, .finding, .stat, .surf, .rec, .payer-col, .bar-row, .tw { break-inside: avoid; }
section { break-inside: auto; }
h2, h3, .sec-head { break-after: avoid; }
.mast { break-after: avoid; }
section { padding-top: 22px !important; }
footer { break-before: auto; }
/* Shadows and hovers are noise in print */
.block, .stats, .findings, .surfaces, .tw, .rec { box-shadow: none !important; }
a { text-decoration: none; color: inherit; }
a[href^="http"]::after { content: ""; }
"""

SKELETON = """<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{ color-scheme: light; }}
  body {{ margin: 0; font: 14px system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; background: #fff; }}
  img {{ max-width: 100%; }}
  [hidden] {{ display: none !important; }}
</style>
{fragment}
<style>{print_css}</style>
</head>
<body>{body}</body>
</html>
"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if pathlib.Path(c).exists():
            return c
    for name in ("chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("No Chromium binary found; cannot render PDFs.")


def build(chrome, src_name, out_name):
    src = DOCS / src_name
    raw = src.read_text()
    head, body = raw.split("</style>", 1)
    head += "</style>"
    doc = SKELETON.format(fragment=head, print_css=PRINT_CSS, body=body)

    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "page.html"
        page.write_text(doc)
        out = OUT / out_name
        cmd = [
            chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=15000", f"--print-to-pdf={out}",
            f"--user-data-dir={tmp}/profile", page.as_uri(),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if not out.exists():
            sys.exit(f"Failed to render {out_name}\n{r.stderr[-2000:]}")
        return out


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    chrome = find_chrome()
    print(f"chromium: {chrome}\n")
    for src_name, out_name in PAGES:
        out = build(chrome, src_name, out_name)
        print(f"  {out.relative_to(ROOT)}  {out.stat().st_size/1024:,.0f} KB")
