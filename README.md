# news-image-20261122 — "THE WORLD IN ONE PAGE"

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Ysf30/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/Ysf30/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

Sum up Sunday 22 November 2026's world news in one image.

## The image

A single-page newspaper front page, 1024×1024, drawn with Pillow and
DejaVu fonts (`build_image.py` → `entry.png`):

- **Masthead:** THE WORLD IN ONE PAGE — Sunday 22 November 2026
- **Lead 1:** Gulf war widens — Iran hits US bases in Bahrain again,
  tankers struck off Oman, Bahrain probes a crashed Patriot
  interceptor; Trump: Iran deal "could last 20 years".
- **Lead 2:** COP31 deadlocked over fossil fuels in Antalya.
- **24 more stories** in a three-column grid: Sparta II ablaze in the
  Baltic, Estonia shuts its border, Sweden summons Russia's envoy,
  Zelenskyy floats G-20 talks, Kryvyi Rih hit, UNIFIL Lebanon
  handover, France turns to the UN on Myanmar, Yemen aid at risk,
  Houthi missiles downed, Gaza breach, Macklemore's Gaza single, Iraq
  moves on Hezbollah, 'El Chapo Isidro' caught (11 killed in
  Sinaloa), EU budget slashed $224bn, Blair on rejoining, China's
  nuclear buildup, USDA hacked, Thanksgiving threat warning, cash
  rounded to the nickel, Black lawmakers surge, Modi opens Nitish
  Setu, Cyclone Akvan, India v New Zealand 1st Test, Cummins stays
  captain.
- **Footer ticker:** Chahal joins BJP, Honduras verdict (3 Americans
  convicted), Texas lethal injection, Iran internet bill, Berlin
  presses Moscow, Peru quake no casualties.

All stories were reported on 22 November 2026 (Reuters/AP/AFP/BBC
wires via the day's news digests, researched live in this session).

## Files

- `build_image.py` — draws `entry.png` (Pillow; run `python3 build_image.py`)
- `main.py` — entry point: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  byte for byte (stdlib only, no network, deterministic)
- `entry.png` — the submitted image

## Verify

```sh
python3 build_image.py
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
md5sum entry.png /tmp/out1/entry.png /tmp/out2/entry.png
# all three identical: 97d9acd854ce418a9ebb48102cc3e391
# entry.png: 1024x1024, 140,440 bytes — inside the 1 MiB / 1024x1024 caps
```
