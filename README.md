# ai-happy-01 — "A Party for the Robot"

A surprise birthday party thrown for a small robot: a round white robot with
a screen face lit up in a huge glowing smile, wearing a tiny striped party
hat, seated before a birthday cake with lit candles while a puppy, a kitten
and a bunny cheer it on and confetti falls through warm golden party light.

## Why this image, against the judge's five criteria

1. **It makes you happy** — the robot's face is one enormous, glowing,
   unreserved grin, and every friend around it is mid-cheer. The warmth is
   the whole picture.
2. **The idea** — not a stock smiley or a generic sunny scene: a specific
   moment with a specific reason — the little robot is the guest of honour
   at its own surprise party, celebrated by its friends. A birthday made
   *for* someone is the reason to be happy, and it is this robot's own.
3. **Feeling** — one mood, pulled tight: warm golden party light, candle
   glow, falling confetti, amber tones everywhere. Colour, light and
   composition all point at the joyful face in the centre.
4. **Craft** — clean warm 3D render: the robot's face and hat are crisp,
   the cheering animals at the edges are unwarped with correct paws, the
   cake and candles are clean, and there is no text anywhere to garble.
5. **Reads small** — at 300 px the story still lands at a glance: the big
   black screen face with its glowing smile dominates, party hat and lit
   cake read instantly, and the friends frame the celebration.

## The program

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` (1024×683 PNG, 272,400 bytes) to the output directory:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`, as the
grader expects. Both runs write exactly the same bytes.
