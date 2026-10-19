"""Precompute 'spreading territory' regions between two map states."""
import pickle, math
import numpy as np
from PIL import Image, ImageDraw
import worldmap as M

W = 7200
P = M.Proj(W)

def emp_masks(data):
    M.WD = data
    land, emp = M.masks(W, ss=1)
    out = {}
    for (name, col, polys, lab), m in zip(data.EMPIRES, emp):
        out[name] = np.array(m) > 110
    return np.array(land) > 110, out

def poly_mask(pts, shape):
    im = Image.new("L", (shape[1], shape[0]), 0)
    ImageDraw.Draw(im).polygon(P.poly(pts), fill=255)
    return np.array(im) > 0

def make_region(mask, origin, noise_amp=0.14, seed=1):
    ys, xs = np.nonzero(mask)
    if len(xs) == 0: return None
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    sub = mask[y0:y1, x0:x1]
    ox, oy = P(*origin)
    yy, xx = np.mgrid[y0:y1, x0:x1]
    d = np.sqrt((xx - ox) ** 2 + (yy - oy) ** 2)
    rng = np.random.default_rng(seed)
    nh, nw = max(2, (y1 - y0) // 40 + 2), max(2, (x1 - x0) // 40 + 2)
    n = rng.normal(0, 1, (nh, nw)).astype(np.float32)
    n = np.array(Image.fromarray(((n + 3) * 40).clip(0, 255).astype(np.uint8)).resize((x1 - x0, y1 - y0), Image.BICUBIC)).astype(np.float32)
    n = (n - 120) / 40
    dmax_raw = d[sub].max()
    d = d + n * noise_amp * dmax_raw
    d[~sub] = np.inf
    dmin = d[sub].min(); d = d - dmin
    return dict(bbox=(int(x0), int(y0), int(x1), int(y1)), dist=d.astype(np.float32), maxd=float(d[sub].max()))

def build(A, B, specs, out):
    landA, mA = emp_masks(A)
    landB, mB = emp_masks(B)
    shape = landA.shape
    assigned = np.zeros(shape, bool)
    regions = {}
    for sp in specs:
        nm = sp["empire"]
        if sp.get("mode", "gain") == "gain":
            m = mB[nm] & ~mA.get(nm, np.zeros(shape, bool))
        else:  # retreat: area held in B that is given up
            m = mB[nm].copy()
        if "clip" in sp: m &= poly_mask(sp["clip"], shape)
        if sp.get("exclusive", True) and sp.get("mode", "gain") == "gain":
            m &= ~assigned; assigned |= m
        r = make_region(m, sp["origin"], seed=len(regions) + 3)
        if r is None: print("empty region", sp["key"]); continue
        r.update(key=sp["key"], color=sp["color"], src=sp.get("src", "B"))
        regions[sp["key"]] = r
        print(sp["key"], r["bbox"], int(r["maxd"]))
    pickle.dump(regions, open(out, "wb"))
