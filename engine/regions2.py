"""Spreading regions on the detailed Mercator map."""
import pickle
import numpy as np
from PIL import Image, ImageDraw
import geo
from regions import make_region as _mr
import regions as R0
R0.P = geo.P
Image.MAX_IMAGE_PIXELS = None
LAND = None

def masks(data):
    land = np.asarray(Image.open("/home/claude/shortgen/hd_land.png").convert("L")) > 110
    out = {}
    for name, col, polys, lab in data.EMPIRES:
        im = Image.new("L", (geo.W, geo.H), 0); d = ImageDraw.Draw(im)
        for pts in polys: d.polygon(geo.P.poly(pts), fill=255)
        out[name] = (np.asarray(im) > 0) & land
    if getattr(data, "EXCLUSIVE", False):
        names = [e[0] for e in data.EMPIRES]
        for i, nm in enumerate(names):
            for nm2 in names[i + 1:]: out[nm] = out[nm] & ~out[nm2]
    return out

def poly_mask(pts):
    im = Image.new("L", (geo.W, geo.H), 0); ImageDraw.Draw(im).polygon(geo.P.poly(pts), fill=255)
    return np.asarray(im) > 0

_mc = {}
def _masks(D):
    if D.__name__ not in _mc: _mc[D.__name__] = masks(D)
    return _mc[D.__name__]

def build(A, B, specs, out, merge=None):
    mA, mB = _masks(A), _masks(B)
    shape = (geo.H, geo.W); assigned = np.zeros(shape, bool); regs = {}
    for sp in specs:
        nm = sp["empire"]
        if sp.get("mode", "gain") == "gain":
            m = mB[nm] & ~mA.get(nm, np.zeros(shape, bool))
        else:
            m = mB[nm].copy()
        if "clip" in sp: m &= poly_mask(sp["clip"])
        if sp.get("mode", "gain") == "gain": m &= ~assigned; assigned |= m
        r = _mr(m, sp["origin"], seed=len(regs) + 3)
        if r is None: print("empty", sp["key"]); continue
        r.update(key=sp["key"], color=sp["color"], src=sp.get("src", "B")); regs[sp["key"]] = r
        print(sp["key"], r["bbox"], int(r["maxd"]))
    if merge is not None: merge.update(regs); return regs
    pickle.dump(regs, open(out, "wb"))

if __name__ == "__main__":
    import world_data as A, world_data_117 as B
    RED = (196, 52, 62)
    specs = [
     dict(key="britain", empire="ROMAN EMPIRE", origin=(1.3, 51.1), color=RED, clip=[(-7, 49.5), (3, 49.5), (3, 56.5), (-7, 56.5)]),
     dict(key="mauretania", empire="ROMAN EMPIRE", origin=(1, 36.3), color=RED, clip=[(-11, 30), (9, 30), (9, 37.8), (-11, 37.8)]),
     dict(key="dacia", empire="ROMAN EMPIRE", origin=(22.5, 44.4), color=RED, clip=[(19.5, 43.5), (30, 43.5), (30, 49), (19.5, 49)]),
     dict(key="arabia", empire="ROMAN EMPIRE", origin=(36.3, 33.3), color=RED, clip=[(32, 24), (40.5, 24), (40.5, 33.6), (32, 33.6)]),
     dict(key="east", empire="ROMAN EMPIRE", origin=(38.3, 37.5), color=RED, clip=[(36.5, 28.5), (50, 28.5), (50, 42.8), (36.5, 42.8)]),
     dict(key="rest_rome", empire="ROMAN EMPIRE", origin=(30, 40), color=RED),
     dict(key="kushan", empire="KUSHAN EMPIRE", origin=(67, 37.8), color=(150, 110, 200)),
     dict(key="wsatraps", empire="WESTERN SATRAPS", origin=(70.5, 22.8), color=(210, 100, 150)),
     dict(key="xianbei", empire="XIANBEI", origin=(123, 46), color=(64, 168, 150)),
     dict(key="aksum", empire="AKSUM", origin=(39, 14.5), color=(120, 150, 200)),
     dict(key="retreat", empire="ROMAN EMPIRE", origin=(48.5, 30), mode="retreat", src="A", color=(214, 140, 52),
          clip=[(38.9, 42.8), (49, 42.8), (49.5, 28.5), (44, 29.5), (39.2, 35.6), (38.7, 38)]),
    ]
    build(A, B, specs, "/home/claude/shortgen/regions_ep02_hd.pkl")
