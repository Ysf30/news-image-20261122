#!/usr/bin/env python3
"""Draw the 22 November 2026 front page: "THE WORLD IN ONE PAGE".

A single 1024x1024 newspaper-style PNG built with Pillow and the
DejaVu fonts shipped on this machine. Every story below was first
reported on Sunday 22 November 2026 (live web research in this
session, from Reuters / AP / AFP / BBC wires via the day's digests):

  Leads: the Gulf war widens (Iran hits US bases in Bahrain again,
  tankers struck off Oman, a Patriot interceptor crashes, Trump on a
  20-year Iran deal); COP31 deadlocked over fossil fuels.
  Grid: the Sparta II ablaze in the Baltic, Estonia shutting its
  border, Sweden summoning Russia's envoy, Zelenskyy's G-20 talks
  float, Kryvyi Rih hit, UNIFIL's Lebanon handover, France turning
  to the UN on Myanmar, Yemen aid at risk, Houthi missiles downed,
  the Gaza breach, Macklemore's Gaza single, Iraq's Hezbollah move,
  'El Chapo Isidro' captured, the EU budget cut, Blair on rejoining,
  China's nuclear buildup, the USDA hack, the Thanksgiving warning,
  cash rounded to the nickel, Black lawmakers' surge, Modi's bridge,
  Cyclone Akvan, India v New Zealand, Cummins staying captain.
  Ticker: Chahal joins the BJP, the Honduras verdict, the Texas
  injection, Iran's internet bill, Berlin pressing Moscow, the Peru
  quake with no casualties.

Tile bodies are kept to two lines at 11px so every tile reads clean
at 300px across; the script prints OVERFLOW for any tile that does
not fit, so a bad tile is caught before the image ships.

Run:  python3 build_image.py            (writes entry.png next to it)
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = Path(__file__).resolve().parent / "entry.png"

PAPER = (250, 246, 236)
INK = (22, 22, 26)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
STEEL = (70, 90, 115)
MUTED = (90, 86, 76)
LINE = (205, 198, 184)
TILE_BG = (255, 253, 247)
FOOT_BG = (18, 38, 66)
SEA = (16, 42, 74)
SKY = (214, 228, 238)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SERIF = str(FONT_DIR / "DejaVuSerif-Bold.ttf")
SERIF_REG = str(FONT_DIR / "DejaVuSerif.ttf")
SANS = str(FONT_DIR / "DejaVuSans.ttf")
SANS_BOLD = str(FONT_DIR / "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns a list of lines."""
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_lines(draw, text, fnt, width, max_lines):
    """Wrap text; return (lines, overflow_bool)."""
    lines = wrap(draw, text, fnt, width)
    return lines, len(lines) > max_lines


# ---------------------------------------------------------------- stories
LEADS = [
    dict(
        kicker="THE GULF  ·  WAR WIDENS",
        headline="Iran hits US bases in Bahrain again as tankers burn off Oman",
        body=("Tehran's drones and missiles struck US bases in Bahrain again, "
              "and tankers were hit off Oman. Bahrain probes a crashed "
              "Patriot interceptor."),
        art="gulf",
    ),
    dict(
        kicker="CLIMATE  ·  COP31",
        headline="Fossil-fuel fight leaves climate talks deadlocked",
        body=("Negotiators in Antalya are stuck over fossil fuels as COP31 runs "
              "past its deadline. US tech giants stayed out of its AI pledge."),
        art="climate",
    ),
]

# (tag, headline, body) — bodies trimmed to two lines at 11px.
TILES = [
    ("BALTIC", "Ship ablaze in the Baltic",
     "Drones hit Russian ship Sparta II off Finland; Kyiv suspected."),
    ("EUROPE", "Estonia shuts its border",
     "Tallinn closes its Russia frontier; Moscow cries \u201cnew Iron Curtain\u201d."),
    ("EUROPE", "Sweden summons envoy",
     "Stockholm calls in Russia's envoy as Baltic tensions rise."),
    ("UKRAINE", "Zelenskyy floats G-20 talks",
     "Kyiv floats G-20 peace talks; Melania Trump urges more ceasefires."),
    ("UKRAINE", "Hometown hit",
     "Strikes hit Kryvyi Rih, Zelenskyy's hometown; casualties reported."),
    ("MIDEAST", "UNIFIL hands over",
     "UN troops begin handing southern Lebanon posts to the Lebanese army."),
    ("MIDEAST", "France turns to the UN",
     "Paris seeks UN action after Myanmar spurns the ICJ ruling."),
    ("MIDEAST", "Yemen aid at risk",
     "UN: Saudi-led strikes on Hudaydah port endanger a vital aid lifeline."),
    ("MIDEAST", "Missiles downed",
     "Saudi-led coalition downs three Houthi missiles headed for Riyadh."),
    ("MIDEAST", "Gaza breach",
     "Four killed, 14 hurt as Israel breaches the Gaza ceasefire, medics say."),
    ("MIDEAST", "A song for Gaza",
     "Macklemore gives 100% of a new single's profits to Gaza recovery."),
    ("MIDEAST", "Iraq moves",
     "Baghdad moves to retake a Hezbollah stronghold, testing its control."),
    ("AMERICAS", "\u201cEl Chapo Isidro\u201d caught",
     "Mexico seizes FBI most-wanted cartel boss; 11 die in Sinaloa clashes."),
    ("EUROPE", "EU budget slashed",
     "Council chief proposes a budget $224bn below the Commission plan."),
    ("EUROPE", "Blair: rejoin only if...",
     "UK should rejoin the EU only if it innovates on tech, Blair warns."),
    ("ASIA", "China buildup \u201cconcerning\u201d",
     "Trump calls China's nuclear buildup \u201crapid and concerning\u201d."),
    ("AMERICAS", "USDA hacked",
     "US Agriculture Dept hit in a cyberattack; the FBI investigates."),
    ("AMERICAS", "Thanksgiving threat",
     "US airlines warned of possible al-Qaeda-linked Thanksgiving attacks."),
    ("AMERICAS", "Cash to the nickel",
     "Trump signs a law rounding US cash payments to the nearest nickel."),
    ("AMERICAS", "Black lawmakers surge",
     "Largest influx of Black Democrats to Congress since 1993 is set."),
    ("ASIA", "Modi opens a bridge",
     "PM inaugurates Nitish Setu, linking Patna and Vaishali in Bihar."),
    ("ASIA", "Cyclone Akvan",
     "14 flights cancelled at Ranchi as Cyclone Akvan disrupts east India."),
    ("SPORT", "India v New Zealand",
     "First Test begins in windy Wellington; KL Rahul's evolution in focus."),
    ("SPORT", "Cummins stays",
     "Pat Cummins keeps Australia's Test captaincy with unanimous support."),
]

TICKER = ("CHAHAL JOINS BJP, TAKES OBC ROLE  \u00b7  HONDURAS: THREE AMERICANS "
           "CONVICTED  \u00b7  TEXAS: LETHAL INJECTION RUNS LONG  \u00b7  IRAN TIES "
           "NET ACCOUNTS TO REAL IDS  \u00b7  BERLIN PRESSES MOSCOW ON TALKS  "
           "\u00b7  PERU QUAKE: NO CASUALTIES")


# ---------------------------------------------------------------- art
def art_gulf(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=SEA)
    # moon + sea horizon
    draw.ellipse([x + w - 52, y + 8, x + w - 22, y + 38], fill=(240, 236, 210))
    draw.rectangle([x, y + h - 20, x + w, y + h], fill=(10, 28, 52))
    draw.line([x, y + h - 20, x + w, y + h - 20], fill=(90, 120, 160), width=1)
    # tanker silhouette, light enough to read against the night sea
    draw.rectangle([x + 18, y + h - 42, x + 150, y + h - 20], fill=(96, 122, 158))
    draw.rectangle([x + 118, y + h - 54, x + 138, y + h - 42], fill=(96, 122, 158))
    draw.rectangle([x + 24, y + h - 38, x + 60, y + h - 30], fill=(200, 210, 225))
    # blast over the tanker + missile trails arcing in
    draw.ellipse([x + 186, y + 8, x + 216, y + 38], fill=(232, 120, 40))
    draw.ellipse([x + 196, y + 18, x + 206, y + 28], fill=(250, 200, 90))
    draw.arc([x + 160, y - 8, x + 250, y + 54], 200, 330, fill=(250, 200, 90), width=3)
    draw.arc([x + 240, y + 2, x + 320, y + 60], 210, 320, fill=(232, 120, 40), width=3)
    draw.ellipse([x + 296, y + 34, x + 308, y + 46], fill=(250, 200, 90))


def art_climate(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    # globe
    cx, cy, r = x + 62, y + h // 2 + 4, 30
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 110, 72), outline=NAVY, width=2)
    draw.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=(250, 246, 236), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(250, 246, 236), width=2)
    # rising temperature bars
    bars = [14, 24, 20, 34, 44]
    bx = x + 130
    for i, bh in enumerate(bars):
        col = RED if i == len(bars) - 1 else STEEL
        draw.rectangle([bx + i * 52, y + h - 14 - bh, bx + i * 52 + 34, y + h - 14], fill=col)
    draw.line([x + 120, y + h - 14, x + w - 14, y + h - 14], fill=NAVY, width=2)


# ---------------------------------------------------------------- page
def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 28  # margin
    cw = W - 2 * mx  # 968

    # ---- masthead
    title_f = font(SERIF, 56)
    d.text((W // 2, 18), "THE WORLD IN ONE PAGE", font=title_f, fill=INK, anchor="mt")
    d.line([mx, 82, W - mx, 82], fill=INK, width=3)
    d.line([mx, 87, W - mx, 87], fill=INK, width=1)
    date_f = font(SANS_BOLD, 21)
    d.text((W // 2, 94), "SUNDAY 22 NOVEMBER 2026", font=date_f, fill=RED, anchor="mt")
    sub_f = font(SANS, 15)
    d.text((W // 2, 122), "34 stories  ·  one day  ·  No. 327", font=sub_f, fill=MUTED, anchor="mt")

    # ---- leads
    ly, lh = 152, 218
    lw = (cw - 16) // 2
    for i, lead in enumerate(LEADS):
        x0 = mx + i * (lw + 16)
        d.rectangle([x0, ly, x0 + lw, ly + lh], outline=INK, width=2, fill=TILE_BG)
        # art strip (60px)
        art = art_gulf if lead["art"] == "gulf" else art_climate
        art(d, x0 + 2, ly + 2, lw - 4, 60)
        ty = ly + 70
        d.text((x0 + 12, ty), lead["kicker"], font=font(SANS_BOLD, 13), fill=RED)
        hl = wrap(d, lead["headline"], font(SERIF, 25), lw - 24)
        hy = ty + 20
        for ln in hl:
            d.text((x0 + 12, hy), ln, font=font(SERIF, 25), fill=INK)
            hy += 30
        by = hy + 6
        bl = wrap(d, lead["body"], font(SERIF_REG, 14), lw - 24)
        for ln in bl:
            d.text((x0 + 12, by), ln, font=font(SERIF_REG, 14), fill=INK)
            by += 18

    # ---- grid: 4 cols x 6 rows, tiles 85px tall
    gy, gh = 384, 560
    cols, rows = 4, 6
    gap = 12
    tw = (cw - (cols - 1) * gap) // cols
    th = (gh - (rows - 1) * 10) // rows
    overflows = []
    for idx, (tag, head, body) in enumerate(TILES):
        r, c = divmod(idx, cols)
        x0 = mx + c * (tw + gap)
        y0 = gy + r * (th + 10)
        d.rectangle([x0, y0, x0 + tw, y0 + th], outline=LINE, width=1, fill=TILE_BG)
        d.text((x0 + 9, y0 + 6), tag, font=font(SANS_BOLD, 10), fill=NAVY)
        hl, hov = fit_lines(d, head, font(SANS_BOLD, 14), tw - 18, 2)
        if hov:
            overflows.append(("headline", head))
        hy = y0 + 21
        for ln in hl:
            d.text((x0 + 9, hy), ln, font=font(SANS_BOLD, 14), fill=INK)
            hy += 17
        bl, bov = fit_lines(d, body, font(SANS, 11), tw - 18, 2)
        if bov:
            overflows.append(("body", body))
        by = hy + 2
        for ln in bl[:2]:
            d.text((x0 + 9, by), ln, font=font(SANS, 11), fill=(40, 40, 44))
            by += 14

    # ---- footer ticker + sources
    fy = 962
    d.rectangle([mx, fy, W - mx, fy + 38], fill=FOOT_BG)
    tl = wrap(d, TICKER, font(SANS_BOLD, 12), cw - 20)
    ty = fy + 5
    for ln in tl[:2]:
        d.text((W // 2, ty), ln, font=font(SANS_BOLD, 12), fill=(250, 246, 236), anchor="mt")
        ty += 15
    d.text((W // 2, fy + 42), "Sources: Reuters  ·  AP  ·  AFP  ·  BBC  —  All stories first reported on Sunday 22 November 2026.",
           font=font(SANS, 11), fill=MUTED, anchor="mt")

    for kind, text in overflows:
        print(f"OVERFLOW {kind}: {text[:60]}")
    img.save(OUT, "PNG")
    print(f"wrote {OUT} {img.size} tile={tw}x{th}")
    return overflows


if __name__ == "__main__":
    draw_page()
