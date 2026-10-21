"""Episode 10 – Year 1453: the fall of Constantinople (Grunwald, Agincourt, Ceuta, Beijing, Joan of Arc, Zheng He, Pachacuti, Varna, Gutenberg)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1453)
import world_data_1405 as A, world_data_1453 as B

S = eval(open("/home/claude/shortgen/vo_ep10/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (40, 40, 2950)
CONST = (28.97, 41.01)
shots = [(28.6, 41.2, 950), (25, 45, 2950), (20.6, 53.6, 1100), (0.6, 50.0, 1250), (-10.5, 34.0, 2100), (116.5, 36.5, 1500), (1.2, 48.3, 1150),
         (98, 13, 2800), (-72.6, -14.0, 900), (27.6, 42.4, 1250), (8.4, 49.9, 1200), (28.4, 41.3, 950), WIDE]
keys = [(0.0, 28.9, 41.0, 1500), (0.3, 28.9, 41.0, 1500), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SWB = (s[11] - 0.85, s[11] + 0.3)
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
T_ENGLOSS = s[6] + 2.8; T_BYZ = s[11] + 3.6
reveals = [rv("byz_fall", 0.0, 0.01, until=T_BYZ),
           rv("england_fr", s[3] + 2.6, s[3] + 5.0, until=T_ENGLOSS),
           dict(key="eng_loss", t0=T_ENGLOSS, t1=T_ENGLOSS + 2.4, mode="shatter", origin=(1.9, 47.9), under="B", piece_src="N"),
           rv("inca", s[8] + 1.8, s[8] + 5.6),
           rv("ottoman", s[9] + 3.2, s[9] + 6.4),
           dict(key="byz_fall", t0=T_BYZ, t1=T_BYZ + 1.8, mode="shatter", origin=CONST, under="B", piece_src="A")]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
OTC = (200, 60, 60)
labels = [dict(text="CONSTANTINOPLE", pos=(30.5, 46.3), kind="event", color=GOLD, t_in=1.0, t_out=s[1])]
labels += [lab(A, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", t_in=T1, t_out=s[2] - 0.6), lab(A, "GOLDEN HORDE", "GOLDEN\nHORDE", t_in=T1, t_out=s[2] - 0.6),
           lab(A, "TEUTONIC ORDER", "TEUTONIC\nORDER", t_in=s[2], t_out=en[2]),
           lab(A, "FRANCE", pos=(1.0, 44.2), t_in=s[3], t_out=en[3]),
           lab(A, "PORTUGAL", pos=(-6.5, 41.6), t_in=s[4], t_out=en[4]),
           lab(A, "MING DYNASTY", "MING\nDYNASTY", kind="emp", pos=(106.0, 28.0), t_in=s[5], t_out=en[5]), lab(A, "JOSEON", kind="small", t_in=s[5], t_out=en[5]),
           lab(A, "MING DYNASTY", "MING\nDYNASTY", kind="emp", pos=(106.0, 28.0), t_in=s[7], t_out=en[7]),
           lab(B, "INCA EMPIRE", "INCA\nEMPIRE", pos=(-72.0, -19.6), t_in=s[8] + 4.0, t_out=en[8]),
           lab(A, "HUNGARY", t_in=s[9], t_out=en[9]),
           dict(text="OTTOMAN\nEMPIRE", pos=(32.0, 41.3), kind="emp", color=OTC, t_in=s[9] + 3.0, t_out=en[9]),
           dict(text="OTTOMAN\nEMPIRE", pos=(22.5, 43.0), kind="emp", color=OTC, t_in=T_BYZ + 1.6, t_out=s[12])]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("GRUNWALD", (20.5, 49.6), s[2] + 2.4, en[2] + 0.2), ev("AGINCOURT", (2.6, 54.2), s[3] + 2.2, en[3] + 0.2),
           ev("CEUTA", (-4.5, 31.0), s[4] + 2.4, en[4] + 0.2), ev("MADEIRA", (-16.9, 33.4), s[4] + 4.4, en[4] + 0.2),
           ev("BEIJING", (116.4, 40.6), s[5] + 2.2, en[5] + 0.2),
           ev("ORLEANS", (2.0, 43.6), s[6] + 1.8, en[6] + 0.2), ev("CALICUT", (75.78, 12.2), s[7] + 0.4, s[7] + 3.0),
           ev("NANJING", (119.8, 30.0), s[7] + 4.0, en[7] + 0.2), ev("CUSCO", (-78.5, -11.0), s[8] + 0.4, en[8] + 0.2),
           ev("VARNA", (29.0, 46.4), s[9] + 2.2, en[9] + 0.2), ev("MAINZ", (8.27, 50.35), s[10] + 0.6, en[10] + 0.2),
           ev("CONSTANTINOPLE", (30.5, 46.3), s[11] + 0.4, en[11] + 0.3)]

ticker = [(0, 1453), (s[1], 1453), (s[1] + 1.3, 1405), (s[2], 1405), (s[2] + 0.6, 1410), (s[3], 1410), (s[3] + 0.6, 1415), (s[5], 1415),
          (s[5] + 0.6, 1421), (s[6], 1421), (s[6] + 0.6, 1429), (s[7], 1429), (s[7] + 0.6, 1433), (s[8], 1433), (s[8] + 0.6, 1438), (s[9], 1438),
          (s[9] + 0.6, 1444), (s[10], 1444), (s[10] + 0.6, 1450), (s[11], 1450), (s[11] + 0.6, 1453), (DUR, 1453)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 1453", l2="CONSTANTINOPLE", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1405", GOLD), hd(2, "YEAR 1410", "BATTLE OF GRUNWALD"), hd(3, "YEAR 1415", "AGINCOURT"),
            hd(4, "YEAR 1415", "PORTUGAL SETS SAIL", GRN), hd(5, "YEAR 1421", "THE FORBIDDEN CITY", GOLD), hd(6, "YEAR 1429", "JOAN OF ARC", CYN),
            hd(7, "YEAR 1433", "THE LAST VOYAGE", GOLD), hd(8, "YEAR 1438", "THE INCA EMPIRE", GOLD), hd(9, "YEAR 1444", "BATTLE OF VARNA"),
            hd(10, "AROUND 1450", "THE PRINTING PRESS", CYN), hd(11, "YEAR 1453", "CONSTANTINOPLE FALLS")]

MNC = (215, 70, 60); ENC = (200, 70, 80); FRC = (60, 90, 190); PLC = (220, 100, 100); LTC = (170, 200, 110); HUC = (110, 170, 110)
PTC = (80, 150, 90); INC = (235, 105, 35); BYC = (150, 50, 130)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
FLEET = [(121.1, 31.5), (122.6, 29.5), (120.5, 25.5), (117.5, 22.6), (113, 19.5), (111.0, 15.5), (110.0, 11.5), (107.5, 7.0), (105.0, 3.2), (104.4, 1.3),
         (103.2, 1.15), (101.5, 2.4), (100.8, 2.9), (98.5, 5.0), (96.2, 6.4), (94, 6.6), (87, 6.0), (82, 5.3), (80.5, 5.4), (78.5, 7.2), (76.2, 8.6), (75.6, 11.3)]
HOME = FLEET[::-1]
EXPLORE = [(-9.4, 38.6), (-11.5, 36.5), (-14.5, 34.0), (-16.9, 32.9), (-16.5, 30.5), (-15.4, 28.3), (-14.6, 26.6), (-14.9, 25.6)]
fx = [
    M([(26.56, 41.68), (27.7, 41.35), (28.86, 41.04)], 0.4, en[0] - 0.2, OTC, kind="janissary", until=en[0] + 0.3),
    M([(26.67, 40.41), (27.6, 40.62), (28.4, 40.85), (28.95, 40.98)], 0.8, en[0] - 0.2, OTC, kind="janissary", until=en[0] + 0.3),
    PP("mehmed2", "MEHMED II", "OTTOMAN SULTAN, AGE 21", 1.6, en[0] + 0.2),
    M([(19.8, 51.4), (19.95, 52.5), (20.05, 53.38)], s[2] + 0.3, s[2] + 2.8, PLC, kind="polish"),
    M([(23.9, 54.5), (21.5, 53.8), (20.2, 53.5)], s[2] + 0.5, s[2] + 2.8, LTC, kind="polish"),
    M([(18.4, 54.6), (19.3, 54.05), (20.1, 53.58)], s[2] + 0.3, s[2] + 2.6, (235, 235, 235), kind="teutonic"),
    PP("jogaila", "JOGAILA", "KING OF POLAND", s[2] + 0.4, en[2] + 0.2),
    M([(-1.4, 50.8), (-0.6, 50.1), (0.11, 49.5), (1.0, 49.95), (2.0, 50.4)], s[3] + 0.2, s[3] + 3.4, ENC, kind="longbow"),
    M([(2.6, 49.5), (2.4, 50.0), (2.2, 50.38)], s[3] + 1.2, s[3] + 3.2, FRC, kind="french"),
    PP("henry5", "HENRY V", "KING OF ENGLAND", s[3] + 0.4, en[3] + 0.2),
    M([(-9.14, 38.65), (-9.4, 37.2), (-7.0, 36.2), (-5.35, 35.92)], s[4] + 0.2, s[4] + 2.6, PTC, kind="knight", until=en[4] + 0.2),
    PP("henrynav", "HENRY THE NAVIGATOR", "PRINCE OF PORTUGAL", s[4] + 0.4, en[4] + 0.2),
    M([(118.8, 32.05), (117.2, 35.0), (116.4, 39.9)], s[5] + 0.3, s[5] + 3.0, MNC, kind="han"),
    PP("yongle", "ZHU DI", "THE YONGLE EMPEROR", s[5] + 0.4, en[5] + 0.2),
    M([(-0.6, 46.4), (0.24, 47.17), (1.0, 47.6), (1.85, 47.88)], s[6] + 0.3, s[6] + 2.8, FRC, kind="french"),
    M([(1.95, 47.95), (2.3, 48.6), (2.6, 49.5)], s[6] + 2.8, s[6] + 4.8, ENC, kind="longbow"),
    PP("joan", "JOAN OF ARC", "THE MAID OF ORLEANS", s[6] + 0.4, en[6] + 0.2),
    M(HOME, s[7] + 0.2, en[7] + 0.1, MNC, kind="han", ship="junk", soldiers=6, until=en[7] + 0.3),
    PP("zhenghe", "ZHENG HE", "ADMIRAL OF THE FLEET", s[7] + 0.4, en[7] + 0.2),
    M([(-71.97, -13.53), (-73.3, -13.65), (-75.2, -12.4)], s[8] + 0.3, s[8] + 3.0, INC, kind="inca"),
    M([(-71.97, -13.53), (-70.8, -14.6), (-69.6, -15.7)], s[8] + 0.6, s[8] + 3.0, INC, kind="inca"),
    PP("pachacuti", "PACHACUTI", "RULER OF THE INCA", s[8] + 0.4, en[8] + 0.2),
    M([(22.9, 44.6), (25.5, 43.85), (27.8, 43.25)], s[9] + 0.3, s[9] + 2.8, HUC, kind="polish"),
    M([(29.3, 40.9), (29.05, 41.15), (28.3, 42.0), (27.9, 43.1)], s[9] + 0.3, s[9] + 2.8, OTC, kind="janissary"),
    PP("murad2", "MURAD II", "OTTOMAN SULTAN", s[9] + 0.4, en[9] + 0.2, x=300),
    PP("wladyslaw", "WLADYSLAW III", "KING OF POLAND AND HUNGARY", s[9] + 0.7, en[9] + 0.2),
    IC("scroll", (8.27, 44.6), s[10] + 1.0, en[10] + 0.2),
    PP("gutenberg", "JOHANNES GUTENBERG", "PRINTER", s[10] + 0.4, en[10] + 0.2),
    M([(26.56, 41.68), (27.7, 41.35), (28.9, 41.03)], s[11] + 0.3, s[11] + 3.2, OTC, kind="janissary"),
    M([(27.4, 42.7), (28.2, 41.8), (28.92, 41.08)], s[11] + 0.6, s[11] + 3.2, OTC, kind="janissary"),
    M([(26.67, 40.41), (27.6, 40.62), (28.4, 40.85), (28.97, 40.99)], s[11] + 0.6, s[11] + 3.2, OTC, kind="janissary", soldiers=4),
    IC("fire", (28.97, 41.01), T_BYZ + 0.2, en[11] + 0.3),
    PP("mehmed2", "MEHMED II", "THE CONQUEROR", s[11] + 0.4, en[11] + 0.2),
    PP("constantine11", "CONSTANTINE XI", "LAST BYZANTINE EMPEROR", s[11] + 0.7, T_BYZ + 0.4, x=300),
]
routes = [dict(pts=EXPLORE, t0=s[4] + 2.6, t1=en[4], until=en[4] + 0.3, color=GOLD),
          dict(pts=HOME, t0=s[7] + 0.2, t1=en[7] + 0.1, until=en[7] + 0.3, color=GOLD)]

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
    put(fr, glow_text("YEAR 1492", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("COLUMBUS SAILS WEST", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=10, dur=DUR, base_a="/home/claude/shortgen/hd_1405.png", base_b="/home/claude/shortgen/hd_1453.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1420.png"),
           regions="/home/claude/shortgen/regions_ep10_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[2] + 2.6, 0.2), (s[3] + 2.6, 0.2), (s[9] + 2.8, 0.2), (T_BYZ, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
