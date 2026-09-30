# 3 Definite Causes of AI Slop

Working notes. Not published. `index.html` is the only file that gets pasted.

SLUG:              /ai-slop-causes          (NO year — §13.2)
KEYWORDS:          ai, writing, slop

```
THE THREE CAUSES, and why these three and not five:
  A hard cap of three applies here too. The topic has no shortage of candidate
  causes - unoriginal premises, passive voice, hedging, fake enthusiasm,
  uniform paragraph length. Those are SYMPTOMS. The three below are causes:
  each one is a decision someone made, and removing the decision removes the
  symptom. Symptom-lists read like checklists; cause-lists actually tell you
  something to do differently.

  1. Shipping the first draft.
     Symptom: fluent, well-structured, says nothing by paragraph four.
     Why it happens: reading someone else's output is comfortable, editing it is
     not. Smooth reads as finished. This is a comfort failure, not a skill
     failure.
     Fix: delete the draft, write four sentences first, use AI for structure.

  2. Prompting for count instead of for a position.
     Symptom: ten interchangeable tips that can be reordered freely.
     Why it happens: asking for a number gets a number. Count is a shape, not
     an argument.
     Fix: ask for the strongest claim plus what would have to be true to falsify
     it. Forces commitment, produces 4-5 real points instead of 10 filler ones.

  3. Letting something that cannot check do the checking.
     Symptom: confident prices, specs and citations that do not resolve.
     Why it happens: the model predicts the next likely token. The most likely
     form of a price is a price. It is not lying - lying requires knowing the
     truth.
     Fix: verify every number against a non-model source, or round it away.
     This is the only one of the three that can genuinely hurt a reader.

THE OWN-REFERENCE, and it is the credibility of this piece:
  Cause 3 is illustrated with real incidents from building THIS site, not with
  a hypothetical. Specifically:
    - An early draft of the laptop article asserted battery capacities and
      prices for two phones (Tecno Spark Go 3, Infinix Hot 60i) that could not
      be verified, and both turned out not to be sold in the US market the site
      targets. The prices did not merely go unverified - they did not exist for
      the reader.
    - A generated graphic was labelled with USD street prices for those same
      phones. Those labels were wrong in the direction that matters.
    - Several of the most authoritative-sounding sources found while researching
      the AI-apps article were affiliate pages citing each other's figures.
      Circular, confident, and entirely fictional as earnings claims.
  This is why the piece is worth publishing from this site specifically. Do not
  soften it into a general observation - the credibility IS the incident.

DELIBERATELY NOT INCLUDED:
  - No "AI detector" claims. Detectors are unreliable, and pointing at one
    invites the reader to use one.
  - No accusation of bad faith toward AI users. Three of the four causes are
    process failures by capable people, and the piece says so in paragraph two.
    Turning this into a purity test is exactly how a good argument becomes
    slop itself.
  - No advice about "sounding more human". Prompt-level style tweaks are a
    symptom fix and would undercut the whole argument.

STRUCTURE NOTE:
  The "What Slop Is Not" section exists to pre-empt the reading where this
  piece becomes an excuse for shipping lazy work. It is load-bearing, not an
  aside - without it the piece invites exactly the behaviour it criticises.

IMAGES:
  ONE image per post, uploaded to Blogger's own media library so
  data:post.thumbnailUrl picks it up. Blogger only generates a post thumbnail
  from an image hosted on blogger.googleusercontent.com; any other host leaves
  it EMPTY, the homepage card renders with no picture, and og:image goes
  missing too.

  UPLOAD STEPS:
    1. Whitelist blogger.com in Brave first. Shields silently fails the upload
       otherwise, with no error shown.
    2. New post -> HTML view -> paste the body from index.html
    3. Insert image (toolbar, NOT right-click, NOT Compose) -> Upload files
    4. Fix the alt text afterwards. Blogger's dialog writes alt="" and wraps
       the image in an <a href> pointing at the image file itself.
    5. Strip the wrapper: no <a>, no <div class=separator>, no border=, no
       inline style=. Keep width/height.
    6. Fill Blogger's Title field.

  Blogger caps an image at 1600px on its LONGEST side. These graphics are
  1080x1800+, so a /s1600/ URL comes back downscaled to 878x1600 and the small
  type goes soft on a high-DPR phone. Use /s0/ to get full resolution.
```
