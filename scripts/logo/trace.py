"""Retraces the ORBIT logo from brand/logo-concept-orbit-FINAL.jpg into clean SVG paths (potrace via potracer).
Run with a venv that has: potracer opencv-python-headless numpy pillow. Output: scripts/logo/trace.json (paths in source px)."""
import json, sys, numpy as np, cv2, potrace
SRC = sys.argv[1] if len(sys.argv) > 1 else "/workspace/nynz/brand/logo-concept-orbit-FINAL.jpg"
im = cv2.imread(SRC); S = 4  # upsample for smooth edges
x0, y0, x1, y1 = 90, 170, 710, 400
c = im[y0:y1, x0:x1]; c = cv2.resize(c, None, fx=S, fy=S, interpolation=cv2.INTER_CUBIC)
b, g, r = [c[..., i].astype(int) for i in range(3)]
white = ((np.minimum(np.minimum(r, g), b) > 150)).astype(np.uint8)
orange = ((r > 170) & (b < 120) & (r - b > 90)).astype(np.uint8)
def trace(mask, turd=400, opt=0.6):
    mask = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 1.6) > 0.5
    bm = potrace.Bitmap(~mask)
    pl = bm.trace(turdsize=turd, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=0.9, opticurve=True, opttolerance=opt)
    d = []
    f = lambda p: f"{p.x/S+x0:.2f} {p.y/S+y0:.2f}"
    for cv in pl:
        d.append("M" + f(cv.start_point))
        for s in cv.segments:
            if s.is_corner: d.append("L" + f(s.c) + " L" + f(s.end_point))
            else: d.append("C" + f(s.c1) + " " + f(s.c2) + " " + f(s.end_point))
        d.append("Z")
    return "".join(d)
out = {"white": trace(white), "orange": trace(orange, 200)}
ys, xs = np.where(white > 0); ow = np.where(orange > 0)
out["bbox_white"] = [xs.min()/S+x0, ys.min()/S+y0, xs.max()/S+x0, ys.max()/S+y0]
out["bbox_orange"] = [ow[1].min()/S+x0, ow[0].min()/S+y0, ow[1].max()/S+x0, ow[0].max()/S+y0]
json.dump(out, open("trace.json", "w"))
print(out["bbox_white"], out["bbox_orange"], len(out["white"]), len(out["orange"]))
