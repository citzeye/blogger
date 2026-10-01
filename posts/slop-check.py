#!/usr/bin/env python3
"""
Flag predictable AI-writing patterns in a post's prose.

Runs beside validate-post.py and checks a different thing. validate-post.py
enforces structural rules from AGENT.md (heading order, link targets, image
dimensions). This one reads the sentences: filler openers, business jargon, the
"serves as" dodge, vague attributions, hollow participial analysis.

WHY THIS EXISTS SEPARATELY
    The site publishes articles about why numbers in spec sheets mislead, and an
    article about AI content quality. If the prose of those articles carries the
    patterns they analyse, the argument collapses on contact with the reader.

    The catalogue is adapted from Stephen D. Turner's `skill-deslop`
    (github.com/stephenturner/skill-deslop, MIT, (c) 2026), vendored into
    OpenSEO. See references/catalog.md for provenance and for the four edits
    made on adaptation.

TUNED AGAINST THE PUBLISHED CORPUS
    The rule set was calibrated by running it against all ten live posts. Two
    upstream rules were dropped because they fired on correct writing here:

      - em dashes. 136 uses across the corpus, and the template plus AGENT.md
        both rely on them. House style, not a tic. Not checked.
      - bold-first bullets. 115 uses, mostly spec fields (`Processor:` 9x,
        `Display:` 9x, `Price:` 9x). Scannable reference data, which is the
        purpose of these articles. Not checked.

    `actually` is counted and reported but never fails: it appears 28 times
    across the corpus and means "in fact" every time.
    `landscape` is only flagged when it is not the literal orientation sense.

USAGE
    python3 slop-check.py <post.html> [...]      exit 0 clean, 1 if any file flagged
    python3 slop-check.py posts/*/index.html     check everything
"""
import os
import re
import sys

# --------------------------------------------------------------------------
# Level 1 and 2: patterns with no legitimate technical use. These fail.
# Each entry is (label, regex, message).
# --------------------------------------------------------------------------

PHRASES = [
    ("throat-clearing opener", r"here'?s the (?:thing|kicker|deal|problem though)"),
    ("throat-clearing opener", r"here'?s what most people miss"),
    ("throat-clearing opener", r"here'?s where it gets interesting"),
    ("throat-clearing opener", r"the uncomfortable truth is"),
    ("throat-clearing opener", r"\bit turns out\b"),
    ("throat-clearing opener", r"\blet me be clear\b"),
    ("throat-clearing opener", r"\bcan we talk about\b"),

    ("emphasis crutch", r"\blet that sink in\b"),
    ("emphasis crutch", r"\bmake no mistake\b"),
    ("emphasis crutch", r"\bthis matters because\b"),

    ("pedagogical hand-holding", r"\blet'?s (?:break this down|unpack|explore|dive in|dive into)\b"),
    ("pedagogical hand-holding", r"\bthink of it (?:as|like)\b"),
    ("pedagogical hand-holding", r"\bimagine a world (?:where|in which)\b"),

    ("filler transition", r"\bit'?s worth noting\b"),
    ("filler transition", r"\bit bears mentioning\b"),
    ("filler transition", r"\bat the end of the day\b"),
    ("filler transition", r"\bat its core\b"),
    ("filler transition", r"\bin today'?s\b"),
    ("filler transition", r"\bwhen it comes to\b"),
    ("filler transition", r"\bthe reality is\b"),
    ("filler transition", r"\bin a world where\b"),
    ("filler transition", r"\bnotably\b"),

    ("meta-commentary", r"\bplot twist\b"),
    ("meta-commentary", r"\bspoiler:"),
    ("meta-commentary", r"\byou already know this,? but\b"),
    ("meta-commentary", r"\bbut that'?s another post\b"),
    ("meta-commentary", r"\bthe rest of this (?:essay|article|post|piece) (?:explains|covers|walks)\b"),
    ("meta-commentary", r"\blet me walk you through\b"),
    ("meta-commentary", r"\bin this section,? we(?:'ll| will)\b"),
    ("meta-commentary", r"\bas we(?:'ll| will) see\b"),
    ("meta-commentary", r"\bi want to explore\b"),
    ("meta-commentary", r"\bin conclusion\b"),
    ("meta-commentary", r"\bto sum up\b"),
    ("meta-commentary", r"\bin summary\b"),
    ("meta-commentary", r"\bas we(?:'ve| have) seen in this section\b"),
    ("meta-commentary", r"\band so we return to where we began\b"),

    ("self-certifying candor", r"\bthe honest (?:answer|framing|truth)\b"),
    ("self-certifying candor", r"\bthe most honest signal\b"),
    ("self-certifying candor", r"\ban honest forecast\b"),

    ("vague attribution", r"\bexperts (?:argue|say|believe|agree)\b"),
    ("vague attribution", r"\bindustry reports (?:suggest|show|indicate)\b"),
    ("vague attribution", r"\bobservers have cited\b"),
    ("vague attribution", r"\bseveral publications have noted\b"),
    ("vague attribution", r"\bstudies (?:show|suggest|indicate)\b"),
    ("vague attribution", r"\bresearch (?:shows|suggests|indicates)\b"),

    ("vague declarative", r"\bthe reasons are structural\b"),
    ("vague declarative", r"\bthe implications are (?:significant|important)\b"),
    ("vague declarative", r"\bthis is the deepest problem\b"),
    ("vague declarative", r"\bthe stakes are high\b"),
    ("vague declarative", r"\bthe consequences are real\b"),

    ("participial analysis", r"\bhighlighting its\b"),
    ("participial analysis", r"\bunderscoring its\b"),
    ("participial analysis", r"\breflecting broader trends\b"),
    ("participial analysis", r"\bcontributing to (?:the region|its|our)\b"),

    ("formulaic dismissal", r"\bdespite (?:these|its|the) challenges\b"),

    ("serves-as dodge", r"\bserves as\b"),
    ("serves-as dodge", r"\bstands as\b"),
]

WORDS = [
    "delve", "tapestry", "nuanced", "remarkably", "arguably",
    "game-changer", "game changer", "double down", "deep dive", "circle back",
    "take a step back", "moving forward", "on the same page", "paradigm",
    "synergy", "leverage", "utilize", "robust", "streamline", "harness",
    "lean into", "ecosystem",
]

# Literal senses that are correct on this site and must not be flagged.
# `landscape` is deliberately absent from WORDS rather than excepted here:
# upstream bans it outright, but this site writes about screen and photo
# orientation, so it is used correctly at least once in the corpus. Excluding it
# by absence is the honest way to say "never flag this word".
WORD_EXCEPTIONS = {
    # A technical verb in a hardware context is fine.
    "harness": r"\bharness(?:ed|ing)?\s+(?:the|a|an|its|their|power|voltage)\b",
    "ecosystem": r"\b(?:android|google|samsung|apple|app|developer|vendor|open)\s+ecosystem\b",
}

UNICODE_ARROW = re.compile(r"[\u2192\u2190\u21d2]")

# --------------------------------------------------------------------------
# Advisory only. Reported, never failed.
# --------------------------------------------------------------------------
ADVISORY_ADVERBS = [
    "actually", "simply", "really", "genuinely", "honestly", "literally",
    "importantly", "crucially", "interestingly", "fundamentally", "inherently",
    "inevitably", "deeply", "truly",
    # `quietly` is the most overrepresented adverb in machine-generated prose,
    # and upstream fails it. It is advisory here because it has a live
    # adverbial sense that careful prose depends on: "two of them quietly cost
    # you something else" means the cost is not obvious, which is the point of
    # the sentence. Measured against the corpus, two of three hits were that
    # sense, so failing it would punish correct writing.
    "quietly",
]


def prose_only(raw):
    """Return the article body with markup and editorial comments removed.

    The header comment and any mid-body editor notes must not count, or the
    check would flag its own rule names. Comments are stripped first, then tags,
    so an attribute value never contributes.
    """
    m = re.search(r"<!--\s*END (?:EDITOR )?NOTES\s*-->", raw, re.I)
    body = raw[m.end():] if m else raw
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = (body.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))
    return re.sub(r"\s+", " ", body)


def occurrences(pattern, text, limit=6):
    out = []
    for m in re.finditer(pattern, text, re.I):
        start = max(0, m.start() - 42)
        out.append(("..." + text[start:m.end() + 42].strip() + "...").strip())
        if len(out) >= limit:
            break
    return out


def check(path):
    raw = open(path, encoding="utf-8").read()
    text = prose_only(raw)
    findings = []

    for label, pattern in PHRASES:
        hits = occurrences(pattern, text)
        if hits:
            findings.append((label, len(hits), hits))

    for word in WORDS:
        pat = r"\b" + re.escape(word).replace(r"\ ", r"\s+") + r"\b"
        skip = WORD_EXCEPTIONS.get(word)
        if skip:
            scrubbed = re.sub(skip, " ", text, flags=re.I)
        else:
            scrubbed = text
        hits = occurrences(pat, scrubbed)
        if hits:
            findings.append((f"jargon: {word}", len(hits), hits))

    arrows = occurrences(UNICODE_ARROW.pattern, text)
    if arrows:
        findings.append(("unicode arrow", len(arrows), arrows))

    advisory = {}
    for word in ADVISORY_ADVERBS:
        n = len(re.findall(r"\b" + word + r"\b", text, re.I))
        if n:
            advisory[word] = n

    return findings, advisory, len(text.split())


def main(paths):
    total_flagged = 0
    for path in paths:
        if not os.path.isfile(path):
            print(f"  SKIP  {path} (not found)")
            continue
        findings, advisory, words = check(path)
        name = os.path.basename(os.path.dirname(path)) or os.path.basename(path)
        print(f"=== {name} ({words} words) ===")
        if not findings:
            print("  CLEAN  no flagged patterns")
        for label, n, hits in findings:
            print(f"  FLAG   {label} x{n}")
            for h in hits:
                print(f"           {h}")
        if advisory:
            total = sum(advisory.values())
            top = ", ".join(f"{k} {v}" for k, v in
                            sorted(advisory.items(), key=lambda x: -x[1])[:6])
            print(f"  note   adverbs {total} (never fails): {top}")
        if findings:
            total_flagged += 1
        print()

    print("=" * 46)
    print(f"  {'CLEAN' if not total_flagged else str(total_flagged) + ' file(s) flagged'}")
    print("=" * 46)
    return 1 if total_flagged else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        args = ["3 Phones Under $250/index.html"]
    sys.exit(main(args))
