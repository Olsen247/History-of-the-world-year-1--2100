"""South-polar globe medallion for Episode 21 (the race to the South Pole): the Mercator map stops at 56 S,
so Antarctica is shown as an azimuthal disc seen from above the pole, Ross Sea at the top.
Routes: Amundsen (Bay of Whales, Axel Heiberg Glacier) and Scott (Ross Island, Beardmore Glacier)."""
import math
from PIL import Image, ImageDraw, ImageFilter
import geo
from hist_engine3 import put, pr, eo, eback, glow_text, GOLD, WHITE

R = 340; S = 2; LAT_EDGE = -63.0
AMUNDSEN = [(-163.7, -78.5), (-163.5, -80.5), (-164.0, -82.5), (-166.0, -84.5), (-168.0, -85.6), (-170.0, -87.0), (0.0, -90.0)]
SCOTT = [(166.7, -77.6), (168.0, -79.5), (170.0, -81.5), (170.5, -83.4), (164.0, -84.8), (160.0, -86.5), (155.0, -88.0), (0.0, -90.0)]


def xy(lon, lat, r=R, c=None):
    c = c if c is not None else (r, r)
    rr = (lat + 90.0) / (LAT_EDGE + 90.0) * r
    a = math.radians(lon)
    return (c[0] - rr * math.sin(a), c[1] + rr * math.cos(a))


_DISC = None
def disc():
    global _DISC
    if _DISC is not None: return _DISC
    n = R * 2 * S
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, n - 1, n - 1], fill=(14, 38, 72, 255))
    for k in range(1, 4):   # latitude rings 80, 70, 60 S
        rr = (k * 10) / (LAT_EDGE + 90.0) * R * S
        d.ellipse([n / 2 - rr, n / 2 - rr, n / 2 + rr, n / 2 + rr], outline=(60, 95, 140, 255), width=S)
    land = Image.new("L", (n, n), 0); dl = ImageDraw.Draw(land)
    for poly in geo.topo_rings():
        for i, ring in enumerate(poly):
            if min(la for lo, la in ring) > LAT_EDGE + 1: continue
            pts = [xy(lo, max(la, -89.99), R * S) for lo, la in ring]
            dl.polygon(pts, fill=0 if i else 255)
    shade = Image.new("RGBA", (n, n), (236, 242, 248, 255))
    sd = ImageDraw.Draw(shade)
    for k in range(18):   # soft inland blue-grey shading towards the plateau
        rr = R * S * (0.62 - k * 0.03)
        if rr <= 0: break
        sd.ellipse([n / 2 - rr, n / 2 - rr, n / 2 + rr, n / 2 + rr], fill=(236 - k * 2, 242 - k, 250, 255))
    im.paste(shade, (0, 0), land.filter(ImageFilter.GaussianBlur(S * 0.6)))
    mask = Image.new("L", (n, n), 0); ImageDraw.Draw(mask).ellipse([0, 0, n - 1, n - 1], fill=255)
    im.putalpha(mask)
    ring = Image.new("RGBA", (n + 40 * S, n + 40 * S), (0, 0, 0, 0)); dr = ImageDraw.Draw(ring)
    dr.ellipse([20 * S - 6 * S, 20 * S - 6 * S, n + 20 * S + 6 * S, n + 20 * S + 6 * S], outline=GOLD + (255,), width=7 * S)
    glow = ring.filter(ImageFilter.GaussianBlur(10 * S))
    out = Image.new("RGBA", ring.size, (0, 0, 0, 0)); out.alpha_composite(glow); out.alpha_composite(glow)
    out.alpha_composite(im, (20 * S, 20 * S)); out.alpha_composite(ring)
    _DISC = out.resize((out.width // S, out.height // S), Image.LANCZOS)
    return _DISC


def _path_upto(pts, f):
    P = [xy(*p) for p in pts]
    L = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(P, P[1:])]; tot = sum(L); want = tot * f
    out = [P[0]]
    for (a, b), l in zip(zip(P, P[1:]), L):
        if want >= l: out.append(b); want -= l
        else:
            k = want / l if l else 0; out.append((a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)); break
    return out


def _flag_no(w=34, h=24):
    im = Image.new("RGBA", (w, h), (186, 12, 47, 255)); d = ImageDraw.Draw(im)
    d.rectangle([w * .30, 0, w * .48, h], fill=(255, 255, 255, 255)); d.rectangle([0, h * .38, w, h * .62], fill=(255, 255, 255, 255))
    d.rectangle([w * .345, 0, w * .435, h], fill=(0, 32, 91, 255)); d.rectangle([0, h * .44, w, h * .56], fill=(0, 32, 91, 255))
    return im


_TXT = {}
def _t(s, sz, col):
    k = (s, sz, col)
    if k not in _TXT: _TXT[k] = glow_text(s, sz, col)
    return _TXT[k]


def draw(fr, t, t0, t1, cx=540, cy=770, amund=(1.0, 4.6), scott=(1.4, 5.4), labels=True, size=1.0):
    """Disc visible t0..t1 (pops in and out); routes drawn between t0+amund[0]..t0+amund[1]."""
    if t < t0 or t > t1 + 0.4: return
    k = eback(pr(t, t0, t0 + 0.45), 2.0) if t < t1 else 1.0 - pr(t, t1, t1 + 0.35)
    alpha = min(1.0, pr(t, t0, t0 + 0.25)) * (1.0 - pr(t, t1, t1 + 0.35))
    D = disc().copy(); dd = ImageDraw.Draw(D); o = 20
    def P(p): return (p[0] + o, p[1] + o)
    fa = eo(pr(t, t0 + amund[0], t0 + amund[1])); fs = eo(pr(t, t0 + scott[0], t0 + scott[1])) * 0.80   # Scott is 34 days behind
    for pts, f, col in ((SCOTT, fs, (140, 190, 255)), (AMUNDSEN, fa, (240, 70, 80))):
        if f <= 0: continue
        seg = [P(q) for q in _path_upto(pts, f)]
        for a, b in zip(seg, seg[1:]): dd.line([a, b], fill=col + (255,), width=5)
        hx, hy = seg[-1]; dd.ellipse([hx - 7, hy - 7, hx + 7, hy + 7], fill=col + (255,), outline=(255, 255, 255, 255), width=2)
    pole = P(xy(0, -90))
    dd.ellipse([pole[0] - 5, pole[1] - 5, pole[0] + 5, pole[1] + 5], fill=(255, 255, 255, 255))
    if labels:
        put(D, _t("SOUTH POLE", 30, GOLD), pole[0], pole[1] + 44, alpha=pr(t, t0 + 0.5, t0 + 0.9))
        a0 = P(xy(*AMUNDSEN[0])); s0 = P(xy(*SCOTT[0]))
        put(D, _t("AMUNDSEN", 26, (255, 120, 120)), a0[0] + 72, a0[1] - 18, alpha=pr(t, t0 + 0.8, t0 + 1.2))
        put(D, _t("SCOTT", 26, (160, 205, 255)), s0[0] - 50, s0[1] - 18, alpha=pr(t, t0 + 1.2, t0 + 1.6))
        put(D, _t("ROSS SEA", 22, (170, 200, 230)), D.width / 2, o + 52, alpha=pr(t, t0 + 0.5, t0 + 0.9))
    if fa >= 0.999:   # flag planted
        kf = eback(pr(t, t0 + amund[1], t0 + amund[1] + 0.35), 2.4)
        if kf > 0:
            fl = _flag_no(); W_ = int(fl.width * kf) or 1
            dd.line([pole[0], pole[1], pole[0], pole[1] - 46 * kf], fill=(235, 235, 235, 255), width=3)
            D.alpha_composite(fl.resize((W_, max(1, int(fl.height * kf)))), (int(pole[0] + 1), int(pole[1] - 46 * kf)))
    put(fr, D, cx, cy, scale=max(0.02, k * size), alpha=alpha)
