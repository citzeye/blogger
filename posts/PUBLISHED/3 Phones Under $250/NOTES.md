# 3 Phones Under $250

Working notes. Not published. `index.html` is the only file that gets pasted.

```
SLUG:      /best-phone-under-usd-250     (NO year)
KEYWORDS:  phone, budget, samsung, xiaomi

WHAT THIS POST REPLACES, and why the old one had to go rather than be edited:
  The previous version of this article was titled "5 Phones Worth Buying Under IDR
  2 Million", slug /best-phone-under-2-juta, with prices in Rp. It failed the
  site's own rules on four counts:
    1. IDR and "juta" on an English site aimed at US and UK readers. USD only.
    2. Five picks. The cap is three, because a longer list returns the decision
       to the reader instead of making it for them.
    3. Two of the five - Tecno Spark Go 3 and Infinix Hot 60i - are not sold in
       the US or UK. A US or UK reader cannot buy them or check their price, so
       the recommendation was un-actionable. This is exactly the failure mode
       cause #3 in "3 Definite Causes of AI Slop" describes, and the graphic for
       the old post was labelled with USD street prices for phones that have no
       USD street price. Those graphics were quarantined in images/_JANGAN-DIPAKAI/.
    4. A generated composite once showed the SAME laptop photo in all three
       product cards, because every source photo was normalised into one
       working file that overwrote itself. Fixed with a per-product working file
       plus an md5 guard in make-laptop-images.py.

PRICES. Every figure is an approximate US price in USD observed September 2026,
and every one is written as a range. Sources actually used:
  - Samsung Galaxy A17 5G: $249.99 at launch (smartprix US, Aug 2025); ~$254.99
    for 8/256 (smartprix US, Sep 2026); from $213.01 (kimovil). Published as
    $210-255.
  - Xiaomi Redmi Note 14: from $199 (smartprix US); from $199-200 (kimovil).
    Published as $195-200. The graphic shows $197, the midpoint. Note the
    midpoint of 195-200 is 197.5; 197 is used so the figure is a real price the
    reader could see on a shelf, not a decimal.
  - Samsung Galaxy A16 5G: $134.97 (smartprix US). Published as ~$135.
  - Motorola Moto G Power (2026): $399.99 on Motorola's own US store; raised
    from $299.99 (PhoneArena, April 2026, on memory chip costs). Published as
    the "stopped being budget" section.

SPEC CLAIMS AND THEIR SOURCES - check these before republishing:
  - A17 5G: 6 years OS + security updates, 6.7in AMOLED 90Hz, Exynos 1330,
    5000mAh 25W, 50MP, 128/256GB. Sources: 91mobiles comparison (6yr OS+security),
    HT Tech spec sheet (AMOLED 90Hz, Exynos 1330, 5000mAh 25W, 50MP triple),
    smartprix (8GB/256GB variant).
  - Redmi Note 14: up to 256GB, 6.67in AMOLED 120Hz, Dimensity 7025 Ultra,
    5110mAh 45W. Sources: kimovil (Dimensity 7025, 8/256, 5110mAh),
    gadgets360 (5110mAh, 45W), 91mobiles (AMOLED, 45W).
    CAMERA DELIBERATELY NOT QUOTED: the 4G global variant has a 108MP main and the
    5G has 50MP. Rather than pick one and risk being wrong for the SKU a reader
    actually buys, the camera is omitted and a warning was added that the model
    name covers 4G and 5G variants with different cameras and chips.
  - A16 5G: 6.7in AMOLED 90Hz, Exynos 1330, 8GB/128GB expandable to 1.5TB,
    5000mAh 25W, 50MP. Sources: smartprix US, HT Tech, 91mobiles.

UK PRICING: NOT INVENTED. No GBP figure was verified, so the article points UK
readers at UK retailers and warns that UK prices run higher than the US
equivalents. Add GBP only after checking a UK source.

DELIBERATELY NOT INCLUDED:
  - No Moto G Play (2026) at $249.99. Its 4GB RAM and 64GB storage are below the
    floor this article already argues for in the RAM section.
  - No Moto G Power as a pick. At $399.99 it is outside the band, and pretending
    otherwise would repeat the original article's mistake.
  - No unverified battery-hour figures. Only the 120Hz vs 90Hz difference and
    the charging wattages, both of which are on spec sheets.

IMAGES:
  ONE image per post, uploaded to Blogger's own media library so
  data:post.thumbnailUrl picks it up. Blogger only generates a post thumbnail
  from an image hosted on blogger.googleusercontent.com. Any other host leaves it
  EMPTY: the homepage card renders with no picture and og:image goes missing.

  UPLOAD STEPS:
    1. Whitelist blogger.com in Brave first. Shields silently fails the upload
       otherwise, with no error shown.
    2. New post -> HTML view -> paste the body from index.html
    3. Insert image (toolbar, NOT right-click, NOT Compose) -> Upload files
    4. Fix the alt text. Blogger's dialog writes alt="" and wraps the image in
       an <a href> pointing at the image file itself.
    5. Strip the wrapper: no <a>, no <div class=separator>, no border=, no
       inline style=. Keep width/height.
    6. Fill Blogger's Title field.

  Blogger caps an image at 1600px on its LONGEST side, so a /s1600/ URL comes
  back downscaled and the small type in the graphic goes soft on a high-DPR
  phone. Use /s0/ for full resolution.

REPLACING THE PUBLISHED POST:
  The old IDR post is already live. Blogger derives a post's URL from its title,
  so changing the title changes the URL and orphans the old one - which is
  against AGENT.md §13.10 for anything already indexed. Two options:
    A. Set a CUSTOM PERMALINK on the post, keeping the old URL alive, and use
       the new content. Cleanest for anything with traffic.
    B. Publish as a new post on the new slug and leave the old one up as-is.
       Creates near-duplicate content, which is worse for the site than either
       option alone.
  Recommend A. Do not delete the old URL either way - a 404 on an indexed page
  costs more than a redirect.
```


---

## EDITOR NOTES (dipindah dari index.html)

1600x1067 JPEG, 3:2 landscape. It is 3:2 on purpose: the homepage card and
     the sidebar widget render a 3:2 frame with object-fit contain, so a 3:2
     source fills that frame exactly - no crop, no letterbox. The handsets inside
     are portrait, and each sits in its own portrait stage, so none of them is
     cut either.
     Upload to Blogger's own media library, NOT to another host. Blogger only
     builds a post thumbnail from an image on blogger.googleusercontent.com; from
     any other host data:post.thumbnailUrl comes back empty, the homepage card
     renders with no picture, and og:image goes missing.
     After uploading: fix alt (Blogger writes alt=""), strip the <a href> wrapper
     it adds around the image, drop border= and any inline style, and keep
     width="1600" height="1067". Use /s0/ rather than /s1600/ if the URL shows a
     size segment - Blogger caps at 1600px on the longest side and would send
     back a downscaled copy. Full steps in NOTES.md.
