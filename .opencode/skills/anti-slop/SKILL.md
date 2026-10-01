---
name: anti-slop
description: Remove predictable AI-writing patterns from post prose. Use when drafting, editing, or reviewing any post in posts/, or when asked to deslop, de-AI, "make it sound human", remove AI patterns or filler, or check whether prose reads as machine-written. Runs before a post is committed. Catalog at references/catalog.md; mechanical check via posts/slop-check.py.
---

# Anti-slop

The site publishes articles arguing that spec-sheet numbers mislead and that AI
content has recognisable failure modes. If the prose of those articles carries
the patterns they analyse, the argument does not survive contact with the
reader. This skill exists to stop that happening quietly.

## Run the checker first

```sh
python3 posts/slop-check.py "posts/<Post Folder>/index.html"
```

It prints the offending phrase with surrounding context, grouped by pattern
type. Exit 0 means clean, 1 means flagged. Run it again after editing until
clean. `slop-check.py` is mechanical; it catches phrases, not judgement.

Then read the prose for the structural patterns below, which no grep can catch.

## What the checker catches

Phrases with no legitimate technical use, and vocabulary with a plain
replacement. Full catalog and the reasoning behind each rule:
`references/catalog.md`.

- Throat-clearing openers — "Here's the thing", "It turns out"
- Emphasis crutches — "Let that sink in"
- Pedagogical hand-holding — "Let's break this down", "Think of it as"
- Filler transitions — "It's worth noting", "At its core"
- Meta-commentary — "In this section, we'll", "In conclusion"
- Self-certifying candor — "the honest answer"
- Vague attribution — "Experts argue", "Research shows"
- Vague declaratives — "The implications are significant"
- Participial analysis — "highlighting its", "underscoring its"
- Formulaic dismissal — "Despite these challenges"
- The "serves as" dodge
- Jargon — delve, tapestry, nuanced, leverage, robust, harness, synergy, paradigm
- Unicode arrows

## What the checker does not catch, and will not

Read for these yourself:

- **Binary contrast** — "Not X. Y." State Y directly.
- **Dramatic fragmentation** — stacking short sentences to manufacture weight.
- **Self-posed rhetorical question** — asked then answered in the next clause.
- **Tricolon** — three-item lists are the machine default. Use two.
- **Anaphora abuse** — repeating a sentence opener for rhythm.
- **False agency** — inanimate things doing human verbs. "The team fixed it", not
  "the complaint becomes a fix".
- **Narrator from a distance** — "It has long been recognized that".
- **Listicle in a trench coat** — "The first... The second..." dressed as prose.
- **False ranges** — "From innovation to implementation to transformation."
- **Historical analogy stacking** — "Apple didn't build Uber. Facebook didn't
  build Spotify." One example examined beats five name-drops.
- **Invented concept labels** — "the supervision paradox", "workload creep".
- **Lazy extremes** — every, always, never doing vague work.
- **One-point dilution** — one argument in ten framings. More than twice is a cut.
- **Dead metaphor** — one metaphor across five to ten paragraphs.
- **Fractal summary** — say what you are about to say, say it, then summarise it.
- **Rhythm** — three consecutive sentences of the same length means one is wrong.

## Three rules this site deliberately does not follow

Do not "fix" these. Each was measured against the published corpus and each one
would damage correct writing. Details in `references/catalog.md`.

1. **Em dashes are house style.** 136 uses across the published posts, and the
   template and `AGENT.md` both depend on them.
2. **Bold-first bullets are load-bearing.** 115 uses, mostly spec fields:
   `Processor:` 9x, `Display:` 9x, `Price:` 9x. Scannable reference data is the
   point of these articles.
3. **`actually` and `quietly` are counted, never failed.** `actually` means "in
   fact" in all 28 corpus uses. `quietly` has a live adverbial sense — "two of
   them quietly cost you something else" — and two of its three corpus hits were
   that sense. A rule that fires on correct writing is a rule that gets ignored.

## Review scoring

For a full pass rather than a spot check, rate 1-10 on each. Below 35 of 50,
revise.

| Dimension | Question |
|---|---|
| Directness | Statements, or announcements? |
| Rhythm | Varied, or metronomic? |
| Trust | Respects the reader's intelligence? |
| Authenticity | Sounds like a specific person wrote it? |
| Density | Anything cuttable? |

## Attribution

Catalog adapted from `skill-deslop` by **Stephen D. Turner**, MIT, (c) 2026,
`github.com/stephenturner/skill-deslop`. Vendored in OpenSEO
(`github.com/every-app/open-seo`). Credit Turner, not OpenSEO.
