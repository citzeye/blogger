#!/usr/bin/env python3
"""Build the single graphic for "3 Definite Causes of AI Slop".

Typography only, no photography and no vendor logos: this post is about writing,
so a fake screenshot or a stock image would undercut its own argument.

    python3 posts/make-slop-images.py "3 Definite Causes of AI Slop"

OUT
    images/01-ai-slop-causes.jpg    <- the only deliverable
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_POST = "3 Definite Causes of AI Slop"
OUT_STEM = "01-ai-slop-causes"

CAUSES = [
    ("01", "#ff6767", "Shipping the first draft",
     "It reads fine, so it ships",
     "Write four sentences first"),
    ("02", "#ffca85", "Prompting for count",
     "Ten tips, any order, no argument",
     "Ask for a claim, not a number"),
    ("03", "#a277ff", "Unchecked specifics",
     "Confident prices that are fiction",
     "Verify every number, or round it"),
]


def card(canvas, mri, number, colour, title, symptom, fix, y, width):
    canvas.rect(mri.M, y, width, 400, mri.CARD, rx=6)
    canvas.rect(mri.M, y, 6, 400, colour, rx=0)
    x = mri.M + 40

    canvas.text(x, y + 74, number, 40, mri.DIM, weight=True)
    canvas.text(x, y + 168, title, 52, mri.FG, weight=True)
    canvas.text(x, y + 232, symptom, 28, mri.MUTED)

    canvas.rect(x, y + 268, width - 80, 1, mri.BORDER, rx=0)
    canvas.text(x, y + 312, "FIX", 20, colour, weight=True)
    canvas.text(x, y + 356, fix, 30, mri.FG)


def build(mri):
    W, M = mri.W, mri.M
    width = W - 2 * M
    head = ("~/WRITING", ["3 DEFINITE CAUSES", "OF AI SLOP"],
            "Not a model failure. A process failure.")
    head_h = mri.Canvas(10).header(*head)

    card_h, gap = 400, 22
    h = head_h + 3 * card_h + 2 * gap + 150
    c = mri.Canvas(h)
    y = c.header(*head)
    for row in CAUSES:
        card(c, mri, *row, y, width)
        y += card_h + gap
    c.text(M, y + 52, "All three are decisions, not habits.", 26, mri.FG)
    c.text(M, y + 90, "Which is why removing one removes the symptom.", 24, mri.DIM)
    return c


def main():
    post = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_POST
    spec = importlib.util.spec_from_file_location(
        "mri", os.path.join(HERE, "make-real-images.py"))
    mri = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mri)
    mri.set_post_dir(post)
    mri.render(OUT_STEM, build(mri))
    print("done")


if __name__ == "__main__":
    main()
