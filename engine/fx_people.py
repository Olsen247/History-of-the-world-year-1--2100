"""Stylised portrait medallions of historical people + boats for sea crossings."""
import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
SERIF_B = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
S = 3

def _beard(d, n, kind, col, cx, chin):
    if kind == "none": return
    if kind == "stubble":
        d.chord([cx - n*.17, chin - n*.16, cx + n*.17, chin + n*.03], 0, 180, fill=col[:3] + (110,)); return
    if kind == "goatee":   # 17th-century upturned mustache + small pointed chin beard (Gustavus Adolphus, Tasman)
        d.polygon([(cx - n*.10, chin - n*.10), (cx, chin - n*.115), (cx + n*.10, chin - n*.10), (cx + n*.06, chin - n*.085), (cx, chin - n*.10), (cx - n*.06, chin - n*.085)], fill=col)
        d.line([(cx - n*.095, chin - n*.10), (cx - n*.13, chin - n*.15)], fill=col, width=int(n*.018))
        d.line([(cx + n*.095, chin - n*.10), (cx + n*.13, chin - n*.15)], fill=col, width=int(n*.018))
        d.polygon([(cx - n*.04, chin - n*.04), (cx + n*.04, chin - n*.04), (cx, chin + n*.07)], fill=col); return
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
    if spec.get("lapels"):   # 18th-century coat: facings/lapels in a second colour, white stock/cravat (and gold epaulette lace)
        lc = spec["lapels"] + (255,)
        d.polygon([(cx - n*.10, n*.74), (cx - n*.26, n*.80), (cx - n*.20, n*1.0), (cx - n*.05, n*1.0)], fill=lc)
        d.polygon([(cx + n*.10, n*.74), (cx + n*.26, n*.80), (cx + n*.20, n*1.0), (cx + n*.05, n*1.0)], fill=lc)
        if spec.get("lace"):
            for sx in (-1, 1): d.line([(cx + sx*n*.22, n*.80), (cx + sx*n*.16, n*1.0)], fill=(230, 190, 70, 255), width=int(n*.014))
        d.polygon([(cx - n*.08, n*.70), (cx + n*.08, n*.70), (cx + n*.05, n*.84), (cx, n*.88), (cx - n*.05, n*.84)], fill=(250, 250, 246, 255))
    if spec.get("ruff"):   # Elizabethan millstone ruff / falling lace collar
        rc = (250, 250, 246, 255); rs = (200, 200, 196, 255)
        if spec["ruff"] == "lace":
            d.polygon([(cx - n*.24, n*.70), (cx + n*.24, n*.70), (cx + n*.30, n*.84), (cx, n*.88), (cx - n*.30, n*.84)], fill=rc, outline=rs)
        else:
            for k in range(13):
                a = math.pi * (k / 12); x = cx - math.cos(a) * n * .25; y = n * .72 + math.sin(a) * n * .045
                d.ellipse([x - n*.055, y - n*.045, x + n*.055, y + n*.045], fill=rc, outline=rs, width=int(n*.006))
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
    if hs == "wig":   # 18th-century powdered wig: smooth top, rolled side curls over the ears
        d.chord([cx - n*.205, top - n*.03, cx + n*.205, top + n*.24], 180, 360, fill=hair)
        d.rectangle([cx - n*.205, top + n*.10, cx - n*.18, top + n*.20], fill=hair); d.rectangle([cx + n*.18, top + n*.10, cx + n*.205, top + n*.20], fill=hair)
        hd = tuple(max(0, v - 40) for v in hair[:3]) + (255,)
        for sx in (-1, 1):
            for k in range(2):
                yy = n*.34 + k*n*.075
                d.ellipse([cx + sx*n*.215 - n*.065, yy - n*.035, cx + sx*n*.215 + n*.065, yy + n*.035], fill=hair, outline=hd, width=int(n*.008))
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
    elif hat == "hood":         # Dominican friar's black cowl drawn over the head (Savonarola)
        hc = spec.get("hat_col", (28, 26, 30)) + (255,)
        d.chord([cx - n*.27, top - n*.10, cx + n*.27, top + n*.50], 180, 360, fill=hc)
        d.rectangle([cx - n*.27, top + n*.19, cx - n*.19, n*.80], fill=hc); d.rectangle([cx + n*.19, top + n*.19, cx + n*.27, n*.80], fill=hc)
        d.chord([n*.10, n*.66, n*.90, n*1.35], 180, 360, fill=hc)
        d.polygon([(cx - n*.10, n*.70), (cx, n*.80), (cx + n*.10, n*.70)], fill=(235, 232, 225, 255))
    elif hat == "flatbonnet":   # wide flat late-15th-century bonnet with up-turned brim (+ gold badge)
        hc = spec.get("hat_col", (25, 25, 30)) + (255,)
        d.ellipse([cx - n*.30, top - n*.08, cx + n*.30, top + n*.10], fill=hc)
        d.rounded_rectangle([cx - n*.25, top + n*.00, cx + n*.25, top + n*.13], radius=n*.03, fill=hc)
        d.line([(cx - n*.25, top + n*.13), (cx + n*.25, top + n*.13)], fill=tuple(min(255, v + 40) for v in hc[:3]) + (255,), width=int(n*.012))
        if spec.get("badge"): d.ellipse([cx + n*.08, top + n*.01, cx + n*.15, top + n*.08], fill=gold, outline=gdk)
    elif hat == "taj":          # Safavid Qizilbash taj: white turban wound round a tall red twelve-gored baton
        d.polygon([(cx - n*.07, top - n*.02), (cx + n*.07, top - n*.02), (cx + n*.035, top - n*.40), (cx - n*.035, top - n*.40)], fill=(200, 35, 40, 255), outline=(120, 20, 25, 255))
        for k in range(3): d.line([(cx - n*.06 + k*n*.04, top - n*.04), (cx - n*.03 + k*n*.03, top - n*.38)], fill=(150, 25, 30, 255), width=int(n*.006))
        tc = (248, 246, 238, 255); sh = (200, 196, 186, 255)
        d.ellipse([cx - n*.27, top - n*.12, cx + n*.27, top + n*.18], fill=tc, outline=sh, width=int(n*.01))
        for k in range(3): d.arc([cx - n*.26, top - n*.09 + k*n*.06, cx + n*.26, top + n*.19 + k*n*.06], 200, 340, fill=sh, width=int(n*.01))
        if spec.get("jewel"): d.ellipse([cx - n*.03, top - n*.02, cx + n*.03, top + n*.04], fill=(220, 40, 60, 255))
    elif hat == "plumebonnet":  # 16th-century flat velvet bonnet worn tilted, with a white ostrich plume (Francis I, Pizarro)
        hc = spec.get("hat_col", (25, 25, 30)) + (255,)
        d.ellipse([cx - n*.32, top - n*.06, cx + n*.28, top + n*.12], fill=hc)
        d.rounded_rectangle([cx - n*.24, top + n*.02, cx + n*.22, top + n*.14], radius=n*.03, fill=hc)
        d.ellipse([cx + n*.06, top - n*.16, cx + n*.40, top + n*.02], fill=(248, 248, 244, 255), outline=(200, 200, 196, 255), width=int(n*.008))
        if spec.get("badge"): d.ellipse([cx - n*.02, top + n*.03, cx + n*.05, top + n*.10], fill=gold, outline=gdk)
    elif hat == "suleimanturban":  # Suleiman's very tall, bulbous white ceremonial turban with a jewelled aigrette
        tc = (250, 248, 242, 255); sh = (205, 200, 190, 255)
        d.ellipse([cx - n*.27, top - n*.42, cx + n*.27, top + n*.18], fill=tc, outline=sh, width=int(n*.01))
        for k in range(5): d.arc([cx - n*.26, top - n*.38 + k*n*.10, cx + n*.26, top - n*.02 + k*n*.06], 200, 340, fill=sh, width=int(n*.009))
        d.ellipse([cx - n*.035, top - n*.12, cx + n*.035, top - n*.05], fill=(200, 40, 60, 255), outline=gold)
        d.line([(cx, top - n*.12), (cx + n*.06, top - n*.32)], fill=(30, 30, 35, 255), width=int(n*.018))
    elif hat == "morion":       # Spanish conquistador morion: steel dome with high comb and up-curved brim
        mc = (190, 192, 200, 255); md = (100, 102, 112, 255)
        d.chord([cx - n*.19, top - n*.10, cx + n*.19, top + n*.24], 180, 360, fill=mc, outline=md, width=int(n*.008))
        d.chord([cx - n*.06, top - n*.22, cx + n*.06, top + n*.04], 180, 360, fill=mc, outline=md, width=int(n*.008))
        d.polygon([(cx - n*.34, top + n*.02), (cx - n*.20, top + n*.10), (cx + n*.20, top + n*.10), (cx + n*.34, top + n*.02), (cx + n*.30, top + n*.12), (cx - n*.30, top + n*.12)], fill=mc, outline=md)
    elif hat == "monomakh":     # Cap of Monomakh: gold filigree dome with sable fur rim, jewels and a small cross on top
        d.chord([cx - n*.19, top - n*.16, cx + n*.19, top + n*.22], 180, 360, fill=gold, outline=gdk, width=int(n*.01))
        for k in range(5): x = cx - n*.14 + k*n*.07; d.line([(x, top + n*.03), (cx, top - n*.15)], fill=gdk, width=int(n*.006))
        for k, gc in enumerate([(200, 30, 50), (40, 140, 70), (40, 80, 180)]): x = cx - n*.08 + k*n*.08; d.ellipse([x - n*.02, top - n*.04, x + n*.02, top], fill=gc + (255,))
        d.rounded_rectangle([cx - n*.235, top + n*.02, cx + n*.235, top + n*.15], radius=n*.05, fill=(70, 50, 35, 255))
        for k in range(10): x = cx - n*.21 + k*n*.047; d.line([(x, top + n*.03), (x + n*.01, top + n*.14)], fill=(45, 32, 22, 255), width=int(n*.006))
        d.line([(cx, top - n*.16), (cx, top - n*.27)], fill=gold, width=int(n*.016)); d.line([(cx - n*.04, top - n*.225), (cx + n*.04, top - n*.225)], fill=gold, width=int(n*.016))
    elif hat == "eboshi":       # tall black lacquered Japanese court cap (formal portraits of Tokugawa Ieyasu)
        hc = (22, 22, 26, 255)
        d.polygon([(cx - n*.17, top + n*.08), (cx + n*.17, top + n*.08), (cx + n*.12, top - n*.30), (cx - n*.06, top - n*.34), (cx - n*.15, top - n*.10)], fill=hc)
        d.chord([cx - n*.205, top - n*.02, cx + n*.205, top + n*.24], 180, 360, fill=hc)
    elif hat == "smallcrown":   # small jewelled crown set on top of curled hair (Elizabeth I)
        d.rectangle([cx - n*.12, top - n*.06, cx + n*.12, top + n*.02], fill=gold, outline=gdk)
        for k in range(4): x = cx - n*.12 + k*n*.08; d.polygon([(x, top - n*.06), (x + n*.04, top - n*.14), (x + n*.08, top - n*.06)], fill=gold, outline=gdk)
        for k in range(5): x = cx - n*.10 + k*n*.05; d.ellipse([x - n*.012, top - n*.045, x + n*.012, top - n*.02], fill=(250, 248, 240, 255))
    elif hat == "mughalturban": # Shah Jahan: gold-striped turban with jewelled sarpech and a feather aigrette
        tc = (238, 220, 170, 255); sh = (190, 150, 70, 255)
        d.ellipse([cx - n*.25, top - n*.14, cx + n*.25, top + n*.18], fill=tc, outline=sh, width=int(n*.01))
        for k in range(4): d.arc([cx - n*.24, top - n*.11 + k*n*.06, cx + n*.24, top + n*.19 + k*n*.06], 200, 340, fill=sh, width=int(n*.01))
        d.ellipse([cx - n*.04, top - n*.06, cx + n*.04, top + n*.03], fill=(200, 30, 50, 255), outline=gold, width=int(n*.01))
        d.line([(cx, top - n*.06), (cx + n*.05, top - n*.30)], fill=(30, 30, 35, 255), width=int(n*.02))
        for k in range(5): d.ellipse([cx - n*.20 + k*n*.10 - n*.012, n*.80, cx - n*.20 + k*n*.10 + n*.012, n*.83], fill=(250, 248, 240, 255))
    elif hat == "bicorne":      # Napoleon's black bicorne worn sideways ("en bataille"), small tricolour cockade
        hc = (22, 22, 26, 255)
        d.chord([cx - n*.34, top - n*.22, cx + n*.34, top + n*.24], 180, 360, fill=hc)
        d.rectangle([cx - n*.34, top + n*.0, cx + n*.34, top + n*.06], fill=hc)
        for k, cc in enumerate([(40, 70, 170), (245, 245, 240), (200, 30, 40)]):
            r = n * (.055 - k * .017); d.ellipse([cx + n*.22 - r, top - n*.07 - r, cx + n*.22 + r, top - n*.07 + r], fill=cc + (255,))
    elif hat == "bicorne_fa":   # naval bicorne worn fore-and-aft, gold lace edge (Nelson); optional plume
        hc = (22, 22, 26, 255)
        d.polygon([(cx - n*.22, top + n*.08), (cx + n*.22, top + n*.08), (cx + n*.10, top - n*.24), (cx - n*.10, top - n*.24)], fill=hc, outline=gold, width=int(n*.012))
        if spec.get("plume"): d.ellipse([cx - n*.18, top - n*.36, cx + n*.18, top - n*.18], fill=spec["plume"] + (255,))
    elif hat == "tricorne":     # black three-cornered hat with gold lace edge
        hc = spec.get("hat_col", (25, 25, 30)) + (255,)
        d.polygon([(cx - n*.32, top + n*.08), (cx + n*.32, top + n*.08), (cx + n*.20, top - n*.14), (cx, top - n*.04), (cx - n*.20, top - n*.14)], fill=hc, outline=gold, width=int(n*.012))
    elif hat == "kolah":        # Nader Shah's kolah-e Naderi: tall red four-peaked cap wound with a white shawl-turban, jewelled aigrette
        d.polygon([(cx - n*.13, top + n*.04), (cx + n*.13, top + n*.04), (cx + n*.10, top - n*.30), (cx + n*.04, top - n*.24), (cx, top - n*.34), (cx - n*.04, top - n*.24), (cx - n*.10, top - n*.30)], fill=(190, 30, 40, 255), outline=gdk)
        d.ellipse([cx - n*.25, top - n*.06, cx + n*.25, top + n*.16], fill=(245, 240, 225, 255), outline=(200, 190, 170, 255), width=int(n*.01))
        for k in range(3): d.arc([cx - n*.24, top - n*.04 + k*n*.05, cx + n*.24, top + n*.16 + k*n*.05], 200, 340, fill=(200, 160, 80, 255), width=int(n*.008))
        d.ellipse([cx - n*.04, top - n*.06, cx + n*.04, top + n*.02], fill=(30, 140, 80, 255), outline=gold, width=int(n*.01))
        d.line([(cx, top - n*.06), (cx - n*.06, top - n*.26)], fill=(245, 245, 245, 255), width=int(n*.02))
    elif hat == "kalpak":       # Polish fur kołpak with jewelled clasp and heron-feather plume (Jan III Sobieski)
        hc = spec.get("hat_col", (110, 30, 40)) + (255,)
        d.rounded_rectangle([cx - n*.17, top - n*.16, cx + n*.17, top + n*.06], radius=n*.06, fill=hc)
        d.rounded_rectangle([cx - n*.22, top - n*.02, cx + n*.22, top + n*.10], radius=n*.05, fill=(70, 50, 38, 255))
        d.ellipse([cx - n*.035, top - n*.03, cx + n*.035, top + n*.04], fill=gold, outline=gdk)
        d.line([(cx, top - n*.02), (cx + n*.08, top - n*.34)], fill=(245, 245, 245, 255), width=int(n*.024))
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
 # Ep 12
 "askia": dict(hat="turban", hat_col=(248, 246, 238), beard="short", hair="short", hair_col=(25, 20, 18), robe=(30, 60, 130), cloak=(240, 238, 230), skin=(100, 66, 45), bg=(190, 120, 50)),
 "charles8": dict(hat="flatbonnet", badge=True, beard="none", hair="long", hair_col=(140, 95, 50), robe=(30, 50, 140), cloak=(230, 190, 70), skin=(232, 196, 165), nose=1.9, eye=(70, 90, 120), bg=(50, 80, 160)),
 "savonarola": dict(hat="hood", beard="none", hair="none", robe=(28, 26, 30), skin=(205, 165, 130), nose=2.0, eye=(40, 30, 25), age=True, bg=(110, 40, 30)),
 "cabot": dict(hat="cap", hat_col=(150, 30, 40), beard="full", hair="short", hair_col=(60, 45, 30), beard_col=(70, 50, 35), robe=(40, 40, 50), cloak=(140, 30, 40), skin=(225, 185, 150), bg=(170, 50, 60)),
 "dagama": dict(hat="flatbonnet", beard="long", hair="short", hair_col=(35, 28, 22), beard_col=(40, 32, 25), robe=(25, 25, 30), cloak=(170, 40, 40), skin=(222, 180, 145), nose=1.3, bg=(40, 110, 80)),
 # Ep 13
 "cabral": dict(hat="cap", hat_col=(25, 25, 30), beard="full", hair="short", hair_col=(40, 30, 22), beard_col=(45, 32, 24), armor=(170, 172, 180), cloak=(40, 110, 80), skin=(222, 180, 145), nose=1.3, bg=(40, 110, 80)),
 "ismail": dict(hat="taj", jewel=True, beard="mustache", hair="short", hair_col=(120, 70, 35), beard_col=(120, 70, 35), robe=(40, 120, 90), cloak=(220, 180, 70), skin=(226, 186, 150), bg=(40, 130, 100)),
 "albuquerque": dict(hat="cap", hat_col=(25, 25, 30), beard="long", hair="short", hair_col=(215, 215, 210), beard_col=(235, 235, 230), robe=(30, 30, 35), cloak=(150, 30, 40), skin=(222, 180, 145), age=True, nose=1.4, bg=(40, 110, 80)),
 "balboa": dict(hat="morion", beard="full", hair="short", hair_col=(110, 75, 40), beard_col=(120, 80, 45), armor=(175, 178, 186), cloak=(170, 40, 40), skin=(226, 186, 150), bg=(170, 110, 50)),
 "selim": dict(hat="bigturban", beard="mustache", hair="none", beard_col=(40, 28, 20), robe=(150, 30, 40), cloak=(220, 180, 70), skin=(210, 165, 125), nose=1.5, eye=(40, 30, 25), bg=(170, 40, 45)),
 "magellan": dict(hat="none", beard="full", hair="short", hair_col=(35, 28, 22), beard_col=(40, 32, 25), armor=(165, 168, 178), cloak=(30, 30, 35), skin=(222, 180, 145), nose=1.3, bg=(170, 110, 50)),
 "cortes": dict(hat="cap", hat_col=(25, 25, 30), beard="short", hair="short", hair_col=(55, 40, 28), beard_col=(60, 45, 30), armor=(175, 178, 186), cloak=(150, 30, 40), skin=(226, 186, 150), bg=(170, 110, 50)),
 "elcano": dict(hat="cap", hat_col=(40, 30, 25), beard="short", hair="short", hair_col=(60, 45, 30), beard_col=(70, 50, 35), robe=(40, 40, 50), cloak=(160, 120, 50), skin=(222, 180, 145), bg=(50, 90, 140)),
 "zhenghe": dict(hat="wingcap", beard="none", hair="short", hair_col=(25, 20, 18), robe=(170, 40, 45), skin=(205, 160, 120), bg=(40, 90, 140)),
 # Ep 14
 "gustav": dict(hat="flatbonnet", hat_col=(25, 25, 30), beard="long", hair="short", hair_col=(150, 110, 70), beard_col=(165, 125, 80), robe=(30, 30, 35), cloak=(40, 80, 170), skin=(228, 190, 158), age=True, bg=(40, 80, 160)),
 "charlesv": dict(hat="flatbonnet", hat_col=(20, 20, 24), beard="short", hair="fringe", hair_col=(95, 70, 40), beard_col=(100, 75, 45), armor=(170, 172, 180), cloak=(30, 30, 35), skin=(230, 192, 160), nose=1.4, bg=(180, 150, 60)),
 "francis": dict(hat="plumebonnet", hat_col=(25, 25, 30), badge=True, beard="full", hair="short", hair_col=(45, 32, 24), beard_col=(50, 36, 26), robe=(240, 236, 226), cloak=(40, 70, 170), skin=(226, 186, 150), nose=1.8, bg=(50, 80, 160)),
 "babur": dict(hat="turban", hat_col=(245, 242, 232), jewel=True, beard="short", hair="short", hair_col=(30, 24, 20), beard_col=(35, 28, 22), robe=(40, 140, 90), cloak=(210, 170, 70), skin=(212, 168, 128), bg=(40, 130, 90)),
 "suleiman": dict(hat="suleimanturban", beard="mustache", hair="none", beard_col=(50, 36, 26), robe=(170, 40, 45), cloak=(220, 180, 70), skin=(215, 172, 132), nose=1.7, eye=(40, 30, 25), bg=(170, 40, 45)),
 "atahualpa": dict(hat="mascaypacha", beard="none", hair="short", hair_col=(25, 20, 18), robe=(40, 120, 150), cloak=(200, 150, 50), skin=(175, 120, 85), bg=(190, 120, 40)),
 # Ep 15
 "ivan4": dict(hat="monomakh", beard="long", hair="long", hair_col=(60, 40, 25), beard_col=(70, 45, 28), robe=(150, 30, 40), cloak=(220, 180, 70), skin=(222, 180, 145), nose=1.7, eye=(40, 30, 25), bg=(120, 40, 40)),
 "elizabeth": dict(female=True, hat="smallcrown", hair="curly", hair_col=(200, 90, 40), ruff="millstone", robe=(30, 30, 40), cloak=(150, 30, 40), skin=(245, 225, 210), nose=1.3, bg=(160, 40, 50)),
 "ieyasu": dict(hat="eboshi", beard="mustache", hair="short", hair_col=(25, 22, 20), beard_col=(35, 30, 26), robe=(40, 40, 50), cloak=(190, 170, 120), skin=(220, 185, 150), age=True, bg=(150, 40, 40)),
 "gustavus": dict(beard="goatee", hair="short", hair_col=(170, 130, 70), beard_col=(175, 135, 75), armor=(150, 152, 160), ruff="lace", cloak=(40, 80, 170), skin=(232, 196, 165), eye=(70, 110, 160), bg=(40, 80, 160)),
 "shahjahan": dict(hat="mughalturban", beard="full", hair="short", hair_col=(30, 24, 20), beard_col=(30, 24, 20), robe=(240, 236, 220), cloak=(60, 140, 90), skin=(200, 155, 115), nose=1.4, bg=(40, 130, 90)),
 "tasman": dict(beard="goatee", hair="long", hair_col=(45, 32, 24), beard_col=(50, 36, 26), robe=(25, 25, 30), ruff="lace", skin=(226, 186, 150), bg=(220, 120, 40)),
 "pizarro": dict(hat="plumebonnet", hat_col=(25, 25, 30), beard="long", hair="short", hair_col=(150, 145, 140), beard_col=(185, 180, 172), armor=(175, 178, 186), cloak=(150, 30, 40), skin=(222, 180, 145), age=True, nose=1.4, bg=(170, 110, 50)),
 # Ep 16
 "cook": dict(hair="wig", hair_col=(225, 222, 215), beard="none", robe=(25, 40, 90), lapels=(240, 236, 226), lace=True, skin=(230, 192, 160), nose=1.3, eye=(70, 100, 130), bg=(40, 70, 130)),
 "sobieski": dict(hat="kalpak", hat_col=(150, 30, 40), beard="mustache", hair="short", hair_col=(60, 42, 28), beard_col=(60, 42, 28), robe=(150, 30, 40), cloak=(220, 180, 70), armor=(175, 178, 186), skin=(228, 186, 150), nose=1.2, bg=(170, 40, 50)),
 "peter1": dict(hair="curly", hair_col=(40, 28, 20), beard="mustache", beard_col=(40, 28, 20), armor=(170, 172, 180), cloak=(60, 120, 70), skin=(230, 192, 160), eye=(40, 30, 25), bg=(60, 110, 70)),
 "nader": dict(hat="kolah", beard="full", hair="short", hair_col=(30, 24, 20), beard_col=(35, 28, 22), robe=(150, 30, 40), cloak=(220, 180, 70), skin=(205, 160, 120), nose=1.5, eye=(35, 28, 22), bg=(60, 130, 100)),
 "clive": dict(hair="wig", hair_col=(200, 196, 188), beard="none", robe=(190, 30, 40), lapels=(30, 50, 110), lace=True, skin=(232, 196, 165), nose=1.3, bg=(170, 40, 50)),
 "wolfe": dict(hat="tricorne", hair="wig", hair_col=(200, 120, 70), beard="none", robe=(190, 30, 40), lapels=(30, 40, 90), skin=(236, 205, 180), nose=1.6, bg=(170, 40, 50)),
 # Ep 17
 "washington": dict(hair="wig", hair_col=(230, 228, 222), beard="none", robe=(30, 45, 100), lapels=(220, 195, 140), lace=True, skin=(232, 196, 168), nose=1.4, eye=(80, 100, 120), age=True, bg=(40, 70, 140)),
 "catherine": dict(female=True, hat="smallcrown", hair="wig", hair_col=(215, 210, 200), robe=(240, 236, 226), cloak=(60, 110, 160), skin=(242, 214, 196), bg=(60, 110, 160)),
 "pugachev": dict(hat="fur", hat_col=(60, 45, 35), beard="full", hair="short", hair_col=(40, 28, 20), beard_col=(40, 28, 20), robe=(150, 30, 40), skin=(220, 178, 140), eye=(35, 28, 22), bg=(120, 70, 40)),
 "jefferson": dict(hair="wig", hair_col=(200, 120, 80), beard="none", robe=(60, 45, 35), lapels=(70, 55, 42), skin=(236, 205, 180), nose=1.3, eye=(80, 110, 120), bg=(70, 90, 130)),
 # Ep 18
 "napoleon": dict(hat="bicorne", hair="short", hair_col=(60, 42, 28), beard="none", robe=(30, 45, 110), lapels=(240, 236, 226), lace=True, skin=(236, 206, 182), nose=1.3, eye=(90, 110, 130), bg=(40, 70, 150)),
 "napoleon_emp": dict(hat="laurel", hair="short", hair_col=(60, 42, 28), beard="none", robe=(150, 25, 40), cloak=(245, 242, 235), skin=(236, 206, 182), nose=1.3, eye=(90, 110, 130), bg=(150, 30, 45)),
 "nelson": dict(hat="bicorne_fa", hair="wig", hair_col=(225, 222, 215), beard="none", robe=(25, 35, 80), lapels=(240, 236, 226), lace=True, skin=(232, 198, 172), nose=1.5, eye=(80, 100, 120), bg=(30, 60, 120)),
 "phillip": dict(hair="wig", hair_col=(220, 218, 210), beard="none", robe=(25, 40, 90), lapels=(240, 236, 226), skin=(230, 192, 160), nose=1.6, eye=(70, 90, 110), age=True, bg=(40, 90, 130)),
 "dessalines": dict(hat="bicorne_fa", plume=(200, 30, 40), hair="short", hair_col=(25, 20, 18), beard="none", robe=(30, 45, 110), lapels=(200, 30, 40), lace=True, skin=(105, 70, 48), eye=(35, 28, 22), bg=(40, 50, 140)),
 "kutuzov": dict(hair="short", hair_col=(225, 222, 215), beard="none", robe=(30, 70, 45), lapels=(200, 40, 40), lace=True, skin=(232, 196, 168), nose=1.4, eye=(70, 90, 110), age=True, bg=(60, 110, 70)),
}

def get(who, size=210):
    return medallion(P[who], size=size)
