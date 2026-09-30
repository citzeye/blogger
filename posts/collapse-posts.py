#!/usr/bin/env python3
"""Collapse every post to a single file.

Before: index.html carried a long editor-notes block, plus a separate
IMAGE-FIX.html holding a duplicate copy of the opening paragraphs. Two files to
keep in sync per post, and the second one drifted out of date constantly.

After: one index.html per post. The top holds exactly two things -
TITLE and DESCRIPTION - in a comment the author deletes before pasting. The
body below is the post. Nothing else.

The long notes (sources, caveats, verification checklists) are not thrown away:
they are archived to NOTES.md next to the post, so the reasoning survives
without sitting in the file that gets pasted into Blogger.

    python3 posts/collapse-posts.py
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def split_notes(raw):
    """Return (notes_text, body_html). Handles both old and new layouts."""
    m = re.search(r"<!--\s*END (?:EDITOR )?NOTES\s*-->", raw, re.I)
    if m:
        notes, body = raw[:m.start()], raw[m.end():]
    else:
        # No marker: treat everything up to the first content tag as notes.
        i = re.search(r"<(?:p|h2|img)\b", raw)
        if not i:
            return "", raw
        notes, body = raw[:i.start()], raw[i.start():]
    # strip the comment delimiters so the archive reads as plain text
    notes = re.sub(r"<!--\s*", "", notes)
    notes = re.sub(r"-->\s*$", "", notes)
    notes = re.sub(r"^\s*-->\s*$", "", notes, flags=re.M)
    notes = re.sub(r"<-- EDITOR NOTES", "", notes)
    return notes.strip("\n"), body.strip("\n")


def field(notes, *names):
    for n in names:
        m = re.search(rf"^{n}(?:\s*\([^)]*\))?\s*:\s*(.+)$", notes, re.M)
        if m:
            v = " ".join(m.group(1).split())
            v = re.sub(r"\s*\(\d+\s*chars?\)\s*$", "", v).strip()
            return v
    return ""


HEADER = """<!--
TITLE:       {title}
DESCRIPTION: {desc}
Delete this comment before pasting into Blogger, then fill Blogger's Title
field with the TITLE line above and the Description field with DESCRIPTION.
-->

"""


def main():
    for d in sorted(os.listdir(HERE)):
        p = os.path.join(HERE, d, "index.html")
        if not os.path.isfile(p):
            continue
        raw = io.open(p, encoding="utf-8").read()
        notes, body = split_notes(raw)

        title = field(notes, "TITLE") or f"UNSET - fill this in"
        desc = field(notes, "META DESCRIPTION", "DESCRIPTION")

        # drop any leftover comment fragments from the body
        body = re.sub(r"<!--\s*END (?:EDITOR )?NOTES\s*-->", "", body)
        body = body.strip("\n")

        out = HEADER.format(title=title, desc=desc or "UNSET - fill this in")
        out += body + "\n"
        io.open(p, "w", encoding="utf-8").write(out)

        # archive the long notes beside the post instead of losing them
        if notes.strip():
            np = os.path.join(HERE, d, "NOTES.md")
            body_note = (
                f"# {d}\n\n"
                f"Working notes for this post. Not published. The reasoning behind\n"
                f"the claims, the sources, and the checks still to do before this\n"
                f"post goes out. `index.html` is the only file that gets pasted.\n\n"
                f"```\n{notes}\n```\n")
            io.open(np, "w", encoding="utf-8").write(body_note)

        # the duplicate paste block is gone for good
        fx = os.path.join(HERE, d, "IMAGE-FIX.html")
        if os.path.exists(fx):
            os.remove(fx)

        print(f"  {d}")
        print(f"     title: {title[:64]}")
        print(f"     desc : {(desc[:60] + '...') if len(desc) > 60 else desc}")


if __name__ == "__main__":
    main()
