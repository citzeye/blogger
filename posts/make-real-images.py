#!/usr/bin/env python3
"""Build the article graphics, mobile-first.

DESIGN CONSTRAINT THAT DRIVES EVERYTHING HERE
--------------------------------------------
The reader is on a ~375px-wide phone. An image N px wide renders its text at
    rendered_px = font_px * 375 / N
For text to stay >= 12 CSS px on a phone, at N=1080 the font must be >= 34px.
The previous 1600x-wide landscape layouts used 15-25px labels, which rendered at
3-5px on a phone: unreadable, and pinch-zoom did not rescue it because the
problem was type size in the artwork, not pixel density.

So: portrait canvases (taller on screen for the same width), few columns, and
every label >= 34px with the important ones at 44-68px.

ImageMagick's built-in SVG renderer IGNORES <image href>, so the text/shape layer
is rendered to PNG and the real product photos are composited on top.

Run:  python3 make-real-images.py
Out:  images/01-featured.{svg,png,webp}
      images/02-price-ladder.{svg,png,webp}
      images/03-which-one.{svg,png,webp}
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))   # posts/ - shared tooling root
POSTS = HERE

# One folder per post, named after the post title:
#   posts/<Post Title>/index.html
#   posts/<Post Title>/images/<composites>
#   posts/<Post Title>/images/refs/<product photos>
# The two globals below are repointed per post by set_post_dir().
IMG = os.path.join(POSTS, "images")
REFS = os.path.join(IMG, "refs")


def set_post_dir(name):
    """Point IMG/REFS at posts/<name>. Returns the post directory."""
    global IMG, REFS
    d = os.path.join(POSTS, name)
    if not os.path.isdir(d):
        have = sorted(p for p in os.listdir(POSTS)
                      if os.path.isdir(os.path.join(POSTS, p)))
        raise SystemExit(
            f"No such post folder: {d}\nPost folders available:\n  "
            + "\n  ".join(have))
    IMG = os.path.join(d, "images")
    REFS = os.path.join(IMG, "refs")
    os.makedirs(IMG, exist_ok=True)
    return d


def list_posts():
    """Post folders only: a subdirectory that actually contains an index.html."""
    return sorted(
        p for p in os.listdir(POSTS)
        if os.path.isdir(os.path.join(POSTS, p))
        and not p.startswith((".", "_"))
        and os.path.isfile(os.path.join(POSTS, p, "index.html")))


W = 1080                      # portrait-ish: tall on a phone for its width
M = 56

BG = "#15141b"
CARD = "#1c1b23"
BORDER = "#262431"
FG = "#edecee"
MUTED = "#9a95ab"
DIM = "#6c6785"
ACCENT = "#a277ff"
SOFT = "#f694ff"
SKY = "#82aaff"
SUCCESS = "#61ffca"
WARN = "#ffca85"
STAGE = "#ffffff"

FONT = "DejaVu Sans Mono,monospace"

# Minimum sizes. Do not lower these without re-checking the render on a phone.
FS_EYEBROW = 30
FS_TITLE = 64
FS_SUB = 30
FS_NAME = 46          # renders ~16px on a 375px phone
FS_PRICE = 42
FS_TAG = 30
FS_SMALL = 30

# name, price USD, photo, colour, tag
PHONES = [
    ("Redmi Note 14",   185, "redmi-note-14.jpg",             ACCENT,  "BEST OVERALL"),
    ("Galaxy A07",      180, "samsung-galaxy-a07-tight.jpg",  SKY,     "LONGEST SUPPORT"),
    ("Redmi 15",        165, "redmi-15.jpg",                  SUCCESS, "BIGGEST BATTERY"),
    ("Spark Go 3",      140, "tecno-spark-go-3.jpg",          SOFT,    "MOST DURABLE"),
    ("Infinix Hot 60i", 130, "infinix-hot-60i.jpg",           WARN,    "CHEAPEST 120 HZ"),
]
MAXP = max(p[1] for p in PHONES)


def usd(n):
    return "$" + str(n)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def width_of(text, size):
    """DejaVu Sans Mono advance width is 0.602em."""
    return len(text) * 0.602 * size


class Canvas:
    def __init__(self, height):
        self.h = height
        self.svg = [
            f'<rect width="{W}" height="{height}" fill="{BG}"/>',
            f'<rect width="{W}" height="8" fill="{FG}"/>',
        ]
        self.photos = []

    def rect(self, x, y, w, h, fill, rx=6, stroke=None, sw=0):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                        f'fill="{fill}"{st}/>')

    def text(self, x, y, s, size, fill, weight=None, anchor=None):
        a = f' text-anchor="{anchor}"' if anchor else ""
        wt = ' font-weight="bold"' if weight else ""
        self.svg.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}"'
                        f'{wt} fill="{fill}"{a}>{esc(s)}</text>')

    def photo(self, ref, x, y, w, h, pad=8):
        p = os.path.join(REFS, ref)
        if not os.path.exists(p):
            raise SystemExit(f"missing product photo: {p}")
        self.rect(x, y, w, h, STAGE, rx=4)
        self.photos.append((ref, x + pad, y + pad, w - 2 * pad, h - 2 * pad))

    def header(self, eyebrow, lines, subtitle):
        self.text(M, 88, eyebrow, FS_EYEBROW, DIM, weight=True)
        y = 176
        for ln in lines:
            self.text(M, y, ln, FS_TITLE, FG, weight=True)
            y += int(FS_TITLE * 1.2)
        self.text(M, y + 24, subtitle, FS_SUB, MUTED)
        y += 58
        self.rect(M, y, 60, 6, ACCENT, rx=0)
        return y + 42

    def dump(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{self.h}" '
                f'viewBox="0 0 {W} {self.h}">\n' + "\n".join(self.svg) + "\n</svg>\n")


def render(stem, c, keep_intermediate=False):
    """Write the JPEG deliverable - one format only.

    JPEG because that is what Blogger serves anyway: it re-encodes every upload
    to JPEG, so shipping a WebP only meant paying for the conversion twice.
    Emitting JPEG directly makes the local file byte-for-byte the thing the
    reader downloads.

    The SVG and PNG layers are build steps, not deliverables. The .svg in
    particular must never be uploaded: ImageMagick's SVG renderer ignores
    <image href>, so it carries the text and boxes but zero product photos.
    Pass keep_intermediate=True to keep both when debugging a layout."""
    base = os.path.join(IMG, stem)
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(c.dump())
    subprocess.run(["magick", "-background", BG, base + ".svg", base + ".png"], check=True)
    with tempfile.TemporaryDirectory() as td:
        for i, (ref, x, y, w, h) in enumerate(c.photos):
            fitted = os.path.join(td, f"p{i}.png")
            subprocess.run(
                ["magick", os.path.join(REFS, ref), "-resize", f"{w}x{h}",
                 "-background", STAGE, "-gravity", "center", "-extent", f"{w}x{h}", fitted],
                check=True)
            subprocess.run(["magick", base + ".png", fitted, "-geometry", f"+{x}+{y}",
                            "-composite", base + ".png"], check=True)
    # q90 keeps the small type crisp; q88 was visibly soft on the 27-30px labels.
    subprocess.run(["magick", base + ".png", "-quality", "90", "-strip",
                    "-interlace", "Plane", base + ".jpg"], check=True)
    if not keep_intermediate:
        for ext in ("svg", "png", "webp"):
            if os.path.exists(f"{base}.{ext}"):
                os.remove(f"{base}.{ext}")
    out = []
    for ext in ("svg", "png", "webp", "jpg"):
        if ext != "jpg" and not os.path.exists(f"{base}.{ext}"):
            continue
        kb = os.path.getsize(f"{base}.{ext}") / 1024
        if ext == "svg":
            out.append(f"{stem}.svg {kb:.0f}KB")
        else:
            d = subprocess.run(["magick", "identify", "-format", "%wx%h", f"{base}.{ext}"],
                               capture_output=True, text=True).stdout
            out.append(f"{stem}.{ext} {d} {kb:.0f}KB")
    print("  " + " | ".join(out))


# ----------------------------------------------------------------- 01 featured
def build_featured():
    ch, gap = 292, 22
    probe = Canvas(10)
    y0 = probe.header("~/PHONE BUYING GUIDE",
                      ["5 PHONES UNDER", "$200"],
                      "US street prices, checked Sept 2026")
    h = y0 + 5 * ch + 4 * gap + 110
    c = Canvas(h)
    y = c.header("~/PHONE BUYING GUIDE",
                 ["5 PHONES UNDER", "$200"],
                 "US street prices, checked Sept 2026")
    cw = W - 2 * M
    ph = ch - 96
    for name, price, ref, col, tag in PHONES:
        c.rect(M, y, cw, ch, CARD, stroke=col, sw=3)
        c.photo(ref, M + 8, y + 8, 200, ph)
        tx = M + 8 + 200 + 28
        c.text(tx, y + 96, name, FS_NAME, FG, weight=True)
        c.text(tx, y + 156, usd(price), FS_PRICE, col, weight=True)
        c.text(tx, y + 214, tag, FS_TAG, DIM)
        y += ch + gap
    c.text(W - M, y + 44, "All five shown", FS_SMALL, DIM, anchor="end")
    return c


# ------------------------------------------------------------- 02 price ladder
def build_price_ladder():
    rh, gap = 200, 18
    probe = Canvas(10)
    y0 = probe.header("~/PRICE LADDER", ["EVERY PICK,", "SORTED BY PRICE"],
                      "What $200 and under actually gets you")
    h = y0 + 5 * rh + 4 * gap + 110
    c = Canvas(h)
    y = c.header("~/PRICE LADDER", ["EVERY PICK,", "SORTED BY PRICE"],
                 "What $200 and under actually gets you")
    cw = W - 2 * M
    bar_x, bar_w = M + 28, cw - 300
    for name, price, ref, col, tag in PHONES:
        c.rect(M, y, cw, rh, CARD)
        c.photo(ref, M + 10, y + 10, 180, rh - 20, pad=0)
        c.text(M + 216, y + 92, name, FS_NAME, FG, weight=True)
        c.text(W - M - 24, y + 92, usd(price), FS_PRICE, col, weight=True, anchor="end")
        c.rect(bar_x, y + 136, bar_w, 14, BORDER, rx=7)
        c.rect(bar_x, y + 136, round(bar_w * price / MAXP), 14, col, rx=7)
        y += rh + gap
    c.text(M, y + 44, "Bar length = street price. Re-check before you buy.",
           FS_SMALL, DIM)
    return c


# --------------------------------------------------------------- 03 which one
PANELS = [
    ("BEST BALANCE",    "Default buy. Stops the search."),
    ("6 YRS UPDATES",   "Current for the longest."),
    ("7,000 mAh BATTERY", "Fewest charges per week."),
    ("IP54 + TOUGH",    "For crews and field work."),
    ("120 Hz CHEAPEST", "Smooth screen, lowest price."),
]


def build_which_one():
    ch, gap = 300, 22
    probe = Canvas(10)
    y0 = probe.header("~/WHICH ONE", ["PICK BY", "PRIORITY"],
                      "Five phones, five reasons")
    h = y0 + 5 * ch + 4 * gap + 110
    c = Canvas(h)
    y = c.header("~/WHICH ONE", ["PICK BY", "PRIORITY"], "Five phones, five reasons")
    cw = W - 2 * M
    for i, (name, price, ref, col, tag) in enumerate(PHONES):
        kicker, blurb = PANELS[i]
        c.rect(M, y, cw, ch, CARD, stroke=col, sw=3)
        c.photo(ref, M + 8, y + 8, 190, ch - 96)
        tx = M + 8 + 190 + 28
        c.text(tx, y + 84, kicker, FS_TAG, col, weight=True)
        c.text(tx, y + 148, name, FS_NAME, FG, weight=True)
        c.text(tx, y + 206, blurb, FS_SMALL, MUTED)
        y += ch + gap
    c.text(M, y + 44, "Prices checked September 2026", FS_SMALL, DIM)
    return c


if __name__ == "__main__":
    # usage: make-real-images.py "<Post Title folder>"
    target = sys.argv[1] if len(sys.argv) > 1 else "3 Phones Under $250"
    d = set_post_dir(target)
    print(f"post folder: {os.path.basename(d)}")
    for stem, fn in (("01-featured", build_featured),
                     ("02-price-ladder", build_price_ladder),
                     ("03-which-one", build_which_one)):
        render(stem, fn())
    print("done")
