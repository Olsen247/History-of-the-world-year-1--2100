"""Episode 30 – Year 1953: the Cold War begins.
Churchill's Iron Curtain speech at Fulton (5 March 1946); the Marshall Plan (announced June 1947, about 13 billion dollars 1948-52;
Moscow made Poland and Czechoslovakia refuse, July 1947); the Berlin Blockade (24 June 1948 - 12 May 1949) and the airlift
(peak: 1,398 flights in 24 hours, April 1949); NATO founded by 12 nations incl. Norway (4 April 1949); West Germany (23 May 1949);
the first Soviet atomic test RDS-1 at Semipalatinsk (29 August 1949); Mao proclaims the People's Republic (1 October 1949),
the Nationalist government moves to Taipei (December 1949); North Korea invades with T-34-85 tanks (25 June 1950), Seoul falls
28 June, the Pusan Perimeter (August); Inchon (15 September 1950, about 75,000 men, 261 ships), UN forces cross the 38th parallel
(1 October) and reach the Yalu (late October / November); Chinese People's Volunteers cross the Yalu from 19 October, the big
night offensives of late November, Chosin Reservoir at about minus 30 degrees, Seoul lost again on 4 January 1951; two years of
stalemate; Stalin dies 5 March 1953; armistice at Panmunjom 27 July 1953."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1950)
import world_data_1945 as A_, world_data_1950 as G_, world_data_1953 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep30/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(15.0, 50.0, 1100), (25.0, 48.0, 2950), (13.5, 49.5, 700), (2.0, 48.0, 1500), (11.6, 52.3, 330), (-36.0, 47.0, 2950),
         (74.0, 49.0, 1100), (113.0, 30.5, 1350), (127.4, 37.0, 330), (126.7, 37.6, 230), (126.6, 39.6, 380), (127.4, 37.8, 300),
         (20.0, 8.0, 2950)]
ZOOM = {5: (s[5] + 3.4, (9.5, 51.0, 700)), 9: (s[9] + 2.6, (127.2, 39.4, 420))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, *shots[0]), (3.0, 16.0, 50.5, 1000)]
for i in range(1, len(shots)):
    a, b = endshot[i - 1], shots[i]
    if i >= 2 and abs(a[0] - b[0]) > 50:     # long jumps (Europe -> Asia): pull far out, then drop in
        keys += [(s[i] - 0.85, *a), (s[i] - 0.2, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 2950), (s[i] + 0.7, *b)]
        continue
    keys.append((s[i] - 0.85, *a))
    keys.append((s[i] + 0.35, *b))
keys.append((DUR, *shots[-1]))
for i, (t, sh) in ZOOM.items(): keys += [(t - 0.6, *shots[i]), (t + 0.6, *sh)]
keys = sorted(keys, key=lambda k: k[0])

SWG = (s[8] - 0.75, s[8] - 0.3)          # 1945 -> June-1950 map during the swoop from China to Korea
SWB = (s[11] - 0.6, s[11] - 0.15)       # June-1950 -> 1953 map while the front still covers the line
UG, UB = SWG[1] + 0.1, SWB[1] + 0.1
SH = lambda key, a, b, org, under, src, until: dict(key=key, t0=a, t1=b, mode="shatter", origin=org, under=under, piece_src=src, until=until)
reveals = [dict(key="frg_gain", t0=s[5] + 4.0, t1=s[5] + 5.6, until=UG),
           dict(key="prc_gain", t0=s[7] + 0.3, t1=s[7] + 3.4, until=UG), dict(key="tw_gain", t0=s[7] + 4.0, t1=s[7] + 5.2, until=UG),
           dict(key="nk_gain", t0=s[8] + 1.2, t1=s[8] + 6.4, until=s[9] + 1.8),
           SH("nk_loss", s[9] + 1.8, s[9] + 3.6, (126.6, 37.47), "G", "K", s[9] + 3.8),
           dict(key="un_gain", t0=s[9] + 2.6, t1=s[9] + 6.0, until=s[10] + 1.6),
           SH("un_loss", s[10] + 1.6, s[10] + 3.6, (126.0, 40.6), "G", "K", s[10] + 3.8),
           dict(key="red_gain", t0=s[10] + 2.6, t1=s[10] + 5.8, until=s[11] + 1.2),
           SH("red_loss", s[11] + 1.2, s[11] + 3.2, (127.5, 37.1), "B", "K", s[11] + 3.4)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250); SOVC = (150, 200, 110)
PRCC = (240, 110, 100); ROCC = (240, 205, 110); FRGC = (240, 215, 120); NKL = (160, 210, 120)
labels = [
    # hook + iron curtain
    lb("WEST", (6.5, 49.0), 1.2, en[0] + 0.2, USB, kind="emp"), lb("EAST", (22.0, 51.5), 1.2, en[0] + 0.2, RRED, kind="emp"),
    ev("IRON CURTAIN", (17.4, 50.6), s[2] + 2.2, en[2] + 0.2, WT),
    lb("SOVIET UNION", (25.5, 54.0), s[2] + 0.4, en[3] + 0.2, SOVC, kind="emp"),
    # Marshall Plan
    # Berlin
    ev("WEST BERLIN", (13.3, 52.75), s[4] + 0.3, en[4] + 0.2), lb("SOVIET ZONE", (11.7, 51.2), s[4] + 0.4, en[4] + 0.2, SOVC, kind="small"),
    lb("HAMBURG", (10.0, 53.8), s[4] + 0.8, en[4] + 0.2, WT, kind="small"), lb("HANOVER", (9.6, 52.15), s[4] + 0.8, en[4] + 0.2, WT, kind="small"),
    lb("FRANKFURT", (8.7, 50.35), s[4] + 0.8, en[4] + 0.2, WT, kind="small"),
    # NATO
    ev("NATO", (-30.0, 47.0), s[5] + 0.5, s[5] + 3.4), lb("UNITED STATES", (-70.5, 41.0), s[5] + 0.6, s[5] + 3.4, USB),
    lb("CANADA", (-80.0, 55.0), s[5] + 0.6, s[5] + 3.4, (240, 170, 170)), lb("NORWAY", (9.5, 62.0), s[5] + 0.8, s[5] + 3.4, (190, 170, 240)),
    lb("WEST GERMANY", (9.4, 50.7), s[5] + 4.2, en[5] + 0.2, FRGC),
    # Soviet bomb
    ev("SEMIPALATINSK", (77.8, 51.4), s[6] + 0.5, en[6] + 0.2, WT), lb("SOVIET UNION", (66.0, 56.0), s[6] + 0.3, en[6] + 0.2, SOVC, kind="emp"),
    # China
    ev("BEIJING", (116.4, 40.5), s[7] + 0.3, en[7] + 0.2), lb("PEOPLE'S REPUBLIC OF CHINA", (104.5, 31.0), s[7] + 2.0, en[7] + 0.2, PRCC),
    ev("TAIWAN", (121.0, 22.6), s[7] + 4.2, en[7] + 0.2, ROCC),
    # Korea
    lb("NORTH KOREA", (127.0, 40.4), s[8] + 0.3, s[8] + 3.0, NKL), lb("SOUTH KOREA", (128.2, 36.0), s[8] + 0.3, s[8] + 3.0, USB),
    lb("38TH PARALLEL", (125.2, 38.25), s[8] + 0.4, s[8] + 3.4, WT, kind="small"),
    ev("SEOUL", (126.25, 37.7), s[8] + 2.4, en[8] + 0.2), ev("PUSAN", (129.05, 35.0), s[8] + 4.4, en[8] + 0.2, WT),
    ev("INCHON", (126.4, 37.35), s[9] + 0.3, s[9] + 3.0), lb("YALU", (125.3, 40.75), s[9] + 4.4, s[10] + 0.3, CYN, kind="small"),
    ev("CHOSIN", (128.65, 39.75), s[10] + 2.8, en[10] + 0.2, CYN), lb("CHINA", (124.2, 42.4), s[10] + 0.3, en[10] + 0.2, PRCC, kind="emp"),
    ev("PANMUNJOM", (125.55, 37.5), s[11] + 2.2, en[11] + 0.2), lb("NORTH KOREA", (127.3, 39.4), s[11] + 3.0, en[11] + 0.2, NKL),
    lb("SOUTH KOREA", (128.1, 36.2), s[11] + 3.0, en[11] + 0.2, USB),
]
labels += WP.labels(A_, 1946, s[1] + 0.8, SWG[0])
labels += WP.labels(G_, 1950, SWG[1], s[12])

ticker = [(0, 1953), (s[1], 1953), (s[1] + 1.3, 1945)]
for i, y in ((2, 1946), (3, 1947), (4, 1948), (5, 1949), (8, 1950), (11, 1953)):
    ticker += [(s[i], ticker[-1][1]), (s[i] + 0.5, y)]
ticker.append((DUR, 1953))
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1953", l2="THE COLD WAR", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1945", GOLD), hd(2, "5 MARCH 1946", "THE IRON CURTAIN", WHITE),
            hd(3, "JUNE 1947", "THE MARSHALL PLAN", GOLD), hd(4, "JUNE 1948", "THE BERLIN AIRLIFT", CYN),
            hd(5, "4 APRIL 1949", "NATO IS BORN", CYN), hd(6, "29 AUGUST 1949", "THE SOVIET BOMB"),
            hd(7, "1 OCTOBER 1949", "MAO'S CHINA"), hd(8, "25 JUNE 1950", "THE KOREAN WAR"),
            hd(9, "SEPTEMBER 1950", "INCHON", CYN), hd(10, "LATE 1950", "CHINA ENTERS THE WAR"),
            hd(11, "27 JULY 1953", "ARMISTICE", GOLD)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
RED = ["rgb:200,40,40"] * 6; WEST = ["us", "uk", "fr", "us", "uk", "fr"]; UNF = ["rgb:60,90,200", "us", "rgb:60,90,200", "us", "rgb:60,90,200", "us"]
KPA = (190, 60, 60); USA = (110, 150, 220); PVA = (200, 70, 70); PLA = (200, 70, 70)
FR = lambda p0, p1, a, b, m0, m1, sa=RED, sb=UNF, sc=0.5: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1,
                                                               side_a=sa, side_b=sb, by_segment=True, rows=2, scale=sc)
# the Iron Curtain, north to south: Lubeck, the inner German border, Bohemia, Austria, Hungary, down to Trieste
CURTAIN = [(10.9, 54.0), (10.75, 53.4), (10.6, 52.8), (10.9, 52.2), (10.4, 51.6), (10.0, 51.2), (10.2, 50.6), (11.1, 50.35), (12.1, 50.3),
           (12.5, 49.9), (12.6, 49.4), (13.5, 48.8), (14.9, 48.95), (16.0, 48.75), (16.9, 48.6), (17.1, 48.0), (16.5, 47.5), (16.1, 46.9),
           (15.2, 46.5), (13.9, 45.65)]
# Korean War front lines, west to east (side_a = the communist side, to the north)
F38 = [(124.7, 38.0), (125.6, 38.0), (126.5, 38.0), (127.3, 38.0), (128.1, 38.0), (128.65, 38.0)]
FPUS = [(128.35, 35.2), (128.45, 35.55), (128.42, 35.9), (128.55, 36.12), (128.95, 36.15), (129.35, 36.05)]
FYALU = [(125.0, 39.75), (125.8, 39.72), (126.5, 40.1), (127.2, 40.6), (128.2, 41.4), (129.6, 41.8)]
F37 = [(126.4, 36.97), (126.9, 37.0), (127.4, 37.1), (127.95, 37.3), (128.6, 37.25), (129.2, 37.4)]
FDMZ = [(126.15, 37.75), (126.7, 37.95), (127.1, 38.25), (127.6, 38.3), (128.1, 38.33), (128.35, 38.6)]
NATO = [(-77.0, 38.9), (-75.7, 45.4), (-21.9, 64.1), (10.75, 59.9), (12.57, 55.68), (-0.13, 51.5), (2.35, 48.86), (4.35, 50.85),
        (4.9, 52.37), (6.13, 49.61), (-9.14, 38.72), (12.5, 41.9)]
fx = [
    # hook: the continent splits – two rows of flags face each other along the Iron Curtain
    FR(CURTAIN, CURTAIN, 0.6, en[0] + 0.3, 1e9, 1e9, sa=RED, sb=WEST, sc=0.6),
    GL((37.6, 55.75), 0.6, en[0] + 0.2, 260, 20, 80),
    # Iron Curtain: the line is drawn from the Baltic to the Adriatic
    GL((20.0, 51.0), s[2] + 2.0, en[2] + 0.2, 420, 20, 70),
    PP("churchill", "WINSTON CHURCHILL", "FORMER BRITISH PRIME MINISTER", s[2] + 0.4, en[2] + 0.2, x=780),
    # Marshall Plan: aid across the Atlantic (gold), Stalin keeps the East out
    *[dict(type="icon", icon="gold", pos=p, t0=s[3] + 1.4 + 0.25 * k, t1=en[3] + 0.2, scale=0.45)
      for k, p in enumerate([(-1.5, 52.5), (2.3, 47.2), (12.6, 43.0), (5.3, 52.2), (9.5, 49.8)])],
    GL((22.0, 50.5), s[3] + 3.6, en[3] + 0.2, 300, 20, 90),
    PP("truman", "HARRY S. TRUMAN", "PRESIDENT OF THE UNITED STATES", s[3] + 0.4, s[3] + 3.4, x=780),
    PP("stalin", "JOSEPH STALIN", "LEADER OF THE SOVIET UNION", s[3] + 3.4, en[3] + 0.2, x=300),
    # Berlin: the blockade, then planes in the three air corridors
    GL((13.4, 52.5), s[4] + 0.3, en[4] + 0.2, 45, 60, 150),
    *[VH("plane", [p, (13.35, 52.48)], s[4] + 1.0 + 0.55 * k + 0.18 * j, s[4] + 2.6 + 0.55 * k + 0.18 * j, until=s[4] + 2.8 + 0.55 * k + 0.18 * j)
      for k in range(9) for j, p in enumerate([(10.0, 53.55), (9.05, 52.27), (8.68, 50.11)])],
    PP("stalin", "JOSEPH STALIN", "LEADER OF THE SOVIET UNION", s[4] + 0.4, en[4] + 0.2, x=780),
    # NATO: twelve founding members light up on both sides of the Atlantic; then West Germany
    dict(type="cities", cities=[(x, y, 1.5) for x, y in NATO], t0=s[5] + 0.8, t1=s[5] + 2.0, until=s[5] + 3.8, color=(140, 200, 255)),
    PP("truman", "HARRY S. TRUMAN", "PRESIDENT OF THE UNITED STATES", s[5] + 0.6, s[5] + 3.4, x=780),
    # the Soviet bomb
    BM((77.8, 50.4), s[6] + 0.6, 0.5), BM((77.8, 50.4), s[6] + 1.6, 0.4), GL((77.8, 50.4), s[6] + 0.6, en[6] + 0.2, 220, 90, 245),
    PP("stalin", "JOSEPH STALIN", "LEADER OF THE SOVIET UNION", s[6] + 0.4, en[6] + 0.2, x=780),
    # China: the People's Liberation Army sweeps south; the Nationalists cross to Taiwan
    M_([(116.4, 39.9), (114.3, 34.8), (113.0, 28.2), (113.3, 23.2)], s[7] + 0.3, s[7] + 3.4, PLA, kind="pva", soldiers=6, ships=False, until=en[7] + 0.2),
    M_([(121.5, 31.2), (120.2, 30.3), (117.0, 28.0)], s[7] + 0.5, s[7] + 3.0, PLA, kind="pva", soldiers=5, ships=False, until=en[7] + 0.2),
    *[VH("warship", [(119.4 + 0.3 * k, 25.9 - 0.4 * k), (120.6, 25.2 - 0.3 * k), (121.6, 25.1 - 0.4 * k)], s[7] + 3.6 + 0.2 * k, s[7] + 5.0 + 0.2 * k,
         until=en[7] + 0.2) for k in range(2)],
    GL((116.4, 39.9), s[7] + 0.3, en[7] + 0.2, 70, 60, 170),
    PP("mao", "MAO ZEDONG", "CHAIRMAN, COMMUNIST PARTY OF CHINA", s[7] + 0.4, s[7] + 3.5, x=300),
    PP("chiang", "CHIANG KAI-SHEK", "NATIONALIST LEADER", s[7] + 3.6, en[7] + 0.2, x=300),
    # Korea, June 1950: T-34s across the 38th parallel, Seoul falls, the front is pushed back to Pusan
    FR(F38, FPUS, s[8] + 0.3, en[8] + 0.3, s[8] + 1.2, s[8] + 6.4),
    VH("tank", [(126.9, 38.3), (127.0, 37.6), (127.4, 36.6), (128.2, 35.9)], s[8] + 0.6, s[8] + 5.6, until=en[8] + 0.2),
    VH("tank", [(126.4, 38.2), (126.95, 37.55)], s[8] + 0.6, s[8] + 2.6, until=s[8] + 3.6),
    M_([(127.6, 38.3), (127.9, 37.3), (128.3, 36.4)], s[8] + 1.2, s[8] + 5.4, KPA, kind="kpa", soldiers=6, ships=False, until=en[8] + 0.2),
    BM((126.98, 37.57), s[8] + 2.6, 0.3),
    PP("kimilsung", "KIM IL-SUNG", "LEADER OF NORTH KOREA", s[8] + 0.4, en[8] + 0.2, x=300),
    # Inchon: the fleet comes in behind the lines, Seoul is retaken and the UN races north
    VH("carrier", [(124.4, 36.4), (125.6, 37.0)], s[9] + 0.2, s[9] + 1.6, until=s[9] + 3.4),
    *[VH("warship", [(124.8 + 0.2 * k, 37.2 + 0.15 * k), (126.1 + 0.1 * k, 37.38 + 0.06 * k)], s[9] + 0.2, s[9] + 1.6, until=s[9] + 3.4) for k in range(2)],
    *[VH("landing_craft", [(126.15, 37.32 + 0.06 * k), (126.6, 37.46 + 0.02 * k)], s[9] + 0.8 + 0.2 * k, s[9] + 2.0 + 0.2 * k, until=s[9] + 3.0) for k in range(3)],
    BM((126.62, 37.47), s[9] + 1.9, 0.26),
    M_([(126.63, 37.47), (126.98, 37.57), (126.6, 38.6), (125.8, 39.4)], s[9] + 2.2, s[9] + 6.4, USA, kind="gi", soldiers=6, ships=False, until=en[9] + 0.2),
    FR(FPUS, FYALU, s[9] + 0.2, en[9] + 0.3, s[9] + 2.4, s[9] + 6.4),
    PP("macarthur", "DOUGLAS MACARTHUR", "UN COMMANDER IN KOREA", s[9] + 0.4, en[9] + 0.2, x=780),
    # China enters: columns cross the Yalu by night, jets duel over the river, the front is pushed south again
    M_([(124.0, 40.6), (124.4, 40.05), (125.2, 39.6)], s[10] + 0.4, s[10] + 3.0, PVA, kind="pva", soldiers=6, ships=False, until=en[10] + 0.2),
    M_([(126.2, 41.4), (126.4, 40.8), (126.9, 40.3)], s[10] + 0.6, s[10] + 3.2, PVA, kind="pva", soldiers=6, ships=False, until=en[10] + 0.2),
    M_([(127.3, 40.8), (127.2, 40.35), (127.0, 39.6)], s[10] + 2.6, s[10] + 5.4, PVA, kind="pva", soldiers=5, ships=False, until=en[10] + 0.2),
    VH("jet", [(123.6, 41.2), (125.0, 40.0), (126.0, 39.6)], s[10] + 0.6, s[10] + 2.4, until=s[10] + 3.2),
    VH("jet", [(127.4, 38.6), (125.6, 39.9), (124.6, 40.5)], s[10] + 0.8, s[10] + 2.6, until=s[10] + 3.4),
    GL((127.3, 40.45), s[10] + 2.6, en[10] + 0.2, 60, 60, 160),
    FR(FYALU, F37, s[10] + 0.2, en[10] + 0.3, s[10] + 1.6, s[10] + 5.8),
    PP("mao", "MAO ZEDONG", "CHAIRMAN, COMMUNIST PARTY OF CHINA", s[10] + 0.4, en[10] + 0.2, x=300),
    # armistice: the front settles on the line that still divides Korea
    FR(F37, FDMZ, s[11] + 0.1, en[11] + 0.4, s[11] + 0.6, s[11] + 2.8),
    GL((126.68, 37.96), s[11] + 2.2, en[11] + 0.2, 40, 60, 160),
    PP("eisenhower53", "DWIGHT D. EISENHOWER", "PRESIDENT OF THE UNITED STATES", s[11] + 0.4, en[11] + 0.2, x=300),
]
routes = [dict(pts=CURTAIN, t0=s[2] + 0.6, t1=s[2] + 3.4, until=en[2] + 0.2, color=(245, 245, 245)),
          dict(pts=[(-74.0, 40.7), (-50.0, 44.0), (-25.0, 46.5), (-5.0, 48.0)], t0=s[3] + 0.4, t1=s[3] + 2.0, until=en[3] + 0.2, color=(240, 205, 90))]

def vig(t):
    if t < en[0] + 0.3 or t > s[12] + 0.2: return 1.0
    if s[10] <= t <= en[10]: return 0.75       # the Chinese attacks came at night
    return 0.6

def outro(fr, t):
    t0 = s[12] + 0.3
    if t < t0: return
    lt = t - t0
    dim = Image.new("RGBA", (E.W, E.H), (2, 6, 14, int(205 * pr(lt, 0, 0.5)))); fr.paste(dim, (0, 0), dim)
    k = eback(pr(lt, 0, 0.35), 2.2)
    put(fr, glow_text("NEXT EPISODE", 56, WHITE), 540, 640, scale=min(k, 1.1), alpha=min(1, k * 2))
    k2 = eback(pr(lt, 0.3, 0.65), 2.4)
    put(fr, glow_text("YEAR 1960", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE YEAR OF AFRICA", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=30, dur=DUR, base_a="/home/claude/shortgen/hd_1945.png", base_b="/home/claude/shortgen/hd_1953.png",
           extra_bases=dict(G="/home/claude/shortgen/hd_1950.png", K="/home/claude/shortgen/hd_1950kx.png"),
           regions="/home/claude/shortgen/regions_ep30_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWG[0], SWG[1], "A", "G"), (SWB[0], SWB[1], "G", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 0.6, 0.2), (s[4] + 0.4, 0.2), (s[5] + 0.8, 0.2), (s[6] + 0.6, 0.4), (s[6] + 1.6, 0.25),
                                              (s[7] + 0.3, 0.2), (s[8] + 2.6, 0.25), (s[9] + 1.9, 0.25), (s[10] + 0.4, 0.2),
                                              (s[11] + 0.6, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
