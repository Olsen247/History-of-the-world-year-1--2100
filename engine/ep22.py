"""Episode 22 – Year 1914: the road to the First World War.
Italy invades Libya + first air raid (1911), Puyi abdicates (Feb 1912), Titanic (Apr 1912), First Balkan War (Oct 1912),
Second Balkan War (1913), two armed camps (1914), Sarajevo (28 Jun 1914), Austria-Hungary declares war on Serbia (28 Jul) and Russia
mobilises, Germany declares war and invades Belgium, Britain enters (Aug), the Marne and the trench line by Christmas 1914."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1914)
import world_data_1911 as A, world_data_1913 as M, world_data_1914 as B, world_data_1914w as W
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep22/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (15.0, 33.0, 2850)
shots = [(14.0, 48.5, 1300), WIDE, (15.0, 31.5, 1000), (110.0, 32.0, 1700), (-26.0, 47.0, 1900), (22.6, 41.7, 400), (24.4, 42.3, 420),
         (17.0, 49.5, 1300), (18.4, 43.9, 210), (20.6, 44.6, 420), (4.2, 49.9, 360), (3.6, 49.3, 360), (15.0, 45.0, 2850)]
EXTRA = {2: [(3.4, None), (4.1, (13.25, 32.8, 300))], 9: [(2.8, None), (3.5, (27.0, 49.5, 1700))], 11: [(3.6, None), (4.4, (4.8, 49.0, 620))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, 18.4, 43.9, 260), (2.2, 18.4, 44.2, 360), (3.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

SW1 = s[6] - 0.85; SW2 = s[7] - 0.85; SW3 = s[12] - 0.85
UA, UB, UC = SW1 + 0.7, SW2 + 0.7, SW3 + 0.7
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("libya_coast", s[2] + 1.6, s[2] + 3.6, UA), rv("china", s[3] + 0.8, s[3] + 4.0, UA), rv("libya_rest", s[5] + 1.0, s[5] + 3.0, UA),
           rv("montenegro", s[5] + 0.8, s[5] + 2.6, UA), rv("serbia", s[5] + 1.0, s[5] + 3.6, UA), rv("greece", s[5] + 1.2, s[5] + 3.8, UA),
           rv("bulgaria", s[5] + 1.0, s[5] + 3.8, UA), rv("albania", s[5] + 4.0, s[5] + 5.2, UA),
           rv("edirne", s[6] + 2.2, s[6] + 4.8, UB), rv("greece2", s[6] + 2.6, s[6] + 4.4, UB), rv("dobruja", s[6] + 3.0, s[6] + 5.0, UB),
           rv("occ", s[10] + 1.6, s[10] + 6.4, UC)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); GRN = (110, 210, 150)
H0 = en[0] + 0.2
labels = [lab(B, "AUSTRIA-HUNGARY", kind="mid", pos=(17.6, 45.4), t_in=0.5, t_out=2.6), lab(B, "SERBIA", kind="small", pos=(20.9, 43.6), t_in=0.6, t_out=2.6),
          lab(B, "GERMAN EMPIRE", pos=(10.5, 51.6), t_in=3.0, t_out=H0), lab(B, "AUSTRIA-HUNGARY", kind="mid", pos=(17.5, 47.6), t_in=3.1, t_out=H0),
          lab(B, "RUSSIAN EMPIRE", "RUSSIA", kind="emp", pos=(27.0, 56.0), t_in=3.2, t_out=H0), lab(B, "FRENCH EMPIRE", "FRANCE", kind="emp", pos=(2.4, 46.8), t_in=3.3, t_out=H0),
          lab(B, "BRITISH EMPIRE", "BRITAIN", kind="mid", pos=(-1.8, 52.8), t_in=3.4, t_out=H0),
          # 1911 Libya
          lab(A, "ITALY", pos=(13.0, 42.3), kind="mid", t_in=s[2] + 0.4, t_out=en[2] + 0.2),
          lab(A, "OTTOMAN EMPIRE", "OTTOMAN\nLIBYA", kind="mid", pos=(17.5, 28.0), t_in=s[2] + 0.4, t_out=s[2] + 2.6),
          lab(M, "ITALY", "ITALIAN\nLIBYA", kind="mid", pos=(17.5, 28.0), t_in=s[2] + 3.0, t_out=s[2] + 3.6),
          # 1912 China
          lab(A, "QING EMPIRE", pos=(103.0, 36.0), t_in=s[3] + 0.3, t_out=s[3] + 1.4),
          lab(M, "REPUBLIC OF CHINA", kind="emp", pos=(106.0, 31.0), t_in=s[3] + 2.8, t_out=en[3] + 0.2),
          lab(M, "MONGOLIA", kind="mid", pos=(103.0, 46.8), t_in=s[3] + 3.0, t_out=en[3] + 0.2),
          # 1912 Titanic
          lab(A, "BRITISH EMPIRE", "BRITAIN", kind="mid", pos=(-2.0, 53.3), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(A, "UNITED STATES", kind="mid", pos=(-82.0, 40.0), t_in=s[4] + 0.6, t_out=en[4] + 0.2),
          # 1912 First Balkan War
          lab(A, "OTTOMAN EMPIRE", kind="mid", pos=(22.4, 41.25), t_in=s[5] + 0.2, t_out=s[5] + 1.6),
          lab(M, "SERBIA", kind="mid", pos=(20.4, 44.3), t_in=s[5] + 1.8, t_out=en[5] + 0.2),
          lab(M, "BULGARIA", kind="mid", pos=(25.2, 42.6), t_in=s[5] + 1.8, t_out=en[5] + 0.2),
          lab(M, "GREECE", kind="mid", pos=(22.0, 39.3), t_in=s[5] + 2.0, t_out=en[5] + 0.2),
          lab(M, "MONTENEGRO", kind="small", pos=(18.6, 43.5), t_in=s[5] + 1.4, t_out=en[5] + 0.2),
          lab(M, "ALBANIA", kind="small", pos=(20.0, 40.9), t_in=s[5] + 4.6, t_out=en[5] + 0.2),
          # 1913 Second Balkan War
          lab(M, "BULGARIA", kind="mid", pos=(25.0, 42.6), t_in=s[6] + 0.3, t_out=en[6] + 0.2),
          lab(M, "SERBIA", kind="mid", pos=(21.3, 43.0), t_in=s[6] + 0.4, t_out=en[6] + 0.2),
          lab(B, "GREECE", kind="mid", pos=(22.4, 40.1), t_in=s[6] + 0.5, t_out=en[6] + 0.2),
          lab(B, "ROMANIA", kind="mid", pos=(24.6, 44.9), t_in=s[6] + 2.8, t_out=en[6] + 0.2),
          lab(B, "OTTOMAN EMPIRE", "OTTOMANS", kind="mid", pos=(28.3, 41.6), t_in=s[6] + 3.6, t_out=en[6] + 0.2),
          # 1914 two camps
          lab(B, "GERMAN EMPIRE", "GERMANY", kind="emp", pos=(10.0, 51.0), t_in=s[7] + 0.4, t_out=en[7] + 0.2),
          lab(B, "AUSTRIA-HUNGARY", kind="mid", pos=(17.5, 47.6), t_in=s[7] + 0.6, t_out=en[7] + 0.2),
          lab(B, "FRENCH EMPIRE", "FRANCE", kind="emp", pos=(2.0, 46.4), t_in=s[7] + 2.6, t_out=en[7] + 0.2),
          lab(B, "RUSSIAN EMPIRE", "RUSSIA", kind="emp", pos=(27.0, 56.0), t_in=s[7] + 2.8, t_out=en[7] + 0.2),
          lab(B, "BRITISH EMPIRE", "BRITAIN", kind="mid", pos=(-1.8, 52.8), t_in=s[7] + 3.0, t_out=en[7] + 0.2),
          # Sarajevo
          lab(B, "AUSTRIA-HUNGARY", kind="mid", pos=(17.6, 44.6), t_in=s[8] + 0.3, t_out=en[8] + 0.2),
          lab(B, "SERBIA", kind="mid", pos=(20.4, 43.75), t_in=s[8] + 0.4, t_out=en[8] + 0.2),
          # July
          lab(B, "AUSTRIA-HUNGARY", kind="mid", pos=(19.6, 45.9), t_in=s[9] + 0.3, t_out=s[9] + 3.0),
          lab(B, "SERBIA", kind="mid", pos=(21.3, 43.75), t_in=s[9] + 0.4, t_out=s[9] + 3.0),
          lab(B, "RUSSIAN EMPIRE", pos=(35.0, 51.0), t_in=s[9] + 3.6, t_out=en[9] + 0.2),
          # August / September
          lab(B, "GERMAN EMPIRE", "GERMANY", kind="emp", pos=(8.6, 50.6), t_in=s[10] + 0.3, t_out=en[11] + 0.2),
          lab(B, "FRENCH EMPIRE", "FRANCE", kind="emp", pos=(1.6, 47.4), t_in=s[10] + 0.3, t_out=en[11] + 0.2),
          lab(B, "BELGIUM", kind="small", pos=(4.3, 50.45), t_in=s[10] + 0.4, t_out=s[10] + 2.2),
          lab(B, "BRITISH EMPIRE", "BRITAIN", kind="mid", pos=(-1.2, 51.9), t_in=s[10] + 4.0, t_out=en[11] + 0.2),
          lab(B, "SWITZERLAND", kind="small", pos=(8.0, 46.75), t_in=s[11] + 4.4, t_out=en[11] + 0.2)]
labels += [ev("SARAJEVO", (18.41, 44.05), 0.3, 3.0),
           ev("TRIPOLI", (13.18, 33.2), s[2] + 1.0, en[2] + 0.2),
           ev("BEIJING", (116.4, 40.25), s[3] + 0.6, en[3] + 0.2, WT), ev("NANJING", (118.8, 32.4), s[3] + 0.8, en[3] + 0.2),
           ev("SOUTHAMPTON", (-6.5, 51.7), s[4] + 0.4, s[4] + 3.4, WT),            ev("TITANIC", (-49.95, 42.6), s[4] + 3.4, en[4] + 0.2),
           
           ev("SARAJEVO", (18.41, 44.0), s[8] + 0.6, en[8] + 0.2),
           ev("MOSCOW", (37.6, 56.0), s[9] + 3.6, en[9] + 0.2, WT), ev("WARSAW", (21.0, 52.45), s[9] + 3.8, en[9] + 0.2, WT),
           ev("LIÈGE", (4.9, 50.95), s[10] + 1.0, s[10] + 3.4), ev("PARIS", (1.9, 48.4), s[10] + 2.6, en[10] + 0.2, WT), ev("PARIS", (1.9, 48.4), s[11] + 4.2, en[11] + 0.2, WT),
           ev("THE MARNE", (2.9, 48.25), s[11] + 0.6, s[11] + 4.0), ev("NORTH SEA", (3.4, 52.7), s[11] + 4.4, en[11] + 0.2, CYN)]

ticker = [(0, 1914), (s[1], 1914), (s[1] + 1.3, 1911), (s[3], 1911), (s[3] + 0.6, 1912), (s[6], 1912), (s[6] + 0.6, 1913), (s[7], 1913),
          (s[7] + 0.6, 1914), (DUR, 1914)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1914", l2="THE ROAD TO WAR", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1911", GOLD), hd(2, "YEAR 1911", "ITALY INVADES LIBYA", GRN), hd(3, "YEAR 1912", "CHINA'S LAST EMPEROR", GOLD),
            hd(4, "YEAR 1912", "THE TITANIC SINKS", CYN), hd(5, "YEAR 1912", "THE FIRST BALKAN WAR"), hd(6, "YEAR 1913", "THE SECOND BALKAN WAR"),
            hd(7, "YEAR 1914", "TWO ARMED CAMPS", GOLD), hd(8, "YEAR 1914", "THE ASSASSINATION"), hd(9, "YEAR 1914", "WAR ON SERBIA"),
            hd(10, "AUGUST 1914", "EUROPE AT WAR"), hd(11, "SEPTEMBER 1914", "THE MARNE", CYN)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
ITC = (110, 185, 150); OTC = (200, 60, 60); SRC = (170, 90, 90); BGC = (110, 160, 90); GRC = (100, 160, 220); MNC = (150, 120, 180); ROC = (220, 190, 80)
TITANIC = [(-1.4, 50.75), (-1.6, 50.1), (-1.62, 49.7), (-4.5, 49.6), (-8.3, 51.6), (-15.0, 50.5), (-25.0, 48.0), (-38.0, 44.5), (-49.95, 41.73)]
FLIGHT = [(13.0, 33.0), (13.2, 32.85), (13.3, 32.75), (13.45, 32.62)]
P0 = [(6.05, 51.0), (6.1, 50.6), (6.35, 50.15), (6.3, 49.5), (6.4, 49.0), (6.9, 48.5), (7.1, 47.7)]
PM = [(3.0, 51.1), (2.9, 50.4), (2.6, 49.4), (2.85, 48.95), (4.5, 48.75), (5.6, 48.95), (7.0, 47.75)]
P1 = [(2.8, 51.1), (2.85, 50.5), (2.8, 49.95), (3.3, 49.38), (4.6, 49.25), (5.6, 48.95), (7.0, 47.75)]
WEST = [(6.0, 49.45), (6.6, 48.6), (7.0, 47.9), (7.2, 47.5)]
EAST = [(22.8, 54.4), (21.0, 53.1), (19.5, 52.9), (18.6, 51.6), (19.5, 50.2), (22.5, 50.3), (24.2, 50.0), (26.5, 48.3)]
DANUBE = [(19.1, 44.9), (19.9, 44.85), (20.5, 44.85), (21.4, 44.75), (22.4, 44.65)]
AL = ["be", "uk", "fr", "fr", "fr", "fr", "fr"]
fx = [
    PP("franzferdinand", "FRANZ FERDINAND", "HEIR TO AUSTRIA-HUNGARY", 0.5, 3.0, x=300),
    PP("princip", "GAVRILO PRINCIP", "THE ASSASSIN, AGE 19", 0.9, 3.0, x=780),
    # 1911 Libya
    M_([(15.0, 37.2), (14.0, 35.0), (13.18, 32.9)], s[2] + 0.6, s[2] + 2.6, ITC, kind="bersagliere", soldiers=6, until=s[2] + 4.0),
    M_([(14.3, 32.0), (13.8, 32.4), (13.5, 32.65)], s[2] + 1.0, s[2] + 2.8, OTC, kind="ottoman1912", soldiers=5, ships=False, until=s[2] + 3.8),
    VH("plane", FLIGHT, s[2] + 4.4, s[2] + 6.6, until=en[2] + 0.2),
    # 1912 China
    PP("puyi", "PUYI", "LAST EMPEROR, AGE 6", s[3] + 0.4, en[3] + 0.2),
    PP("sunyatsen", "SUN YAT-SEN", "PROVISIONAL PRESIDENT", s[3] + 2.0, en[3] + 0.2, x=300),
    # 1912 Titanic
    VH("steamer", TITANIC, s[4] + 0.4, s[4] + 3.6, until=s[4] + 4.3),
    PP("smith", "EDWARD SMITH", "CAPTAIN OF THE TITANIC", s[4] + 1.2, en[4] + 0.2),
    # 1912 First Balkan War
    M_([(21.0, 43.7), (21.2, 42.65), (21.45, 41.9)], s[5] + 0.6, s[5] + 3.4, SRC, kind="serb1912", soldiers=6, ships=False, until=en[5]),
    M_([(19.26, 42.44), (19.5, 42.07)], s[5] + 0.6, s[5] + 2.4, MNC, kind="montenegrin", soldiers=4, ships=False, until=s[5] + 3.6),
    M_([(22.4, 39.6), (22.6, 40.1), (22.94, 40.64)], s[5] + 0.8, s[5] + 3.6, GRC, kind="evzone", soldiers=6, ships=False, until=en[5]),
    M_([(26.0, 42.3), (26.55, 41.75), (27.8, 41.35)], s[5] + 0.8, s[5] + 3.8, BGC, kind="bulgar1912", soldiers=6, ships=False, until=en[5]),
    # 1913 Second Balkan War
    M_([(23.3, 42.0), (22.5, 41.7)], s[6] + 0.6, s[6] + 2.2, BGC, kind="bulgar1912", soldiers=5, ships=False, until=s[6] + 3.0),
    M_([(21.6, 41.6), (22.6, 41.75)], s[6] + 1.6, s[6] + 3.4, SRC, kind="serb1912", soldiers=5, ships=False, until=s[6] + 4.6),
    M_([(22.94, 40.75), (23.6, 41.0), (24.3, 41.1)], s[6] + 1.8, s[6] + 3.8, GRC, kind="evzone", soldiers=5, ships=False, until=s[6] + 5.0),
    M_([(27.6, 40.95), (27.0, 41.3), (26.6, 41.6)], s[6] + 2.2, s[6] + 4.6, OTC, kind="ottoman1912", soldiers=5, ships=False, until=en[6]),
    M_([(27.6, 44.4), (27.8, 43.95), (28.0, 43.6)], s[6] + 2.8, s[6] + 4.8, ROC, kind="dorobant", soldiers=5, ships=False, until=en[6]),
    # 1914 two camps
    dict(type="front", path0=WEST, t_in=s[7] + 2.4, t_out=en[7], side_a=["de1914"], side_b=["fr"], rows=1),
    dict(type="front", path0=EAST, t_in=s[7] + 3.0, t_out=en[7], side_a=["ru"], side_b=["de1914", "de1914", "de1914", "ah", "ah", "ah", "ah"], by_segment=True, rows=1),
    PP("wilhelm2", "WILHELM II", "GERMAN EMPEROR", s[7] + 0.4, en[7] + 0.2, x=300),
    PP("nicholas2", "NICHOLAS II", "TSAR OF RUSSIA", s[7] + 2.8, en[7] + 0.2),
    # Sarajevo
    PP("franzferdinand", "FRANZ FERDINAND", "HEIR TO AUSTRIA-HUNGARY", s[8] + 0.4, en[8] + 0.2, x=300),
    PP("princip", "GAVRILO PRINCIP", "BOSNIAN SERB, AGE 19", s[8] + 1.4, en[8] + 0.2),
    dict(type="glow", pos=(18.41, 43.86), t0=s[8] + 2.4, t1=s[8] + 4.4, radius=120, a0=40, a1=110),
    # July: war on Serbia, Russia mobilises by rail
    dict(type="front", path0=DANUBE, t_in=s[9] + 0.6, t_out=s[9] + 3.2, side_a=["ah"], side_b=["rs"], rows=2),
    PP("franzjoseph", "FRANZ JOSEPH", "EMPEROR OF AUSTRIA-HUNGARY", s[9] + 0.3, s[9] + 3.2, x=300),
    VH("train", [(37.6, 55.75), (32.0, 54.8), (27.55, 53.9), (23.7, 52.1), (21.0, 52.2)], s[9] + 3.6, en[9], until=en[9] + 0.2),
    VH("train", [(30.5, 50.45), (28.0, 50.0), (26.0, 49.9)], s[9] + 3.8, en[9], until=en[9] + 0.2),
    PP("nicholas2", "NICHOLAS II", "TSAR OF RUSSIA", s[9] + 3.4, en[9] + 0.2),
    # August: the Western Front
    dict(type="front", path0=P0, path1=PM, t_in=s[10] + 0.6, t_out=s[11] + 0.05, move0=s[10] + 1.4, move1=s[10] + 6.2, side_a=["de1914"], side_b=AL, by_segment=True, rows=2),
    dict(type="boom", pos=(5.57, 50.63), t0=s[10] + 1.8, swords=False, scale=0.36),
    dict(type="boom", pos=(4.0, 50.4), t0=s[10] + 3.6, swords=False, scale=0.32),
    VH("warship", [(-1.4, 50.7), (-0.6, 50.1), (0.1, 49.5)], s[10] + 4.2, s[10] + 6.4, until=en[10] + 0.2, scale=0.9),
    PP("wilhelm2", "WILHELM II", "GERMAN EMPEROR", s[10] + 0.4, s[10] + 3.6, x=780),
    # September: the Marne, trenches by Christmas
    dict(type="front", path0=PM, path1=P1, t_in=s[11], t_out=DUR, move0=s[11] + 1.0, move1=s[11] + 4.0, side_a=["de1914"], side_b=AL, by_segment=True, rows=2),
    dict(type="boom", pos=(3.3, 48.95), t0=s[11] + 0.8, swords=False, scale=0.4),
    VH("plane", [(1.5, 48.6), (2.6, 48.8), (3.6, 49.2)], s[11] + 0.6, s[11] + 3.4, scale=0.9),
    PP("joffre", "JOSEPH JOFFRE", "FRENCH COMMANDER", s[11] + 0.4, s[11] + 4.2, x=780),
    dict(type="glow", pos=(4.6, 49.6), t0=s[11] + 4.4, t1=en[11], radius=300, a0=40, a1=100),
]
routes = [dict(pts=TITANIC, t0=s[4] + 0.4, t1=s[4] + 3.6, until=en[4] + 0.2, color=(200, 200, 210))]
labels += WP.labels(A, 1911, s[1] + 0.8, SW1)
labels += WP.labels(M, 1913, SW1 + 0.6, SW2)
labels += WP.labels(B, 1914, SW2 + 0.6, s[12])

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
    put(fr, glow_text("YEAR 1922", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("AFTER THE GREAT WAR", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=22, dur=DUR, base_a="/home/claude/shortgen/hd_1911.png", base_b="/home/claude/shortgen/hd_1914.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1913.png", W="/home/claude/shortgen/hd_1914w.png"),
           regions="/home/claude/shortgen/regions_ep22_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1, SW1 + 0.6, "A", "M"), (SW2, SW2 + 0.6, "M", "B"), (SW3, SW3 + 0.6, "B", "W")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.6, 0.2), (s[3] + 0.8, 0.2), (s[4] + 3.6, 0.25), (s[5] + 1.0, 0.25),
                                              (s[6] + 2.2, 0.2), (s[7] + 2.4, 0.2), (s[8] + 2.4, 0.3), (s[9] + 0.6, 0.25), (s[10] + 1.6, 0.25),
                                              (s[11] + 0.8, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
