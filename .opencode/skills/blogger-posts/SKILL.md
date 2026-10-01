---
name: blogger-posts
description: "Rules for writing, editing, publishing and illustrating posts for the citzeye.blogspot.com tech blog - US/UK audience, USD pricing, English slugs, Blogger Title-field semantics, real-product-photo graphics. Use when touching citzeyeblogspot.xml, AGENT.md, or anything under posts/."
license: "project"
compatibility: "opencode"
metadata:
  project: "citzeyeblogspot"
  blog: "citzeye.blogspot.com"
---

# Blogger posts — citzeye.blogspot.com

**First action, always: read `AGENT.md` at the repo root.** It is the 288-line
playbook (SEO, Core Web Vitals, responsive, evergreen, anti-patterns).
Everything below is either (b) the site's fixed identity, or (c) a mistake
actually made, so each rule carries its known failure.

---

## 1. Site identity — fixed, do not re-litigate

| | |
|---|---|
| Audience | **US and UK readers** (English-speaking) |
| Language | **US English** — `lang='en-US'`, `og:locale='en_US'` |
| Currency | **USD** (`$`) |
| Niche | phones, computers, hardware — **not** "reviews" |
| Post type | evergreen, no year in title or slug |

**Never describe the audience as "Western".** Say **US and UK**. They are two
markets with different retailers, prices, plug types, and spelling. Vague
shorthand hides exactly the detail that matters when choosing products.
*Mistake made:* wrote "Western readers" in the first draft of these rules
after being told the target was US/UK.

### Currency: USD, never IDR

- Prices in body text, tables, graphics, and alt text: **USD**.
- Slugs carry the unit: `/best-phone-under-usd-200`, not `/best-phone-under-200`.
- **Never** write `IDR`, `Rp`, or `juta` in a title, slug, meta description, or
  heading on this site.
  *Mistake made:* first article was titled "5 Phones Worth Buying Under IDR 2
  Million", slug `/best-phone-under-2-juta` — Indonesian currency and an
  Indonesian numeral word, on an English site aimed at US/UK readers.
- For UK readers, add a GBP figure in the **price line** when the UK price
  differs materially. GBP never appears in the title or slug; USD is the site's
  anchor currency.

### Products must be buyable by the reader

- A US/UK reader must be able to buy it and verify the price.
- Check availability in **both** US and UK retailers. A US-only model does not
  work for a UK reader and vice versa.
- Fine: Galaxy A16, Redmi Note 14 Pro, Moto G Power, Pixel 8a, Nothing Phone
  (2a) — all sold in both markets.
- Do NOT use: Tecno Spark Go 3, Infinix Hot 60i, and other Indonesian-only
  models. They have no US/UK street price the reader can check, which makes the
  article un-actionable.
- UK-specific: plug type G, UK retailers (Amazon UK, Argos, Currys, Phones 4U),
  and UK warranty terms.
- §13.5 still applies: quote a **range**, plus a "checked on <Month Year>" line.
  A bare absolute price is an anti-pattern.

### Language: US English, always

The site is **US English**, not generic "English" and not UK English. Spell US
variants in every part of a post — body, headings, alt text, tables, meta
description, and image graphics.

- Use: `color`, `behavior`, `center`, `organize`, `recognize`, `summarize`,
  `optimize`, `prioritize`, `analyze`, `meter`, `gray`, `catalog`, `defense`,
  `license`, `favorite`, `traveling`.
- Never use: `colour`, `behaviour`, `centre`, `organise`, `realise`, `metre`,
  `grey`, `catalogue`, `defence`, `licence`, `favourite`, `travelling`.
- Do not mix the two variants inside one post. Mixed spelling is a visible
  quality defect on a site that has no other trust signals.
- UK readers are still served by this site, so where UK usage genuinely differs
  (plug type G, UK retailers, GBP prices) handle it in the body text — never by
  switching the spelling convention.
- Known sweep still outstanding: `posts/best-phone-under-2-juta.html` is
  UK-spelled — `colour` at line 167, `grey` at line 382, zero US spellings. If
  any of that content is reused, convert it to US English first.

### Slug and title hygiene

- No year in title or URL (§13.2). No "Best Phones 2026".
- One topic per article (§12.8).
- Never emit a placeholder or junk slug. *Mistake made:* a slug table shipped
  `/舊` — a Chinese character — as the slug for a battery article. Correct:
  `/phone-battery-last-longer`.
- Internal links are site-absolute: `/p/about.html`, `/search/label/Phone`.

### Maximum 3 picks per list article — hard cap

**A recommendation list is capped at three items. Three is the target, two is
fine, never four or more.**

Reason: every extra option is not more value for the reader, it is another
decision to defer. A list of five does not help someone choose — it hands the
choice straight back to them, which is the exact job the article was supposed to
do.

*Decision made by the user:* "makin banyak list nya org makin bingung mutusin.
3 cukup." Do not propose 5-, 7- or 10-item lists, and do not pad a list to make
a graphic look fuller.

Enforcement:
- The picks get one H3 each. Three H3 pick sections, not five.
- At most three product photos in any one graphic. The featured composite shows
  three handsets/laptops, not five.
- If a category genuinely has more than three good options, the article narrows
  by **priority** and says who each pick is *not* for, rather than listing all
  of them.
- Supporting/criteria sections are unaffected — those are explanation, not
  choices.

---

## 2. Blogger mechanics that are not guessable

### The title is NOT an `<h1>` in the body

- The post title goes in Blogger's **Title** field. That is the page's single H1.
- The body must contain **zero** `<h1>`.
- *Mistake made:* shipped `<h1>5 Phones Worth Buying...</h1>` in the body while
  also filling the Title field → two H1s per page, an anti-pattern (§13) and a
  real SEO defect.
- `validate-post.py` now asserts `0` H1 in the body, not `1`.

### Never let Blogger's image dialog write your images

Blogger's **Insert image** dialog, and anything inserted via Compose view,
rewrites the markup and injects:

```html
<div class="separator" style="clear: both;"><div class="separator" style="clear: both; text-align: center;"><a href="&lt;the image itself&gt;"><img ... /></a></div>
```

Three defects in one line:

1. It opens **two** `.separator` divs and closes **one**. The orphan div encloses
   the entire rest of the post and inherits `text-align:center`, so every
   paragraph after the first image renders centred.
2. It wraps the image in `<a href>` pointing at the image file — a useless link
   that strips the alt text.
3. It adds obsolete `border="0"` and inline `style="margin-left:1em;..."`.

**Rules:**
- Paste in **HTML view** only, never Compose.
- Body images are a bare `<img>` with `alt`, `width`, `height`, `loading`
  (first image eager, rest lazy).
- No wrapper `<div>`, no `<a>` around an `<img>`, no `style=`, no `border=`.
- The **first** image sets `data:post.thumbnailUrl` → it must stay first, and
  should be the most representative graphic.

---

## 3. Images: real product photos, no abstract chart art

- **Every graphic must contain real product photography.** The reader opens the
  post to see the hardware. A chart-only post reads as filler and was rejected
  outright — "user mau lihat hapenya bukan mau liat table".
- 2–3 products per composite is the sweet spot; one clean product shot per card.
- At most one table and one chart per article.
- Normalise every product photo to a **pure white (#ffffff)** background and use
  a white stage, so letterboxing is invisible. Mixed off-white backgrounds make
  contained photos look stranded in the middle of a box.
- Give each product its own accent colour, reused consistently across graphics.

### ImageMagick gotchas (each one cost real time)

- **The built-in SVG renderer IGNORES `<image href>`.** A layout that embeds
  photos as `<image>` renders with empty boxes. Correct approach: render the
  text/shape layer to PNG, then `magick composite` the real photo files on top
  with `-geometry +x+y`. See `posts/make-real-images.py`.
- Do not pass `%-22s` to `magick -format`; it warns and drops the field. Use
  plain `%f %wx%h`.
- `magick -resize WxH` = contain/fit. `-resize WxH^` = fill, then `-extent` to
  crop. A wide stage plus contain-fit is exactly what makes a product look
  stranded mid-box.
- Samsung: the only asset under
  `images.samsung.com/is/image/samsung/p6pim/id/<sku>/gallery/<name>-thumb-<id>`
  is **330×330**. The `is/image` service only upscales it (`?wid=1600`); there
  is no larger master. Get the tight box with
  `magick in.png -colorspace gray -threshold 92% -negate -format "%@" info:` and
  crop from the original, not from a guess.
- Infinix: `sec1/mb` is a promo card with marketing text; `sec1/pc` is a
  1920×1080 banner. Crop the handset out of the banner rather than shipping the
  promo card. Every other path on that CDN returns 403.

---

## 4. Editor-notes blocks and validation

- Never split a file on the first `-->`. Editor-notes blocks contain nested
  comments, so that split cuts the file in the wrong place.
  *Mistake made:* both `index("-->")` and `rindex("-->")` were wrong — one put a
  marker mid-notes, the other left a stray `-->` that opened a comment and
  swallowed the whole article.
- Use an explicit `<!-- END EDITOR NOTES -->` marker, and **strip all HTML
  comments before any structural check** — comments legitimately mention tags
  (e.g. "do not add `<h1>`") and get counted as real markup.
- Verify nesting with a real parser (`html.parser` / lxml), never by reading
  tags and counting by eye.
- Every article: `python3 posts/validate-post.py posts/<file>.html`.
- Every article, prose pass: `python3 posts/slop-check.py posts/<file>.html`.
  Different job from the validator above: that one enforces structure (heading
  order, link targets, image dimensions), this one reads the sentences for
  filler and AI tells. See the `anti-slop` skill. Both must be clean.
- Every template change: re-check XML well-formedness, CSS brace balance per
  `<style>` block, zero missing `b:include`, zero invalid `b:widget-setting`,
  zero `<img>` without `alt`, and exactly one H1 per page (from the Title
  field).

---

## 5. Working with the user

- They are impatient and they publish early. **Stop when the post is
  published.** Do not keep polishing assets "for later" — *mistake made:*
  continued regenerating graphics after the post was already live.
- When a market, currency, or product choice would force a rewrite of live
  content, ask **once** with concrete options, then commit. Do not guess.
- If something already published is wrong, deliver a **paste-ready replacement
  body** (e.g. `posts/post-body-FIXED.html`) with self-verification output — not
  a promise to redo it later.
