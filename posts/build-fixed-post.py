#!/usr/bin/env python3
"""Build a clean, paste-ready body for the already-published post.

Fixes, all in the content HTML only (no template edits):
  1. The published post had TWO <div class="separator"> opened before the first
     image but only ONE closed. The orphan .separator div wrapped every
     paragraph from the first image to the end of the post, and inherited
     text-align:center, so everything after image #1 rendered centred. This
     script emits zero wrapper divs, so that cannot recur.
  2. Images are no longer wrapped in <a href="...same image...">, which added a
     pointless link and stripped the alt text in Blogger's inserter.
  3. Obsolete border="0" and the inline margin-left/right:1em are dropped.
  4. The <!--SLOT LINK ... --> editorial markers are removed.
  5. Every image carries real alt text plus width/height (CLS) and loading=lazy.
  6. No <h1>: Blogger's Title field already renders the page's single H1.

Usage:  python3 build-fixed-post.py   ->  posts/post-body-FIXED.html
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "best-phone-under-2-juta.html")
OUT = os.path.join(HERE, "post-body-FIXED.html")

# Image URLs as they already exist in the live post. Reuse them so the fixed
# body works the moment it is pasted - no re-upload required.
LIVE = {
    "images/01-featured.webp":
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb817nQKFcgmcstbreJOwIk47-VojJkG4b07uiBdsQ4bdL39Mo9To_kquEUzTsOlekPQrICRsHfptNuQ9-HJ0R04CssKXo9KtEFseGxqB4uypVkWe129cQzQXiYut5ZD_95JJQiGhw5t4aBL9dHPwqKEE9-NzIp1UrNuVvgaK8cj8IVhR9WaYjhloVxh04/s1600/01-featured.webp",
    "images/02-price-comparison.png":
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFeYQhxbPE5kGPSWMgXGz7fgY4jRflSD3xstJGNec1If3yLBdHDc94ianaXuVFHeVxPhBoA5HKOi1v7sRzmw5Sj5tTPZ6ToFEYkeiQdBdS8CPHnGtijP_LSCVAc-K_UwVp31dKdAhiK6rG9asONsWy2A7S2Aks_vkhdA1A7xyL93tsuzkOFgymm3sigvUu/s1600/02-price-comparison.webp",
    "images/03-what-matters.png":
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3W4ZhfQT27MDMHdyPzVHcKzpIp0ACwyo8s4fLEUvqTFZbanjdmkCvbe61GpA5dhk6uvm1A9bd__Jo6Wg2ESyzWRsOORP6L_jUFMNOa15p-c_jF2MEbeX7wYpmPy2s1Ju0iFNbXQqPO1qcKrwLYjspIS0A4fQPTI30iarBSkiWuKpNon9E_11CRrKHc04q/s1600/03-what-matters.webp",
}

HEADER = """<!-- POST-BODY-FIXED
  Paste this whole block into Blogger: Edit post -> HTML view -> select all ->
  paste -> Publish.

  What this fixes (the centring you saw):
    Blogger's image dialog wrapped the first image in TWO <div class="separator">
    but closed only ONE, so the leftover .separator div enclosed every paragraph
    from the first image to the end of the post and inherited text-align:center.
    This body contains no wrapper divs, so the centring cannot come back.

  Notes:
    - Do NOT add an <h1>: the page's only H1 is the Blogger Title field.
    - Image #1 sets the post thumbnail, so it must stay first.
    - Images 02/03/04 are still the earlier abstract graphics. Once the
      real-product replacements are uploaded, swap the three src values and the
      alt text; the markup shape does not change.
  ===================================================================== -->

"""


def main():
    raw = open(SRC, encoding="utf-8").read()

    # Keep only the publishable body: everything after the editor-notes marker,
    # with all HTML comments stripped.
    m = re.search(r"<!--\s*END (?:EDITOR )?NOTES\s*-->", raw, re.I)
    body = raw[m.end():] if m else raw
    body = re.sub(r"<!--.*?-->", "\n", body, flags=re.S)

    # Image 04 was never uploaded, so it cannot be referenced. Drop it rather
    # than ship a broken <img>.
    body = re.sub(r'<img[^>]*images/04-which-one\.png[^>]*>\n?', "", body)

    # Point images at the URLs already live in the post.
    for local, live in LIVE.items():
        body = body.replace(f'src="{local}"', f'src="{live}"')

    # Guarantee lazy-loading below the fold; the first image stays eager so it
    # is fetched immediately (it is also what sets the post thumbnail).
    def add_lazy(mo):
        tag = mo.group(0)
        if "loading=" in tag:
            return tag
        return tag[:-1].rstrip() + ' loading="lazy">'

    tags = list(re.finditer(r"<img[^>]*>", body))
    if tags:
        first = tags[0]
        head, tail = body[:first.end()], body[first.end():]
        body = head + re.sub(r"<img[^>]*>", add_lazy, tail)

    # Collapse the blank lines left by comment stripping.
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HEADER + body + "\n")

    # ---- verify ----------------------------------------------------------
    print(f"wrote {OUT}  ({os.path.getsize(OUT)} bytes)\n")
    checks = [
        ('no <div> wrapper            ', body.count("<div"), 0),
        ("no <a> wrapping an <img>   ",
         len(re.findall(r"<a[^>]*>\s*<img", body)), 0),
        ("no obsolete border=         ", body.count('border="'), 0),
        ("no inline style=            ", body.count("style="), 0),
        ("no <h1>                    ", len(re.findall(r"<h1[ >]", body)), 0),
        ("no SLOT LINK comment        ", body.count("SLOT LINK"), 0),
        ("every img has alt           ",
         len(re.findall(r'<img(?![^>]*\balt=)[^>]*>', body)), 0),
        ("every img has w+h           ",
         len(re.findall(r'<img(?![^>]*\bwidth=)[^>]*>', body)), 0),
        ("every img is a live URL     ",
         len(re.findall(r'<img[^>]*src="(?!https://blogger\.googleusercontent)',
                        body)), 0),
    ]
    bad = 0
    for label, got, want in checks:
        ok = got == want
        bad += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {label} {got} (want {want})")

    # Stack-based tag balance, mirroring a browser's parser.
    void = {"img", "br", "hr", "meta", "link", "input", "source"}
    stack, mismatch = [], []
    for t in re.finditer(r"<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>", body):
        close, name, self = t.group(1), t.group(2).lower(), t.group(4)
        if name in void or self == "/":
            continue
        if not close:
            stack.append(name)
        elif stack and stack[-1] == name:
            stack.pop()
        elif name in stack:
            while stack and stack.pop() != name:
                pass
            mismatch.append(name)
        else:
            mismatch.append(name)
    ok = not stack and not mismatch
    bad += not ok
    print(f"  {'PASS' if ok else 'FAIL'}  tags balanced          "
          f"unclosed={stack or 'none'} mismatch={mismatch or 'none'}")
    print("\nALL CLEAN" if not bad else f"\n{bad} PROBLEM(S)")


if __name__ == "__main__":
    main()
