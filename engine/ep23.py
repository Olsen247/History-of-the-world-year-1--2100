"""Episode 23 – Year 1916: the First World War, part 2 (how trench warfare worked).
Christmas truce (Dec 1914), chlorine gas at Ypres (22 Apr 1915), Gallipoli landings (25 Apr 1915), Lusitania (7 May 1915),
the Armenian genocide (from 1915), Verdun (21 Feb - 18 Dec 1916) and the Sacred Way, Jutland (31 May 1916),
the first day of the Somme (1 Jul 1916) and the first tanks at Flers-Courcelette (15 Sep 1916), the Somme ends (18 Nov 1916)."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1916)
import world_data_1914w as A, world_data_1916 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep23/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (8.0, 49.0, 2400)
shots = [(3.6, 49.9, 380), WIDE, (3.2, 50.4, 380), (3.0, 50.6, 320), (26.6, 40.3, 220), (-9.5, 51.0, 420), (38.8, 37.8, 650),
         (4.6, 49.0, 380), (4.6, 48.9, 380), (3.0, 56.4, 560), (3.6, 49.9, 380), (3.4, 50.0, 340), (12.0, 48.0, 2600)]
EXTRA = {}
endshot = list(shots)
keys = [(0.0, 3.6, 49.9, 520), (3.0, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW = s[7] - 0.85
reveals = []

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); GRN = (150, 215, 110)
DEC = (110, 110, 122); FRC = (60, 95, 200); BRC = (235, 125, 165); OTC = (200, 60, 60)
labels = [
    # hook: the Somme
    ev("THE SOMME", (6.0, 50.7), 0.4, en[0] + 0.2),
    # Christmas truce
    ev("YPRES", (0.7, 50.95), s[2] + 0.4, en[2] + 0.2, WT),
    # gas
    ev("YPRES", (1.0, 50.7), s[3] + 0.3, en[3] + 0.2, WT), ev("CHLORINE", (1.9, 51.4), s[3] + 1.2, en[3] + 0.2, GRN),
    # Gallipoli
    ev("GALLIPOLI", (27.4, 41.05), s[4] + 0.3, en[4] + 0.2), lb("OTTOMAN EMPIRE", (29.6, 39.7), s[4] + 0.3, s[4] + 3.2, OTC),
    # Lusitania
    ev("LUSITANIA", (-10.6, 49.6), s[5] + 2.6, en[5] + 0.2), lb("IRELAND", (-7.9, 53.1), s[5] + 0.3, en[5] + 0.2, BRC),
    # Armenian genocide
    lb("OTTOMAN EMPIRE", (32.5, 39.2), s[6] + 0.3, en[6] + 0.2, OTC), ev("ARMENIANS", (42.6, 41.3), s[6] + 0.4, en[6] + 0.2, WT),
    ev("ALEPPO", (35.2, 36.2), s[6] + 2.4, en[6] + 0.2, WT), ev("SYRIAN DESERT", (40.5, 34.1), s[6] + 2.8, en[6] + 0.2),
    # Verdun
    ev("VERDUN", (3.3, 48.45), s[7] + 0.4, en[8] + 0.2),
    ev("THE SACRED WAY", (2.3, 47.85), s[8] + 1.0, en[8] + 0.2),
    # Jutland
    ev("JUTLAND", (5.6, 58.4), s[9] + 1.8, en[9] + 0.2), ev("NORTH SEA", (3.0, 55.9), s[9] + 0.3, en[9] + 0.2, CYN),
    lb("BRITAIN", (-4.6, 57.7), s[9] + 0.3, en[9] + 0.2, BRC),
    # Somme
    ev("THE SOMME", (6.0, 50.7), s[10] + 0.3, en[11] + 0.2),
]
labels += WP.labels(A, 1915, s[1] + 0.8, SW)
labels += WP.labels(B, 1916, SW + 0.6, s[12])

ticker = [(0, 1916), (s[1], 1916), (s[1] + 1.3, 1914), (s[3], 1914), (s[3] + 0.6, 1915), (s[7], 1915), (s[7] + 0.6, 1916), (DUR, 1916)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1916", l2="BRITAIN'S BLOODIEST DAY", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1914", GOLD), hd(2, "CHRISTMAS 1914", "THE TRUCE", GOLD), hd(3, "APRIL 1915", "POISON GAS", GRN),
            hd(4, "APRIL 1915", "GALLIPOLI"), hd(5, "MAY 1915", "LUSITANIA", CYN), hd(6, "YEAR 1915", "ARMENIAN GENOCIDE", WT),
            hd(7, "FEBRUARY 1916", "VERDUN"), hd(8, "VERDUN", "303 DAYS", GOLD), hd(9, "MAY 1916", "JUTLAND", CYN),
            hd(10, "JULY 1916", "THE SOMME"), hd(11, "SEPTEMBER 1916", "THE FIRST TANKS", GOLD)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)

# The whole Western Front (Dec 1914 - 1916), drawn at true scale; battles are marked on it.
WF = [(2.75, 51.13), (2.88, 50.93), (3.0, 50.84), (2.88, 50.69), (2.8, 50.45), (2.82, 50.29), (2.67, 50.14), (2.7, 50.0), (2.85, 49.9),
      (2.8, 49.7), (2.92, 49.55), (3.35, 49.42), (4.05, 49.32), (4.9, 49.2), (5.3, 49.27), (5.58, 49.1), (5.55, 48.9), (6.05, 48.9),
      (6.7, 48.55), (7.0, 48.2), (7.15, 47.5)]
def wf(**chg):
    p = list(WF)
    for i, v in chg.items(): p[int(i[1:])] = v
    return p
WF_GAS = wf(i1=(2.87, 50.89))                                   # 22 Apr 1915: the salient pushed in from the north
WF_VD = wf(i1=(2.87, 50.89), i14=(5.38, 49.22), i15=(5.55, 49.12))   # Feb 1916: Germans take Douaumont
WF_SM = wf(i1=(2.87, 50.89), i14=(5.38, 49.22), i15=(5.55, 49.12), i7=(2.82, 50.05), i8=(2.93, 49.93))   # Nov 1916: the Somme bulge, ~10 km
WF_AL = ["be"] + ["uk"] * 7 + ["fr"] * 12
FR = lambda p0, p1, a, b, m0=1e9, m1=1e9: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1, side_a=["de1914"],
                                              side_b=WF_AL, by_segment=True, rows=2, scale=0.8)
CANDLES = [(3.6, 51.0, .6), (3.75, 50.8, .55), (3.6, 50.58, .6), (3.55, 50.35, .55), (3.5, 50.12, .6), (3.45, 49.9, .55), (3.55, 49.65, .55)]
SACRED = [(5.16, 48.77), (5.2, 48.86), (5.24, 48.94), (5.29, 49.03), (5.34, 49.1), (5.38, 49.16)]
KH = (150, 130, 90); BRK = (190, 170, 120); OTK = (200, 60, 60)
fx = [
    # hook: the Somme, 1 July 1916
    FR(WF, WF, 0.3, en[0] + 0.3),
    BM((2.76, 50.06), 0.6), BM((2.82, 49.99), 1.3), BM((2.73, 50.12), 2.0), BM((2.85, 50.05), 2.8, 0.36),
    dict(type="glow", pos=(2.7, 50.05), t0=3.0, t1=en[0], radius=260, a0=40, a1=110),
    # Christmas 1914: the truce – candles along the German parapets
    FR(WF, WF_GAS, s[2], en[3] + 0.2, s[3] + 3.4, s[3] + 5.4),
    dict(type="cities", cities=CANDLES, t0=s[2] + 1.0, t1=s[2] + 2.6, until=en[2] + 0.2, color=(255, 205, 120)),
    # April 1915: chlorine at Ypres
    dict(type="gas", line=[(2.82, 50.97), (2.9, 50.96), (2.98, 50.94)], drift=(-0.12, -0.16), t0=s[3] + 0.8, t1=s[3] + 4.6, until=en[3] + 0.3, puffs=80),
    # Gallipoli: landings at Anzac Cove and Cape Helles, Ottoman reinforcements on the heights
    VH("warship", [(25.25, 39.87), (25.7, 40.0), (26.05, 40.12)], s[4] + 0.4, s[4] + 2.4, until=en[4] + 0.2, scale=0.8),
    VH("warship", [(25.25, 39.8), (25.7, 39.85), (26.05, 39.98)], s[4] + 0.6, s[4] + 2.6, until=en[4] + 0.2, scale=0.8),
    M_([(25.6, 40.2), (26.1, 40.24), (26.28, 40.24)], s[4] + 0.6, s[4] + 3.0, KH, kind="anzac", soldiers=5, until=en[4] + 0.2),
    M_([(25.7, 39.95), (26.1, 40.03), (26.19, 40.06)], s[4] + 0.8, s[4] + 3.2, BRK, kind="tommy", soldiers=5, until=en[4] + 0.2),
    M_([(26.7, 40.45), (26.5, 40.32), (26.36, 40.26)], s[4] + 2.6, s[4] + 4.6, OTK, kind="ottoman1912", soldiers=6, ships=False, until=en[4] + 0.2),
    BM((26.3, 40.25), s[4] + 3.2, 0.28), BM((26.22, 40.08), s[4] + 3.6, 0.28),
    PP("kemal", "MUSTAFA KEMAL", "OTTOMAN DIVISION COMMANDER", s[4] + 3.4, en[4] + 0.2),
    # Lusitania, 7 May 1915, off the Old Head of Kinsale
    VH("steamer", [(-20.0, 50.2), (-15.0, 50.7), (-11.0, 51.2), (-8.6, 51.4)], s[5] + 0.3, s[5] + 2.6, until=s[5] + 3.3, scale=1.1),
    VH("submarine", [(-8.0, 50.7), (-8.3, 51.0), (-8.5, 51.25)], s[5] + 0.6, s[5] + 2.4, until=en[5] + 0.2),
    BM((-8.6, 51.4), s[5] + 2.5, 0.4),
    # Armenian genocide: deportation routes to the Syrian desert (drawn as routes below, no soldiers, no blasts)
    # Verdun, 21 Feb 1916: over 1,200 guns, the front pushed back to Douaumont
    FR(WF_GAS, WF_VD, s[7] + 0.2, en[8] + 0.2, s[7] + 2.0, s[7] + 5.0),
    BM((5.33, 49.3), s[7] + 0.6, 0.26), BM((5.45, 49.25), s[7] + 1.0, 0.3), BM((5.55, 49.18), s[7] + 1.5, 0.26), BM((5.25, 49.3), s[7] + 2.1, 0.28),
    BM((5.44, 49.215), s[7] + 3.4, 0.32), BM((5.38, 49.28), s[7] + 4.3, 0.26),
    PP("falkenhayn", "ERICH VON FALKENHAYN", "GERMAN CHIEF OF STAFF", s[7] + 2.4, en[7] + 0.2, x=300),
    # the Sacred Way: trucks day and night from Bar-le-Duc
    *[VH("truck", SACRED, s[8] + 0.3 + 1.1 * k, s[8] + 3.6 + 1.1 * k, until=en[8] + 0.2, route=(k == 0), scale=0.75) for k in range(3)],
    PP("petain", "PHILIPPE PÉTAIN", "DEFENDER OF VERDUN", s[8] + 0.4, en[8] + 0.2, x=780),
    # Jutland, 31 May 1916
    VH("warship", [(-3.0, 58.85), (-1.0, 58.4), (2.0, 57.6), (4.6, 57.1), (5.6, 56.95)], s[9] + 0.3, s[9] + 3.2, until=en[9] + 0.2),
    VH("warship", [(-3.3, 56.02), (-1.5, 56.25), (1.5, 56.6), (4.4, 56.75), (5.5, 56.75)], s[9] + 0.4, s[9] + 3.0, until=en[9] + 0.2),
    VH("warship", [(8.1, 53.6), (7.6, 54.6), (7.0, 55.6), (6.5, 56.4), (6.1, 56.8)], s[9] + 0.5, s[9] + 3.2, until=en[9] + 0.2),
    VH("warship", [(7.9, 54.1), (7.2, 55.3), (6.6, 56.2), (6.3, 56.55)], s[9] + 0.6, s[9] + 3.0, until=en[9] + 0.2, scale=0.85),
    BM((5.9, 56.85), s[9] + 3.0, 0.4), BM((6.15, 56.6), s[9] + 3.6, 0.34), BM((5.7, 56.7), s[9] + 4.4, 0.34),
    PP("jellicoe", "JOHN JELLICOE", "BRITISH GRAND FLEET", s[9] + 0.6, en[9] + 0.2, x=300),
    PP("scheer", "REINHARD SCHEER", "GERMAN HIGH SEAS FLEET", s[9] + 1.2, en[9] + 0.2, x=780),
    # the Somme: a week of shelling, then the walk into the machine guns (1 July); tanks at Flers (15 Sep); the line of 18 Nov
    FR(WF_VD, WF_VD, s[10], en[10] + 0.1),
    *[BM(p, s[10] + 0.4 + 0.45 * k, 0.26) for k, p in enumerate([(2.82, 50.1), (2.86, 50.03), (2.9, 50.0), (2.8, 50.07), (2.95, 49.97), (2.84, 50.13)])],
    dict(type="glow", pos=(2.7, 50.05), t0=s[10] + 3.4, t1=en[10], radius=240, a0=40, a1=110),
    PP("haig", "DOUGLAS HAIG", "BRITISH COMMANDER", s[10] + 0.4, en[10] + 0.2, x=300),
    FR(WF_VD, WF_SM, en[10] + 0.1, DUR, s[11] + 1.0, s[11] + 5.4),
    VH("tank1916", [(2.79, 49.99), (2.81, 50.04), (2.83, 50.07)], s[11] + 0.4, s[11] + 3.2, until=en[11] + 0.2),
    VH("tank1916", [(2.73, 50.0), (2.75, 50.05), (2.77, 50.08)], s[11] + 0.6, s[11] + 3.4, until=en[11] + 0.2),
    VH("tank1916", [(2.85, 49.97), (2.87, 50.02), (2.88, 50.05)], s[11] + 0.8, s[11] + 3.6, until=en[11] + 0.2),
    VH("plane", [(2.55, 49.95), (2.75, 50.02), (2.95, 50.1)], s[11] + 1.0, s[11] + 3.6, scale=0.9),
]
ARM = (215, 200, 190)
routes = [dict(pts=[(41.27, 39.9), (39.5, 39.75), (39.25, 38.7), (38.8, 37.15), (37.16, 36.2)], t0=s[6] + 0.6, t1=s[6] + 3.2, until=en[6] + 0.2, color=ARM),
          dict(pts=[(43.38, 38.5), (42.1, 38.4), (40.22, 37.91), (40.74, 37.31), (40.07, 36.85), (40.14, 35.33)], t0=s[6] + 0.8, t1=s[6] + 3.6, until=en[6] + 0.2, color=ARM),
          dict(pts=[(37.02, 39.75), (38.31, 38.35), (37.38, 37.07), (37.16, 36.2), (39.0, 35.95), (40.14, 35.33)], t0=s[6] + 1.0, t1=s[6] + 4.0, until=en[6] + 0.2, color=ARM)]

def vig(t):
    if t < en[0] + 0.3 or t > s[12] + 0.2: return 1.0
    return 0.6

def outro(fr, t):
    t0 = s[12] + 0.3
    if t < t0: return
    lt = t - t0
    dim = Image.new("RGBA", (E.W, E.H), (2, 6, 14, int(205 * pr(lt, 0, 0.5)))); fr.paste(dim, (0, 0), dim)
    k = eback(pr(lt, 0, 0.35), 2.2)
    put(fr, glow_text("NEXT EPISODE", 56, WHITE), 540, 640, scale=min(k, 1.1), alpha=min(1, k * 2))
    k2 = eback(pr(lt, 0.3, 0.65), 2.4)
    put(fr, glow_text("YEAR 1918", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE GUNS FALL SILENT", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=23, dur=DUR, base_a="/home/claude/shortgen/hd_1914w.png", base_b="/home/claude/shortgen/hd_1916.png",
           regions=None, keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW, SW + 0.6, "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.0, 0.2), (s[3] + 0.8, 0.2), (s[4] + 3.2, 0.25), (s[5] + 2.5, 0.25),
                                              (s[7] + 0.6, 0.25), (s[9] + 3.0, 0.25), (s[10] + 3.4, 0.25), (s[11] + 0.6, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
