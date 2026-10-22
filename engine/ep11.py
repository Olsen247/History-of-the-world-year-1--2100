"""Episode 11 – Year 1492: Columbus reaches the Americas (Wars of the Roses, Vlad III, Onin War, Songhai, Isabella & Ferdinand, Ugra, Dias, Granada)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1492)
import world_data_1453b as A, world_data_1492 as B

S = eval(open("/home/claude/shortgen/vo_ep11/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (0, 25, 2950)
shots = [(-37, 28, 1500), (12, 44, 2950), (-1.0, 52.6, 420), (27.0, 43.0, 800), (135.5, 35.2, 480), (-2.0, 15.5, 650), (-3.0, 40.5, 650),
         (37.0, 54.5, 800), (10, -10, 2600), (-4.0, 37.6, 420), (-38, 29, 2000), (-75.5, 22.5, 600), WIDE]
keys = [(0.0, -36, 28, 2700), (0.3, -36, 28, 2700), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SWB = (s[10] - 0.85, s[10] + 0.3)
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("ott_serbia", s[3] + 2.6, s[3] + 5.0), rv("ott_morea", s[3] + 2.9, s[3] + 5.0), rv("ott_treb", s[3] + 3.2, s[3] + 5.2),
           rv("songhai", s[5] + 2.6, s[5] + 5.6), rv("muscovy", s[7] + 1.0, s[7] + 3.6), rv("granada", s[9] + 2.2, s[9] + 4.4)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
OTC = (200, 60, 60); CAC = (200, 120, 60)
labels = [dict(text="ATLANTIC\nOCEAN", pos=(-37, 35.5), kind="event", color=GOLD, t_in=1.0, t_out=s[1])]
labels += [lab(A, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", t_in=T1, t_out=s[2] - 0.6), lab(A, "CASTILE", t_in=T1, t_out=s[2] - 0.6),
           lab(A, "FRANCE", t_in=T1, t_out=s[2] - 0.6),
           lab(A, "ENGLAND", pos=(-2.6, 51.1), t_in=s[2], t_out=en[2]),
           lab(B, "SONGHAI EMPIRE", "SONGHAI\nEMPIRE", pos=(-0.6, 14.4), t_in=s[5] + 4.6, t_out=en[5]),
           lab(A, "MALI EMPIRE", "MALI", kind="mid", pos=(-10.5, 13.6), t_in=s[5], t_out=en[5]),
           lab(A, "CASTILE", pos=(-4.0, 40.3), t_in=s[6], t_out=en[6]), lab(A, "ARAGON", pos=(-0.6, 41.0), t_in=s[6], t_out=en[6]),
           lab(B, "MUSCOVY", pos=(37.5, 57.6), t_in=s[7] + 3.0, t_out=en[7]), lab(A, "GREAT HORDE", "GREAT\nHORDE", pos=(44.5, 51.5), t_in=s[7], t_out=en[7]),
           lab(A, "PORTUGAL", pos=(-8.0, 40.5), t_in=s[8], t_out=s[8] + 3.0),
           lab(B, "CASTILE", pos=(-4.2, 38.9), t_in=s[9] + 4.2, t_out=en[9])]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("ST ALBANS", (2.6, 52.4), s[2] + 2.4, en[2] + 0.2), ev("WALLACHIA", (25.5, 47.1), s[3] + 0.6, en[3] + 0.2),
           ev("KYOTO", (138.3, 36.4), s[4] + 1.0, en[4] + 0.2), ev("TIMBUKTU", (-3.0, 18.6), s[5] + 2.2, en[5] + 0.2),
           ev("UGRA RIVER", (32.0, 54.6), s[7] + 2.4, en[7] + 0.2), ev("CAPE OF\nGOOD HOPE", (18.5, -40.0), s[8] + 4.0, en[8] + 0.2),
           ev("GRANADA", (-3.6, 36.2), s[9] + 0.6, en[9] + 0.2), ev("PALOS", (-6.9, 38.2), s[10] + 0.4, s[10] + 3.0),
           ev("BAHAMAS", (-73.0, 26.6), s[11] + 0.4, en[11] + 0.2), ev("CUBA", (-79.5, 21.0), s[11] + 2.6, en[11] + 0.2),
           ev("HISPANIOLA", (-71.0, 17.6), s[11] + 3.6, en[11] + 0.2)]

ticker = [(0, 1492), (s[1], 1492), (s[1] + 1.3, 1453), (s[2], 1453), (s[2] + 0.6, 1455), (s[3], 1455), (s[3] + 0.6, 1462), (s[4], 1462),
          (s[4] + 0.6, 1467), (s[5], 1467), (s[5] + 0.6, 1468), (s[6], 1468), (s[6] + 0.6, 1469), (s[7], 1469), (s[7] + 0.6, 1480), (s[8], 1480),
          (s[8] + 0.6, 1488), (s[9], 1488), (s[9] + 0.6, 1492), (DUR, 1492)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 1492", l2="SAILING WEST", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1453", GOLD), hd(2, "YEAR 1455", "WARS OF THE ROSES"), hd(3, "YEAR 1462", "THE NIGHT ATTACK"),
            hd(4, "YEAR 1467", "THE ONIN WAR"), hd(5, "YEAR 1468", "SONGHAI RISES", GOLD), hd(6, "YEAR 1469", "A ROYAL WEDDING", CYN),
            hd(7, "YEAR 1480", "THE UGRA RIVER", GRN), hd(8, "YEAR 1488", "CAPE OF GOOD HOPE", GOLD), hd(9, "YEAR 1492", "GRANADA FALLS"),
            hd(10, "AUGUST 1492", "COLUMBUS SETS SAIL", CYN), hd(11, "OCTOBER 1492", "LAND AHOY!", GOLD)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
HOOK = [(-17.1, 28.1), (-25, 28.0), (-33, 27.8), (-41, 27.4), (-49, 26.8), (-57, 26.0)]
CROSS = [(-6.9, 37.2), (-8.5, 35.0), (-12.5, 31.0), (-15.4, 28.15), (-17.1, 28.1), (-25, 28.0), (-35, 27.7), (-45, 27.2), (-55, 26.4), (-63, 25.6),
         (-69, 24.9), (-74.3, 24.1)]
CARIB = [(-74.3, 24.1), (-75.2, 23.4), (-75.9, 22.4), (-75.9, 21.25), (-74.6, 20.6), (-73.4, 20.2), (-72.8, 19.95)]
DIAS = [(-9.2, 38.6), (-11.5, 34.0), (-16.5, 27.0), (-18.5, 20.0), (-18.0, 12.0), (-14.0, 6.0), (-6.0, 3.5), (3.0, 2.5), (8.0, -3.0), (10.5, -10.0),
        (11.5, -17.0), (13.5, -25.0), (15.5, -31.5), (18.4, -35.6), (22.0, -35.4), (26.6, -33.9)]
COL = (60, 110, 200); PTC = (80, 150, 90)
fx = [
    M(HOOK, 0.4, en[0] + 0.2, COL, kind="conquistador", soldiers=7, until=en[0] + 0.5),
    PP("columbus", "CHRISTOPHER COLUMBUS", "SAILING FOR SPAIN", 1.6, en[0] + 0.2),
    M([(-1.08, 53.96), (-1.2, 53.1), (-0.75, 52.4), (-0.36, 51.80)], s[2] + 0.3, s[2] + 3.0, (235, 235, 235), kind="longbow"),
    M([(-0.13, 51.50), (-0.75, 51.45), (-0.62, 51.66), (-0.36, 51.74)], s[2] + 0.6, s[2] + 3.0, (200, 40, 50), kind="longbow"),
    M([(28.9, 41.05), (26.6, 41.7), (25.6, 42.7), (24.9, 43.7), (25.3, 44.6)], s[3] + 0.3, s[3] + 3.0, OTC, kind="janissary"),
    M([(23.0, 44.95), (24.4, 45.0), (25.3, 44.7)], s[3] + 2.6, s[3] + 4.6, (60, 80, 170), kind="wallachian"),
    PP("vlad3", "VLAD III", "THE IMPALER", s[3] + 0.4, en[3] + 0.2),
    PP("mehmed2", "MEHMED II", "OTTOMAN SULTAN", s[3] + 0.7, en[3] + 0.2, x=300),
    M([(133.6, 34.0), (134.7, 34.5), (135.5, 34.75), (135.76, 35.0)], s[4] + 0.3, s[4] + 2.8, (60, 90, 180), kind="samurai"),
    M([(132.6, 35.4), (134.2, 35.45), (135.74, 35.04)], s[4] + 0.5, s[4] + 2.8, (200, 60, 60), kind="samurai"),
    IC("fire", (135.77, 35.01), s[4] + 2.8, en[4] + 0.2),
    M([(-0.04, 16.27), (-1.6, 16.75), (-3.0, 16.77)], s[5] + 0.3, s[5] + 2.8, (200, 110, 60), kind="songhai"),
    PP("sonniali", "SONNI ALI", "RULER OF SONGHAI", s[5] + 0.4, en[5] + 0.2),
    PP("isabella", "ISABELLA", "QUEEN OF CASTILE", s[6] + 0.4, en[6] + 0.2, x=300),
    PP("ferdinand", "FERDINAND", "PRINCE OF ARAGON", s[6] + 0.7, en[6] + 0.2),
    M([(37.6, 55.75), (36.6, 55.1), (35.8, 54.55)], s[7] + 0.3, s[7] + 2.8, (120, 170, 90), kind="rus"),
    M([(40.0, 50.0), (37.5, 52.4), (36.0, 53.9)], s[7] + 0.6, s[7] + 3.0, (190, 150, 60), kind="mongol", until=s[7] + 4.4),
    PP("ivan3", "IVAN III", "GRAND PRINCE OF MOSCOW", s[7] + 0.4, en[7] + 0.2, x=300),
    M(DIAS, s[8] + 0.2, en[8] + 0.1, PTC, kind="knight", soldiers=4, until=en[8] + 0.3),
    PP("dias", "BARTOLOMEU DIAS", "PORTUGUESE EXPLORER", s[8] + 0.4, en[8] + 0.2, x=300),
    M([(-4.78, 37.88), (-4.25, 37.45), (-3.62, 37.18)], s[9] + 0.3, s[9] + 2.6, CAC, kind="conquistador"),
    M([(-3.79, 37.77), (-3.70, 37.45), (-3.60, 37.2)], s[9] + 0.5, s[9] + 2.6, (210, 180, 60), kind="conquistador"),
    PP("isabella", "ISABELLA", "QUEEN OF CASTILE", s[9] + 0.4, en[9] + 0.2, x=300),
    PP("ferdinand", "FERDINAND", "KING OF ARAGON", s[9] + 0.7, en[9] + 0.2),
    M(CROSS, s[10] + 0.2, en[10] + 0.3, COL, kind="conquistador", soldiers=7, until=s[11] + 0.6),
    PP("columbus", "CHRISTOPHER COLUMBUS", "ADMIRAL OF THE OCEAN SEA", s[10] + 0.4, en[10] + 0.2),
    M(CARIB, s[11] + 0.3, en[11] - 0.4, COL, kind="conquistador", soldiers=7, until=en[11] + 0.3),
]
routes = [dict(pts=DIAS, t0=s[8] + 0.2, t1=en[8] + 0.1, until=en[8] + 0.3, color=GOLD),
          dict(pts=CROSS, t0=s[10] + 0.2, t1=en[10] + 0.3, until=en[11] + 0.3, color=GOLD),
          dict(pts=CARIB, t0=s[11] + 0.3, t1=en[11] - 0.4, until=en[11] + 0.3, color=GOLD)]

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
    put(fr, glow_text("YEAR 1498", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("BY SEA TO INDIA", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=11, dur=DUR, base_a="/home/claude/shortgen/hd_1453b.png", base_b="/home/claude/shortgen/hd_1492.png",
           regions="/home/claude/shortgen/regions_ep11_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[3] + 2.8, 0.2), (s[4] + 2.8, 0.2), (s[9] + 2.4, 0.2), (s[11] + 0.4, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
