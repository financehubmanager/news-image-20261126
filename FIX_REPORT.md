# FIX REPORT — news-image-20261126

Fixer for the entry built at commit `bf3b2ea` (BUILD_REPORT.md) and
independently tested at the same commit (TEST_REPORT.md: verdict BERSIH,
0 KRITIS / 0 SEDANG / 4 KECIL). Only the small fixes below were made;
no redesign, no story swaps, no font-size changes.

## Changes

1. **README.md — 3 live make.fun badges (wajib sebelum submit).**
   Added at the very top of README.md, exactly per the submit pattern:
   the competition badge, the rank badge and the reward badge for
   `news-image-20261126` / `financehubmanager/news-image-20261126`,
   plus the `<sub>Entered on make.fun …</sub>` line. Also synced the
   story-1 line in README ("Vietnam 35%" → "Vietnam 20–35%") so the
   README matches the image.
2. **K-2 (Vietnam) — fixed in `render.py` STORIES[0].**
   Summary was "China up to 20%; Vietnam 35%; EU 15%. Hearing Jan 25."
   — 35% is the tariff WITHOUT a deal (20% with a deal, per Reuters).
   Now: "China up to 20%; Vietnam 20–35%; EU 15%. Hearing Jan 25."
   The range form adds only 3 characters, keeps the summary on 2 lines
   and stays accurate (20% with deal, 35% without).
3. **K-3 (Cairo) — fixed in `render.py` STORIES[1].**
   Headline was "Fuel tanker fire kills 31 in Cairo"; the toll was
   preliminary ("at least 31" in all sources). Now: "Fuel tanker fire
   kills at least 31 in Cairo". It wraps to 3 lines (allowed, max 3);
   the existing `draw_panel` guard kept the summary clear of the
   headline — visually verified, no overlap, no crowding.

## Deliberately NOT changed (per task)

- K-1 (five of six stories announced 25 Nov local time): left as is —
  the "in any time zone" rule and the judge's pre-13-Nov cutoff already
  mitigate it, and there is no fix without swapping stories.
- K-4 (summary/footer font size): left as is — still readable at
  ~300px, and the task forbade changing it.

## Verification (after the fixes)

- `python3 render.py` from scratch → `entry.png`: 1024×1024, RGB, PNG,
  **136.828 bytes** (limit 1.048.576), sha256
  `12d1836750f9dafb2b78022ab707fa85ed8a586edd82f04b9bff5d479d180ba8`
  (was `b9bfcdef…` at build).
- PNG chunk walk: signature OK; IHDR, IDAT ×3, IEND — all CRCs OK,
  ends exactly at IEND, 0 trailing bytes.
- `main.py` run twice (`MAKEFUN_OUTPUT_DIR=/tmp/fix1` and `/tmp/fix2`):
  both outputs byte-identical to each other and to `entry.png`
  (same sha256 `12d18367…`).
- Visual, full size: Cairo headline 3 lines with a clear gap to the
  summary; tariff summary reads "Vietnam 20–35%"; no overlapping or
  clipped text anywhere; no new artefacts.
- Visual, 300×300 downscale: date banner and all six headlines still
  readable; summaries small but unchanged from the tested version.

## Files changed

- `README.md` (badges + synced Vietnam line)
- `render.py` (STORIES[0] summary, STORIES[1] headline)
- `entry.png` (re-rendered)
- `FIX_REPORT.md` (this file)

## One-line verdict

The two factual qualifications the tester flagged are now in the
image without any layout damage, the README carries the required
badges, and determinism/format checks all pass — the entry is
strictly stronger than the builder version and ready to submit.
