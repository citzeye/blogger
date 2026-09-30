#!/usr/bin/env python3
"""Build ONE graphic for the school-laptop article: all three laptops in a
single portrait image, each product's NAME AT THE TOP of its own card.

    python3 posts/make-laptop-images.py "<Post Title folder>"

Source photos: posts/<Post Title>/images/refs/laptop/
    acer-chromebook-plus-514.*     (acer, chromebook)
    lenovo-ideapad-slim-3i.*        (lenovo, ideapad, slim 3i)
    hp-omnibook-3.*                 (hp, omnibook)
jpg/jpeg/png/webp/avif, any filename containing one of those keywords.

OUT
    images/01-laptops-for-school.webp     <- upload this one
    images/01-laptops-for-school.png      <- lossless fallback, ~8x bigger

WHY NOT SVG: ImageMagick's built-in SVG renderer ignores <image href>, so the
.svg written next to the PNG contains the text and boxes but NO product photos.
Opening it renders empty frames. It is a build artifact, not a deliverable.
Why not PNG: ~360 KB versus ~55 KB for the same picture. Both are exact at this
size; WebP wins on weight, which is what PageSpeed measures.
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_POST = "3 Cheap Laptops for School That Hold Up"

# The verdict line is the only per-post difference between the two articles that
# share these three laptops. Everything else - geometry, sizes, colours - is
# identical on purpose, so the graphics read as one set.
THIRD_LINE = {
    "3 Cheap Laptops for School That Hold Up": {
        "acer":   "Chrome OS, 14in 1920x1200 matte",
        "lenovo": "Windows 11, 15.6in 1080p",
        "hp":     "Windows 11, 512GB SSD",
    },
    "Can Budget Laptops Run AI Locally": {
        "acer":   "No NPU - cloud AI only",
        "lenovo": "No NPU - small models, slowly",
        "hp":     "No NPU - cloud AI only",
    },
}
HEADINGS = {
    "3 Cheap Laptops for School That Hold Up":
        ("~/SCHOOL LAPTOPS", ["3 CHEAP LAPTOPS", "FOR SCHOOL"],
         "US street prices, checked September 2026"),
    "Can Budget Laptops Run AI Locally":
        ("~/ON-DEVICE AI", ["THE AI LABEL", "ON A BUDGET LAPTOP"],
         "Checked against Microsoft Copilot+ requirements"),
}
ACCENT_LINE = {
    "3 Cheap Laptops for School That Hold Up": "Street prices are ranges. Re-check before you buy.",
    "Can Budget Laptops Run AI Locally":
        "None of these three has a neural processing unit.",
}
EXT = (".jpg", ".jpeg", ".png", ".webp", ".avif")
OUT_STEM = {
    "3 Cheap Laptops for School That Hold Up": "01-laptops-for-school",
    "Can Budget Laptops Run AI Locally": "01-budget-laptop-ai-verdict",
}
NORMALISED = (1200, 900)          # 4:3 working copy, so every stage fills evenly

# label, price, keywords, colour key, tag, blurb
LAPTOPS = [
    ("Acer Chromebook Plus 514", 340, ("acer", "chromebook"), "accent",
     "BEST OVERALL", "acer"),
    ("Lenovo IdeaPad Slim 3i", 325, ("lenovo", "ideapad", "slim 3i"), "sky",
     "CHEAPEST WINDOWS", "lenovo"),
    ("HP OmniBook 3", 475, ("hp", "omnibook", "omni book"), "success",
     "MOST STORAGE", "hp"),
]

CARD_H, GAP = 460, 20
PHOTO_W, PHOTO_H = 400, 300        # 4:3


def load_engine():
    spec = importlib.util.spec_from_file_location(
        "mri", os.path.join(HERE, "make-real-images.py"))
    mri = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mri)
    return mri


def collect(refdir):
    files = [os.path.join(refdir, f) for f in sorted(os.listdir(refdir))
             if f.lower().endswith(EXT)]
    found = {}
    for label, _p, keys, *_ in LAPTOPS:
        for f in files:
            if f in found.values():
                continue
            low = os.path.basename(f).lower()
            if any(k in low for k in keys):
                found[label] = f
                break
    spare = [f for f in files if f not in found.values()]
    for label, *_ in LAPTOPS:
        if label not in found and spare:
            found[label] = spare.pop(0)
    return found


def normalise(src, work):
    """Trim whitespace, then pad to an exact 4:3 so the stage fills evenly."""
    subprocess.run(
        ["magick", src, "-fuzz", "4%", "-trim", "+repage",
         "-background", "white", "-alpha", "remove", "-alpha", "off",
         "-bordercolor", "white", "-border", "8",
         "-resize", f"{NORMALISED[0]}x{NORMALISED[1]}",
         "-gravity", "center", "-extent", f"{NORMALISED[0]}x{NORMALISED[1]}",
         "-quality", "93", work], check=True)


def build(mri, work_names, colours, post):
    W, M = mri.W, mri.M
    cw = W - 2 * M
    blurb = THIRD_LINE[post]
    head = HEADINGS[post]
    head_h = mri.Canvas(10).header(*head)
    h = head_h + 3 * CARD_H + 2 * GAP + 120

    c = mri.Canvas(h)
    y = c.header(*head)

    for i, (label, price, _keys, ck, tag, key) in enumerate(LAPTOPS):
        col = colours[ck]
        c.rect(M, y, cw, CARD_H, mri.CARD, stroke=col, sw=3)
        # ---- NAME AT THE TOP of the card ----
        c.text(M + 24, y + 58, tag, 30, col, weight=True)
        c.text(M + 24, y + 116, label, 46, mri.FG, weight=True)
        # ---- photo, left ----
        py = y + 140
        c.rect(M + 24, py, PHOTO_W, PHOTO_H, "#ffffff", rx=4)
        c.photos.append((work_names[i], M + 30, py + 6,
                         PHOTO_W - 12, PHOTO_H - 12))
        # ---- price + reason, right ----
        tx = M + 24 + PHOTO_W + 34
        c.text(tx, y + 250, f"${price}", 46, col, weight=True)
        c.text(tx, y + 300, blurb[key], 27, mri.MUTED)
        bar_w = cw - (tx - M) - 24
        c.rect(tx, y + 340, bar_w, 12, mri.BORDER, rx=6)
        top = max(p for _l, p, *_ in LAPTOPS)
        c.rect(tx, y + 340, round(bar_w * price / top), 12, col, rx=6)
        y += CARD_H + GAP

    c.text(M, y + 48, ACCENT_LINE[post], mri.FS_SMALL, mri.DIM)
    return c


def main():
    post = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_POST
    mri = load_engine()
    mri.set_post_dir(post)
    refdir = os.path.join(mri.REFS, "laptop")
    os.makedirs(refdir, exist_ok=True)

    mapping = collect(refdir)
    missing = [lbl for lbl, *_ in LAPTOPS if lbl not in mapping]
    if missing:
        print("MISSING PRODUCT PHOTOS - the graphic must show real hardware.\n")
        for lbl, _p, keys, *_ in LAPTOPS:
            print(f"  {'OK  ' if lbl in mapping else '--  '}{lbl:<28} "
                  f"filename must contain: {'/'.join(keys)}")
        print(f"\nDrop them into:\n  {refdir}")
        sys.exit(1)

    # Normalise each source into its OWN working file. Writing them all to one
    # shared _work.jpg silently made every card render the last image - three
    # different products showing the same laptop.
    work_names = []
    works = []
    for i, (label, *_rest) in enumerate(LAPTOPS):
        work = os.path.join(mri.REFS, f"_work-{i}.jpg")
        normalise(mapping[label], work)
        works.append(work)
        work_names.append(os.path.basename(work))

    # Guard: the three working files must genuinely differ. Identical hashes mean
    # the same photo got reused, which would put the wrong laptop under a
    # recommendation.
    digests = [subprocess.run(["md5sum", w], capture_output=True,
                              text=True).stdout.split()[0] for w in works]
    if len(set(digests)) != len(digests):
        dupes = [LABTOPS[i][0] for i, d in enumerate(digests) if digests.count(d) > 1]
        for w in works:
            os.remove(w)
        sys.exit("ABORT: these laptops resolved to the same photo: "
                 + ", ".join(dupes) + "\nCheck the filenames in refs/laptop/ - "
                 "each must contain its own keyword.")

    colours = {"accent": mri.ACCENT, "sky": mri.SKY, "success": mri.SUCCESS}
    mri.render(OUT_STEM[post], build(mri, work_names, colours, post))
    for w in works:
        os.remove(w)


if __name__ == "__main__":
    main()
