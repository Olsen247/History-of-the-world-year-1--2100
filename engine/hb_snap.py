"""Snap the hand-drawn empire polygons to real historical borders.

Borders come from the open dataset "historical-basemaps" (A. Ourednik, GPL-3.0, github.com/aourednik/historical-basemaps),
stored as hb/world_<year>.geojson (bc years: world_bc100.geojson ...).

How it works: every border shape (country/state) in the dataset year closest to the map's year is rasterised once.
Each shape is given to the empire whose rough polygon covers most of it (at least MIN_SHARE of the shape's land).
The empire then gets the exact shape, so colours fill countries edge to edge, with no gaps and no overlaps.
Land the dataset does not cover at all keeps the rough polygon (so peoples/areas the dataset leaves blank still show).
"""
import glob, json, os, re
import numpy as np
from PIL import Image, ImageDraw

HB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hb")
MIN_SHARE = 0.35
_cache = {}

def _years():
    out = {}
    for f in glob.glob(os.path.join(HB_DIR, "world_*.geojson")):
        m = re.match(r"world_(bc)?(\d+)\.geojson", os.path.basename(f))
        if m: out[-int(m.group(2)) if m.group(1) else int(m.group(2))] = f
    return out

def nearest_file(year):
    ys = _years()
    if not ys: return None, None
    y = min(ys, key=lambda k: (abs(k - year), -k))
    return y, ys[y]

def _rings(geom):
    if geom is None: return []
    t, c = geom["type"], geom["coordinates"]
    if t == "Polygon": return [c[0]]
    if t == "MultiPolygon": return [p[0] for p in c]
    return []

def label_image(year, P, W, H):
    """int32 image: 0 = no shape, i = shape i (1-based). Cached per dataset year."""
    y, f = nearest_file(year)
    if f is None: return None, None
    key = (y, W, H)
    if key not in _cache:
        feats = [ft for ft in json.load(open(f))["features"] if (ft.get("properties") or {}).get("NAME")]   # unnamed = unclaimed land
        def _area(ft):   # big shapes first, so smaller shapes drawn later stay on top where the dataset overlaps
            a = 0.0
            for r in _rings(ft.get("geometry")):
                a += abs(sum(x0 * y1 - x1 * y0 for (x0, y0, *_), (x1, y1, *_) in zip(r, r[1:] + r[:1]))) / 2
            return -a
        feats.sort(key=_area)
        im = Image.new("I", (W, H), 0); d = ImageDraw.Draw(im); names = [None]
        for i, ft in enumerate(feats, 1):
            names.append((ft.get("properties") or {}).get("NAME"))
            for ring in _rings(ft.get("geometry")):
                pts = [(float(lo), float(la)) for lo, la, *_ in ring]
                if len(pts) < 3: continue
                # split rings that jump across the date line
                xs = [p[0] for p in pts]
                if max(xs) - min(xs) > 300:
                    for side in (1, -1):
                        q = [(lo if (lo > 0) == (side > 0) else side * 180.0, la) for lo, la in pts]
                        d.polygon(P.poly(q), fill=i)
                else:
                    d.polygon(P.poly(pts), fill=i)
        _cache[key] = (np.asarray(im, np.int32), names, y)
    lab, names, y = _cache[key]
    return lab, names

def snap(rough_masks, land, year, P, W, H, exclusive=True):
    """rough_masks: list of uint8 HxW arrays (already clipped to land, in EMPIRES order).
    Returns new list of masks snapped to real borders."""
    lab, names = label_image(year, P, W, H)
    if lab is None: return rough_masks
    landb = land > 127
    labl = np.where(landb, lab, 0)
    n = int(labl.max()) + 1
    area = np.bincount(labl.ravel(), minlength=n).astype(np.float64)
    owner = np.zeros(n, np.int32) - 1; best = np.zeros(n)
    for e, m in enumerate(rough_masks):
        cnt = np.bincount(labl[m > 127].ravel(), minlength=n).astype(np.float64)
        share = cnt / np.maximum(area, 1)
        take = (share >= MIN_SHARE) & ((share > best) | (exclusive & (share >= best)))   # later empires win ties (EXCLUSIVE)
        take[0] = False
        owner[take] = e; best[take] = share[take]
    out = []
    for e, m in enumerate(rough_masks):
        feat = np.isin(labl, np.nonzero(owner == e)[0])
        keep_rough = (m > 127) & (labl == 0)          # land the dataset leaves blank
        out.append(((feat | keep_rough) & landb).astype(np.uint8) * 255)
    return out
