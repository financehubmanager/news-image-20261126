#!/usr/bin/env python3
"""Render entry.png: a one-day world-news infographic for
Thursday, 26 November 2026. All facts were researched from Reuters,
CNN, Al Jazeera and AP reports of 26 November 2026 (see BUILD_REPORT.md).
Everything is drawn with PIL shapes and DejaVu fonts; no photos,
no copied artwork. Run: python3 render.py  -> writes entry.png (1024x1024).
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

NAVY = (15, 42, 67)
GOLD = (232, 163, 61)
PAPER = (247, 243, 234)
WHITE = (255, 255, 255)
INK = (24, 28, 34)
MUTED = (96, 104, 112)
BORDER = (214, 208, 194)

W, H = 1024, 1024


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def fit_font(draw, text, name, size, max_width):
    """Largest size <= `size` that makes `text` fit `max_width`."""
    while size > 10:
        f = font(name, size)
        if draw.textlength(text, font=f) <= max_width:
            return f
        size -= 2
    return font(name, size)


def wrap(draw, text, f, max_width):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- icons
def icon_bars(d, cx, cy, r, color):
    # bar chart, three ascending bars
    bw, gap = 13, 7
    heights = (18, 30, 42)
    x0 = cx - (3 * bw + 2 * gap) // 2
    for i, hgt in enumerate(heights):
        x = x0 + i * (bw + gap)
        d.rectangle([x, cy + 22 - hgt, x + bw, cy + 22], fill=WHITE)
    d.line([x0 - 4, cy + 22, x0 + 3 * bw + 2 * gap + 4, cy + 22],
           fill=WHITE, width=4)


def icon_flame(d, cx, cy, r, color):
    # stylised flame: outer teardrop + inner flame
    outer = [(cx, cy - 26), (cx + 16, cy - 4), (cx + 13, cy + 14),
             (cx + 5, cy + 22), (cx - 5, cy + 22), (cx - 13, cy + 14),
             (cx - 16, cy - 4)]
    d.polygon(outer, fill=WHITE)
    inner = [(cx, cy - 8), (cx + 8, cy + 4), (cx + 6, cy + 14),
             (cx - 6, cy + 14), (cx - 8, cy + 4)]
    d.polygon(inner, fill=color)


def icon_building(d, cx, cy, r, color):
    # building with windows + impact star at the top corner
    d.rectangle([cx - 18, cy - 16, cx + 18, cy + 24], fill=WHITE)
    d.rectangle([cx - 18, cy - 16, cx + 18, cy - 8], fill=WHITE)
    for gx in (-11, 0, 11):
        for gy in (-2, 10):
            d.rectangle([cx + gx - 4, cy + gy - 4, cx + gx + 4, cy + gy + 4],
                        fill=color)
    # small starburst at top-right corner (kept inside the badge)
    sx, sy = cx + 17, cy - 15
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([sx, sy, sx + 8 * math.cos(a), sy + 8 * math.sin(a)],
               fill=WHITE, width=3)


def icon_scales(d, cx, cy, r, color):
    # scales of justice
    d.line([cx, cy - 24, cx, cy + 22], fill=WHITE, width=5)
    d.line([cx - 20, cy - 18, cx + 20, cy - 18], fill=WHITE, width=5)
    d.ellipse([cx - 4, cy - 28, cx + 4, cy - 20], fill=WHITE)
    for off in (-20, 20):
        sx = cx + off
        d.line([sx, cy - 18, sx - 8, cy + 2], fill=WHITE, width=3)
        d.line([sx, cy - 18, sx + 8, cy + 2], fill=WHITE, width=3)
        d.polygon([(sx - 11, cy + 2), (sx + 11, cy + 2), (sx, cy + 12)],
                  fill=WHITE)
    d.line([cx - 14, cy + 22, cx + 14, cy + 22], fill=WHITE, width=5)


def icon_shield(d, cx, cy, r, color):
    # shield outline + check mark
    pts = [(cx, cy - 24), (cx + 18, cy - 16), (cx + 18, cy + 2),
           (cx, cy + 24), (cx - 18, cy + 2), (cx - 18, cy - 16)]
    d.polygon(pts, outline=WHITE, width=5)
    d.line([cx - 9, cy + 1, cx - 2, cy + 9, cx + 11, cy - 9],
           fill=WHITE, width=5, joint="curve")


def icon_balloon(d, cx, cy, r, color):
    # parade balloon: ellipse + knot + wavy string
    d.ellipse([cx - 16, cy - 26, cx + 16, cy + 4], fill=WHITE)
    d.polygon([(cx - 5, cy + 4), (cx + 5, cy + 4), (cx, cy + 12)],
              fill=WHITE)
    pts = []
    import math
    for i in range(9):
        t = i / 8
        pts.append((cx + 7 * math.sin(t * math.pi * 2), cy + 12 + t * 12))
    d.line(pts, fill=WHITE, width=3, joint="curve")


ICONS = {
    "bars": icon_bars,
    "flame": icon_flame,
    "building": icon_building,
    "scales": icon_scales,
    "shield": icon_shield,
    "balloon": icon_balloon,
}

# ---------------------------------------------------------------- stories
# (tag, headline, summary, accent colour, icon)
STORIES = [
    ("USA  ·  TRADE",
     "US unveils tariffs on 14 partners",
     "China up to 20%; Vietnam 20\u201335%; EU 15%. Hearing Jan 25.",
     (29, 78, 137), "bars"),
    ("EGYPT  ·  DISASTER",
     "Fuel tanker fire kills at least 31 in Cairo",
     "Blaze on the Ring Road in Giza; 21 hurt, dozens of cars charred.",
     (192, 57, 43), "flame"),
    ("UKRAINE  ·  WAR",
     "Missiles hit Kyiv shopping centre",
     "7 wounded in overnight strikes; 113 drones launched at Ukraine.",
     (108, 52, 131), "building"),
    ("ISRAEL  ·  JUSTICE",
     "Netanyahu bribery case may be dropped",
     "Case 4000 \u2018unlikely\u2019 to convict, judges say. Not a ruling yet.",
     (14, 124, 123), "scales"),
    ("PACIFIC  ·  SECURITY",
     "Solomons pick Australia as security partner",
     "Treaty bars foreign military bases; A$740m aid over 10 years.",
     (46, 125, 50), "shield"),
    ("USA  ·  CULTURE",
     "Macy\u2019s parade postponed, a first in 100 years",
     "Nor\u2019easter moves the 100th parade to Saturday, Nov 28.",
     (183, 121, 31), "balloon"),
]


def draw_panel(d, x, y, w, h, story):
    tag, headline, summary, accent, icon_name = story
    d.rounded_rectangle([x, y, x + w, y + h], radius=14,
                        fill=WHITE, outline=BORDER, width=2)
    d.rectangle([x, y + 14, x + 8, y + h - 14], fill=accent)

    pad = 24
    ix, iy = x + pad + 34, y + 36  # icon badge centre
    d.ellipse([ix - 34, iy - 34, ix + 34, iy + 34], fill=accent)
    ICONS[icon_name](d, ix, iy, 34, accent)

    tx = x + pad + 84
    tw = x + w - pad - tx
    f_tag = font("DejaVuSans-Bold.ttf", 21)
    d.text((tx, y + 16), tag, font=f_tag, fill=accent)

    f_head = font("DejaVuSans-Bold.ttf", 32)
    lines = wrap(d, headline, f_head, tw)
    ly = y + 52
    for ln in lines[:3]:
        d.text((tx, ly), ln, font=f_head, fill=INK)
        ly += 40
    headline_bottom = ly - 40 + 34

    f_sum = font("DejaVuSans.ttf", 24)
    slines = wrap(d, summary, f_sum, w - 2 * pad - 8)
    sy = y + h - 24 - len(slines) * 30
    sy = max(sy, headline_bottom + 12)  # never overlap the headline
    for ln in slines:
        d.text((x + pad + 8, sy), ln, font=f_sum, fill=(52, 58, 66))
        sy += 30


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header band ----
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.rectangle([0, 168, W, 172], fill=GOLD)
    f_kick = font("DejaVuSans-Bold.ttf", 26)
    d.text((24, 18), "T H E   W O R L D   I N   O N E   D A Y",
           font=f_kick, fill=GOLD)
    f_date = fit_font(d, "THURSDAY, 26 NOVEMBER 2026",
                      "DejaVuSans-Bold.ttf", 56, W - 48)
    d.text((24, 56), "THURSDAY, 26 NOVEMBER 2026", font=f_date, fill=WHITE)
    f_sub = font("DejaVuSans.ttf", 25)
    d.text((24, 122), "Six stories that defined the day",
           font=f_sub, fill=(196, 205, 214))

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = 24, 192
    pw, ph, gap = 480, 250, 16
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        draw_panel(d, gx + col * (pw + gap), gy + row * (ph + gap),
                   pw, ph, story)

    # ---- footer ----
    f_foot = font("DejaVuSans.ttf", 20)
    foot = ("Sources: Reuters \u00b7 CNN \u00b7 Al Jazeera \u00b7 AP"
            " \u2014 as reported on 26 November 2026")
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, 982), foot, font=f_foot, fill=MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
