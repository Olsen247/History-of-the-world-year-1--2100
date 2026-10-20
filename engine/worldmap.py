"""Render a stylised world map for 1 AD (Natural Earth I projection)."""
import math, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import world_data as WD0
WD = WD0

SERIF_B = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
SANS_B = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
SANS_M = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
LAT_N, LAT_S = 80, -56

def ne(lon, lat):
    l, p = math.radians(lon), math.radians(lat)
    p2 = p * p; p4 = p2 * p2
    x = l * (0.8707 - 0.131979 * p2 + p4 * (-0.013791 + p4 * (0.003971 * p2 - 0.001529 * p4)))
    y = p * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4)))
    return x, y

XMAX = ne(180, 0)[0]
YN, YS = ne(0, LAT_N)[1], ne(0, LAT_S)[1]

class Proj:
    def __init__(self, width):
        self.W = width; self.s = width / (2 * XMAX)
        self.H = int((YN - YS) * self.s)
    def __call__(self, lon, lat):
        x, y = ne(lon, lat)
        return (x + XMAX) * self.s, (YN - y) * self.s
    def poly(self, pts):
        return [self(lo, la) for lo, la in pts]

def masks(width, ss=2):
    P = Proj(width * ss)
    land = Image.new("L", (P.W, P.H), 0); d = ImageDraw.Draw(land)
    for pts in WD.LAND.values(): d.polygon(P.poly(pts), fill=255)
    for pts in WD.WATER.values(): d.polygon(P.poly(pts), fill=0)
    emp = []
    for name, col, polys, lab in WD.EMPIRES:
        m = Image.new("L", (P.W, P.H), 0); dm = ImageDraw.Draw(m)
        for pts in polys: dm.polygon(P.poly(pts), fill=255)
        m = Image.fromarray(np.minimum(np.array(m), np.array(land)))
        emp.append(m.resize((width, P.H // ss), Image.LANCZOS))
    return land.resize((width, P.H // ss), Image.LANCZOS), emp

def render(width=3600, labels=True, title=True, ss=2, data=None, title_text="THE WORLD IN YEAR 1", pop_text="World population ≈ 200–300 million"):
    global WD
    if data is not None: WD = data
    P = Proj(width)
    land, emp = masks(width, ss)
    W, H = land.size
    y = np.linspace(0, 1, H)[:, None]
    ocean = np.zeros((H, W, 3))
    ocean[:] = np.array([16, 44, 70]) * (1 - y[..., None]) + np.array([10, 28, 48]) * y[..., None]
    img = Image.fromarray(ocean.astype(np.uint8), "RGB").convert("RGBA")
    d = ImageDraw.Draw(img, "RGBA")
    lw = max(1, width // 1800)
    for lon in range(-180, 181, 30):
        d.line(P.poly([(lon, la) for la in range(LAT_S, LAT_N + 1, 2)]), fill=(120, 170, 220, 28), width=lw)
    for lat in range(-60, 81, 20):
        if LAT_S <= lat <= LAT_N:
            d.line(P.poly([(lo, lat) for lo in range(-180, 181, 3)]), fill=(120, 170, 220, 28), width=lw)
    # land with subtle texture
    rng = np.random.default_rng(3)
    noise = rng.normal(0, 1, (H // 4 + 1, W // 4 + 1))
    noise = np.array(Image.fromarray(((noise + 3) * 40).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(float)
    base = np.array([206, 190, 152], float)[None, None, :] + (noise[..., None] - 120) * 0.06
    land_img = Image.fromarray(base.clip(0, 255).astype(np.uint8), "RGB").convert("RGBA")
    # coastal glow in the sea
    glow = land.filter(ImageFilter.GaussianBlur(width / 300))
    gl = Image.new("RGBA", (W, H), (90, 150, 190, 255)); gl.putalpha(glow.point(lambda v: int(v * 0.35)))
    img.alpha_composite(gl)
    img.paste(land_img, (0, 0), land)
    # empires
    for (name, col, polys, lab), m in zip(WD.EMPIRES, emp):
        fill = Image.new("RGBA", (W, H), col + (255,)); fill.putalpha(m.point(lambda v: int(v * 0.82)))
        img.alpha_composite(fill)
        edge = m.filter(ImageFilter.MaxFilter(3)); inner = m.filter(ImageFilter.MinFilter(max(3, (width // 900) * 2 + 1)))
        e = Image.fromarray(np.clip(np.array(edge).astype(int) - np.array(inner).astype(int), 0, 255).astype(np.uint8))
        dark = tuple(int(c * 0.55) for c in col)
        ed = Image.new("RGBA", (W, H), dark + (255,)); ed.putalpha(e)
        img.alpha_composite(ed)
    # coastline
    edge = land.filter(ImageFilter.MaxFilter(3)); inner = land.filter(ImageFilter.MinFilter(3))
    e = Image.fromarray(np.clip(np.array(edge).astype(int) - np.array(inner).astype(int), 0, 255).astype(np.uint8))
    co = Image.new("RGBA", (W, H), (40, 34, 26, 255)); co.putalpha(e.point(lambda v: int(v * 0.6)))
    img.alpha_composite(co)
    if labels: draw_labels(img, P, width)
    if title: draw_title(img, width, title_text, pop_text)
    return img

def text_centered(d, xy, s, font, fill, stroke, scol, spacing=0):
    if spacing:
        widths = [font.getlength(c) for c in s]; total = sum(widths) + spacing * (len(s) - 1)
        x = xy[0] - total / 2
        for c, w in zip(s, widths):
            d.text((x, xy[1]), c, font=font, fill=fill, anchor="lm", stroke_width=stroke, stroke_fill=scol); x += w + spacing
    else:
        d.text(xy, s, font=font, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=scol)

MID = {"KUSHAN EMPIRE", "PARTHIAN EMPIRE"}
LABEL_OVERRIDE = {"KUSHAN EMPIRE": "KUSHAN\nEMPIRE", "PARTHIAN EMPIRE": "PARTHIAN\nEMPIRE", "WESTERN SATRAPS": "WESTERN\nSATRAPS"}
SMALL = {"YUEZHI", "TAMIL KINGDOMS", "KUSH", "NABATAEANS", "KOREA", "SATAVAHANA", "INDO-SCYTHIANS", "AKSUM", "WESTERN SATRAPS"}

def draw_labels(img, P, width):
    d = ImageDraw.Draw(img, "RGBA"); u = width / 3600
    for name, (lo, la) in WD.OCEANS:
        text_centered(d, P(lo, la), name, ImageFont.truetype(SERIF_I, int(46 * u)), (150, 190, 225, 170), 0, None, spacing=int(10 * u))
    for name, (lo, la) in WD.CULTURES:
        f = ImageFont.truetype(SERIF_I, int(30 * u))
        on_sea = name in ("Polynesian voyagers", "Celtic Britons")
        if on_sea:
            text_centered(d, P(lo, la), name, f, (200, 222, 240, 235), 0, None)
        else:
            text_centered(d, P(lo, la), name, f, (60, 46, 32, 255), max(2, int(3 * u)), (224, 210, 176, 230))
    for name, col, polys, (lo, la) in WD.EMPIRES:
        sz = 34 if name in SMALL else (46 if name in MID else 58)
        if name == "ROMAN EMPIRE": sz = 64
        disp = LABEL_OVERRIDE.get(name, name)
        if "\n" in disp: sz = int(sz * 0.8)
        f = ImageFont.truetype(SERIF_B, int(sz * u))
        lines = disp.split("\n"); x, y = P(lo, la)
        for k, ln in enumerate(lines):
            yy = y + (k - (len(lines) - 1) / 2) * sz * u * 1.05
            text_centered(d, (x, yy), ln, f, (255, 255, 255, 255), max(2, int(4 * u)), tuple(int(c * 0.4) for c in col), spacing=int(3 * u))

def draw_title(img, width, title_text="THE WORLD IN YEAR 1", pop_text="World population ≈ 200–300 million"):
    d = ImageDraw.Draw(img, "RGBA"); u = width / 3600
    W, H = img.size
    d.rounded_rectangle([60 * u, H - 250 * u, 1050 * u, H - 60 * u], radius=24 * u, fill=(8, 18, 32, 215), outline=(255, 205, 80, 255), width=int(3 * u))
    d.text((100 * u, H - 210 * u), title_text, font=ImageFont.truetype(SANS_B, int(64 * u)), fill=(255, 255, 255))
    d.text((100 * u, H - 125 * u), pop_text, font=ImageFont.truetype(SANS_M, int(34 * u)), fill=(255, 205, 80))
    d.text((W - 60 * u, H - 40 * u), "Borders approximate · stylised map", font=ImageFont.truetype(SANS_M, int(24 * u)),
           fill=(160, 180, 200, 200), anchor="rd")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "world_1ad.png"
    im = render(3600)
    im.convert("RGB").save(out, quality=95)
    print(im.size)
