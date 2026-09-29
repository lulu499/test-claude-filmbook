# Dune Filmbook: effect analysis

Source: *Dune | Filmbooks: House Harkonnen* (Warner Bros., YouTube `HQOEfU6Nt9Y`), 1920×1080, 23.976 fps, 1:50, 2,637 frames.
The House Atreides filmbook (`nL8tdegPQPg`) belongs to the same series and uses the same template.

All values are in source pixels at 1080p. Frame counts are at 23.976 fps.

## Method

- `tools/track_cards.py` finds the bright card edges on every frame. It splits the video into holds and fits size and centre over time, which gives the hold motion and the transition curves.
- Per-frame border-line detection in the transition windows gives the push, zoom and slam easing.
- FFT and phase-folded profiles give the texture pitches (card mesh, screen grid) and their contrast.
- Per-pixel RGB profiles across card edges give the border, glow and colour fringing.
- The ghost-card fade comes from regressing ghost pixels against the same card before the stack cut.
- `tools/analyze.sh` makes contact sheets and per-cut frame grids.
- The lab was checked by stepping it frame by frame at 23.976 fps, running the same edge tracker on its output, and comparing against the source numbers. Most transitions now match to within a few pixels and one frame.

## Stage

- **Background.** One static cloud plate for the whole video; it doesn't pan during pushes (phase correlation shows 0 px shift).
  - Corners are RGB 7,7,7 and the median luminance is 10.
  - Smoke is concentrated in the bottom-right. Along the bottom strip, luminance rises from about 8 on the left to about 52 on the right.
- **Screen grid.** A fixed 3.0px grid covers the background only (measured period 3.00–3.01px on both axes) and is strongly visible.
- **Flares.** Two constant flares that don't twinkle (peak 243–249 all video):
  - top at x≈575, with an amber fringe on one side and a faint downward spill
  - bottom-right at x≈1765, with soft starburst rays
- **Dust.** About 5 small specks drift at 3–5px per second.
- **Fades.** The stage fades up from black over 12 frames at 0:02.3.

## Cards

- **LED mesh.** The mesh is attached to each card and is always 300 cells across the card width.
  - The pitch follows the card as it shrinks: 4.36px at 1308 wide, 4.16 at 1248, 3.98 at 1194, 3.85 at 1154.
  - Contrast is about 10% peak-to-peak on content after YouTube compression. It's much stronger on the border and the halo just outside, which makes the edges look dotted.
- **Border.** A single cream stroke about 3.6px wide (≈238,228,211).
  - The two-tone look comes from colour fringing: blue is shifted down-right, giving an amber fringe on the top and left and a cool one on the right.
  - An inner glow fades over 8–10px. A faint halo sits outside, biased up-left.
- **Tone.** The darkest 1% of card pixels sits at about 9 and highlights top out around 240. Some shots are graded heavy sepia and others keep their colour.
- **Flicker.** Even still concept art varies in brightness by ±2–3% from frame to frame.
- **Sizes at hold start:**
  - scope 2.39:1 cards, 1250–1450 wide (the first card is 1657)
  - 16:9 cards, 1348×759
  - portrait pairs, 477×739 and 458×712, with a 68px gap
  - concept-art cards, 762×835 and 711×913

## Hold motion

Every hold, 30 of them measured, follows one rule. The whole layout shrinks linearly by about 2.2% of its size per second, anchored at the exact frame centre (959, 539). It never grows and never drifts sideways. Stacked cards shrink toward the centre too, so a stack drifts slowly as it shrinks.

## Transitions

| Type | Count | Measured behaviour |
|---|---|---|
| Push | 11 | Shots sit one full screen apart, and the camera pans 1,900px sideways or 1,060px vertically. Position follows a Laplace CDF with k≈0.38 per frame: speed grows ×1.5 per frame, peaks at about 300px per frame, then decays ×0.68 per frame. About 26 frames in all. |
| Stack cut | 9 | The old card stays exactly where it is and powers down: desaturated, lifted toward grey (≈0.45·c + 0.18), with a stronger mesh. Its clip keeps playing. The new card lands in front about 4% bigger, offset (−78, +52), and is about 90% opaque. The ghost blinks off 2 frames after the cut. The stack reaches 3 deep. |
| Zoom-through | 3 | The old card accelerates away (×1.4 per frame) for about 6 frames down to 90–94%. After a cut, the new card lands at 110–118% and decays ×0.45 to ×0.68 per frame. |
| Slam | 2 | Hard cut to a card at about 185% (full-bleed for 4 frames). It decays ×0.76 per frame at 0:32.8 and ×0.83 at 1:39.5. |
| Power-on | 1 | Black, then full-bleed, then 155%, then one blank frame showing only the tag, then 114% decaying ×0.72 per frame. This matched the source within about 5px on every frame. |
| Power-off | 1 | On, half, off, on, half, off. |
| Hard cut | 1 | Concept art at 1:27.3. |
| Rapid cuts | 1 | Fire clips swap inside one card after 3, 1, 5, 3, 4 and 6 frames. |
| Blink | 1 | The left card of the portrait pair drops out for single frames while landing. |

## Tags

- **Appearance.** Flat dark red boxes, about 92% opaque (≈158,54,46), with an embossed Coptic-style glyph script: a dark red shadow down-right and a light bevel up-left. They appear with their card and have no animation.
- **Title tags** are about 60px tall, with a 25px glyph em and wide spacing (for example 296×60 with 9 glyphs).
- **Paragraph tags** are 350–650px wide with 23.5px line spacing. The first line is a quoted title.
- **Positions**, relative to the card:

| Position | Tag placement |
|---|---|
| Bottom title | Centred, top edge 12px above the card's bottom edge |
| Pair title | Overlaps the right card's right edge by 36px, vertically centred |
| Bottom-right paragraph | Right edge 90px past the card, top edge 74px above the card's bottom |
| Top-left paragraph | 84px left of the card, 75px above it |
| Bottom-left paragraph | 67px left of the card, 27px below it |

## Shot log

| Time | Transition | Notes |
|---|---|---|
| 0:02.3 | Fade in | Empty stage for 1.7 s |
| 0:03.9 | Power-on | Card 1657 wide, bottom title tag |
| 0:09.7 | Stack cut | Ghost blinks at frame 234 |
| 0:13.5 | Push → | Portrait pair, side title tag, left card blinks |
| 0:17.8 | Zoom-through | |
| 0:19.8 | Stack cut | |
| 0:21.4 | Push ↓ | Frameless cut-out with a title tag and a paragraph tag |
| 0:24.2 | Push ← | |
| 0:29.6 | Stack cut | |
| 0:32.8 | Slam | Bottom-left paragraph tag |
| 0:38.9 | Push ← | Bottom-right paragraph tag |
| 0:42.1 | Push ↑ | |
| 0:44.0 | Stack cut | |
| 0:46.3 | Zoom-through | |
| 0:49.0 | Zoom-through | |
| 0:52.5 | Push ↓ | 16:9 card |
| 0:57.9 | Push → | |
| 1:04.8 | Push ↓ | |
| 1:07.2 | Stack cut | |
| 1:08.9 | Push ← | |
| 1:11.1 | Push ↑ | Bottom-right paragraph tag |
| 1:15.2 | Stack cut | Top-left paragraph tag |
| 1:18.0 | Zoom-through, then rapid cuts | |
| 1:19.5 | Cut | |
| 1:23.6 | Push → | |
| 1:27.3 | Cut | Concept art |
| 1:30.9 | Stack cut | Concept art |
| 1:32.6 | Push ↓ | |
| 1:34.0 | Stack cut | |
| 1:37.2 | Stack cut | Three deep |
| 1:39.5 | Slam | |
| 1:42.7 | Power-off | Then the end card |

Push times are the moment of peak speed. The lab starts each push 13 frames earlier so that its peak lands on the same frame.

## Corrections from the first pass

| First pass | Measured in this pass |
|---|---|
| Random drift, growing or shrinking | Always a linear 2.2%/s shrink toward the centre |
| Pushes of about 0.4 s with a 60px gap | About 1.1 s, a full screen apart, Laplace easing |
| Ghost pushed back and scaled 0.957 | Ghost stays put and powers down; the new card lands offset and bigger |
| Fixed 3px dot mask over everything | A 300-cell mesh per card, plus a separate 3px grid on the background only |
| Smoke drifting everywhere | Static plate, bottom-right bank |
| Flares that twinkle | Constant |
| Border in two colours | One cream stroke plus colour fringing |

## Not replicated

- The live-action opener and the end card.
- The real film footage. The lab plays built-in animated scenes, or whatever videos you load.
- The exact Chakobsa typeface. The lab draws its own Coptic-style glyph set.
- Narration, music and sound design.
