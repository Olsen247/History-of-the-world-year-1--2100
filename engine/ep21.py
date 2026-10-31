"""Episode 21 – Year 1911: Australia federates and Queen Victoria dies (1901), the Boer War ends (1902), the Wright brothers fly (1903),
Tsushima (1905), Norway leaves the union with Sweden (1905), Belgium takes the Congo from Leopold II (1908), Japan annexes Korea (1910),
the Mexican Revolution (Nov 1910), the Wuchang uprising and China's revolution (Oct 1911), Amundsen at the South Pole (14 Dec 1911).
The Mercator map stops at 56 S, so the race to the Pole is shown on a south-polar disc (polar.py)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1911)
import world_data_1900 as A, world_data_1911 as B
import world_peoples as WP
import polar

S = eval(open("/home/claude/shortgen/vo_ep21/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10.0, 28.0, 2850)
shots = [(108.0, 33.0, 1700), WIDE, (134.0, -27.0, 1400), (27.5, -27.5, 700), (-76.4, 36.3, 420), (22.0, 38.0, 2850), (15.0, 59.5, 900),
         (22.0, -4.0, 1100), (128.5, 38.0, 700), (-103.0, 21.5, 900), (110.0, 31.5, 1700), (170.0, -45.0, 2000), (60.0, 22.0, 2850)]
EXTRA = {2: [(3.9, None), (4.7, (-1.0, 52.5, 900))], 5: [(0.9, None), (1.7, (35.0, -12.0, 2850)), (2.5, (95.0, 6.0, 2850)), (3.1, (124.0, 30.0, 2200)), (3.8, (133.0, 40.0, 1200))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, 112.0, 30.0, 2000), (2.6, 110.0, 32.0, 1850), (5.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

SWB = s[12] - 0.85
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
U = SWB + 1.2
reveals = [rv("boer", s[3] + 2.6, s[3] + 4.8, U), rv("kwantung", s[5] + 5.0, s[5] + 5.8, U), rv("sakh", s[5] + 5.0, s[5] + 6.6, U),
           rv("norway", s[6] + 0.8, s[6] + 3.6, U), rv("congo", s[7] + 3.0, s[7] + 5.6, U), rv("korea", s[8] + 0.8, s[8] + 3.2, U),
           rv("china_rev", s[10] + 1.0, s[10] + 5.0, U), rv("mongolia", s[10] + 5.0, s[10] + 6.6, U)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200)
H0 = en[0] + 0.2
GB = "BRITISH EMPIRE"
labels = [lab(B, "CHINESE REVOLUTION", "REVOLUTION", kind="emp", pos=(106.5, 28.5), t_in=3.4, t_out=H0),
          lab(B, "QING EMPIRE", "QING EMPIRE", kind="mid", pos=(122.0, 43.5), t_in=3.6, t_out=H0),
          lab(B, "MONGOLIA", kind="small", pos=(103.0, 47.0), t_in=3.8, t_out=H0),
          # 1901
          lab(A, GB, "AUSTRALIA", kind="emp", pos=(134.0, -24.5), t_in=s[2] + 0.6, t_out=s[2] + 4.0),
          # 1902
          lab(A, "TRANSVAAL", kind="small", pos=(30.2, -23.6), t_in=s[3] + 0.4, t_out=s[3] + 3.4),
          lab(A, "ORANGE FREE STATE", "ORANGE\nFREE STATE", kind="small", pos=(25.3, -29.5), t_in=s[3] + 0.5, t_out=s[3] + 3.4),
          lab(B, GB, "BRITISH", kind="mid", pos=(26.5, -29.2), t_in=s[3] + 4.4, t_out=en[3] + 0.2),
          # 1903
          lab(A, "UNITED STATES", "UNITED STATES", kind="mid", pos=(-77.8, 37.3), t_in=s[4] + 0.4, t_out=en[4] + 0.2),
          # 1905
          lab(A, "RUSSIAN EMPIRE", pos=(30.0, 57.0), t_in=s[5] + 0.4, t_out=s[5] + 3.0),
          lab(A, "JAPAN", pos=(138.5, 36.6), t_in=s[5] + 3.8, t_out=en[5] + 0.2),
          lab(A, "RUSSIAN EMPIRE", "RUSSIA", kind="mid", pos=(131.0, 47.5), t_in=s[5] + 3.8, t_out=en[5] + 0.2),
          lab(A, "NORWAY", pos=(9.0, 61.6), t_in=s[6] + 2.4, t_out=en[6] + 0.2),
          lab(A, "SWEDEN", pos=(16.0, 63.5), t_in=s[6] + 0.4, t_out=en[6] + 0.2),
          # 1908
          lab(A, "CONGO FREE STATE", "CONGO\nFREE STATE", kind="mid", pos=(23.0, -2.5), t_in=s[7] + 0.4, t_out=s[7] + 3.2),
          lab(B, "BELGIAN CONGO", "BELGIAN\nCONGO", kind="mid", pos=(23.0, -2.5), t_in=s[7] + 4.6, t_out=en[7] + 0.2),
          # 1910
          lab(A, "KOREAN EMPIRE", "KOREA", kind="mid", pos=(127.9, 39.7), t_in=s[8] + 0.3, t_out=s[8] + 2.2),
          lab(B, "JAPAN", "JAPANESE\nKOREA", kind="mid", pos=(127.9, 39.7), t_in=s[8] + 3.0, t_out=en[8] + 0.2),
          lab(B, "JAPAN", pos=(133.6, 34.6), kind="mid", t_in=s[8] + 0.5, t_out=en[8] + 0.2),
          lab(A, "MEXICO", pos=(-99.3, 26.6), t_in=s[9] + 0.3, t_out=en[9] + 0.2),
          lab(A, "UNITED STATES", "UNITED STATES", kind="mid", pos=(-99.0, 33.5), t_in=s[9] + 0.6, t_out=en[9] + 0.2),
          # 1911
          lab(A, "QING EMPIRE", pos=(103.0, 36.0), t_in=s[10] + 0.3, t_out=s[10] + 3.0),
          lab(B, "CHINESE REVOLUTION", "REVOLUTION", kind="emp", pos=(109.5, 26.5), t_in=s[10] + 4.0, t_out=en[10] + 0.2),
          lab(B, "QING EMPIRE", "QING", kind="mid", pos=(98.0, 37.5), t_in=s[10] + 4.2, t_out=en[10] + 0.2),
          lab(B, "MONGOLIA", kind="mid", pos=(103.0, 46.8), t_in=s[10] + 5.8, t_out=en[10] + 0.2)]
labels += [ev("SYDNEY", (151.2, -33.2), s[2] + 0.8, s[2] + 4.0, WT), ev("MELBOURNE", (145.0, -37.1), s[2] + 0.9, s[2] + 4.0, WT),
           ev("LONDON", (-0.12, 52.1), s[2] + 4.6, en[2] + 0.2),
           ev("PRETORIA", (28.19, -25.3), s[3] + 0.6, en[3] + 0.2, WT),            ev("KITTY HAWK", (-76.9, 35.95), s[4] + 0.6, en[4] + 0.2),
           ev("TSUSHIMA", (128.3, 32.7), s[5] + 4.0, en[5] + 0.2), ev("PORT ARTHUR", (121.2, 39.4), s[5] + 5.6, en[5] + 0.2, WT),
           ev("SAKHALIN", (145.6, 47.8), s[5] + 5.8, en[5] + 0.2, WT),
           ev("KRISTIANIA", (9.3, 59.7), s[6] + 0.6, en[6] + 0.2), ev("STOCKHOLM", (18.9, 58.9), s[6] + 0.8, en[6] + 0.2, WT),
           ev("BOMA", (13.05, -5.3), s[7] + 2.8, en[7] + 0.2),
           ev("SEOUL", (126.5, 37.3), s[8] + 0.6, en[8] + 0.2),
           ev("MEXICO CITY", (-94.6, 17.9), s[9] + 0.8, en[9] + 0.2),
           ev("WUCHANG", (111.0, 30.4), s[10] + 0.6, en[10] + 0.2), ev("BEIJING", (116.4, 40.25), s[10] + 3.4, en[10] + 0.2, WT),
           ev("NANJING", (120.8, 33.2), s[10] + 3.2, en[10] + 0.2, WT)]

ticker = [(0, 1911), (s[1], 1911), (s[1] + 1.3, 1900), (s[2], 1900), (s[2] + 0.6, 1901), (s[3], 1901), (s[3] + 0.6, 1902), (s[4], 1902),
          (s[4] + 0.6, 1903), (s[5], 1903), (s[5] + 0.6, 1905), (s[7], 1905), (s[7] + 0.6, 1908), (s[8], 1908), (s[8] + 0.6, 1910),
          (s[10], 1910), (s[10] + 0.6, 1911), (DUR, 1911)]
RRED = (232, 64, 72); GRN = (110, 210, 150); PNK = (240, 140, 175)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1911", l2="THE RACE TO THE POLE", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1900", GOLD), hd(2, "YEAR 1901", "A NEW CENTURY", CYN), hd(3, "YEAR 1902", "THE BOER WAR ENDS"),
            hd(4, "YEAR 1903", "THE FIRST FLIGHT", CYN), hd(5, "YEAR 1905", "TSUSHIMA"), hd(6, "YEAR 1905", "NORWAY IS FREE", GOLD),
            hd(7, "YEAR 1908", "THE BELGIAN CONGO", PNK), hd(8, "YEAR 1910", "JAPAN TAKES KOREA"), hd(9, "YEAR 1910", "THE MEXICAN REVOLUTION", GRN),
            hd(10, "YEAR 1911", "CHINA'S REVOLUTION"), hd(11, "YEAR 1911", "THE SOUTH POLE", CYN)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
KHK = (170, 150, 100); BOER = (120, 95, 60); RUC = (60, 110, 60); JPC = (200, 50, 50); RVC = (60, 140, 70); FED = (60, 70, 110); CNR = (205, 45, 55)
DURBAN = [(31.0, -29.85), (30.4, -29.0), (29.8, -28.0), (29.0, -27.0), (28.2, -26.3)]
KIMB = [(24.8, -28.75), (25.5, -28.95), (26.2, -29.1), (27.2, -27.5), (28.0, -26.0)]
BOERS = [(28.19, -25.75), (28.3, -26.6), (28.5, -27.4)]
FLIGHT = [(-75.67, 36.0), (-75.62, 36.06), (-75.55, 36.13)]
BALTIC = [(21.0, 56.5), (11.0, 57.8), (3.0, 52.0), (-5.0, 48.0), (-10.0, 43.0), (-17.0, 28.0), (-18.5, 14.0), (-12.0, 4.0), (5.0, -2.0),
          (10.0, -15.0), (14.5, -30.0), (19.0, -37.0), (30.0, -35.5), (44.0, -26.0), (48.3, -13.4), (60.0, -6.0), (80.0, 2.0), (95.0, 5.5),
          (103.8, 1.6), (108.5, 10.0), (113.0, 17.0), (119.0, 22.5), (123.5, 28.5), (127.5, 32.5), (129.6, 34.2)]
RU_FLEET = [(125.5, 31.0), (127.4, 32.6), (128.8, 33.6), (129.5, 34.2)]
RU_FLEET2 = [(126.0, 30.6), (127.8, 32.2), (129.1, 33.4), (129.8, 34.0)]
JP_FLEET = [(128.6, 35.1), (129.1, 34.8), (129.6, 34.5)]
JP_FLEET2 = [(130.5, 34.9), (130.2, 34.6), (129.9, 34.4)]
JUAREZ = [(-106.45, 31.7), (-106.1, 29.5), (-105.5, 27.6), (-104.0, 25.6), (-103.0, 24.2)]
JUAREZ2 = [(-108.5, 30.5), (-107.5, 29.0), (-106.0, 27.4), (-104.8, 26.0)]
FEDS = [(-99.13, 19.43), (-99.8, 20.6), (-100.8, 21.9), (-101.6, 23.0)]
WU = (114.3, 30.55)
WU_CS = [WU, (113.6, 29.6), (113.0, 28.2)]
WU_JX = [WU, (115.2, 29.6), (115.9, 28.7)]
WU_NJ = [WU, (116.0, 31.0), (117.6, 31.6), (118.8, 32.05)]
WU_XA = [WU, (112.5, 31.8), (110.5, 33.2), (108.9, 34.3)]
fx = [
    PP("amundsen", "ROALD AMUNDSEN", "POLAR EXPLORER", 0.5, 3.2, x=780),
    PP("puyi", "PUYI", "EMPEROR OF CHINA, AGE 5", 3.4, en[0] + 0.2, x=780),
    dict(type="cities", cities=[(151.2, -33.87, 1.1), (144.96, -37.81, 1.1), (153.0, -27.47, 0.7), (138.6, -34.93, 0.7), (115.86, -31.95, 0.6)],
         t0=s[2] + 0.4, t1=s[2] + 1.6, until=s[2] + 4.0),
    PP("victoria", "QUEEN VICTORIA", "QUEEN 1837-1901", s[2] + 4.2, en[2] + 0.2),
    M_(DURBAN, s[3] + 0.5, s[3] + 3.4, KHK, kind="tommy", soldiers=6, ships=False, until=s[3] + 4.2),
    M_(BOERS, s[3] + 0.6, s[3] + 2.4, BOER, kind="boer", soldiers=5, ships=False, until=s[3] + 3.0),
    VH("plane", FLIGHT, s[4] + 1.6, s[4] + 4.6, until=en[4] + 0.2),
    PP("wilbur", "WILBUR WRIGHT", "AVIATION PIONEER", s[4] + 0.4, en[4] + 0.2, x=300),
    PP("orville", "ORVILLE WRIGHT", "FLEW FIRST, 12 SECONDS", s[4] + 1.2, en[4] + 0.2),
    VH("steamer", RU_FLEET, s[5] + 3.6, s[5] + 5.4, until=en[5] + 0.3), VH("steamer", RU_FLEET2, s[5] + 3.8, s[5] + 5.6, until=en[5] + 0.3),
    VH("steamer", JP_FLEET, s[5] + 3.8, s[5] + 5.2, until=en[5] + 0.3), VH("steamer", JP_FLEET2, s[5] + 4.0, s[5] + 5.4, until=en[5] + 0.3),
    PP("togo", "TOGO HEIHACHIRO", "ADMIRAL OF JAPAN", s[5] + 3.8, en[5] + 0.2),
    PP("haakon7", "HAAKON VII", "KING OF NORWAY", s[6] + 3.0, en[6] + 0.2),
    PP("leopold2", "LEOPOLD II", "KING OF THE BELGIANS", s[7] + 0.4, s[7] + 3.6, x=300),
    M_(JUAREZ, s[9] + 0.8, s[9] + 4.4, RVC, kind="revolucionario", soldiers=7, ships=False, until=en[9] + 0.2),
    M_(JUAREZ2, s[9] + 1.2, s[9] + 4.4, RVC, kind="revolucionario", soldiers=6, ships=False, until=en[9] + 0.2),
    M_(FEDS, s[9] + 2.2, s[9] + 4.4, FED, kind="rifleman", soldiers=5, ships=False, until=en[9] + 0.2),
    PP("diaz", "PORFIRIO DIAZ", "PRESIDENT OF MEXICO", s[9] + 0.4, en[9] + 0.2, x=300),
    PP("madero", "FRANCISCO MADERO", "LEADER OF THE REVOLUTION", s[9] + 2.4, en[9] + 0.2),
    M_(WU_CS, s[10] + 1.0, s[10] + 3.4, CNR, kind="newarmy", soldiers=5, ships=False, until=s[10] + 4.4),
    M_(WU_JX, s[10] + 1.3, s[10] + 3.6, CNR, kind="newarmy", soldiers=5, ships=False, until=s[10] + 4.4),
    M_(WU_NJ, s[10] + 1.6, s[10] + 4.0, CNR, kind="newarmy", soldiers=5, ships=False, until=s[10] + 4.6),
    M_(WU_XA, s[10] + 1.8, s[10] + 4.2, CNR, kind="newarmy", soldiers=5, ships=False, until=s[10] + 4.6),
    PP("sunyatsen", "SUN YAT-SEN", "REVOLUTIONARY LEADER", s[10] + 0.4, en[10] + 0.2, x=300),
    PP("puyi", "PUYI", "EMPEROR OF CHINA, AGE 5", s[10] + 2.6, en[10] + 0.2),
    PP("amundsen", "ROALD AMUNDSEN", "FIRST AT THE SOUTH POLE", s[11] + 0.6, en[11] + 0.2),
    PP("scott", "ROBERT FALCON SCOTT", "ROYAL NAVY CAPTAIN", s[11] + 2.2, en[11] + 0.2, x=300),
]
routes = [dict(pts=BALTIC, t0=s[5] + 0.4, t1=s[5] + 3.0, until=s[5] + 4.4, color=(200, 200, 210))]
labels += WP.labels(A, 1905, s[1] + 0.8, SWB)
labels += WP.labels(B, 1911, SWB + 1.1, s[12])

def hook(fr, t):
    polar.draw(fr, t, 0.15, 3.1, cy=770, size=0.85, amund=(0.6, 2.4), scott=(0.8, 2.8))
    polar.draw(fr, t, s[11], en[11] + 0.1, cy=770, size=0.9, amund=(1.0, 4.4), scott=(1.4, 5.6))

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
    put(fr, glow_text("YEAR 1914", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE ROAD TO WAR", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=21, dur=DUR, base_a="/home/claude/shortgen/hd_1900.png", base_b="/home/claude/shortgen/hd_1911.png",
           regions="/home/claude/shortgen/regions_ep21_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB, SWB + 1.1, "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=hook, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 4.2, 0.2), (s[3] + 2.6, 0.25), (s[4] + 1.6, 0.2), (s[5] + 3.8, 0.25),
                                              (s[6] + 0.8, 0.25), (s[7] + 3.0, 0.2), (s[8] + 0.8, 0.25), (s[9] + 0.8, 0.2), (s[10] + 1.0, 0.25),
                                              (s[11] + 0.2, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
