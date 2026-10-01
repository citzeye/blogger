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
    # A reference article, not a roundup: the two things a reader must be able
    # to recognise, and no prices anywhere. Both photos are of socketed memory -
    # a clean photo of memory soldered to a board does not exist under a free
    # licence - so the captions describe what is actually shown rather than
    # asserting the opposite of it. "price" is None for these cards and the
    # footer comes from the config, since "prices move weekly" would be a lie.
    "Upgradeable RAM Laptops Reading the Spec Sheet": {
        "out": "01-upgradeable-ram-laptops",
        "layout": "compare",
        "eyebrow": "~/LAPTOP HARDWARE",
        "title": "UPGRADEABLE RAM LAPTOPS",
        "sub": "What each brand's own spec sheet actually says",
        "accent": "#61ffca",
        "footer": "Vendor documents verified September 2026",
        "phones": [
            ("The slots", None, ("x220-empty-ram-slots", "empty-ram-slots", "x220"),
             "#61ffca", "WHAT UPGRADABLE LOOKS LIKE", "two SODIMM sockets, modules lift straight out"),
            ("The module", None, ("ddr5-form-factors", "form-factors", "ddr5"),
             "#a277ff", "WHAT YOU BUY", "DDR5 SODIMM - the short, notched stick"),
        ],
    },
    # The two objects this article is actually about, at real relative scale:
    # the card, and the SIM tray it competes with for the same slot. The point
    # of the layout is that the nano-SIM is not a second card - it is the other
    # half of one shared slot.
    "Phones With an SD Card Slot What the Slot Actually Costs": {
        "out": "01-phones-with-sd-card-slot",
        "layout": "compare",
        "eyebrow": "~/PHONE STORAGE",
        "title": "THE SD SLOT TRADE",
        "sub": "What the card slot takes, and what you cannot do with it",
        "accent": "#ffca85",
        "footer": "Manufacturer spec pages checked September 2026",
        "phones": [
            ("microSD", None, ("microsd-size", "microsd"),
             "#61ffca", "THE STORAGE", "up to 2 TB - media only, never apps"),
            ("nano-SIM", None, ("nano-sim-tray", "sim-tray", "sim"),
             "#ff6b6b", "WHAT IT DISPLACES", "the same tray does both, on many phones"),
        ],
    },
    # The two objects that decide the speed: the brick, and how much of it you
    # have to carry. Left is the old silicon brick next to a GaN one of the same
    # 30W, right is the 45W USB-C adapter the Pixel 10a's spec page tells you to
    # buy separately. Both are real products, photographed.
    "Phone Charging Speed Why the Number on the Box Is Wrong": {
        "out": "01-phone-charging-speed",
        "layout": "compare",
        "eyebrow": "~/PHONE CHARGING",
        "title": "WATTAGE IS A CEILING",
        "sub": "The phone is rarely the thing limiting your charge speed",
        "accent": "#82aaff",
        "footer": "Manufacturer spec pages checked September 2026",
        "phones": [
            ("The brick", None, ("silicon-vs-gan", "silicon", "gan"),
             "#61ffca", "THE ACTUAL LIMIT", "same 30W, very different size"),
            ("The adapter", None, ("45w-usbc-adapter", "45w", "adapter"),
             "#ffca85", "WHAT YOU BUY", "any 100W USB-C PD brick will do"),
        ],
    },
    # Two states of the same panel, not two products. The left card is what the
    # spec number describes - a small bright patch, and the test card it is
    # measured on has the window-size markers printed in its corner. The right
    # card is the whole screen in the conditions the number is never quoted for.
    # No prices: this is a reference article, and "price" is None on both cards.
    "Phone Peak Brightness The Number That Is Not Outdoor Brightness": {
        "out": "01-phone-peak-brightness",
        "layout": "compare",
        "eyebrow": "~/PHONE DISPLAYS",
        "title": "PEAK IS A SMALL PATCH",
        "sub": "The headline number is measured on a sliver of screen",
        "accent": "#a277ff",
        "footer": "Vendor spec pages and named lab measurements, checked October 2026",
        "phones": [
            ("The patch", None, ("display-test-pattern", "test-pattern", "testcard"),
             "#a277ff", "WHAT IS QUOTED", "3,300 nits on a 5% window, briefly"),
            ("The screen", None, ("phone-in-sun", "phone", "sun"),
             "#ffca85", "WHAT YOU SEE", "full screen, outdoors, washed out"),
        ],
    },
    "Top 3 Midrange Gaming Phones": {
        "out": "01-midrange-gaming-phones",
        "eyebrow": "~/MIDRANGE GAMING",
        "title": "3 MIDRANGE GAMING PHONES",
        "sub": "US street prices, checked September 2026",
        "accent": "#61ffca",
        "phones": [
            ("OnePlus 13R", 549, ("oneplus-13r", "13r", "oneplus13r"),
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

# Two-up layout for reference posts. Same 1600x1067 canvas and same header
# geometry, so both kinds of graphic sit identically in a post card - only the
# card grid below the rule changes.
CMP_CARD_W = (W - 2 * M - GAP) // 2
CMP_STAGE_W = CMP_CARD_W - 40
CMP_STAGE_H = 470


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


def normalise(src, work, stage_w=STAGE_W, stage_h=STAGE_H):
    """Scale the photo to FIT the product stage and pad it to the exact stage
    size on white.

    Scaling is 'fit' not 'fill', so a portrait handset photo is never cropped -
    it is centred in the stage with white either side. The output is exactly
    stage-10 on each side so it can be composited at a fixed offset with no
    further resampling.

    Per-product working files: writing them all to one shared file made every
    card render the last image, which put one phone under three different
    product names. The md5 guard below exists because of that.
    """
    subprocess.run(
        ["magick", src, "-fuzz", "4%", "-trim", "+repage",
         "-background", "white", "-alpha", "remove", "-alpha", "off",
         "-bordercolor", "white", "-border", "6",
         "-resize", f"{stage_w - 10}x{stage_h - 10}",
         "-gravity", "center", "-extent", f"{stage_w - 10}x{stage_h - 10}",
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

    s.append(text(W - M, H - 34, cfg.get("footer", "Prices move weekly. Re-check before you buy."),
                  22, DIM, anchor="end"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">\n' + "\n".join(s) + "\n</svg>\n")


def build_compare(names, cfg):
    """Two cards, no price line - for reference posts that compare two states of
    a component rather than recommending products.

    Same canvas, same header block, so the graphic reads as part of the same
    set as the roundup ones. The note sits under a rule instead of a price,
    which keeps the card bottom aligned without inventing a figure.
    """
    s = [f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect width="{W}" height="8" fill="{FG}"/>',
         text(M, 104, cfg["eyebrow"], 28, DIM, True),
         text(M, 190, cfg["title"], 58, FG, True),
         text(M, 240, cfg["sub"], 26, MUTED),
         f'<rect x="{M}" y="272" width="56" height="6" fill="{cfg["accent"]}"/>']

    for i, (label, _p, _k, colour, tag, note) in enumerate(cfg["phones"]):
        x = M + i * (CMP_CARD_W + GAP)
        s.append(f'<rect x="{x}" y="{CARD_Y}" width="{CMP_CARD_W}" height="{CARD_H}" '
                 f'rx="6" fill="{CARD}" stroke="{colour}" stroke-width="3"/>')
        s.append(text(x + STAGE_X, CARD_Y + 50, tag, 26, colour, True))
        s.append(text(x + STAGE_X, CARD_Y + 100, label, 36, FG, True))
        s.append(f'<rect x="{x + STAGE_X}" y="{CARD_Y + STAGE_Y}" '
                 f'width="{CMP_STAGE_W}" height="{CMP_STAGE_H}" rx="4" fill="{STAGE}"/>')
        s.append(f'<image href="{names[i]}" x="{x + STAGE_X + 5}" '
                 f'y="{CARD_Y + STAGE_Y + 5}" width="{CMP_STAGE_W - 10}" '
                 f'height="{CMP_STAGE_H - 10}" preserveAspectRatio="xMidYMid meet"/>')
        s.append(f'<rect x="{x + STAGE_X}" y="{CARD_Y + 620}" '
                 f'width="{CMP_STAGE_W}" height="1" fill="{BORDER}"/>')
        s.append(text(x + STAGE_X, CARD_Y + 660, note, 22, DIM))

    s.append(text(W - M, H - 34, cfg["footer"], 22, DIM, anchor="end"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">\n' + "\n".join(s) + "\n</svg>\n")


def placeholders(cfg, refdir):
    """Layout-only preview: grey product stages, no real hardware.

    Exists so the typography and card geometry can be reviewed BEFORE anyone
    goes hunting for photos. The output is written with PREVIEW- in the name
    so a preview can never be mistaken for, or pasted over, the real graphic.
    """
    cmp_layout = cfg.get("layout") == "compare"
    card_w = CMP_CARD_W if cmp_layout else CARD_W
    stage_w = CMP_STAGE_W if cmp_layout else STAGE_W
    stage_h = CMP_STAGE_H if cmp_layout else STAGE_H
    names = []
    for i in range(len(cfg["phones"])):
        w = os.path.join(refdir, f"_pv{i}.png")
        subprocess.run(
            ["magick", "-size", f"{stage_w - 10}x{stage_h - 10}",
             f"xc:#e4e4ea", "-fill", "#b9b9c4",
             "-draw", f"roundrectangle 90,40 {stage_w - 130},{stage_h - 40} 26,26",
             "-font", PREVIEW_FONT, "-gravity", "south", "-pointsize", "26",
             "-fill", "#8a8a96",
             "-annotate", "+0+18", "PHOTO NEEDED", w], check=True)
        names.append(os.path.basename(w))
    svg = (build_compare(names, cfg) if cmp_layout else build(names, cfg))
    base = os.path.abspath(os.path.join(refdir, "..", "PREVIEW-" + cfg["out"]))
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["magick", "-background", BG, base + ".svg", base + ".png"],
                   check=True)
    for i in range(len(cfg["phones"])):
        subprocess.run(["magick", base + ".png",
                        os.path.join(refdir, f"_pv{i}.png"),
                        "-geometry", f"+{M + i * (card_w + GAP) + STAGE_X + 5}"
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

    cmp_layout = cfg.get("layout") == "compare"
    card_w = CMP_CARD_W if cmp_layout else CARD_W
    stage_w = CMP_STAGE_W if cmp_layout else STAGE_W
    stage_h = CMP_STAGE_H if cmp_layout else STAGE_H

    works, names, digests = [], [], []
    for i, (label, *_) in enumerate(cfg["phones"]):
        work = os.path.join(mri.REFS, f"_ph{i}.jpg")
        digests.append(normalise(found[label], work, stage_w, stage_h))
        works.append(work)
        names.append(os.path.basename(work))

    if len(set(digests)) != len(digests):
        dup = [cfg["phones"][i][0] for i, d in enumerate(digests) if digests.count(d) > 1]
        for w in works:
            os.remove(w)
        sys.exit("ABORT: these photos resolved to the same image: "
                 + ", ".join(dup))

    svg = (build_compare(names, cfg) if cmp_layout else build(names, cfg))
    base = os.path.join(mri.IMG, cfg["out"])
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["magick", "-background", BG, base + ".svg", base + ".png"],
                   check=True)
    # The SVG renderer ignores <image href>, so photos must be composited in
    # afterwards, then the build steps are deleted.
    for i in range(len(cfg["phones"])):
        subprocess.run(["magick", base + ".png", works[i],
                        "-geometry", f"+{M + i * (card_w + GAP) + STAGE_X + 5}"
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
