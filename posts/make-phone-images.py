#!/usr/bin/env python3
"""Build the single graphic for "3 Phones Under $250".

    python3 posts/make-phone-images.py "3 Phones Under $250"

Source photos: posts/<Post Title>/images/refs/
    samsung-galaxy-a17.*    (galaxy-a17, a17)
    xiaomi-redmi-note-14.*   (redmi, note 14)
    samsung-galaxy-a16.*     (galaxy-a16, a16)
jpg/jpeg/png/webp/avif, any filename containing one of those keywords.

    python3 posts/make-phone-images.py --no-photos "3 Phones Under $250"
        Renders the layout with an empty product stage per card, so the
        composition and the type sizes can be checked before the photos exist.
        The output is explicitly NOT for publication.

OUT
    images/01-budget-phones.jpg    <- the only deliverable
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_POST = "3 Phones Under $250"
OUT_STEM = "01-budget-phones"

PHONES = [
    ("Samsung Galaxy A17 5G", 232, "6 years of updates", "#82aaff",
     ("galaxy-a17", "a17", "galaxy a17")),
    ("Xiaomi Redmi Note 14", 197, "Up to 256 GB, 45W", "#ffca85",
     ("redmi", "note 14", "note-14")),
    ("Samsung Galaxy A16 5G", 135, "Cheapest way in", "#61ffca",
     ("galaxy-a16", "a16", "galaxy a16")),
]


def collect(refdir):
    files = [os.path.join(refdir, f) for f in sorted(os.listdir(refdir))
             if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".avif"))]
    found = {}
    for label, _p, _t, _c, keys in PHONES:
        for f in files:
            if f in found.values():
                continue
            low = os.path.basename(f).lower()
            if any(k in low for k in keys):
                found[label] = f
                break
    return found


def normalise(src, work):
    subprocess = __import__("subprocess")
    subprocess.run(
        ["magick", src, "-fuzz", "4%", "-trim", "+repage",
         "-background", "white", "-alpha", "remove", "-alpha", "off",
         "-bordercolor", "white", "-border", "8",
         "-resize", "1100x825", "-gravity", "center", "-extent", "1100x825",
         "-quality", "92", work], check=True)


def build(mri, photo_files):
    W, M = mri.W, mri.M
    width = W - 2 * M
    head = ("~/PHONE BUYING GUIDE", ["3 PHONES UNDER", "$250"],
            "US street prices, checked September 2026")
    head_h = mri.Canvas(10).header(*head)

    ch, gap = 400, 22
    h = head_h + 3 * ch + 2 * gap + 150
    c = mri.Canvas(h)
    y = c.header(*head)

    for label, price, tag, colour, _keys in PHONES:
        c.rect(M, y, width, ch, mri.CARD, stroke=colour, sw=3)
        c.text(M + 24, y + 56, tag, 30, colour, weight=True)
        c.text(M + 24, y + 118, label, 46, mri.FG, weight=True)

        # 4:3 product stage on the left
        px, py, pw, ph = M + 24, y + 140, 380, 285
        c.rect(px, py, pw, ph, "#ffffff", rx=4)
        src = photo_files.get(label)
        if src:
            c.photos.append((src, px + 6, py + 6, pw - 12, ph - 12))

        tx = px + pw + 32
        c.text(tx, y + 236, f"${price}", 52, colour, weight=True)
        c.text(tx, y + 286, "approx street price", 26, mri.MUTED)
        c.text(tx, y + 336, "sold in the US and UK", 24, mri.DIM)
        y += ch + gap

    c.text(M, y + 52, "Prices move weekly in this band.", 26, mri.FG)
    c.text(M, y + 90, "Confirm with the seller before you buy.", 24, mri.DIM)
    return c


def main():
    args = [a for a in sys.argv[1:]]
    no_photos = "--no-photos" in args
    args = [a for a in args if a != "--no-photos"]
    post = args[0] if args else DEFAULT_POST

    spec = importlib.util.spec_from_file_location(
        "mri", os.path.join(HERE, "make-real-images.py"))
    mri = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mri)
    mri.set_post_dir(post)
    refdir = mri.REFS
    os.makedirs(refdir, exist_ok=True)

    photo_files = {}
    if not no_photos:
        found = collect(refdir)
        missing = [lbl for lbl, *_ in PHONES if lbl not in found]
        if missing:
            print("MISSING PRODUCT PHOTOS - the graphic must show real hardware.\n")
            for lbl, _p, _t, _c, keys in PHONES:
                mark = "OK  " if lbl in found else "--  "
                print(f"  {mark}{lbl:<26} filename must contain: {'/'.join(keys)}")
            print(f"\nDrop them into:\n  {refdir}")
            print("\nOr preview the layout without photos:")
            print(f"  python3 posts/make-phone-images.py --no-photos \"{post}\"")
            sys.exit(1)

        import subprocess as sp
        works = []
        for i, (label, *_) in enumerate(PHONES):
            work = os.path.join(mri.REFS, f"_p{i}.jpg")
            normalise(found[label], work)
            works.append(work)
            photo_files[label] = os.path.basename(work)

    stem = OUT_STEM if not no_photos else "PREVIEW-01-budget-phones"
    mri.render(stem, build(mri, photo_files))
    if not no_photos:
        for i in range(len(PHONES)):
            w = os.path.join(mri.REFS, f"_p{i}.jpg")
            if os.path.exists(w):
                os.remove(w)
    print("done")


if __name__ == "__main__":
    main()
