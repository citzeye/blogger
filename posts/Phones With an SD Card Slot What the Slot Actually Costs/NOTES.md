# Phones With SD Card Slot — research notes

## The angle (this is the whole post)

The obvious version of this article is "here are the phones with an SD slot."
Android Central, How-To Geek and Gizmochina all published exactly that in the
last year, and the SERP is full of them. Do not write that article.

The non-obvious finding, which came out of reading the manufacturers' own spec
pages rather than the reviews:

**An SD card slot is not one feature. It is three, sold as a bundle, and they
conflict with each other.**

1. **Extra storage** — the thing people think they are buying.
2. **Storage that apps can live on** — removed from Android in 2019.
3. **A second SIM line** — on many phones, the card slot *is* the second SIM
   slot, and using it for a card means giving up dual-SIM.

Motorola and Samsung both sell "a phone with a microSD slot" right now. On one
you get the card slot *and* two SIMs. On the other the card takes the place of
your second SIM. Both are listed as "expandable storage." Nothing on a spec
sheet tells you which one you are buying.

That is the article. It is a cross-brand structural comparison read from vendor
documents, which is not something a summary can reproduce.

## Keyword research (AGENT.md §9, before the title)

| Candidate | Words | Question? | Intent | Verdict |
|---|---|---|---|---|
| `phones with sd card slot` | 5 | no | commercial | **chosen** — matches how people search |
| `expandable storage phones` | 3 | no | commercial | same intent, weaker brand association |
| `best phones with sd card slot` | 6 | no | commercial | "best" listicle — crowded, and not what this post is |
| `can i add a micro sd card to my phone` | 9 | yes | informational | rejected — question form |

Non-question, 5 words, commercial/buying intent. No year in the slug
(AGENT.md §13.2).

### SERP check

Ranking today: Android Central ("The best Android phones with an SD card slot
2026", Jul 2026), How-To Geek ("Samsung still sells great phones with a MicroSD
slot", Aug 2026), Gizmochina budget list, 91mobiles/Hindustan Times India
filterers, plus a Reddit thread.

All of them answer **"which phones have the slot."** None of them answer **"what
does having the slot actually cost you, and what can it not do."** That is the
gap, and it is a structural one rather than a freshness one — a new post can
compete on it even against a site with more authority.

## Primary sources

### Samsung (samsung.com product pages — the "SIM Slot Type" field)

This field is the entire argument. Verbatim across Samsung's own regional
stores:

| Model | External Storage Support | SIM Slot Type |
|---|---|---|
| Galaxy A27 5G | "MicroSD (Up to 2TB)" | **"SIM 1 + Hybrid (SIM or MicroSD)"** |
| Galaxy A17 5G | — | **"SIM 1 + Hybrid (SIM or MicroSD)"** |
| Galaxy A17 5G (pt store) | — | "SIM 1 + Híbrido (SIM ou MicroSD)" |

Samsung also lists `Number of SIM: Dual-SIM` on the same page — which is how the
same page says both "dual SIM" and "one SIM plus a card slot." Corroborated by
GSMArena: "microSDXC (**uses shared SIM slot**)".

Samsung dropped microSD from the Galaxy S series starting with the S21 (2021);
S20 and earlier had it.

### Motorola (motorola.com US + en-us.support.motorola.com)

Motorola spells out the consequence directly. Verbatim:

| Model | Storage | SIM Card |
|---|---|---|
| moto g (2026) | "128GB built-in … Expand up to 1TB with a microSD card" | **"Dual SIM (1 physical Nano SIM + eSIM + 1 microSD)"** |
| moto g power (2026) | "128GB built-in … up to 1TB microSD card expandable UFS2.2" | **"Dual SIM (1 physical Nano SIM + eSIM + 1 microSD)"** |
| moto g power (2025) | "Up to 1 TB microSD card expandable (sold separately, may not be possible to move content with DRM restrictions)" | same "1 physical Nano SIM + eSIM + 1 microSD" |
| moto g play (2026) | "up to 64GB of built-in UFS 2.2 storage and the option to expand up to 1TB via a **dedicated** microSD card slot" | — |

So Motorola keeps a **dedicated** slot and can therefore afford real dual-SIM.
GSMArena on the Moto G (2026): "microSDXC (**dedicated slot**)", SIM listed as
"Nano-SIM + eSIM".

The moto g power (2026) spec page also notes the DRM caveat: content with DRM
restrictions "may not be possible to move to the card" — which also appears on
motorola.com's own product page footnote.

### The app-storage restriction (Motorola support, repeated verbatim)

On every Moto G support page:

> "Your phone uses the card as **portable storage** for media files: photos,
> videos and music. … **You can't store apps on the SD card because it is
> portable storage.**"

Motorola's general SD help page adds the historical reason:

> "To move apps to your SD card: 1. Make sure it's formatted as internal
> storage. … If you don't see this option, the developer does not allow the app
> to be stored on an SD card."
> "**If you don't see Format as internal, then your phone only supports SD cards
> formatted as portable storage.**"

And its own comparison table:

|  | Portable storage | Internal storage |
|---|---|---|
| Store media | yes | yes |
| **Store apps** | **no** | **yes** |
| Content encrypted | no | yes |
| Read card in other devices | yes | no |

A Tom's Guide forum thread documents the consequence on a Moto G Play (2024):
"starting from Android 10, the ability to format an SD card as internal storage
has been removed." (Android 10 shipped in 2019 — the year the feature died.)

### Sony — the premium exception

Android Police (Jun 2026): "Sony stands out as one of the few major
manufacturers that offer expandable storage in its premium Xperia phones."

### The manufacturers that have never had one

- **Google Pixel** — no Pixel has ever shipped a microSD slot.
- **Apple iPhone** — never.

## What this means for the site's own claims

Cross-check against the existing live posts. The "3 Phones Under $250" post
recommends the Galaxy A17 5G. On Samsung's own spec page that model is
"**SIM 1 + Hybrid (SIM or MicroSD)**" — so a reader in the US who is
dual-SIM today would lose a line buying it. That is worth an honest footnote in
the new post, and it is the kind of caveat a generated summary would never
produce.

## Deliberately NOT included

- **No "best phone with SD slot" picks list.** That is the crowded article, and
  a 3-pick roundup would repeat the site's existing coverage without adding
  anything.
- **No card speed benchmarks.** Not needed for the argument, and would need
  measurement this site does not do.
- **One topic only** (§13.8): what an SD card slot does and does not give you.
  The SIM conflict and the app-storage limit are two consequences of that one
  fact, not separate topics.

## Images — Wikimedia Commons

To be sourced at build time; both must show a real microSD card or a real SIM
tray. Licences recorded in the post footer, as Commons terms require.


---

## EDITOR NOTES (dipindah dari index.html)

SLUG:      /phones-with-sd-card-slot      (NO year)
KEYWORDS:  phone, sd card, microsd, expandable storage, dual sim, samsung, motorola
           motorola, android

NO PRICE LIST, AND DELIBERATELY NOT A "BEST PHONES WITH SD SLOT" ARTICLE.
Android Central, How-To Geek and Gizmochina all published that in the last 12
months and it ranks already. This post answers a different question. See
NOTES.md for the SERP check.

THE THESIS: an SD card slot is three features sold as one, and they conflict.
  1. extra storage
  2. storage apps can live on  — removed from Android in 2019
  3. a second SIM line        — on many phones the card slot IS the SIM slot

EVERY FACT BELOW IS FROM A MANUFACTURER PAGE OR SUPPORT DOC, quoted verbatim.

  SAMSUNG (samsung.com product pages, "SIM Slot Type" field):
    Galaxy A27 5G   External Storage Support "MicroSD (Up to 2TB)"
                    SIM Slot Type  "SIM 1 + Hybrid (SIM or MicroSD)"
    Galaxy A17 5G   SIM Slot Type  "SIM 1 + Hybrid (SIM or MicroSD)"
    The SAME page also says Number of SIM: Dual-SIM — which is how one page
    claims dual SIM and one SIM plus a card. GSMArena: "microSDXC (uses shared
    SIM slot)".
    Samsung dropped microSD from the Galaxy S series with the S21 (2021).

  MOTOROLA (motorola.com US + en-us.support.motorola.com):
    moto g (2026)       "Expand up to 1TB with a microSD card"
                        SIM Card "Dual SIM (1 physical Nano SIM + eSIM + 1 microSD)"
    moto g power (2026) "up to 1TB microSD card expandable UFS2.2"
                        SIM Card "Dual SIM (1 physical Nano SIM + eSIM + 1 microSD)"
    moto g play (2026)  "...expand up to 1TB via a DEDICATED microSD card slot"
    GSMArena on Moto G (2026): "microSDXC (dedicated slot)"
    moto g power (2026) footnote: "may not be possible to move content with DRM
                        restrictions"
    So Motorola keeps a dedicated slot, and can afford real dual-SIM as well.

  THE APP LIMIT (Motorola support, repeated on every Moto G page):
    "Your phone uses the card as PORTABLE STORAGE for media files: photos,
     videos and music. ... YOU CAN'T STORE APPS ON THE SD CARD because it is
     portable storage."
    And on formatting: "If you don't see Format as internal, then your phone
     only supports SD cards formatted as portable storage."
    Motorola's own comparison table:
                       Portable | Internal
      Store media         yes    | yes
      Store apps          NO     | yes
      Content encrypted   no     | yes
      Read in other devs  yes    | no

  ANDROID 10 (2019) is when internal-storage formatting was removed. A Tom's
  Guide thread records the user-visible consequence on a Moto G Play (2024):
  "starting from Android 10, the ability to format an SD card as internal
  storage has been removed."

  NEVER HAD ONE: no Google Pixel has ever shipped a microSD slot. No iPhone
  has either.
  PREMIUM EXCEPTION: Sony still offers it on Xperia (Android Police, Jun 2026).

HONEST CROSS-CHECK AGAINST OUR OWN SITE: the live "3 Phones Under $250" post
recommends the Galaxy A17 5G. Samsung's own page lists that model as
"SIM 1 + Hybrid (SIM or MicroSD)", so a dual-SIM reader would lose a line. That
caveat is in the body text below rather than left for a reader to discover.
