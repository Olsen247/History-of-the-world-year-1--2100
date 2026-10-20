"""Map effects: symbol icons, marching armies with arrows, explosions/clashes."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

S3 = 4  # supersample

def _finish(im, size, outline=True, shadow=True):
    im = im.resize((size, size), Image.LANCZOS)
    pad = int(size * 0.18)
    out = Image.new("RGBA", (size + 2 * pad, size + 2 * pad), (0, 0, 0, 0))
    a = Image.new("L", out.size, 0); a.paste(im.getchannel("A"), (pad, pad))
    if shadow:
        sh = Image.new("RGBA", out.size, (0, 0, 0, 255)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(size * 0.05)).point(lambda v: int(v * 0.75)))
        out.alpha_composite(sh, (int(size * 0.03), int(size * 0.05)))
    if outline:
        ol = Image.new("RGBA", out.size, (255, 255, 255, 255)); ol.putalpha(a.filter(ImageFilter.MaxFilter(5)))
        out.alpha_composite(ol)
    out.alpha_composite(im, (pad, pad))
    return out

def _canvas(size): n = size * S3; return Image.new("RGBA", (n, n), (0, 0, 0, 0)), n

def icon_gold(size=130):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    def bar(cx, cy, w, h):
        top = [(cx - w * 0.36, cy - h / 2), (cx + w * 0.36, cy - h / 2), (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)]
        d.polygon(top, fill=(214, 160, 30, 255), outline=(120, 80, 10, 255), width=n // 90)
        d.polygon([(cx - w * 0.36, cy - h / 2), (cx + w * 0.36, cy - h / 2), (cx + w * 0.30, cy - h * 0.2), (cx - w * 0.30, cy - h * 0.2)], fill=(255, 226, 110, 255))
        d.line([(cx - w * 0.28, cy - h * 0.35), (cx + w * 0.05, cy - h * 0.35)], fill=(255, 250, 220, 255), width=n // 70)
    w, h = n * 0.44, n * 0.2
    bar(n * 0.28, n * 0.70, w, h); bar(n * 0.72, n * 0.70, w, h); bar(n * 0.50, n * 0.48, w, h)
    for sx, sy in ((0.22, 0.30), (0.80, 0.36)):
        x, y, r = n * sx, n * sy, n * 0.05
        d.polygon([(x, y - r), (x + r * 0.25, y - r * 0.25), (x + r, y), (x + r * 0.25, y + r * 0.25), (x, y + r), (x - r * 0.25, y + r * 0.25), (x - r, y), (x - r * 0.25, y - r * 0.25)], fill=(255, 250, 200, 255))
    return _finish(im, size)

def icon_scroll(size=130):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    paper = (238, 224, 186, 255); edge = (130, 100, 60, 255); w = n // 80
    d.rounded_rectangle([n * 0.2, n * 0.2, n * 0.8, n * 0.8], radius=n * 0.03, fill=paper, outline=edge, width=w)
    for yy in (0.2, 0.8):
        d.rounded_rectangle([n * 0.14, n * (yy - 0.06), n * 0.86, n * (yy + 0.06)], radius=n * 0.06, fill=(214, 194, 150, 255), outline=edge, width=w)
    for i in range(5):
        x = n * (0.32 + i * 0.09)
        for j in range(4):
            y = n * (0.33 + j * 0.11)
            d.line([(x, y), (x, y + n * 0.06)], fill=(40, 30, 20, 255), width=n // 60)
            d.line([(x - n * 0.025, y + n * 0.03), (x + n * 0.025, y + n * 0.03)], fill=(40, 30, 20, 255), width=n // 80)
    return _finish(im, size)

def icon_temple(size=140, col=(214, 140, 120)):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    c = col + (255,); dk = tuple(int(v * 0.55) for v in col) + (255,); w = n // 90
    d.polygon([(n * 0.12, n * 0.32), (n * 0.5, n * 0.12), (n * 0.88, n * 0.32)], fill=c, outline=dk, width=w)
    d.rectangle([n * 0.14, n * 0.32, n * 0.86, n * 0.38], fill=c, outline=dk, width=w)
    for i in range(5):
        x = n * (0.2 + i * 0.15)
        d.rectangle([x - n * 0.03, n * 0.38, x + n * 0.03, n * 0.78], fill=c, outline=dk, width=w)
    d.rectangle([n * 0.1, n * 0.78, n * 0.9, n * 0.86], fill=c, outline=dk, width=w)
    return _finish(im, size)

def icon_wheel(size=130):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    gold = (238, 186, 50, 255); dk = (120, 80, 10, 255); c = n / 2; R = n * 0.36
    d.ellipse([c - R, c - R, c + R, c + R], outline=gold, width=n // 14)
    d.ellipse([c - R * 0.22, c - R * 0.22, c + R * 0.22, c + R * 0.22], fill=gold, outline=dk, width=n // 90)
    for k in range(8):
        a = k * math.pi / 4
        d.line([(c + math.cos(a) * R * 0.2, c + math.sin(a) * R * 0.2), (c + math.cos(a) * R, c + math.sin(a) * R)], fill=gold, width=n // 22)
        x, y = c + math.cos(a) * R * 1.12, c + math.sin(a) * R * 1.12
        d.ellipse([x - n * 0.035, y - n * 0.035, x + n * 0.035, y + n * 0.035], fill=gold)
    return _finish(im, size)

def icon_ship(size=130, sail=(196, 52, 62)):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    wood = (120, 78, 40, 255); dk = (60, 36, 16, 255); w = n // 90
    d.polygon([(n * 0.1, n * 0.62), (n * 0.9, n * 0.62), (n * 0.78, n * 0.78), (n * 0.22, n * 0.78)], fill=wood, outline=dk, width=w)
    for i in range(7): d.line([(n * (0.22 + i * 0.09), n * 0.78), (n * (0.18 + i * 0.09), n * 0.9)], fill=dk, width=n // 70)
    d.line([(n * 0.5, n * 0.62), (n * 0.5, n * 0.14)], fill=dk, width=n // 40)
    d.polygon([(n * 0.26, n * 0.2), (n * 0.74, n * 0.2), (n * 0.7, n * 0.56), (n * 0.3, n * 0.56)], fill=sail + (255,), outline=dk, width=w)
    return _finish(im, size)

def icon_camel(size=130):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    c = (196, 150, 96, 255); dk = (90, 60, 30, 255)
    pts = [(0.18, 0.55), (0.25, 0.42), (0.36, 0.4), (0.42, 0.28), (0.5, 0.38), (0.58, 0.3), (0.66, 0.4), (0.72, 0.42), (0.78, 0.3),
           (0.84, 0.22), (0.92, 0.24), (0.9, 0.3), (0.84, 0.32), (0.8, 0.55), (0.74, 0.58), (0.26, 0.58)]
    d.polygon([(x * n, y * n) for x, y in pts], fill=c, outline=dk, width=n // 90)
    for x in (0.3, 0.38, 0.66, 0.74):
        d.line([(x * n, 0.56 * n), (x * n, 0.86 * n)], fill=dk, width=n // 28)
    return _finish(im, size)

def icon_people(size=130, crossed=False):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    for i, (x, s_) in enumerate(((0.3, 0.8), (0.7, 0.8), (0.5, 1.0))):
        c = (236, 236, 240, 255) if i == 2 else (200, 204, 214, 255)
        r = n * 0.09 * s_; cx, cy = n * x, n * (0.36 if i == 2 else 0.42)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
        d.rounded_rectangle([cx - r * 1.6, cy + r * 1.3, cx + r * 1.6, cy + r * 4.4], radius=r * 1.2, fill=c)
    if crossed:
        d.ellipse([n * 0.08, n * 0.08, n * 0.92, n * 0.92], outline=(226, 50, 50, 255), width=n // 14)
        d.line([(n * 0.22, n * 0.22), (n * 0.78, n * 0.78)], fill=(226, 50, 50, 255), width=n // 14)
    return _finish(im, size)

def icon_laurel(size=140, col=(160, 160, 160)):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    c = col + (255,); dk = tuple(int(v * 0.5) for v in col) + (255,); cx, cy, R = n / 2, n * 0.52, n * 0.34
    for side in (-1, 1):
        for k in range(8):
            a = math.radians(-80 + k * 21)
            x = cx + side * R * math.cos(a); y = cy - R * math.sin(a)
            ang = math.atan2(-(math.cos(a)), side * math.sin(a))
            L, Wd = n * 0.09, n * 0.035
            pts = [(x + L * math.cos(t) * math.cos(ang) - Wd * math.sin(t) * math.sin(ang),
                    y + L * math.cos(t) * math.sin(ang) + Wd * math.sin(t) * math.cos(ang)) for t in np.linspace(0, 2 * math.pi, 16)]
            d.polygon(pts, fill=c, outline=dk)
    d.line([(cx - n * 0.1, cy + R * 0.98), (cx + n * 0.1, cy + R * 0.98)], fill=dk, width=n // 30)
    d.line([(n * 0.5, n * 0.1), (n * 0.42, n * 0.45), (n * 0.56, n * 0.55), (n * 0.48, n * 0.9)], fill=(20, 20, 24, 255), width=n // 40)
    return _finish(im, size)

def icon_swords(size=120):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    steel = (226, 230, 238, 255); dk = (70, 74, 84, 255); hilt = (150, 100, 40, 255)
    for s_ in (-1, 1):
        a = math.radians(45 * s_); ca, sa = math.cos(a), math.sin(a)
        def P(u, v): return (n / 2 + u * ca * n - v * sa * n, n / 2 + u * sa * n + v * ca * n)
        d.polygon([P(-0.02, -0.4), P(0.02, -0.4), P(0.03, 0.18), P(0, 0.24), P(-0.03, 0.18)][::-1] and
                  [P(-0.035, 0.2), P(-0.035, -0.32), P(0, -0.42), P(0.035, -0.32), P(0.035, 0.2)], fill=steel, outline=dk, width=n // 100)
        d.line([P(-0.12, 0.2), P(0.12, 0.2)], fill=hilt, width=n // 25)
        d.line([P(0, 0.2), P(0, 0.36)], fill=hilt, width=n // 22)
        d.ellipse([P(0, 0.38)[0] - n * 0.03, P(0, 0.38)[1] - n * 0.03, P(0, 0.38)[0] + n * 0.03, P(0, 0.38)[1] + n * 0.03], fill=hilt)
    return _finish(im, size)

def icon_bird(size=150):
    """Nazca hummingbird geoglyph style (white line drawing)."""
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    w = n // 45; c = (250, 246, 236, 255)
    L = lambda pts: d.line([(x * n, y * n) for x, y in pts], fill=c, width=w, joint="curve")
    L([(0.5, 0.02), (0.5, 0.26)])                                   # beak
    d.ellipse([n * 0.44, n * 0.24, n * 0.56, n * 0.36], outline=c, width=w)  # head
    L([(0.46, 0.35), (0.42, 0.62), (0.5, 0.7), (0.58, 0.62), (0.54, 0.35)])  # body
    L([(0.45, 0.42), (0.08, 0.36), (0.14, 0.44), (0.1, 0.5), (0.18, 0.54), (0.16, 0.6), (0.44, 0.52)])  # left wing
    L([(0.55, 0.42), (0.92, 0.36), (0.86, 0.44), (0.9, 0.5), (0.82, 0.54), (0.84, 0.6), (0.56, 0.52)])  # right wing
    L([(0.46, 0.68), (0.36, 0.95), (0.46, 0.84), (0.5, 0.97), (0.54, 0.84), (0.64, 0.95), (0.54, 0.68)])  # tail
    return _finish(im, size, outline=False)

def icon_fire(size=140):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    def flame(cx, base, h, w, col):
        pts = []
        for k in range(25):
            t = k / 24; a = math.pi * t
            r = math.sin(a) ** 0.8 * w * (1 - 0.6 * t)
            pts.append((cx - r, base - h * t))
        top = (cx + w * 0.15, base - h * 1.05)
        right = [(cx + p[0] * -1 + 2 * cx - 2 * cx, 0) for p in []]
        pts2 = [(2 * cx - x, y) for x, y in pts[::-1]]
        d.polygon(pts + [top] + pts2, fill=col)
    flame(n * 0.5, n * 0.9, n * 0.8, n * 0.36, (220, 60, 20, 255))
    flame(n * 0.5, n * 0.9, n * 0.58, n * 0.26, (250, 140, 30, 255))
    flame(n * 0.5, n * 0.9, n * 0.36, n * 0.15, (255, 230, 120, 255))
    return _finish(im, size)

def icon_rat(size=140):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    g = (110, 105, 100, 255); dg = (70, 66, 62, 255)
    d.ellipse([n * 0.18, n * 0.38, n * 0.72, n * 0.74], fill=g)
    d.polygon([(n * 0.66, n * 0.44), (n * 0.92, n * 0.56), (n * 0.66, n * 0.68)], fill=g)
    d.ellipse([n * 0.58, n * 0.34, n * 0.72, n * 0.48], fill=(170, 140, 140, 255))
    d.ellipse([n * 0.78, n * 0.50, n * 0.82, n * 0.54], fill=(20, 20, 20, 255))
    d.arc([n * 0.02, n * 0.40, n * 0.30, n * 0.86], 90, 250, fill=dg, width=int(n * 0.03))
    for x in (0.32, 0.56): d.line([(n * x, n * 0.72), (n * x, n * 0.80)], fill=dg, width=int(n * 0.04))
    return _finish(im, size)

def icon_pyramid(size=140):
    im, n = _canvas(size); d = ImageDraw.Draw(im)
    for i in range(5):
        y0 = n * (0.82 - i * 0.13); hw = n * (0.42 - i * 0.075)
        d.polygon([(n / 2 - hw, y0), (n / 2 + hw, y0), (n / 2 + hw - n * 0.04, y0 - n * 0.13), (n / 2 - hw + n * 0.04, y0 - n * 0.13)],
                  fill=(186, 150, 110, 255), outline=(100, 74, 50, 255), width=n // 90)
    d.rectangle([n * 0.46, n * 0.17, n * 0.54, n * 0.82], fill=(150, 116, 80, 255))
    return _finish(im, size)

ICONS = dict(gold=icon_gold, scroll=icon_scroll, temple=icon_temple, wheel=icon_wheel, ship=icon_ship, camel=icon_camel,
             people=icon_people, nopeople=lambda size=130: icon_people(size, True), laurel=icon_laurel, swords=icon_swords,
             bird=icon_bird, pyramid=icon_pyramid, fire=icon_fire, rat=icon_rat)

def _horse(d, n, x0, y0, sc, coat=(110, 72, 44, 255)):
    """Side-view horse facing right; (x0, y0) = top-left of a 1.0 x 0.8 box scaled by sc*n."""
    P = lambda x, y: (x0 + x * n * sc, y0 + y * n * sc)
    body = [P(0.18, 0.30), P(0.70, 0.28), P(0.80, 0.18), P(0.88, 0.05), P(1.0, 0.08), P(0.98, 0.16), P(0.90, 0.20),
            P(0.82, 0.42), P(0.74, 0.48), P(0.26, 0.50), P(0.12, 0.44), P(0.06, 0.52), P(0.04, 0.40)]
    d.polygon(body, fill=coat)
    lw = max(2, int(n * sc * 0.06))
    for (xa, xb) in ((0.26, 0.20), (0.34, 0.40), (0.70, 0.64), (0.78, 0.84)):
        d.line([P(xa, 0.46), P(xb, 0.80)], fill=coat, width=lw)
    d.line([P(0.86, 0.06), P(0.74, 0.26)], fill=(40, 26, 16, 255), width=max(2, lw // 2))

def soldier(col, size=40, kind="legion"):
    import fx_eras as FE
    if kind in FE.FOOT2:
        im = FE.soldier(col, size, kind); return _sol_finish(im.crop(im.getbbox()))
    n = size * S3; W_, H_ = int(n * 1.5), int(n * 1.5)
    im = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    body = (40, 34, 30, 255); c = col + (255,); dk = tuple(int(v * 0.5) for v in col) + (255,)
    if kind in ("han", "rebel", "redturban"):
        ox = n * 0.25
        skin = (214, 170, 130, 255)
        d.ellipse([ox + n * 0.38, n * 0.14, ox + n * 0.62, n * 0.38], fill=skin)
        if kind == "han":   # Chinese infantry: conical helmet, lamellar coat, ji halberd
            d.polygon([(ox + n * 0.32, n * 0.22), (ox + n * 0.68, n * 0.22), (ox + n * 0.5, n * 0.02)], fill=(70, 70, 76, 255))
            d.rounded_rectangle([ox + n * 0.33, n * 0.38, ox + n * 0.67, n * 1.0], radius=n * 0.08, fill=c, outline=dk, width=n // 30)
            for yy in (0.52, 0.66, 0.8): d.line([(ox + n * 0.36, n * yy), (ox + n * 0.64, n * yy)], fill=dk, width=n // 50)
            d.line([(ox + n * 0.82, n * 0.0), (ox + n * 0.82, n * 1.36)], fill=(120, 90, 50, 255), width=n // 20)
            d.polygon([(ox + n * 0.78, n * 0.04), (ox + n * 0.86, n * 0.04), (ox + n * 0.82, -n * 0.1)], fill=(220, 220, 228, 255))
            d.polygon([(ox + n * 0.82, n * 0.12), (ox + n * 0.98, n * 0.08), (ox + n * 0.98, n * 0.18), (ox + n * 0.82, n * 0.2)], fill=(220, 220, 228, 255))
        else:               # Yellow Turban (rebel) / Red Turban (redturban) rebel: coloured headband, plain tunic, pitchfork
            band = (220, 40, 40, 255) if kind == "redturban" else (250, 210, 30, 255)
            d.rectangle([ox + n * 0.36, n * 0.16, ox + n * 0.64, n * 0.24], fill=band)
            d.polygon([(ox + n * 0.62, n * 0.18), (ox + n * 0.78, n * 0.12), (ox + n * 0.74, n * 0.26)], fill=band)
            d.rounded_rectangle([ox + n * 0.35, n * 0.38, ox + n * 0.65, n * 0.98], radius=n * 0.08, fill=(150, 120, 80, 255))
            d.line([(ox + n * 0.84, n * 0.06), (ox + n * 0.84, n * 1.36)], fill=(120, 90, 50, 255), width=n // 20)
            for dx in (-0.06, 0, 0.06): d.line([(ox + n * (0.84 + dx), n * -0.04), (ox + n * (0.84 + dx), n * 0.08)], fill=(160, 160, 165, 255), width=n // 40)
            d.line([(ox + n * 0.78, n * 0.08), (ox + n * 0.90, n * 0.08)], fill=(160, 160, 165, 255), width=n // 40)
        d.line([(ox + n * 0.42, n * 0.96), (ox + n * 0.36, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.58, n * 0.96), (ox + n * 0.64, n * 1.46)], fill=body, width=n // 9)
    elif kind in ("goth", "viking", "frank", "byzantine"):
        ox = n * 0.25; skin = (226, 186, 150, 255)
        hair = (180, 130, 70, 255) if kind != "byzantine" else (60, 45, 30, 255)
        d.rounded_rectangle([ox + n * 0.36, n * 0.40, ox + n * 0.64, n * 0.98], radius=n * 0.08, fill=c, outline=dk, width=n // 30)
        d.line([(ox + n * 0.42, n * 0.96), (ox + n * 0.36, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.58, n * 0.96), (ox + n * 0.64, n * 1.46)], fill=body, width=n // 9)
        if kind in ("goth", "frank"): d.rounded_rectangle([ox + n * 0.33, n * 0.12, ox + n * 0.67, n * 0.56], radius=n * 0.1, fill=hair)
        d.ellipse([ox + n * 0.37, n * 0.13, ox + n * 0.63, n * 0.40], fill=skin)
        if kind != "byzantine": d.chord([ox + n * 0.37, n * 0.26, ox + n * 0.63, n * 0.48], 0, 180, fill=hair)
        if kind == "viking":   # conical helmet with nose guard, round painted shield, axe
            d.polygon([(ox + n * 0.34, n * 0.24), (ox + n * 0.66, n * 0.24), (ox + n * 0.5, n * 0.02)], fill=(130, 130, 140, 255))
            d.rectangle([ox + n * 0.48, n * 0.22, ox + n * 0.52, n * 0.34], fill=(130, 130, 140, 255))
            d.line([(ox + n * 0.80, n * 0.20), (ox + n * 0.80, n * 1.2)], fill=(120, 90, 50, 255), width=n // 18)
            d.chord([ox + n * 0.74, n * 0.14, ox + n * 1.0, n * 0.42], 270, 90, fill=(210, 210, 220, 255))
        elif kind == "frank":  # throwing axe
            d.line([(ox + n * 0.80, n * 0.30), (ox + n * 0.80, n * 1.0)], fill=(120, 90, 50, 255), width=n // 18)
            d.chord([ox + n * 0.74, n * 0.22, ox + n * 0.98, n * 0.46], 270, 90, fill=(210, 210, 220, 255))
        elif kind == "byzantine":  # plumed helmet + spear
            d.chord([ox + n * 0.36, n * 0.10, ox + n * 0.64, n * 0.34], 180, 360, fill=(170, 170, 180, 255))
            d.ellipse([ox + n * 0.44, -n * 0.04, ox + n * 0.56, n * 0.14], fill=c)
            d.line([(ox + n * 0.80, n * 0.0), (ox + n * 0.80, n * 1.32)], fill=(140, 110, 70, 255), width=n // 18)
            d.polygon([(ox + n * 0.76, n * 0.02), (ox + n * 0.84, n * 0.02), (ox + n * 0.80, -n * 0.12)], fill=(220, 220, 228, 255))
        else:                  # goth: spear
            d.line([(ox + n * 0.80, n * 0.02), (ox + n * 0.80, n * 1.32)], fill=(140, 110, 70, 255), width=n // 18)
            d.polygon([(ox + n * 0.76, n * 0.04), (ox + n * 0.84, n * 0.04), (ox + n * 0.80, -n * 0.12)], fill=(220, 220, 228, 255))
        if kind == "byzantine":
            d.ellipse([ox + n * 0.04, n * 0.40, ox + n * 0.50, n * 1.12], fill=c, outline=(240, 210, 90, 255), width=n // 26)
        else:
            d.ellipse([ox + n * 0.02, n * 0.46, ox + n * 0.50, n * 0.94], fill=c, outline=dk, width=n // 22)
            if kind == "viking":
                d.line([(ox + n * 0.26, n * 0.47), (ox + n * 0.26, n * 0.93)], fill=(240, 240, 240, 255), width=n // 30)
                d.line([(ox + n * 0.03, n * 0.70), (ox + n * 0.49, n * 0.70)], fill=(240, 240, 240, 255), width=n // 30)
            d.ellipse([ox + n * 0.20, n * 0.64, ox + n * 0.32, n * 0.76], fill=(200, 200, 205, 255))
    elif kind == "aztec":   # Mexica warrior: feather headdress, round shield, wooden club
        ox = n * 0.25; skin = (170, 115, 80, 255)
        d.rounded_rectangle([ox + n * 0.36, n * 0.40, ox + n * 0.64, n * 0.98], radius=n * 0.08, fill=c, outline=dk, width=n // 30)
        d.line([(ox + n * 0.42, n * 0.96), (ox + n * 0.36, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.58, n * 0.96), (ox + n * 0.64, n * 1.46)], fill=body, width=n // 9)
        d.ellipse([ox + n * 0.37, n * 0.13, ox + n * 0.63, n * 0.40], fill=skin)
        for k, fc in enumerate([(40, 160, 90), (230, 60, 50), (40, 160, 90), (240, 200, 60), (40, 160, 90)]):
            a = math.radians(200 + k * 35); d.line([(ox + n * 0.5, n * 0.18), (ox + n * 0.5 + math.cos(a) * n * 0.26, n * 0.18 + math.sin(a) * n * 0.26)], fill=fc + (255,), width=n // 14)
        d.rectangle([ox + n * 0.78, n * 0.20, ox + n * 0.84, n * 1.0], fill=(110, 75, 40, 255))
        for yy in (0.28, 0.42, 0.56): d.polygon([(ox + n * 0.84, n * yy), (ox + n * 0.92, n * (yy + 0.04)), (ox + n * 0.84, n * (yy + 0.08))], fill=(40, 40, 50, 255))
        d.ellipse([ox + n * 0.02, n * 0.46, ox + n * 0.50, n * 0.94], fill=(240, 230, 200, 255), outline=dk, width=n // 22)
        d.ellipse([ox + n * 0.14, n * 0.58, ox + n * 0.38, n * 0.82], outline=c, width=n // 22)
    elif kind == "rus":     # Muscovite foot soldier: tall pointed shishak helmet, red kite shield, spear
        ox = n * 0.25; skin = (226, 186, 150, 255); hair = (120, 85, 50, 255)
        d.rounded_rectangle([ox + n * 0.36, n * 0.40, ox + n * 0.64, n * 0.98], radius=n * 0.08, fill=c, outline=dk, width=n // 30)
        d.line([(ox + n * 0.42, n * 0.96), (ox + n * 0.36, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.58, n * 0.96), (ox + n * 0.64, n * 1.46)], fill=body, width=n // 9)
        d.ellipse([ox + n * 0.37, n * 0.13, ox + n * 0.63, n * 0.40], fill=skin)
        d.chord([ox + n * 0.37, n * 0.28, ox + n * 0.63, n * 0.50], 0, 180, fill=hair)
        d.polygon([(ox + n * 0.34, n * 0.24), (ox + n * 0.66, n * 0.24), (ox + n * 0.56, n * 0.06), (ox + n * 0.5, -n * 0.12), (ox + n * 0.44, n * 0.06)], fill=(150, 150, 160, 255), outline=(90, 90, 100, 255))
        d.line([(ox + n * 0.80, n * 0.0), (ox + n * 0.80, n * 1.32)], fill=(140, 110, 70, 255), width=n // 18)
        d.polygon([(ox + n * 0.76, n * 0.02), (ox + n * 0.84, n * 0.02), (ox + n * 0.80, -n * 0.12)], fill=(220, 220, 228, 255))
        d.polygon([(ox + n * 0.04, n * 0.44), (ox + n * 0.48, n * 0.44), (ox + n * 0.46, n * 0.70), (ox + n * 0.26, n * 1.16), (ox + n * 0.06, n * 0.70)], fill=(190, 40, 40, 255), outline=(240, 210, 90, 255))
    elif kind == "legion":  # Roman legionary: crested helmet, big rectangular shield, pilum
        ox = n * 0.25
        d.ellipse([ox + n * 0.36, n * 0.12, ox + n * 0.64, n * 0.40], fill=(150, 150, 160, 255))
        d.polygon([(ox + n * 0.34, n * 0.16), (ox + n * 0.66, n * 0.16), (ox + n * 0.5, n * 0.02)], fill=c)
        d.rounded_rectangle([ox + n * 0.36, n * 0.40, ox + n * 0.64, n * 0.96], radius=n * 0.1, fill=body)
        d.line([(ox + n * 0.42, n * 0.94), (ox + n * 0.36, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.58, n * 0.94), (ox + n * 0.64, n * 1.46)], fill=body, width=n // 9)
        d.line([(ox + n * 0.80, n * 0.10), (ox + n * 0.80, n * 1.30)], fill=(140, 110, 70, 255), width=n // 18)
        d.polygon([(ox + n * 0.76, n * 0.12), (ox + n * 0.84, n * 0.12), (ox + n * 0.80, -n * 0.0)], fill=(220, 220, 228, 255))
        d.rounded_rectangle([ox + n * 0.06, n * 0.42, ox + n * 0.52, n * 1.10], radius=n * 0.06, fill=c, outline=dk, width=n // 28)
        d.ellipse([ox + n * 0.23, n * 0.70, ox + n * 0.35, n * 0.82], fill=(240, 210, 90, 255))
    else:
        coat = {"xianbei": (150, 130, 110, 255), "hun": (70, 50, 36, 255), "mongol": (120, 95, 70, 255), "knight": (235, 232, 225, 255), "sasanian": (150, 150, 160, 255), "arab": (230, 225, 215, 255), "timurid": (90, 70, 60, 255), "serb": (110, 100, 95, 255)}.get(kind, (96, 64, 40, 255))
        _horse(d, n, n * 0.02, n * 0.62, 1.4, coat=coat)
        if kind == "sasanian":   # armoured horse: mail barding rows
            pass
        rx, ry = n * 0.50, n * 0.40   # rider on the horse back
        d.rounded_rectangle([rx, ry + n * 0.28, rx + n * 0.26, ry + n * 0.62], radius=n * 0.08, fill=c, outline=dk, width=n // 30)
        d.ellipse([rx + n * 0.03, ry + n * 0.04, rx + n * 0.23, ry + n * 0.26], fill=(200, 160, 120, 255))
        d.line([(rx + n * 0.12, ry + n * 0.6), (rx + n * 0.02, ry + n * 0.86)], fill=body, width=n // 12)
        if kind == "parthian":   # horse archer: pointed cap + bow
            d.polygon([(rx + n * 0.0, ry + n * 0.10), (rx + n * 0.26, ry + n * 0.10), (rx + n * 0.08, ry - n * 0.12)], fill=dk)
            d.arc([rx + n * 0.24, ry + n * 0.06, rx + n * 0.56, ry + n * 0.62], 280, 80, fill=(120, 80, 30, 255), width=n // 22)
            d.line([(rx + n * 0.46, ry + n * 0.08), (rx + n * 0.46, ry + n * 0.6)], fill=(230, 230, 230, 255), width=n // 60)
        elif kind == "kushan":   # armoured lancer: tall helmet + long lance + pennant
            d.polygon([(rx + n * 0.02, ry + n * 0.10), (rx + n * 0.24, ry + n * 0.10), (rx + n * 0.13, ry - n * 0.08)], fill=(170, 170, 180, 255))
            d.line([(rx - n * 0.30, ry + n * 0.56), (rx + n * 0.90, ry + n * 0.16)], fill=(130, 100, 60, 255), width=n // 20)
            d.polygon([(rx + n * 0.90, ry + n * 0.16), (rx + n * 0.80, ry + n * 0.14), (rx + n * 0.84, ry + n * 0.24)], fill=(225, 225, 232, 255))
            d.polygon([(rx + n * 0.66, ry + n * 0.24), (rx + n * 0.80, ry + n * 0.10), (rx + n * 0.74, ry + n * 0.30)], fill=c)
        elif kind == "hun":      # Hun horse archer: tall fur-trimmed cap + recurve bow + scale coat
            d.polygon([(rx + n * 0.0, ry + n * 0.10), (rx + n * 0.26, ry + n * 0.10), (rx + n * 0.18, ry - n * 0.16), (rx + n * 0.06, ry - n * 0.14)], fill=(70, 45, 35, 255))
            d.rectangle([rx - n * 0.02, ry + n * 0.06, rx + n * 0.28, ry + n * 0.12], fill=(170, 140, 100, 255))
            d.arc([rx + n * 0.20, ry + n * 0.02, rx + n * 0.58, ry + n * 0.66], 270, 90, fill=(60, 40, 20, 255), width=n // 18)
            d.line([(rx + n * 0.39, ry + n * 0.04), (rx + n * 0.39, ry + n * 0.64)], fill=(230, 230, 230, 255), width=n // 60)
        elif kind == "sasanian": # cataphract: plumed helmet + lance + banner
            d.chord([rx + n * 0.0, ry - n * 0.04, rx + n * 0.26, ry + n * 0.20], 180, 360, fill=(170, 170, 180, 255))
            d.ellipse([rx + n * 0.06, ry - n * 0.16, rx + n * 0.20, ry - n * 0.02], fill=c)
            d.line([(rx - n * 0.30, ry + n * 0.56), (rx + n * 0.90, ry + n * 0.16)], fill=(130, 100, 60, 255), width=n // 20)
            d.polygon([(rx + n * 0.90, ry + n * 0.16), (rx + n * 0.80, ry + n * 0.14), (rx + n * 0.84, ry + n * 0.24)], fill=(225, 225, 232, 255))
        elif kind == "mongol":   # Mongol horse archer: round fur-brimmed hat with point, recurve bow, deel coat
            d.ellipse([rx - n * 0.03, ry + n * 0.02, rx + n * 0.29, ry + n * 0.14], fill=(150, 110, 70, 255))
            d.polygon([(rx + n * 0.04, ry + n * 0.06), (rx + n * 0.22, ry + n * 0.06), (rx + n * 0.13, ry - n * 0.14)], fill=c)
            d.arc([rx + n * 0.20, ry + n * 0.02, rx + n * 0.58, ry + n * 0.66], 270, 90, fill=(60, 40, 20, 255), width=n // 18)
            d.line([(rx + n * 0.39, ry + n * 0.04), (rx + n * 0.39, ry + n * 0.64)], fill=(230, 230, 230, 255), width=n // 60)
        elif kind == "knight":   # crusader knight: flat-top great helm, white surcoat with red cross, lance + pennant
            d.rectangle([rx + n * 0.02, ry + n * 0.0, rx + n * 0.24, ry + n * 0.24], fill=(170, 170, 180, 255))
            d.line([(rx + n * 0.04, ry + n * 0.10), (rx + n * 0.22, ry + n * 0.10)], fill=(40, 40, 45, 255), width=n // 40)
            d.rounded_rectangle([rx - n * 0.01, ry + n * 0.26, rx + n * 0.27, ry + n * 0.62], radius=n * 0.06, fill=(245, 245, 245, 255), outline=dk, width=n // 40)
            d.line([(rx + n * 0.13, ry + n * 0.30), (rx + n * 0.13, ry + n * 0.58)], fill=c, width=n // 18)
            d.line([(rx + n * 0.03, ry + n * 0.40), (rx + n * 0.23, ry + n * 0.40)], fill=c, width=n // 18)
            d.line([(rx - n * 0.30, ry + n * 0.56), (rx + n * 0.90, ry + n * 0.16)], fill=(130, 100, 60, 255), width=n // 20)
            d.polygon([(rx + n * 0.66, ry + n * 0.24), (rx + n * 0.80, ry + n * 0.10), (rx + n * 0.74, ry + n * 0.30)], fill=c)
        elif kind == "arab":     # Arab rider: turban + spear + banner
            d.ellipse([rx - n * 0.01, ry - n * 0.04, rx + n * 0.27, ry + n * 0.14], fill=(245, 242, 232, 255))
            d.line([(rx + n * 0.40, ry - n * 0.40), (rx + n * 0.40, ry + n * 0.70)], fill=(130, 100, 60, 255), width=n // 22)
            d.polygon([(rx + n * 0.40, ry - n * 0.40), (rx + n * 0.70, ry - n * 0.32), (rx + n * 0.40, ry - n * 0.20)], fill=c)
        elif kind == "timurid":  # Timurid lancer: spiked helmet with mail neck guard, lance with horse-tail standard
            d.chord([rx + n * 0.0, ry - n * 0.02, rx + n * 0.26, ry + n * 0.22], 180, 360, fill=(170, 170, 180, 255))
            d.line([(rx + n * 0.13, ry - n * 0.02), (rx + n * 0.13, ry - n * 0.16)], fill=(170, 170, 180, 255), width=n // 30)
            d.rectangle([rx - n * 0.01, ry + n * 0.10, rx + n * 0.04, ry + n * 0.26], fill=(130, 130, 140, 255))
            d.line([(rx + n * 0.40, ry - n * 0.44), (rx + n * 0.40, ry + n * 0.70)], fill=(130, 100, 60, 255), width=n // 22)
            d.polygon([(rx + n * 0.36, ry - n * 0.44), (rx + n * 0.44, ry - n * 0.44), (rx + n * 0.40, ry - n * 0.56)], fill=(225, 225, 232, 255))
            for k in range(5): d.line([(rx + n * 0.40, ry - n * 0.36), (rx + n * (0.30 - k * 0.03), ry - n * (0.10 - k * 0.02))], fill=(60, 45, 35, 255), width=n // 40)
        elif kind == "serb":     # Serbian heavy horseman: rounded helmet with plume, surcoat in banner colour, lance + pennant
            d.chord([rx + n * 0.0, ry - n * 0.02, rx + n * 0.26, ry + n * 0.24], 180, 360, fill=(175, 175, 185, 255))
            d.ellipse([rx + n * 0.08, ry - n * 0.14, rx + n * 0.20, ry - n * 0.0], fill=(240, 240, 240, 255))
            d.line([(rx - n * 0.30, ry + n * 0.56), (rx + n * 0.90, ry + n * 0.16)], fill=(130, 100, 60, 255), width=n // 20)
            d.polygon([(rx + n * 0.66, ry + n * 0.24), (rx + n * 0.80, ry + n * 0.10), (rx + n * 0.74, ry + n * 0.30)], fill=(240, 240, 240, 255))
        elif kind == "xianbei":  # steppe rider: fur hat + round shield + bow on back
            d.ellipse([rx - n * 0.02, ry - n * 0.02, rx + n * 0.28, ry + n * 0.14], fill=(90, 70, 50, 255))
            d.ellipse([rx - n * 0.14, ry + n * 0.30, rx + n * 0.12, ry + n * 0.56], fill=dk, outline=c, width=n // 26)
            d.arc([rx + n * 0.16, ry + n * 0.10, rx + n * 0.44, ry + n * 0.58], 270, 90, fill=(120, 80, 30, 255), width=n // 24)
    im = im.resize((int(W_ / S3), int(H_ / S3)), Image.LANCZOS)
    return _sol_finish(im.crop(im.getbbox()))

def _sol_finish(im):
    pad = 6; out = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    a = Image.new("L", out.size, 0); a.paste(im.getchannel("A"), (pad, pad))
    ol = Image.new("RGBA", out.size, (255, 255, 255, 255)); ol.putalpha(a.filter(ImageFilter.MaxFilter(3)).point(lambda v: int(v * 0.85)))
    out.alpha_composite(ol); out.alpha_composite(im, (pad, pad))
    return out

_cache = {}
def get_icon(name, size):
    k = (name, size)
    if k not in _cache: _cache[k] = ICONS[name](size)
    return _cache[k]
SHIP_STYLE = None   # None/"classic" = old sail boat; "junk", "carrack", "galleon", "steamer", "modern" (see fx_eras)
def set_year(y):
    """Call from an episode config: picks the era-correct ship automatically."""
    global SHIP_STYLE
    import fx_eras as FE; SHIP_STYLE = FE.ship_for_year(y)
def get_ship(col, size, flip, style=None):
    style = style or SHIP_STYLE or "classic"
    k = ("ship", col, size, flip, style)
    if k not in _cache:
        if style == "classic":
            import fx_people as FP; im = FP.ship(col, size)
        elif style == "modern":
            import fx_modern as FM; im = FM.sprite("warship", int(size * 1.3))
        else:
            import fx_eras as FE; im = FE.ship(style, col, size)
        _cache[k] = im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im
    return _cache[k]
def get_soldier(col, size, flip, kind="legion"):
    k = ("sol", col, size, flip, kind)
    if k not in _cache:
        im = soldier(col, size, kind); _cache[k] = im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im
    return _cache[k]

def cl(x, a=0.0, b=1.0): return max(a, min(b, x))
def pr(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eio(x): x = cl(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def eback(x, s=2.0):
    x = cl(x); c3 = s + 1; return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2

def zscale(vw): return cl((2400 / vw) ** 0.45, 0.8, 1.35)

def paste(fr, im, cx, cy, scale=1.0, alpha=1.0):
    if alpha <= 0.01: return
    if abs(scale - 1) > 0.01:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if alpha < 0.999:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    fr.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)

def path_point(pts, k):
    seg = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    tot = sum(seg) or 1; target = tot * cl(k); acc = 0
    for (a, b), L in zip(zip(pts, pts[1:]), seg):
        if acc + L >= target:
            f = (target - acc) / L if L else 0
            return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), math.atan2(b[1] - a[1], b[0] - a[0]), target
        acc += L
    a, b = pts[-2], pts[-1]
    return pts[-1], math.atan2(b[1] - a[1], b[0] - a[0]), tot

def draw_icon(fr, S, vw, t, ev):
    t0, t1 = ev["t0"], ev["t1"]
    if t < t0 or t > t1 + 0.35: return
    k = eback(pr(t, t0, t0 + 0.4), 2.4); out = pr(t, t1, t1 + 0.35)
    x, y = S(*ev["pos"])
    sc = (min(k, 1.2) if k < 1.2 else 1.0) * zscale(vw) * ev.get("scale", 1.0) * 1.55
    bob = math.sin((t - t0) * 3.2) * 5
    for j in range(ev.get("count", 1)):
        dx = (j - (ev.get("count", 1) - 1) / 2) * 80 * sc
        paste(fr, get_icon(ev["icon"], 130), x + dx, y + bob - 20 * (1 - min(k, 1)), scale=sc * (1 - 0.3 * out), alpha=min(1, k * 2) * (1 - out))

_LAND = None
def is_water(lon, lat):
    global _LAND
    if _LAND is None:
        import numpy as _np, geo as _g
        _LAND = (_np.asarray(Image.open("/home/claude/shortgen/hd_land.png").convert("L")) > 110, _g.P)
    m, P = _LAND
    x, y = P(lon, lat); x = int(min(max(x, 0), m.shape[1] - 1)); y = int(min(max(y, 0), m.shape[0] - 1))
    return not m[y, x]

def geo_at(pts, gpts, target):
    acc = 0
    for (a, b), (ga, gb) in zip(zip(pts, pts[1:]), zip(gpts, gpts[1:])):
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        if acc + L >= target or b is pts[-1]:
            f = cl((target - acc) / L) if L else 0
            return ga[0] + (gb[0] - ga[0]) * f, ga[1] + (gb[1] - ga[1]) * f
        acc += L
    return gpts[-1]

_pc = {}
def draw_person(fr, S, vw, t, ev):
    t0, t1 = ev["t0"], ev["t1"]
    if t < t0 or t > t1 + 0.4: return
    import fx_people as FP
    key = (ev["who"], ev.get("name"), ev.get("sub"))
    if key not in _pc:
        _pc[key] = (FP.get(ev["who"], 215), FP.name_plate(ev.get("name", ev["who"].upper()), ev.get("sub"), 42))
    med, plate = _pc[key]
    k = eback(pr(t, t0, t0 + 0.45), 1.8); out = pr(t, t1, t1 + 0.4)
    if "screen" in ev: x, y = ev["screen"]
    else:
        x, y = S(*ev["pos"]); dx, dy = ev.get("off", (0, -230)); x += dx; y += dy
        x = min(max(x, 170), 910); y = min(max(y, 470), 1380)
    sc = max(0.01, k) * (1 - 0.25 * out); a = min(1, pr(t, t0, t0 + 0.25)) * (1 - out)
    bob = math.sin((t - t0) * 2.2) * 4
    paste(fr, med, x, y + bob, scale=sc, alpha=a)
    paste(fr, plate, x, y + bob + med.height * 0.5 * sc + plate.height * 0.42, scale=min(1, sc), alpha=a * pr(t, t0 + 0.2, t0 + 0.5))

def draw_march(fr, S, vw, t, ev):
    t0, t1 = ev["t0"], ev["t1"]; until = ev.get("until", t1 + 1.2)
    if t < t0 or t > until: return
    fade = 1 - pr(t, until - 0.4, until)
    pts = [S(*p) for p in ev["path"]]
    k = eio(pr(t, t0, t1))
    (hx, hy), ang, dist = path_point(pts, k)
    col = ev["color"]
    # arrow along travelled path
    seg_pts = [pts[0]]
    acc = 0
    for a, b in zip(pts, pts[1:]):
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        if acc + L < dist: seg_pts.append(b); acc += L
        else: break
    seg_pts.append((hx, hy))
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    wid = int(34 * zscale(vw))
    d.line(seg_pts, fill=(0, 0, 0, int(120 * fade)), width=wid + 10, joint="curve")
    d.line(seg_pts, fill=col + (int(235 * fade),), width=wid, joint="curve")
    L = wid * 2.2
    tip = (hx + math.cos(ang) * L * 0.9, hy + math.sin(ang) * L * 0.9)
    l1 = (hx + math.cos(ang + 2.4) * L * 0.8, hy + math.sin(ang + 2.4) * L * 0.8)
    l2 = (hx + math.cos(ang - 2.4) * L * 0.8, hy + math.sin(ang - 2.4) * L * 0.8)
    d.polygon([tip, l1, l2], fill=col + (int(250 * fade),), outline=(0, 0, 0, int(160 * fade)))
    fr.paste(lay, (0, 0), lay)
    # soldiers trailing behind the head
    kind = ev.get("kind", "legion")
    import fx_eras as FE
    foot = kind in ("legion", "han", "rebel", "goth", "viking", "frank", "byzantine", "aztec", "rus", "redturban") + FE.FOOT2
    n = ev.get("soldiers", 9 if foot else 6); sz = int((44 if foot else 50) * zscale(vw))
    flip = math.cos(ang) < 0
    rnd = random.Random(int(t0 * 100))
    offs = [(rnd.uniform(-1, 1), rnd.uniform(0, 1)) for _ in range(n)]
    for i in range(n):
        per = 3 if foot else 2
        back = (i // per) * sz * (1.1 if foot else 1.5) + 14
        side = ((i % per) - (per - 1) / 2) * sz * (0.9 if foot else 1.1) + offs[i][0] * 4
        if dist - back < 0: continue
        (sx, sy), a2, _ = path_point(pts, (dist - back) / max(1, sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:]))))
        px, py = sx - math.sin(a2) * side, sy + math.cos(a2) * side
        if ev.get("ships", True) and is_water(*geo_at(pts, ev["path"], dist - back)):
            if i % per: continue
            bob = math.sin((t - t0) * 3 + i) * 3
            paste(fr, get_ship(col, int(sz * 1.25), flip, ev.get("ship")), sx, sy + bob - sz * 0.5, alpha=fade); continue
        walk = abs(math.sin((t - t0) * (9 if foot else 12) + i)) * (4 if foot else 6) if k < 1 else 0
        paste(fr, get_soldier(col, sz, flip, kind), px, py - walk - sz * 0.4, alpha=fade)

def draw_boom(fr, S, vw, t, ev):
    t0 = ev["t0"]; dur = ev.get("dur", 1.4)
    if t < t0 or t > t0 + dur + ev.get("hold", 1.0): return
    lt = t - t0; x, y = S(*ev["pos"]); z = zscale(vw) * ev.get("scale", 1.0) * 1.5
    lay = Image.new("RGBA", fr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    rnd = random.Random(int(t0 * 1000))
    if lt < dur:
        p = lt / dur
        R = (40 + 170 * (1 - (1 - p) ** 3)) * z
        d.ellipse([x - R, y - R, x + R, y + R], outline=(255, 230, 160, int(220 * (1 - p))), width=max(2, int(10 * (1 - p) * z)))
        for i in range(16):  # smoke
            a = rnd.uniform(0, 2 * math.pi); sp = rnd.uniform(30, 90) * z
            rr = (18 + 50 * p) * z * rnd.uniform(0.7, 1.3)
            cx, cy = x + math.cos(a) * sp * p, y + math.sin(a) * sp * p - 40 * p * z
            g = int(70 + 40 * rnd.random())
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(g, g - 4, g - 8, int(170 * (1 - p) ** 1.2)))
        fb = max(0, 1 - p * 2.2)
        if fb > 0:  # fireball
            for rr_, colr in ((70, (255, 120, 30)), (48, (255, 190, 60)), (26, (255, 250, 210))):
                r2 = rr_ * z * (0.7 + 0.6 * p)
                d.ellipse([x - r2, y - r2, x + r2, y + r2], fill=colr + (int(255 * fb),))
        for i in range(22):  # sparks
            a = rnd.uniform(0, 2 * math.pi); sp = rnd.uniform(80, 240) * z
            px, py = x + math.cos(a) * sp * p, y + math.sin(a) * sp * p + 120 * p * p * z
            r3 = 4 * z * (1 - p)
            d.ellipse([px - r3, py - r3, px + r3, py + r3], fill=(255, 210, 90, int(255 * (1 - p))))
        lay2 = lay.filter(ImageFilter.GaussianBlur(2))
        fr.paste(lay2, (0, 0), lay2)
    if ev.get("swords", True) and lt > 0.15:
        k = eback(pr(lt, 0.15, 0.5), 2.6); out = pr(lt, dur + ev.get("hold", 1.0) - 0.35, dur + ev.get("hold", 1.0))
        shake = math.sin(lt * 40) * 6 * max(0, 1 - lt / 0.6)
        paste(fr, get_icon("swords", 120), x + shake, y - 6, scale=(min(k, 1.2) if k < 1.2 else 1.0) * zscale(vw) * 1.35, alpha=min(1, k * 2) * (1 - out))

def draw_all(fr, S, vw, t, events):
    import fx_modern as FM
    for ev in events:
        if ev["type"] == "cities": FM.draw_cities(fr, S, vw, t, ev, zscale)
    for ev in events:
        if ev["type"] == "glow": FM.draw_glow(fr, S, vw, t, ev)
    for ev in events:
        if ev["type"] == "front": FM.draw_front(fr, S, vw, t, ev, zscale)
    for ev in events:
        if ev["type"] == "vehicle": FM.draw_vehicle(fr, S, vw, t, ev, zscale)
    for ev in events:
        if ev["type"] == "march": draw_march(fr, S, vw, t, ev)
    for ev in events:
        if ev["type"] == "boom": draw_boom(fr, S, vw, t, ev)
    for ev in events:
        if ev["type"] == "icon": draw_icon(fr, S, vw, t, ev)

def draw_people(fr, S, vw, t, events):
    for ev in events:
        if ev["type"] == "person": draw_person(fr, S, vw, t, ev)

if __name__ == "__main__":
    sheet = Image.new("RGBA", (1600, 420), (30, 60, 90, 255))
    for i, k in enumerate(ICONS):
        im = get_icon(k, 130); sheet.alpha_composite(im, (20 + (i % 8) * 195, 20 + (i // 8) * 200))
    for j, (kd, col) in enumerate((("legion", (196, 52, 62)), ("parthian", (214, 140, 52)), ("kushan", (150, 110, 200)), ("xianbei", (64, 168, 150)), ("han", (70, 110, 200)), ("rebel", (230, 200, 40)))):
        sheet.alpha_composite(get_soldier(col, 70, False, kd), (500 + j * 180, 230))
    sheet.convert("RGB").save("/tmp/claude-0/-home-claude/3fbdae20-9fc1-5a7b-89aa-2250f8cbf832/scratchpad/icons.png")
