"""Episode 24 – Year 1918: the First World War, part 3 (U-boats, America, Russia's revolutions, the Arab Revolt,
the Spring Offensive, the Hundred Days and the armistice).
Unrestricted U-boat war (1 Feb 1917, 860,000 t sunk in April), the Tsar abdicates (15 Mar 1917), Zimmermann telegram and the US
declaration of war (6 Apr 1917), Aqaba (6 Jul 1917), the Bolsheviks seize power (7 Nov 1917) and Brest-Litovsk (3 Mar 1918),
Operation Michael (21 Mar 1918, ~6,600 guns, fog, stormtroopers), the Paris Gun (from 23 Mar) and the Aisne to the Marne
(May-June), Amiens (8 Aug 1918, 'black day'), Damascus (1 Oct), the naval mutinies, the Kaiser to the Netherlands (10 Nov),
the armistice (11 Nov 1918, 11:00)."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1918)
import world_data_1916 as A, world_data_1917 as M, world_data_1918 as B, world_data_1918n as N
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep24/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (8.0, 49.0, 2400)
shots = [(2.95, 49.85, 220), WIDE, (-10.0, 51.0, 1300), (30.4, 59.5, 600), (-55.0, 36.0, 3300), (35.9, 29.5, 380), (31.0, 53.5, 1700),
         (2.95, 49.8, 200), (2.95, 49.25, 280), (2.45, 49.8, 180), (36.3, 33.6, 600), (4.0, 49.8, 340), (14.0, 47.0, 2600)]
endshot = list(shots)
keys = [(0.0, 2.95, 49.85, 420), (3.0, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))
# line 10: Damascus first, then fly to Germany (Kiel, Spa, the Netherlands)
KIEL = (6.8, 51.8, 700)
keys += [(s[10] + 1.1, *shots[10]), (s[10] + 2.1, *KIEL)]
keys = sorted(keys, key=lambda k: k[0])
keys = [k if k[0] != s[11] - 0.85 else (k[0], *KIEL) for k in keys]

SW1 = (s[2] - 0.35, s[2] + 0.25)          # 1916 -> spring 1917 while flying to the Atlantic
SW2 = (s[7] - 0.85, s[7] - 0.25)          # spring 1917 -> mid-1918 while flying to France
SW3 = (s[11] - 0.85, s[11] - 0.25)        # mid-1918 -> 11 November 1918
UB, UN = SW2[1] + 0.1, SW3[1] + 0.1
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("aqaba", s[5] + 2.4, s[5] + 4.6, UB),
           rv("finland", s[6] + 1.0, s[6] + 2.6, UB), rv("east", s[6] + 2.4, s[6] + 5.6, UB),
           rv("syria", s[10] + 0.4, s[10] + 2.6, UN), rv("levant", s[10] + 0.6, s[10] + 2.6, UN),
           dict(key="occ_loss", t0=s[10] + 2.4, t1=s[10] + 4.8, mode="shatter", origin=(3.0, 49.8), under="N", piece_src="B")]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); GRN = (150, 215, 110); USB = (150, 190, 250)
BRC = (235, 125, 165); OTC = (200, 60, 60); RUC = (130, 175, 95); ARC = (120, 200, 120); DEC = (150, 150, 165)
labels = [
    # hook: the Spring Offensive
    ev("WESTERN FRONT", (1.0, 49.1), 0.6, en[0] + 0.2, WT),
    # U-boats
    lb("ATLANTIC", (-22.0, 44.0), s[2] + 0.3, en[2] + 0.2, CYN), lb("BRITAIN", (-2.0, 54.4), s[2] + 0.3, en[2] + 0.2, BRC),
    ev("U-BOATS", (-11.5, 48.6), s[2] + 1.6, en[2] + 0.2, RRED),
    # Petrograd
    ev("PETROGRAD", (30.3, 60.45), s[3] + 0.4, en[3] + 0.2), lb("RUSSIAN EMPIRE", (33.5, 58.6), s[3] + 0.3, en[3] + 0.2, RUC),
    # telegram, America
    ev("BERLIN", (13.4, 53.3), s[4] + 0.3, s[4] + 3.4, WT), ev("LONDON", (-0.1, 52.0), s[4] + 0.6, s[4] + 3.4, WT),
    ev("MEXICO", (-102.0, 23.5), s[4] + 2.4, en[4] + 0.2, (150, 190, 90)),
    lb("UNITED STATES", (-98.0, 40.0), s[4] + 0.4, en[4] + 0.2, USB, kind="emp"),
    # Aqaba
    ev("AQABA", (33.9, 29.55), s[5] + 0.4, en[5] + 0.2), lb("OTTOMAN EMPIRE", (39.8, 31.8), s[5] + 0.3, en[5] + 0.2, OTC),
    lb("ARAB REVOLT", (37.6, 26.6), s[5] + 0.6, en[5] + 0.2, ARC),
    # Lenin, Brest-Litovsk
    ev("PETROGRAD", (30.3, 60.4), s[6] + 0.3, s[6] + 2.6), ev("BREST-LITOVSK", (17.5, 49.6), s[6] + 2.6, en[6] + 0.2),
    lb("SOVIET RUSSIA", (40.0, 56.5), s[6] + 0.6, en[6] + 0.2, RUC), lb("UKRAINE", (32.5, 46.9), s[6] + 4.0, en[6] + 0.2, WT),
    lb("BALTICS", (25.0, 57.6), s[6] + 4.0, en[6] + 0.2, WT, kind="small"), lb("FINLAND", (26.5, 62.8), s[6] + 2.2, en[6] + 0.2, WT, kind="small"),
    # Michael
    ev("OPERATION MICHAEL", (1.7, 51.25), s[7] + 0.3, en[7] + 0.2),
    # Paris gun, the Marne
    ev("PARIS", (1.9, 48.65), s[8] + 0.3, en[8] + 0.2, WT), ev("PARIS GUN", (4.5, 49.85), s[8] + 0.9, en[8] + 0.2),
    # Amiens
    ev("AMIENS", (1.5, 50.2), s[9] + 0.3, en[9] + 0.2), lb("AUSTRALIANS", (1.6, 49.72), s[9] + 1.0, s[9] + 4.4, BRC, kind="small"),
    lb("CANADIANS", (1.7, 49.55), s[9] + 1.2, s[9] + 4.4, (220, 80, 80), kind="small"),
    # collapse
    ev("DAMASCUS", (36.3, 34.1), s[10] + 0.3, s[10] + 2.0), ev("KIEL", (10.1, 55.0), s[10] + 1.9, en[10] + 0.2, WT),
    lb("NETHERLANDS", (5.6, 52.9), s[10] + 3.6, en[10] + 0.2, (240, 140, 40), kind="small"),
    # armistice
    ev("COMPIÈGNE", (2.8, 49.25), s[11] + 0.3, en[11] + 0.2), lb("GERMANY", (7.6, 50.6), s[11] + 0.3, en[11] + 0.2, DEC),
    lb("BELGIUM", (5.0, 50.95), s[11] + 0.3, en[11] + 0.2, (235, 195, 60), kind="small"),
]
labels += WP.labels(M, 1917, s[2] + 0.6, SW2[0])
labels += WP.labels(B, 1918, SW2[1], s[12])

ticker = [(0, 1918), (s[1], 1918), (s[1] + 1.3, 1916), (s[2], 1916), (s[2] + 0.6, 1917), (s[6] + 2.4, 1917), (s[6] + 3.0, 1918), (DUR, 1918)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1918", l2="ONE LAST GAMBLE", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1916", GOLD), hd(2, "FEBRUARY 1917", "U-BOAT WAR", CYN), hd(3, "MARCH 1917", "THE TSAR FALLS"),
            hd(4, "APRIL 1917", "AMERICA JOINS", USB), hd(5, "JULY 1917", "THE ARAB REVOLT", GOLD), hd(6, "NOVEMBER 1917", "LENIN TAKES POWER"),
            hd(7, "21 MARCH 1918", "STORMTROOPERS"), hd(8, "SPRING 1918", "THE PARIS GUN", GOLD), hd(9, "8 AUGUST 1918", "AMIENS", GOLD),
            hd(10, "AUTUMN 1918", "COLLAPSE"), hd(11, "11 NOVEMBER 1918", "ARMISTICE", GOLD)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)

# Western Front, 20 points from the Channel to Switzerland (approximate).
F18 = [(2.75, 51.13), (2.95, 51.0), (3.02, 50.88), (2.9, 50.7), (2.85, 50.45), (2.85, 50.29), (3.05, 50.15), (3.2, 49.95), (3.25, 49.8),
       (3.35, 49.65), (3.5, 49.47), (4.03, 49.27), (4.9, 49.2), (5.35, 49.15), (5.55, 48.92), (6.05, 48.9), (6.7, 48.55), (7.0, 48.2),
       (7.1, 47.85), (7.15, 47.5)]                                      # early 1918 (Hindenburg Line)
def mod(base, **chg):
    p = list(base)
    for k, v in chg.items(): p[int(k[1:])] = v
    return p
MICH = mod(F18, i2=(2.88, 50.82), i3=(2.65, 50.65), i5=(2.78, 50.29), i6=(2.65, 50.05), i7=(2.52, 49.87), i8=(2.55, 49.68), i9=(3.0, 49.57))
BLU = mod(MICH, i9=(3.0, 49.5), i10=(3.1, 49.35), i11=(3.4, 49.06), i12=(3.95, 49.15))     # Aisne offensive to the Marne (June)
HUND = mod(F18, i2=(3.1, 50.85), i14=(5.75, 49.02))                                       # end of Sept: back at the Hindenburg Line
ARM = [(3.75, 51.3), (3.72, 51.05), (3.8, 50.85), (3.85, 50.7), (3.95, 50.45), (4.05, 50.28), (4.15, 50.12), (4.4, 50.0), (4.7, 49.85),
       (4.95, 49.7), (5.1, 49.55), (5.2, 49.45), (5.45, 49.3), (5.75, 49.02), (6.05, 48.92), (6.7, 48.55), (7.0, 48.2), (7.1, 47.85),
       (7.12, 47.68), (7.15, 47.5)]                                   # armistice line, 11 Nov 1918
AL0 = ["be", "be"] + ["uk"] * 7 + ["fr"] * 10
AL1 = ["be", "be"] + ["uk"] * 7 + ["fr"] * 3 + ["us"] * 3 + ["fr"] * 4
FR = lambda p0, p1, a, b, m0=1e9, m1=1e9, al=AL1, sa=("de1914",): dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1,
                                                                       side_a=list(sa), side_b=al, by_segment=True, rows=2, scale=0.8)
# Eastern front: 1916 line -> the Brest-Litovsk line of spring 1918 (Soviet side as a plain red chip)
E16 = [(23.9, 57.0), (26.4, 55.85), (26.6, 54.4), (26.0, 53.1), (26.0, 52.1), (25.6, 50.9), (25.5, 50.1), (26.0, 48.6)]
E18 = [(28.0, 59.3), (28.3, 57.8), (29.6, 56.3), (30.4, 54.5), (30.9, 53.0), (33.6, 52.4), (37.8, 50.1), (39.7, 47.3)]
KH = (150, 130, 90); DEG = (110, 110, 122); ARAB = (70, 145, 75); RUS = (130, 175, 95)
fx = [
    # hook: 21 March 1918 – the German wave
    FR(F18, MICH, 0.3, en[0] + 0.3, 1.4, 5.4, al=AL0),
    dict(type="gas", line=[(3.3, 50.15), (3.4, 49.9), (3.5, 49.65)], drift=(-0.25, 0.0), t0=0.4, t1=4.0, until=en[0] + 0.3, puffs=60, color=(235, 235, 235)),
    BM((3.05, 50.0), 0.7), BM((3.2, 49.8), 1.2), BM((2.9, 49.9), 2.0), BM((2.7, 49.95), 3.0, 0.36), BM((2.6, 49.85), 4.0),
    dict(type="glow", pos=(2.9, 49.85), t0=3.4, t1=en[0], radius=240, a0=40, a1=110),
    # U-boat war: merchant ships heading for Britain, U-boats waiting off Ireland
    VH("steamer", [(-30.0, 49.0), (-20.0, 49.8), (-12.5, 50.4)], s[2] + 0.3, s[2] + 3.2, until=s[2] + 3.6),
    VH("steamer", [(-30.0, 52.5), (-20.0, 52.4), (-12.0, 52.0)], s[2] + 0.5, s[2] + 3.6, until=s[2] + 4.4),
    VH("steamer", [(-30.0, 46.5), (-18.0, 47.5), (-9.0, 48.6), (-5.5, 49.8)], s[2] + 0.4, s[2] + 5.0, until=en[2] + 0.2),
    VH("steamer", [(-28.0, 55.0), (-16.0, 55.5), (-8.5, 55.6)], s[2] + 0.8, s[2] + 4.2, until=s[2] + 5.4),
    VH("submarine", [(-8.0, 49.6), (-10.5, 50.0), (-12.2, 50.3)], s[2] + 1.0, s[2] + 3.0, until=en[2] + 0.2),
    VH("submarine", [(-7.0, 51.2), (-9.5, 51.6), (-11.7, 51.9)], s[2] + 1.2, s[2] + 3.4, until=en[2] + 0.2),
    VH("submarine", [(-6.0, 54.2), (-7.0, 55.2), (-8.3, 55.6)], s[2] + 1.6, s[2] + 4.2, until=en[2] + 0.2),
    BM((-12.5, 50.4), s[2] + 3.4, 0.36), BM((-12.0, 52.0), s[2] + 4.1, 0.36), BM((-8.5, 55.6), s[2] + 5.1, 0.36),
    # Petrograd: mutinous soldiers join the crowds
    M_([(30.0, 59.2), (30.2, 59.6), (30.3, 59.88)], s[3] + 0.6, s[3] + 3.2, RUS, kind="ww1", soldiers=6, ships=False, until=en[3] + 0.2),
    M_([(31.0, 59.5), (30.6, 59.75), (30.36, 59.92)], s[3] + 0.9, s[3] + 3.4, RUS, kind="ww1", soldiers=5, ships=False, until=en[3] + 0.2),
    dict(type="glow", pos=(30.3, 59.93), t0=s[3] + 2.6, t1=en[3], radius=200, a0=40, a1=120),
    PP("nicholas2", "NICHOLAS II", "LAST TSAR OF RUSSIA", s[3] + 2.8, en[3] + 0.2),
    # America joins: US troopships cross the Atlantic
    dict(type="glow", pos=(-97.0, 39.0), t0=s[4] + 3.4, t1=en[4], radius=420, a0=30, a1=90),
    PP("wilson", "WOODROW WILSON", "PRESIDENT OF THE USA", s[4] + 3.2, en[4] + 0.2, x=780),
    VH("warship", [(-74.0, 40.4), (-55.0, 43.0), (-30.0, 46.5), (-10.0, 47.8), (-4.6, 48.3)], s[4] + 3.6, en[4] + 0.1, until=en[4] + 0.2, scale=1.3),
    # Aqaba: from the desert, the unguarded land side
    M_([(37.6, 28.4), (37.0, 29.6), (35.9, 30.05), (35.15, 29.65)], s[5] + 0.6, s[5] + 3.4, ARAB, kind="arabrevolt", soldiers=7, ships=False, until=en[5] + 0.2),
    M_([(37.9, 29.2), (36.8, 30.2), (35.7, 30.15), (35.1, 29.75)], s[5] + 0.9, s[5] + 3.6, ARAB, kind="arabrevolt", soldiers=5, ships=False, until=en[5] + 0.2),
    PP("lawrence", "T. E. LAWRENCE", "BRITISH LIAISON OFFICER", s[5] + 0.5, en[5] + 0.2, x=780),
    PP("auda", "AUDA ABU TAYI", "HOWEITAT CHIEF", s[5] + 1.2, en[5] + 0.2, x=300),
    # Lenin; the Central Powers march east until Brest-Litovsk
    dict(type="glow", pos=(30.3, 59.93), t0=s[6] + 0.3, t1=s[6] + 2.6, radius=180, a0=40, a1=110),
    PP("lenin", "VLADIMIR LENIN", "BOLSHEVIK LEADER", s[6] + 0.4, en[6] + 0.2, x=780),
    FR(E16, E18, s[6] + 0.4, en[6] + 0.2, s[6] + 2.4, s[6] + 5.6, al=["rgb:200,40,40"] * 7, sa=("de1914", "de1914", "de1914", "de1914", "ah", "ah", "ah")),
    # Operation Michael: fog, stormtroopers slip through, strongpoints left for later waves
    FR(F18, MICH, s[7] - 0.2, en[7] + 0.2, s[7] + 2.0, s[7] + 6.6, al=AL0),
    dict(type="gas", line=[(3.3, 50.15), (3.4, 49.9), (3.5, 49.65)], drift=(-0.35, 0.0), t0=s[7] + 0.4, t1=s[7] + 4.0, until=en[7] + 0.2, puffs=70, color=(235, 235, 235)),
    *[BM(p, s[7] + 0.3 + 0.35 * k, 0.26) for k, p in enumerate([(3.15, 50.05), (3.25, 49.85), (3.3, 49.7), (3.1, 49.95), (3.35, 49.6), (3.2, 50.1)])],
    M_([(3.55, 50.05), (3.2, 50.0), (2.85, 49.95)], s[7] + 1.8, s[7] + 5.4, DEG, kind="stormtrooper", soldiers=5, ships=False, until=en[7] + 0.2),
    M_([(3.6, 49.8), (3.25, 49.78), (2.8, 49.75)], s[7] + 2.0, s[7] + 5.6, DEG, kind="stormtrooper", soldiers=5, ships=False, until=en[7] + 0.2),
    M_([(3.65, 49.6), (3.3, 49.6), (3.0, 49.62)], s[7] + 2.2, s[7] + 5.8, DEG, kind="stormtrooper", soldiers=4, ships=False, until=en[7] + 0.2),
    PP("ludendorff", "ERICH LUDENDORFF", "GERMAN ARMY COMMAND", s[7] + 0.4, en[7] + 0.2, x=300),
    # deeper still, the Paris Gun, and the Americans at Château-Thierry
    FR(MICH, BLU, s[8] - 0.2, en[8] + 0.2, s[8] + 0.6, s[8] + 3.2, al=AL1),
    BM((2.3, 48.86), s[8] + 2.4, 0.3), BM((2.38, 48.84), s[8] + 3.1, 0.26),
    M_([(3.0, 48.75), (3.2, 48.92), (3.36, 49.02)], s[8] + 3.8, en[8], USB, kind="doughboy", soldiers=6, ships=False, until=en[8] + 0.2),
    # Amiens: tanks, aircraft, Australians and Canadians break through
    FR(BLU, HUND, s[9] - 0.2, en[9] + 0.2, s[9] + 1.2, s[9] + 6.0, al=AL1),
    VH("tank1916", [(2.42, 49.86), (2.55, 49.86), (2.66, 49.85)], s[9] + 0.5, s[9] + 3.4, until=en[9] + 0.2),
    VH("tank1916", [(2.42, 49.78), (2.55, 49.78), (2.66, 49.77)], s[9] + 0.7, s[9] + 3.6, until=en[9] + 0.2),
    VH("tank1916", [(2.45, 49.70), (2.58, 49.70), (2.68, 49.70)], s[9] + 0.9, s[9] + 3.8, until=en[9] + 0.2),
    VH("plane", [(2.2, 49.95), (2.5, 49.9), (2.85, 49.85)], s[9] + 0.6, s[9] + 3.2, scale=0.9),
    VH("plane", [(2.2, 49.75), (2.5, 49.78), (2.85, 49.8)], s[9] + 1.0, s[9] + 3.6, scale=0.9),
    M_([(2.35, 49.84), (2.5, 49.84), (2.62, 49.84)], s[9] + 1.0, s[9] + 3.8, BRC, kind="brodie", soldiers=4, ships=False, until=en[9] + 0.2),
    M_([(2.35, 49.74), (2.5, 49.74), (2.62, 49.74)], s[9] + 1.2, s[9] + 4.0, (220, 80, 80), kind="brodie", soldiers=4, ships=False, until=en[9] + 0.2),
    BM((2.68, 49.86), s[9] + 2.2, 0.26), BM((2.7, 49.76), s[9] + 2.7, 0.26), BM((2.72, 49.7), s[9] + 3.2, 0.26),
    # collapse: Damascus, the sailors' mutiny, the Kaiser leaves Spa for the Netherlands; the Germans fall back
    FR(HUND, ARM, s[10] - 0.2, s[11] + 2.8, s[10] + 2.4, s[10] + 4.8, al=AL1),
    M_([(36.9, 32.2), (36.5, 32.9), (36.3, 33.45)], s[10] + 0.4, s[10] + 2.6, ARAB, kind="arabrevolt", soldiers=4, ships=False, until=s[10] + 3.2),
    dict(type="glow", pos=(10.1, 54.3), t0=s[10] + 1.9, t1=en[10], radius=160, a0=40, a1=120),
    VH("train", [(5.86, 50.49), (5.72, 50.77), (5.6, 51.3), (5.46, 52.0)], s[10] + 3.8, en[10] - 0.2, until=en[10] + 0.2),
    PP("wilhelm2", "WILHELM II", "GERMAN EMPEROR", s[10] + 3.4, en[10] + 0.2, x=780),
    # the armistice: signed in a railway carriage, the guns fall silent at 11:00
    VH("train", [(2.7, 49.41), (2.82, 49.42), (2.93, 49.43)], s[11] + 0.3, s[11] + 1.8, until=en[11] + 0.2),
    PP("foch", "FERDINAND FOCH", "ALLIED SUPREME COMMANDER", s[11] + 0.4, en[11] + 0.2, x=300),
    dict(type="glow", pos=(4.6, 49.9), t0=s[11] + 2.8, t1=en[11], radius=320, a0=30, a1=90),
]
routes = [dict(pts=[(13.4, 52.5), (2.0, 53.5), (-30.0, 48.0), (-60.0, 42.0), (-77.0, 38.9), (-90.0, 28.0), (-99.1, 19.4)],
               t0=s[4] + 0.4, t1=s[4] + 3.0, until=en[4] + 0.2, color=(240, 205, 90)),
          dict(pts=[(3.52, 49.62), (3.2, 49.5), (2.8, 49.2), (2.35, 48.86)], t0=s[8] + 1.4, t1=s[8] + 2.4, until=en[8] + 0.2, color=(240, 205, 90))]

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
    put(fr, glow_text("A WORLD REMADE", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=24, dur=DUR, base_a="/home/claude/shortgen/hd_1916.png", base_b="/home/claude/shortgen/hd_1918.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1917.png", N="/home/claude/shortgen/hd_1918n.png"),
           regions="/home/claude/shortgen/regions_ep24_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1[0], SW1[1], "A", "M"), (SW2[0], SW2[1], "M", "B"), (SW3[0], SW3[1], "B", "N")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 3.4, 0.2), (s[3] + 2.6, 0.2), (s[4] + 3.4, 0.25), (s[5] + 2.4, 0.25),
                                              (s[6] + 2.4, 0.2), (s[7] + 0.4, 0.25), (s[8] + 2.4, 0.25), (s[9] + 0.6, 0.25), (s[10] + 2.4, 0.25),
                                              (s[11] + 2.8, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
