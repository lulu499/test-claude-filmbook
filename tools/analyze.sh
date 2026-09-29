#!/usr/bin/env bash
# Frame analysis helpers used to reverse-engineer the filmbook effects.
# Usage: tools/analyze.sh path/to/video.mp4 [outdir]
set -euo pipefail
V="$1"; OUT="${2:-analysis}"; mkdir -p "$OUT"

# 1. Overview: one frame per second, 30 per sheet
ffmpeg -hide_banner -loglevel error -y -i "$V" -vf "fps=1,scale=384:-1,tile=6x5" -q:v 3 "$OUT/sheet_%02d.jpg"

# 2. Transition timestamps (scene score above 0.08 on a downscaled copy)
ffmpeg -hide_banner -loglevel error -i "$V" -vf "scale=240:135,select='gt(scene,0.08)',metadata=print:file=$OUT/scenes.txt" -vsync vfr -f null -
grep -o "pts_time:[0-9.]*" "$OUT/scenes.txt" | cut -d: -f2 > "$OUT/cuts.txt"

# 3. Every frame of half a second around each cut (6x2 grid, 24 fps)
while read -r t; do
  s=$(python3 -c "print(max(0, $t - 0.2))")
  ffmpeg -hide_banner -loglevel error -y -ss "$s" -t 0.5 -i "$V" -vf "scale=400:-1,tile=6x2" -frames:v 1 -q:v 3 "$OUT/cut_$t.jpg"
done < "$OUT/cuts.txt"

echo "Wrote sheets, cuts.txt and per-cut frame grids to $OUT/"
