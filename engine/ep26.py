"""Episode 26 – Year 1939: the Second World War, part 1 – the road to war.
Wall Street crash (24-29 Oct 1929), ~6 million unemployed Germans (early 1932); the Mukden Incident (18 Sept 1931) and
Manchukuo (1932); Hitler chancellor (30 Jan 1933), one-party state (14 July 1933), persecution of Jews (April 1933 boycott and
laws); the generals' revolt (17-18 July 1936), Franco Nationalist leader (Oct 1936), the German airlift from Morocco, Guernica
bombed by the Condor Legion and Italian aircraft (26 Apr 1937); Marco Polo Bridge (7 July 1937), Shanghai (Aug-Nov 1937),
Nanjing (Dec 1937); the Anschluss (12-13 March 1938), Kristallnacht (9-10 Nov 1938); Munich (29-30 Sept 1938), Prague
(15 March 1939); the Molotov-Ribbentrop pact with its secret protocol (23 Aug 1939); the invasion of Poland (1 Sept 1939:
Westerplatte, Wieluń, panzer columns, Stukas, radio), Britain and France declare war (3 Sept), the Soviet invasion (17 Sept),
Warsaw surrenders (27-28 Sept) after a siege from 8 Sept."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1939)
import world_data_1931 as C_, world_data_1937 as E_, world_data_1938 as F_, world_data_1939 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep26/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(15.0, 49.0, 1300), (10.0, 45.0, 2850), (-74.0, 40.5, 900), (122.5, 42.5, 820), (11.5, 51.0, 640), (-4.0, 40.3, 560),
         (117.5, 35.5, 900), (13.0, 49.6, 560), (14.6, 49.9, 460), (28.0, 53.5, 1150), (19.5, 52.2, 620), (15.0, 51.0, 1400),
         (14.0, 47.0, 2600)]
endshot = list(shots)
keys = [(0.0, 15.0, 50.0, 950), (3.0, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))
# line 2: from Wall Street out across the Atlantic to Europe ("six million Germans")
keys += [(s[2] + 2.4, -74.0, 40.5, 900), (s[2] + 4.2, -40.0, 46.0, 2300), (s[2] + 6.2, 6.0, 50.0, 1300)]
keys = sorted(keys, key=lambda k: k[0])

SWC = (s[2] - 0.2, s[2] + 0.3)            # 1922 -> 1931 map right after the rewind (same borders, China recoloured)
SWE = (s[7] - 0.85, s[7] - 0.25)          # 1931 -> 1937 map while flying from China to Austria
SWF = (s[9] - 0.85, s[9] - 0.25)          # 1937 -> 1938 map while flying out to Moscow
SWB = (s[12] - 0.85, s[12] - 0.25)        # 1938 -> 1939 map for the outro
UE, UF, UB = SWE[1] + 0.1, SWF[1] + 0.1, SWB[1] + 0.1
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("manchukuo", s[3] + 2.4, s[3] + 6.0, UE), rv("nationalists", s[5] + 0.6, s[5] + 4.2, UE),
           rv("jc37n", s[6] + 0.6, s[6] + 4.0, UE), rv("jc37s", s[6] + 3.2, s[6] + 6.4, UE),
           rv("austria", s[7] + 0.5, s[7] + 3.0, UF), rv("sudeten", s[8] + 1.4, s[8] + 3.4, UF),
           rv("prague", s[8] + 4.0, s[8] + 5.8, UB), rv("slovakia", s[8] + 4.4, s[8] + 5.9, UB), rv("ruthenia", s[8] + 4.6, s[8] + 5.9, UB),
           rv("poland_de", s[10] + 0.8, s[10] + 7.2, UB), rv("poland_su", s[11] + 2.2, s[11] + 4.6, UB)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); GRN = (150, 215, 110); USB = (150, 190, 250)
BRC = (235, 125, 165); DEC = (175, 175, 190); PLC = (240, 110, 120); FRC = (120, 150, 240); SOVC = (150, 200, 110)
JPC = (245, 120, 95); CHC = (240, 200, 100); NTC = (200, 165, 115); RPC = (240, 200, 70); ITC = (120, 200, 160)
labels = [
    # hook: Europe in September 1939
    lb("GERMANY", (11.0, 51.0), 0.6, en[0] + 0.2, DEC, kind="emp"), lb("SOVIET UNION", (24.5, 58.0), 0.9, en[0] + 0.2, SOVC, kind="emp"),
    lb("FRANCE", (2.5, 46.8), 1.1, en[0] + 0.2, FRC), lb("BRITAIN", (-2.2, 53.4), 1.2, en[0] + 0.2, BRC), lb("ITALY", (12.8, 42.6), 1.4, en[0] + 0.2, ITC),
    # crash
    ev("WALL STREET", (-74.0, 41.6), s[2] + 0.3, en[2] + 0.2), lb("UNITED STATES", (-98.0, 39.0), s[2] + 0.4, en[2] + 0.2, USB),
    lb("ATLANTIC", (-40.0, 38.0), s[2] + 0.5, en[2] + 0.2, CYN), lb("GERMANY", (10.5, 51.0), s[2] + 3.6, en[2] + 0.2, DEC),
    lb("BRITAIN", (-2.2, 53.4), s[2] + 2.4, en[2] + 0.2, BRC, kind="small"), lb("FRANCE", (2.5, 46.8), s[2] + 2.6, en[2] + 0.2, FRC, kind="small"),
    # Manchuria
    ev("MUKDEN", (125.8, 40.9), s[3] + 0.4, en[3] + 0.2), lb("MANCHURIA", (129.0, 47.6), s[3] + 2.6, en[3] + 0.2, JPC),
    lb("JAPAN", (138.5, 37.5), s[3] + 0.6, en[3] + 0.2, JPC), lb("KOREA", (127.6, 37.6), s[3] + 0.8, en[3] + 0.2, JPC, kind="small"),
    lb("CHINA", (113.5, 37.0), s[3] + 0.8, en[3] + 0.2, CHC), lb("SOVIET UNION", (131.0, 50.5), s[3] + 1.0, en[3] + 0.2, SOVC, kind="small"),
    # Hitler
    ev("BERLIN", (13.4, 52.9), s[4] + 0.3, en[4] + 0.2), lb("GERMANY", (10.0, 50.6), s[4] + 0.5, en[4] + 0.2, DEC, kind="emp"),
    # Spain
    lb("SPAIN", (-3.5, 41.6), s[5] + 0.2, s[5] + 1.0, RPC), lb("NATIONALISTS", (-6.0, 39.4), s[5] + 2.8, en[5] + 0.2, NTC),
    lb("REPUBLIC", (-0.9, 38.6), s[5] + 2.8, en[5] + 0.2, RPC), ev("MADRID", (-3.7, 40.65), s[5] + 2.2, s[5] + 4.6, WT),
    lb("MOROCCO", (-5.4, 35.0), s[5] + 0.3, s[5] + 3.4, WT, kind="small"), ev("GUERNICA", (-6.6, 42.7), s[5] + 5.0, en[5] + 0.2),
    # China
    ev("BEIJING", (113.6, 40.6), s[6] + 0.3, en[6] + 0.2, WT), ev("SHANGHAI", (118.4, 29.2), s[6] + 2.0, en[6] + 0.2),
    ev("NANJING", (116.9, 32.7), s[6] + 4.6, en[6] + 0.2), lb("CHINA", (110.5, 33.5), s[6] + 0.4, en[6] + 0.2, CHC, kind="emp"),
    lb("JAPAN", (133.5, 34.6), s[6] + 0.6, en[6] + 0.2, JPC, kind="small"), lb("MANCHUKUO", (124.5, 44.5), s[6] + 0.6, en[6] + 0.2, JPC, kind="small"),
    # Austria, Kristallnacht
    ev("VIENNA", (17.0, 46.7), s[7] + 0.4, s[7] + 3.8, WT),
    lb("GERMANY", (10.0, 51.3), s[7] + 0.4, en[7] + 0.2, DEC), lb("CZECHOSLOVAKIA", (15.4, 49.75), s[7] + 0.6, en[7] + 0.2, (140, 180, 240), kind="small"),
    # Munich, Prague
    ev("MUNICH", (11.58, 48.45), s[8] + 0.3, en[8] + 0.2), lb("SUDETENLAND", (13.6, 50.75), s[8] + 2.0, s[8] + 4.0, DEC, kind="small"),
    ev("PRAGUE", (15.7, 49.5), s[8] + 4.2, en[8] + 0.2), lb("SLOVAKIA", (19.3, 48.75), s[8] + 4.8, en[8] + 0.2, (140, 180, 240), kind="small"),
    # the pact
    ev("MOSCOW", (37.6, 56.1), s[9] + 0.3, en[9] + 0.2), lb("SOVIET UNION", (36.0, 53.0), s[9] + 0.5, en[9] + 0.2, SOVC, kind="emp"),
    lb("GERMANY", (13.5, 51.0), s[9] + 0.5, en[9] + 0.2, DEC), lb("POLAND", (19.5, 52.3), s[9] + 2.2, en[9] + 0.2, PLC),
    # invasion of Poland
    ev("DANZIG", (15.8, 54.95), s[10] + 0.2, en[10] + 0.2, WT), ev("WARSAW", (24.7, 53.0), s[10] + 0.4, en[10] + 0.2),
    lb("WIELUŃ", (18.0, 50.95), s[10] + 3.6, en[10] + 0.2, WT, kind="small"),
    # war
    lb("BRITAIN", (-2.2, 53.4), s[11] + 0.3, en[11] + 0.2, BRC), lb("FRANCE", (2.5, 46.8), s[11] + 0.5, en[11] + 0.2, FRC),
    lb("SOVIET UNION", (31.0, 59.5), s[11] + 1.8, en[11] + 0.2, SOVC), ev("WARSAW", (19.6, 52.0), s[11] + 4.0, en[11] + 0.2),
    lb("GERMANY", (10.5, 51.0), s[11] + 0.6, en[11] + 0.2, DEC),
]
labels += WP.labels(C_, 1931, s[2] + 0.6, SWE[0])
labels += WP.labels(E_, 1937, SWE[1], SWF[0])
labels += WP.labels(F_, 1938, SWF[1], s[12])

ticker = [(0, 1939), (s[1], 1939), (s[1] + 1.3, 1922), (s[2], 1922), (s[2] + 0.5, 1929), (s[3], 1929), (s[3] + 0.5, 1931), (s[4], 1931),
          (s[4] + 0.5, 1933), (s[5], 1933), (s[5] + 0.5, 1936), (s[5] + 4.4, 1936), (s[5] + 4.9, 1937), (s[7], 1937), (s[7] + 0.5, 1938),
          (s[8] + 3.7, 1938), (s[8] + 4.2, 1939), (DUR, 1939)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1939", l2="THE ROAD TO WAR", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1922", GOLD), hd(2, "OCTOBER 1929", "WALL STREET CRASH"), hd(3, "SEPTEMBER 1931", "MANCHURIA", GOLD),
            hd(4, "30 JANUARY 1933", "HITLER IN POWER"), hd(5, "JULY 1936", "SPANISH CIVIL WAR", t1=s[5] + 4.6),
            dict(t0=s[5] + 4.7, t1=en[5] + 0.2, l1="APRIL 1937", l2="GUERNICA", c2=RRED),
            hd(6, "JULY 1937", "JAPAN INVADES CHINA"), hd(7, "MARCH 1938", "ANSCHLUSS", GOLD, t1=s[7] + 3.7),
            dict(t0=s[7] + 3.8, t1=en[7] + 0.2, l1="NOVEMBER 1938", l2="KRISTALLNACHT", c2=RRED),
            hd(8, "SEPTEMBER 1938", "MUNICH", GOLD, t1=s[8] + 3.8), dict(t0=s[8] + 3.9, t1=en[8] + 0.2, l1="MARCH 1939", l2="PRAGUE", c2=RRED),
            hd(9, "23 AUGUST 1939", "HITLER-STALIN PACT", GOLD), hd(10, "1 SEPTEMBER 1939", "BLITZKRIEG"), hd(11, "SEPTEMBER 1939", "WAR IN EUROPE")]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
GRY = (120, 120, 132); JPN = (215, 90, 70); NRA = (100, 112, 128); NATC = (150, 120, 80); MIL = (60, 80, 140); RA = (200, 40, 40)
# Poland, 1-28 Sept 1939: the German front rolls east from the borders to the Vistula and the Bug
P0 = [(18.2, 54.5), (17.2, 53.7), (16.5, 52.9), (16.6, 52.0), (17.6, 51.2), (18.6, 50.2), (19.4, 49.6), (20.6, 49.4)]
P1 = [(21.0, 53.6), (21.3, 53.0), (21.2, 52.35), (21.4, 51.6), (21.9, 51.0), (22.3, 50.4), (22.7, 49.9), (22.8, 49.3)]
FR = lambda p0, p1, a, b, m0, m1: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1, side_a=["rgb:120,120,132"] * 6,
                                       side_b=["pl"] * 6, by_segment=True, rows=2, scale=0.8)
fx = [
    # hook: Europe on the brink – a red glow over Poland
    GL((19.5, 52.0), 1.0, en[0], 420, 20, 80),
    # the crash: Wall Street, then the Depression spreading to Europe's cities
    GL((-74.0, 40.7), s[2] + 0.4, en[2], 180, 50, 140), BM((-74.0, 40.7), s[2] + 0.7, 0.28),
    *[GL(p, s[2] + 1.8 + 0.45 * k, en[2], 150, 30, 110) for k, p in enumerate([(-87.6, 41.9), (-0.1, 51.5), (2.35, 48.86), (13.4, 52.5),
                                                                              (-79.4, 43.7), (16.37, 48.2), (-43.2, -22.9)])],
    # Mukden: the bomb on the railway, then the Kwantung Army fans out across Manchuria
    BM((123.42, 41.88), s[3] + 0.6, 0.3),
    M_([(123.4, 41.8), (124.6, 43.2), (125.3, 43.9), (126.6, 45.75)], s[3] + 1.8, s[3] + 5.2, JPN, kind="ija", soldiers=6, ships=False, until=en[3] + 0.2),
    VH("train", [(121.6, 38.9), (122.8, 40.7), (123.4, 41.8), (125.3, 43.9)], s[3] + 1.2, s[3] + 4.8, until=en[3] + 0.2),
    # Hitler in power: Berlin
    GL((13.4, 52.5), s[4] + 0.3, en[4], 260, 40, 130), GL((10.5, 51.0), s[4] + 1.6, en[4], 520, 20, 70),
    PP("hitler", "ADOLF HITLER", "CHANCELLOR OF GERMANY", s[4] + 0.6, en[4] + 0.2, x=780),
    # Spain: German planes fly the Army of Africa over from Morocco, columns close on Madrid, the militias hold;
    # April 1937: German and Italian bombers over Guernica
    VH("plane", [(-5.37, 35.57), (-5.7, 36.5), (-5.98, 37.39)], s[5] + 0.3, s[5] + 2.2, until=s[5] + 4.6),
    VH("plane", [(-5.2, 35.4), (-5.6, 36.4), (-5.9, 37.25)], s[5] + 0.6, s[5] + 2.5, until=s[5] + 4.6),
    M_([(-5.98, 37.39), (-6.3, 38.6), (-5.0, 39.9), (-3.9, 40.3)], s[5] + 1.6, s[5] + 4.4, NATC, kind="carlist", soldiers=6, ships=False, until=s[5] + 4.7),
    M_([(-3.7, 42.34), (-3.9, 41.4), (-4.0, 40.8)], s[5] + 1.8, s[5] + 4.2, NATC, kind="carlist", soldiers=5, ships=False, until=s[5] + 4.7),
    M_([(-3.7, 40.42), (-3.75, 40.6)], s[5] + 2.4, s[5] + 4.2, MIL, kind="miliciano", soldiers=4, ships=False, until=s[5] + 4.7),
    PP("franco", "FRANCISCO FRANCO", "NATIONALIST LEADER", s[5] + 1.4, s[5] + 4.6, x=300),
    VH("bomber", [(-2.67, 42.85), (-2.7, 43.1), (-2.68, 43.31)], s[5] + 5.0, s[5] + 6.6, until=en[5] + 0.2),
    VH("bomber", [(-2.95, 42.8), (-2.85, 43.05), (-2.72, 43.3)], s[5] + 5.3, s[5] + 6.9, until=en[5] + 0.2),
    BM((-2.68, 43.31), s[5] + 6.7, 0.3), BM((-2.66, 43.33), s[5] + 7.1, 0.26),
    IC("fire", (-2.68, 43.31), s[5] + 7.0, en[5] + 0.2, scale=0.7),
    # China: Marco Polo Bridge, the push south from Beijing, Shanghai, then the march on Nanjing
    BM((116.21, 39.85), s[6] + 0.4, 0.3),
    M_([(116.2, 39.8), (115.5, 38.6), (114.9, 37.4), (114.4, 36.3)], s[6] + 0.8, s[6] + 4.0, JPN, kind="ija", soldiers=6, ships=False, until=en[6] + 0.2),
    M_([(118.8, 32.06), (120.0, 31.6), (121.2, 31.3)], s[6] + 1.0, s[6] + 3.0, NRA, kind="nra", soldiers=5, ships=False, until=s[6] + 3.6),
    VH("warship", [(129.9, 32.7), (125.5, 31.9), (122.0, 31.4)], s[6] + 1.4, s[6] + 3.4, until=en[6] + 0.2),
    VH("steamer", [(129.6, 33.2), (125.4, 32.3), (121.9, 31.6)], s[6] + 1.6, s[6] + 3.6, until=en[6] + 0.2),
    BM((121.47, 31.23), s[6] + 3.0, 0.3),
    M_([(121.4, 31.3), (120.3, 31.5), (119.4, 31.9), (118.85, 32.05)], s[6] + 3.6, s[6] + 6.4, JPN, kind="ija", soldiers=6, ships=False, until=en[6] + 0.2),
    BM((118.8, 32.06), s[6] + 6.2, 0.28),
    PP("chiang", "CHIANG KAI-SHEK", "LEADER OF CHINA", s[6] + 1.2, en[6] + 0.2, x=300),
    # Anschluss: columns roll into Austria unopposed; November: synagogues burn across the Reich
    M_([(12.9, 48.25), (14.3, 48.3), (15.6, 48.2), (16.3, 48.2)], s[7] + 0.4, s[7] + 3.2, GRY, kind="wehrmacht", soldiers=6, ships=False, until=s[7] + 3.8),
    M_([(11.9, 47.6), (12.9, 47.8), (13.05, 47.8)], s[7] + 0.6, s[7] + 3.0, GRY, kind="wehrmacht", soldiers=4, ships=False, until=s[7] + 3.8),
    *[IC("fire", p, s[7] + 4.0 + 0.35 * k, en[7] + 0.2, scale=0.55) for k, p in enumerate([(13.4, 52.5), (16.37, 48.2), (8.68, 50.11), (11.58, 48.14)])],
    # Munich: Chamberlain flies to Germany, the Sudetenland is handed over; March 1939: German troops enter Prague
    VH("plane", [(-0.4, 51.47), (5.0, 50.0), (11.6, 48.15)], s[8] + 0.2, s[8] + 1.8, until=s[8] + 3.6),
    GL((11.58, 48.14), s[8] + 0.6, s[8] + 3.6, 120, 40, 130),
    PP("chamberlain", "NEVILLE CHAMBERLAIN", "BRITISH PRIME MINISTER", s[8] + 0.8, s[8] + 3.9, x=780),
    M_([(13.0, 50.6), (13.8, 50.4), (14.42, 50.08)], s[8] + 4.0, s[8] + 5.8, GRY, kind="wehrmacht", soldiers=5, ships=False, until=en[8] + 0.2),
    # the pact: Moscow; the secret line through Poland
    GL((37.6, 55.75), s[9] + 0.3, en[9], 220, 40, 130),
    PP("stalin", "JOSEPH STALIN", "SOVIET LEADER", s[9] + 0.5, en[9] + 0.2, x=780),
    PP("hitler", "ADOLF HITLER", "LEADER OF GERMANY", s[9] + 0.9, en[9] + 0.2, x=300),
    VH("plane", [(13.4, 52.5), (25.0, 54.5), (37.6, 55.75)], s[9] + 0.6, s[9] + 2.6, until=s[9] + 3.4),
    # 1 September: Westerplatte at 4.45 a.m., panzer columns from Pomerania, East Prussia and Silesia, Stukas over roads and towns
    FR(P0, P1, s[10] + 0.6, en[10] + 0.2, s[10] + 1.0, s[10] + 7.2),
    VH("warship", [(18.55, 54.5), (18.62, 54.42)], s[10] + 0.1, s[10] + 1.0, until=en[10] + 0.2), BM((18.67, 54.41), s[10] + 0.9, 0.26),
    VH("tank", [(16.8, 53.2), (18.2, 52.95), (19.6, 52.6)], s[10] + 1.6, s[10] + 5.2, until=en[10] + 0.2),
    VH("tank", [(17.2, 51.1), (18.8, 51.35), (20.4, 51.9)], s[10] + 1.8, s[10] + 5.6, until=en[10] + 0.2),
    VH("tank", [(20.9, 53.7), (21.1, 53.1), (21.2, 52.6)], s[10] + 2.0, s[10] + 5.4, until=en[10] + 0.2),
    VH("plane", [(16.5, 51.4), (17.7, 51.3), (18.57, 51.22)], s[10] + 2.6, s[10] + 3.8, until=s[10] + 4.6), BM((18.57, 51.22), s[10] + 3.8, 0.28),
    VH("plane", [(18.0, 52.6), (19.5, 52.4), (20.6, 52.3)], s[10] + 3.0, s[10] + 4.6, until=s[10] + 5.4), BM((19.9, 52.35), s[10] + 4.5, 0.26),
    GL((19.0, 52.0), s[10] + 3.0, en[10], 400, 20, 70),
    # war declared in London and Paris; the Red Army crosses in the east; Warsaw shelled until it surrenders
    GL((-0.1, 51.5), s[11] + 0.3, en[11], 140, 40, 130), GL((2.35, 48.86), s[11] + 0.5, en[11], 140, 40, 130),
    M_([(28.0, 53.2), (26.3, 52.9), (24.2, 52.5)], s[11] + 2.0, s[11] + 4.8, RA, kind="redarmy", soldiers=6, ships=False, until=en[11] + 0.2),
    M_([(27.5, 50.3), (25.8, 49.9), (24.03, 49.84)], s[11] + 2.2, s[11] + 5.0, RA, kind="redarmy", soldiers=5, ships=False, until=en[11] + 0.2),
    BM((21.0, 52.23), s[11] + 4.2, 0.3), BM((20.95, 52.27), s[11] + 4.7, 0.28), BM((21.05, 52.2), s[11] + 5.2, 0.26),
]
routes = [dict(pts=[(21.9, 54.4), (21.9, 53.45), (21.6, 52.9), (22.0, 52.6), (23.0, 52.3), (23.65, 52.08), (23.55, 51.55), (23.75, 51.0),
                    (24.1, 50.6), (23.4, 50.3), (22.8, 49.8), (22.7, 49.1)], t0=s[9] + 3.0, t1=s[9] + 4.6, until=en[9] + 0.2, color=(240, 205, 90)),
          dict(pts=[(-5.37, 35.57), (-5.98, 37.39)], t0=s[5] + 0.3, t1=s[5] + 1.6, until=s[5] + 4.6, color=(240, 205, 90))]

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
    put(fr, glow_text("YEAR 1941", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("FROM DUNKIRK TO PEARL HARBOR", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=26, dur=DUR, base_a="/home/claude/shortgen/hd_1922.png", base_b="/home/claude/shortgen/hd_1939.png",
           extra_bases=dict(C="/home/claude/shortgen/hd_1931.png", E="/home/claude/shortgen/hd_1937.png", F="/home/claude/shortgen/hd_1938.png"),
           regions="/home/claude/shortgen/regions_ep26_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWC[0], SWC[1], "A", "C"), (SWE[0], SWE[1], "C", "E"), (SWF[0], SWF[1], "E", "F"),
                          (SWB[0], SWB[1], "F", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 0.7, 0.25), (s[3] + 0.6, 0.25), (s[4] + 0.6, 0.2), (s[5] + 0.6, 0.2),
                                              (s[5] + 6.7, 0.25), (s[6] + 0.4, 0.25), (s[7] + 0.5, 0.2), (s[7] + 4.0, 0.2), (s[8] + 1.4, 0.2),
                                              (s[8] + 4.0, 0.2), (s[9] + 0.5, 0.2), (s[10] + 0.9, 0.3), (s[11] + 2.2, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
