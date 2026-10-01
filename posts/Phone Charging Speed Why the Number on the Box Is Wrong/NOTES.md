# Phone Charging Speed — research notes

## The angle

The obvious version: "fastest charging phones 2026." Rejected — pure spec
leaderboard, no defensible ground, and it goes stale on every launch.

The version worth writing is about **the number on the box being the wrong
number**, and it is not a contrarian take. It is documented, by the
manufacturer, in the manufacturer's own words.

Three separate traps, all from primary sources:

1. **Wattage is region-dependent on the same model.** OnePlus's US page says
   55W, its global page says 80W, its own spec page says 80W.
2. **The phone is not the limit — the brick is.** The Pixel 10a is a 30W phone
   that Google tells you to charge with a 45W charger, sold separately.
3. **There may be no brick at all**, and what you already own may not do the
   wattage the phone is capable of.

That third point is the one readers actually get wrong, and it is the reason
"80W phone" and "fast phone" are different claims.

## Keyword research (AGENT.md §9, before the title)

| Candidate | Words | Question? | Intent | Verdict |
|---|---|---|---|---|
| `phone charging speed` | 3 | no | commercial | **chosen** |
| `does my phone need a specific charger` | 7 | yes | informational | rejected — question form |
| `why is my phone charging slow` | 6 | yes | troubleshooting | rejected — question form |
| `usb c charger wattage phone` | 4 | no | commercial | same territory |
| `fastest charging phone` | 3 | no | commercial | leaderboard, rejected |

Noun phrase, 3 words, buying intent. No year in the slug (§13.2).

## Primary sources

### The OnePlus contradiction (oneplus.com, three pages, same handset)

| Page | Says |
|---|---|
| `oneplus.com/us/13r` (US store) | "Amp up your power with the **55W** SUPERVOOC charging." / "1-50% in **23** mins" / footnote "Up to 80W with OnePlus SUPERVOOC 80W Dual Ports GaN Power Adapter or OnePlus SUPERVOOC 100W Dual Ports Power Adapter" |
| `oneplus.com/global/13r` | "Amp up your power with the **80W** SUPERVOOC charging." / "1-50% in **20** mins" |
| `oneplus.com/no/13r/specs` (spec sheet) | "Charge: **80W SUPERVOOC™**" |
| `oneplus.com/in/13r/specs` | "Charge: **80W SUPERVOOC™**"; "In The Box: OnePlus 13R SUPERVOOC Power Adapter Type-A to C Cable" |

This is the article in one row. The US marketing page leads with 55W. The
regional spec sheet for the identical handset says 80W. The 80W figure is real
but conditional — OnePlus's own footnote says it needs a GaN adapter you buy
separately.

CNET (Jan 2025) states the mechanism plainly:
> "The phone can charge at 55W speeds using the included SuperVooc power adapter,
> although a OnePlus representative said it can support 80W and 100W speeds,
> however you'll have to buy those SuperVooc charger models separately. **Over the
> more widely available USB-PD standard, it can charge at 18W speeds.**"

GSMArena's review concurs:
> "The handset supports up to 80W of fast charging over the proprietary SuperVOOC
> standard, so you'd have to buy a charger separately."

That 18W figure is the one that matters most to a reader in the US or UK with a
third-party charger on the desk, and it appears in almost no summary.

### OnePlus box contents (oneplus.com/in/13r/specs)

> "In The Box — OnePlus 13R SUPERVOOC Power Adapter / Type-A to C Cable / Quick
> Start Guide / Protective Case / SIM Tray Ejector"

And oneplus.com/us/charging, on why:
> "Your charger is always included in the box."

### Google Pixel 10a (store.google.com — the official spec page)

> "Fast charging – up to 50% in about 30 minutes – using **45W USB-C® PPS
> charger or higher, sold separately**"
> "Wireless charging (Qi-certified)"
> "What's in the box — Pixel 10a / 1 m USB-C® to USB-C® cable (USB 2.0) / SIM
> tool"

So: a 30W phone (Wikipedia/PhoneArena: "Charging: 30W wired, 10W Qi"), no brick,
and an instruction to use a 45W charger. Note the direction of the oddity —
the phone is 30W and the recommended brick is 45W, because the charger supplies
headroom and the phone draws what it can.

Corroborated by the Pixel 9a comparison (Ars Technica, Feb 2026): 23W wired /
7.5W wireless on the 9a → **30W wired / 10W wireless on the 10a**. Google raised
it and still calls it a budget phone.

### Why the brick left the box

Samsung UK support page, on the Galaxy S21 onward:
> "Samsung discovered that many Galaxy users are reusing earphones and chargers
> that they already have at home even after purchasing a new phone. Our past
> models already have standardised chargers, and these chargers are widely
> available at home."
> "Note: In-box items may vary depending on the model or the country or region
> you live in."

That last note matters for a US/UK site: box contents vary **by region**, not
just by model.

Samsung dropped the brick from the S series with the S21 (2021) and extended it
to the A series with the A33/A53/A73 in 2022 (SamMobile). Google said the Pixel
5a would be the last Pixel with a brick (The Verge, Aug 2021). Apple first, in
2020.

The packaging numbers, from Uniqbe via BGR (Mar 2026):
> "companies could reduce the amount of necessary packaging materials per
> smartphone box by **50%**, meaning thinner boxes. These thinner boxes allow
> manufacturers to stuff more phones onto shipping pallets (**70% more**)."

### Wireless, for contrast

- Nothing Phone (1): "33W wired, PD3.0, QC4 … 15W wireless … 5W reverse wireless"
  (GSMArena)
- OnePlus 12 / 10 Pro / 9 Pro: 50W wireless; OnePlus 8 Pro: 30W
  (ChargerLAB, from OnePlus official info)
- Pixel 10a: 10W Qi, and Ars Technica notes "**There are no Qi2 magnets
  inside**"

## Structure the post will take

1. The wattage on the box is a ceiling, not a promise — with the OnePlus 13R
   three-page contradiction as the worked example.
2. Your phone is not the bottleneck. The charger is — with 80W→18W over generic
   USB-PD as the concrete number.
3. Sometimes there is no charger, and what you own may be 20W.
4. What "45W charger or higher" actually means (the Pixel 10a line).
5. What to buy if you need to buy something — and the answer is usually the
   cheapest 100W USB-C PD brick, not the proprietary one.
6. Wireless is a different trade, and mostly a slower one.

## Deliberately NOT included

- **No "fastest charging phone" leaderboard.** It goes stale every launch and
  the site already has roundups.
- **No charging-time measurements.** This site does not lab-test; every number
  here is a manufacturer claim, and the post says so rather than implying it
  measured anything.
- **No prices for chargers.** Would need a `checked` date and would rot; the
  advice is "any 100W USB-C PD brick", which does not need a price.

## One topic (§13.8)

Topic: **why a phone's advertised charging speed is not what you will get, and
what to do about it.** Regions, bricks and wattage are three aspects of that one
question.


---

## EDITOR NOTES (dipindah dari index.html)

SLUG:      /phone-charging-speed      (NO year)
KEYWORDS:  phone, charging, wattage, charger, adapter, oneplus, pixel
           pixel

NO CHARGER PRICES. The advice is "any 100W USB-C PD brick", which needs no
price and does not rot. See NOTES.md.

NO "FASTEST CHARGING PHONE" LEADERBOARD. That is a spec table that goes stale on
every launch, and the site already has roundups.

THE THESIS: a phone's advertised wattage is a ceiling, not a prediction. Three
things stand between you and that number, all documented by the manufacturers.

EVERY FACT BELOW IS FROM A MANUFACTURER PAGE OR A NAMED OUTLET, quoted.

  1. WATTAGE VARIES BY REGION ON THE SAME MODEL. OnePlus's own pages disagree:
       oneplus.com/us/13r      "Amp up your power with the 55W SUPERVOOC
                               charging."  /  "1-50% in 23 mins"
       oneplus.com/global/13r  "Amp up your power with the 80W SUPERVOOC
                               charging."  /  "1-50% in 20 mins"
       oneplus.com/no/13r/specs and oneplus.com/in/13r/specs
                               "Charge: 80W SUPERVOOC"
     And the footnote on the US page that explains it:
       "Up to 80W with OnePlus SUPERVOOC 80W Dual Ports GaN Power Adapter or
        OnePlus SUPERVOOC 100W Dual Ports Power Adapter"

  2. THE BRICK IS THE LIMIT, NOT THE PHONE. CNET, Jan 2025:
       "The phone can charge at 55W speeds using the included SuperVooc power
        adapter, although a OnePlus representative said it can support 80W and
        100W speeds, however you'll have to buy those SuperVooc charger models
        separately. OVER THE MORE WIDELY AVAILABLE USB-PD STANDARD, IT CAN
        CHARGE AT 18W SPEEDS."
     GSMArena's 13R review agrees: "The handset supports up to 80W of fast
     charging over the proprietary SuperVOOC standard, so you'd have to buy a
     charger separately."

  3. THERE MAY BE NO BRICK, AND A PHONE CAN ASK FOR MORE THAN IT USES.
       store.google.com Pixel 10a spec page:
         "Fast charging - up to 50% in about 30 minutes - using 45W USB-C PPS
          charger or higher, SOLD SEPARATELY"
         "What's in the box: Pixel 10a / 1 m USB-C to USB-C cable (USB 2.0) /
          SIM tool"
       So a 30W phone (Wikipedia/PhoneArena: 30W wired, 10W Qi) ships with no
       brick and asks for a 45W one. Ars Technica Feb 2026 confirms the step up
       from the 9a: 23W wired / 7.5W wireless -> 30W wired / 10W wireless.

  ONEPLUS BOX CONTENTS, oneplus.com/in/13r/specs:
    "In The Box - OnePlus 13R SUPERVOOC Power Adapter / Type-A to C Cable /
     Quick Start Guide / Protective Case / SIM Tray Ejector"
  oneplus.com/us/charging: "Your charger is always included in the box."

  WHY THE BRICK LEFT (Samsung UK support page, Galaxy S21 onward):
    "Samsung discovered that many Galaxy users are reusing earphones and
     chargers that they already have at home even after purchasing a new phone."
    "Note: In-box items may vary depending on the model or the country or
     region you live in."   <- region matters, not just model
  Samsung dropped it at the S21 (2021), extended to A33/A53/A73 (2022).
  Google said the Pixel 5a would be the last Pixel with a brick (Verge, 2021).
  Apple first, in 2020.
  Packaging effect, Uniqbe via BGR Mar 2026: "50%" less packaging per box,
  "70% more" phones per pallet.

  WIRELESS, for contrast:
    Nothing Phone (1), GSMArena: "33W wired, PD3.0, QC4 ... 15W wireless ...
      5W reverse wireless"
    OnePlus 12 / 10 Pro / 9 Pro: 50W wireless; OnePlus 8 Pro: 30W
      (ChargerLAB, from OnePlus official info)
    Pixel 10a: 10W Qi. Ars Technica: "There are no Qi2 magnets inside."

NOTHING HERE WAS MEASURED BY US. Every charge time is a manufacturer claim and
the post says so. This site does not lab-test batteries.
