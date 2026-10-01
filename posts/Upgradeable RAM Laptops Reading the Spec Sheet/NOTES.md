# Upgradeable RAM Laptops — research notes

## Positioning

The point of this post is **not** to list "good laptops". It is to explain the
one thing buyers get wrong constantly, in a way a search result cannot: how to
tell, from a manufacturer's own documents, whether a laptop has real RAM slots.

The angle is that **each brand words the same hardware differently**, so a
generic "soldered vs socketed" explainer is useless at the point of purchase.
HP in particular ships manuals that describe identical soldered hardware with
opposite-sounding words.

## Keyword / query research (AGENT.md §9, done before the title)

| Candidate query | Words | Question form? | Intent | Verdict |
|---|---|---|---|---|
| `upgradeable ram laptops` | 3 | no | commercial / transactional | **chosen** |
| `laptop ram upgrade` | 3 | no | transactional | too broad, retailer-dominated |
| `laptops with upgradeable memory` | 4 | no | commercial | same page as the chosen one |
| `how to tell if laptop ram is soldered` | 8 | yes | informational | rejected — "how" queries are the highest AI-Overview activation category |
| `can i upgrade my laptop ram` | 6 | yes | transactional | rejected — question form |

Why this query shape: non-question queries trigger an AI Overview far less
often than question-form ones, and "upgradeable RAM" is a buying decision
(commercial/transactional), not a definition. Per AGENT.md §13.2 the slug
carries no year.

### SERP check — is there a real gap?

Checked the top results. What is actually ranking:

- `finalboss.io` — gaming-laptop listicle, 18 models, filterable
- `digitaltrends.com/computing/best-upgradeable-laptops` — dated **2024-01-02**,
  stale, and only lists 5 models
- `whatramfits.com/laptops` — a compatibility database (213 models), not an
  editorial explanation
- Kingston / Lenovo / Best Buy — retail and vendor shop pages
- `computercompatibility.com` — HP ProBook only

Nobody is ranking a **cross-brand explanation of how to read the manufacturer
documents**. That is the gap. Also note the HP support forums are full of
directly contradictory answers on this exact question, including one thread
where the poster reports "opposite answers from HP French customer service".

## Primary sources — everything below is quoted from the vendor's own document

### Lenovo (PSREF — psref.lenovo.com, the spec reference Lenovo uses internally)

The `Memory Slots` field is the authoritative one. Wording is explicit.

| Model | Memory Slots (verbatim) | Max Memory |
|---|---|---|
| IdeaPad Slim 3 15IRH10 | "One memory soldered to systemboard, one DDR5 SODIMM slot, dual-channel capable" | "Up to 24GB (8GB soldered + 16GB SODIMM) DDR5-4800 offering" |
| ThinkPad E14 Gen 6 (Intel) | "Two DDR5 SODIMM slots, dual-channel capable" | "Up to 64GB DDR5-5600" |
| ThinkPad E14 Gen 6 (AMD) | "Two DDR5 SODIMM slots, dual-channel capable" | "Up to 64GB DDR5-4800" — note: "The 64GB memory is for special bid only" |
| ThinkPad L14 Gen 6 (Intel) | "Two DDR5 SODIMM slots, dual-channel capable" | "Up to 64GB DDR5-5600" |
| ThinkPad 11e 5th Gen | "4GB soldered memory, not upgradable" / "8GB soldered memory" | none — page notes "(last verified: 2026-09-02)" |
| IdeaPad Slim 3 15IRH10 (footnote) | "Installed memory is actually DDR5-5600 but runs as DDR5-4800 due to platform limitation" | — |

Note the E14 Gen 6 caveat: PSREF says 64GB, but flags it as
**special-bid-only**, i.e. not something a normal buyer can order or fit. Worth
calling out because a spec sheet alone implies you can.

### HP (Maintenance and Service Guide, kaas.hpcloud.hp.com)

**This is the whole story of the post.** HP describes the *same* physical
arrangement with different words:

| Model | HP's own wording |
|---|---|
| Pavilion 15 Laptop PC | "Two SODIMM memory module slots, **non-customer-accessible/non-upgradable**" |
| HP 15 Laptop PC | "Two SODIMM slots, **not customer accessible or upgradeable**" |
| HP 15 Notebook PC (Win10 gen) | "Two SODIMM **customer-accessible/upgradable** memory module slots" |
| OMEN by HP 15 | "Two SODIMM slots, **customer accessible/upgradeable**", "Supports up to 32 GB" |
| Victus by HP 15.6" (15-fa2xxx/fa3xxx) | "Two memory slots supporting up to 16 GB of RAM", "DDR5-5600 or DDR4-3200" |
| Victus by HP 15.6" (15-fb3xxx, AMD) | "Two memory slots supporting up to 16 GB of RAM", "DDR5-5600" |
| Envy x360 14 (14-fc0xxx) | "The memory is soldered to the motherboard, it cannot be upgraded" |

So "two SODIMM slots" tells you nothing on its own — HP uses it for both
upgradeable and sealed machines, and the only word that separates them is
*customer-accessible*.

The community shorthand for this, from an HP forum answer:
> "Soldered memory is referred to as ONBOARD on HP documentation, so RAM is not
> soldered."

### ASUS (asus.com techspec pages)

ASUS publishes memory in the product spec table, not a service manual.

| Model | Memory (verbatim) | Expansion Slots |
|---|---|---|
| Vivobook 15 (F1502) | "8GB DDR4 on board 8GB DDR4 SO-DIMM Max Total system memory up to:16GB" | "1x M.2 2280 PCIe 4.0x4 **1x DDR4 SO-DIMM slot**" |
| Vivobook 16 (M1607) | "Max Total system memory up to:32GB" | "1x M.2 2280 PCIe 4.0x4 **1x DDR5 SO-DIMM slot**" |
| TUF Gaming A15 (FA506NCR/NCG) | "16GB DDR5-4800 SO-DIMM, Max Capacity:64GB" | "2x M.2 PCIe **2x DDR5 SO-DIMM slots**" |
| TUF Gaming F16 (2025) FX607VU | "**16GB DDR5 on board**, 16GB DDR5-5600 SO-DIMM … Max Capacity:64GB" | "2x M.2 PCIe **2x DDR5 SO-DIMM slots**" |

ASUS's own footnote, which is worth quoting:
> "Memory specification is rated for 5600MHz, but due to a CPU limitation is
> limited to 4800MHz."

Note the two TUF generations differ: the A15 lists only SODIMM, the F16 (2025)
lists on-board memory *plus* SODIMMs. "TUF Gaming" is not one spec.

### Kingston compatibility database (kingston.com/en/memory/search/model/…)

Independent cross-check, phrased as a socket count.

| Model | Kingston wording |
|---|---|
| ThinkBook 14 G6 IRL | "2 Socket(s)", max 64GB |
| TUF Gaming F16 (2024) FX607JU/JV | "2 Socket(s)", max 32GB |
| Vivobook 15 (X1504) | "1 Socket(s)", "4 GB (Non-removable) / 8 GB (Non-removable)", "Maximum 12 GB with 4GB soldered / 16 GB with 8GB soldered" |
| ThinkPad Twist S230u | "0 Slot(s) (Memory soldered to systemboard)" |
| Dell Precision 5690 | "0 Socket(s) for memory" |
| HP OmniBook 5 16 (af1xxx) | "0 Socket(s) for DRAM" |

Kingston's "N Socket(s)" is the cleanest single field for this and it is worth
telling readers it exists — it is the one number that is comparable across
brands, unlike the prose in vendor manuals.

## The check that works without opening the laptop

From ASUS's upgrade guidance and Lenovo support:

> "If Task Manager does not show a 'Slots used' field, or if it shows '0 of 0
> slots,' the RAM is soldered."

Path: `Ctrl+Shift+Esc` → **Performance** → **Memory** → read **Slots used**.

Also documented by HP, for the maximum the board accepts:
> `wmic memphysical get maxcapacity`
> "The capacity is shown in Kilobytes, so you have to convert to Gigabytes by
> dividing the number provided in the report by 1,048,576."

Caveat worth stating honestly: the `Slots used` figure can be wrong on some
firmware, and iFixit forum answers show people being told by Task Manager that
32GB is possible on a machine that is physically sealed. Treat it as a strong
signal, not proof.

## Deliberately NOT included

- **No prices.** This is a reference article, not a roundup. Adding price
  bands would make it stale in a way a spec table is not, and AGENT.md §13.5
  would then require a `checked` date on figures that add nothing to the
  argument.
- **No benchmarks.** Nothing here needs a performance number.
- **Not a "best laptops" list.** That would collide with the site's existing
  roundups and would be an informational query (highest AIO category).

## One topic only (AGENT.md §13.8)

Topic: **how to determine whether a laptop's RAM can be upgraded.** The
vendor-wording table and the Task Manager check are two ways of answering that
one question, not two topics. The M.2 form-factor trap is mentioned only inside
the table notes, not given its own section, because it is a different question.

## Images — Wikimedia Commons, licenses recorded

| File | Author | License |
|---|---|---|
| `images/refs/x220-empty-ram-slots.jpg` | Siarhei Besarab | CC BY-SA 4.0 |
| `images/refs/ddr5-form-factors.jpg` | 4300streetcar | CC BY 4.0 |

Both freely licensed, both show the actual hardware (socketed SODIMM slots /
DDR5 module form factors). Attribution goes in the post footer as
`AGENT.md`/Commons terms require.
