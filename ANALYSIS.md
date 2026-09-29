# Dune Filmbook: effect analysis

Source: *Dune | Filmbooks: House Harkonnen* (Warner Bros., YouTube `HQOEfU6Nt9Y`), 1920×1080, 23.976 fps, 1:50.
The House Atreides filmbook (`nL8tdegPQPg`) belongs to the same series and uses the same template.

All measurements are in source pixels at 1080p. Frame counts are at 23.976 fps.
`tools/analyze.sh` regenerates the contact sheets and per-cut frame grids used here.

## Stage

- Background: near-black, RGB 7,7,7 in the corners. Grey smoke drifts slowly in the lower third and up the right edge. The centre stays black.
- Two small star flares sit on the frame edges: top at x≈575, y≈0 and bottom-right at x≈1765, y≈1080. Each has a bluish-white core and a warm fringe, with a faint horizontal streak.
- A dot-matrix screen texture covers everything, with a pitch of about 3px. It is most visible in dark areas and around bright edges, where glows break up into rows of dots.
- Light grain and a soft vignette.

## Cards

- Border, from outside in: 1px dark line, about 3px cream (≈238,228,211), then a 1–2px cool grey line before the image. The warm-outside/cool-inside split reads as chromatic fringing.
- A soft cream halo spreads about 15px outside the border and shows through the dot texture as dotted light.
- Aspect ratios:
  - 2.39:1, most common, 1100–1540px wide
  - 1.85:1
  - portrait pairs at about 0.62:1 with a gap of about 45–60px
  - single concept-art cards at about 0.9:1
- Motion while holding: cards never sit still. They drift a few pixels and scale by about ±4% over a 3–6 s hold. The source clips also move inside the card.
- Colour: some shots are graded heavy sepia and others keep their original colour. Everything looks slightly milky, with lifted blacks and soft highlights.

## Ghost stack

On a stack cut, the old card moves behind the new one:

- scaled to 0.957 per level
- offset +71px right and −50px up per level
- up to two ghosts (three cards in total) near the end of the video

The front card is about 90% opaque, so the ghost's edges show through it. The whole group is centred on the stage.

## Red tags

- Flat red box (≈172,64,53) with cream glyph text (Chakobsa-style script) and a dark red drop shadow.
- One-line title tags are centred on the bottom edge, overlapping the border.
- Paragraph tags (2–5 lines of small glyphs) hang off the bottom-right corner, the top-left corner, the bottom-left, or the right side of a portrait pair.
- A tag moves with its card and does not animate on its own.

## Transitions

| Type | Frames | Behaviour |
|---|---|---|
| Power-on | ~14 | 2 blank frames, then the card at 145%, then 135% (shifted), then one frame with only the tag visible, then 112% easing to 100% over about 9 frames. Used at 0:03.9 after an empty stage. |
| Stack cut | 0 + 6 | Hard cut. The new card lands in front and slides about 30px left, easing out over 6 frames. The previous card becomes the ghost. |
| Push | 8–10 | The old group and the new group move together as one strip with a 60–70px gap, eased in and out. Seen in all four directions. |
| Scale settle | ~6 | Hard cut to the new card at about 112%, easing to 100%. |
| Slam | ~10 | The new card starts bigger than the stage (full bleed) and shrinks to card size with a quartic ease-out. |
| Rapid cuts | 3–5 each | Hard cuts inside the same card, about 5 images in 1 s (the fire montage at 1:18.5). |
| Blink | 1 each | While settling, one card of a pair vanishes for single frames (0:13.5). |
| Blackout | — | The card disappears, leaving smoke and flares only (1:42.7). |

## Shot log

| Time | Transition | Notes |
|---|---|---|
| 0:00.0 | Live action | Paul opens the filmbook device |
| 0:02.3 | Empty stage | 1.7 s of smoke and flares |
| 0:03.9 | Power-on | Sepia 2.39 card, bottom-centre title tag |
| 0:09.7 | Stack cut | First ghost |
| 0:13.5 | Push → | Portrait pair, side tag, left card blinks |
| 0:17.8 | Cut | Dark wide card |
| 0:19.8 | Stack cut | |
| 0:21.4 | Cut-out | Frameless illustration drifts in diagonally with two tags |
| 0:24.2 | Push ← | |
| 0:29.6 | Stack cut | |
| 0:32.8 | Slam | Tag bottom-left |
| 0:42.9 | Push ↑ | Paragraph tag |
| 0:46.3 | Scale settle | |
| 0:52.6 | Push ↓ | |
| 0:58.0 | Push ← | |
| 1:04.8 | Push ↓ | |
| 1:07.2 | Stack cut | |
| 1:09.0 | Push ← | |
| 1:11.2 | Push ↑ | |
| 1:15.2 | Stack cut | Tag top-left |
| 1:18.5 | Rapid cuts | Fire montage |
| 1:27.3 | Cut | Concept-art card |
| 1:34.0 | Stack cut | |
| 1:37.2 | Stack cut | Stack three deep |
| 1:39.5 | Slam | |
| 1:42.7 | Blackout | Then the end card |

## Not replicated

- The live-action opener and the end card.
- The frameless cut-out shot at 0:21.4, which needs a transparent PNG subject.
- Motion inside the cards. The source cards play video clips, while the lab uses stills with a slow push-in.
- The exact Chakobsa font. The lab approximates it with Uncial Antiqua and scrambled letters.
