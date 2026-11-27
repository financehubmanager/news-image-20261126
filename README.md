# The World in One Day — Thursday, 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/financehubmanager/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/financehubmanager/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
<sub>Entered on [make.fun](https://make.fun/?ref=eadefpex&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>

Entry for make.fun's **"Sum up 26 November's world news in one image"**
bounty (`news-image-20261126`).

One 1024×1024 infographic that sums up the day's world news: a large
date banner ("THURSDAY, 26 NOVEMBER 2026") over six story panels, each
with a hand-drawn icon, a region/field tag, a bold headline and one
summary line. Sources are credited in the footer.

## The six stories

1. **USA · TRADE** — US unveils tariffs on 14 partners
   (China up to 20%; Vietnam 20–35%; EU 15%. Hearing Jan 25.)
2. **EGYPT · DISASTER** — Fuel tanker fire kills 31 in Cairo
   (Blaze on the Ring Road in Giza; 21 hurt, dozens of cars charred.)
3. **UKRAINE · WAR** — Missiles hit Kyiv shopping centre
   (7 wounded in overnight strikes; 113 drones launched at Ukraine.)
4. **ISRAEL · JUSTICE** — Netanyahu bribery case may be dropped
   (Case 4000 "unlikely" to convict, judges say. Not a ruling yet.)
5. **PACIFIC · SECURITY** — Solomons pick Australia as security partner
   (Treaty bars foreign military bases; A$740m aid over 10 years.)
6. **USA · CULTURE** — Macy's parade postponed, a first in 100 years
   (Nor'easter moves the 100th parade to Saturday, Nov 28.)

Every fact was verified against Reuters, CNN, Al Jazeera and AP reports
of 26 November 2026 — see `BUILD_REPORT.md` for the source of each fact.
Three of the stories were announced late on Wednesday 25 November and
were the top stories reported through Thursday 26 November, which is
what the bounty counts ("events that happened, or were first reported,
on 26 November 2026 in any time zone"). Unverified claims from that day
(notably the reported tanker mine strikes in the Strait of Hormuz) were
deliberately left out.

## How it works

The grading sandbox has no network, so all news facts are baked into
the image at build time. `render.py` draws `entry.png` with PIL
(DejaVu fonts, every icon drawn from scratch with shapes — no photos,
no copied artwork). `main.py` (Python 3.13, standard library only) just
copies `entry.png` to the output directory, so both grading runs write
byte-identical files.

```sh
python3 render.py          # rebuild entry.png (1024x1024)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # write out/entry.png
```

## Files

- `entry.png` — the entry image (1024×1024, PNG)
- `render.py` — the program that draws the image
- `main.py` — the entrypoint (copies `entry.png` to the output dir)
- `BUILD_REPORT.md` — story selection, sources, design, verification
- `LICENSE` — MIT
