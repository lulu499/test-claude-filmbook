#!/usr/bin/env python3
"""Track the bright card edges on every frame of a filmbook video and fit the hold motion.

Usage: python3 tools/track_cards.py video.mp4 [out.json]
Needs: pip install opencv-python-headless numpy

Prints one line per hold: time range, size change, shrink rate in %/s, and centre drift.
The JSON holds [frame, x0, x1, y0, y1, mean_luma] per frame (-1 when no card edge is found).
"""
import json
import sys

import cv2
import numpy as np

FPS = 23.976


def track(path):
    cap = cv2.VideoCapture(path)
    out, i = [], 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        m = g > 150
        ry = np.where(m.sum(1) > 150)[0]
        cx = np.where(m.sum(0) > 80)[0]
        box = [int(cx[0]), int(cx[-1]), int(ry[0]), int(ry[-1])] if len(ry) and len(cx) else [-1, -1, -1, -1]
        out.append([i, *box, round(float(g.mean()), 2)])
        i += 1
    return out


def holds(rows):
    segs, cur = [], [rows[0]]
    for a, b in zip(rows, rows[1:]):
        smooth = a[1] >= 0 and b[1] >= 0 and abs((b[2] - b[1]) - (a[2] - a[1])) < 8 \
            and abs((b[1] + b[2]) - (a[1] + a[2])) < 12 and abs((b[3] + b[4]) - (a[3] + a[4])) < 12
        if smooth:
            cur.append(b)
        else:
            segs.append(cur)
            cur = [b]
    segs.append(cur)
    return [s for s in segs if len(s) >= 12]


def main():
    rows = track(sys.argv[1])
    if len(sys.argv) > 2:
        json.dump(rows, open(sys.argv[2], 'w'))
    for s in holds(rows):
        f = np.array([r[0] for r in s]) / FPS
        w = np.array([r[2] - r[1] for r in s])
        cx = np.array([(r[1] + r[2]) / 2 for r in s])
        cy = np.array([(r[3] + r[4]) / 2 for r in s])
        k = int(len(s) * .3)                      # skip the settle at the start of a hold
        dw = np.polyfit(f[k:], w[k:], 1)[0]
        print(f'{f[0]:6.2f}-{f[-1]:6.2f}s  w {w[0]:4d}->{w[-1]:4d}  {100 * dw / w.mean():+5.2f}%/s  '
              f'centre ({cx[0]:.0f},{cy[0]:.0f})->({cx[-1]:.0f},{cy[-1]:.0f})')


if __name__ == '__main__':
    main()
