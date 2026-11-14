"""Episode 27 – Year 1941: the Second World War, part 2 – Blitzkrieg to Pearl Harbor.
Winter War (30 Nov 1939 - 13 Mar 1940, Finnish ski troops, Mannerheim Line, Karelia ceded); Weserübung (9 Apr 1940: Denmark and
Norway, Blücher sunk at Drøbak by Oscarsborg's guns and torpedoes); Fall Gelb (10 May 1940: Netherlands, Belgium, the panzers through
the Ardennes, Sedan 13 May, Abbeville and the Channel 20 May); Dynamo (26 May - 4 Jun, 338,226 men); Paris (14 Jun), armistice (22 Jun);
Battle of Britain (Jul-Oct 1940, Chain Home radar, Spitfires and Hurricanes, Sea Lion postponed 17 Sep); Afrika Korps (Tripoli, Feb
1941); Yugoslavia and Greece (6-30 Apr 1941); Barbarossa (22 Jun 1941: ~3 million German soldiers, ~3,350 tanks, three army groups);
Kiev pocket (Sep 1941), Babi Yar (29-30 Sep 1941, 33,771 Jews murdered); Moscow (Germans stopped, Soviet counter-offensive 5 Dec);
Pearl Harbor (7 Dec 1941: six carriers, 353 aircraft, all eight battleships damaged)."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1941)
import world_data_1939 as A_, world_data_1940 as G_, world_data_1941 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep27/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(24.0, 52.0, 2300), (14.0, 54.0, 2850), (29.0, 62.0, 950), (10.5, 60.0, 1000), (4.0, 50.0, 820), (1.8, 50.2, 760),
         (-0.5, 51.6, 820), (19.0, 37.5, 1800), (27.0, 53.0, 1700), (31.5, 51.5, 1150), (36.5, 55.3, 950), (-158.0, 23.6, 700),
         (10.0, 45.0, 2900)]
ZOOM = {3: (s[3] + 3.3, (10.62, 59.62, 420)), 5: (s[5] + 3.9, (2.6, 47.6, 1150)), 9: (s[9] + 3.3, (30.6, 50.6, 800)),
        11: (s[11] + 2.6, (-157.95, 21.45, 420))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, 22.0, 51.0, 2000), (3.0, *shots[0])]
for i in range(1, len(shots)):
    if i == 11:   # Moscow -> Hawaii: pull far out over the world, then drop onto Oahu
        keys += [(s[i] - 0.85, *endshot[i - 1]), (s[i] - 0.2, -60.0, 40.0, 2950), (s[i] + 0.7, *shots[i])]
        continue
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))
for i, (t, sh) in ZOOM.items(): keys += [(t - 0.6, *shots[i]), (t + 0.6, *sh)]
keys = sorted(keys, key=lambda k: k[0])

SWG = (s[6] - 0.85, s[6] - 0.25)          # 1939 -> 1940 map while flying from France to Britain
SWB = (s[12] - 0.85, s[12] - 0.25)        # 1940 -> 1941 map for the outro
UG, UB = SWG[1] + 0.1, SWB[1] + 0.1
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("karelia", s[2] + 5.4, s[2] + 7.4, UG),
           rv("denmark", s[3] + 0.4, s[3] + 2.2, UG), rv("norway", s[3] + 1.0, s[3] + 5.0, UG),
           rv("neth", s[4] + 0.3, s[4] + 2.0, UG), rv("belg", s[4] + 0.5, s[4] + 2.4, UG), rv("france_n", s[4] + 1.4, s[4] + 4.6, UG),
           rv("france_s", s[5] + 4.0, s[5] + 6.6, UG),
           rv("yugo", s[7] + 3.4, s[7] + 5.8, UB), rv("greece", s[7] + 3.9, s[7] + 6.6, UB),
           rv("barb_w", s[8] + 0.8, s[8] + 5.6, UB), rv("finkar", s[9] + 0.6, s[9] + 3.0, UB), rv("barb_e", s[9] + 0.4, s[10] + 2.2, UB)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250); BRC = (235, 125, 165)
DEC = (175, 175, 190); FRC = (120, 150, 240); SOVC = (150, 200, 110); JPC = (245, 120, 95); ITC = (120, 200, 160); FIC = (225, 230, 245)
NOC = (235, 120, 120)
labels = [
    # hook: Europe in 1941
    lb("GERMANY", (11.0, 51.0), 0.6, en[0] + 0.2, DEC, kind="emp"), lb("SOVIET UNION", (40.0, 57.0), 0.9, en[0] + 0.2, SOVC, kind="emp"),
    lb("BRITAIN", (-2.2, 53.4), 1.2, en[0] + 0.2, BRC), 
    # Winter War
    lb("FINLAND", (26.0, 63.4), s[2] + 0.3, en[2] + 0.2, FIC, kind="emp"), lb("SOVIET UNION", (35.5, 63.8), s[2] + 0.4, en[2] + 0.2, SOVC),
    ev("MANNERHEIM LINE", (26.2, 60.2), s[2] + 2.0, s[2] + 5.2),
    ev("SUOMUSSALMI", (27.6, 66.3), s[2] + 2.6, s[2] + 5.6, WT), lb("KARELIA", (31.2, 61.4), s[2] + 5.8, en[2] + 0.2, SOVC, kind="small"),
    # Norway
    lb("NORWAY", (9.0, 62.2), s[3] + 0.3, s[3] + 3.0, NOC), lb("DENMARK", (9.2, 56.3), s[3] + 0.3, s[3] + 2.8, NOC, kind="small"),
    ev("OSLO", (10.75, 60.1), s[3] + 1.4, s[3] + 3.0, WT), ev("NARVIK", (17.4, 68.7), s[3] + 1.6, s[3] + 3.0, WT),
    ev("DRØBAK", (11.3, 60.0), s[3] + 3.9, en[3] + 0.2),
    # the West
    ev("ARDENNES", (5.8, 50.6), s[4] + 0.3, s[4] + 1.3), ev("SEDAN", (5.0, 48.95), s[4] + 1.4, s[4] + 3.4, WT),
    ev("ABBEVILLE", (1.83, 50.3), s[4] + 3.6, en[4] + 0.2, WT), lb("ENGLISH CHANNEL", (0.3, 50.45), s[4] + 3.8, en[4] + 0.2, CYN, kind="small"),
    lb("FRANCE", (2.6, 48.6), s[4] + 0.4, s[4] + 3.4, FRC), lb("BELGIUM", (4.6, 50.85), s[4] + 0.4, s[4] + 2.6, NOC, kind="small"),
    lb("NETHERLANDS", (5.4, 53.4), s[4] + 0.4, s[4] + 2.6, NOC, kind="small"),
    ev("DUNKIRK", (3.0, 51.65), s[5] + 0.2, s[5] + 3.8),
    ev("PARIS", (2.35, 49.1), s[5] + 5.0, en[5] + 0.2), lb("VICHY FRANCE", (3.3, 45.3), s[5] + 5.6, en[5] + 0.2, FRC, kind="small"),
    # Battle of Britain
    ev("LONDON", (-1.0, 52.2), s[6] + 0.3, en[6] + 0.2, WT), ev("RADAR", (2.6, 52.9), s[6] + 0.9, s[6] + 3.2),
    lb("OCCUPIED FRANCE", (1.0, 49.4), s[6] + 0.4, en[6] + 0.2, DEC, kind="small"),
    # Africa and the Balkans
    ev("TRIPOLI", (11.2, 34.4), s[7] + 0.4, s[7] + 3.4, WT), lb("LIBYA", (17.5, 28.0), s[7] + 0.5, s[7] + 3.4, ITC),
    lb("ITALY", (13.0, 42.4), s[7] + 0.4, en[7] + 0.2, ITC, kind="small"),
    ev("BELGRADE", (20.6, 43.6), s[7] + 3.5, en[7] + 0.2, WT), ev("ATHENS", (24.6, 37.4), s[7] + 5.4, en[7] + 0.2, WT),
    # Barbarossa
    lb("SOVIET UNION", (43.0, 57.0), s[8] + 0.3, en[8] + 0.2, SOVC, kind="emp"), lb("GERMANY", (13.5, 51.6), s[8] + 0.3, en[8] + 0.2, DEC),
    # Kiev pocket, Babi Yar
    ev("KIEV", (30.52, 50.75), s[9] + 0.3, en[9] + 0.2, WT), lb("UKRAINE", (34.5, 48.6), s[9] + 0.4, s[9] + 3.0, DEC, kind="small"),
    ev("BABI YAR", (30.45, 50.62), s[9] + 3.6, en[9] + 0.2, WT),
    # Moscow
    ev("MOSCOW", (38.6, 57.3), s[10] + 0.2, en[10] + 0.2),
    # Pearl Harbor
    ev("PEARL HARBOR", (-157.95, 21.62), s[11] + 1.0, en[11] + 0.2),
]
labels += WP.labels(A_, 1939, s[2] + 0.6, SWG[0])
labels += WP.labels(G_, 1940, SWG[1], s[11] - 0.8)

ticker = [(0, 1941), (s[1], 1941), (s[1] + 1.3, 1939), (s[2], 1939), (s[3], 1939), (s[3] + 0.5, 1940), (s[7], 1940), (s[7] + 0.5, 1941),
          (DUR, 1941)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1941", l2="A WORLD AT WAR", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1939", GOLD), hd(2, "NOVEMBER 1939", "THE WINTER WAR", CYN),
            hd(3, "9 APRIL 1940", "NORWAY INVADED"), hd(4, "MAY 1940", "BLITZKRIEG IN THE WEST"),
            hd(5, "DUNKIRK", "338,000 RESCUED", GOLD, t1=s[5] + 3.8), dict(t0=s[5] + 3.9, t1=en[5] + 0.2, l1="JUNE 1940", l2="FRANCE FALLS", c2=RRED),
            hd(6, "SUMMER 1940", "BATTLE OF BRITAIN", GOLD), hd(7, "FEBRUARY 1941", "AFRIKA KORPS", GOLD, t1=s[7] + 3.2),
            dict(t0=s[7] + 3.3, t1=en[7] + 0.2, l1="APRIL 1941", l2="BALKANS OVERRUN", c2=RRED),
            hd(8, "22 JUNE 1941", "OPERATION BARBAROSSA"), hd(9, "SEPTEMBER 1941", "KIEV ENCIRCLED", t1=s[9] + 3.2),
            dict(t0=s[9] + 3.3, t1=en[9] + 0.2, l1="29-30 SEPTEMBER 1941", l2="BABI YAR", c2=WHITE),
            hd(10, "DECEMBER 1941", "THE GATES OF MOSCOW", CYN), hd(11, "7 DECEMBER 1941", "PEARL HARBOR")]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
GRY = (120, 120, 132); RA = (200, 40, 40); FINW = (235, 238, 245); DAK = (200, 180, 130)
GERC = ["rgb:120,120,132"] * 6; SOVF = ["rgb:200,40,40"] * 6
FR = lambda p0, p1, a, b, m0, m1, sa=GERC, sb=SOVF, sc=0.8: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1,
                                                                  side_a=sa, side_b=sb, by_segment=True, rows=2, scale=sc)
# Barbarossa: from the border of 22 June to the line of late September (Leningrad, Ilmen, east of Smolensk, the Kiev pocket, the Dnieper bend)
B0 = [(21.2, 55.6), (22.8, 54.4), (23.5, 53.0), (23.7, 52.1), (23.9, 51.0), (24.0, 50.4), (23.0, 49.4), (26.6, 48.3), (28.2, 46.6), (28.6, 45.5)]
B1 = [(29.8, 59.6), (31.2, 58.4), (32.0, 56.6), (33.0, 55.0), (33.2, 53.5), (33.4, 52.0), (33.6, 50.4), (34.3, 49.0), (35.0, 47.6), (36.5, 47.0)]
# Moscow: the October line and the line of 5 December
M0 = [(34.6, 57.2), (35.2, 56.3), (35.0, 55.3), (35.6, 54.3), (36.4, 53.4)]
M1 = [(35.9, 56.9), (37.3, 56.15), (36.8, 55.45), (37.3, 54.85), (37.9, 54.1)]
fx = [
    # hook: occupied Europe glows, the panzers swing east
    GL((13.4, 52.5), 1.0, en[0], 380, 20, 70), VH("tank", [(14.0, 52.4), (21.0, 52.2), (30.0, 53.6)], 2.0, 5.6, until=en[0] + 0.2),
    # Winter War: Red Army columns at the Mannerheim Line and in the northern forests; Finnish ski troops strike back
    IC("snow", (24.5, 68.0), s[2] + 0.6, en[2] + 0.2, scale=0.6),
    M_([(30.3, 59.95), (29.9, 60.3), (29.5, 60.55)], s[2] + 0.8, s[2] + 3.2, RA, kind="redarmy41", soldiers=6, ships=False, until=s[2] + 5.4),
    M_([(31.8, 64.9), (30.4, 64.9), (29.3, 64.9)], s[2] + 1.0, s[2] + 3.6, RA, kind="redarmy41", soldiers=5, ships=False, until=s[2] + 5.4),
    M_([(27.4, 64.3), (28.2, 64.6), (28.85, 64.85)], s[2] + 2.6, s[2] + 4.8, FINW, kind="finn", soldiers=5, ships=False, until=s[2] + 5.6),
    M_([(28.0, 61.0), (28.6, 60.75)], s[2] + 2.8, s[2] + 4.6, FINW, kind="finn", soldiers=4, ships=False, until=s[2] + 5.6),
    PP("mannerheim", "C. G. E. MANNERHEIM", "FIELD MARSHAL", s[2] + 1.2, en[2] + 0.2, x=300),
    # Norway: warships and transports from Kiel, paratroopers by air; the Blücher sails up the Oslofjord into Oscarsborg's guns
    VH("warship", [(10.15, 54.4), (8.0, 57.8), (5.0, 60.0), (5.0, 63.6), (11.0, 67.0), (15.0, 68.2), (17.4, 68.4)], s[3] + 0.4, s[3] + 3.0, until=s[3] + 3.4),
    VH("warship", [(10.15, 54.4), (7.0, 57.5), (4.6, 59.6), (5.3, 60.4)], s[3] + 0.5, s[3] + 2.6, until=s[3] + 3.4),
    VH("plane", [(9.9, 53.6), (10.3, 57.0), (10.6, 59.9)], s[3] + 0.6, s[3] + 2.4, until=s[3] + 3.2),
    M_([(9.4, 54.8), (9.5, 55.9), (10.0, 56.9)], s[3] + 0.4, s[3] + 2.2, GRY, kind="wehrmacht", soldiers=5, ships=False, until=s[3] + 3.2),
    VH("warship", [(10.5, 59.25), (10.57, 59.5), (10.62, 59.66)], s[3] + 3.4, s[3] + 5.0, until=en[3] + 0.2),
    BM((10.63, 59.67), s[3] + 5.0, 0.3), BM((10.6, 59.64), s[3] + 5.5, 0.26), IC("fire", (10.62, 59.66), s[3] + 5.6, en[3] + 0.2, scale=0.6),
    GL((10.6, 59.66), s[3] + 4.9, en[3] + 0.2, 90, 50, 140),
    # the West: into the Netherlands and Belgium, then the panzers through the Ardennes, over the Meuse at Sedan, to the Channel
    M_([(7.0, 52.1), (6.0, 52.1), (4.9, 52.3)], s[4] + 0.3, s[4] + 2.2, GRY, kind="wehrmacht", soldiers=5, ships=False, until=s[4] + 3.0),
    VH("tank", [(6.4, 50.1), (5.4, 49.85), (4.95, 49.7), (3.3, 49.85), (1.83, 50.1)], s[4] + 0.4, s[4] + 4.4, until=en[4] + 0.2),
    VH("tank", [(6.3, 49.75), (5.3, 49.6), (4.6, 49.55), (3.0, 49.6), (2.0, 49.85)], s[4] + 0.6, s[4] + 4.6, until=en[4] + 0.2),
    VH("bomber", [(6.0, 50.4), (5.4, 50.0), (4.95, 49.72)], s[4] + 0.6, s[4] + 1.6, until=s[4] + 2.4), BM((4.95, 49.7), s[4] + 1.6, 0.28),
    # Dunkirk: destroyers and little ships shuttle the army home; June: into Paris
    *[VH("steamer", [(2.37 - 0.08 * k, 51.06), (1.8, 51.18 - 0.03 * k), (1.35, 51.12)], s[5] + 0.3 + 0.5 * k, s[5] + 2.3 + 0.5 * k, until=s[5] + 3.8)
      for k in range(4)],
    VH("warship", [(2.3, 51.08), (1.8, 51.25), (1.32, 51.1)], s[5] + 0.5, s[5] + 2.8, until=s[5] + 3.8),
    VH("bomber", [(3.4, 50.6), (2.8, 50.9), (2.38, 51.03)], s[5] + 0.8, s[5] + 1.8, until=s[5] + 2.6), BM((2.37, 51.03), s[5] + 1.8, 0.24),
    GL((2.37, 51.04), s[5] + 0.3, s[5] + 3.8, 110, 40, 120),
    M_([(3.2, 49.9), (2.8, 49.4), (2.4, 48.9)], s[5] + 3.6, s[5] + 4.9, GRY, kind="wehrmacht", soldiers=5, ships=False, until=s[5] + 5.0),
    # Battle of Britain: radar stations glow, bombers cross the Channel, RAF fighters climb to meet them; the Blitz on London
    *[GL(p, s[6] + 0.6 + 0.25 * k, s[6] + 4.0, 70, 60, 170) for k, p in enumerate([(1.4, 52.0), (1.3, 51.15), (-0.5, 50.83), (1.15, 51.4)])],
    VH("bomber", [(2.0, 50.6), (1.0, 51.1), (-0.1, 51.5)], s[6] + 1.0, s[6] + 3.6, until=s[6] + 4.6),
    VH("bomber", [(1.6, 49.7), (0.0, 50.4), (-1.4, 50.9)], s[6] + 1.2, s[6] + 3.8, until=s[6] + 4.6),
    VH("plane", [(-0.6, 51.75), (0.2, 51.4), (0.9, 51.2)], s[6] + 1.8, s[6] + 3.2, until=s[6] + 4.6),
    VH("plane", [(-1.2, 51.2), (-0.8, 50.95), (-0.3, 50.85)], s[6] + 2.0, s[6] + 3.4, until=s[6] + 4.6),
    BM((-0.1, 51.5), s[6] + 3.7, 0.26), BM((0.0, 51.52), s[6] + 4.2, 0.24),
    PP("churchill", "WINSTON CHURCHILL", "PRIME MINISTER", s[6] + 0.6, en[6] + 0.2, x=780),
    # Afrika Korps to Tripoli and east; the Balkans: Belgrade bombed, columns from Austria and Bulgaria to Belgrade and Athens
    VH("steamer", [(14.25, 40.8), (12.6, 37.6), (13.18, 32.95)], s[7] + 0.2, s[7] + 1.8, until=s[7] + 3.2),
    M_([(13.2, 32.85), (15.6, 31.2), (19.2, 30.4), (23.9, 32.05)], s[7] + 1.2, s[7] + 3.4, DAK, kind="dak", soldiers=6, ships=False, until=s[7] + 3.6),
    PP("rommel", "ERWIN ROMMEL", "COMMANDER, AFRIKA KORPS", s[7] + 0.6, s[7] + 3.4, x=300),
    VH("bomber", [(17.0, 46.2), (19.0, 45.4), (20.46, 44.82)], s[7] + 3.3, s[7] + 4.2, until=s[7] + 5.0), BM((20.46, 44.82), s[7] + 4.2, 0.26),
    M_([(15.4, 46.7), (17.5, 45.6), (20.4, 44.85)], s[7] + 3.5, s[7] + 5.6, GRY, kind="wehrmacht", soldiers=5, ships=False, until=en[7] + 0.2),
    M_([(23.3, 42.7), (22.94, 40.7), (22.4, 39.6), (23.7, 38.05)], s[7] + 3.9, s[7] + 6.4, GRY, kind="wehrmacht", soldiers=5, ships=False, until=en[7] + 0.2),
    # Barbarossa: the front rolls east, three panzer thrusts, bombers on the Soviet airfields
    FR(B0, B1, s[8] + 0.4, s[9] + 3.2, s[8] + 0.9, s[9] + 2.8),
    BM((25.3, 54.7), s[8] + 0.6, 0.26), BM((27.6, 53.9), s[8] + 0.9, 0.26), BM((24.0, 49.8), s[8] + 1.1, 0.24),
    VH("tank", [(21.6, 55.2), (24.0, 56.4), (28.3, 57.8)], s[8] + 1.0, s[8] + 5.2, until=en[8] + 0.2),
    VH("tank", [(23.7, 52.1), (27.56, 53.9), (32.05, 54.78)], s[8] + 1.2, s[8] + 5.4, until=en[8] + 0.2),
    VH("tank", [(24.0, 50.4), (27.0, 50.3), (30.0, 50.4)], s[8] + 1.4, s[8] + 5.4, until=en[8] + 0.2),
    PP("hitler", "ADOLF HITLER", "LEADER OF GERMANY", s[8] + 0.5, en[8] + 0.2, x=300),
    PP("stalin", "JOSEPH STALIN", "SOVIET LEADER", s[8] + 1.0, en[8] + 0.2, x=780),
    # Kiev: Guderian from the north, Kleist from the south, the pincers close at Lokhvitsa; Babi Yar (no effects, only a quiet light)
    VH("tank", [(32.2, 53.2), (32.9, 51.8), (33.27, 50.37)], s[9] + 0.3, s[9] + 2.6, until=s[9] + 3.4),
    VH("tank", [(33.2, 48.7), (33.4, 49.6), (33.27, 50.37)], s[9] + 0.5, s[9] + 2.6, until=s[9] + 3.4),
    M_([(31.5, 50.0), (32.2, 50.2)], s[9] + 1.0, s[9] + 3.0, RA, kind="redarmy41", soldiers=5, ships=False, until=s[9] + 3.4),
    GL((31.8, 50.3), s[9] + 2.4, s[9] + 3.4, 240, 30, 100),
    GL((30.45, 50.47), s[9] + 3.6, en[9] + 0.2, 60, 30, 80),
    # Moscow: snow and frost, the front grinds to a halt, Zhukov's counter-attack drives west
    IC("snow", (33.6, 57.3), s[10] + 0.2, en[10] + 0.2, scale=0.5),
    FR(M0, M1, s[10] + 0.1, en[10] + 0.2, s[10] + 0.2, s[10] + 1.6),
    M_([(37.6, 55.75), (36.9, 55.95), (36.2, 56.15)], s[10] + 1.8, s[10] + 4.0, RA, kind="redarmy41", soldiers=6, ships=False, until=en[10] + 0.2),
    M_([(38.2, 54.4), (37.4, 54.1), (36.6, 53.9)], s[10] + 2.0, s[10] + 4.1, RA, kind="redarmy41", soldiers=5, ships=False, until=en[10] + 0.2),
    PP("zhukov", "GEORGY ZHUKOV", "SOVIET GENERAL", s[10] + 1.6, en[10] + 0.2, x=780),
    # Pearl Harbor: the carriers north of Oahu, two waves of planes, Battleship Row
    *[VH("carrier", [(-158.6 + 0.5 * k, 27.6), (-158.4 + 0.5 * k, 26.1)], s[11] + 0.3, s[11] + 1.8, until=s[11] + 2.6) for k in range(3)],
    *[VH("bomber" if k % 2 else "plane", [(-158.3 + 0.35 * k, 25.9), (-158.1 + 0.15 * k, 23.6), (-157.95 + 0.02 * k, 21.37)],
         s[11] + 1.2 + 0.3 * k, s[11] + 3.0 + 0.3 * k, until=s[11] + 4.0 + 0.3 * k) for k in range(4)],
    *[BM(p, s[11] + 3.0 + 0.35 * k, 0.24) for k, p in enumerate([(-157.95, 21.365), (-157.94, 21.36), (-157.96, 21.37), (-157.93, 21.355)])],
    IC("fire", (-157.95, 21.37), s[11] + 4.4, en[11] + 0.2, scale=0.6),
    PP("yamamoto", "ISOROKU YAMAMOTO", "ADMIRAL, COMBINED FLEET", s[11] + 0.6, en[11] + 0.2, x=300),
    PP("roosevelt", "FRANKLIN D. ROOSEVELT", "PRESIDENT OF THE USA", s[11] + 4.0, en[11] + 0.2, x=780),
]
routes = [dict(pts=[(-158.4, 26.1), (-158.1, 23.6), (-157.95, 21.37)], t0=s[11] + 1.0, t1=s[11] + 2.4, until=en[11] + 0.2, color=(240, 205, 90))]

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
    put(fr, glow_text("YEAR 1943", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("MIDWAY, STALINGRAD, KURSK", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=27, dur=DUR, base_a="/home/claude/shortgen/hd_1939.png", base_b="/home/claude/shortgen/hd_1941.png",
           extra_bases=dict(G="/home/claude/shortgen/hd_1940.png"),
           regions="/home/claude/shortgen/regions_ep27_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWG[0], SWG[1], "A", "G"), (SWB[0], SWB[1], "G", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 0.8, 0.2), (s[3] + 0.4, 0.2), (s[3] + 5.0, 0.3), (s[4] + 1.6, 0.25),
                                              (s[5] + 3.9, 0.2), (s[6] + 3.7, 0.2), (s[7] + 4.2, 0.2), (s[8] + 0.6, 0.3), (s[9] + 2.6, 0.2),
                                              (s[10] + 1.8, 0.2), (s[11] + 3.0, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
