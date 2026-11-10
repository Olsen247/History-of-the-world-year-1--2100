"""Episode 25 – Year 1922: the world after the First World War.
The Spanish flu (autumn 1918), the new nations of 1918 (Poland after 123 years, Czechoslovakia, the Baltic states …),
Versailles (28 June 1919: colonies, ~13 % of Germany's land, army capped at 100,000), the League of Nations (10 Jan 1920,
without the USA) and the British/French mandates (San Remo, April 1920), the Battle of Warsaw (13-25 Aug 1920, Piłsudski's
flank attack from the Wieprz on 16 Aug), Wrangel's evacuation of the Crimea (13-16 Nov 1920, ~126 ships), the Anglo-Irish
Treaty (6 Dec 1921), the March on Rome (27-30 Oct 1922), Kemal's victory over Greece (Aug-Sept 1922) and the end of the
sultanate (1 Nov 1922), the founding of the USSR (30 Dec 1922)."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1920)
import world_data_1918n as A, world_data_1920 as M, world_data_1922 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep25/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (18.0, 48.0, 1500)
shots = [(20.0, 50.0, 1300), WIDE, (-30.0, 30.0, 2850), (21.0, 51.0, 800), (8.0, 50.5, 620), (39.0, 33.5, 560), (22.0, 52.2, 300),
         (31.5, 43.5, 480), (-6.8, 53.8, 300), (11.8, 43.2, 420), (30.0, 39.0, 560), (55.0, 55.0, 2000), (14.0, 47.0, 2600)]
endshot = list(shots)
keys = [(0.0, 20.0, 50.0, 1000), (3.0, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))
# line 5: Geneva first (the League), then fly to the Middle East
GENEVA = (6.5, 46.5, 300)
keys = [k for k in keys if k[0] != s[5] + 0.35] + [(s[5] + 0.35, *GENEVA), (s[5] + 1.8, *GENEVA), (s[5] + 3.0, *shots[5])]
keys = sorted(keys, key=lambda k: k[0])

SWM = (s[6] - 0.85, s[6] - 0.25)          # 1918 -> 1920 map while flying to Warsaw
SWB = (s[12] - 0.85, s[12] - 0.25)        # 1920 -> 1922 map while flying out for the outro
UM, UB = SWM[1] + 0.1, SWB[1] + 0.1
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("poland", s[3] + 0.5, s[3] + 2.6, UM), rv("czech", s[3] + 2.4, s[3] + 4.0, UM), rv("scs", s[3] + 2.8, s[3] + 4.6, UM),
           rv("austria", s[3] + 2.6, s[3] + 4.0, UM), rv("hungary", s[3] + 2.8, s[3] + 4.2, UM), rv("romania", s[3] + 3.2, s[3] + 4.8, UM),
           rv("lithuania", s[3] + 5.0, s[3] + 6.4, UM), rv("latvia", s[3] + 5.2, s[3] + 6.6, UM), rv("estonia", s[3] + 5.4, s[3] + 6.8, UM),
           dict(key="ger_loss", t0=s[4] + 2.2, t1=s[4] + 4.6, mode="shatter", origin=(10.0, 51.0), under="M", piece_src="A", until=UM),
           rv("br_mand", s[5] + 3.4, s[5] + 5.6, UM), rv("fr_mand", s[5] + 3.6, s[5] + 5.6, UM),
           dict(key="whites", t0=s[7] + 2.6, t1=s[7] + 5.0, mode="shatter", origin=(34.0, 45.0), under="B", piece_src="M", until=UB),
           rv("ireland", s[8] + 0.6, s[8] + 2.8, UB), rv("turkey", s[10] + 0.8, s[10] + 3.4, UB), rv("ussr", s[11] + 0.6, s[11] + 4.6, UB)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); GRN = (150, 215, 110); USB = (150, 190, 250)
BRC = (235, 125, 165); OTC = (200, 60, 60); SOVC = (150, 200, 110); DEC = (150, 150, 165); PLC = (240, 110, 120); FRC = (120, 150, 240)
labels = [
    # hook: the 1922 map of Europe
    lb("SOVIET UNION", (32.0, 55.5), 0.6, en[0] + 0.2, SOVC, kind="emp"), lb("POLAND", (19.5, 52.2), 1.0, en[0] + 0.2, PLC),
    lb("GERMANY", (10.3, 51.0), 1.2, en[0] + 0.2, DEC), lb("TURKEY", (33.0, 39.2), 1.4, en[0] + 0.2, OTC),
    # flu
    lb("ATLANTIC", (-38.0, 36.0), s[2] + 0.3, en[2] + 0.2, CYN), lb("UNITED STATES", (-98.0, 39.0), s[2] + 0.4, en[2] + 0.2, USB),
    lb("EUROPE", (12.0, 50.0), s[2] + 0.4, en[2] + 0.2, WT), lb("AFRICA", (18.0, 8.0), s[2] + 0.6, en[2] + 0.2, WT),
    # new nations
    lb("POLAND", (19.5, 52.2), s[3] + 1.2, en[3] + 0.2, PLC), lb("CZECHOSLOVAKIA", (16.8, 49.45), s[3] + 3.0, en[3] + 0.2, (140, 180, 240), kind="small"),
    lb("AUSTRIA", (14.3, 47.45), s[3] + 3.0, en[3] + 0.2, (240, 225, 120), kind="small"), lb("HUNGARY", (19.4, 47.0), s[3] + 3.2, en[3] + 0.2, (150, 200, 130), kind="small"),
    lb("SERBS, CROATS & SLOVENES", (18.6, 44.2), s[3] + 3.4, en[3] + 0.2, (220, 140, 140), kind="small"),
    lb("LITHUANIA", (23.9, 55.3), s[3] + 5.4, en[3] + 0.2, (220, 190, 120), kind="small"), lb("LATVIA", (25.6, 56.85), s[3] + 5.6, en[3] + 0.2, (230, 140, 150), kind="small"),
    lb("ESTONIA", (25.8, 58.75), s[3] + 5.8, en[3] + 0.2, (140, 175, 235), kind="small"),
    # Versailles
    ev("VERSAILLES", (2.3, 49.25), s[4] + 0.3, en[4] + 0.2), lb("GERMANY", (10.3, 51.2), s[4] + 0.3, en[4] + 0.2, DEC),
    lb("ALSACE-LORRAINE", (6.9, 48.35), s[4] + 2.6, en[4] + 0.2, FRC, kind="small"), lb("TO POLAND", (15.4, 52.6), s[4] + 2.8, en[4] + 0.2, PLC, kind="small"),
    # League of Nations, the mandates
    ev("GENEVA", (6.15, 46.0), s[5] + 0.4, s[5] + 2.4), lb("OTTOMAN EMPIRE", (33.0, 39.0), s[5] + 2.6, en[5] + 0.2, OTC),
    lb("IRAQ", (44.0, 32.8), s[5] + 4.0, en[5] + 0.2, BRC), lb("PALESTINE", (34.0, 31.0), s[5] + 4.0, en[5] + 0.2, BRC, kind="small"),
    lb("SYRIA", (38.5, 35.0), s[5] + 4.2, en[5] + 0.2, FRC), 
    # Warsaw
    ev("WARSAW", (20.4, 51.7), s[6] + 0.3, en[6] + 0.2), lb("VISTULA", (19.9, 52.55), s[6] + 1.0, en[6] + 0.2, CYN, kind="small"),
    lb("WIEPRZ", (22.6, 51.25), s[6] + 2.6, en[6] + 0.2, CYN, kind="small"), 
    # Crimea
    ev("CRIMEA", (35.8, 45.6), s[7] + 0.3, en[7] + 0.2), 
    lb("BLACK SEA", (33.0, 43.2), s[7] + 0.5, en[7] + 0.2, CYN, kind="small"), ev("CONSTANTINOPLE", (28.3, 40.6), s[7] + 3.2, en[7] + 0.2, WT),
    # Ireland
    lb("IRISH FREE STATE", (-8.3, 52.8), s[8] + 1.4, en[8] + 0.2, (120, 210, 130)), ev("DUBLIN", (-6.26, 53.55), s[8] + 0.6, en[8] + 0.2, WT),
    lb("NORTHERN IRELAND", (-6.7, 54.85), s[8] + 3.0, en[8] + 0.2, BRC, kind="small"), lb("BRITAIN", (-2.9, 54.2), s[8] + 0.4, en[8] + 0.2, BRC),
    # Rome
    ev("ROME", (12.5, 41.3), s[9] + 0.3, en[9] + 0.2), lb("ITALY", (10.6, 44.1), s[9] + 0.3, en[9] + 0.2, (120, 200, 160)),
    lb("MILAN", (9.19, 45.3), s[9] + 0.6, s[9] + 3.2, WT, kind="small"),
    # Turkey
    ev("SMYRNA", (26.6, 37.3), s[10] + 0.3, en[10] + 0.2), ev("ANKARA", (32.85, 39.75), s[10] + 0.6, en[10] + 0.2, WT),
    lb("TURKEY", (34.5, 38.6), s[10] + 3.0, en[10] + 0.2, OTC), lb("GREECE", (22.0, 39.3), s[10] + 0.4, en[10] + 0.2, (140, 190, 240)),
    ev("CONSTANTINOPLE", (29.0, 41.3), s[10] + 3.6, en[10] + 0.2, WT),
    # USSR
    lb("SOVIET UNION", (66.0, 60.0), s[11] + 1.6, en[11] + 0.2, SOVC, kind="emp"), ev("MOSCOW", (37.6, 55.6), s[11] + 0.4, en[11] + 0.2, WT),
    lb("UKRAINE", (31.5, 49.0), s[11] + 1.4, en[11] + 0.2, SOVC, kind="small"), lb("BELARUS", (28.0, 53.6), s[11] + 1.6, en[11] + 0.2, SOVC, kind="small"),
    lb("TRANSCAUCASIA", (45.0, 41.3), s[11] + 1.8, en[11] + 0.2, SOVC, kind="small"),
]
labels += WP.labels(A, 1918, s[2] + 0.6, SWM[0])
labels += WP.labels(M, 1920, SWM[1], s[12])

ticker = [(0, 1922), (s[1], 1922), (s[1] + 1.3, 1918), (s[4], 1918), (s[4] + 0.6, 1919), (s[5], 1919), (s[5] + 0.6, 1920), (s[8], 1920),
          (s[8] + 0.6, 1921), (s[9], 1921), (s[9] + 0.6, 1922), (DUR, 1922)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1922", l2="A WORLD REMADE", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1918", GOLD), hd(2, "AUTUMN 1918", "THE SPANISH FLU", GRN), hd(3, "1918", "NEW NATIONS", GOLD),
            hd(4, "28 JUNE 1919", "VERSAILLES"), hd(5, "1920", "LEAGUE OF NATIONS", CYN), hd(6, "AUGUST 1920", "BATTLE OF WARSAW"),
            hd(7, "NOVEMBER 1920", "THE WHITES FLEE"), hd(8, "DECEMBER 1921", "IRISH FREE STATE", GRN), hd(9, "OCTOBER 1922", "MARCH ON ROME"),
            hd(10, "1922", "THE SULTANATE ENDS", GOLD), hd(11, "30 DECEMBER 1922", "THE SOVIET UNION")]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
RA = (200, 40, 40); PLS = (225, 80, 90); BLK = (40, 40, 45); TRK = (200, 60, 60); GRK = (90, 140, 210)
# Battle of Warsaw: the Red Army front closes on Warsaw (12-15 Aug), then the Polish counter-attack throws it back (16-25 Aug)
W0 = [(21.0, 53.9), (22.4, 53.4), (23.5, 52.6), (24.0, 51.8), (24.3, 51.0), (24.6, 50.3), (24.5, 49.6)]
W1 = [(19.6, 53.1), (20.4, 52.65), (21.15, 52.4), (21.5, 52.0), (22.3, 51.6), (23.6, 50.9), (24.1, 49.9)]
W2 = [(21.6, 54.1), (22.8, 53.6), (23.8, 53.0), (24.6, 52.3), (25.0, 51.5), (25.0, 50.6), (24.8, 49.7)]
FR = lambda p0, p1, a, b, m0, m1: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1, side_a=["rgb:200,40,40"] * 6,
                                       side_b=["rgb:235,235,235"] * 6, by_segment=True, rows=2, scale=0.8)
fx = [
    # hook: four empires gone – a glow over the new map
    GL((20.0, 50.0), 1.0, en[0], 520, 20, 70),
    # the flu rides the troopships: ships home from France, sickness flaring in ports around the world
    VH("steamer", [(-4.5, 48.4), (-25.0, 46.0), (-50.0, 43.0), (-71.0, 42.3)], s[2] + 0.3, s[2] + 3.6, until=en[2] + 0.2),
    VH("steamer", [(-1.1, 50.8), (-20.0, 38.0), (-17.0, 18.0), (-13.2, 8.5)], s[2] + 0.5, s[2] + 3.8, until=en[2] + 0.2),
    VH("steamer", [(-71.0, 42.0), (-45.0, 44.5), (-20.0, 47.5), (-4.6, 48.3)], s[2] + 0.8, s[2] + 4.2, until=en[2] + 0.2),
    *[GL(p, s[2] + 1.0 + 0.45 * k, en[2], 150, 30, 120) for k, p in enumerate([(-71.0, 42.3), (-4.5, 48.4), (-13.2, 8.5), (-87.6, 41.9),
                                                                              (2.35, 48.86), (-0.1, 51.5), (-75.2, 39.95), (13.4, 52.5)])],
    # new nations: Piłsudski returns to Warsaw
    PP("pilsudski", "JÓZEF PIŁSUDSKI", "CHIEF OF STATE OF POLAND", s[3] + 1.0, en[3] + 0.2, x=780),
    GL((21.0, 52.23), s[3] + 0.6, s[3] + 3.0, 160, 40, 120),
    # Versailles: the Big Three; Germany's lost lands break away
    GL((2.13, 48.8), s[4] + 0.4, s[4] + 2.6, 120, 40, 130),
    PP("clemenceau", "GEORGES CLEMENCEAU", "PRIME MINISTER OF FRANCE", s[4] + 0.6, en[4] + 0.2, x=300),
    PP("wilson", "WOODROW WILSON", "PRESIDENT OF THE USA", s[4] + 1.0, en[4] + 0.2, x=780),
    # League of Nations, then British and French columns move into the mandates
    GL((6.15, 46.2), s[5] + 0.5, s[5] + 2.4, 120, 40, 130),
    M_([(35.5, 31.2), (38.5, 32.3), (41.5, 33.2), (44.0, 33.3)], s[5] + 3.2, s[5] + 5.6, BRC, kind="brodie", soldiers=5, ships=False, until=en[5] + 0.2),
    M_([(35.6, 34.3), (36.2, 33.8), (36.3, 33.5)], s[5] + 3.4, s[5] + 5.6, (60, 95, 200), kind="ww1", soldiers=4, ships=False, until=en[5] + 0.2),
    # Warsaw: the Red Army closes in, Piłsudski's strike force hits the open southern flank from the Wieprz
    FR(W0, W1, s[6] + 0.2, s[6] + 3.6, s[6] + 0.4, s[6] + 2.6),
    FR(W1, W2, s[6] + 3.5, en[6] + 0.2, s[6] + 4.0, s[6] + 6.6),
    M_([(24.4, 53.2), (23.0, 52.8), (21.6, 52.5)], s[6] + 0.4, s[6] + 2.6, RA, kind="redarmy", soldiers=6, ships=False, until=s[6] + 3.4),
    M_([(22.4, 51.35), (22.7, 51.9), (23.0, 52.5), (23.3, 53.1)], s[6] + 2.8, s[6] + 5.8, PLS, kind="polish1920", soldiers=6, ships=False, until=en[6] + 0.2),
    M_([(21.2, 52.3), (21.9, 52.6), (22.7, 52.9)], s[6] + 3.6, s[6] + 6.0, PLS, kind="polish1920", soldiers=5, ships=False, until=en[6] + 0.2),
    BM((21.18, 52.42), s[6] + 2.2, 0.3), BM((21.4, 52.2), s[6] + 2.8, 0.28), BM((22.5, 51.9), s[6] + 3.6, 0.3),
    PP("pilsudski", "JÓZEF PIŁSUDSKI", "POLISH COMMANDER-IN-CHIEF", s[6] + 2.4, en[6] + 0.2, x=300),
    # Crimea: Reds break through at Perekop, Wrangel's fleet sails for Constantinople; Trotsky's armoured train
    M_([(34.6, 47.3), (33.9, 46.6), (33.7, 46.0), (34.0, 45.3)], s[7] + 0.4, s[7] + 3.6, RA, kind="redarmy", soldiers=6, ships=False, until=en[7] + 0.2),
    VH("warship", [(33.5, 44.6), (31.5, 43.2), (29.0, 41.1)], s[7] + 1.8, s[7] + 5.4, until=en[7] + 0.2),
    VH("steamer", [(35.4, 45.0), (33.5, 43.3), (29.1, 41.2)], s[7] + 2.0, s[7] + 5.8, until=en[7] + 0.2),
    VH("steamer", [(36.4, 45.3), (34.5, 43.6), (29.2, 41.3)], s[7] + 2.3, s[7] + 6.2, until=en[7] + 0.2),
    VH("steamer", [(32.4, 45.2), (31.0, 43.6), (28.9, 41.0)], s[7] + 2.6, s[7] + 6.4, until=en[7] + 0.2),
    VH("train", [(36.2, 50.0), (35.6, 48.6), (35.1, 47.8), (34.6, 46.9)], s[7] + 0.6, s[7] + 3.4, until=en[7] + 0.2),
    PP("trotsky", "LEON TROTSKY", "LEADER OF THE RED ARMY", s[7] + 0.8, en[7] + 0.2, x=780),
    # Ireland: the Free State
    GL((-6.26, 53.35), s[8] + 0.4, en[8], 140, 40, 120),
    PP("collins", "MICHAEL COLLINS", "IRISH TREATY NEGOTIATOR", s[8] + 0.8, en[8] + 0.2, x=780),
    # March on Rome: Blackshirt columns converge, Mussolini arrives from Milan by train
    M_([(12.39, 43.11), (12.45, 42.5), (12.48, 41.98)], s[9] + 0.4, s[9] + 3.2, BLK, kind="blackshirt", soldiers=5, ships=False, until=en[9] + 0.2),
    M_([(12.8, 41.96), (12.65, 41.93), (12.52, 41.91)], s[9] + 0.6, s[9] + 3.0, BLK, kind="blackshirt", soldiers=4, ships=False, until=en[9] + 0.2),
    M_([(11.85, 42.03), (12.2, 41.95), (12.44, 41.9)], s[9] + 0.8, s[9] + 3.4, BLK, kind="blackshirt", soldiers=4, ships=False, until=en[9] + 0.2),
    VH("train", [(9.19, 45.46), (11.34, 44.49), (11.25, 43.77), (11.9, 43.0), (12.5, 41.9)], s[9] + 2.6, en[9] - 0.2, until=en[9] + 0.2),
    PP("mussolini", "BENITO MUSSOLINI", "PRIME MINISTER OF ITALY", s[9] + 2.8, en[9] + 0.2, x=780),
    # Turkey: the Great Offensive drives the Greek army to the sea; Greek ships leave Smyrna
    M_([(30.54, 38.76), (29.4, 38.6), (28.2, 38.5), (27.3, 38.45)], s[10] + 0.4, s[10] + 3.4, TRK, kind="kemalist", soldiers=6, ships=False, until=en[10] + 0.2),
    M_([(30.0, 39.4), (28.9, 39.2), (27.9, 38.9)], s[10] + 0.6, s[10] + 3.6, TRK, kind="kemalist", soldiers=5, ships=False, until=en[10] + 0.2),
    VH("steamer", [(27.0, 38.45), (25.8, 38.2), (24.2, 37.95)], s[10] + 2.6, en[10] - 0.2, until=en[10] + 0.2),
    PP("kemal", "MUSTAFA KEMAL", "TURKISH NATIONAL LEADER", s[10] + 0.6, en[10] + 0.2, x=780),
    # the Soviet Union
    GL((37.6, 55.75), s[11] + 0.4, en[11], 260, 30, 110),
    PP("lenin", "VLADIMIR LENIN", "SOVIET LEADER", s[11] + 0.6, en[11] + 0.2, x=780),
]
routes = [dict(pts=[(-4.5, 48.4), (-30.0, 45.0), (-71.0, 42.3)], t0=s[2] + 0.3, t1=s[2] + 2.0, until=en[2] + 0.2, color=(240, 205, 90)),
          dict(pts=[(33.5, 44.6), (31.0, 43.0), (29.0, 41.0)], t0=s[7] + 1.6, t1=s[7] + 3.2, until=en[7] + 0.2, color=(240, 205, 90))]

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
    put(fr, glow_text("YEAR 1939", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE WORLD AT WAR AGAIN", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=25, dur=DUR, base_a="/home/claude/shortgen/hd_1918n.png", base_b="/home/claude/shortgen/hd_1922.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1920.png"),
           regions="/home/claude/shortgen/regions_ep25_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWM[0], SWM[1], "A", "M"), (SWB[0], SWB[1], "M", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.0, 0.2), (s[3] + 0.6, 0.2), (s[4] + 2.2, 0.25), (s[5] + 3.4, 0.2),
                                              (s[6] + 2.8, 0.25), (s[7] + 2.6, 0.2), (s[8] + 0.6, 0.2), (s[9] + 2.6, 0.2), (s[10] + 0.8, 0.25),
                                              (s[11] + 0.6, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
