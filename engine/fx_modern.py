"""Modern-war effects: flag-unit front lines, planes, airships, warships with dotted routes."""
import math, random
from PIL import Image, ImageDraw, ImageFilter

S3 = 3
_cache = {}

def cl(x, a=0.0, b=1.0): return max(a, min(b, x))
def pr(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eio(x): x = cl(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2

# ---------------- flags (simplified, period-correct, no hate symbols) ----------------
def _flag(code, w=30, h=20):
    W, H = w * S3, h * S3
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    def hstripes(cols):
        n = len(cols)
        for i, c in enumerate(cols): d.rectangle([0, H * i / n, W, H * (i + 1) / n], fill=c)
    def vstripes(cols):
        n = len(cols)
        for i, c in enumerate(cols): d.rectangle([W * i / n, 0, W * (i + 1) / n, H], fill=c)
    R, Wh, B, K, Y, G = (200, 30, 40), (245, 245, 245), (30, 60, 150), (20, 20, 20), (250, 210, 40), (20, 130, 60)
    if code == "de1914": hstripes([K, Wh, R])
    elif code == "fr": vstripes([B, Wh, R])
    elif code == "be": vstripes([K, Y, R])
    elif code == "it": vstripes([G, Wh, R])
    elif code == "ru": hstripes([Wh, (40, 80, 180), R])
    elif code == "ah": hstripes([R, Wh, R])
    elif code == "nl": hstripes([R, Wh, B])
    elif code == "ot":
        d.rectangle([0, 0, W, H], fill=R)
        d.ellipse([W * .30, H * .25, W * .55, H * .75], fill=Wh); d.ellipse([W * .36, H * .28, W * .60, H * .72], fill=R)
    elif code == "us":
        for i in range(7): d.rectangle([0, H * i / 7, W, H * (i + 0.5) / 7], fill=R)
        d.rectangle([0, H * 0.5 / 7, W, H], outline=None)
        for i in range(7): d.rectangle([0, H * (i + 0.5) / 7, W, H * (i + 1) / 7], fill=Wh)
        d.rectangle([0, 0, W * .42, H * .54], fill=B)
    elif code == "uk":
        d.rectangle([0, 0, W, H], fill=B)
        d.line([(0, 0), (W, H)], fill=Wh, width=int(H * .22)); d.line([(0, H), (W, 0)], fill=Wh, width=int(H * .22))
        d.line([(0, 0), (W, H)], fill=R, width=int(H * .08)); d.line([(0, H), (W, 0)], fill=R, width=int(H * .08))
        d.rectangle([W * .40, 0, W * .60, H], fill=Wh); d.rectangle([0, H * .35, W, H * .65], fill=Wh)
        d.rectangle([W * .45, 0, W * .55, H], fill=R); d.rectangle([0, H * .41, W, H * .59], fill=R)
    else:  # plain colour chip, code = "rgb:r,g,b"
        r, g, b = [int(v) for v in code.split(":")[1].split(",")]
        d.rectangle([0, 0, W, H], fill=(r, g, b))
    im = im.resize((w, h), Image.LANCZOS)
    out = Image.new("RGBA", (w + 6, h + 6), (0, 0, 0, 0))
    sh = Image.new("RGBA", (w + 2, h + 2), (0, 0, 0, 150)); out.alpha_composite(sh, (3, 4))
    border = Image.new("RGBA", (w + 2, h + 2), (255, 255, 255, 230)); out.alpha_composite(border, (1, 1))
    out.alpha_composite(im, (2, 2))
    return out

def flag(code, scale=1.0):
    k = ("flag", code, round(scale, 2))
    if k not in _cache:
        _cache[k] = _flag(code, max(8, int(30 * scale)), max(6, int(20 * scale)))
    return _cache[k]

# ---------------- vehicles ----------------
def _plane(size=60, col=(225, 225, 220)):
    n = size * S3; im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    dk = (90, 90, 90, 255); c = col + (255,)
    d.rounded_rectangle([n * .44, n * .10, n * .56, n * .86], radius=n * .05, fill=c, outline=dk, width=S3)       # fuselage (nose up)
    d.rounded_rectangle([n * .06, n * .26, n * .94, n * .38], radius=n * .04, fill=c, outline=dk, width=S3)       # upper wing
    d.rounded_rectangle([n * .12, n * .40, n * .88, n * .49], radius=n * .04, fill=col + (230,), outline=dk, width=S3)
    d.rounded_rectangle([n * .32, n * .76, n * .68, n * .84], radius=n * .03, fill=c, outline=dk, width=S3)       # tail
    d.line([(n * .40, n * .08), (n * .60, n * .08)], fill=dk, width=2 * S3)                                        # propeller
    im = im.resize((size, size), Image.LANCZOS)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda v: int(v * .45)))
    out = Image.new("RGBA", (size + 14, size + 14), (0, 0, 0, 0)); out.alpha_composite(sh, (12, 12)); out.alpha_composite(im, (0, 0))
    return out

def _airship(size=110):
    n = size * S3; im = Image.new("RGBA", (n, int(n * .45)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    h = n * .45
    d.ellipse([0, h * .1, n, h * .8], fill=(190, 195, 200, 255), outline=(90, 95, 100, 255), width=2 * S3)
    for k in range(1, 8): x = n * k / 8; d.line([(x, h * .14), (x, h * .76)], fill=(150, 155, 160, 255), width=S3)
    d.polygon([(n * .02, h * .45), (-n * .0, h * .15), (n * .12, h * .35)], fill=(160, 165, 170, 255))
    d.rounded_rectangle([n * .42, h * .78, n * .58, h * .95], radius=S3 * 3, fill=(80, 80, 85, 255))
    im = im.resize((size, int(size * .45)), Image.LANCZOS)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda v: int(v * .4)))
    out = Image.new("RGBA", (im.width + 24, im.height + 24), (0, 0, 0, 0)); out.alpha_composite(sh, (20, 20)); out.alpha_composite(im, (0, 0))
    return out

def _warship(size=70):
    n = size * S3; im = Image.new("RGBA", (n, int(n * .32)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    h = n * .32
    d.polygon([(0, h * .55), (n * .12, h * .25), (n * .88, h * .25), (n, h * .55), (n * .88, h * .85), (n * .12, h * .85)], fill=(175, 180, 185, 255),
              outline=(80, 85, 90, 255))
    d.rectangle([n * .38, h * .30, n * .62, h * .70], fill=(140, 145, 150, 255))
    for x in (.22, .78): d.ellipse([n * x - h * .14, h * .41, n * x + h * .14, h * .69], fill=(110, 115, 120, 255))
    im = im.resize((size, int(size * .32)), Image.LANCZOS)
    return im

def _jet(size=60, col=(215, 220, 228)):
    n = size * S3; im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    dk = (80, 85, 95, 255); c = col + (255,)
    d.polygon([(n * .5, n * .04), (n * .56, n * .2), (n * .56, n * .84), (n * .44, n * .84), (n * .44, n * .2)], fill=c, outline=dk)   # fuselage, nose up
    d.polygon([(n * .44, n * .36), (n * .04, n * .62), (n * .06, n * .68), (n * .44, n * .54)], fill=c, outline=dk)                 # swept wings
    d.polygon([(n * .56, n * .36), (n * .96, n * .62), (n * .94, n * .68), (n * .56, n * .54)], fill=c, outline=dk)
    d.polygon([(n * .44, n * .74), (n * .28, n * .88), (n * .44, n * .86)], fill=c, outline=dk)
    d.polygon([(n * .56, n * .74), (n * .72, n * .88), (n * .56, n * .86)], fill=c, outline=dk)
    im = im.resize((size, size), Image.LANCZOS)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda v: int(v * .45)))
    out = Image.new("RGBA", (size + 14, size + 14), (0, 0, 0, 0)); out.alpha_composite(sh, (12, 12)); out.alpha_composite(im, (0, 0))
    return out

def _train(size=70):
    n = size * S3; h = int(n * .5); im = Image.new("RGBA", (n, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    blk = (30, 30, 34, 255); red = (170, 40, 40, 255)
    d.rounded_rectangle([n * .30, h * .35, n * .92, h * .78], radius=h * .12, fill=blk)                          # boiler
    d.rectangle([n * .06, h * .18, n * .34, h * .78], fill=red, outline=blk, width=S3 * 2)                        # cab
    d.rectangle([n * .70, h * .08, n * .80, h * .38], fill=blk)                                                  # chimney
    d.polygon([(n * .92, h * .62), (n * 1.0, h * .86), (n * .88, h * .86)], fill=(120, 120, 125, 255))           # cowcatcher
    for x in (.18, .46, .66, .84): d.ellipse([n * x - h * .12, h * .70, n * x + h * .12, h * .94], fill=(60, 60, 64, 255), outline=(200, 170, 70, 255), width=S3)
    im = im.resize((size, int(size * .5)), Image.LANCZOS)
    out = Image.new("RGBA", (im.width + 10, im.height + 10), (0, 0, 0, 0))
    a = Image.new("L", out.size, 0); a.paste(im.getchannel("A"), (5, 5))
    ol = Image.new("RGBA", out.size, (255, 255, 255, 255)); ol.putalpha(a.filter(ImageFilter.MaxFilter(3)).point(lambda v: int(v * .85)))
    out.alpha_composite(ol); out.alpha_composite(im, (5, 5)); return out

def _rocket(size=90):
    n = size * S3; w = int(n * .36); im = Image.new("RGBA", (w, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    wh = (240, 240, 236, 255); dk = (60, 60, 66, 255)
    d.polygon([(w * .5, 0), (w * .70, n * .16), (w * .30, n * .16)], fill=wh, outline=dk)
    d.rectangle([w * .30, n * .16, w * .70, n * .80], fill=wh, outline=dk)
    for y in (.34, .56): d.rectangle([w * .30, n * y, w * .70, n * (y + .04)], fill=dk)
    d.polygon([(w * .30, n * .64), (w * .02, n * .86), (w * .30, n * .80)], fill=dk)
    d.polygon([(w * .70, n * .64), (w * .98, n * .86), (w * .70, n * .80)], fill=dk)
    d.polygon([(w * .34, n * .80), (w * .66, n * .80), (w * .5, n * 1.0)], fill=(255, 170, 40, 255))
    return im.resize((int(w / S3), size), Image.LANCZOS)

def sprite(kind, size):
    k = (kind, size)
    if k not in _cache:
        if kind == "steamer":
            import fx_eras as FE; _cache[k] = FE.ship("steamer", (190, 60, 50), size)
        else:
            _cache[k] = {"plane": _plane, "airship": _airship, "warship": _warship, "jet": _jet, "train": _train, "rocket": _rocket}[kind](size)
    return _cache[k]

# ---------------- path helpers ----------------
def _lens(pts): return [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
def point_at(pts, f):
    L = _lens(pts); tot = sum(L) or 1; tgt = tot * cl(f); acc = 0
    for (a, b), l in zip(zip(pts, pts[1:]), L):
        if acc + l >= tgt:
            u = (tgt - acc) / l if l else 0
            return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u), math.atan2(b[1] - a[1], b[0] - a[0])
        acc += l
    return pts[-1], math.atan2(pts[-1][1] - pts[-2][1], pts[-1][0] - pts[-2][0])

def dotted(d, pts, upto, col=(240, 240, 240, 200), dash=10, gap=9, width=4):
    L = _lens(pts); tot = sum(L); s = 0.0
    while s < tot * upto:
        p0, _ = point_at(pts, s / tot); p1, _ = point_at(pts, min(s + dash, tot * upto) / tot)
        d.line([p0, p1], fill=col, width=width); s += dash + gap

def rotate(im, ang_deg): return im.rotate(ang_deg, resample=Image.BICUBIC, expand=True)

# ---------------- drawers ----------------
def draw_front(fr, S, vw, t, ev, zscale):
    """Two rows of flag units along a (moving) front line."""
    t0 = ev.get("t_in", -1); tout = ev.get("t_out", 1e9)
    if t < t0 or t > tout + 0.5: return
    a = min(pr(t, t0, t0 + 0.6), 1 - pr(t, tout, tout + 0.5))
    k = eio(pr(t, ev.get("move0", 1e9), ev.get("move1", 1e9)))
    P0, P1 = ev["path0"], ev.get("path1", ev["path0"])
    geo = [(p0[0] + (p1[0] - p0[0]) * k, p0[1] + (p1[1] - p0[1]) * k) for p0, p1 in zip(P0, P1)]
    pts = [S(*p) for p in geo]
    sc = cl(zscale(vw) * ev.get("scale", 0.9), 0.55, 1.3)
    tot = sum(_lens(pts)); step = 30 * sc * ev.get("density", 1.0)
    n = int(tot / step)
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.line(pts, fill=(255, 255, 255, int(170 * a)), width=max(2, int(4 * sc)), joint="curve")
    lay = lay.filter(ImageFilter.GaussianBlur(1.2)); fr.paste(lay, (0, 0), lay)
    rnd = random.Random(7)
    for side, codes in ((-1, ev["side_a"]), (1, ev["side_b"])):
        for i in range(n):
            f = (i + 0.5) / n
            (x, y), ang = point_at(pts, f)
            code = codes[int(f * len(codes)) % len(codes)] if isinstance(codes[0], str) and ev.get("by_segment") else codes[i % len(codes)]
            jit = rnd.uniform(-3, 3); wob = math.sin(t * 2.5 + i) * 1.2
            for row in range(ev.get("rows", 2)):
                off = (16 + row * 22) * sc + jit
                px = x - math.sin(ang) * off * side; py = y + math.cos(ang) * off * side + wob
                im = flag(code, sc)
                if a < 0.999:
                    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
                fr.paste(im, (int(px - im.width / 2), int(py - im.height / 2)), im)

def draw_vehicle(fr, S, vw, t, ev, zscale):
    t0, t1 = ev["t0"], ev["t1"]; until = ev.get("until", t1 + 0.8)
    if t < t0 or t > until: return
    fade = 1 - pr(t, until - 0.5, until)
    if ev["kind"] == "rocket": return _draw_rocket(fr, S, vw, t, ev, zscale, fade)
    pts = [S(*p) for p in ev["path"]]
    k = pr(t, t0, t1) if ev.get("linear", True) else eio(pr(t, t0, t1))
    if ev.get("route", True):
        lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        kind = ev["kind"]; zw = zscale(vw)
        if kind == "train":      # railway: dark line with white sleepers, laid as the train goes
            seg = _upto(pts, 1.0 if ev.get("rail_first") else k)
            if len(seg) > 1:
                d.line(seg, fill=(30, 30, 30, int(230 * fade)), width=max(3, int(7 * zw)), joint="curve")
                dotted(d, seg, 1.0, col=(240, 240, 235, int(220 * fade)), dash=3, gap=9, width=max(5, int(13 * zw)))
                d.line(seg, fill=(30, 30, 30, int(230 * fade)), width=max(2, int(3 * zw)), joint="curve")
        elif kind == "jet":      # contrail: solid white line fading towards the tail
            seg = _upto(pts, k)
            if len(seg) > 1:
                d.line(seg, fill=(255, 255, 255, int(150 * fade)), width=max(2, int(5 * zw)), joint="curve")
                lay = lay.filter(ImageFilter.GaussianBlur(1.5)); d = ImageDraw.Draw(lay)
        elif kind == "rocket":
            pass
        else:
            dotted(d, pts, k if kind not in ("warship", "steamer") else 1.0, col=(235, 235, 235, int(190 * fade)), width=max(2, int(4 * zw)))
        fr.paste(lay, (0, 0), lay)
    (x, y), ang = point_at(pts, k)
    size = int({"plane": 54, "airship": 120, "warship": 78, "jet": 58, "train": 64, "steamer": 66}[ev["kind"]] * zscale(vw) * ev.get("scale", 1.0))
    im = sprite(ev["kind"], size)
    if ev["kind"] == "train":
        rnd = random.Random(int(t * 30))
        lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)   # steam puffs drifting behind
        for j in range(5):
            (px, py), _ = point_at(pts, max(0, k - 0.015 * (j + 1)))
            r = (7 + j * 4) * zscale(vw); py -= (18 + j * 6) * zscale(vw)
            d.ellipse([px - r, py - r, px + r, py + r], fill=(245, 245, 245, int(150 * fade * (1 - j / 5))))
        fr.paste(lay.filter(ImageFilter.GaussianBlur(2)), (0, 0), lay.filter(ImageFilter.GaussianBlur(2)))
        if math.cos(ang) < 0: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif ev["kind"] in ("plane", "jet"): im = rotate(im, -math.degrees(ang) - 90)
    elif ev["kind"] == "steamer":
        if math.cos(ang) < 0: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif ev["kind"] == "warship":
        im = rotate(im, -math.degrees(ang))
        lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)   # wake
        for j in range(6):
            (wx, wy), _ = point_at(pts, max(0, k - 0.012 * (j + 1)))
            r = (6 + j * 3) * zscale(vw); d.ellipse([wx - r, wy - r, wx + r, wy + r], outline=(255, 255, 255, int(120 * fade * (1 - j / 6))), width=2)
        fr.paste(lay, (0, 0), lay)
    else:
        if math.cos(ang) < 0: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if fade < 0.999:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * fade)))
    fr.paste(im, (int(x - im.width / 2), int(y - im.height / 2)), im)

def _upto(pts, k):
    L = _lens(pts); tot = sum(L); tgt = tot * cl(k); out = [pts[0]]; acc = 0
    for (a, b), l in zip(zip(pts, pts[1:]), L):
        if acc + l < tgt: out.append(b); acc += l
        else:
            u = (tgt - acc) / l if l else 0; out.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)); break
    return out

def _draw_rocket(fr, S, vw, t, ev, zscale, fade):
    """Rocket launch from ev["path"][0]: rises straight up on screen with a flame and smoke column."""
    x, y = S(*ev["path"][0]); p = eio(pr(t, ev["t0"], ev["t1"])); z = zscale(vw) * ev.get("scale", 1.0)
    rise = p * ev.get("height", 700) * z
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rnd = random.Random(int(t * 25))
    for j in range(14):
        f = j / 14; yy = y - rise * f; r = (10 + 22 * (1 - f)) * z * rnd.uniform(.8, 1.2)
        d.ellipse([x - r + rnd.uniform(-4, 4), yy - r, x + r, yy + r], fill=(235, 235, 235, int(150 * fade * (0.4 + 0.6 * (1 - f)))))
    fr.paste(lay.filter(ImageFilter.GaussianBlur(4)), (0, 0), lay.filter(ImageFilter.GaussianBlur(4)))
    im = sprite("rocket", int(90 * z))
    if fade < 0.999:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * fade)))
    fr.paste(im, (int(x - im.width / 2), int(y - rise - im.height * .8)), im)

def draw_glow(fr, S, vw, t, ev):
    """A soft searchlight sweep over a conquered area."""
    t0, t1 = ev["t0"], ev["t1"]
    if t < t0 or t > t1: return
    p = pr(t, t0, t1); a = math.sin(math.pi * p)
    x, y = S(*ev["pos"]); R = ev.get("radius", 420)
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ang = ev.get("a0", -40) + (ev.get("a1", 40) - ev.get("a0", -40)) * p
    d.pieslice([x - R, y - R, x + R, y + R], ang - 14, ang + 14, fill=(255, 235, 225, int(110 * a)))
    lay = lay.filter(ImageFilter.GaussianBlur(28)); fr.paste(lay, (0, 0), lay)

def draw_cities(fr, S, vw, t, ev, zscale):
    """Glowing city lights (industrial/modern eras). ev: cities=[(lon,lat,weight 0.3-1.5)], t0, t1 (fade/grow in), until."""
    t0 = ev["t0"]; until = ev.get("until", 1e9)
    if t < t0 or t > until: return
    g = eio(pr(t, t0, ev.get("t1", t0 + 1.5))) * (1 - pr(t, until - 0.5, until))
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); z = zscale(vw)
    col = ev.get("color", (255, 214, 140))
    for i, (lon, lat, w) in enumerate(ev["cities"]):
        x, y = S(lon, lat)
        if x < -50 or y < -50 or x > fr.width + 50 or y > fr.height + 50: continue
        tw = 0.85 + 0.15 * math.sin(t * 3 + i * 1.7)
        r = 46 * w * z * g * tw
        d.ellipse([x - r, y - r, x + r, y + r], fill=col + (int(170 * g),))
    lay = lay.filter(ImageFilter.GaussianBlur(10 * z))
    d = ImageDraw.Draw(lay)
    for lon, lat, w in ev["cities"]:
        x, y = S(lon, lat); r = 6 * w * z * g
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 250, 235, int(255 * g)))
    fr.paste(lay, (0, 0), lay)
