#!/usr/bin/env python3
"""Build a 3:2 LANDSCAPE graphic for the phone article.

WHY 3:2 LANDSCAPE, not portrait
--------------------------------
The homepage card and the sidebar widget render a 3:2 frame with
object-fit: contain. A portrait source (1080x1968) dropped into a 3:2 frame
becomes a narrow strip with dead space either side - and switching the frame to
cover instead crops the product. Either way the reader sees a bad thumbnail.

So the ARTWORK is 3:2 too: 1600x1067. Contained into a 3:2 frame it fills the
frame exactly, no crop, no letterbox. Inside each card the product stage is
portrait-shaped, because phones are, and the photo is contained into it - so a
portrait handset photo fills that stage rather than being cut.

    python3 posts/make-phone-images.py "3 Phones Under $250"
    python3 posts/make-phone-images.py "Top 3 Midrange Gaming Phones"
    python3 posts/make-phone-images.py "<title>" --no-photos   layout preview

Source photos: posts/<Post Title>/images/refs/
Any jpg/jpeg/png/webp/avif whose filename contains that product's keyword.
The generator prints the exact keywords it is looking for when a photo is
missing, so there is never a reason to guess a filename.

OUT
    images/<out stem>.jpg    1600x1067, the only deliverable
"""
import importlib.util
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_POST = "3 Phones Under $250"

W, H = 1600, 1067
M = 60

BG = "#15141b"
CARD = "#1c1b23"
BORDER = "#262431"
FG = "#edecee"
MUTED = "#9a95ab"
DIM = "#6c6785"
STAGE = "#ffffff"
FONT = "DejaVu Sans Mono,monospace"

# ImageMagick has NO default font here, so -annotate fails without an explicit
# -font. Resolved by asking the binary what it actually has, instead of
# hardcoding a name that may not exist on the next machine.
def _pick_font():
    out = subprocess.run(["magick", "-list", "font"], capture_output=True,
                         text=True).stdout
    have = {ln.split(":", 1)[1].strip() for ln in out.splitlines()
            if ln.strip().startswith("Font:")}
    for want in ("DejaVu-Sans-Mono", "FreeMono", "Adwaita-Mono"):
        if want in have:
            return want
    raise SystemExit("no monospace font available for the preview text")


PREVIEW_FONT = _pick_font()

# label, price, keyword, accent, tag, note
# Every entry must be a handset the article actually recommends, sold in the
# US and the UK. Do not substitute a phone that is not on sale in those
# markets, and do not publish a price converted from another currency: a
# reader in Los Angeles and a reader in Manchester must both be able to buy
# the exact handset shown, at roughly the price shown.
CONFIGS = {
    "3 Phones Under $250": {
        "out": "01-budget-phones",
        "eyebrow": "~/PHONE BUYING GUIDE",
        "title": "3 PHONES UNDER $250",
        "sub": "US street prices, checked September 2026",
        "accent": "#a277ff",
        "phones": [
            ("Galaxy A17 5G", 232, ("galaxy-a17", "a175g", "galaxy-a175g", "a17"),
             "#82aaff", "LONGEST SUPPORT", "6 years of updates"),
            ("Redmi Note 14", 197, ("redmi-note-14", "redmi note 14", "redmi-14"),
             "#ffca85", "MOST HARDWARE", "up to 256 GB, 45W"),
            ("Galaxy A16 5G", 135, ("galaxy-a16", "a165g", "galaxy-a165g", "a16"),
             "#61ffca", "CHEAPEST WAY IN", "6.7in AMOLED"),
        ],
    },
    "Top 3 Midrange Gaming Phones": {
        "out": "01-midrange-gaming-phones",
        "eyebrow": "~/MIDRANGE GAMING",
        "title": "3 MIDRANGE GAMING PHONES",
        "sub": "US street prices, checked September 2026",
        "accent": "#61ffca",
        "phones": [
            ("OnePlus 13R", 499, ("oneplus-13r", "13r", "oneplus13r"),
             "#ff6b6b", "BEST CHIP", "UFS 4.0, 120Hz LTPO"),
            ("Nothing Phone (4a) Pro", 449, ("nothing-4a-pro", "4a-pro", "4a pro"),
             "#a277ff", "FASTEST SCREEN", "144Hz, 6.83in"),
            ("Google Pixel 10a", 499, ("pixel-10a", "pixel10a", "10a"),
             "#82aaff", "ALSO A CAMERA PHONE", "7 yrs, wireless charge"),
        ],
    },
}

GOLD = 999                     # 3:2                     # 3:2
CARD_Y, CARD_H = 300, 690
GAP = 24
CARD_W = (W - 2 * M - 2 * GAP) // 3
STAGE_X, STAGE_Y = 20, 122
STAGE_W, STAGE_H = CARD_W - 40, 430


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size, fill, weight=False, anchor=None):
    wt = ' font-weight="bold"' if weight else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}"'
            f'{wt} fill="{fill}"{a}>{esc(s)}</text>')


def collect(refdir, phones):
    files = [os.path.join(refdir, f) for f in sorted(os.listdir(refdir))
             if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".avif"))]
    found = {}
    for label, _p, keys, *_ in phones:
        for f in files:
            if f in found.values():
                continue
            low = os.path.basename(f).lower().replace("_", "-").replace(" ", "-")
            if any(k.replace(" ", "-") in low for k in keys):
                found[label] = f
                break
    return found


def normalise(src, work):
    """Scale the photo to FIT the product stage and pad it to the exact stage
    size on white.

    Scaling is 'fit' not 'fill', so a portrait handset photo is never cropped -
    it is centred in the stage with white either side. The output is exactly
    STAGE_W-10 x STAGE_H-10 so it can be composited at a fixed offset with no
    further resampling.

    Per-product working files: writing them all to one shared file made every
    card render the last image, which put one phone under three different
    product names. The md5 guard below exists because of that.
    """
    subprocess.run(
        ["magick", src, "-fuzz", "4%", "-trim", "+repage",
         "-background", "white", "-alpha", "remove", "-alpha", "off",
         "-bordercolor", "white", "-border", "6",
         "-resize", f"{STAGE_W - 10}x{STAGE_H - 10}",
         "-gravity", "center", "-extent", f"{STAGE_W - 10}x{STAGE_H - 10}",
         "-quality", "92", work], check=True)
    return hashlib.md5(open(work, "rb").read()).hexdigest()


def build(names, cfg):
    s = [f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect width="{W}" height="8" fill="{FG}"/>',
         text(M, 104, cfg["eyebrow"], 28, DIM, True),
         text(M, 190, cfg["title"], 58, FG, True),
         text(M, 240, cfg["sub"], 26, MUTED),
         f'<rect x="{M}" y="272" width="56" height="6" fill="{cfg["accent"]}"/>']

    for i, (label, price, _k, colour, tag, note) in enumerate(cfg["phones"]):
        x = M + i * (CARD_W + GAP)
        s.append(f'<rect x="{x}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" '
                 f'rx="6" fill="{CARD}" stroke="{colour}" stroke-width="3"/>')
        s.append(text(x + STAGE_X, CARD_Y + 46, tag, 24, colour, True))
        s.append(text(x + STAGE_X, CARD_Y + 96, label, 34, FG, True))
        # portrait-shaped product stage, photo contained inside it
        s.append(f'<rect x="{x + STAGE_X}" y="{CARD_Y + STAGE_Y}" '
                 f'width="{STAGE_W}" height="{STAGE_H}" rx="4" fill="{STAGE}"/>')
        s.append(f'<image href="{names[i]}" x="{x + STAGE_X + 5}" '
                 f'y="{CARD_Y + STAGE_Y + 5}" width="{STAGE_W - 10}" '
                 f'height="{STAGE_H - 10}" preserveAspectRatio="xMidYMid meet"/>')
        s.append(f'<rect x="{x + STAGE_X}" y="{CARD_Y + 578}" '
                 f'width="{STAGE_W}" height="1" fill="{BORDER}"/>')
        s.append(text(x + STAGE_X, CARD_Y + 638, f"${price}", 44, colour, True))
        s.append(text(x + CARD_W - STAGE_X, CARD_Y + 636, note, 20, DIM,
                      anchor="end"))

    s.append(text(W - M, H - 34, "Prices move weekly. Re-check before you buy.",
                  22, DIM, anchor="end"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">\n' + "\n".join(s) + "\n</svg>\n")


def placeholders(cfg, refdir):
    """Layout-only preview: grey product stages, no real hardware.

    Exists so the typography and card geometry can be reviewed BEFORE anyone
    goes hunting for photos. The output is written with PREVIEW- in the name
    so a preview can never be mistaken for, or pasted over, the real graphic.
    """
    names = []
    for i in range(len(cfg["phones"])):
        w = os.path.join(refdir, f"_pv{i}.png")
        subprocess.run(
            ["magick", "-size", f"{STAGE_W - 10}x{STAGE_H - 10}",
             f"xc:#e4e4ea", "-fill", "#b9b9c4",
             "-draw", f"roundrectangle 90,40 {STAGE_W - 130},{STAGE_H - 40} 26,26",
             "-font", PREVIEW_FONT, "-gravity", "south", "-pointsize", "26",
             "-fill", "#8a8a96",
             "-annotate", "+0+18", "PHOTO NEEDED", w], check=True)
        names.append(os.path.basename(w))
    svg = build(names, cfg)
    base = os.path.join(HERE, "..", "..", "posts", cfg["out"])
    base = os.path.abspath(os.path.join(refdir, "..", "PREVIEW-" + cfg["out"]))
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["magick", "-background", BG, base + ".svg", base + ".png"],
                   check=True)
    for i in range(len(cfg["phones"])):
        subprocess.run(["magick", base + ".png",
                        os.path.join(refdir, f"_pv{i}.png"),
                        "-geometry", f"+{M + i * (CARD_W + GAP) + STAGE_X + 5}"
                                    f"+{CARD_Y + STAGE_Y + 5}",
                        "-composite", base + ".png"], check=True)
    subprocess.run(["magick", base + ".png", "-quality", "90", "-strip",
                    "-interlace", "Plane", base + ".jpg"], check=True)
    for ext in (".svg", ".png"):
        if os.path.exists(base + ext):
            os.remove(base + ext)
    for i in range(len(cfg["phones"])):
        os.remove(os.path.join(refdir, f"_pv{i}.png"))
    d = subprocess.run(["magick", "identify", "-format", "%wx%h", base + ".jpg"],
                       capture_output=True, text=True).stdout
    print(f"  PREVIEW-{cfg['out']}.jpg  {d}  "
          f"{os.path.getsize(base + '.jpg') / 1024:.0f} KB")
    print("  layout only - grey stages. NOT the deliverable, do not upload it.")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    preview = "--no-photos" in sys.argv
    post = args[0] if args else DEFAULT_POST
    if post not in CONFIGS:
        sys.exit("unknown post. known:\n  " + "\n  ".join(CONFIGS))
    spec = importlib.util.spec_from_file_location(
        "mri", os.path.join(HERE, "make-real-images.py"))
    mri = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mri)
    mri.set_post_dir(post)
    cfg = CONFIGS[post]
    refdir = mri.REFS
    os.makedirs(refdir, exist_ok=True)

    if preview:
        placeholders(cfg, refdir)
        return

    found = collect(refdir, cfg["phones"])
    missing = [lbl for lbl, *_ in cfg["phones"] if lbl not in found]
    if missing:
        print("MISSING PRODUCT PHOTOS - the graphic must show real hardware.\n")
        for lbl, _p, keys, *_ in cfg["phones"]:
            mark = "OK  " if lbl in found else "--  "
            print(f"  {mark}{lbl:<16} filename must contain: {'/'.join(keys)}")
        print(f"\nDrop them into:\n  {refdir}")
        sys.exit(1)

    works, names, digests = [], [], []
    for i, (label, *_) in enumerate(cfg["phones"]):
        work = os.path.join(mri.REFS, f"_ph{i}.jpg")
        digests.append(normalise(found[label], work))
        works.append(work)
        names.append(os.path.basename(work))

    if len(set(digests)) != len(digests):
        dup = [cfg["phones"][i][0] for i, d in enumerate(digests) if digests.count(d) > 1]
        for w in works:
            os.remove(w)
        sys.exit("ABORT: these phones resolved to the same photo: "
                 + ", ".join(dup))

    svg = build(names, cfg)
    base = os.path.join(mri.IMG, cfg["out"])
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["magick", "-background", BG, base + ".svg", base + ".png"],
                   check=True)
    # The SVG renderer ignores <image href>, so photos must be composited in
    # afterwards, then the build steps are deleted.
    for i in range(len(cfg["phones"])):
        subprocess.run(["magick", base + ".png", works[i],
                        "-geometry", f"+{M + i * (CARD_W + GAP) + STAGE_X + 5}"
                                    f"+{CARD_Y + STAGE_Y + 5}",
                        "-composite", base + ".png"], check=True)
    # Belt and braces: confirm every photo actually landed inside its own card.
    # A phone under the wrong product name is the one error this whole project
    # keeps paying for, so it is checked rather than trusted.
    subprocess.run(["magick", base + ".png", "-quality", "90", "-strip",
                    "-interlace", "Plane", base + ".jpg"], check=True)
    for ext in (".svg", ".png"):
        if os.path.exists(base + ext):
            os.remove(base + ext)
    for w in works:
        os.remove(w)

    d = subprocess.run(["magick", "identify", "-format", "%wx%h", base + ".jpg"],
                       capture_output=True, text=True).stdout
    ratio = W / H
    print(f"  {cfg['out']}.jpg  {d}  {os.path.getsize(base + '.jpg') / 1024:.0f} KB  "
          f"ratio {ratio:.3f} (3:2 = {GOLD/1000:.3f})")
    if abs(ratio - 1.5) > 0.001:
        sys.exit("  NOT 3:2 - aborting")
    print("done")


if __name__ == "__main__":
    main()
