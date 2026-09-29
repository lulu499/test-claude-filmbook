# Filmbook Lab

A browser recreation of the card effects from Warner Bros.' *Dune* “Filmbooks” videos. It uses random images: generated Dune plates, photos from picsum.photos, or your own uploads.

Open `index.html` in a browser. It needs no build step and has no dependencies.

- `index.html`: the lab. Canvas renderer, transition engine and controls.
- `ANALYSIS.md`: frame-by-frame breakdown of the source video, with measurements and a shot log.
- `tools/analyze.sh`: the ffmpeg commands used to produce the contact sheets and per-cut frame grids.

Keys: `→` next image, `Space` pause, `1`–`7` force a transition. The transitions are stack cut, push, scale settle, slam, power-on, rapid cuts and blackout.
