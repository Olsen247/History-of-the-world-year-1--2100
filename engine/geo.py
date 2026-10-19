"""Detailed map: Mercator projection, Natural Earth land, NASA Blue Marble + NE shaded relief."""
import json, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None

BMD = "/usr/local/lib/python3.13/dist-packages/mpl_toolkits/basemap_data/"
TOPO = "/home/claude/geo/node_modules/world-atlas/land-50m.json"
LAT_N, LAT_S = 78.0, -56.0
W = 9600

def merc_y(lat): return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
YN, YS = merc_y(LAT_N), merc_y(LAT_S)

class Proj:
    """Mercator, lon -180..180 → 0..W, lat LAT_N..LAT_S → 0..H."""
    def __init__(self, width=W):
        self.W = width; self.s = width / (2 * math.pi)
        self.H = int(round((YN - YS) * self.s))
    def __call__(self, lon, lat):
        lat = max(-85, min(85, lat))
        return (lon + 180) / 360 * self.W, (YN - merc_y(lat)) * self.s
    def poly(self, pts): return [self(lo, la) for lo, la in pts]
    def lat_of_y(self, y):
        m = YN - np.asarray(y, np.float64) / self.s
        return np.degrees(2 * np.arctan(np.exp(m)) - math.pi / 2)

P = Proj(W); H = P.H

def topo_rings(path=TOPO):
    t = json.load(open(path))
    sx, sy = t["transform"]["scale"]; tx, ty = t["transform"]["translate"]
    arcs = []
    for a in t["arcs"]:
        x = y = 0; pts = []
        for dx, dy in a:
            x += dx; y += dy; pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)
    def ring(idx):
        out = []
        for i in idx:
            pts = arcs[i] if i >= 0 else arcs[~i][::-1]
            out.extend(pts if not out else pts[1:])
        return out
    polys = []
    def geom(g):
        if g["type"] == "GeometryCollection":
            for gg in g["geometries"]: geom(gg)
        elif g["type"] == "Polygon": polys.append([ring(r) for r in g["arcs"]])
        elif g["type"] == "MultiPolygon":
            for p in g["arcs"]: polys.append([ring(r) for r in p])
    for o in t["objects"].values(): geom(o)
    return polys

def unwrap(ring):
    out = []; off = 0; prev = None
    for lo, la in ring:
        if prev is not None:
            if lo - prev > 180: off -= 360
            elif lo - prev < -180: off += 360
        out.append((lo + off, la)); prev = lo
    return out

def draw_ring(d, ring, fill):
    u = unwrap(ring)
    los = [p[0] for p in u]
    shifts = [0]
    if max(los) > 180: shifts.append(-360)
    if min(los) < -180: shifts.append(360)
    for sh in shifts:
        d.polygon([((lo + sh + 180) / 360 * W, P(0, la)[1]) for lo, la in u], fill=fill)

def land_mask(extra_water=()):
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    for poly in topo_rings():
        draw_ring(d, poly[0], 255)
        for hole in poly[1:]: draw_ring(d, hole, 0)
    for pts in extra_water: d.polygon(P.poly(pts), fill=0)
    return im

def reproject(src, out_w=W):
    """Equirectangular (lon -180..180, lat 90..-90) → our Mercator crop."""
    sw, sh = src.size
    a = np.asarray(src)
    ys = np.arange(H) + 0.5
    lat = P.lat_of_y(ys)
    sy = (90 - lat) / 180 * sh - 0.5
    sx = (np.arange(out_w) + 0.5) / out_w * sw - 0.5
    y0 = np.clip(np.floor(sy).astype(int), 0, sh - 1); y1 = np.clip(y0 + 1, 0, sh - 1); fy = (sy - np.floor(sy))[:, None, None]
    x0 = np.clip(np.floor(sx).astype(int), 0, sw - 1); x1 = np.clip(x0 + 1, 0, sw - 1); fx = (sx - np.floor(sx))[None, :, None]
    out = np.empty((H, out_w, a.shape[2]), np.float32)
    CH = 400
    for r in range(0, H, CH):
        ya, yb = y0[r:r + CH], y1[r:r + CH]; f = fy[r:r + CH]
        top = a[ya][:, x0].astype(np.float32) * (1 - fx) + a[ya][:, x1].astype(np.float32) * fx
        bot = a[yb][:, x0].astype(np.float32) * (1 - fx) + a[yb][:, x1].astype(np.float32) * fx
        out[r:r + CH] = top * (1 - f) + bot * f
    return out

def build_terrain():
    bm = reproject(Image.open(BMD + "bmng.jpg").convert("RGB")).astype(np.uint8)
    sr = reproject(Image.open(BMD + "shadedrelief.jpg").convert("RGB"))
    lum = sr.mean(axis=2).astype(np.float32); del sr
    lumi = Image.fromarray(np.clip(lum, 0, 255).astype(np.uint8))
    low = np.asarray(lumi.filter(ImageFilter.GaussianBlur(4)), np.float32)
    landi = land_mask()
    lm8 = np.asarray(landi)
    out = np.empty_like(bm)
    CH = 500
    for r in range(0, H, CH):
        lmc = lm8[r:r + CH].astype(np.float32)[..., None] / 255
        det = ((lum[r:r + CH] - low[r:r + CH]) / 255)[..., None]
        o = bm[r:r + CH].astype(np.float32) * (1 + det * 1.6 * lmc) / 255
        o = np.clip((o - 0.5) * 1.12 + 0.5, 0, 1) ** 1.05
        sea = 1 - lmc
        o = o * (1 - sea) + o * np.array([0.78, 0.9, 1.0], np.float32) * sea
        out[r:r + CH] = np.clip(o * 255, 0, 255).astype(np.uint8)
    del bm, lum, low
    img = Image.fromarray(out, "RGB").filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
    return img, landi

def empire_masks(data, land_l):
    land = np.asarray(land_l)
    out = []
    for name, col, polys, lab in data.EMPIRES:
        im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
        for pts in polys: d.polygon(P.poly(pts), fill=255)
        m = np.minimum(np.asarray(im), land)
        if getattr(data, "EXCLUSIVE", False):
            later = Image.new("L", (W, H), 0); dl = ImageDraw.Draw(later)
            idx = [e[0] for e in data.EMPIRES].index(name)
            for e2 in data.EMPIRES[idx + 1:]:
                for pts in e2[2]: dl.polygon(P.poly(pts), fill=255)
            m = np.where(np.asarray(later) > 0, 0, m).astype(np.uint8)
        ys, xs = np.nonzero(m)
        if len(xs) == 0: continue
        pad = 40
        bb = (max(0, xs.min() - pad), max(0, ys.min() - pad), min(W, xs.max() + pad), min(H, ys.max() + pad))
        out.append((name, col, Image.fromarray(m[bb[1]:bb[3], bb[0]:bb[2]]), bb))
    return out

def overlay_empires(ter, masks, alpha=0.88):
    img = ter.copy()
    # drop shadows first
    for name, col, mi, bb in masks:
        x0, y0, x1, y1 = bb
        crop = np.asarray(img.crop(bb), np.float32)
        m = np.asarray(mi, np.float32) / 255
        s = np.asarray(mi.filter(ImageFilter.GaussianBlur(10)), np.float32) / 255
        s = np.roll(np.roll(s, 9, 0), 7, 1)
        crop *= (1 - 0.55 * s * (1 - m))[..., None]
        img.paste(Image.fromarray(np.clip(crop, 0, 255).astype(np.uint8)), (x0, y0))
    for name, col, mi, bb in masks:
        x0, y0, x1, y1 = bb
        crop = np.asarray(img.crop(bb), np.float32)
        m = np.asarray(mi, np.float32) / 255
        lum = crop.mean(axis=2, keepdims=True) / 128
        c = np.array(col, np.float32) * 0.82
        tint = c * (0.58 + 0.3 * np.clip(lum, 0.4, 1.5))
        a = (m * alpha)[..., None]
        out = crop * (1 - a) + tint * a
        bl = np.asarray(mi.filter(ImageFilter.GaussianBlur(5)), np.float32) / 255
        gy, gx = np.gradient(bl)
        out *= (1 + np.clip((gx + gy) * -22, -0.4, 0.4) * m)[..., None]
        er = np.asarray(mi.filter(ImageFilter.MinFilter(5)), np.float32) / 255
        edge = np.clip(m - er, 0, 1)[..., None]
        out = out * (1 - edge * 0.7) + (c * 0.5) * edge * 0.7
        img.paste(Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), (x0, y0))
    return img

if __name__ == "__main__":
    import world_data as A, world_data_117 as B
    import os, sys
    if os.path.exists("/home/claude/shortgen/hd_terrain.png"):
        ter = Image.open("/home/claude/shortgen/hd_terrain.png").convert("RGB"); land = Image.open("/home/claude/shortgen/hd_land.png").convert("L")
    else:
        ter, lm = build_terrain()
        ter.save("/home/claude/shortgen/hd_terrain.png")
        land = lm; land.save("/home/claude/shortgen/hd_land.png")
    if len(sys.argv) <= 1: overlay_empires(ter, empire_masks(A, land)).save("/home/claude/shortgen/hd_1.png")
    import sys
    if len(sys.argv) > 1:
        import importlib; D = importlib.import_module(sys.argv[1])
        overlay_empires(ter, empire_masks(D, land)).save(sys.argv[2]); print("ok", sys.argv[2]); raise SystemExit
    overlay_empires(ter, empire_masks(B, land)).save("/home/claude/shortgen/hd_117.png")
    print("ok", ter.size)
