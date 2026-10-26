"""Episode 15 – Year 1642: Europeans reach Australia and New Zealand (Kazan 1552, Lepanto 1571, the Armada 1588, Sekigahara 1600,
the Duyfken at Cape York 1606, Jamestown 1607, Dirk Hartog 1616, Gustavus Adolphus 1630-31, the Taj Mahal 1632, Tasman 1642)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1642)
import world_data_1533 as A, world_data_1600 as N, world_data_1642 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep15/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
shots = [(130, -31, 2600), WIDE, (49.5, 55.5, 900), (19.8, 38.6, 620), (-3.0, 49.0, 1100), (137.2, 35.3, 620), (137.5, -9.0, 1150),
         (-75.8, 37.4, 700), (110.5, -27.5, 1000), (13.5, 52.5, 620), (78.0, 25.5, 800), (158, -40.5, 1700), WIDE]
EXTRA = {4: [(3.4, None), (5.0, (-4.5, 55.0, 1600))], 11: [(3.2, None), (4.4, (172.9, -40.85, 260))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, 128, -24, 3000), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("kazan_ru", s[2] + 2.2, s[2] + 4.6), rv("virginia_en", s[7] + 2.6, s[7] + 4.4), rv("livonia_sw", s[9] + 0.6, s[9] + 2.4)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
labels = [lab(N, "TSARDOM OF RUSSIA", "TSARDOM OF\nRUSSIA", pos=(43.0, 58.6), t_in=s[2] + 3.6, t_out=en[2] + 0.2),
          lab(A, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", pos=(23.5, 41.3), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(A, "ENGLAND", pos=(-1.6, 53.0), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(A, "SPAIN", pos=(-4.0, 40.0), t_in=s[4] + 0.3, t_out=s[4] + 3.4),
          lab(N, "JAPAN", pos=(140.4, 39.6), t_in=s[5] + 0.3, t_out=en[5] + 0.2),
          lab(N, "SWEDEN", pos=(15.0, 57.4), t_in=s[9] + 0.3, t_out=en[9] + 0.2),
          lab(N, "HOLY ROMAN EMPIRE", "HOLY ROMAN\nEMPIRE", pos=(9.0, 49.3), t_in=s[9] + 0.3, t_out=en[9] + 0.2),
          lab(N, "POLISH-LITHUANIAN COMMONWEALTH", "POLAND-\nLITHUANIA", kind="mid", pos=(20.8, 52.3), t_in=s[9] + 0.3, t_out=en[9] + 0.2),
          lab(N, "MUGHAL EMPIRE", "MUGHAL\nEMPIRE", pos=(73.0, 23.0), t_in=s[10] + 0.3, t_out=en[10] + 0.2),
          lab(B, "TSARDOM OF RUSSIA", "RUSSIA", pos=(95.0, 64.0), t_in=s[12] - 0.2, t_out=s[12] + 0.2),
          lab(B, "SPAIN", pos=(-62.0, -6.0), t_in=s[12] - 0.2, t_out=s[12] + 0.2)]
labels += [ev("KAZAN", (49.4, 53.6), s[2] + 0.4, en[2] + 0.2),
           ev("LEPANTO", (22.6, 37.5), s[3] + 0.4, en[3] + 0.2), ev("HOLY LEAGUE", (14.6, 40.7), s[3] + 1.0, en[3] + 0.2, (240, 230, 200)),
           ev("CALAIS", (3.6, 49.9), s[4] + 1.6, s[4] + 2.9),
           ev("SEKIGAHARA", (135.0, 37.9), s[5] + 0.4, en[5] + 0.2),
           ev("CAPE YORK", (146.2, -16.6), s[6] + 2.6, en[6] + 0.2), ev("NEW GUINEA", (138.0, -3.6), s[6] + 0.6, en[6] + 0.2, (240, 230, 200)),
           ev("JAMESTOWN", (-79.8, 38.9), s[7] + 2.4, en[7] + 0.2),
           ev("SHARK BAY", (118.5, -27.5), s[8] + 2.6, en[8] + 0.2),
           ev("BREITENFELD", (12.6, 50.5), s[9] + 4.0, en[9] + 0.2),
           ev("AGRA", (78.0, 27.9), s[10] + 0.4, en[10] + 0.2), ev("TAJ MAHAL", (78.0, 25.6), s[10] + 2.0, en[10] + 0.2, WHITE),
           ev("TASMANIA", (146.5, -39.6), s[11] + 1.4, s[11] + 3.4), ev("NEW ZEALAND", (175.0, -37.0), s[11] + 2.4, s[11] + 3.6),
           ev("GOLDEN BAY", (173.1, -41.65), s[11] + 4.4, en[11] + 0.2)]

ticker = [(0, 1642), (s[1], 1642), (s[1] + 1.3, 1533), (s[2], 1533), (s[2] + 0.6, 1552), (s[3], 1552), (s[3] + 0.6, 1571), (s[4], 1571), (s[4] + 0.6, 1588),
          (s[5], 1588), (s[5] + 0.6, 1600), (s[6], 1600), (s[6] + 0.6, 1606), (s[7], 1606), (s[7] + 0.6, 1607), (s[8], 1607), (s[8] + 0.6, 1616),
          (s[9], 1616), (s[9] + 0.6, 1630), (s[9] + 3.4, 1630), (s[9] + 4.0, 1631), (s[10], 1631), (s[10] + 0.6, 1632), (s[11], 1632),
          (s[11] + 0.6, 1642), (DUR, 1642)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150); ORG = (245, 150, 50)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1642", l2="THE SOUTHERN LAND", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1533", GOLD), hd(2, "OCTOBER 1552", "KAZAN FALLS", GRN), hd(3, "OCTOBER 1571", "BATTLE OF LEPANTO", CYN),
            hd(4, "YEAR 1588", "THE SPANISH ARMADA"), hd(5, "OCTOBER 1600", "SEKIGAHARA"), hd(6, "YEAR 1606", "FIRST LANDING IN AUSTRALIA", ORG),
            hd(7, "YEAR 1607", "JAMESTOWN", CYN), hd(8, "OCTOBER 1616", "THE HARTOG PLATE", ORG), hd(9, "YEAR 1630", "SWEDEN ENTERS THE WAR", CYN),
            hd(10, "YEAR 1632", "THE TAJ MAHAL", GOLD), hd(11, "YEAR 1642", "NEW ZEALAND", ORG)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
NLC = (240, 140, 40); RUC = (170, 40, 40); KZC = (170, 130, 70); HLC = (240, 230, 200); OTC = (200, 60, 60); SPC = (235, 180, 40)
ENC = (200, 70, 80); TKC = (40, 60, 150); WSC = (200, 60, 60); SWC = (80, 130, 205); IMC = (235, 235, 235); MOC = (150, 40, 30)
TASMAN = [(106.8, -6.2), (95, -12), (75, -18), (57.5, -20.2), (65, -33), (80, -43), (100, -46), (120, -46), (140, -45), (145.5, -44.2), (148.6, -43.2), (160, -42),
          (172.6, -40.7), (172.5, -36), (175, -30), (179.3, -21), (179.0, -17), (168, -9), (155, -3), (140, -1.0), (128, -2.5), (118, -5.5), (106.8, -6.2)]
KAZAN = [(37.6, 55.75), (40.4, 56.1), (43.9, 56.3), (46.5, 56.0), (48.0, 55.8), (49.05, 55.8)]
KAZD = [(49.6, 55.85), (49.3, 55.82), (49.15, 55.8)]
HL = [(15.6, 38.2), (16.6, 38.0), (17.8, 38.6), (19.3, 39.2), (20.2, 39.0), (20.8, 38.5), (21.05, 38.3)]
OT = [(21.82, 38.38), (21.55, 38.33), (21.3, 38.28)]
ARM = [(-8.4, 43.4), (-7.0, 46.0), (-5.2, 48.8), (-3.0, 49.9), (-0.5, 50.3), (1.6, 50.95)]
FIRE = [(1.35, 51.12), (1.55, 51.05), (1.75, 50.98)]
FLEE = [(2.2, 51.3), (2.6, 53.0), (1.5, 56.0), (-0.5, 58.5), (-2.8, 59.6), (-6.5, 58.8), (-9.0, 56.5), (-10.6, 54.0), (-10.8, 51.6)]
EAST = [(139.7, 35.7), (139.0, 35.25), (138.2, 34.95), (137.4, 35.1), (136.9, 35.25), (136.5, 35.36)]
WEST = [(135.5, 34.7), (135.8, 34.95), (136.1, 35.2), (136.35, 35.36)]
DUYF = [(129.9, -4.6), (133.0, -6.6), (136.5, -8.2), (139.2, -9.3), (141.0, -11.0), (141.55, -12.5)]
DLAND = [(141.6, -12.55), (141.75, -12.58), (141.9, -12.6)]
JAME = [(-70.5, 35.2), (-73.5, 36.4), (-75.6, 36.95), (-76.2, 37.0), (-76.55, 37.08), (-76.78, 37.21)]
HART = [(92.0, -36.0), (100.0, -33.0), (106.0, -30.0), (110.5, -27.2), (112.6, -25.6), (112.95, -25.5)]
SWSEA = [(18.07, 59.33), (18.6, 58.4), (17.6, 56.6), (15.6, 55.1), (14.3, 54.4), (13.85, 54.15)]
SWLAND = [(13.85, 54.1), (13.5, 53.4), (12.9, 52.6), (12.45, 51.9), (12.38, 51.45)]
IMP = [(11.2, 50.95), (11.7, 51.2), (12.05, 51.33), (12.3, 51.4)]
TAS2 = [(100.0, -44.0), (120.0, -46.0), (140.0, -45.0), (145.5, -44.2), (148.6, -43.2), (152.0, -42.6), (162.0, -41.8), (170.0, -40.8), (172.65, -40.72)]
WAKA = [(173.5, -41.05), (173.15, -40.9), (172.8, -40.78)]
fx = [
    M(TASMAN, 0.4, en[0] - 0.1, NLC, kind="dutch", soldiers=1, sea_only=True, until=en[0] + 0.4),
    PP("tasman", "ABEL TASMAN", "DUTCH EXPLORER", 2.6, en[0] + 0.2, x=300),
    M(KAZAN, s[2] + 0.4, s[2] + 2.6, RUC, kind="strelets", soldiers=10, ships=False, until=en[2] + 0.3),
    M(KAZD, s[2] + 0.8, s[2] + 2.4, KZC, kind="mongol", soldiers=4, ships=False, until=s[2] + 2.8),
    IC("fire", (49.6, 56.7), s[2] + 2.4, s[2] + 4.6),
    PP("ivan4", "IVAN THE TERRIBLE", "TSAR OF RUSSIA", s[2] + 0.4, en[2] + 0.2, x=300),
    M(HL, s[3] + 0.4, s[3] + 3.6, HLC, kind="knight", soldiers=6, sea_only=True, ship="galley", until=en[3] + 0.3),
    M(OT, s[3] + 1.6, s[3] + 3.6, OTC, kind="janissary", soldiers=4, sea_only=True, ship="galley", until=s[3] + 4.4),
    M(ARM, s[4] + 0.4, s[4] + 2.6, SPC, kind="conquistador", soldiers=8, sea_only=True, until=s[4] + 3.0),
    M(FIRE, s[4] + 2.2, s[4] + 3.2, ENC, kind="musketeer", soldiers=4, sea_only=True, until=s[4] + 3.6),
    IC("fire", (1.9, 51.4), s[4] + 2.9, s[4] + 4.4),
    M(FLEE, s[4] + 3.4, en[4] - 0.2, SPC, kind="conquistador", soldiers=6, sea_only=True, until=en[4] + 0.3),
    PP("elizabeth", "ELIZABETH I", "QUEEN OF ENGLAND", s[4] + 0.4, en[4] + 0.2),
    M(EAST, s[5] + 0.4, s[5] + 3.4, TKC, kind="samurai", soldiers=10, ships=False, until=en[5] + 0.3),
    M(WEST, s[5] + 0.6, s[5] + 3.0, WSC, kind="samurai", soldiers=6, ships=False, until=s[5] + 3.6),
    PP("ieyasu", "TOKUGAWA IEYASU", "FIRST TOKUGAWA SHOGUN", s[5] + 0.4, en[5] + 0.2),
    M(DUYF, s[6] + 0.4, s[6] + 3.0, NLC, kind="dutch", soldiers=3, sea_only=True, until=en[6] + 0.3),
    M(DLAND, s[6] + 3.0, s[6] + 4.2, NLC, kind="dutch", soldiers=3, ships=False, until=en[6] + 0.3),
    M(JAME, s[7] + 0.4, s[7] + 2.6, ENC, kind="musketeer", soldiers=6, sea_only=True, until=en[7] + 0.3),
    M(HART, s[8] + 0.4, s[8] + 2.8, NLC, kind="dutch", soldiers=3, sea_only=True, until=en[8] + 0.3),
    M(SWSEA, s[9] + 0.4, s[9] + 2.4, SWC, kind="swede", soldiers=6, sea_only=True, until=s[9] + 2.8),
    M(SWLAND, s[9] + 2.4, s[9] + 4.4, SWC, kind="swede", soldiers=9, ships=False, until=en[9] + 0.3),
    M(IMP, s[9] + 3.0, s[9] + 4.4, IMC, kind="musketeer", soldiers=6, ships=False, until=s[9] + 5.0),
    PP("gustavus", "GUSTAVUS ADOLPHUS", "KING OF SWEDEN", s[9] + 0.4, en[9] + 0.2),
    PP("shahjahan", "SHAH JAHAN", "MUGHAL EMPEROR", s[10] + 0.4, en[10] + 0.2),
    M(TAS2, s[11] + 0.3, s[11] + 3.6, NLC, kind="dutch", soldiers=2, sea_only=True, until=en[11] + 0.3),
    M(WAKA, s[11] + 4.4, s[11] + 5.8, MOC, kind="maori", soldiers=3, sea_only=True, ship="waka", until=en[11] + 0.3),
    PP("tasman", "ABEL TASMAN", "DUTCH EXPLORER", s[11] + 0.4, en[11] + 0.2, x=300),
]
routes = [dict(pts=TASMAN, t0=0.4, t1=en[0] - 0.1, until=en[0] + 0.5, color=GOLD),
          dict(pts=DUYF, t0=s[6] + 0.4, t1=s[6] + 3.0, until=en[6] + 0.3, color=GOLD),
          dict(pts=HART, t0=s[8] + 0.4, t1=s[8] + 2.8, until=en[8] + 0.3, color=GOLD),
          dict(pts=TAS2, t0=s[11] + 0.3, t1=s[11] + 3.6, until=en[11] + 0.3, color=GOLD)]
SW1, SW2 = s[5] - 0.85, s[11] - 0.85
labels += WP.labels(A, 1560, T1, SW1 + 0.4) + WP.labels(N, 1610, SW1 + 0.4, SW2 + 0.4, skip=("Chamorro",)) + WP.labels(B, 1642, SW2 + 0.4, s[12], skip=("Chamorro",))

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
    put(fr, glow_text("YEAR 1770", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("JAMES COOK IN THE PACIFIC", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=15, dur=DUR, base_a="/home/claude/shortgen/hd_1533.png", base_b="/home/claude/shortgen/hd_1642.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1600.png"),
           regions="/home/claude/shortgen/regions_ep15_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1, SW1 + 1.1, "A", "N"), (SW2, SW2 + 1.1, "N", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 2.4, 0.25), (s[3] + 3.6, 0.25), (s[4] + 3.0, 0.2), (s[5] + 3.4, 0.25),
                                              (s[6] + 3.0, 0.2), (s[9] + 4.4, 0.25), (s[11] + 5.6, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
