"""Episode 13 – Year 1522: Magellan's expedition sails around the world (Cabral reaches Brazil, Shah Ismail and the Safavids,
Albuquerque takes Malacca, Balboa sees the Pacific, Selim takes Cairo + Luther's 95 Theses, Magellan's voyage, Mactan,
the fall of Tenochtitlan, the Victoria comes home)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1522)
import world_data_1498 as A, world_data_1522 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep13/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
shots = [(-16, 2, 2850), (-16, 8, 2850), (-24, -2, 2300), (50.5, 34.5, 1350), (88, 10, 2100), (-74.5, 14, 1650), (25, 41, 2300),
         (-25, 8, 2600), (-63, -43, 1500), (140, 12, 2000), (-98.3, 19.4, 620), (110, -8, 2850), WIDE]
EXTRA = {5: [(2.2, None), (3.4, (-78.3, 8.9, 520))], 8: [(3.0, None), (4.6, (-118, -16, 2850))],
         9: [(2.6, None), (3.6, (124.1, 10.35, 420))], 11: [(1.2, None), (4.6, (30, -12, 2850)), (6.6, (-2, 10, 2850))]}
endshot = list(shots)
for i, ex in EXTRA.items(): endshot[i] = ex[-1][1]
keys = [(0.0, -16, 2, 2850), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

SWB = (s[11] - 0.85, s[11] + 0.3)
REF = s[6] + 3.6        # second half of line 6: Luther (October 1517)
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("brazil_pt", s[2] + 4.2, s[2] + 5.4), rv("safavid", s[3] + 2.6, s[3] + 6.2), rv("india_pt", s[4] + 2.4, s[4] + 4.6),
           rv("carib_sp", s[5] + 0.4, s[5] + 2.4), rv("ottoman", s[6] + 1.0, s[6] + 3.4), rv("mexico_sp", s[10] + 3.3, s[10] + 5.0)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
labels = [lab(B, "SPAIN", pos=(-4.0, 40.0), t_in=0.6, t_out=en[0]),
          lab(A, "SONGHAI EMPIRE", "SONGHAI\nEMPIRE", t_in=T1, t_out=en[2]),
          lab(A, "AQ QOYUNLU", pos=(51.0, 32.0), t_in=s[3] + 0.2, t_out=s[3] + 2.6), lab(A, "TIMURID EMPIRE", "TIMURID\nEMPIRE", pos=(64.0, 36.5), t_in=s[3] + 0.2, t_out=en[3]),
          lab(B, "SAFAVID EMPIRE", "SAFAVID\nEMPIRE", pos=(56.0, 31.0), t_in=s[3] + 3.4, t_out=en[3] + 0.2),
          lab(A, "MAJAPAHIT", pos=(111.0, -7.6), t_in=s[4] + 0.3, t_out=en[4]),
          lab(A, "MAMLUK SULTANATE", "MAMLUK\nSULTANATE", pos=(28.0, 25.0), t_in=s[6] + 0.2, t_out=s[6] + 1.0),
          lab(B, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", pos=(33.5, 38.9), t_in=s[6] + 2.2, t_out=en[6] + 0.2),
          lab(A, "INCA EMPIRE", "INCA\nEMPIRE", pos=(-66.5, -17.5), t_in=s[7] + 0.3, t_out=s[8] + 3.6),
          lab(A, "AZTEC EMPIRE", "AZTEC\nEMPIRE", pos=(-95.9, 17.0), t_in=s[10] + 0.2, t_out=s[10] + 3.3),
          lab(B, "SPAIN", pos=(-4.0, 40.0), t_in=s[11] + 4.5, t_out=s[12] + 0.2),
          lab(B, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", pos=(33.5, 38.9), t_in=s[11] + 3.2, t_out=s[12] + 0.2),
          lab(B, "SONGHAI EMPIRE", "SONGHAI\nEMPIRE", pos=(-1.6, 13.4), t_in=s[11] + 4.5, t_out=s[12] + 0.2)]
labels += [ev("LISBON", (-9.1, 37.6), s[2] + 0.3, s[2] + 2.6), ev("BRAZIL", (-45.5, -11.0), s[2] + 4.2, en[2] + 0.2),
           ev("TABRIZ", (45.4, 39.9), s[3] + 0.4, s[3] + 2.4),
           ev("GOA", (72.4, 16.6), s[4] + 0.3, en[4] + 0.2), ev("MALACCA", (100.2, -0.4), s[4] + 3.0, en[4] + 0.2),
           ev("SPAIN", (-70.8, 21.2), s[5] + 1.2, s[5] + 3.2, (240, 200, 80)), ev("PANAMA", (-81.3, 9.9), s[5] + 3.6, en[5] + 0.2),
           ev("PACIFIC", (-79.4, 7.65), s[5] + 5.2, en[5] + 0.2, (120, 200, 240)),
           ev("CAIRO", (31.2, 29.2), s[6] + 2.4, REF), ev("WITTENBERG", (12.6, 52.8), REF, en[6] + 0.2),
           ev("SPAIN", (-4.5, 39.6), s[7] + 0.3, s[7] + 3.0, (240, 200, 80)),
           ev("STRAIT", (-64.5, -52.2), s[8] + 1.6, s[8] + 4.0), ev("PACIFIC OCEAN", (-125.0, -24.0), s[8] + 4.6, en[8] + 0.2, (120, 200, 240)),
           ev("GUAM", (144.7, 15.0), s[9] + 1.0, s[9] + 3.0), ev("MACTAN", (121.9, 11.2), s[9] + 3.6, en[9] + 0.2),
           ev("TENOCHTITLAN", (-100.2, 21.9), s[10] + 0.4, en[10] + 0.2), ev("NEW SPAIN", (-96.2, 16.9), s[10] + 4.0, en[10] + 0.2, (240, 200, 80)),
           ev("TIDORE", (127.4, 2.0), s[11] + 0.4, s[11] + 2.6)]

ticker = [(0, 1522), (s[1], 1522), (s[1] + 1.3, 1498), (s[2], 1498), (s[2] + 0.6, 1500), (s[3], 1500), (s[3] + 0.6, 1501), (s[4], 1501), (s[4] + 0.6, 1511),
          (s[5], 1511), (s[5] + 0.6, 1513), (s[6], 1513), (s[6] + 0.6, 1517), (s[7], 1517), (s[7] + 0.6, 1519), (s[8], 1519), (s[8] + 0.6, 1520),
          (s[8] + 4.0, 1520), (s[8] + 4.6, 1521), (s[11], 1521), (s[11] + 0.6, 1522), (DUR, 1522)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1522", l2="AROUND THE WORLD", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1498", GOLD), hd(2, "YEAR 1500", "CABRAL REACHES BRAZIL", GRN), hd(3, "YEAR 1501", "THE SAFAVID EMPIRE", GRN),
            hd(4, "YEAR 1511", "MALACCA FALLS", GOLD), hd(5, "YEAR 1513", "A NEW OCEAN", CYN), hd(6, "YEAR 1517", "SELIM TAKES CAIRO", t1=REF),
            dict(t0=REF, t1=en[6] + 0.2, l1="OCTOBER 1517", l2="THE REFORMATION", c2=GOLD),
            hd(7, "SEPTEMBER 1519", "MAGELLAN SETS SAIL", CYN), hd(8, "NOVEMBER 1520", "INTO THE PACIFIC", CYN), hd(9, "APRIL 1521", "DEATH ON MACTAN"),
            hd(10, "AUGUST 1521", "TENOCHTITLAN FALLS"), hd(11, "SEPTEMBER 1522", "18 MEN COME HOME", GOLD)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
SPC = (235, 180, 40); PTC = (80, 150, 90); OTC = (200, 60, 60); SFC = (60, 150, 120); TLX = (200, 200, 210); VIS = (200, 60, 50)
HOOK_W = [(-6.4, 36.6), (-12.0, 31.0), (-17.0, 25.0), (-25.0, 18.0), (-35.0, 10.0), (-42.0, 2.0)]
HOOK_E = [(18.0, -36.0), (11.0, -30.0), (5.0, -20.0), (-4.0, -6.0), (-14.0, 5.0), (-21.0, 14.0), (-21.5, 24.0), (-14.0, 32.5), (-6.6, 36.6)]
CABRAL = [(-9.15, 38.7), (-13.0, 30.0), (-18.0, 21.0), (-23.5, 14.9), (-27.0, 5.0), (-32.0, -5.0), (-36.0, -12.0), (-38.9, -16.4)]
ALBU = [(73.6, 15.3), (74.3, 10.5), (76.8, 6.6), (80.5, 5.2), (88.0, 5.8), (95.0, 5.9), (98.6, 4.4), (101.3, 2.7), (102.15, 2.25)]
BALBOA = [(-77.55, 9.0), (-77.85, 8.7), (-78.15, 8.45), (-78.45, 8.35)]
SELIM = [(37.3, 36.5), (36.7, 34.6), (36.3, 33.5), (35.4, 32.3), (34.4, 31.3), (32.6, 30.6), (31.25, 30.05)]
QIZIL = [(46.3, 38.1), (48.2, 37.2), (50.0, 36.3), (51.4, 35.7)]
MAG1 = [(-6.35, 36.75), (-10.0, 33.0), (-13.5, 28.3), (-17.0, 22.0), (-20.0, 14.0), (-25.0, 5.0), (-31.0, -3.0), (-35.5, -9.0), (-38.0, -16.0),
        (-40.5, -22.6), (-43.17, -23.1)]
MAG2 = [(-43.17, -23.1), (-46.0, -30.0), (-52.0, -37.0), (-60.0, -42.0), (-65.5, -47.5), (-68.3, -52.3), (-70.4, -53.3), (-72.6, -53.6), (-75.0, -52.6)]
MAG3 = [(-75.0, -52.6), (-78.0, -48.0), (-80.5, -38.0), (-85.0, -28.0), (-95.0, -18.0), (-110.0, -10.0), (-125.0, -3.0), (-140.0, 3.0), (-160.0, 8.0), (-179.5, 11.5)]
MAG4 = [(179.5, 12.0), (165.0, 13.0), (150.0, 13.4), (144.7, 13.4), (135.0, 12.0), (126.2, 10.8), (124.6, 10.5), (124.12, 10.38)]
LANDING = [(124.28, 10.5), (124.17, 10.42), (124.07, 10.34)]
LAPU = [(123.97, 10.24), (124.0, 10.28), (124.04, 10.32)]
CORTES = [(-96.1, 19.2), (-97.0, 19.45), (-98.2, 19.32), (-98.6, 19.5), (-98.88, 19.51), (-99.13, 19.43)]
ALLIES = [(-98.2, 19.18), (-98.6, 19.3), (-98.9, 19.38), (-99.1, 19.4)]
VICT = [(127.4, 0.7), (125.5, -4.5), (124.5, -9.6), (115.0, -15.0), (100.0, -22.0), (80.0, -30.0), (55.0, -37.0), (35.0, -37.5), (20.0, -36.3),
        (12.0, -30.0), (5.0, -20.0), (-4.0, -6.0), (-14.0, 5.0), (-21.0, 14.0), (-21.5, 24.0), (-14.0, 32.5), (-6.4, 36.75)]
fx = [
    M(HOOK_W, 0.4, 3.2, SPC, kind="conquistador", soldiers=15, sea_only=True, until=3.4),
    M(HOOK_E, 2.8, en[0] - 0.1, SPC, kind="conquistador", soldiers=1, sea_only=True, until=en[0] + 0.5),
    PP("magellan", "FERDINAND MAGELLAN", "EXPLORER", 1.2, en[0] + 0.2),
    M(CABRAL, s[2] + 0.3, s[2] + 4.4, PTC, kind="knight", soldiers=4, sea_only=True, until=en[2] + 0.3),
    PP("cabral", "PEDRO ÁLVARES CABRAL", "PORTUGUESE CAPTAIN", s[2] + 0.4, en[2] + 0.2),
    M(QIZIL, s[3] + 2.4, s[3] + 5.6, SFC, kind="qizilbash", until=en[3] + 0.3),
    PP("ismail", "SHAH ISMAIL I", "FOUNDER OF THE SAFAVID EMPIRE", s[3] + 0.4, en[3] + 0.2, x=300),
    M(ALBU, s[4] + 0.3, s[4] + 3.4, PTC, kind="knight", soldiers=4, sea_only=True, until=en[4] + 0.3),
    IC("spice", (105.0, 9.0), s[4] + 3.4, en[4] + 0.2),
    PP("albuquerque", "AFONSO DE ALBUQUERQUE", "PORTUGUESE COMMANDER", s[4] + 0.4, en[4] + 0.2, x=300),
    M(BALBOA, s[5] + 3.4, s[5] + 5.4, SPC, kind="conquistador", soldiers=6, ships=False, until=en[5] + 0.3),
    PP("balboa", "VASCO NÚÑEZ DE BALBOA", "SPANISH EXPLORER", s[5] + 0.4, en[5] + 0.2),
    M(SELIM, s[6] + 0.4, s[6] + 2.6, OTC, kind="janissary", soldiers=9, until=REF),
    PP("selim", "SULTAN SELIM I", "OTTOMAN EMPIRE", s[6] + 0.4, REF, x=300),
    M(MAG1, s[7] + 0.3, en[7] - 0.2, SPC, kind="conquistador", soldiers=15, sea_only=True, until=en[7] + 0.3),
    PP("magellan", "FERDINAND MAGELLAN", "SAILING FOR SPAIN", s[7] + 0.4, en[7] + 0.2),
    M(MAG2, s[8] + 0.2, s[8] + 3.2, SPC, kind="conquistador", soldiers=9, sea_only=True, until=s[8] + 3.4),
    M(MAG3, s[8] + 3.2, en[8] + 0.2, SPC, kind="conquistador", soldiers=9, sea_only=True, until=en[8] + 0.3),
    M(MAG4, s[9] + 0.1, s[9] + 2.8, SPC, kind="conquistador", soldiers=9, sea_only=True, until=s[9] + 3.2),
    M(LANDING, s[9] + 3.2, s[9] + 4.6, SPC, kind="conquistador", soldiers=3, ships=False, until=en[9] + 0.3),
    M(LAPU, s[9] + 3.8, s[9] + 5.4, VIS, kind="visayan", soldiers=3, ships=False, until=en[9] + 0.3),
    PP("magellan", "FERDINAND MAGELLAN", "KILLED ON MACTAN", s[9] + 0.4, en[9] + 0.2, x=300),
    M(CORTES, s[10] + 0.3, s[10] + 3.3, SPC, kind="conquistador", soldiers=6, until=en[10] + 0.3),
    M(ALLIES, s[10] + 0.7, s[10] + 3.3, TLX, kind="aztec", soldiers=6, until=en[10] + 0.3),
    IC("fire", (-99.13, 19.9), s[10] + 3.3, en[10] + 0.2),
    PP("cortes", "HERNÁN CORTÉS", "SPANISH CONQUISTADOR", s[10] + 0.4, en[10] + 0.2, x=300),
    IC("spice", (136.0, 6.5), s[11] + 0.5, s[11] + 2.6),
    M(VICT, s[11] + 0.4, en[11] - 0.4, SPC, kind="conquistador", soldiers=1, sea_only=True, until=en[11] + 0.3),
    PP("elcano", "JUAN SEBASTIÁN ELCANO", "CAPTAIN OF THE VICTORIA", s[11] + 0.4, s[11] + 3.4, x=300),
    PP("elcano", "JUAN SEBASTIÁN ELCANO", "CAPTAIN OF THE VICTORIA", s[11] + 3.6, en[11] + 0.2),
]
routes = [dict(pts=HOOK_E, t0=2.8, t1=en[0] - 0.1, until=en[0] + 0.5, color=GOLD),
          dict(pts=CABRAL, t0=s[2] + 0.3, t1=s[2] + 4.4, until=en[2] + 0.3, color=GOLD),
          dict(pts=ALBU, t0=s[4] + 0.3, t1=s[4] + 3.4, until=en[4] + 0.3, color=GOLD),
          dict(pts=MAG1, t0=s[7] + 0.3, t1=en[7] - 0.2, until=en[11] + 0.3, color=GOLD),
          dict(pts=MAG2, t0=s[8] + 0.2, t1=s[8] + 3.2, until=en[11] + 0.3, color=GOLD),
          dict(pts=MAG3, t0=s[8] + 3.2, t1=en[8] + 0.2, until=en[11] + 0.3, color=GOLD),
          dict(pts=MAG4, t0=s[9] + 0.1, t1=s[9] + 2.8, until=en[11] + 0.3, color=GOLD),
          dict(pts=VICT, t0=s[11] + 0.4, t1=en[11] - 0.4, until=s[12] + 0.3, color=GOLD)]
labels += WP.labels(B, 1522, s[1] + 0.8, s[12])

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
    put(fr, glow_text("YEAR 1533", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE FALL OF THE INCA", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=13, dur=DUR, base_a="/home/claude/shortgen/hd_1498.png", base_b="/home/claude/shortgen/hd_1522.png",
           regions="/home/claude/shortgen/regions_ep13_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[3] + 2.6, 0.2), (s[6] + 1.0, 0.2), (s[9] + 4.4, 0.25), (s[10] + 3.3, 0.25), (en[11] - 1.0, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
