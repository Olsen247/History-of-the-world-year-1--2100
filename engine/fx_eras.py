"""Era upgrades: ships and soldiers that change as the series moves towards modern times.

Ships (used automatically when a march crosses water):
    galley/longship (default, up to ~1400) -> junk (Chinese fleets) -> carrack (1400-1550) -> galleon (1550-1830)
    -> steamer (1830-1910) -> modern warship (fx_modern, 1910+)
Set per march with ev["ship"]="carrack", or for the whole episode with FX.SHIP_STYLE = "galleon" (or FX.set_year(1492)).

New foot soldiers (march kind=...):
    janissary   – Ottoman, tall white börk hat, musket/halberd           (1400-1800)
    conquistador – Spanish, morion helmet, steel breastplate, sword      (1490-1600)
    inca        – Inca warrior, tunic with checker band, sling/mace      (1400-1540)
    musketeer   – broad-brimmed hat, matchlock musket                   (1600-1700)
    line        – tricorne, coat in the nation's colour, musket+bayonet (1700-1800)
    napoleonic  – shako, coat in nation's colour, white cross-belts     (1795-1870)
    rifleman    – kepi / soft cap, rifle (American Civil War, colonial) (1850-1900)
    ww1         – steel helmet + rifle (only if a march is used instead of a front, 1914-1918)
"""
import math
from PIL import Image, ImageDraw, ImageFilter

S = 3
FOOT2 = ("landsknecht", "swede", "hussar", "qizilbash", "visayan", "samurai", "strelets", "maori", "dutch", "longbow", "janissary", "conquistador", "inca", "musketeer", "line", "napoleonic", "rifleman", "ww1", "bannerman", "mughal", "sepoy", "minuteman", "carolean", "grenadier", "sansculotte", "haitian")

def ship_for_year(y):
    if y is None or y < 1400: return "classic"
    if y < 1550: return "carrack"
    if y < 1830: return "galleon"
    if y < 1910: return "steamer"
    return "modern"

def _outline(im, pad=5):
    out = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    a = Image.new("L", out.size, 0); a.paste(im.getchannel("A"), (pad, pad))
    ol = Image.new("RGBA", out.size, (255, 255, 255, 255)); ol.putalpha(a.filter(ImageFilter.MaxFilter(3)).point(lambda v: int(v * 0.85)))
    out.alpha_composite(ol); out.alpha_composite(im, (pad, pad)); return out

def ship(style, col, size=60):
    """Side view, bow to the right."""
    n = size * S; W, H = int(n * 1.5), int(n * 1.6)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = col + (255,); dk = (55, 34, 18, 255); wood = (115, 72, 38, 255); sail = (238, 230, 210, 255); lw = int(n * .03)
    base = n * 1.3
    if style == "junk":   # Chinese treasure ship: high stern, battened red sails
        d.polygon([(n * .05, base - n * .30), (n * 1.40, base - n * .20), (n * 1.20, base + n * .08), (n * .22, base + n * .08)], fill=(120, 60, 30, 255), outline=dk, width=lw)
        d.rectangle([n * .05, base - n * .42, n * .30, base - n * .26], fill=(140, 70, 35, 255), outline=dk, width=lw)
        for x, h in ((.45, .80), (.80, .92), (1.12, .66)):
            d.line([(n * x, base - n * .22), (n * x, base - n * h)], fill=dk, width=int(n * .04))
            d.polygon([(n * (x - .17), base - n * (h - .04)), (n * (x + .13), base - n * (h - .04)), (n * (x + .15), base - n * .30), (n * (x - .19), base - n * .30)], fill=(190, 60, 45, 255), outline=dk, width=lw)
            for k in range(1, 5):
                yy = base - n * (h - .04) + (n * (h - .34)) * k / 5; d.line([(n * (x - .18), yy), (n * (x + .14), yy)], fill=dk, width=max(1, lw // 2))
    elif style in ("carrack", "galleon"):
        hull = (100, 62, 32, 255)
        d.polygon([(n * .02, base - n * .40), (n * .30, base - n * .26), (n * 1.10, base - n * .26), (n * 1.42, base - n * .40),
                   (n * 1.22, base + n * .06), (n * .22, base + n * .06)], fill=hull, outline=dk, width=lw)
        d.line([(n * .22, base - n * .10), (n * 1.24, base - n * .10)], fill=c if style == "galleon" else (200, 170, 90, 255), width=int(n * .05))
        if style == "galleon":
            for x in (.42, .62, .82, 1.02): d.rectangle([n * x, base - n * .06, n * (x + .05), base - n * .01], fill=(20, 15, 10, 255))
        d.line([(n * 1.30, base - n * .38), (n * 1.50, base - n * .58)], fill=dk, width=lw)   # bowsprit
        masts = ((.40, .78), (.78, 1.0), (1.10, .72)) if style == "galleon" else ((.42, .70), (.80, .92), (1.12, .62))
        for i, (x, h) in enumerate(masts):
            d.line([(n * x, base - n * .26), (n * x, base - n * h - n * .06)], fill=dk, width=int(n * .035))
            if style == "carrack" and i == 2:   # lateen mizzen
                d.polygon([(n * (x - .16), base - n * .30), (n * (x + .06), base - n * h), (n * (x + .10), base - n * .30)], fill=sail, outline=dk, width=lw)
                continue
            for top, bot, wsc in ((h, h * .62, .8), (h * .58, .32, 1.0)) if style == "galleon" else ((h, .32, 1.0),):
                wd = .17 * wsc
                d.chord([n * (x - wd), base - n * top, n * (x + wd), base - n * bot + n * .10], 180, 360, fill=sail, outline=dk, width=lw)
                d.rectangle([n * (x - wd), base - n * top + n * .0, n * (x + wd), base - n * bot], fill=sail, outline=dk, width=lw)
        if style == "carrack": d.line([(n * .80, base - n * .66), (n * .80, base - n * .44)], fill=(200, 40, 40, 255), width=int(n * .06))  # cross on sail
        d.polygon([(n * x0, base - n * h0) for x0, h0 in ((.80, 1.06), (.96, 1.02), (.80, .98))], fill=c)   # pennant
    elif style == "galley":   # Mediterranean war galley (Lepanto): long low hull, banks of oars, lateen sails
        d.polygon([(n * .00, base - n * .30), (n * 1.46, base - n * .26), (n * 1.30, base + n * .02), (n * .12, base + n * .02)], fill=(105, 66, 34, 255), outline=dk, width=lw)
        d.line([(n * .12, base - n * .14), (n * 1.32, base - n * .14)], fill=c, width=int(n * .05))
        for k in range(11): x = n * (.18 + k * .10); d.line([(x, base - n * .04), (x - n * .10, base + n * .20)], fill=dk, width=max(1, lw))
        for x, h in ((.55, .95), (1.00, .78)):
            d.line([(n * x, base - n * .26), (n * x, base - n * h)], fill=dk, width=int(n * .035))
            d.polygon([(n * (x - .30), base - n * .32), (n * (x + .22), base - n * h), (n * (x + .14), base - n * .30)], fill=sail, outline=dk, width=lw)
        d.polygon([(n * 1.40, base - n * .27), (n * 1.62, base - n * .22), (n * 1.40, base - n * .18)], fill=dk)
    elif style == "waka":     # Maori waka taua (war canoe): long dark hull, carved prow and stern, paddlers
        d.polygon([(n * .05, base - n * .20), (n * 1.40, base - n * .20), (n * 1.25, base + n * .04), (n * .18, base + n * .04)], fill=(90, 45, 25, 255), outline=dk, width=lw)
        d.polygon([(n * 1.36, base - n * .20), (n * 1.52, base - n * .42), (n * 1.46, base - n * .16)], fill=(150, 40, 30, 255), outline=dk)
        d.polygon([(n * .08, base - n * .20), (n * .00, base - n * .70), (n * .14, base - n * .22)], fill=(150, 40, 30, 255), outline=dk)
        for k in range(6):
            x = n * (.30 + k * .17)
            d.ellipse([x - n * .05, base - n * .44, x + n * .05, base - n * .34], fill=(60, 40, 30, 255))
            d.line([(x, base - n * .34), (x, base - n * .20)], fill=(60, 40, 30, 255), width=int(n * .05))
            d.line([(x + n * .03, base - n * .30), (x - n * .08, base + n * .14)], fill=(150, 110, 60, 255), width=max(1, lw))
    elif style == "steamer":
        d.polygon([(n * .04, base - n * .28), (n * 1.42, base - n * .28), (n * 1.24, base + n * .06), (n * .16, base + n * .06)], fill=(40, 40, 46, 255), outline=(15, 15, 18, 255), width=lw)
        d.line([(n * .10, base - n * .06), (n * 1.32, base - n * .06)], fill=(170, 40, 40, 255), width=int(n * .05))
        d.rectangle([n * .40, base - n * .46, n * 1.02, base - n * .28], fill=(235, 232, 222, 255), outline=dk, width=lw)
        for x in (.56, .84):
            d.rectangle([n * (x - .05), base - n * .80, n * (x + .05), base - n * .46], fill=c, outline=dk, width=lw)
            d.rectangle([n * (x - .05), base - n * .80, n * (x + .05), base - n * .72], fill=(25, 25, 25, 255))
        for k in range(5): d.ellipse([n * (.06 + k * .10), base - n * (1.0 + k * .07), n * (.20 + k * .12), base - n * (.86 + k * .07)], fill=(200, 200, 205, 200 - k * 30))
        d.line([(n * .25, base - n * .28), (n * .25, base - n * .70)], fill=dk, width=lw); d.line([(n * 1.18, base - n * .28), (n * 1.18, base - n * .62)], fill=dk, width=lw)
    im = im.resize((int(W / S), int(H / S)), Image.LANCZOS)
    return _outline(im.crop(im.getbbox()))

# ---------------- soldiers ----------------
class _Shift:
    """ImageDraw wrapper that moves every y coordinate down (so tall hats are not clipped)."""
    def __init__(self, d, off): self.d, self.off = d, off
    def _xy(self, xy):
        if xy and isinstance(xy[0], (tuple, list)): return [(x, y + self.off) for x, y in xy]
        return [v + (self.off if i % 2 else 0) for i, v in enumerate(xy)]
    def __getattr__(self, name):
        f = getattr(self.d, name)
        return lambda xy, *a, **k: f(self._xy(xy), *a, **k)

def soldier(col, size=40, kind="line"):
    n = size * S; OFF = n * .35; im = Image.new("RGBA", (int(n * 1.5), int(n * 1.5 + OFF)), (0, 0, 0, 0)); d = _Shift(ImageDraw.Draw(im), OFF)
    c = col + (255,); dk = tuple(int(v * .5) for v in col) + (255,); ox = n * .25
    skin = {"maori": (165, 112, 78, 255), "inca": (170, 115, 80, 255), "janissary": (205, 160, 120, 255), "visayan": (160, 110, 72, 255), "qizilbash": (215, 172, 132, 255), "haitian": (112, 74, 50, 255)}.get(kind, (226, 186, 150, 255))
    trousers = {"line": (235, 230, 215, 255), "napoleonic": (235, 232, 222, 255), "haitian": (235, 232, 222, 255), "sansculotte": (235, 232, 222, 255), "ww1": (95, 100, 80, 255)}.get(kind, (45, 38, 32, 255))
    metal = (185, 188, 196, 255); wood = (110, 72, 40, 255); blk = (25, 22, 20, 255)
    # legs + body
    d.line([(ox + n * .42, n * .96), (ox + n * .36, n * 1.46)], fill=trousers, width=n // 9)
    d.line([(ox + n * .58, n * .96), (ox + n * .64, n * 1.46)], fill=trousers, width=n // 9)
    for x in (.36, .64): d.ellipse([ox + n * (x - .07), n * 1.40, ox + n * (x + .07), n * 1.50], fill=blk)
    coat = c
    if kind == "conquistador": coat = (150, 40, 40, 255)
    if kind == "inca": coat = (200, 150, 60, 255) if col == (0, 0, 0) else c
    if kind == "ww1": coat = c
    if kind == "visayan": coat = (160, 110, 72, 255)
    if kind == "maori": coat = (165, 112, 78, 255)
    long_coat = kind in ("janissary", "line", "napoleonic", "haitian")
    d.rounded_rectangle([ox + n * .34, n * .40, ox + n * .66, n * (1.10 if long_coat else .98)], radius=n * .08, fill=coat, outline=dk, width=n // 30)
    d.ellipse([ox + n * .38, n * .14, ox + n * .62, n * .40], fill=skin)
    # gear per kind
    def musket(bayonet=False, y0=-.02):
        d.line([(ox + n * .80, n * y0), (ox + n * .80, n * 1.22)], fill=wood, width=n // 16)
        d.line([(ox + n * .80, n * y0), (ox + n * .80, n * (y0 + .55))], fill=(70, 70, 76, 255), width=n // 26)
        if bayonet: d.polygon([(ox + n * .78, n * y0), (ox + n * .82, n * y0), (ox + n * .80, n * (y0 - .22))], fill=metal)
    if kind == "janissary":     # tall white börk folding back, red/blue kaftan, halberd-musket
        d.polygon([(ox + n * .38, n * .18), (ox + n * .62, n * .18), (ox + n * .58, -n * .22), (ox + n * .20, -n * .30), (ox + n * .44, -n * .04)], fill=(245, 242, 232, 255), outline=(150, 145, 135, 255))
        d.rectangle([ox + n * .37, n * .14, ox + n * .63, n * .21], fill=(220, 180, 70, 255))
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .44], 0, 180, fill=(40, 30, 25, 255))   # moustache
        d.rectangle([ox + n * .34, n * .66, ox + n * .66, n * .72], fill=(240, 200, 80, 255))
        musket(y0=.02)
    elif kind == "longbow":      # English longbowman: kettle hat, coat with red St George cross, tall longbow + arrow
        d.chord([ox + n * .32, n * .06, ox + n * .68, n * .26], 180, 360, fill=metal)
        d.polygon([(ox + n * .26, n * .18), (ox + n * .74, n * .18), (ox + n * .68, n * .13), (ox + n * .32, n * .13)], fill=metal)
        d.rectangle([ox + n * .36, n * .44, ox + n * .64, n * .94], fill=(240, 238, 230, 255))
        d.line([(ox + n * .50, n * .46), (ox + n * .50, n * .90)], fill=(200, 30, 40, 255), width=n // 16)
        d.line([(ox + n * .38, n * .62), (ox + n * .62, n * .62)], fill=(200, 30, 40, 255), width=n // 16)
        d.arc([ox + n * .62, -n * .10, ox + n * 1.02, n * 1.30], 285, 75, fill=wood, width=n // 18)
        d.line([(ox + n * .90, -n * .06), (ox + n * .90, n * 1.26)], fill=(235, 235, 235, 255), width=max(1, n // 70))
    elif kind == "conquistador":  # morion helmet with crest, steel cuirass, sword up
        d.chord([ox + n * .30, n * .06, ox + n * .70, n * .30], 180, 360, fill=metal)
        d.polygon([(ox + n * .26, n * .20), (ox + n * .74, n * .20), (ox + n * .78, n * .14), (ox + n * .22, n * .14)], fill=metal)
        d.polygon([(ox + n * .40, n * .08), (ox + n * .60, n * .08), (ox + n * .50, -n * .06)], fill=metal)
        d.chord([ox + n * .38, n * .28, ox + n * .62, n * .44], 0, 180, fill=(50, 35, 25, 255))   # beard
        d.rounded_rectangle([ox + n * .35, n * .42, ox + n * .65, n * .78], radius=n * .1, fill=metal, outline=(110, 112, 120, 255), width=n // 40)
        d.line([(ox + n * .80, n * .62), (ox + n * .94, -n * .06)], fill=metal, width=n // 22)
        d.line([(ox + n * .72, n * .60), (ox + n * .88, n * .64)], fill=(200, 170, 70, 255), width=n // 26)
    elif kind == "inca":         # tocapu checker band, feathered headband, sling/mace
        d.rectangle([ox + n * .36, n * .14, ox + n * .64, n * .20], fill=(220, 50, 40, 255))
        for k, fc in enumerate([(240, 200, 60), (230, 60, 50), (40, 150, 90)]):
            d.line([(ox + n * (.44 + k * .06), n * .16), (ox + n * (.40 + k * .08), -n * .04)], fill=fc + (255,), width=n // 20)
        for i in range(4):
            for j in range(2):
                if (i + j) % 2: d.rectangle([ox + n * (.36 + i * .07), n * (.62 + j * .07), ox + n * (.43 + i * .07), n * (.69 + j * .07)], fill=blk)
        d.line([(ox + n * .80, n * .20), (ox + n * .80, n * 1.10)], fill=wood, width=n // 18)
        d.ellipse([ox + n * .72, n * .10, ox + n * .88, n * .26], fill=(180, 160, 70, 255))
        for a in range(0, 360, 60):
            r = math.radians(a); d.polygon([(ox + n * .80 + math.cos(r) * n * .07, n * .18 + math.sin(r) * n * .07), (ox + n * .80 + math.cos(r + .3) * n * .12, n * .18 + math.sin(r + .3) * n * .12), (ox + n * .80 + math.cos(r + .6) * n * .07, n * .18 + math.sin(r + .6) * n * .07)], fill=(180, 160, 70, 255))
    elif kind == "musketeer":    # broad-brimmed hat with feather, sash, matchlock
        d.ellipse([ox + n * .22, n * .10, ox + n * .78, n * .24], fill=blk)
        d.rounded_rectangle([ox + n * .38, n * .00, ox + n * .62, n * .18], radius=n * .05, fill=blk)
        d.line([(ox + n * .58, n * .06), (ox + n * .80, -n * .10)], fill=(240, 240, 240, 255), width=n // 18)
        d.line([(ox + n * .34, n * .44), (ox + n * .66, n * .90)], fill=(240, 220, 120, 255), width=n // 18)
        d.chord([ox + n * .42, n * .30, ox + n * .58, n * .42], 0, 180, fill=(70, 50, 30, 255))
        musket()
    elif kind == "line":         # tricorne, coat in nation colour, white cross-belts
        d.polygon([(ox + n * .28, n * .18), (ox + n * .72, n * .18), (ox + n * .62, n * .04), (ox + n * .50, n * .10), (ox + n * .38, n * .04)], fill=blk, outline=(220, 200, 120, 255))
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        d.line([(ox + n * .65, n * .44), (ox + n * .35, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        musket(bayonet=True)
    elif kind == "napoleonic":   # tall shako with plume, cross-belts
        d.rectangle([ox + n * .38, -n * .06, ox + n * .62, n * .20], fill=blk)
        d.rectangle([ox + n * .36, n * .16, ox + n * .64, n * .21], fill=blk)
        d.ellipse([ox + n * .46, -n * .20, ox + n * .54, -n * .04], fill=(230, 40, 40, 255))
        d.polygon([(ox + n * .46, n * .02), (ox + n * .54, n * .02), (ox + n * .50, n * .10)], fill=(230, 200, 90, 255))
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        d.line([(ox + n * .65, n * .44), (ox + n * .35, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        musket(bayonet=True)
    elif kind == "rifleman":     # kepi, belt, rifle
        d.polygon([(ox + n * .36, n * .20), (ox + n * .64, n * .20), (ox + n * .60, n * .04), (ox + n * .40, n * .06)], fill=dk)
        d.polygon([(ox + n * .58, n * .20), (ox + n * .74, n * .22), (ox + n * .60, n * .24)], fill=blk)
        d.rectangle([ox + n * .34, n * .70, ox + n * .66, n * .76], fill=blk)
        musket(bayonet=True, y0=.04)
    elif kind == "ww1":          # steel helmet, webbing, rifle
        d.chord([ox + n * .30, n * .06, ox + n * .70, n * .34], 180, 360, fill=(95, 100, 85, 255))
        d.line([(ox + n * .26, n * .20), (ox + n * .74, n * .20)], fill=(80, 85, 70, 255), width=n // 22)
        d.rectangle([ox + n * .34, n * .70, ox + n * .66, n * .76], fill=(70, 60, 45, 255))
        musket(bayonet=True, y0=.06)
    elif kind == "qizilbash":    # Safavid Qizilbash ("red head"): white turban round a tall red baton, kaftan in banner colour, spear
        d.polygon([(ox + n * .45, n * .14), (ox + n * .55, n * .14), (ox + n * .53, -n * .18), (ox + n * .47, -n * .18)], fill=(200, 35, 40, 255))
        d.ellipse([ox + n * .33, n * .06, ox + n * .67, n * .24], fill=(245, 242, 232, 255), outline=(170, 165, 155, 255))
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .44], 0, 180, fill=(60, 40, 25, 255))
        d.rectangle([ox + n * .34, n * .66, ox + n * .66, n * .72], fill=(200, 35, 40, 255))
        d.line([(ox + n * .80, -n * .20), (ox + n * .80, n * 1.24)], fill=wood, width=n // 22)
        d.polygon([(ox + n * .77, -n * .20), (ox + n * .83, -n * .20), (ox + n * .80, -n * .38)], fill=metal)
    elif kind == "visayan":      # Visayan warrior of Mactan: red head cloth, tattooed bare chest, loincloth, kampilan sword + round wooden shield
        d.rectangle([ox + n * .37, n * .13, ox + n * .63, n * .20], fill=(200, 35, 40, 255))
        d.polygon([(ox + n * .62, n * .15), (ox + n * .76, n * .10), (ox + n * .72, n * .22)], fill=(200, 35, 40, 255))
        for k in range(3): d.arc([ox + n * .38, n * (.46 + k * .10), ox + n * .62, n * (.60 + k * .10)], 200, 340, fill=(60, 40, 30, 255), width=n // 40)
        d.rectangle([ox + n * .35, n * .82, ox + n * .65, n * .98], fill=c, outline=dk, width=n // 40)
        d.line([(ox + n * .80, n * .62), (ox + n * .92, -n * .12)], fill=metal, width=n // 16)
        d.line([(ox + n * .74, n * .60), (ox + n * .86, n * .66)], fill=wood, width=n // 22)
        d.ellipse([ox + n * .02, n * .44, ox + n * .36, n * .86], fill=(130, 85, 45, 255), outline=(70, 45, 25, 255), width=n // 30)
    elif kind == "landsknecht":  # German Landsknecht: huge slashed beret with ostrich feathers, puffed striped sleeves, long pike
        d.ellipse([ox + n * .26, n * .06, ox + n * .74, n * .22], fill=(150, 30, 40, 255), outline=(80, 15, 20, 255))
        d.line([(ox + n * .56, n * .10), (ox + n * .78, -n * .16)], fill=(250, 250, 250, 255), width=n // 14)
        d.line([(ox + n * .48, n * .10), (ox + n * .60, -n * .14)], fill=(240, 210, 80, 255), width=n // 18)
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .44], 0, 180, fill=(120, 80, 40, 255))
        for k in range(4): d.line([(ox + n * (.38 + k * .08), n * .44), (ox + n * (.38 + k * .08), n * .94)], fill=(240, 220, 120, 255) if k % 2 else dk, width=n // 22)
        d.ellipse([ox + n * .22, n * .40, ox + n * .40, n * .62], fill=(240, 220, 120, 255), outline=dk)
        d.line([(ox + n * .82, -n * .40), (ox + n * .82, n * 1.28)], fill=wood, width=n // 26)
        d.polygon([(ox + n * .79, -n * .40), (ox + n * .85, -n * .40), (ox + n * .82, -n * .56)], fill=metal)
    elif kind == "swede":        # Swedish peasant soldier of Gustav Vasa (Dalecarlians): kettle hat, blue coat with yellow cross, halberd
        d.chord([ox + n * .32, n * .06, ox + n * .68, n * .26], 180, 360, fill=metal)
        d.polygon([(ox + n * .26, n * .18), (ox + n * .74, n * .18), (ox + n * .68, n * .13), (ox + n * .32, n * .13)], fill=metal)
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .44], 0, 180, fill=(190, 150, 90, 255))
        d.rectangle([ox + n * .36, n * .44, ox + n * .64, n * .94], fill=(40, 80, 170, 255))
        d.line([(ox + n * .46, n * .46), (ox + n * .46, n * .92)], fill=(250, 210, 40, 255), width=n // 14)
        d.line([(ox + n * .37, n * .62), (ox + n * .63, n * .62)], fill=(250, 210, 40, 255), width=n // 14)
        d.line([(ox + n * .80, -n * .24), (ox + n * .80, n * 1.24)], fill=wood, width=n // 22)
        d.polygon([(ox + n * .80, -n * .10), (ox + n * .96, -n * .02), (ox + n * .96, n * .14), (ox + n * .80, n * .10)], fill=metal)
        d.polygon([(ox + n * .77, -n * .24), (ox + n * .83, -n * .24), (ox + n * .80, -n * .40)], fill=metal)
    elif kind == "hussar":       # Hungarian hussar / foot soldier: tall fur kalpak with feather, braided dolman in banner colour, shield + lance
        d.rectangle([ox + n * .36, -n * .04, ox + n * .64, n * .20], fill=(60, 45, 35, 255))
        d.line([(ox + n * .58, n * .00), (ox + n * .70, -n * .26)], fill=(245, 245, 240, 255), width=n // 18)
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .40], 0, 180, fill=(60, 40, 25, 255))
        for k in range(4): d.line([(ox + n * .38, n * (.50 + k * .09)), (ox + n * .62, n * (.50 + k * .09))], fill=(240, 210, 90, 255), width=n // 36)
        d.polygon([(ox + n * .06, n * .44), (ox + n * .34, n * .40), (ox + n * .30, n * .90), (ox + n * .14, n * .80)], fill=(200, 40, 50, 255), outline=(250, 250, 250, 255))
        d.line([(ox + n * .80, -n * .30), (ox + n * .80, n * 1.24)], fill=wood, width=n // 26)
        d.polygon([(ox + n * .80, -n * .26), (ox + n * 1.00, -n * .20), (ox + n * .80, -n * .12)], fill=(60, 140, 70, 255))
    elif kind == "samurai":      # Japanese ashigaru/samurai: kabuto with gold crest horns, lamellar armour in clan colour, sashimono flag, yari spear
        d.chord([ox + n * .30, n * .04, ox + n * .70, n * .32], 180, 360, fill=(40, 38, 44, 255))
        d.polygon([(ox + n * .24, n * .20), (ox + n * .76, n * .20), (ox + n * .70, n * .30), (ox + n * .30, n * .30)], fill=(40, 38, 44, 255))
        d.line([(ox + n * .46, n * .08), (ox + n * .36, -n * .10)], fill=(236, 190, 70, 255), width=n // 24)
        d.line([(ox + n * .54, n * .08), (ox + n * .64, -n * .10)], fill=(236, 190, 70, 255), width=n // 24)
        for k in range(4): d.line([(ox + n * .36, n * (.50 + k * .11)), (ox + n * .64, n * (.50 + k * .11))], fill=dk, width=n // 40)
        d.line([(ox + n * .30, n * .40), (ox + n * .30, -n * .30)], fill=wood, width=n // 30)
        d.rectangle([ox + n * .12, -n * .30, ox + n * .30, -n * .02], fill=c, outline=dk, width=n // 40)
        d.line([(ox + n * .80, -n * .20), (ox + n * .80, n * 1.24)], fill=wood, width=n // 22)
        d.polygon([(ox + n * .77, -n * .20), (ox + n * .83, -n * .20), (ox + n * .80, -n * .38)], fill=metal)
    elif kind == "strelets":     # Muscovite strelets (from 1550): fur-trimmed cap, long kaftan in banner colour, berdysh axe + arquebus
        d.chord([ox + n * .34, n * .00, ox + n * .66, n * .30], 180, 360, fill=c, outline=dk)
        d.rounded_rectangle([ox + n * .32, n * .12, ox + n * .68, n * .21], radius=n * .04, fill=(70, 50, 35, 255))
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .46], 0, 180, fill=(110, 75, 45, 255))
        d.rectangle([ox + n * .34, n * .40, ox + n * .66, n * 1.08], fill=c, outline=dk, width=n // 30)
        d.line([(ox + n * .50, n * .44), (ox + n * .50, n * 1.06)], fill=(240, 210, 90, 255), width=n // 30)
        d.line([(ox + n * .80, -n * .20), (ox + n * .80, n * 1.24)], fill=wood, width=n // 22)
        d.chord([ox + n * .80, -n * .26, ox + n * 1.02, n * .26], 270, 90, fill=metal, outline=(90, 90, 100, 255))
        d.line([(ox + n * .20, n * .46), (ox + n * .20, n * 1.20)], fill=wood, width=n // 22)
    elif kind == "maori":        # Maori warrior: topknot with feathers, moko lines, flax kilt, taiaha staff
        d.ellipse([ox + n * .44, n * .02, ox + n * .56, n * .14], fill=(30, 24, 20, 255))
        d.line([(ox + n * .52, n * .05), (ox + n * .60, -n * .14)], fill=(245, 245, 240, 255), width=n // 22)
        d.line([(ox + n * .48, n * .05), (ox + n * .42, -n * .12)], fill=(30, 30, 30, 255), width=n // 22)
        d.chord([ox + n * .38, n * .12, ox + n * .62, n * .30], 180, 360, fill=(30, 24, 20, 255))
        for k in range(3): d.arc([ox + n * (.40 + k * .02), n * (.24 + k * .03), ox + n * (.60 - k * .02), n * (.38 + k * .02)], 200, 340, fill=(40, 40, 60, 255), width=n // 50)
        for k in range(6): d.line([(ox + n * (.35 + k * .06), n * .78), (ox + n * (.34 + k * .06), n * 1.06)], fill=(190, 160, 90, 255), width=n // 24)
        d.line([(ox + n * .82, -n * .18), (ox + n * .82, n * 1.24)], fill=(120, 70, 35, 255), width=n // 18)
        d.ellipse([ox + n * .78, -n * .26, ox + n * .86, -n * .14], fill=(200, 40, 40, 255))
    elif kind == "bannerman":    # Manchu Qing bannerman: round helmet with tall spike + red tassel, studded armour coat in banner colour, flag on the back, bow
        d.chord([ox + n * .36, n * .06, ox + n * .64, n * .30], 180, 360, fill=(70, 66, 70, 255))
        d.line([(ox + n * .50, n * .08), (ox + n * .50, -n * .16)], fill=(70, 66, 70, 255), width=n // 30)
        d.ellipse([ox + n * .45, -n * .24, ox + n * .55, -n * .12], fill=(200, 30, 40, 255))
        for k in range(4):
            for j in range(3): d.ellipse([ox + n * (.39 + j * .09), n * (.50 + k * .12), ox + n * (.43 + j * .09), n * (.54 + k * .12)], fill=(240, 210, 90, 255))
        d.line([(ox + n * .32, n * .40), (ox + n * .32, -n * .30)], fill=wood, width=n // 30)
        d.polygon([(ox + n * .32, -n * .30), (ox + n * .12, -n * .20), (ox + n * .32, -n * .06)], fill=c, outline=dk)
        d.arc([ox + n * .66, n * .10, ox + n * .96, n * 1.0], 270, 90, fill=(120, 80, 30, 255), width=n // 22)
        d.line([(ox + n * .81, n * .10), (ox + n * .81, n * 1.0)], fill=(230, 230, 220, 255), width=n // 60)
    elif kind == "mughal":       # Mughal / Bengal soldier: white turban, long jama in banner colour with sash, round dhal shield, curved talwar
        d.ellipse([ox + n * .34, n * .04, ox + n * .66, n * .22], fill=(245, 242, 232, 255))
        d.chord([ox + n * .40, n * .28, ox + n * .60, n * .42], 0, 180, fill=(30, 24, 20, 255))
        d.rectangle([ox + n * .34, n * .62, ox + n * .66, n * .70], fill=(240, 210, 90, 255))
        d.rounded_rectangle([ox + n * .30, n * .70, ox + n * .70, n * 1.12], radius=n * .06, fill=c, outline=dk, width=n // 30)
        d.ellipse([ox + n * .04, n * .44, ox + n * .34, n * .74], fill=(110, 70, 40, 255), outline=(240, 210, 90, 255), width=n // 30)
        d.arc([ox + n * .62, -n * .20, ox + n * 1.02, n * .70], 300, 60, fill=metal, width=n // 22)
    elif kind == "sepoy":        # East India Company sepoy: turban in coat colour, red coat, white cross-belts, musket with bayonet
        d.ellipse([ox + n * .34, n * .06, ox + n * .66, n * .22], fill=(245, 245, 240, 255))
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        d.line([(ox + n * .65, n * .44), (ox + n * .35, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        musket(bayonet=True)
    elif kind == "minuteman":    # American militiaman: black tricorne, brown hunting coat/plain clothes, powder horn, long musket
        d.polygon([(ox + n * .28, n * .18), (ox + n * .72, n * .18), (ox + n * .62, n * .04), (ox + n * .50, n * .10), (ox + n * .38, n * .04)], fill=blk)
        d.line([(ox + n * .36, n * .44), (ox + n * .64, n * .86)], fill=(90, 60, 30, 255), width=n // 26)
        d.polygon([(ox + n * .58, n * .80), (ox + n * .72, n * .84), (ox + n * .66, n * .92)], fill=(235, 225, 195, 255))
        musket()
    elif kind == "carolean":     # Swedish Carolean (Charles XII): black tricorne, blue coat with yellow cuffs/belt, sword raised for the charge
        d.polygon([(ox + n * .28, n * .18), (ox + n * .72, n * .18), (ox + n * .62, n * .04), (ox + n * .50, n * .10), (ox + n * .38, n * .04)], fill=blk)
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(250, 210, 40, 255), width=n // 18)
        d.rectangle([ox + n * .34, n * .86, ox + n * .66, n * .94], fill=(250, 210, 40, 255))
        d.line([(ox + n * .70, n * .50), (ox + n * .92, -n * .10)], fill=metal, width=n // 22)
        d.line([(ox + n * .66, n * .56), (ox + n * .78, n * .48)], fill=(200, 170, 60, 255), width=n // 22)
    elif kind == "grenadier":    # Prussian grenadier: tall pointed brass-fronted mitre cap, dark-blue coat, white cross-belts, musket
        d.polygon([(ox + n * .36, n * .18), (ox + n * .64, n * .18), (ox + n * .56, -n * .14), (ox + n * .50, -n * .18), (ox + n * .44, -n * .14)], fill=(220, 190, 80, 255), outline=(150, 120, 40, 255))
        d.ellipse([ox + n * .47, -n * .22, ox + n * .53, -n * .16], fill=(240, 240, 240, 255))
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        d.line([(ox + n * .65, n * .44), (ox + n * .35, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        musket(bayonet=True)
    elif kind == "sansculotte":  # Paris revolutionary of 1789: red Phrygian cap (bonnet rouge), tricolour cockade, striped trousers, pike
        d.polygon([(ox + n * .36, n * .20), (ox + n * .64, n * .20), (ox + n * .62, n * .06), (ox + n * .46, n * .00), (ox + n * .30, n * .10)], fill=(200, 30, 40, 255))
        for k, cc in enumerate([(40, 70, 170), (245, 245, 240), (200, 30, 40)]): d.ellipse([ox + n * (.52 + k * .0), n * (.10 + k * .0), ox + n * (.60 - k * .02), n * (.18 - k * .02)], fill=cc + (255,))
        for k in range(4): d.line([(ox + n * (.38 + k * .08), n * .98), (ox + n * (.38 + k * .08), n * 1.40)], fill=(40, 60, 140, 255), width=max(1, n // 40))
        d.line([(ox + n * .80, -n * .20), (ox + n * .80, n * 1.30)], fill=wood, width=n // 18)
        d.polygon([(ox + n * .76, -n * .18), (ox + n * .84, -n * .18), (ox + n * .80, -n * .38)], fill=metal)
    elif kind == "haitian":      # Haitian revolutionary soldier (Dessalines' army): black bicorne with red-blue cockade, blue coat with red facings, musket
        d.chord([ox + n * .24, n * .02, ox + n * .76, n * .34], 180, 360, fill=blk)
        d.ellipse([ox + n * .54, n * .06, ox + n * .64, n * .16], fill=(200, 30, 40, 255))
        d.polygon([(ox + n * .42, n * .42), (ox + n * .58, n * .42), (ox + n * .50, n * .70)], fill=(200, 30, 40, 255))
        d.line([(ox + n * .35, n * .44), (ox + n * .65, n * .92)], fill=(245, 245, 240, 255), width=n // 20)
        musket(bayonet=True)
    elif kind == "dutch":        # Dutch VOC sailor-soldier: wide black hat, orange sash, morion-less, musket
        d.ellipse([ox + n * .22, n * .10, ox + n * .78, n * .22], fill=blk)
        d.rectangle([ox + n * .38, n * .00, ox + n * .62, n * .16], fill=blk)
        d.rectangle([ox + n * .36, n * .62, ox + n * .64, n * .70], fill=(240, 130, 30, 255))
        d.polygon([(ox + n * .40, n * .40), (ox + n * .60, n * .40), (ox + n * .50, n * .52)], fill=(245, 245, 240, 255))
        musket()
    return im.resize((int(im.width / S), int(im.height / S)), Image.LANCZOS)
