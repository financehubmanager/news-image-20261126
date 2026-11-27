# BUILD REPORT — news-image-20261126

Entry for make.fun's "Sum up 26 November's world news in one image"
bounty. Built 27 November 2026 (WIB) by the builder agent.

## Story selection and sources

Six stories, chosen for impact and breadth (trade, disaster, war,
justice, Pacific security, culture/weather; USA, Egypt, Ukraine, Israel,
Solomon Islands/Australia). Every fact below was verified against at
least one trusted news source reporting on 26 November 2026. Three
stories were announced late on Wednesday 25 November and were the top
stories reported through Thursday 26 November — the bounty counts
"events that happened, or were first reported, on 26 November 2026 in
any time zone", and the day's own briefings (e.g. Algenom's "The world
today", edition Thursday 26 November 2026) list them as the day's top
stories.

1. **US unveils tariffs on 14 partners** — USTR proposed new tariffs on
   14 economies over excess industrial capacity; China up to 20% (40%
   if the trade truce lapses on 10 Jan), Vietnam 20% with a deal / 35%
   without, India 17% / 25%, EU/Japan/S. Korea/Taiwan/Switzerland 15%;
   public hearing 25 January.
   Sources: Reuters, "Five takeaways from Trump's new tariffs",
   26 Nov 2026 (reuters.com/world/china/five-takeaways-trumps-new-tariffs-2026-11-26/);
   The Business Standard explainer, 26 Nov 2026.
2. **Fuel tanker fire kills 31 in Cairo** — a fuel tanker crashed and
   burst into flames on the Ring Road in Warraq, Giza, on Wednesday
   evening; at least 31 killed, 21 injured, dozens of cars charred.
   Sources: Reuters, "Egyptians mourn, demand accountability after
   deadly tanker explosion kills 31", 26 Nov 2026; CNN, "At least 31
   killed in fuel tanker fire near Cairo", 26 Nov 2026; Al Jazeera.
3. **Missiles hit Kyiv shopping centre** — Russian ballistic missiles
   struck a shopping centre and two other buildings in Kyiv's
   Desnianskyi district overnight; 7 wounded (2 seriously); 113 drones
   launched at Ukraine overnight.
   Sources: Reuters via TBS News, "Russian forces hit Kyiv with
   ballistic missiles, seven wounded, mayor says", 26 Nov 2026;
   Kyiv City Military Administration, 26 Nov 2026.
4. **Netanyahu bribery case may be dropped** — judges in the corruption
   trial recommended prosecutors drop the Case 4000 bribery charge
   (conviction "unlikely"), reconsider Case 2000, and seek a deal in
   Case 1000. The recommendation is not a ruling.
   Sources: Reuters, "Israeli judges recommend prosecutors drop one
   bribery case against Netanyahu", 25 Nov 2026; CNN, "Netanyahu gets
   major legal boost as court casts doubt on corruption case",
   25 Nov 2026.
5. **Solomons pick Australia as security partner** — Solomon Islands
   and Australia signed a treaty in Canberra naming Australia the
   "primary security partner"; no foreign military or security base on
   Solomon Islands soil; Australia to provide A$740m over 10 years.
   Sources: AP via Al Jazeera / The News, 25–26 Nov 2026; AAP,
   26 Nov 2026.
6. **Macy's parade postponed, a first in 100 years** — the 100th
   Macy's Thanksgiving Day Parade postponed from Thursday 26 Nov to
   Saturday 28 Nov because of a nor'easter (heavy rain, strong winds);
   first weather postponement in the parade's history (suspended
   1942–1944 for WWII, never rescheduled for weather).
   Sources: CNN, "100th Macy's Thanksgiving Day Parade moved to
   Saturday due to projected storm", 25 Nov 2026; USA Today, 25 Nov 2026.

Deliberately left out: the reported tanker mine strikes in the Strait
of Hormuz (Iranian claims, explicitly unverified in the 26 Nov
briefings), and the Bogor gold-mine flood (death tolls conflicted
between sources: 13 vs 16 dead). Nothing in the image is speculation
presented as fact; every number comes from the sources above.

## Design

- 1024×1024 PNG, "newspaper front page" composition: navy banner with
  the date in large white type ("THURSDAY, 26 NOVEMBER 2026", 52–56 pt
  bold, auto-fit to the full width) and a gold "THE WORLD IN ONE DAY"
  kicker, then a 2×3 grid of white story cards on a warm paper
  background, footer crediting Reuters · CNN · Al Jazeera · AP.
- Each card: coloured left bar, a hand-drawn icon in a coloured badge
  (bar chart, flame, building, scales of justice, shield, balloon),
  a region/field tag, a bold headline (32 pt) and one summary line
  (24 pt). No text smaller than 20 pt anywhere; the date, tags and
  headlines stay decipherable when the image is shrunk to ~300 px
  (checked with a 300×300 downscale).
- Everything is drawn from scratch with PIL shapes and DejaVu fonts
  (bundled on the system). No photos, no copied artwork, no starter-kit
  image (the kit's pixel-art globe placeholder was not used).

## Bugs found and fixed during the build

1. Headline/summary collision: 3-line headlines overlapped the
   bottom-anchored summary. Fixed by shortening three headlines to
   two lines and adding a guard in `draw_panel` (`sy` is never placed
   above the headline's bottom + 12 px).
2. `icon_scales` coordinate bug: the loop `for sx in (-20, 20)` used
   `sx` as an absolute x coordinate, so the scales' pans were drawn at
   x = −20/+20 instead of next to the stem — one pan landed as a stray
   white triangle over the Ukraine panel's accent bar (x 9–23,
   y 476–506), the other off-canvas. The scales badge itself showed
   only a "T". Fixed to `sx = cx + off`; the stray triangle is gone
   (verified: 0 stray white pixels left of the Ukraine panel) and the
   scales now show both pans.
3. The building icon's starburst rays poked outside its badge circle;
   shortened and moved inward.

## Verification

- `python3 render.py` → `entry.png`: 1024×1024, RGB, PNG,
  **132,418 bytes** (limit 1,048,576), sha256
  `b9bfcdef7812c7eac2d6a15d75ab0b7769f12aaca3ff4cf227cb828c2ace72fc`.
- `main.py` run twice (`MAKEFUN_OUTPUT_DIR=/tmp/out1` and `/tmp/out2`):
  both outputs byte-identical to each other and to `entry.png`
  (same sha256 above). PNG opens and verifies with PIL.
- Visual check at full size and at 300×300: date banner clearly
  readable; all six headlines decipherable; no overlapping text, no
  stray marks, no garbled text.
- `main.py` is Python 3 stdlib only (`os`, `shutil`); it copies the
  shipped `entry.png` and performs no network access. The image is
  pre-rendered at build time, as the grading sandbox has no network.

## Files

- `entry.png` — the entry image
- `render.py` — draws `entry.png` (build-time only, uses PIL)
- `main.py` — entrypoint: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`)
- `README.md`, `LICENSE` (MIT), `.makefun/owner.json`
