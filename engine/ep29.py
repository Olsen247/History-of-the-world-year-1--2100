"""Episode 29 – Year 1945: the Second World War, part 4 – the end of the war.
Sicily (10 July 1943), Mussolini deposed (25 July), Italy's armistice (announced 8 Sept 1943), the Germans seize Rome and the north;
D-Day (6 June 1944: airborne landings in the night, nearly 7,000 vessels, about 156,000 men landed by sea and air on Utah, Omaha,
Gold, Juno and Sword), Paris liberated 25 Aug 1944; Operation Bagration (22 June 1944, Army Group Centre destroyed, the Red Army
reaches the Vistula and Warsaw's Praga suburb, some 500-600 km); Leyte Gulf (23-26 Oct 1944, first organised kamikaze attacks on
25 Oct); the Ardennes offensive (16 Dec 1944, Bastogne encircled, relieved by Patton's Third Army 26 Dec); Auschwitz reached by the
Red Army 27 Jan 1945, six million Jews murdered in camps, ghettos and mass shootings; Iwo Jima (19 Feb - 26 Mar 1945, about 21,000
defenders, 216 captured); Berlin (16 Apr - 2 May 1945, about 2.5 million Soviet soldiers; Hitler's suicide 30 Apr; surrender in
force 8 May); Hiroshima 6 Aug, Nagasaki 9 Aug, Soviet invasion of Manchuria 9 Aug; Japan signs on USS Missouri 2 Sept 1945;
70-85 million dead in the whole war."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1945)
import world_data_1943 as A_, world_data_1944 as P_, world_data_1945 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep29/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(136.0, 35.5, 1300), (25.0, 45.0, 2950), (13.5, 40.2, 520), (-0.75, 49.45, 170), (26.0, 53.2, 640), (125.6, 11.2, 520),
         (5.6, 50.2, 260), (19.6, 50.4, 380), (141.3, 24.8, 200), (13.9, 52.4, 360), (131.2, 33.8, 400), (139.7, 35.4, 420),
         (20.0, 42.0, 2950)]
ZOOM = {3: (s[3] + 6.0, (1.6, 48.2, 640)), 10: (s[10] + 2.9, (128.0, 41.0, 1100)), 9: (s[9] + 3.0, (14.5, 50.0, 1500)), 11: (s[11] + 1.8, (122.0, 24.0, 1800))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, 60.0, 40.0, 2950), (3.0, *shots[0])]
for i in range(1, len(shots)):
    a, b = endshot[i - 1], shots[i]
    if i >= 2 and abs(a[0] - b[0]) > 60:     # long jump between Europe and the Pacific: pull far out over the world, then drop in
        keys += [(s[i] - 0.85, *a), (s[i] - 0.2, (a[0] + b[0]) / 2, 35.0, 2950), (s[i] + 0.7, *b)]
        continue
    keys.append((s[i] - 0.85, *a))
    keys.append((s[i] + 0.35, *b))
keys.append((DUR, *shots[-1]))
for i, (t, sh) in ZOOM.items(): keys += [(t - 0.6, *shots[i]), (t + 0.6, *sh)]
keys = sorted(keys, key=lambda k: k[0])

SWG = (s[5] - 0.75, s[5] - 0.3)          # 1943 -> late-1944 map during the long swoop to Leyte
SWB = (s[12] - 0.6, s[12] - 0.15)       # late-1944 -> September-1945 map going into the outro
UG, UB = SWG[1] + 0.1, SWB[1] + 0.1
SH = lambda key, a, b, org, under, src, until: dict(key=key, t0=a, t1=b, mode="shatter", origin=org, under=under, piece_src=src, until=until)
reveals = [SH("france_loss", s[3] + 6.3, s[3] + 9.4, (-0.8, 49.3), "G", "A", UG), SH("belgium_loss", s[3] + 7.4, s[3] + 9.6, (3.0, 50.6), "G", "A", UG),
           SH("lux_loss", s[3] + 7.6, s[3] + 9.6, (5.9, 49.6), "G", "A", UG),
           SH("east_loss", s[4] + 0.8, s[4] + 4.6, (30.0, 54.5), "G", "A", UG), dict(key="pl_gain", t0=s[4] + 3.6, t1=s[4] + 5.4, until=UG)]
for k_, org in (("ger_loss", (13.4, 52.5)), ("nl_loss", (5.5, 52.5)), ("dk_loss", (9.5, 56.0)), ("no_loss", (10.7, 59.9)), ("bm_loss", (14.4, 50.1)),
                ("gpl_loss", (21.0, 52.2)), ("kur_loss", (22.0, 57.0)), ("it_loss", (11.0, 44.3)), ("yu_loss", (18.4, 44.0))):
    reveals.append(SH(k_, s[9] + 3.4, s[9] + 5.6, org, "B", "G", UB))
reveals += [SH("man_loss", s[10] + 3.4, s[10] + 5.6, (127.0, 46.0), "B", "G", UB),
            SH("jc_loss", s[11] + 2.2, s[11] + 4.8, (112.0, 2.0), "B", "G", UB), SH("jchina_loss", s[11] + 2.0, s[11] + 4.6, (116.0, 34.0), "B", "G", UB),
            dict(key="korea_n", t0=s[11] + 2.4, t1=s[11] + 4.2, until=UB), dict(key="korea_s", t0=s[11] + 2.6, t1=s[11] + 4.4, until=UB)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250); BRC = (235, 125, 165)
DEC = (175, 175, 190); SOVC = (150, 200, 110); JPC = (245, 120, 95); ITC = (120, 200, 160); FRC = (120, 150, 235)
labels = [
    # hook
    lb("JAPAN", (138.5, 37.8), 2.6, en[0] + 0.2, JPC, kind="emp"),
    # Italy
    ev("SICILY", (14.2, 37.6), s[2] + 0.3, en[2] + 0.2), ev("SALERNO", (14.75, 40.55), s[2] + 3.6, en[2] + 0.2, WT),
    ev("ROME", (12.5, 41.95), s[2] + 4.6, en[2] + 0.2), lb("ITALY", (16.3, 41.3), s[2] + 0.4, en[2] + 0.2, ITC),
    # D-Day: the five beaches
    lb("UTAH", (-1.25, 49.68), s[3] + 1.8, s[3] + 6.0, USB, kind="small"), lb("OMAHA", (-0.85, 49.22), s[3] + 2.0, s[3] + 6.0, USB, kind="small"),
    lb("SWORD", (-0.05, 49.68), s[3] + 2.6, s[3] + 6.0, BRC, kind="small"), ev("NORMANDY", (-0.6, 49.0), s[3] + 0.4, s[3] + 5.8),
    ev("PARIS", (2.35, 48.86), s[3] + 6.8, en[3] + 0.2), lb("FRANCE", (2.0, 46.9), s[3] + 7.4, en[3] + 0.2, FRC),
    # Bagration
    ev("MINSK", (27.56, 54.25), s[4] + 2.2, en[4] + 0.2), ev("VITEBSK", (30.2, 55.19), s[4] + 0.5, s[4] + 3.0, WT),
    ev("BOBRUISK", (29.22, 53.14), s[4] + 0.6, s[4] + 3.0, WT), ev("WARSAW", (19.7, 51.95), s[4] + 3.8, en[4] + 0.2),
    # Leyte Gulf
    ev("LEYTE GULF", (125.4, 10.9), s[5] + 0.6, en[5] + 0.2), lb("PHILIPPINES", (122.0, 13.8), s[5] + 0.8, en[5] + 0.2, USB, kind="small"),
    lb("SURIGAO STRAIT", (125.3, 9.6), s[5] + 1.0, s[5] + 3.4, CYN, kind="small"), lb("SAMAR", (125.9, 12.2), s[5] + 1.0, s[5] + 3.4, WT, kind="small"),
    # Bulge
    ev("BASTOGNE", (4.95, 49.62), s[6] + 2.6, en[6] + 0.2), lb("ARDENNES", (5.6, 50.45), s[6] + 0.4, s[6] + 2.6, WT, kind="small"),
    lb("MEUSE", (4.75, 50.6), s[6] + 0.5, en[6] + 0.2, CYN, kind="small"),
    # Auschwitz
    ev("AUSCHWITZ", (19.2, 49.88), s[7] + 0.6, en[7] + 0.2, WT), ev("KRAKOW", (19.94, 50.06), s[7] + 0.3, s[7] + 2.6, WT),
    # Iwo Jima
    ev("IWO JIMA", (141.32, 25.25), s[8] + 0.4, en[8] + 0.2), lb("MOUNT SURIBACHI", (141.29, 24.4), s[8] + 3.0, en[8] + 0.2, WT, kind="small"),
    # Berlin
    ev("BERLIN", (12.7, 52.0), s[9] + 0.2, en[9] + 0.2), lb("ODER", (14.6, 52.6), s[9] + 0.4, s[9] + 3.0, CYN, kind="small"),
    # bombs and Manchuria
    ev("HIROSHIMA", (133.0, 34.75), s[10] + 0.6, s[10] + 2.9), ev("NAGASAKI", (129.6, 32.4), s[10] + 2.0, s[10] + 2.9),
    ev("MANCHURIA", (126.5, 45.5), s[10] + 3.2, en[10] + 0.2, WT),
    # surrender
    ev("TOKYO BAY", (139.78, 35.35), s[11] + 0.3, s[11] + 2.2),
]
labels += WP.labels(A_, 1943, s[2] + 0.6, SWG[0])
labels += WP.labels(P_, 1944, SWG[1], SWB[0])

ticker = [(0, 1945), (s[1], 1945), (s[1] + 1.3, 1943), (s[2], 1943), (s[3], 1943), (s[3] + 0.6, 1944), (s[7], 1944), (s[7] + 0.5, 1945),
          (DUR, 1945)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1945", l2="THE WAR ENDS", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1943", GOLD), hd(2, "JULY 1943", "SICILY AND ITALY", GOLD),
            hd(3, "6 JUNE 1944", "D-DAY", CYN), hd(4, "22 JUNE 1944", "OPERATION BAGRATION"),
            hd(5, "OCTOBER 1944", "LEYTE GULF", CYN), hd(6, "DECEMBER 1944", "BATTLE OF THE BULGE"),
            hd(7, "27 JANUARY 1945", "AUSCHWITZ", WHITE), hd(8, "FEBRUARY 1945", "IWO JIMA", CYN),
            hd(9, "APRIL 1945", "THE FALL OF BERLIN"), hd(10, "AUGUST 1945", "HIROSHIMA AND NAGASAKI", WHITE),
            hd(11, "2 SEPTEMBER 1945", "JAPAN SURRENDERS", GOLD)]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
GRY = (120, 120, 132); RA = (200, 40, 40); USA = (110, 150, 220); UKR = (210, 110, 140); JAPR = (225, 90, 70)
GERC = ["rgb:120,120,132"] * 6; SOVF = ["rgb:200,40,40"] * 6; USF = ["us"] * 6
FR = lambda p0, p1, a, b, m0, m1, sa=GERC, sb=SOVF, sc=0.8: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1,
                                                                  side_a=sa, side_b=sb, by_segment=True, rows=2, scale=sc)
# Bagration: the German line of 22 June 1944 (Vitebsk, Orsha, Mogilev, Bobruisk) and the line of late August (East Prussia, Narew, Vistula)
BG0 = [(30.6, 55.7), (30.5, 55.1), (30.7, 54.5), (30.6, 53.9), (30.2, 53.3), (29.7, 52.6), (28.8, 52.0)]
BG1 = [(23.0, 55.5), (22.9, 54.6), (22.4, 53.8), (21.7, 53.0), (21.1, 52.3), (21.5, 51.6), (21.9, 50.9)]
# Bulge: the line of 16 December 1944 and the deepest point of the German salient (near Dinant, 24-25 December)
BU0 = [(6.25, 50.55), (6.2, 50.3), (6.1, 50.08), (6.2, 49.88), (6.45, 49.75)]
BU1 = [(6.2, 50.55), (5.75, 50.38), (5.0, 50.25), (5.45, 50.07), (6.0, 49.88)]
fx = [
    # hook: the war ends – a single bomber over Japan, one flash
    GL((13.4, 52.5), 0.3, 2.6, 300, 20, 80),
    VH("bomber", [(145.5, 15.0), (138.0, 28.0), (132.46, 34.39)], 1.6, 4.0, until=4.3),
    BM((132.46, 34.39), 4.1, 0.45), GL((132.46, 34.39), 4.1, en[0] + 0.2, 90, 80, 220),
    # Italy: landings in Sicily from North Africa, across to the mainland and Salerno; the Germans pour in to Rome
    *[VH("landing_craft", [(11.0 + 0.6 * k, 36.6), (13.0 + 0.8 * k, 36.8), (14.2 + 0.6 * k, 37.0)], s[2] + 0.3, s[2] + 2.0, until=s[2] + 2.6) for k in range(3)],
    VH("warship", [(12.0, 36.2), (14.0, 36.6)], s[2] + 0.3, s[2] + 2.0, until=s[2] + 2.6),
    M_([(14.25, 37.15), (14.6, 37.6), (15.4, 38.1), (16.1, 38.6)], s[2] + 1.6, s[2] + 3.6, USA, kind="gi", soldiers=5, ships=False, until=en[2] + 0.2),
    VH("landing_craft", [(14.2, 39.6), (14.8, 40.4)], s[2] + 3.0, s[2] + 4.2, until=en[2] + 0.2),
    M_([(11.4, 47.0), (11.3, 45.4), (11.7, 43.8), (12.45, 42.1)], s[2] + 4.0, s[2] + 6.8, GRY, kind="wehrmacht", soldiers=6, ships=False, until=en[2] + 0.2),
    PP("mussolini", "BENITO MUSSOLINI", "DICTATOR OF ITALY", s[2] + 2.0, en[2] + 0.2, x=300),
    PP("montgomery", "BERNARD MONTGOMERY", "COMMANDER, EIGHTH ARMY", s[2] + 0.6, s[2] + 3.8, x=780),
    # D-Day: paratroopers in the night, the armada crosses the Channel, five beaches; then Paris is freed
    *[VH("plane", [(-1.6 + 0.35 * k, 51.0), (-1.4 + 0.35 * k, 50.0), (-1.3 + 0.45 * k, 49.3)], s[3] + 0.2 + 0.15 * k, s[3] + 1.8 + 0.15 * k, until=s[3] + 2.2)
      for k in range(3)],
    *[VH("landing_craft", [(-1.3 + 0.25 * k, 50.6), (-1.2 + 0.24 * k, 49.9), (bx, by)], s[3] + 1.2 + 0.15 * k, s[3] + 3.4 + 0.15 * k, until=s[3] + 6.0)
      for k, (bx, by) in enumerate([(-1.18, 49.43), (-0.87, 49.38), (-0.57, 49.35), (-0.4, 49.35), (-0.28, 49.31)])],
    VH("warship", [(-1.0, 50.7), (-0.9, 49.7)], s[3] + 1.0, s[3] + 3.2, until=s[3] + 6.0),
    VH("warship", [(-0.5, 50.7), (-0.4, 49.65)], s[3] + 1.2, s[3] + 3.4, until=s[3] + 6.0),
    *[BM(p, s[3] + 3.4 + 0.2 * k, 0.24) for k, p in enumerate([(-1.18, 49.42), (-0.87, 49.37), (-0.57, 49.34), (-0.4, 49.34), (-0.28, 49.3)])],
    M_([(-1.18, 49.42), (-1.3, 49.3), (-1.4, 49.15)], s[3] + 3.8, s[3] + 5.8, USA, kind="gi", soldiers=4, ships=False, until=s[3] + 6.0),
    M_([(-0.87, 49.37), (-0.85, 49.25), (-0.8, 49.15)], s[3] + 3.9, s[3] + 5.8, USA, kind="gi", soldiers=4, ships=False, until=s[3] + 6.0),
    M_([(-0.45, 49.34), (-0.42, 49.24), (-0.38, 49.15)], s[3] + 4.0, s[3] + 5.8, UKR, kind="tommy44", soldiers=5, ships=False, until=s[3] + 6.0),
    PP("eisenhower", "DWIGHT D. EISENHOWER", "SUPREME ALLIED COMMANDER", s[3] + 0.6, en[3] + 0.2, x=780),
    GL((2.35, 48.86), s[3] + 6.8, en[3] + 0.2, 60, 60, 160),
    # Bagration: the front collapses and races west to the Vistula; tanks punch through at Vitebsk and Bobruisk
    FR(BG0, BG1, s[4] + 0.2, en[4] + 0.2, s[4] + 0.8, s[4] + 4.6, sc=0.5),
    VH("tank", [(31.2, 55.3), (29.5, 54.8), (27.6, 54.0)], s[4] + 0.6, s[4] + 2.8, until=en[4] + 0.2),
    VH("tank", [(30.3, 52.9), (28.8, 53.3), (27.7, 53.8)], s[4] + 0.7, s[4] + 2.8, until=en[4] + 0.2),
    M_([(28.0, 53.6), (25.8, 53.0), (23.6, 52.5)], s[4] + 2.6, s[4] + 4.6, RA, kind="redarmy41", soldiers=6, ships=False, until=en[4] + 0.2),
    BM((30.2, 55.15), s[4] + 1.0, 0.28), BM((29.2, 53.15), s[4] + 1.2, 0.28),
    PP("rokossovsky", "KONSTANTIN ROKOSSOVSKY", "COMMANDER, 1ST BELORUSSIAN FRONT", s[4] + 0.6, en[4] + 0.2, x=780),
    # Leyte Gulf: the US fleet and landings, Japan's fleet comes from three sides, the kamikazes dive
    *[VH("carrier", [(128.5 + 0.4 * k, 12.6 - 0.5 * k), (126.6 + 0.3 * k, 11.6 - 0.4 * k)], s[5] + 0.3, s[5] + 2.0, until=en[5] + 0.2) for k in range(2)],
    VH("landing_craft", [(126.2, 11.0), (125.15, 10.95)], s[5] + 0.4, s[5] + 1.8, until=s[5] + 3.0),
    VH("warship", [(123.0, 8.0), (124.6, 9.4), (125.35, 10.2)], s[5] + 0.8, s[5] + 2.4, until=s[5] + 3.2),
    VH("warship", [(123.0, 13.4), (124.3, 12.6), (125.6, 12.2), (126.2, 11.9)], s[5] + 0.8, s[5] + 2.6, until=s[5] + 3.4),
    BM((125.3, 10.1), s[5] + 2.5, 0.28), BM((126.1, 11.9), s[5] + 2.7, 0.26),
    *[VH("plane", [(121.5, 15.0 - 0.4 * k), (124.5, 13.0 - 0.4 * k), (126.6 + 0.3 * k, 11.5 - 0.4 * k)], s[5] + 3.2 + 0.25 * k, s[5] + 4.6 + 0.25 * k,
         until=s[5] + 4.8 + 0.25 * k) for k in range(2)],
    *[BM((126.6 + 0.3 * k, 11.5 - 0.4 * k), s[5] + 4.7 + 0.25 * k, 0.26) for k in range(2)],
    PP("macarthur", "DOUGLAS MACARTHUR", "GENERAL, SOUTH-WEST PACIFIC", s[5] + 0.6, en[5] + 0.2, x=780),
    # Bulge: German tanks push west through the forest towards the Meuse; Bastogne surrounded; Patton's tanks from the south
    FR(BU0, BU1, s[6] + 0.2, en[6] + 0.2, s[6] + 0.6, s[6] + 3.0, sb=USF, sc=0.42),
    VH("tank", [(6.4, 50.3), (5.8, 50.3), (5.1, 50.25)], s[6] + 0.6, s[6] + 3.0, until=s[6] + 4.4),
    GL((5.72, 50.0), s[6] + 2.6, en[6] + 0.2, 45, 60, 160),
    VH("tank", [(6.1, 49.45), (5.85, 49.75), (5.73, 49.97)], s[6] + 3.4, s[6] + 5.2, until=en[6] + 0.2),
    PP("patton", "GEORGE S. PATTON", "COMMANDER, US THIRD ARMY", s[6] + 3.2, en[6] + 0.2, x=780),
    # Auschwitz: no battle effects – Soviet soldiers arrive, then only quiet lights
    M_([(20.6, 50.7), (19.9, 50.4), (19.45, 50.18)], s[7] + 0.3, s[7] + 2.4, RA, kind="redarmy41", soldiers=4, ships=False, until=s[7] + 3.6),
    GL((19.2, 50.03), s[7] + 2.4, en[7] + 0.2, 70, 20, 80),
    # Iwo Jima: the fleet, the landing craft run in, Marines across the black sand towards Mount Suribachi
    *[VH("warship", [(141.9 + 0.2 * k, 24.3 + 0.3 * k), (141.6 + 0.15 * k, 24.62 + 0.2 * k)], s[8] + 0.2, s[8] + 1.6, until=en[8] + 0.2) for k in range(3)],
    *[VH("landing_craft", [(141.55, 24.66 + 0.05 * k), (141.36, 24.74 + 0.03 * k)], s[8] + 0.8 + 0.2 * k, s[8] + 2.2 + 0.2 * k, until=s[8] + 3.4) for k in range(3)],
    *[BM((141.3 + 0.03 * k, 24.77 + 0.02 * k), s[8] + 1.6 + 0.4 * k, 0.2) for k in range(3)],
    GL((141.29, 24.75), s[8] + 3.4, en[8] + 0.2, 40, 30, 110),
    # Berlin: Zhukov's tanks across the Oder at Seelow, Konev from the south; the ring closes; then all of Europe is freed
    VH("tank", [(14.65, 52.6), (14.1, 52.55), (13.55, 52.52)], s[9] + 0.4, s[9] + 2.6, until=s[9] + 3.4),
    VH("tank", [(14.6, 51.6), (14.0, 52.0), (13.45, 52.42)], s[9] + 0.6, s[9] + 2.8, until=s[9] + 3.4),
    M_([(14.6, 52.75), (14.0, 52.7), (13.5, 52.56)], s[9] + 0.5, s[9] + 2.8, RA, kind="redarmy41", soldiers=6, ships=False, until=s[9] + 3.4),
    BM((14.38, 52.68), s[9] + 0.8, 0.26), BM((13.4, 52.52), s[9] + 2.6, 0.3), GL((13.4, 52.52), s[9] + 2.6, en[9] + 0.2, 120, 40, 120),
    PP("zhukov", "GEORGY ZHUKOV", "COMMANDER, 1ST BELORUSSIAN FRONT", s[9] + 0.4, en[9] + 0.2, x=780),
    # the atomic bombs; the Soviet tank armies sweep into Manchuria from three sides
    VH("bomber", [(145.7, 15.1), (137.0, 28.0), (132.46, 34.39)], s[10] + 0.2, s[10] + 1.2, until=s[10] + 1.4),
    BM((132.46, 34.39), s[10] + 1.3, 0.45), GL((132.46, 34.39), s[10] + 1.3, en[10] + 0.2, 80, 80, 220),
    VH("bomber", [(145.7, 15.1), (134.0, 28.0), (129.87, 32.75)], s[10] + 1.4, s[10] + 2.3, until=s[10] + 2.5),
    BM((129.87, 32.75), s[10] + 2.4, 0.42), GL((129.87, 32.75), s[10] + 2.4, en[10] + 0.2, 70, 80, 220),
    dict(type="icon", icon="fire", pos=(132.46, 34.1), t0=s[10] + 1.5, t1=en[10] + 0.2, scale=0.55),
    VH("tank", [(117.5, 49.0), (121.5, 46.5), (124.5, 45.2)], s[10] + 3.0, s[10] + 5.4, until=en[10] + 0.2),
    VH("tank", [(131.5, 44.5), (129.5, 44.8), (127.0, 45.3)], s[10] + 3.2, s[10] + 5.4, until=en[10] + 0.2),
    M_([(127.6, 50.3), (126.9, 48.0), (126.6, 46.0)], s[10] + 3.2, s[10] + 5.6, RA, kind="redarmy41", soldiers=5, ships=False, until=en[10] + 0.2),
    PP("truman", "HARRY S. TRUMAN", "PRESIDENT OF THE UNITED STATES", s[10] + 0.4, en[10] + 0.2, x=780),
    # the surrender in Tokyo Bay, then Japan's empire falls apart
    *[VH("warship", [(140.2 + 0.15 * k, 34.6 + 0.12 * k), (139.8 + 0.08 * k, 35.25 + 0.05 * k)], s[11] + 0.2, s[11] + 1.6, until=s[11] + 2.4) for k in range(3)],
    GL((139.78, 35.32), s[11] + 0.3, s[11] + 2.2, 40, 60, 160),
    PP("macarthur", "DOUGLAS MACARTHUR", "SUPREME COMMANDER, ALLIED POWERS", s[11] + 0.3, en[11] + 0.2, x=780),
]
routes = [dict(pts=[(-1.2, 50.65), (-0.9, 49.8), (-0.7, 49.4)], t0=s[3] + 1.0, t1=s[3] + 3.0, until=s[3] + 6.0, color=(240, 240, 240)),
          dict(pts=[(145.7, 15.1), (137.0, 28.0), (132.46, 34.39)], t0=s[10] + 0.2, t1=s[10] + 1.2, until=en[10] + 0.2, color=(240, 205, 90))]

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
    put(fr, glow_text("YEAR 1953", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE IRON CURTAIN AND KOREA", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=29, dur=DUR, base_a="/home/claude/shortgen/hd_1943.png", base_b="/home/claude/shortgen/hd_1945.png",
           extra_bases=dict(G="/home/claude/shortgen/hd_1944.png"),
           regions="/home/claude/shortgen/regions_ep29_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWG[0], SWG[1], "A", "G"), (SWB[0], SWB[1], "G", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (4.1, 0.3), (s[2] + 1.8, 0.2), (s[3] + 3.4, 0.25), (s[4] + 1.0, 0.2),
                                              (s[5] + 2.5, 0.2), (s[6] + 0.6, 0.2), (s[8] + 1.6, 0.2), (s[9] + 2.6, 0.25),
                                              (s[10] + 1.3, 0.35), (s[10] + 2.4, 0.3), (s[11] + 2.2, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
