# Slop catalog — adapted from Stephen D. Turner's `skill-deslop`

Provenance, because this has to be attributed correctly:

- Source: `skill-deslop` by **Stephen D. Turner**, MIT licensed, © 2026.
  Repository: `github.com/stephenturner/skill-deslop`
- Vendored into OpenSEO (`github.com/every-app/open-seo`) under
  `.agents/skills/deslop/`. OpenSEO is not the author; credit Turner.
- Upstream files consulted: `SKILL.md`, `references/phrases.md`,
  `references/structures.md`, `references/tropes.md`, `references/examples.md`.

## What was changed on adaptation, and why

This is not a copy. Four deliberate edits:

1. **Scientific-writing guidance removed.** Upstream splits advice for journal
   prose and blog prose. This catalog only covers the blog voice, because that
   is the only register this site publishes in.
2. **The two formatting bans dropped: em dashes and bold-first bullets.**
   Upstream bans both. They are house style here, and one of them is load-
   bearing. See "Deliberate exclusions" below.
3. **"No adverbs" downgraded to advisory.** Upstream says kill all `-ly` words.
   Measured against the ten published posts, `actually` appears 28 times across
   the corpus and reads as "in fact" every time. A rule that fires on correct
   writing is a rule that gets ignored, so adverbs are counted, not failed.
4. **Literal senses added as exceptions.** Upstream bans `landscape` outright.
   This site writes about screen orientation and photo orientation, where
   "landscape" is the correct technical term.

## Deliberate exclusions — do not "fix" these

These are house style or functional. A checker that flags them is wrong.

| Pattern | Why it stays |
|---|---|
| Em dash `—` | 136 uses across the published posts, and the template and `AGENT.md` both rely on it. It is the site's punctuation, not a tic. |
| `<li><strong>Label</strong> — value` | 115 uses, and the majority are reference fields: `Processor:` 9x, `Display:` 9x, `Price:` 9x, `Memory:` 8x, `Battery:` 6x, `Storage:` 5x. This is scannable spec data, which is the whole point of these articles. Upstream's target is a rhetorical tic in flowing prose, which is a different thing. |
| `landscape` meaning a photo or screen orientation | Correct technical usage on this site. |
| `actually` meaning "in fact" | 28 uses in the corpus, all idiomatic. |
| Bold labels inside `<table>` | Data presentation, not prose. |
| One point argued twice | Upstream allows a thesis to land twice before cutting. That limit holds. |

## Level 1 — phrases with no legitimate technical use

Delete on sight. `slop-check.py` fails these.

**Throat-clearing openers**
"Here's the thing" · "Here's the kicker" · "Here's what most people miss" ·
"Here's the deal" · "Here's where it gets interesting" · "The uncomfortable
truth is" · "It turns out" · "Let me be clear" · "Can we talk about"

**Emphasis crutches** (add no meaning)
"Let that sink in" · "Full stop" · "Make no mistake" · "This matters because"

**Pedagogical hand-holding**
"Let's break this down" · "Let's unpack" · "Let's explore" · "Let's dive in" ·
"Think of it as" · "Think of it like" · "Imagine a world where"

**Filler transitions**
"It's worth noting" · "It bears mentioning" · "At the end of the day" ·
"At its core" · "In today's" · "When it comes to" · "The reality is" ·
"In a world where" · "Notably"

**Meta-commentary** (the text should move, not announce itself)
"Plot twist" · "Spoiler:" · "You already know this, but" · "But that's another
post" · "The rest of this essay explains" · "Let me walk you through" ·
"In this section, we'll" · "As we'll see" · "I want to explore" ·
"In conclusion" · "To sum up" · "In summary" · "As we've seen in this section" ·
"And so we return to where we began"

**Self-certifying candor** — announce the honesty instead of being precise
"the honest answer" · "the honest framing" · "the most honest signal" · "an
honest forecast"
Do not swap in "realistic", "candid", "clearest" or "most reliable" — those are
the same failure. State the evidence, the limitation, or the uncertainty
directly.

**Vague attributions** — if you cannot name the source, you do not have one
"Experts argue" · "Industry reports suggest" · "Observers have cited" ·
"Several publications have noted"

**Vague declaratives** — announce importance without naming the thing
"The reasons are structural" · "The implications are significant" · "This is the
deepest problem" · "The stakes are high" · "The consequences are real"

**Participial analysis** — hollow significance-signalling on the end of a sentence
"highlighting its" · "underscoring its" · "reflecting broader trends" ·
"contributing to" · "showcasing"

**Formulaic dismissal** — name the problem, then wave it away
"Despite these challenges" · "Despite its challenges"

## Level 2 — vocabulary with a plain replacement

Fail these too. `slop-check.py` matches word-boundary, case-insensitive.

| Avoid | Use instead |
|---|---|
| delve | examine, look at, explore |
| tapestry | mix, combination, range |
| nuanced | complex, subtle, specific |
| navigate the challenges | handle, address |
| unpack | explain, examine |
| lean into | accept, embrace |
| game-changer | significant, important |
| double down | commit, increase |
| deep dive | analysis, examination |
| circle back | return to, revisit |
| take a step back | reconsider |
| moving forward | next, from now |
| on the same page | aligned, agreed |
| leverage (verb) | use |
| utilize | use |
| robust | strong, solid |
| streamline | simplify |
| harness | use, apply |
| paradigm | model, approach |
| synergy | cooperation, combined effect |
| ecosystem | system, field, community |
| serves as | is |
| stands as | is |
| represents (meaning "is") | is |

Also fail: `quietly`, `remarkably`, `arguably`. "Quietly" is the single most
overrepresented adverb in machine-generated prose.

## Level 3 — structural patterns, judgment required

`slop-check.py` cannot reliably grep these. Read for them.

**Binary contrast** — "Not X. Y." / "Not a X. Not a Y. A Z." State Y directly.

**Dramatic fragmentation** — "Speed. That's it. That's the tradeoff." Stacking
short sentences to manufacture weight.

**Self-posed rhetorical question** — a question asked and answered in the next
clause. Fold it into a statement.

**Tricolon** — three-item lists are the machine default. Use two, or one.

**Anaphora abuse** — repeating a sentence opener to manufacture rhythm.

**False agency** — inanimate things doing human verbs. "The complaint becomes a
fix" is wrong; "the team fixed it" is right. If no person fits, use "we".

**Narrator from a distance** — "It has long been recognized that." For this
site, cut it and name the source.

**Listicle in a trench coat** — "The first wall is... The second wall is..."
numbering points while pretending to be prose. If it is a list, make it a list.

**False ranges** — "From innovation to implementation to cultural
transformation." No real spectrum between the ends. If it is a list, list it.

**Historical analogy stacking** — "Apple didn't build Uber. Facebook didn't build
Spotify." One example examined properly beats five name-drops.

**Invented concept labels** — compound labels with a problem-noun bolted on,
used as if established: "the supervision paradox", "the acceleration trap",
"workload creep". If the concept needs a name, define it; otherwise describe it
in plain words.

**Lazy extremes** — every, always, never, everyone, nobody, doing vague work.
Replace with the specific case.

**One-point dilution** — restating one argument in ten framings. If the piece
circles the same claim more than twice, cut.

**Dead metaphor** — one metaphor used in five to ten paragraphs. Use it once or
twice.

**Fractal summary** — telling the reader what you are about to say, saying it,
then summarizing what you said.

**Signposted conclusion** — "In conclusion", "To sum up". Let it conclude.

**Wh- openers as a crutch** — sentences starting What, When, Where, Which, Who,
Why, How. "What makes this hard is" becomes "The constraint is". This one needs
a caveat: this site publishes how-step instructions and specification prose, so
lead with the verb instead of restructuring the sentence.

## Scoring, for review passes

Rate 1-10 on each. Below 35 of 50, revise.

| Dimension | Question |
|---|---|
| Directness | Statements, or announcements? |
| Rhythm | Varied, or metronomic? |
| Trust | Respects the reader's intelligence? |
| Authenticity | Sounds like a specific person wrote it? |
| Density | Anything cuttable? |
