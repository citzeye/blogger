# Top 3 Midrange Gaming Phones

Working notes. Not published. `index.html` is the only file that gets pasted.

```
SLUG:      /midrange-gaming-phones      (NO year)
KEYWORDS:  gaming, phone, midrange, snapdragon

THE THESIS, which everything else hangs off:
  "Gaming phone" used to mean a flagship chipset in a cheaper body. That
  category is gone. What replaced it is a normal midrange phone with one good
  chip. The consequence worth writing about is that a ~$500 phone and a ~$750
  phone are now much closer in gaming performance than the price gap implies,
  because the chipset available at the low end is already last year's top tier.

  THE HONEST CAVEAT, stated in the intro rather than buried: only two of the
  three picks are really gaming phones. In the US there is no third dedicated
  midrange gaming handset at this price. Slot three is the Pixel 10a, labelled
  as the all-rounder it is. Three slots, three real prices, no padding - and
  the list being short is itself the finding, not a failure to fill it.

SPECS - every one sourced, and this is the section to re-check:
  OnePlus 13R
    Snapdragon 8 Gen 3 (flagship silicon, previous generation)
    6.78in LTPO AMOLED, 120Hz, 450ppi, 4500 nits peak, Gorilla Glass 7i
    12/16 GB RAM, 256/512 GB, UFS 4.0
    6,000 mAh, 80W, 50% in 20 min, 100% in 52-54 min
    206 g
    Source: HT Tech full spec sheet; GSMArena; Android Central rates it
    "best midrange phone" and confirms UFS 4.0 as faster than the 12R.
    WHY UFS 4.0 IS CALLED OUT TWICE: storage speed, not the chip, is what
    prevents mid-match asset stalls. It is the least advertised spec in the
    category and the one most felt.

  Nothing Phone (4a) Pro
    6.83in AMOLED, 144Hz  <- the highest refresh here
    Snapdragon 7 Gen 4
    8 GB / 128 GB
    5,080 mAh, 50W, 100% in ~64 min
    210 g, aluminium unibody
    50MP Sony main + 50MP 3.5x periscope + 8MP ultrawide
    6 years security / 3 years OS
    Source: Gizmochina; Billboard review; PhoneArena; Android Police for the
    5,080 mAh figure (two sources agree on that number).
    NO wireless charging. The Pixel 10a does have it, which is the one
    hardware point where the cheaper phone wins.

  Google Pixel 10a
    6.3in P-OLED, 120Hz
    Tensor G4  <- weakest chip on the list, and the article says so
    8 GB / 256 GB
    5,100 mAh, 45W, wireless charging
    183 g, plastic back
    7 years of security AND OS updates
    Source: Gizmochina; Android Police; gadgetsnow spec sheet.
    FRAMED HONESTLY: this is not a gaming pick. It occupies the third slot
    because in the US there is no third dedicated midrange gaming phone at
    this price, and pretending otherwise would be padding the list.

PRICES - all three now verified. USD, US market, checked September 2026:

  OnePlus 13R             $549.99 live, $599.99 list, $499 promo
    AUTHORITATIVE: the JSON-LD product block on oneplus.com/us/oneplus-13r
    reads "price": "549.99", "priceCurrency": "USD",
    "priceValidUntil": "2026-12-31", availability InStock.
    CORRECTION WORTH RECORDING: search snippets and the site's own hero
    banner both said "$499.99", and Android Central / Tom's Guide /
    PhoneArena all repeat $499 because they were reporting a promotion.
    A promo snapshot is not the live price. The card therefore shows $549,
    and the article says $499 is the sale price and $599.99 the ceiling.
  Nothing Phone (4a) Pro  $499 at launch, ~$449 on sale
    Billboard ("starting at $499 and topping out at $599"),
    PhoneArena Jun 2026 ("costs $499"), Smartprix US price list Sep 5 2026
    ($449; 12/256 variant $539)
    Note the model is on Best Buy shelves as of Jun 2026, so $499 is real
    street pricing rather than a launch-day figure that never stuck.
  Google Pixel 10a        $499
    Gizmochina spec and price listing.

  CONFLICT RESOLVED, NOT HIDDEN:
    GSMArena lists the 13R at "$799.99 / GBP 599.99". The $799.99 is an
    aggregator error - OnePlus's own US store says $599.99 list, and no US
    retailer has ever listed it at $800. Manufacturer beats aggregator. The
    article quotes $499-599 and does not repeat the $799 figure.

  CANDIDATE CUT AFTER CHECKING, NOT AFTER GUESSING:
    OnePlus Nord CE 6 5G was in an earlier draft at ~$300-350. It is out,
    because it fails the availability test:
      - Times of India headline: "OnePlus launches Nord CE6 and Nord CE6
        Lite in India"
      - every price found was in rupees (Rs 27,999-37,999)
      - oneplus.com/us lists only OnePlus 13, 13R, 12, Open and Nord N30 5G
      - Roamix: "Nord models are rarely sold in the US"
    This is exactly the failure that got the Indonesian phones removed from
    the budget article, caught before publish instead of after.

  NO UK FIGURES PUBLISHED. GSMArena shows a GBP figure for the 13R and
  OnePlus does run a UK store, but a single aggregator price is not enough to
  quote as UK pricing. Article is US/USD throughout.

CONTEXT CLAIM USED IN THE PIECE:
  "A current-generation flagship now sits around $700." Supported by the
  MobileRank midrange table (which defines midrange as $400-$800 and lists
  Snapdragon 8 Elite Gen 5 phones from $599 to $799) and by WIRED listing the
  Galaxy A37 at $433. Stated as "around $700", not a precise figure.

DELIBERATELY NOT INCLUDED:
  - No frames-per-second figures for any of the three. None were measured from
    a source, and guessed FPS numbers are the most common lie in gaming phone
    articles.
  - No Poco X7 Pro or Redmagic. The Poco X7 Pro is the classic midrange gaming
    value pick, but it is not officially sold in the US, so it fails the same
    test that removed the Indonesian phones from the budget article.
  - No gaming triggers, bypass charging, or RGB. None of these phones has them,
    and pretending otherwise would be the old "AI laptop" label problem in a new
    outfit.
  - No benchmark scores compared across chips, since one chipset is unknown.

IMAGES:
  ONE image per post, uploaded to Blogger's own media library so
  data:post.thumbnailUrl picks it up. Blogger only generates a post thumbnail
  from an image hosted on blogger.googleusercontent.com. Any other host leaves
  it EMPTY: the homepage card renders with no picture and og:image goes missing.

  UPLOAD STEPS:
    1. Whitelist blogger.com in Brave first. Shields silently fails the upload
       otherwise, with no error shown.
    2. New post -> HTML view -> paste the body from index.html
    3. Insert image (toolbar, NOT right-click, NOT Compose) -> Upload files
    4. Fix the alt text. Blogger's dialog writes alt="" and wraps the image in
       an <a href> pointing at the image file itself.
    5. Strip the wrapper: no <a>, no <div class=separator>, no border=, no
       inline style=. Keep width="1600" height="1067".
    6. Fill Blogger's Title field.

  Blogger caps an image at 1600px on its LONGEST side, so a /s1600/ URL comes
  back downscaled. Use /s0/ for full resolution.

  Build with:  python3 posts/make-phone-images.py "Top 3 Midrange Gaming Phones"
  It needs three product photos in images/refs/ and refuses to render without
  them. Pass --no-photos for a layout-only preview.
```


---

## EDITOR NOTES (dipindah dari index.html)

SLUG:      /midrange-gaming-phones      (NO year)

PRICES - all verified, USD, US market, checked September 2026:
  OnePlus 13R             $549.99 live on oneplus.com/us, $599.99 list,
                          Amazon promos seen at $499
                          (the $549.99 is the manufacturer's own JSON-LD
                           price field, valid until 2026-12-31)
  Nothing Phone (4a) Pro  $499 at launch, ~$449 on sale
                          (Billboard $499, PhoneArena $499,
                           Smartprix US $449)
  Google Pixel 10a        $499  (Gizmochina)

  A FOURTH CANDIDATE WAS CUT: OnePlus Nord CE 6 5G. Times of India reported
  its launch "in India", every price found was in rupees, and oneplus.com/us
  does not list it. It fails the same US/UK availability test that removed the
  Indonesian phones from the budget article.

  SOURCED BUT NOT USED: GSMArena lists the OnePlus 13R at "$799.99". That is
  an aggregator error - OnePlus's own US store says $599.99 list. Where a
  manufacturer and an aggregator disagree, the manufacturer wins.
