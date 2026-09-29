# Filmbook Lab

A browser recreation of the card effects from Warner Bros.' *Dune* “Filmbooks” videos, measured frame by frame from *House Harkonnen*. The cards play video: built-in animated scenes, or your own footage, where each card plays a random 8-second segment.

Open `index.html` in a browser that supports WebGL. It needs no build step and has no dependencies.

- **Replay mode**, the default, plays the House Harkonnen timeline shot for shot: same cues, layouts, tags and transition curves.
- **Random mode** picks transitions and layouts with the same frequencies as the video. Keys `1`–`7` force a transition.
- **Your own footage:** drop videos (MP4, WebM, MOV) or images on the page. A Dune trailer works well. Uploaded footage plays in the framed cards only; the frameless cut-out shot always uses the built-in specimen drawing.

Files:

- `index.html`: the lab. A WebGL renderer, built-in clips, the transition engine, the timeline and the controls.
- `ANALYSIS.md`: the frame-accurate breakdown, with measurements, shot log and method.
- `tools/track_cards.py`: tracks card edges on every frame and fits the hold motion.
- `tools/analyze.sh`: contact sheets and per-cut frame grids.

Keys: `→` next shot, `Space` pause.
