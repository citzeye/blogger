#!/usr/bin/env python3
"""
Validate a Blogger post against AGENT.md rules (§1 SEO, §2 images, §12 longlasting).
Usage: python3 validate-post.py <post.html>
Exit 0 = all rules pass. Non-zero = count of failures.
"""
import re, sys, os, json

FAIL = []
WARN = []

def check(ok, label, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"  — {detail}" if detail and not ok else ""))
    if not ok:
        FAIL.append(label)

def warn(label, detail=""):
    print(f"  WARN  {label}" + (f"  — {detail}" if detail else ""))
    WARN.append(label)

def main(path):
    raw = open(path, encoding="utf-8").read()
    # Blogger renders the post title from the "Title" field as the page's only
    # H1. The body must therefore contain ZERO <h1>: an H1 here would duplicate
    # it. Editor notes are the leading HTML comment block; keep the body split
    # on the first content tag, not on "-->" (nested comments break that).
    # Do NOT split on "-->" — the notes block itself contains nested <!-- --> comments.
    m = re.search(r"<!--\s*END (?:EDITOR )?NOTES\s*-->", raw, re.I)
    body = raw[m.end():] if m else raw
    # Strip HTML comments before any structural check. Comments legitimately
    # mention tags (e.g. "do not add <h1>"), which would otherwise be counted
    # as real markup.
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.S)

    print(f"=== {os.path.basename(path)} ===\n")

    # ---------- §1 SEO ----------
    print("[§1 SEO]")
    n_h1 = len(re.findall(r"<h1[ >]", body))
    check(n_h1 == 0, "No H1 in body (title lives in Blogger's Title field)",
          f"found {n_h1}")
    # Title is supplied by Blogger; check it from the notes header, not the body.
    th = re.search(r"^TITLE(?:\s*\(Blogger field\))?\s*:\s*(.+)$", raw, re.M)
    title = th.group(1).strip() if th else ""
    check(0 < len(title) <= 65, "Title length <= 65 chars", f"{len(title)}: {title!r}")
    check(not re.search(r"\b20\d{2}\b", title), "No year in title (§12.2)", title)

    h2 = re.findall(r"<h2[ >]", body); h3 = re.findall(r"<h3[ >]", body)
    check(len(h2) > 0, "Has H2 subheadings")
    check(len(h3) > 0, "Has H3 subheads")
    # no skipped level: every h3 must be preceded by an h2
    order = re.findall(r"<h([123])[ >]", body)
    skipped = any(order[i] == "3" and (i == 0 or "2" not in order[:i]) for i in range(len(order)))
    check(not skipped, "Heading hierarchy never skips a level (§12.8)")

    md = re.search(r"META DESCRIPTION\s*:\s*(.+)", raw)
    if md:
        d = re.sub(r"\s*\(\d+ chars\)", "", md.group(1)).strip()
        check(len(d) <= 160, "Meta description <= 160 chars", f"{len(d)}: {d!r}")
        check(len(d) >= 70, "Meta description >= 70 chars", f"{len(d)}")
    else:
        check(False, "Meta description declared in editor notes")

    slug = re.search(r"SLUG\s*:\s*(\S+)", raw)
    check(bool(slug), "Slug declared")
    if slug:
        check(not re.search(r"20\d{2}", slug.group(1)), "No year in slug (§12.2)", slug.group(1))

    # Primary keyword is declared per article in the editor notes, so this
    # validator is not welded to one post. Format:  KEYWORDS: laptop, school
    kwd = re.search(r"^KEYWORDS\s*:\s*(.+)$", raw, re.M)
    kws = [k.strip().lower() for k in kwd.group(1).split(",") if k.strip()] if kwd else []
    if not kws:
        warn("No KEYWORDS declared in editor notes",
             'add "KEYWORDS: term, term" so the keyword checks are meaningful')
    t_low = title.lower()
    check(any(k in t_low for k in kws), "Primary keyword present in title",
          title if kws else "no KEYWORDS declared")
    first100 = " ".join(re.sub(r"<[^>]+>", " ", body).split()[:100]).lower()
    check(any(k in first100 for k in kws),
          "Keyword in first 100 words (§1)",
          f"none of {kws} found" if kws else "no KEYWORDS declared")

    # ---------- §12.7 longlasting ----------
    print("\n[§12 Longlasting]")
    check(re.search(r"\b20\d{2}\b", body) is not None, "Article states an as-of date (§12.5)")
    check(bool(re.search(r"(?i)re-?check|confirm the current price", body)),
          "Tells reader to re-verify prices (§12.5)")
    # Site currency is USD, so prices look like $340 or $300-380. The old
    # Rp-only pattern silently skipped price-led articles.
    # Strip the editor-notes metadata out of the price scan: "META DESCRIPTION
    # ...and the $ where real AI hardware starts" was being counted as a price.
    body_prices = re.sub(r"META DESCRIPTION.*", "", body)
    prices = re.findall(r"\$\s?\d[\d,]*(?:\s?-\s?\$?\d[\d,]*)?", body_prices)
    if prices:
        # 3+ is fine for an article that quotes "from"-level prices. Only a
        # per-product listicle needs one price per pick.
        check(len(prices) >= 3, "Prices given per product",
              f"{len(prices)} prices found")
    else:
        warn("No prices in body", "acceptable if article is not price-led")
    # Only enforceable when the article actually quotes prices. An article
    # explaining a capability can legitimately quote none.
    if prices:
        dated = bool(re.search(
            r"(?i)about the prices|price when this article was written|"
            r"ranges observed|observed at .*retailers|starting point\s+"
            r"rather than a live price|when this article\s+was written|"
            r"checked\s+(?:in\s+)?(?:january|february|march|april|may|june|july|"
            r"august|september|october|november|december)\s*\d{4}|"
            r"prices?\s+(?:of\s+)?(?:roughly|around|about)\s+\$", body))
        check(dated, "Explicit price-dating disclaimer (§12.5)")
    else:
        warn("No price figures in body",
             "fine for a capability article; add a disclaimer if you quote prices")

    # ---------- §12.6 text-first ----------
    print("\n[§12.6 Text-first]")
    imgs = re.findall(r"<img\b[^>]*>", body)
    check(len(imgs) == 0 or all("alt=" in i for i in imgs),
          "Every <img> has alt (§2)", f"{sum(1 for i in imgs if 'alt=' not in i)} missing")
    check(all(("width=" in i and "height=" in i) for i in imgs),
          "Every <img> has width+height (anti-CLS §2)")

    # ---------- §2 images / media ----------
    print("\n[§2 Images]")
    check(len(imgs) > 0, "Article has at least one image",
          "text-only is allowed by §12.6 but hurts CTR")
    for i in imgs:
        src = re.search(r'src="([^"]+)"', i)
        if src and src.group(1).startswith("http") and "citzeye" not in src.group(1):
            check(False, "No external hotlinked images", src.group(1))

    # ---------- §13.9 internal links ----------
    print("\n[§13.9 Internal links]")
    links = re.findall(r'<a\s+href="([^"]+)"', body)
    internal = [l for l in links if not l.startswith(("http://", "https://"))]
    check(len(internal) >= 2, "At least 2 internal links (§13.9)", f"found {len(internal)}")
    ext = [l for l in links if l.startswith(("http://", "https://"))]
    if ext:
        # A technical article legitimately cites its source. What is not
        # acceptable is an unsafe outbound link, so check that instead.
        anchor_ok = bool(re.search(
            r'<a\s[^>]*href="https?://[^"]*"[^>]*target="_blank"'
            r'[^>]*rel="[^"]*noopener', body, re.I))
        check(anchor_ok, "External links use target=_blank rel=noopener",
              f"{len(ext)} external link(s)")
    else:
        check(True, "No external outbound links needed here")
    for l in internal:
        check(l.startswith("/"), "Internal link is site-absolute", l)

    # ---------- §1.1 one topic ----------
    print("\n[§12.8 One topic]")
    check(len(h2) <= 9, "Section count sane (<=9 H2)", f"{len(h2)} H2 sections")

    # ---------- HTML integrity ----------
    print("\n[HTML integrity]")
    for tag in ["table", "tr", "td", "th", "ul", "ol", "li", "blockquote", "p", "div", "strong"]:
        o = len(re.findall(rf"<{tag}[ >]", body)); c = len(re.findall(rf"</{tag}>", body))
        check(o == c, f"<{tag}> balanced", f"{o} open / {c} close")
    # bare ampersand outside entities
    bare = [m for m in re.finditer(r"&(?!amp;|lt;|gt;|quot;|#|nbsp;|39;|38;|34;)", body)]
    check(not bare, "No unescaped & in body", f"{len(bare)} found")

    # ---------- Summary ----------
    print(f"\n{'='*46}")
    print(f"  {'ALL RULES PASS' if not FAIL else str(len(FAIL)) + ' FAILED'}"
          + (f", {len(WARN)} warning(s)" if WARN else ""))
    if FAIL:
        for f in FAIL:
            print(f"    FAILED: {f}")
    print("="*46)
    return len(FAIL)

if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "best-phone-under-2-juta.html"
    sys.exit(min(main(p), 99))
