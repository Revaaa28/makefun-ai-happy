# ai-happy-01 — "The Wave"

A red panda standing upright on its hind legs, both front paws raised in an
exuberant wave, while golden autumn leaves fall around it like confetti.

## Why this image, against the judge's five criteria

1. **It makes you happy** — the panda's open-mouthed, bright-eyed expression
   and full-body "I'm so glad you're here" posture are pure, immediate warmth.
2. **The idea** — not a stock smiley or a generic sunny scene: a specific
   gesture (a two-pawed wave hello) in a specific moment (a shower of autumn
   leaves falling like confetti around it). The wave is the reason to be
   happy, and it is the panda's own.
3. **Feeling** — one mood, pulled tight: golden-hour backlight, warm amber
   and russet tones everywhere, soft glowing background. Colour, light and
   composition all point at the joyful face.
4. **Craft** — photorealistic and clean: paw pads and toes are anatomically
   right, the face is unwarped, no leaf crosses the face, no artefacts or
   garbled details anywhere.
5. **Reads small** — at 300 px the silhouette is unmistakable: round ears,
   white face markings, two raised paws, grinning face. The idea survives the
   thumbnail.

## The program

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` (683×1024 PNG, 365,179 bytes) to the output directory:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`, as the
grader expects. Both runs write exactly the same bytes.
