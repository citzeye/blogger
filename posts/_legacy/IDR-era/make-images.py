#!/usr/bin/env python3
"""
Generate original graphics for the article "5 Phones Worth Buying Under IDR 2 Million".

100% original artwork — no copyrighted product photos.
Palette matches the blog's Aura Dark theme.

Output: images/*.png (3:2 to match the card layout) + *.svg source
"""
import os, subprocess

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

# Aura Dark palette (from citzeyeblogspot.xml)
BG      = "#15141b"
BG_CARD = "#1c1b23"
BG_ELEV = "#211f2b"
FG      = "#edecee"
MUTED   = "#9a95ab"
DIM     = "#6c6785"
PURPLE  = "#a277ff"
PINK    = "#f694ff"
SKY     = "#82aaff"
MINT    = "#61ffca"
PEACH   = "#ffca85"
BORDER  = "#2e2a3d"

# Kode Mono is not installed locally; fall back through available monospace fonts
MONO = "DejaVu Sans Mono,Liberation Mono,Noto Sans Mono,monospace"

PHONES = [
    # name, price_idr, tag, accent, blurb
    ("Redmi Note 14", 1895000, "BEST OVERALL",      PURPLE, "AMOLED 120Hz"),
    ("Galaxy A07",    1899000, "LONGEST SUPPORT",  SKY,    "Software updates"),
    ("Redmi 15",      1749000, "BEST BATTERY",     MINT,   "7,000 mAh"),
    ("Tecno Spark Go 3",1599000,"MOST DURABLE",     PEACH,  "IP64, drop tested"),
    ("Infinix Hot 60i",1499000,"CHEAPEST 120Hz",   PINK,   "Lowest price"),
]

def svg_to_png(svg_path, png_path, width):
    subprocess.run(
        ["rsvg-convert", "-w", str(width), "-o", png_path, svg_path],
        check=True,
    )

def money(v):
    return f"Rp {v:,}".replace(",", ",")

# ---------------------------------------------------------------- 1. FEATURED
def featured():
    W, H = 1600, 1067
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    # background + subtle accent glow
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0%" stop-color="{PURPLE}" stop-opacity=".28"/>'
             f'<stop offset="100%" stop-color="{SKY}" stop-opacity=".05"/>'
             f'</linearGradient></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#g)"/>')
    # grid texture
    for x in range(0, W, 64):
        p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{BG_CARD}" stroke-width="1" opacity=".55"/>')
    for y in range(0, H, 64):
        p.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{BG_CARD}" stroke-width="1" opacity=".55"/>')
    # top accent bar
    p.append(f'<rect x="0" y="0" width="{W}" height="10" fill="{PURPLE}"/>')
    # cursor prompt
    p.append(f'<text x="110" y="330" font-family="{MONO}" font-size="52" font-weight="bold" fill="{MINT}">~/</text>')
    p.append(f'<text x="110" y="330" font-family="{MONO}" font-size="52" fill="none"> </text>')
    # headline
    p.append(f'<text x="110" y="440" font-family="{MONO}" font-size="78" font-weight="bold" fill="{FG}">5 PHONES WORTH</text>')
    p.append(f'<text x="110" y="540" font-family="{MONO}" font-size="78" font-weight="bold" fill="{PURPLE}">BUYING UNDER</text>')
    p.append(f'<text x="110" y="640" font-family="{MONO}" font-size="78" font-weight="bold" fill="{FG}">IDR 2 MILLION</text>')
    # blinking-cursor block after the headline
    p.append(f'<rect x="110" y="676" width="34" height="60" fill="{PINK}"/>')
    # subtitle
    p.append(f'<text x="110" y="790" font-family="{MONO}" font-size="30" fill="{MUTED}">A buying guide that will still be</text>')
    p.append(f'<text x="110" y="836" font-family="{MONO}" font-size="30" fill="{MUTED}">useful long after this page is read.</text>')
    # 5 phone cards along the bottom
    cw, gap, x0, y0 = 244, 28, 110, 900
    for i, (name, price, tag, accent, blurb) in enumerate(PHONES):
        x = x0 + i * (cw + gap)
        p.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="130" rx="6" fill="{BG_CARD}" stroke="{accent}" stroke-width="2"/>')
        p.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="6" fill="{accent}"/>')
        p.append(f'<text x="{x+18}" y="{y0+44}" font-family="{MONO}" font-size="19" font-weight="bold" fill="{accent}">{tag}</text>')
        p.append(f'<text x="{x+18}" y="{y0+80}" font-family="{MONO}" font-size="21" font-weight="bold" fill="{FG}">{money(price)}</text>')
        p.append(f'<text x="{x+18}" y="{y0+108}" font-family="{MONO}" font-size="16" fill="{DIM}">{blurb}</text>')
    p.append('</svg>')
    svg = "\n".join(p)
    sp = os.path.join(OUT, "01-featured.svg")
    open(sp, "w", encoding="utf-8").write(svg)
    svg_to_png(sp, os.path.join(OUT, "01-featured.png"), W)

# ------------------------------------------------------- 2. PRICE COMPARISON
def price_chart():
    W, H = 1400, 933
    lo, hi = 1400000, 1950000
    x0, y0, barw, gap = 430, 140, 92, 42
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect x="60" y="52" width="7" height="52" fill="{PURPLE}"/>',
         f'<text x="88" y="92" font-family="{MONO}" font-size="34" font-weight="bold" fill="{FG}">Price comparison</text>',
         f'<text x="88" y="128" font-family="{MONO}" font-size="19" fill="{DIM}">Street price, checked September 2026</text>']
    for i, (name, price, tag, accent, blurb) in enumerate(PHONES):
        y = y0 + i * (barw + gap)
        frac = (price - lo) / (hi - lo)
        w = 300 + frac * 760
        p.append(f'<text x="410" y="{y+barw*0.62}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="21" font-weight="bold" fill="{FG}">{name}</text>')
        p.append(f'<rect x="{x0}" y="{y}" width="810" height="{barw}" rx="6" fill="{BG_ELEV}"/>')
        p.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="{barw}" rx="6" fill="{accent}" opacity=".9"/>')
        p.append(f'<text x="{x0+w+16:.0f}" y="{y+barw*0.62}" font-family="{MONO}" '
                 f'font-size="21" font-weight="bold" fill="{accent}">{money(price)}</text>')
    p.append(f'<line x1="{x0}" y1="{H-70}" x2="{x0+810}" y2="{H-70}" stroke="{BORDER}" stroke-width="2"/>')
    for v, lb in [(1500000, "1.5M"), (1750000, "1.75M"), (1950000, "1.95M")]:
        fx = (v - lo) / (hi - lo)
        x = x0 + fx * 810
        p.append(f'<text x="{x:.0f}" y="{H-40}" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{DIM}">{lb}</text>')
    p.append(f'<text x="{W-60}" y="{H-40}" text-anchor="end" font-family="{MONO}" font-size="18" fill="{DIM}">IDR</text>')
    p.append('</svg>')
    svg = "\n".join(p)
    sp = os.path.join(OUT, "02-price-comparison.svg")
    open(sp, "w", encoding="utf-8").write(svg)
    svg_to_png(sp, os.path.join(OUT, "02-price-comparison.png"), W)

# ---------------------------------------------------------- 3. WHAT MATTERS
def criteria():
    W, H = 1400, 933
    items = [
        ("01", "RAM over storage", "RAM cannot be added later. 8 GB matters more than 256 GB.", PURPLE),
        ("02", "Battery capacity", "5,000 mAh+ is the norm here. Charging speed is the tiebreaker.", MINT),
        ("03", "Refresh rate", "120 Hz vs 90 Hz is the most visible daily difference.", SKY),
        ("04", "Update support", "The one that decides if the phone is still safe in three years.", PINK),
    ]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect x="60" y="52" width="7" height="52" fill="{MINT}"/>',
         f'<text x="88" y="92" font-family="{MONO}" font-size="34" font-weight="bold" fill="{FG}">What actually matters</text>',
         f'<text x="88" y="128" font-family="{MONO}" font-size="19" fill="{DIM}">Four criteria, in order of impact</text>']
    cw, gap, x0, y0, ch = 315, 25, 60, 180, 660
    for i, (num, title, body, accent) in enumerate(items):
        x = x0 + i * (cw + gap)
        p.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="6" fill="{BG_CARD}" stroke="{BORDER}" stroke-width="2"/>')
        p.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="7" fill="{accent}"/>')
        p.append(f'<text x="{x+28}" y="{y0+95}" font-family="{MONO}" font-size="52" font-weight="bold" fill="{accent}" opacity=".85">{num}</text>')
        # wrap title
        words, line, lines = title.split(), "", []
        for w in words:
            t = (line + " " + w).strip()
            if len(t) > 17:
                lines.append(line); line = w
            else:
                line = t
        lines.append(line)
        for j, ln in enumerate(lines[:2]):
            p.append(f'<text x="{x+28}" y="{y0+185+j*38}" font-family="{MONO}" font-size="22" font-weight="bold" fill="{FG}">{ln}</text>')
        # wrap body
        words, line, lines = body.split(), "", []
        for w in words:
            t = (line + " " + w).strip()
            if len(t) > 26:
                lines.append(line); line = w
            else:
                line = t
        lines.append(line)
        for j, ln in enumerate(lines[:11]):
            p.append(f'<text x="{x+28}" y="{y0+300+j*33}" font-family="{MONO}" font-size="16" fill="{MUTED}">{ln}</text>')
    p.append('</svg>')
    svg = "\n".join(p)
    sp = os.path.join(OUT, "03-what-matters.svg")
    open(sp, "w", encoding="utf-8").write(svg)
    svg_to_png(sp, os.path.join(OUT, "03-what-matters.png"), W)

# --------------------------------------------------------- 4. PICK A PHONE
def decision():
    W, H = 1400, 933
    rows = [
        ("Want the best all-rounder?",      "Redmi Note 14",  PURPLE),
        ("Battery is your top concern?",     "Redmi 15",       MINT),
        ("Keeping the phone for years?",     "Galaxy A07",     SKY),
        ("Work on-site or travel often?",    "Tecno Spark Go 3",PEACH),
        ("Cheapest 120 Hz you can get?",     "Infinix Hot 60i",PINK),
    ]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect x="60" y="52" width="7" height="52" fill="{PINK}"/>',
         f'<text x="88" y="92" font-family="{MONO}" font-size="34" font-weight="bold" fill="{FG}">Start from what you need</text>',
         f'<text x="88" y="128" font-family="{MONO}" font-size="19" fill="{DIM}">Find the requirement, then the phone</text>']
    y0, rh = 175, 122
    for i, (q, a, accent) in enumerate(rows):
        y = y0 + i * (rh + 18)
        p.append(f'<rect x="60" y="{y}" width="{W-120}" height="{rh}" rx="6" fill="{BG_CARD}" stroke="{BORDER}" stroke-width="2"/>')
        p.append(f'<rect x="60" y="{y}" width="7" height="{rh}" fill="{accent}"/>')
        p.append(f'<text x="100" y="{y+68}" font-family="{MONO}" font-size="23" fill="{FG}">{q}</text>')
        # arrow
        p.append(f'<text x="900" y="{y+70}" font-family="{MONO}" font-size="26" fill="{DIM}">&#8594;</text>')
        p.append(f'<text x="952" y="{y+68}" font-family="{MONO}" font-size="23" font-weight="bold" fill="{accent}">{a}</text>')
    p.append('</svg>')
    svg = "\n".join(p)
    sp = os.path.join(OUT, "04-which-one.svg")
    open(sp, "w", encoding="utf-8").write(svg)
    svg_to_png(sp, os.path.join(OUT, "04-which-one.png"), W)

for fn in (featured, price_chart, criteria, decision):
    fn()
    print("  dibuat:", fn.__name__)

print("\n=== HASIL ===")
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(f"  {f:<28} {os.path.getsize(p)//1024:>4} KB")
