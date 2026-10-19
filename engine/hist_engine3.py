"""Reusable engine for 'History of the World' episodes:
label-free base maps, spreading/retreating territory reveals, dynamic labels,
year ticker, cards, camera moves, hook and outro."""
import sys, math, pickle, subprocess
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from geo import Proj
import fx as FX
Image.MAX_IMAGE_PIXELS = None

W, H, FPS = 1080, 1920, 30
FD = "/usr/share/fonts/opentype/inter/"
SERIF_B = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
HEAD = FD + "InterDisplay-BlackItalic.otf"; BLACK = FD + "InterDisplay-Black.otf"; MED = FD + "Inter-SemiBold.otf"
GOLD = (255, 205, 80); WHITE = (246, 248, 252); MUTED = (150, 165, 190); RED = (235, 70, 80); DARK = (8, 14, 26)
CFG = None
_fc = {}
def F(p, s):
    if (p, s) not in _fc: _fc[(p, s)] = ImageFont.truetype(p, s)
    return _fc[(p, s)]

def cl(x, a=0.0, b=1.0): return max(a, min(b, x))
def pr(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eo(x): x = cl(x); return 1 - (1 - x) ** 3
def eio(x): x = cl(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def eback(x, s=2.0):
    x = cl(x); c3 = s + 1; return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2
def lerp(a, b, k): return a + (b - a) * k

_tc = {}
def timg(s, font, sz, col, stroke=0, scol=(0, 0, 0)):
    key = (s, font, sz, col, stroke, scol)
    if key in _tc: return _tc[key]
    f = F(font, sz); l, t, r, b = f.getbbox(s, stroke_width=stroke)
    im = Image.new("RGBA", (r - l + 8, b - t + 8), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((4 - l, 4 - t), s, font=f, fill=col + (255,), stroke_width=stroke, stroke_fill=scol + (255,))
    if len(_tc) > 4000: _tc.clear()
    _tc[key] = im; return im

def put(fr, im, cx, cy, scale=1.0, alpha=1.0):
    if alpha <= 0.003 or scale <= 0.01: return
    if abs(scale - 1) > 0.005:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if alpha < 0.999:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    fr.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)

# ---------------- setup ----------------
class Ep: pass

def setup(cfg):
    global CFG
    e = Ep(); e.__dict__.update(cfg)
    e.A = Image.open(cfg["base_a"]).convert("RGB")
    e.B = Image.open(cfg["base_b"]).convert("RGB")
    for k_, p_ in cfg.get("extra_bases", {}).items(): setattr(e, k_, Image.open(p_).convert("RGB"))
    e.MW, e.MH = e.A.size
    e.P = Proj(e.MW)
    e.regions = pickle.load(open(cfg["regions"], "rb")) if cfg.get("regions") else {}
    e.pieces = {}
    for rv in e.reveals:
        if rv.get("mode") == "shatter": e.pieces[rv["key"]] = make_pieces(e, e.regions[rv["key"]], rv)
    e.vig = make_vignette()
    e.routes = cfg.get("routes", [])
    e.fx = cfg.get("fx", [])
    e.emblem_img = make_spqr()
    CFG = e
    return e

def make_vignette():
    y = np.linspace(-1, 1, H)[:, None]; x = np.linspace(-1, 1, W)[None, :]
    d = np.sqrt(x ** 2 * 1.0 + y ** 2 * 0.55)
    a = np.clip((d - 0.45) / 0.75, 0, 1) ** 1.6
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); im.putalpha(Image.fromarray((a * 255).astype(np.uint8)))
    return im

def make_spqr(size=340):
    S = 3; n = size * S
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    gold = (238, 190, 60, 255); dark = (90, 60, 10, 255)
    c = n / 2; R = n * 0.40
    for side in (-1, 1):
        for k in range(11):
            a = math.radians(200 + k * 14) if side < 0 else math.radians(340 - k * 14)
            x = c + R * math.cos(a); y = c - R * math.sin(a) * -1
            ang = a + (math.pi / 2 if side < 0 else -math.pi / 2)
            L, Wd = n * 0.085, n * 0.032
            pts = []
            for t_ in np.linspace(0, 2 * math.pi, 18):
                px, py = L * math.cos(t_), Wd * math.sin(t_)
                pts.append((x + px * math.cos(ang + 0.5 * side) - py * math.sin(ang + 0.5 * side),
                            y + px * math.sin(ang + 0.5 * side) + py * math.cos(ang + 0.5 * side)))
            d.polygon(pts, fill=gold, outline=dark)
    f = F(SERIF_B, int(n * 0.26))
    d.text((c, c + n * 0.02), "SPQR", font=f, fill=gold, anchor="mm", stroke_width=int(n * 0.012), stroke_fill=dark)
    im = im.resize((size, size), Image.LANCZOS)
    glow = im.getchannel("A").filter(ImageFilter.GaussianBlur(14))
    g = Image.new("RGBA", im.size, (255, 200, 80, 255)); g.putalpha(glow.point(lambda v: int(v * 0.7)))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.alpha_composite(g); out.alpha_composite(im)
    return out

def make_pieces(e, R, rv, cell=20):
    import random as _r
    rnd = _r.Random(5)
    bx0, by0, bx1, by1 = R["bbox"]
    reg = np.isfinite(R["dist"])
    src = getattr(e, rv.get("piece_src", "B")).crop((bx0, by0, bx1, by1)).convert("RGBA")
    ox, oy = e.P(*rv.get("origin", (0, 0)))
    out = []
    for yy in range(0, by1 - by0, cell):
        for xx in range(0, bx1 - bx0, cell):
            sub = reg[yy:yy + cell, xx:xx + cell]
            if sub.mean() < 0.15: continue
            jx, jy = rnd.randint(-4, 4), rnd.randint(-4, 4)
            x0, y0 = max(0, xx + jx), max(0, yy + jy)
            x1, y1 = min(bx1 - bx0, x0 + cell + 3), min(by1 - by0, y0 + cell + 3)
            pc = src.crop((x0, y0, x1, y1))
            m = Image.fromarray((reg[y0:y1, x0:x1] * 255).astype(np.uint8))
            pc.putalpha(m)
            cx, cy = bx0 + (x0 + x1) / 2, by0 + (y0 + y1) / 2
            dx, dy = cx - ox, cy - oy; dn = math.hypot(dx, dy) + 1e-3
            dist = R["dist"][min(y1 - 1, (y0 + y1) // 2), min(x1 - 1, (x0 + x1) // 2)]
            delay = (dist / R["maxd"] if np.isfinite(dist) else rnd.random())
            sp = rnd.uniform(60, 160)
            out.append(dict(img=pc, cx=cx, cy=cy, vx=dx / dn * sp + rnd.uniform(-40, 40), vy=dy / dn * sp - rnd.uniform(40, 120),
                            rot=rnd.uniform(-260, 260), delay=delay))
    return out

# ---------------- camera ----------------
def cam(t):
    K = CFG.keys; P = CFG.P
    for (t0, lo0, la0, w0), (t1, lo1, la1, w1) in zip(K, K[1:]):
        if t0 <= t <= t1:
            if (lo0, la0, w0) == (lo1, la1, w1):
                x, y = P(lo0, la0); return x, y, w0 * (1 - 0.06 * pr(t, t0, t1))
            k = eio(pr(t, t0, t1))
            x0, y0 = P(lo0, la0); x1, y1 = P(lo1, la1)
            dist = math.hypot(x1 - x0, y1 - y0)
            bump = min(2.0, dist / max(w0, w1) * 0.6) if dist > 1 else 0
            vw = lerp(w0, w1, k) * (1 + bump * math.sin(math.pi * k))
            return lerp(x0, x1, k), lerp(y0, y1, k), min(vw, 9000)
    t0, lo, la, w = K[-1]; x, y = P(lo, la); return x, y, w

BGC = (11, 28, 47)

def base_at(t):
    """Which base image (and crossfade) to use at time t."""
    e = CFG
    for (ts, te, frm, to) in e.base_switches:
        if t < ts: return (frm, None, 0)
        if t < te: return (frm, to, eio(pr(t, ts, te)))
    return (e.base_switches[-1][3], None, 0) if e.base_switches else ("B", None, 0)

def crop(img, box, size):
    return img.resize(size, Image.BICUBIC, box=box)

def cam_clamped(t):
    e = CFG
    cx, cy, vw = cam(t)
    vw = min(vw, e.MH * W / H * 0.98)
    vh = vw * H / W
    cy = min(max(cy, vh / 2), e.MH - vh / 2)
    cx = min(max(cx, vw / 2), e.MW - vw / 2)
    return cx, cy, vw

def map_frame(t):
    e = CFG
    cx, cy, vw = cam_clamped(t)
    px_, py_, pw_ = cam_clamped(t - 1 / FPS)
    speed = math.hypot(cx - px_, cy - py_) * W / vw + abs(vw - pw_) / vw * 400
    s = W / vw; vh = H / s
    x0, y0 = cx - vw / 2, cy - vh / 2
    fr = Image.new("RGB", (W, H), BGC)
    bx0, by0 = max(0, x0), max(0, y0); bx1, by1 = min(e.MW, x0 + vw), min(e.MH, y0 + vh)
    if bx1 > bx0 and by1 > by0:
        ow, oh = max(1, int(round((bx1 - bx0) * s))), max(1, int(round((by1 - by0) * s)))
        frm, to, k = base_at(t)
        part = crop(getattr(e, frm), (bx0, by0, bx1, by1), (ow, oh))
        if to and k > 0:
            part = Image.blend(part, crop(getattr(e, to), (bx0, by0, bx1, by1), (ow, oh)), k)
        px, py = int(round((bx0 - x0) * s)), int(round((by0 - y0) * s))
        fr.paste(part, (px, py))
        # reveals
        for rv in e.reveals:
            draw_reveal(fr, rv, t, x0, y0, s)
    S = lambda lon, lat: ((e.P(lon, lat)[0] - x0) * s, (e.P(lon, lat)[1] - y0) * s)
    return fr, S, s, vw

def draw_shatter(fr, rv, t, x0, y0, s):
    e = CFG
    t0, t1 = rv["t0"], rv["t1"]
    if t < t0 or t >= rv.get("until", 1e9): return
    R = e.regions[rv["key"]]
    bx0, by0, bx1, by1 = R["bbox"]
    sw, sh = int(round((bx1 - bx0) * s)), int(round((by1 - by0) * s))
    sx, sy = int(round((bx0 - x0) * s)), int(round((by0 - y0) * s))
    under = getattr(e, rv.get("under", "A")).crop((bx0, by0, bx1, by1)).resize((max(1, sw), max(1, sh)), Image.BILINEAR)
    mask = Image.fromarray((np.isfinite(R["dist"]) * 255).astype(np.uint8)).resize((max(1, sw), max(1, sh)), Image.BILINEAR)
    fr.paste(under, (sx, sy), mask)
    dur = t1 - t0
    for p_ in e.pieces[rv["key"]]:
        lt = t - t0 - p_["delay"] * dur * 0.6
        if lt > 1.3: continue
        if lt < 0:
            lt = 0; k = 0
        k = cl(lt / 1.2)
        cx = p_["cx"] + p_["vx"] * lt; cy = p_["cy"] + p_["vy"] * lt + 260 * lt * lt
        sc = s * (1 + 0.6 * k)
        im = p_["img"]
        w_, h_ = max(1, int(im.width * sc)), max(1, int(im.height * sc))
        if w_ < 2 or h_ < 2: continue
        pim = im.resize((w_, h_), Image.BILINEAR)
        if lt > 0: pim = pim.rotate(p_["rot"] * lt, resample=Image.BILINEAR, expand=True)
        a = 1 - k
        if a < 0.999: pim.putalpha(pim.getchannel("A").point(lambda v: int(v * a)))
        px, py = (cx - x0) * s - pim.width / 2, (cy - y0) * s - pim.height / 2
        if lt > 0:
            shd = Image.new("RGBA", pim.size, (0, 0, 0, 255)); shd.putalpha(pim.getchannel("A").point(lambda v: int(v * 0.45)))
            fr.paste(shd, (int(px + 10 * k * s * 6), int(py + 14 * k * s * 6)), shd)
        fr.paste(pim, (int(px), int(py)), pim)

def draw_reveal(fr, rv, t, x0, y0, s):
    e = CFG
    if rv.get("mode") == "shatter": return draw_shatter(fr, rv, t, x0, y0, s)
    key, t0, t1, until = rv["key"], rv["t0"], rv["t1"], rv.get("until", 1e9)
    if t < t0 or t >= until: return
    R = e.regions[key]
    p = eio(pr(t, t0, t1))
    bx0, by0, bx1, by1 = R["bbox"]
    sw, sh = int(round((bx1 - bx0) * s)), int(round((by1 - by0) * s))
    if sw < 2 or sh < 2: return
    sx, sy = int(round((bx0 - x0) * s)), int(round((by0 - y0) * s))
    if sx > W or sy > H or sx + sw < 0 or sy + sh < 0: return
    front = p * R["maxd"] * 1.001
    d = R["dist"]
    m = (d <= front)
    src = getattr(e, R["src"]).crop((bx0, by0, bx1, by1))
    mask = Image.fromarray((m * 255).astype(np.uint8))
    if p < 1:
        ring = (d <= front) & (d > front - max(6, R["maxd"] * 0.05))
        glow = Image.fromarray((ring * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
        col = tuple(min(255, int(c * 0.6 + 255 * 0.4)) for c in R["color"])
        gl = Image.new("RGB", src.size, col)
        src = Image.composite(gl, src, glow)
    src = src.resize((sw, sh), Image.BILINEAR); mask = mask.resize((sw, sh), Image.BILINEAR)
    fr.paste(src, (sx, sy), mask)

# ---------------- labels ----------------
SIZES = {"emp": 46, "mid": 36, "small": 27, "culture": 24, "event": 38}

def label_size(kind, vw):
    k = cl((3400 / vw) ** 0.6, 0.6, 1.4)
    return int(SIZES[kind] * k)

def draw_labels(fr, S, vw, t):
    for lb in CFG.labels:
        a = min(pr(t, lb.get("t_in", -1), lb.get("t_in", -1) + 0.5), 1 - pr(t, lb.get("t_out", 1e9), lb.get("t_out", 1e9) + 0.5))
        if a <= 0.01: continue
        kind = lb["kind"]; sz = label_size(kind, vw)
        if kind == "culture" and sz < 17: continue
        if sz < 14: continue
        x, y = S(*lb["pos"])
        if x < -300 or x > W + 300 or y < -100 or y > H + 100: continue
        lines = lb["text"].split("\n")
        for i, ln in enumerate(lines):
            yy = y + (i - (len(lines) - 1) / 2) * sz * 1.08
            if kind == "culture":
                im = timg(ln, SERIF_I, sz, (60, 46, 32), max(2, sz // 9), (224, 210, 176))
            elif kind == "event":
                im = timg(ln, HEAD, sz, lb.get("color", GOLD), max(3, sz // 8), DARK)
            else:
                im = timg(ln, SERIF_B, sz, WHITE, max(2, sz // 9), (10, 10, 14))
            put(fr, im, x, yy, alpha=a, scale=(1 + 0.25 * (1 - eo(pr(t, lb.get("t_in", -1), lb.get("t_in", -1) + 0.4)))) if kind == "event" else 1.0)

# ---------------- overlays ----------------
def pin(fr, xy, t, t0, t1, col=GOLD):
    a = min(pr(t, t0, t0 + 0.3), 1 - pr(t, t1 - 0.3, t1))
    if a <= 0: return
    d = ImageDraw.Draw(fr, "RGBA"); x, y = xy
    ph = ((t - t0) % 1.4) / 1.4; r = 14 + 40 * ph
    d.ellipse([x - r, y - r, x + r, y + r], outline=col + (int(200 * (1 - ph) * a),), width=4)
    d.ellipse([x - 11, y - 11, x + 11, y + 11], fill=col + (int(255 * a),), outline=DARK + (int(255 * a),), width=3)

def card(fr, t, c):
    t0, t1 = c["t0"], c["t1"]
    a_in = eback(pr(t, t0, t0 + 0.35), 1.8); out = eo(pr(t, t1 - 0.3, t1))
    if t < t0 or out >= 1: return
    tt = timg(c["title"], HEAD, 40, c.get("color", GOLD)); bb = timg(c["big"], HEAD, 70, WHITE); ss = timg(c["sub"], MED, 29, MUTED)
    w = max(tt.width, bb.width, ss.width) + 90; h = tt.height + bb.height + ss.height + 64
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=30, fill=(8, 16, 30, 232), outline=c.get("color", GOLD) + (255,), width=4)
    y_ = 24
    for im in (tt, bb, ss):
        img.alpha_composite(im, ((w - im.width) // 2, y_)); y_ += im.height + 5
    put(fr, img, 540, c.get("y", 1320) + 60 * out, scale=min(a_in, 1.1) if a_in < 1.1 else 1.0, alpha=min(1, a_in * 2) * (1 - out))

def year_at(t):
    K = CFG.ticker
    for (t0, y0), (t1, y1) in zip(K, K[1:]):
        if t0 <= t <= t1:
            return int(round(lerp(y0, y1, eio(pr(t, t0, t1)))))
    return K[-1][1] if t > K[-1][0] else K[0][1]

def spaced(text, font, sz, col, stroke=0, scol=(0, 0, 0), sp=0.08):
    key = ("sp", text, font, sz, col, stroke, scol, sp)
    if key in _tc: return _tc[key]
    ims = [timg(ch if ch != " " else " ", font, sz, col, stroke, scol) for ch in text]
    gap = int(sz * sp)
    w = sum(i.width for i in ims) - 8 * len(ims) + gap * (len(ims) - 1) + 16; h = max(i.height for i in ims)
    out = Image.new("RGBA", (max(1, w), h), (0, 0, 0, 0)); x = 0
    for ch, i in zip(text, ims):
        if ch == " ": x += int(sz * 0.32); continue
        out.alpha_composite(i, (x, h - i.height)); x += i.width - 8 + gap
    out = out.crop((0, 0, max(1, x + 8), h))
    _tc[key] = out; return out

def glow_text(text, sz, col):
    key = ("glow", text, sz, col)
    if key in _tc: return _tc[key]
    t = spaced(text, SERIF_B, sz, col, max(2, sz // 14), (6, 6, 10))
    pad = 30
    out = Image.new("RGBA", (t.width + 2 * pad, t.height + 2 * pad), (0, 0, 0, 0))
    g = Image.new("RGBA", out.size, col + (255,))
    a = Image.new("L", out.size, 0); a.paste(t.getchannel("A"), (pad, pad))
    g.putalpha(a.filter(ImageFilter.GaussianBlur(10)).point(lambda v: int(v * 0.8)))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 255)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(6)).point(lambda v: int(v * 0.9)))
    out.alpha_composite(sh, (3, 5)); out.alpha_composite(g); out.alpha_composite(t, (pad, pad))
    _tc[key] = out; return out

def headings(fr, t):
    e = CFG
    for hd in e.headings:
        t0, t1 = hd["t0"], hd["t1"]
        if t < t0 - 0.01 or t > t1 + 0.4: continue
        a = min(pr(t, t0, t0 + 0.35), 1 - pr(t, t1, t1 + 0.35))
        if a <= 0: continue
        y = hd.get("y", 330)
        l1 = glow_text(hd["l1"], hd.get("s1", 58), WHITE)
        put(fr, l1, 540, y, alpha=a, scale=min(1.0, 1010 / max(1, l1.width)) * (1 + 0.04 * (1 - eo(pr(t, t0, t0 + 0.5)))))
        if hd.get("l2"):
            k2 = pr(t, t0 + 0.15, t0 + 0.5)
            l2 = glow_text(hd["l2"], hd.get("s2", 74), hd.get("c2", GOLD))
            fit = min(1.0, 1010 / max(1, l2.width))
            put(fr, l2, 540, y + hd.get("gap", 80), alpha=a * k2, scale=fit * (1 + 0.12 * (1 - eo(k2))))

def route(fr, S, t, r_):
    k = eio(pr(t, r_["t0"], r_["t1"]))
    if k <= 0 or t > r_.get("until", 1e9): return
    a = 1 - pr(t, r_.get("until", 1e9) - 0.4, r_.get("until", 1e9))
    pts = [S(lo, la) for lo, la in r_["pts"]]
    seg = [math.hypot(b[0] - a_[0], b[1] - a_[1]) for a_, b in zip(pts, pts[1:])]
    total = sum(seg) * k; path = [pts[0]]; acc = 0
    for (p0, p1), L in zip(zip(pts, pts[1:]), seg):
        if acc + L <= total: path.append(p1); acc += L
        else:
            f = (total - acc) / L if L else 0
            path.append((p0[0] + (p1[0] - p0[0]) * f, p0[1] + (p1[1] - p0[1]) * f)); break
    col = r_.get("color", GOLD)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.line(path, fill=col + (255,), width=18, joint="curve")
    lay = lay.filter(ImageFilter.GaussianBlur(9)); lay.putalpha(lay.getchannel("A").point(lambda v: int(v * 0.55 * a)))
    fr.paste(lay, (0, 0), lay)
    d = ImageDraw.Draw(fr, "RGBA")
    d.line(path, fill=(255, 236, 170, int(255 * a)), width=6, joint="curve")
    hx, hy = path[-1]
    d.ellipse([hx - 11, hy - 11, hx + 11, hy + 11], fill=WHITE + (int(255 * a),), outline=col + (int(255 * a),), width=4)

def year_chip(fr, t):
    e = CFG
    a = min(pr(t, e.header_in, e.header_in + 0.4), 1 - pr(t, e.header_out, e.header_out + 0.4))
    if a <= 0: return
    put(fr, glow_text(f"YEAR {year_at(t)}", 40, GOLD), 540, 200, alpha=a)
    if any(t0 <= t < t1 for t0, t1 in e.rewind):
        put(fr, glow_text("◀◀ REWIND", 34, RED), 540, 140, alpha=a * (0.6 + 0.4 * math.sin(t * 12)))

def emblems(fr, S, s, t):
    e = CFG
    for em in e.emblems:
        t0, t1 = em["t0"], em["t1"]
        if t < t0 or t > t1 + 0.4: continue
        k = eback(pr(t, t0, t0 + 0.45), 2.2); out = pr(t, t1, t1 + 0.4)
        x, y = S(*em["pos"])
        sc = em.get("scale", 1.0) * (min(k, 1.15) if k < 1.15 else 1.0) * (1 + 0.03 * math.sin(t * 3))
        put(fr, e.emblem_img, x, y, scale=sc, alpha=min(1, k * 2) * (1 - out))

def frame_at(t):
    e = CFG
    fr, S, s, vw = map_frame(t)
    for r_ in e.routes: route(fr, S, t, r_)
    draw_labels(fr, S, vw, t)
    if e.fx: FX.draw_all(fr, S, vw, t, e.fx)
    emblems(fr, S, s, t)
    e.hook(fr, t)
    v = e.vig_strength(t)
    if v > 0:
        vg = e.vig if v >= 0.999 else e.vig.copy()
        if v < 0.999: vg.putalpha(e.vig.getchannel("A").point(lambda q: int(q * v)))
        fr.paste(vg, (0, 0), vg)
    if e.fx and hasattr(FX, "draw_people"): FX.draw_people(fr, S, vw, t, e.fx)
    headings(fr, t)
    year_chip(fr, t)
    e.outro(fr, t)
    fl = sum(a * math.exp(-(t - te) * 14) for te, a in e.flashes if t >= te)
    if fl > 0.01: fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 255, 255)), min(0.7, fl))
    return fr

def render_idx(i): return frame_at(i / FPS).tobytes()

def main(argv):
    if argv[1] == "stills":
        ts = [float(x) for x in argv[2].split(",")]
        ims = [frame_at(t).resize((360, 640), Image.LANCZOS) for t in ts]
        sh = Image.new("RGB", (360 * len(ims), 640))
        for i, im in enumerate(ims): sh.paste(im, (360 * i, 0))
        sh.save(argv[3]); return
    out, wav = argv[2], argv[3]
    n = int(CFG.dur * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    with Pool(2) as pool:
        for b in pool.imap(render_idx, range(n), chunksize=6): p.stdin.write(b)
    p.stdin.close(); p.wait(); print("done", p.returncode)
