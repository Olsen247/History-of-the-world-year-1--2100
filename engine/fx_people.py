"""Stylised portrait medallions of historical people + boats for sea crossings."""
import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
SERIF_B = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
S = 3

def _beard(d, n, kind, col, cx, chin):
    if kind == "none": return
    if kind == "stubble":
        d.chord([cx - n*.17, chin - n*.16, cx + n*.17, chin + n*.03], 0, 180, fill=col[:3] + (110,)); return
    if kind == "mustache":
        d.polygon([(cx - n*.09, chin - n*.10), (cx, chin - n*.115), (cx + n*.09, chin - n*.10), (cx + n*.06, chin - n*.08), (cx, chin - n*.095), (cx - n*.06, chin - n*.08)], fill=col)
        d.line([(cx - n*.085, chin - n*.10), (cx - n*.12, chin - n*.03)], fill=col, width=int(n*.02))
        d.line([(cx + n*.085, chin - n*.10), (cx + n*.12, chin - n*.03)], fill=col, width=int(n*.02)); return
    L = dict(short=0.06, full=0.12, long=0.24, curly=0.16, thin=0.08)[kind]
    w = 0.19 if kind != "thin" else 0.08
    d.polygon([(cx - n*.19, chin - n*.20), (cx - n*w, chin + n*L*0.4), (cx, chin + n*L), (cx + n*w, chin + n*L*0.4), (cx + n*.19, chin - n*.20),
               (cx + n*.13, chin - n*.06), (cx, chin - n*.03), (cx - n*.13, chin - n*.06)], fill=col)
    # mouth gap + mustache
    d.polygon([(cx - n*.09, chin - n*.10), (cx, chin - n*.12), (cx + n*.09, chin - n*.10), (cx + n*.05, chin - n*.075), (cx - n*.05, chin - n*.075)], fill=col)
    if kind in ("curly", "long"):
        dk = tuple(max(0, v - 35) for v in col[:3]) + (255,)
        for k in range(14):
            rr = random.Random(k)
            x = cx + (rr.random() - 0.5) * n * 0.32; y = chin - n * 0.04 + rr.random() * n * L
            d.arc([x - n*.03, y - n*.02, x + n*.03, y + n*.03], 0, 180, fill=dk, width=int(n * .012))

def face(spec, size=300):
    n = size * S
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    skin = spec.get("skin", (222, 178, 140)) + (255,)
    sk_dk = tuple(int(v * 0.82) for v in skin[:3]) + (255,)
    hair = spec.get("hair_col", (60, 40, 25)) + (255,)
    robe = spec.get("robe", (150, 40, 50)) + (255,)
    cx = n * 0.5; top = n * 0.22; chin = n * 0.66
    # shoulders / clothing
    d.chord([n*.10, n*.68, n*.90, n*1.35], 180, 360, fill=robe)
    if spec.get("armor"):
        a = spec["armor"] + (255,)
        d.chord([n*.18, n*.70, n*.82, n*1.25], 180, 360, fill=a)
        for k in range(4): d.arc([n*.22, n*(.74 + k*.05), n*.78, n*(1.2 + k*.05)], 200, 340, fill=tuple(int(v*.7) for v in a[:3]) + (255,), width=int(n*.01))
    if spec.get("cloak"):
        c = spec["cloak"] + (255,)
        d.polygon([(n*.12, n*1.0), (n*.30, n*.74), (n*.40, n*.80), (n*.26, n*1.0)], fill=c)
        d.polygon([(n*.88, n*1.0), (n*.70, n*.74), (n*.60, n*.80), (n*.74, n*1.0)], fill=c)
        d.ellipse([n*.62, n*.74, n*.70, n*.82], fill=(230, 190, 70, 255))
    neckw = 0.09 if spec.get("female") else 0.11
    d.rectangle([cx - n*neckw, n*.58, cx + n*neckw, n*.76], fill=sk_dk)
    hs = spec.get("hair", "short")
    # hair behind head
    if hs in ("long", "female_long"):
        d.rounded_rectangle([cx - n*.25, top + n*.02, cx + n*.25, n*(0.86 if hs == "female_long" else 0.74)], radius=n*.12, fill=hair)
    if hs == "curly_long":
        for k in range(18):
            a = math.pi * (0.05 + 0.9 * k / 17)
            x = cx - math.cos(a) * n * .25; y = top + n*.18 + math.sin(a) * n * .05 + (k % 3) * n * .06
            d.ellipse([x - n*.06, y - n*.06 + n*.12, x + n*.06, y + n*.06 + n*.12], fill=hair)
    # ears + head
    d.ellipse([cx - n*.235, n*.38, cx - n*.17, n*.50], fill=sk_dk); d.ellipse([cx + n*.17, n*.38, cx + n*.235, n*.50], fill=sk_dk)
    hw = 0.185 if spec.get("female") else 0.2
    d.ellipse([cx - n*hw, top, cx + n*hw, chin + n*.02], fill=skin)
    # hair on top
    if hs in ("short", "long", "curly_long", "curly", "female_long", "bun", "fringe"):
        d.chord([cx - n*.205, top - n*.02, cx + n*.205, top + n*.26], 180, 360, fill=hair)
        d.rectangle([cx - n*.205, top + n*.10, cx - n*.17, top + n*.22], fill=hair); d.rectangle([cx + n*.17, top + n*.10, cx + n*.205, top + n*.22], fill=hair)
        if hs in ("curly", "curly_long"):
            for k in range(9):
                x = cx - n*.18 + k * n*.045; d.ellipse([x - n*.035, top - n*.03, x + n*.035, top + n*.05], fill=hair)
        if hs == "fringe":
            for k in range(7):
                x = cx - n*.15 + k * n*.05; d.polygon([(x - n*.03, top + n*.06), (x + n*.03, top + n*.06), (x, top + n*.14)], fill=hair)
        if hs == "bun": d.ellipse([cx - n*.08, top - n*.12, cx + n*.08, top + n*.02], fill=hair)
    # eyes
    ey = n * 0.43
    look = spec.get("look", 0)
    for sx in (-1, 1):
        ex = cx + sx * n * .085
        d.ellipse([ex - n*.04, ey - n*.022, ex + n*.04, ey + n*.022], fill=(250, 248, 244, 255))
        d.ellipse([ex - n*.018, ey - n*.02 - look*n*.012, ex + n*.018, ey + n*.016 - look*n*.012], fill=spec.get("eye", (60, 40, 30)) + (255,))
        bw = int(n * (0.022 if not spec.get("female") else 0.012))
        d.line([(ex - n*.05, ey - n*.05 + sx*0), (ex + n*.05, ey - n*.055)], fill=tuple(max(0, v - 20) for v in hair[:3]) + (255,), width=bw)
    if spec.get("kohl"):
        for sx in (-1, 1):
            ex = cx + sx * n * .085; d.arc([ex - n*.045, ey - n*.03, ex + n*.045, ey + n*.03], 190, 350, fill=(20, 15, 15, 255), width=int(n*.008))
    # nose + mouth
    nose = spec.get("nose", 1.0)
    d.line([(cx, ey + n*.01), (cx - n*.025*nose, n*.53), (cx + n*.012, n*.535)], fill=sk_dk, width=int(n*.012))
    lip = (170, 80, 80, 255) if spec.get("female") else (150, 85, 75, 255)
    d.arc([cx - n*.06, n*.54, cx + n*.06, n*.60], 20, 160, fill=lip, width=int(n*.014))
    if spec.get("age"):
        for k in (0, 1): d.arc([cx - n*.13, n*(.30 + k*.025), cx + n*.13, n*(.40 + k*.025)], 220, 320, fill=sk_dk, width=int(n*.006))
        d.line([(cx - n*.07, n*.50), (cx - n*.10, n*.57)], fill=sk_dk, width=int(n*.006)); d.line([(cx + n*.07, n*.50), (cx + n*.10, n*.57)], fill=sk_dk, width=int(n*.006))
    bc = spec.get("beard_col", spec.get("hair_col", (60, 40, 25))) + (255,)
    _beard(d, n, spec.get("beard", "none"), bc, cx, chin)
    # headgear
    hat = spec.get("hat", "none")
    gold = (236, 190, 70, 255); gdk = (150, 105, 25, 255)
    if hat == "laurel":
        for side in (-1, 1):
            for k in range(7):
                a = math.radians(200 + k * 18) if side < 0 else math.radians(340 - k * 18)
                x = cx + math.cos(a) * n*.20; y = top + n*.14 + math.sin(a) * n*.10
                d.ellipse([x - n*.035, y - n*.016, x + n*.035, y + n*.016], fill=(80, 150, 60, 255), outline=(40, 90, 30, 255))
    elif hat == "diadem":
        d.rectangle([cx - n*.205, top + n*.11, cx + n*.205, top + n*.15], fill=gold)
        for k in range(7): x = cx - n*.15 + k*n*.05; d.ellipse([x - n*.012, top + n*.115, x + n*.012, top + n*.145], fill=(245, 245, 250, 255))
        d.polygon([(cx + n*.20, top + n*.13), (cx + n*.28, top + n*.26), (cx + n*.24, top + n*.27), (cx + n*.19, top + n*.15)], fill=gold)
    elif hat == "korymbos":   # Sasanian crown: crenellated band + big silk globe + ribbons
        c2 = spec.get("crown_col", gold)
        d.rectangle([cx - n*.21, top + n*.02, cx + n*.21, top + n*.14], fill=c2, outline=gdk)
        for k in range(5): x = cx - n*.18 + k*n*.09; d.polygon([(x, top + n*.02), (x + n*.045, top - n*.06), (x + n*.09, top + n*.02)], fill=c2)
        d.ellipse([cx - n*.16, top - n*.30, cx + n*.16, top - n*.02], fill=spec.get("globe", (110, 60, 140)) + (255,), outline=gdk, width=int(n*.01))
        for sx in (-1, 1):
            d.polygon([(cx + sx*n*.21, top + n*.10), (cx + sx*n*.36, top + n*.34), (cx + sx*n*.31, top + n*.36), (cx + sx*n*.20, top + n*.15)], fill=(200, 60, 60, 255))
    elif hat == "crown":
        d.rectangle([cx - n*.20, top + n*.0, cx + n*.20, top + n*.12], fill=gold, outline=gdk)
        for k in range(5): x = cx - n*.20 + k*n*.10; d.polygon([(x, top), (x + n*.05, top - n*.10), (x + n*.10, top)], fill=gold, outline=gdk)
        for k in range(4): x = cx - n*.15 + k*n*.10; d.ellipse([x - n*.015, top + n*.04, x + n*.015, top + n*.08], fill=(200, 40, 50, 255))
    elif hat == "fur":
        d.chord([cx - n*.22, top - n*.08, cx + n*.22, top + n*.30], 180, 360, fill=spec.get("hat_col", (120, 50, 40)) + (255,))
        d.rounded_rectangle([cx - n*.24, top + n*.06, cx + n*.24, top + n*.17], radius=n*.05, fill=(150, 120, 90, 255))
        for k in range(10): x = cx - n*.22 + k*n*.049; d.line([(x, top + n*.07), (x + n*.01, top + n*.16)], fill=(110, 85, 60, 255), width=int(n*.006))
    elif hat == "helmet":
        hc = spec.get("hat_col", (150, 150, 160)) + (255,)
        d.chord([cx - n*.215, top - n*.06, cx + n*.215, top + n*.34], 180, 360, fill=hc, outline=(80, 80, 90, 255), width=int(n*.01))
        d.rectangle([cx - n*.215, top + n*.13, cx + n*.215, top + n*.17], fill=(110, 110, 120, 255))
        d.rectangle([cx - n*.015, top + n*.15, cx + n*.015, n*.50], fill=hc)
        if spec.get("crest"): d.chord([cx - n*.18, top - n*.18, cx + n*.18, top + n*.06], 180, 360, fill=spec["crest"] + (255,))
    elif hat == "turban":
        tc = spec.get("hat_col", (240, 236, 225)) + (255,)
        d.ellipse([cx - n*.25, top - n*.12, cx + n*.25, top + n*.20], fill=tc, outline=tuple(int(v*.8) for v in tc[:3]) + (255,), width=int(n*.01))
        for k in range(3): d.arc([cx - n*.24, top - n*.08 + k*n*.06, cx + n*.24, top + n*.22 + k*n*.06], 200, 340, fill=tuple(int(v*.8) for v in tc[:3]) + (255,), width=int(n*.01))
        if spec.get("jewel"): d.ellipse([cx - n*.03, top + n*.02, cx + n*.03, top + n*.08], fill=(220, 40, 60, 255))
    elif hat == "veil":
        vc = spec.get("hat_col", (240, 236, 225)) + (255,)
        d.chord([cx - n*.25, top - n*.06, cx + n*.25, top + n*.34], 180, 360, fill=vc)
        d.polygon([(cx - n*.25, top + n*.14), (cx - n*.30, n*.82), (cx - n*.18, n*.80), (cx - n*.19, top + n*.18)], fill=vc)
        d.polygon([(cx + n*.25, top + n*.14), (cx + n*.30, n*.82), (cx + n*.18, n*.80), (cx + n*.19, top + n*.18)], fill=vc)
    elif hat == "cap":
        hc = spec.get("hat_col", (60, 60, 120)) + (255,)
        d.chord([cx - n*.21, top - n*.04, cx + n*.21, top + n*.26], 180, 360, fill=hc)
    elif hat == "wingcap":   # Ming court hat (wushamao): black rounded cap with two flat side wings
        hc = spec.get("hat_col", (25, 25, 30)) + (255,)
        d.rounded_rectangle([cx - n*.40, top + n*.06, cx - n*.17, top + n*.11], radius=n*.02, fill=hc)
        d.rounded_rectangle([cx + n*.17, top + n*.06, cx + n*.40, top + n*.11], radius=n*.02, fill=hc)
        d.chord([cx - n*.20, top - n*.12, cx + n*.20, top + n*.20], 180, 360, fill=hc)
        d.rectangle([cx - n*.215, top + n*.02, cx + n*.215, top + n*.15], fill=hc)
        if spec.get("dragon"):
            for k in range(3): d.arc([n*(.30 + k*.12), n*.80, n*(.40 + k*.12), n*.90], 0, 300, fill=(240, 200, 60, 255), width=int(n*.012))
    elif hat == "mascaypacha":   # Sapa Inca headdress: braided llautu band, red wool fringe on the forehead, upright feathers; gold ear spools
        d.rectangle([cx - n*.215, top + n*.06, cx + n*.215, top + n*.13], fill=(200, 160, 60, 255))
        for k in range(9): x = cx - n*.20 + k*n*.05; d.line([(x, top + n*.07), (x + n*.025, top + n*.12)], fill=(120, 60, 30, 255), width=int(n*.008))
        for k in range(9): x = cx - n*.10 + k*n*.025; d.rectangle([x, top + n*.13, x + n*.016, top + n*.175], fill=(200, 30, 40, 255))
        for k, fc in enumerate([(30, 30, 30), (240, 240, 235), (30, 30, 30)]):
            x = cx + (k - 1) * n*.035; d.polygon([(x - n*.018, top + n*.06), (x + n*.018, top + n*.06), (x, top - n*.20)], fill=fc + (255,))
        for sx in (-1, 1): d.ellipse([cx + sx*n*.205 - n*.045, n*.40, cx + sx*n*.205 + n*.045, n*.49], fill=(236, 190, 70, 255), outline=(150, 105, 25, 255))
    elif hat == "chaperon":     # big draped 15th-century chaperon hat
        hc = spec.get("hat_col", (25, 25, 30)) + (255,)
        d.ellipse([cx - n*.27, top - n*.14, cx + n*.27, top + n*.16], fill=hc)
        d.rounded_rectangle([cx - n*.24, top + n*.02, cx + n*.24, top + n*.13], radius=n*.04, fill=hc)
    elif hat == "bigturban":    # large white Ottoman turban wrapped round a red cap (Mehmed II)
        d.ellipse([cx - n*.10, top - n*.30, cx + n*.10, top - n*.04], fill=(190, 40, 45, 255))
        tc = (248, 246, 238, 255); sh = (200, 196, 186, 255)
        d.ellipse([cx - n*.30, top - n*.16, cx + n*.30, top + n*.20], fill=tc, outline=sh, width=int(n*.01))
        for k in range(4): d.arc([cx - n*.29, top - n*.13 + k*n*.06, cx + n*.29, top + n*.21 + k*n*.06], 200, 340, fill=sh, width=int(n*.01))
    elif hat == "vladcap":      # Vlad III's red velvet cap: gold band with pearl rows, jewelled star and feather
        hc = (175, 25, 40, 255)
        d.rounded_rectangle([cx - n*.23, top - n*.16, cx + n*.20, top + n*.14], radius=n*.08, fill=hc)
        d.rectangle([cx - n*.23, top + n*.06, cx + n*.22, top + n*.14], fill=gold, outline=gdk)
        for row in (0, 1):
            for k in range(7): x = cx - n*.19 + k*n*.06; y = top - n*.08 + row*n*.07; d.ellipse([x - n*.014, y - n*.014, x + n*.014, y + n*.014], fill=(250, 248, 240, 255))
        d.ellipse([cx - n*.05, top - n*.02, cx + n*.05, top + n*.08], fill=(230, 190, 70, 255), outline=gdk)
        d.polygon([(cx + n*.02, top - n*.12), (cx + n*.14, top - n*.42), (cx + n*.10, top - n*.10)], fill=(245, 240, 230, 255))
    if spec.get("halo"):
        pass
    return im

def medallion(spec, size=260, ring=(200, 160, 60)):
    n = size * S
    out = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    m = Image.new("L", (n, n), 0); ImageDraw.Draw(m).ellipse([n*.06, n*.06, n*.94, n*.94], fill=255)
    bg = Image.new("RGBA", (n, n), (0, 0, 0, 0)); bd = ImageDraw.Draw(bg)
    col = spec.get("bg", (40, 60, 90))
    for k in range(40):
        f = k / 39; c = tuple(int(v * (1.25 - 0.75 * f)) for v in col) + (255,)
        r = n * (0.44 - 0.44 * f * 0.98); bd.ellipse([n/2 - r, n/2 - r - n*0.06*(1-f), n/2 + r, n/2 + r - n*0.06*(1-f)], fill=c)
    fs, oy = (0.80, 0.20) if spec.get("hat") == "korymbos" else (0.88, 0.11)
    f = face(spec, size=int(size * fs)).resize((int(n * fs), int(n * fs)), Image.LANCZOS)
    bg.alpha_composite(f, (int(n * (1 - fs) / 2), int(n * oy)))
    bg.putalpha(Image.composite(bg.getchannel("A"), Image.new("L", (n, n), 0), m))
    out.alpha_composite(bg)
    d = ImageDraw.Draw(out)
    d.ellipse([n*.04, n*.04, n*.96, n*.96], outline=(240, 200, 90, 255), width=int(n*.035))
    d.ellipse([n*.085, n*.085, n*.915, n*.915], outline=ring + (255,), width=int(n*.012))
    out = out.resize((size, size), Image.LANCZOS)
    g = out.getchannel("A").filter(ImageFilter.GaussianBlur(10))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 255)); sh.putalpha(g.point(lambda v: int(v * 0.6)))
    fin = Image.new("RGBA", (size + 30, size + 30), (0, 0, 0, 0)); fin.alpha_composite(sh, (15, 22)); fin.alpha_composite(out, (15, 12))
    return fin

def name_plate(name, sub=None, size=40):
    f = ImageFont.truetype(SERIF_B, size); f2 = ImageFont.truetype(SERIF_B, int(size * 0.62))
    w = max(f.getbbox(name, stroke_width=3)[2], f2.getbbox(sub or " ", stroke_width=2)[2]) + 40
    h = int(size * (1.35 + (0.9 if sub else 0))) + 20
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((w / 2, size * 0.7 + 8), name, font=f, fill=(255, 236, 170, 255), anchor="mm", stroke_width=4, stroke_fill=(15, 10, 5, 255))
    if sub: d.text((w / 2, size * 1.65 + 10), sub, font=f2, fill=(235, 238, 245, 255), anchor="mm", stroke_width=3, stroke_fill=(10, 10, 15, 255))
    return im

def ship(col, size=60):
    n = size * S; im = Image.new("RGBA", (int(n * 1.4), int(n * 1.3)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = col + (255,); wood = (110, 70, 40, 255); dk = (60, 36, 20, 255)
    d.polygon([(n*.05, n*.82), (n*1.35, n*.82), (n*1.15, n*1.05), (n*.25, n*1.05)], fill=wood, outline=dk, width=int(n*.03))
    d.polygon([(n*1.35, n*.82), (n*1.40, n*.62), (n*1.25, n*.82)], fill=wood)
    d.line([(n*.70, n*.82), (n*.70, n*.05)], fill=dk, width=int(n*.05))
    d.polygon([(n*.30, n*.14), (n*1.10, n*.14), (n*1.04, n*.70), (n*.36, n*.70)], fill=c, outline=tuple(int(v*.5) for v in col) + (255,), width=int(n*.03))
    d.line([(n*.33, n*.42), (n*1.07, n*.42)], fill=(255, 255, 255, 120), width=int(n*.03))
    for k in range(6): x = n*(.35 + k*.14); d.line([(x, n*1.0), (x - n*.08, n*1.2)], fill=dk, width=int(n*.025))
    im = im.resize((int(im.width / S), int(im.height / S)), Image.LANCZOS)
    pad = 5; out = Image.new("RGBA", (im.width + 2*pad, im.height + 2*pad), (0, 0, 0, 0))
    a = Image.new("L", out.size, 0); a.paste(im.getchannel("A"), (pad, pad))
    ol = Image.new("RGBA", out.size, (255, 255, 255, 255)); ol.putalpha(a.filter(ImageFilter.MaxFilter(3)).point(lambda v: int(v * 0.85)))
    out.alpha_composite(ol); out.alpha_composite(im, (pad, pad))
    return out

# ---------------- people of the series ----------------
P = {
 # Ep 4
 "ardashir": dict(hat="korymbos", beard="curly", hair="curly_long", hair_col=(40, 28, 22), robe=(150, 40, 60), bg=(120, 50, 40), skin=(205, 160, 120), globe=(150, 70, 60)),
 "shapur": dict(hat="korymbos", beard="curly", hair="curly_long", hair_col=(35, 25, 20), robe=(120, 30, 80), bg=(120, 50, 40), skin=(205, 160, 120), globe=(90, 60, 150)),
 "valerian": dict(hat="laurel", beard="short", hair="short", hair_col=(140, 135, 130), robe=(150, 40, 50), cloak=(170, 30, 40), age=True, bg=(110, 30, 40)),
 "zenobia": dict(female=True, hat="diadem", hair="female_long", hair_col=(30, 20, 18), robe=(110, 50, 140), bg=(90, 50, 110), skin=(200, 150, 110), kohl=True),
 "aurelian": dict(hat="laurel", beard="stubble", hair="short", hair_col=(70, 55, 40), armor=(170, 150, 110), cloak=(170, 30, 40), bg=(110, 30, 40)),
 "constantine": dict(hat="diadem", beard="none", hair="fringe", hair_col=(70, 50, 30), robe=(110, 40, 120), cloak=(120, 30, 120), look=1, bg=(90, 40, 100)),
 "alaric": dict(beard="full", hair="long", hair_col=(170, 120, 60), robe=(90, 110, 70), cloak=(120, 80, 40), bg=(70, 90, 60)),
 "attila": dict(hat="fur", beard="thin", hair="short", hair_col=(40, 30, 25), robe=(110, 70, 40), skin=(200, 160, 120), bg=(90, 60, 40), hat_col=(70, 50, 40), nose=1.3),
 "gaiseric": dict(beard="full", hair="long", hair_col=(120, 85, 50), hat="crown", robe=(60, 100, 140), bg=(50, 80, 110)),
 "odoacer": dict(beard="mustache", hair="long", hair_col=(150, 110, 60), robe=(60, 90, 70), cloak=(140, 110, 60), bg=(70, 90, 60)),
 "romulus": dict(hat="diadem", beard="none", hair="short", hair_col=(120, 85, 50), robe=(110, 40, 120), bg=(110, 30, 40)),
 # Ep 5
 "justinian": dict(hat="crown", beard="none", hair="short", hair_col=(80, 55, 35), robe=(110, 40, 120), cloak=(120, 30, 120), bg=(90, 40, 100), skin=(222, 180, 145)),
 "belisarius": dict(hat="helmet", crest=(190, 40, 40), beard="short", hair="short", hair_col=(60, 45, 30), armor=(180, 160, 110), cloak=(150, 40, 120), bg=(90, 40, 100)),
 "tariq": dict(hat="turban", hat_col=(245, 242, 232), beard="full", hair="short", hair_col=(30, 25, 20), robe=(60, 120, 80), skin=(190, 145, 105), bg=(50, 110, 70)),
 "charles": dict(beard="mustache", hair="long", hair_col=(150, 105, 55), armor=(160, 160, 170), cloak=(170, 40, 40), bg=(50, 80, 140)),
 "saffah": dict(hat="turban", hat_col=(35, 35, 40), beard="full", hair="short", hair_col=(25, 20, 18), robe=(40, 40, 48), skin=(200, 155, 115), bg=(70, 70, 85)),
 "abdalrahman": dict(hat="turban", hat_col=(245, 240, 225), beard="short", hair="short", hair_col=(170, 110, 60), beard_col=(170, 110, 60), robe=(240, 238, 230), skin=(215, 170, 130), bg=(50, 130, 80)),
 "xuanzong": dict(hat="cap", hat_col=(30, 30, 35), beard="thin", hair="short", hair_col=(25, 20, 18), robe=(230, 180, 50), skin=(222, 185, 150), bg=(170, 130, 40)),
 "libai": dict(hat="none", hair="bun", hair_col=(25, 20, 18), beard="long", beard_col=(60, 55, 50), robe=(200, 215, 230), skin=(222, 185, 150), bg=(60, 90, 120)),
 # Ep 6
 "erik": dict(beard="long", hair="long", hair_col=(170, 60, 30), beard_col=(170, 60, 30), robe=(90, 70, 50), cloak=(60, 90, 140), bg=(40, 70, 110), age=True),
 "leif": dict(beard="full", hair="long", hair_col=(200, 150, 80), beard_col=(190, 140, 70), robe=(120, 60, 50), cloak=(60, 90, 140), bg=(40, 70, 110)),
 "rollo": dict(hat="helmet", beard="full", hair="long", hair_col=(180, 130, 70), beard_col=(180, 130, 70), armor=(150, 150, 160), cloak=(140, 40, 40), bg=(40, 70, 110)),
 "charlemagne": dict(hat="crown", beard="long", hair="long", hair_col=(220, 220, 215), beard_col=(230, 230, 225), robe=(60, 80, 160), cloak=(150, 30, 40), bg=(50, 80, 140), age=True),
 "basil": dict(hat="crown", beard="full", hair="short", hair_col=(60, 45, 35), armor=(200, 170, 80), cloak=(110, 40, 120), bg=(90, 40, 100)),
 "olaf": dict(hat="crown", beard="short", hair="long", hair_col=(200, 160, 90), robe=(170, 40, 40), cloak=(60, 90, 140), bg=(40, 70, 110)),
 "vladimir": dict(hat="fur", hat_col=(150, 40, 40), beard="full", hair="short", hair_col=(120, 85, 50), robe=(150, 40, 40), bg=(120, 50, 40)),
 "murasaki": dict(female=True, hair="female_long", hair_col=(20, 15, 15), robe=(170, 60, 90), skin=(235, 205, 180), bg=(150, 70, 90)),
 # Ep 7
 "william": dict(hat="helmet", beard="none", hair="short", hair_col=(90, 60, 35), armor=(150, 150, 160), cloak=(170, 40, 40), bg=(150, 120, 40)),
 "saladin": dict(hat="turban", hat_col=(240, 236, 225), jewel=True, beard="full", hair="short", hair_col=(30, 22, 18), robe=(60, 120, 80), skin=(200, 155, 115), bg=(180, 150, 60)),
 "genghis": dict(hat="fur", hat_col=(235, 232, 225), beard="thin", beard_col=(150, 145, 140), hair="short", hair_col=(60, 55, 50), robe=(235, 232, 220), skin=(215, 175, 135), bg=(95, 85, 70), age=True),
 "batu": dict(hat="fur", hat_col=(120, 40, 40), beard="mustache", hair="short", hair_col=(30, 25, 20), robe=(150, 120, 70), skin=(215, 175, 135), bg=(150, 120, 70)),
 "hulagu": dict(hat="fur", hat_col=(60, 60, 90), beard="thin", hair="short", hair_col=(30, 25, 20), robe=(120, 95, 85), skin=(215, 175, 135), bg=(120, 95, 85)),
 "baybars": dict(hat="turban", hat_col=(240, 210, 80), beard="short", hair="short", hair_col=(80, 60, 40), eye=(70, 110, 160), robe=(200, 170, 70), skin=(215, 175, 135), bg=(200, 170, 70)),
 "kublai": dict(hat="cap", hat_col=(240, 236, 225), beard="thin", hair="short", hair_col=(30, 25, 20), robe=(240, 236, 225), skin=(222, 180, 140), bg=(95, 85, 70)),
 "marco": dict(hat="cap", hat_col=(170, 30, 40), beard="short", hair="short", hair_col=(90, 60, 35), robe=(170, 30, 40), bg=(60, 90, 140)),
 # Ep 8
 "osman": dict(hat="turban", hat_col=(245, 242, 232), beard="full", hair="short", hair_col=(40, 30, 25), robe=(150, 40, 40), skin=(205, 160, 120), bg=(150, 40, 40)),
 "mansamusa": dict(hat="crown", beard="short", hair="short", hair_col=(25, 20, 18), robe=(230, 180, 50), skin=(110, 72, 48), bg=(210, 160, 60)),
 "tughluq": dict(hat="turban", hat_col=(70, 140, 110), beard="full", hair="short", hair_col=(25, 20, 18), robe=(60, 140, 110), skin=(170, 125, 90), bg=(60, 140, 110)),
 "edward3": dict(hat="crown", beard="long", hair="long", hair_col=(170, 120, 60), beard_col=(170, 120, 60), robe=(200, 70, 80), cloak=(60, 60, 140), bg=(200, 70, 80)),
 "janibeg": dict(hat="fur", hat_col=(150, 120, 70), beard="thin", hair="short", hair_col=(30, 25, 20), robe=(150, 120, 70), skin=(215, 175, 135), bg=(150, 120, 70)),
 "aryabhata": dict(hat="none", beard="full", hair="bun", hair_col=(25, 20, 18), robe=(230, 150, 50), skin=(160, 115, 80), bg=(150, 90, 40), age=True),
 "hongwu": dict(hat="wingcap", dragon=True, beard="long", beard_col=(40, 35, 30), hair="short", hair_col=(30, 25, 20), robe=(225, 185, 60), skin=(205, 160, 120), bg=(180, 50, 45), nose=1.3, age=True),
 "timur": dict(hat="fur", hat_col=(150, 40, 40), beard="thin", hair="short", hair_col=(80, 50, 30), beard_col=(150, 90, 50), robe=(60, 120, 140), cloak=(170, 140, 60), skin=(210, 170, 130), bg=(70, 130, 150), age=True),
 "dmitry": dict(hat="fur", hat_col=(180, 150, 60), beard="full", hair="long", hair_col=(110, 75, 45), beard_col=(110, 75, 45), robe=(160, 40, 40), cloak=(200, 170, 70), bg=(120, 140, 80)),
 "murad": dict(hat="turban", hat_col=(245, 242, 232), beard="full", hair="short", hair_col=(50, 35, 25), robe=(30, 110, 70), skin=(205, 160, 120), bg=(170, 50, 50)),
 "lazar": dict(hat="crown", beard="long", hair="long", hair_col=(90, 60, 35), beard_col=(90, 60, 35), robe=(150, 40, 60), cloak=(200, 160, 60), bg=(150, 50, 70)),
 "margaret": dict(female=True, hat="crown", hair="female_long", hair_col=(150, 100, 50), robe=(150, 30, 40), cloak=(40, 60, 140), skin=(235, 200, 170), bg=(170, 50, 60)),
 "bayezid": dict(hat="turban", hat_col=(250, 248, 240), jewel=True, beard="full", hair="short", hair_col=(60, 40, 25), beard_col=(90, 55, 30), robe=(170, 40, 40), cloak=(220, 180, 70), skin=(210, 165, 125), bg=(170, 50, 50)),
 "yongle": dict(hat="wingcap", dragon=True, beard="long", beard_col=(30, 25, 22), hair="short", hair_col=(25, 20, 18), robe=(225, 185, 60), skin=(212, 168, 128), bg=(180, 50, 45)),
 # Ep 10
 "jogaila": dict(hat="crown", beard="none", hair="long", hair_col=(120, 85, 50), robe=(170, 30, 40), cloak=(240, 240, 240), skin=(232, 196, 165), bg=(170, 40, 50)),
 "henry5": dict(hat="crown", beard="none", hair="fringe", hair_col=(90, 55, 30), robe=(180, 30, 40), cloak=(40, 60, 150), skin=(235, 200, 170), nose=1.2, bg=(160, 40, 50)),
 "henrynav": dict(hat="chaperon", hat_col=(25, 25, 30), beard="mustache", hair="short", hair_col=(40, 30, 22), robe=(30, 30, 35), skin=(226, 186, 150), bg=(50, 120, 80)),
 "joan": dict(female=True, hat="none", hair="fringe", hair_col=(60, 40, 25), armor=(180, 182, 190), robe=(40, 70, 170), skin=(236, 200, 170), bg=(40, 70, 160)),
 "pachacuti": dict(hat="mascaypacha", beard="none", hair="short", hair_col=(25, 20, 18), robe=(190, 140, 50), cloak=(170, 40, 40), skin=(175, 120, 85), bg=(170, 120, 40)),
 "murad2": dict(hat="turban", hat_col=(248, 246, 238), jewel=True, beard="full", hair="short", hair_col=(50, 35, 22), beard_col=(70, 45, 28), robe=(40, 110, 70), cloak=(220, 180, 70), skin=(210, 165, 125), bg=(170, 50, 50)),
 "wladyslaw": dict(hat="crown", beard="none", hair="long", hair_col=(110, 75, 40), robe=(180, 30, 40), armor=(175, 178, 186), skin=(235, 200, 170), bg=(120, 40, 50)),
 "gutenberg": dict(hat="fur", hat_col=(120, 40, 35), beard="long", hair="short", hair_col=(110, 80, 50), beard_col=(120, 85, 55), robe=(90, 60, 40), skin=(226, 186, 150), age=True, bg=(70, 60, 50)),
 "mehmed2": dict(hat="bigturban", beard="full", hair="short", hair_col=(60, 40, 25), beard_col=(90, 55, 30), robe=(170, 40, 40), cloak=(220, 180, 70), skin=(210, 165, 125), nose=1.5, bg=(170, 40, 45)),
 "constantine11": dict(hat="crown", beard="long", hair="long", hair_col=(80, 55, 35), beard_col=(90, 65, 45), robe=(120, 30, 110), cloak=(230, 190, 70), skin=(225, 185, 150), age=True, bg=(110, 40, 110)),
 "columbus": dict(hat="none", beard="none", hair="long", hair_col=(170, 160, 150), robe=(35, 35, 42), cloak=(110, 30, 40), skin=(230, 190, 160), age=True, bg=(40, 90, 140)),
 "isabella": dict(female=True, hat="crown", hair="female_long", hair_col=(170, 100, 50), robe=(150, 30, 40), cloak=(230, 190, 70), skin=(238, 205, 178), bg=(160, 110, 40)),
 "ferdinand": dict(hat="crown", beard="none", hair="fringe", hair_col=(70, 45, 28), robe=(190, 150, 50), cloak=(160, 30, 40), skin=(226, 186, 150), bg=(170, 50, 50)),
 "vlad3": dict(hat="vladcap", beard="mustache", hair="curly_long", hair_col=(25, 20, 18), robe=(120, 25, 35), cloak=(200, 160, 60), skin=(225, 185, 150), eye=(70, 90, 70), nose=1.5, bg=(90, 30, 35)),
 "sonniali": dict(hat="turban", hat_col=(245, 242, 232), beard="short", hair="short", hair_col=(25, 20, 18), robe=(40, 50, 120), cloak=(230, 180, 60), skin=(105, 70, 48), bg=(180, 110, 50)),
 "ivan3": dict(hat="fur", hat_col=(220, 175, 60), beard="long", hair="long", hair_col=(110, 85, 60), beard_col=(120, 95, 70), robe=(170, 40, 40), cloak=(220, 180, 70), age=True, bg=(120, 140, 80)),
 "dias": dict(hat="cap", hat_col=(30, 30, 35), beard="full", hair="short", hair_col=(45, 32, 24), robe=(35, 35, 40), cloak=(80, 110, 70), skin=(222, 180, 145), bg=(50, 120, 80)),
 "zhenghe": dict(hat="wingcap", beard="none", hair="short", hair_col=(25, 20, 18), robe=(170, 40, 45), skin=(205, 160, 120), bg=(40, 90, 140)),
}

def get(who, size=210):
    return medallion(P[who], size=size)
