# Phone Peak Brightness: The Number That Is Not Outdoor Brightness

Working notes. Not published. `index.html` is the only file that gets pasted.

KEYWORDS:  brightness, nits, hdr, peak, outdoor, samsung, pixel, oled

THE THESIS, in one line: the peak brightness figure on a phone spec sheet
describes a small, bright, momentary patch of screen, and not the whole display
you are reading. That is why a phone quoted at 3,300 nits does not look like
3,300 nits outdoors.

Deliberately NOT a "best bright phones" roundup. Such a list would be a spec
table that goes stale on every launch, it would repeat the mistake the article
argues against, and the site already has roundups. This is a reference article.

NO PRICES ANYWHERE, on purpose. Nothing here is for sale, so there is no price
to date and §12.5 price-dating does not apply. The article stays evergreen
because it explains a measurement convention, not a shopping moment.

---

## PRIMARY SOURCES - manufacturer and standards body

Everything in the "manufacturer says" tier below is quoted from the vendor's own
page. Nothing is paraphrased from a review site.

1. **Google, Pixel 10 Pro spec page**
   https://store.google.com/us/product/pixel_10_pro_specs
   States verbatim: "Up to 2,200 nits (HDR) and up to 3,300 nits (peak
   brightness)". This is the load-bearing fact of the whole article. Google
   publishes BOTH numbers for ONE handset on ONE page, which means the maker
   itself treats them as two different measurements.

2. **Google, Pixel 10 Pro spec page (GB)**
   https://store.google.com/gb/product/pixel_10_pro_specs?hl=en-GB
   Same two figures, same wording, UK store. Confirms it is not a US-only
   phrasing.

3. **Samsung, Galaxy S25 series comparison page**
   https://www.samsung.com/us/smartphones/galaxy-s25-ultra/compare
   Footnotes, verbatim:
   - "These figures are comparisons made based on each model's respective peak
     brightness level."
   - "The display is adaptive, automatically adjusting brightness level based on
     the environment. In areas of 5000 lux or higher, High Brightness Mode and
     Vision Booster will be activated."
   The 5000 lux line is the manufacturer naming the trigger condition for the
   boost. That is why the article says the boost is a reaction to bright ambient
   light rather than a resting state.

4. **Samsung, Galaxy S25 / S25+ spec page (regional)**
   https://www.samsung.com/latin_en/smartphones/galaxy-s25/specs
   Display technology listed as Dynamic AMOLED 2X, 120Hz. The 2,600 nits peak
   figure appears on Samsung's own spec pages and on carrier spec pages for the
   same models (Vodafone UK, Optus AU), so the number is the same across markets.

5. **LG Display newsroom, Tandem WOLED, February 2026**
   https://news.lgdisplay.com/en/2026/02/the-real-story-behind-lg-displays-new-tandem-woled-2
   The panel maker itself, not a reviewer. Verbatim: "Peak brightness is
   important, but perceived brightness in real viewing environments is equally
   critical." And: "improving luminance in specific Average Picture Level (APL)
   is key. Brightness in the APL 25% has improved by approximately 20%."
   This is the strongest possible source for the argument, because it is the
   company that builds the panels admitting that APL 25% is what they optimise.

6. **IEC 62341-6-1:2025**, OLED displays, measuring optical parameters.
   https://standards.iteh.ai/catalog/standards/iec/880a0e0a-ca0a-4450-8362-7cbedac0339a/iec-62341-6-1-2025
   Defines APL: "The APL will normally be expressed as a percentage, where a
   full white screen at maximum drive level would be 100 % APL." Annex F lists
   "F.3 Maximum full screen luminance" and "F.4 4 % window luminance" as two
   separate required measurements. A published standard treating them as
   distinct is the cleanest possible demonstration that they are distinct.

7. **EIZO, on ABL**
   https://www.eizoglobal.com/library/management/oled-abl-control
   Verbatim: "As APL increases, the monitor generally assumes that the OLED
   panel is under greater stress and responds accordingly." From a professional
   reference monitor manufacturer, so the description of the mechanism is
   first-hand rather than reported.

---

## MEASURED SOURCES - named labs, method stated alongside the number

Rule followed here, the same one used in the charging post: a third-party
measurement is only ever quoted with the method that lab stated, and it is never
presented as our own.

8. **GSMArena, Pixel 10 Pro review**
   https://www.gsmarena.com/google_pixel_10_pro-review-2877p3.php
   Verbatim: "Google says the Pixel 10 Pro should be good for up to 2,200nits in
   high-brightness mode (with the whole display lit up) ... For a 5% patch of
   white, the 10 Pro should be able to go as bright as 3,300nits".
   Measured: 1,399 nits manual and 2,351 nits with adaptive brightness, both on
   a 75% lit-up area.
   This is the source that translates Google's two numbers into "whole screen"
   and "5% patch". Without it the article would be asserting the meaning.

9. **GSMArena, Galaxy S25 review**
   https://www.gsmarena.com/samsung_galaxy_s25-review-2794p3.php
   Verbatim: "The maximum brightness when controlling it manually was 438 nits
   without boost and 747 nits with the extra brightness boost."
   The 438 figure is the article's headline contrast: a 2,600-nit phone
   producing 438 nits across the full screen.

10. **PhoneArena, Galaxy S25**
    https://www.phonearena.com/phones/Samsung-Galaxy-S25_id12340
    "Bright Max (20% APL) 2394". Same phone as GSMArena's 438, because it was
    measured on a 20% window rather than full screen. This is the row that
    proves the disagreement is method, not quality.

11. **DXOMARK, Galaxy S25 display test**
    https://www.dxomark.com/samsung-galaxy-s25-display-test
    "The device's peak luminance, measured at 2,600 nits". Included so the
    table's top row is not only a marketing claim: an independent lab does
    reproduce 2,600 when it measures peak.

12. **Bandicoot Lab, Galaxy S26 and Pixel 10**
    https://bandicootlab.com/phone/samsung-galaxy-s26
    Reports manual and HDR peak as separate figures for every model:
    Galaxy S26 640.51 nits manual, 2,791.1 HDR peak. Pixel 10 about
    1,495.84 nits manual, about 3,089.1 HDR peak.
    Used only for the general point that the gap is systematic across models.
    Cited as one lab among several, not as the definitive figure.

---

## WHAT WAS DELIBERATELY LEFT OUT

- **A "sunlight readable" tier list.** It would be a listicle of the thing the
  article criticises, and there is no free-licensed evidence base for it.
- **Any price.** Nothing is being sold.
- **DXOMARK's outdoor readability scores.** Real numbers, but they are a
  composite index with their own weighting, and pulling one line of an index
  into a post about raw nits would confuse the argument.
- **iPhone figures.** Apple publishes 1,000 nits full screen and 1,600 peak on
  the iPad Pro, which would illustrate the point well, but the article is about
  a comparison that already works with two Android vendors' own pages. Adding a
  third vendor would lengthen the piece without strengthening it.

## INTERNAL LINKS - both verified live on 2026-10-01

- /2026/10/phone-charging-speed-why-number-on-box.html - HTTP 200. Same thesis
  shape, ceiling versus reality. The most relevant possible sibling post.
- /2026/09/top-3-midrange-gaming-phones.html - HTTP 200. Gaming phones are used
  outdoors more than any other category, which is where the argument lands.

## IMAGE

images/01-phone-peak-brightness.jpg, 1600x1067, generated from the two Commons
photos in images/refs/. Upload to Blogger's own media library: Blogger only
builds a post thumbnail from an image on blogger.googleusercontent.com, so an
image from another host leaves the homepage card blank. Then fix alt (Blogger
writes alt=""), remove the <a href> wrapper Blogger adds, and keep width/height.
Use /s0/, not /s1600/.

Source photos, both free licences:
- images/refs/phone-in-sun.jpg - "Person holding smartphone with camera app open
  while sitting outdoors on a sunny day, focused on taking a picture of the
  scene" by Shixart1985, CC BY 2.0. Used in the sunlight section; the screen is
  visibly washed out by reflection, which is the whole point. The Commons
  original is portrait 1280x1707, and a portrait source contained into the
  compare layout's landscape stage letterboxes into white bars either side, so
  it was cropped to 1000x667 around the handset. Cropped only - nothing
  retouched, no exposure change.
- images/refs/display-test-pattern.jpg - "EIZO Foris FG2421 VGA computer
  monitor displaying test pattern" by Lucasbosch, CC BY-SA 4.0. Used in the
  measurement section. Note this file arrives from Commons as a PNG despite the
  .jpg name; it was converted and compressed. The test card carries 5% and 10%
  window markers in its top-right corner, which is literally the concept being
  explained.
