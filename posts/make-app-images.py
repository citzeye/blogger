#!/usr/bin/env python3
"""Build the single graphic for "3 AI Apps That Make Your Work Easier".

No vendor logos. OpenAI's site blocks scripted requests outright, and shipping
two real logos next to one wordmark would look worse than not using logos at
all - plus trademark exposure for a blog post. The app names are the identifier
a reader actually needs, set as wordmarks in each product's brand colour.

    python3 posts/make-app-images.py "3 AI Apps That Make Your Work Easier"

OUT
    images/01-ai-apps-easier-work.jpg    <- the only deliverable
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_POST = "3 AI Apps That Make Your Work Easier"
OUT_STEM = "01-ai-apps-easier-work"

# label, colour, cost line, "what it takes off your plate", "what stays yours"
APPS = [
    ("ChatGPT", "#10a37f",
     "Free tier  ·  Plus about $20/mo",
     "Drafting, summarizing, research",
     "Judgement, and anything a client signs off on"),
    ("ElevenLabs", "#000000",
     "Free tier  ·  paid from about $5/mo",
     "Recording, narration, translation",
     "Directing, and the final listen"),
    ("Zapier", "#ff4f00",
     "Free tier  ·  paid from about $20/mo",
     "Clicking between tools by hand",
     "Deciding what is worth automating"),
]

# Brand black for ElevenLabs sits on a dark card, so lift it to a light value.
ON_DARK = {"#000000": "#f4f4f8"}


class Card:
    """One app block: number, wordmark, the job it removes, the job it keeps."""

    def __init__(self, canvas, mri, index, app, y, width):
        label, colour, cost, removes, keeps = app
        fg = ON_DARK.get(colour, colour)
        self.y = y
        canvas.rect(mri.M, y, width, 400, mri.CARD, rx=6)
        canvas.rect(mri.M, y, 6, 400, ON_DARK.get(colour, colour), rx=0)

        x = mri.M + 40
        canvas.text(x, y + 74, f"0{index}", 40, mri.DIM, weight=True)
        canvas.text(x, y + 168, label, 64, fg, weight=True)
        canvas.text(x, y + 224, cost, 28, mri.DIM)

        canvas.rect(x, y + 258, width - 80, 1, mri.BORDER, rx=0)
        canvas.text(x, y + 302, "REMOVES", 20, mri.DIM, weight=True)
        canvas.text(x, y + 340, removes, 30, mri.FG)
        canvas.text(x, y + 380, "YOU STILL DO", 20, mri.DIM, weight=True)
        canvas.text(x + width - 80 - 40, y + 380, keeps, 24, mri.MUTED,
                    anchor="end")


def build(mri):
    W, M = mri.W, mri.M
    width = W - 2 * M
    head = ("~/AI AT WORK", ["3 AI APPS THAT MAKE", "YOUR WORK EASIER"],
            "The boring part goes first")
    head_h = mri.Canvas(10).header(*head)

    card_h, gap = 400, 22
    h = head_h + 3 * card_h + 2 * gap + 150
    c = mri.Canvas(h)
    y = c.header(*head)
    for i, app in enumerate(APPS, 1):
        Card(c, mri, i, app, y, width)
        y += card_h + gap
    c.text(M, y + 52, "Prices are approximate US figures in USD,", 24, mri.DIM)
    c.text(M, y + 88, "checked September 2026. Confirm on the vendor page.", 24, mri.DIM)
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
