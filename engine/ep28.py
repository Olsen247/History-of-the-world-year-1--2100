"""Episode 28 – Year 1943: the Second World War, part 3 – the tide turns.
Japan's conquests (Singapore 15 Feb 1942: about 80,000 British, Indian and Australian troops captured); Midway (4 June 1942:
JN-25 broken, US dive bombers knock out Akagi, Kaga, Soryu and Hiryu); the Battle of the Atlantic (wolf packs, convoys,
Turing and Hut 8 at Bletchley Park); Stalingrad (Chuikov's 62nd Army from 12 Sep 1942, "hugging" the Germans so the Luftwaffe
could not bomb them); Second El Alamein (23 Oct 1942, about 880-900 guns, Montgomery's Eighth Army, Rommel retreats from 2-4 Nov);
Operation Uranus (19-20 Nov 1942, Romanian 3rd and 4th Armies broken, pincers meet near Kalach 22-23 Nov, about 290,000
Axis soldiers trapped); Paulus surrenders 31 Jan 1943 (last pocket 2 Feb), about 91,000 prisoners, about 5,000 came home;
Warsaw Ghetto Uprising (19 Apr 1943) and the Holocaust (mass shootings from 1941, Auschwitz, Treblinka); Black May (43 U-boats
lost in May 1943, Dönitz withdraws 24 May); Kursk (5 July 1943: Soviets forewarned, deep minefields and anti-tank belts,
about 6,000 tanks, 2 million men, the German pincers stopped)."""
import sys
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1943)
import world_data_1941 as A_, world_data_1942 as P_, world_data_1943 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep28/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(30.0, 47.0, 2600), (60.0, 30.0, 2950), (113.0, 8.0, 2950), (-172.0, 28.5, 400), (-33.0, 52.0, 2200), (43.6, 48.9, 520),
         (27.0, 30.9, 650), (43.6, 48.9, 420), (40.0, 49.0, 900), (20.8, 51.6, 600), (-30.0, 54.0, 1700), (36.3, 51.6, 300),
         (20.0, 45.0, 2950)]
ZOOM = {2: (s[2] + 2.3, (103.8, 2.2, 750)), 5: (s[5] + 2.4, (44.5, 48.72, 240))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, 112.0, 14.0, 2950), (3.0, *shots[0])]
for i in range(1, len(shots)):
    if i == 3:   # Singapore -> Midway: pull far out over the world, then drop onto the central Pacific
        keys += [(s[i] - 0.85, *endshot[i - 1]), (s[i] - 0.2, -40.0, 30.0, 2950), (s[i] + 0.7, *shots[i])]
        continue
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))
for i, (t, sh) in ZOOM.items(): keys += [(t - 0.6, *shots[i]), (t + 0.6, *sh)]
keys = sorted(keys, key=lambda k: k[0])

SWP = (s[3] - 0.75, s[3] - 0.3)          # 1941 -> 1942 map during the long swoop to Midway
SWB = (s[9] - 0.85, s[9] - 0.25)        # 1942 -> 1943 map while flying from the Don to Warsaw
UP, UB = SWP[1] + 0.1, SWB[1] + 0.1
reveals = [dict(key="japan", t0=s[2] + 0.4, t1=s[2] + 4.2, until=UP),
           dict(key="egypt_loss", t0=s[6] + 3.0, t1=s[6] + 5.4, mode="shatter", origin=(29.0, 30.9), under="B", piece_src="G", until=UB),
           dict(key="east_loss", t0=s[8] + 1.2, t1=s[8] + 5.0, mode="shatter", origin=(44.5, 48.7), under="B", piece_src="G", until=UB)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250); BRC = (235, 125, 165)
DEC = (175, 175, 190); SOVC = (150, 200, 110); JPC = (245, 120, 95); ITC = (120, 200, 160); ROC = (230, 200, 100)
labels = [
    # hook
    lb("JAPAN", (138.0, 37.5), 0.3, 2.4, JPC, kind="emp"),
    lb("GERMANY", (11.0, 51.0), 2.8, en[0] + 0.2, DEC, kind="emp"), lb("SOVIET UNION", (44.0, 57.0), 3.0, en[0] + 0.2, SOVC, kind="emp"),
    # Japan's conquests
    lb("BURMA", (96.0, 21.5), s[2] + 1.6, s[2] + 2.2, JPC, kind="small"), lb("PHILIPPINES", (123.5, 12.5), s[2] + 1.4, s[2] + 2.2, JPC, kind="small"),
    lb("DUTCH EAST INDIES", (115.0, -1.5), s[2] + 1.6, s[2] + 2.2, JPC, kind="small"),
    ev("SINGAPORE", (103.8, 1.75), s[2] + 2.8, en[2] + 0.2), lb("MALAYA", (101.9, 4.4), s[2] + 3.0, en[2] + 0.2, JPC, kind="small"),
    # Midway
    ev("MIDWAY", (-176.4, 28.55), s[3] + 0.8, en[3] + 0.2),
    # Atlantic
    ev("HALIFAX", (-63.6, 45.3), s[4] + 0.4, s[4] + 3.0, WT), ev("LIVERPOOL", (-3.0, 54.3), s[4] + 0.6, s[4] + 3.0, WT),
    lb("NORTH ATLANTIC", (-38.0, 57.0), s[4] + 0.4, s[4] + 2.8, CYN, kind="small"),
    ev("BLETCHLEY PARK", (-0.74, 52.7), s[4] + 2.9, en[4] + 0.2),
    # Stalingrad
    ev("STALINGRAD", (44.5, 49.02), s[5] + 0.2, s[5] + 2.0), lb("VOLGA", (45.2, 48.35), s[5] + 0.4, s[5] + 2.0, CYN, kind="small"),
    # El Alamein
    ev("EL ALAMEIN", (28.95, 31.3), s[6] + 0.2, en[6] + 0.2), lb("EGYPT", (31.0, 29.7), s[6] + 0.4, en[6] + 0.2, BRC),
    lb("LIBYA", (23.0, 29.7), s[6] + 0.4, en[6] + 0.2, ITC, kind="small"),
    # Uranus
    ev("STALINGRAD", (44.5, 49.02), s[7] + 0.2, en[7] + 0.2, WT), ev("KALACH", (43.0, 48.42), s[7] + 3.0, en[7] + 0.2),
    lb("ROMANIANS", (42.1, 49.95), s[7] + 0.3, s[7] + 2.6, ROC, kind="small"), lb("ROMANIANS", (44.0, 47.75), s[7] + 0.3, s[7] + 2.6, ROC, kind="small"),
    # surrender and the Soviet winter offensive
    ev("STALINGRAD", (44.5, 49.02), s[8] + 0.2, en[8] + 0.2), ev("ROSTOV", (39.7, 46.85), s[8] + 3.4, en[8] + 0.2, WT),
    ev("KHARKOV", (36.25, 49.6), s[8] + 3.8, en[8] + 0.2, WT),
    # Warsaw Ghetto and the death camps
    ev("WARSAW", (20.7, 51.95), s[9] + 0.3, en[9] + 0.2), ev("AUSCHWITZ", (19.2, 49.75), s[9] + 3.4, en[9] + 0.2, WT),
    ev("TREBLINKA", (22.4, 53.1), s[9] + 3.6, en[9] + 0.2, WT),
    # Black May
    lb("NORTH ATLANTIC", (-38.0, 57.0), s[10] + 0.3, en[10] + 0.2, CYN, kind="small"),
    # Kursk
    ev("KURSK", (35.9, 51.6), s[11] + 0.2, en[11] + 0.2), ev("OREL", (36.07, 53.15), s[11] + 0.4, s[11] + 3.0, WT),
    ev("BELGOROD", (36.58, 50.42), s[11] + 0.4, s[11] + 3.0, WT), ev("PROKHOROVKA", (37.9, 51.3), s[11] + 3.2, en[11] + 0.2),
]
labels += WP.labels(A_, 1941, s[2] + 0.6, SWP[0])
labels += WP.labels(P_, 1942, SWP[1], s[9] - 0.8)

ticker = [(0, 1943), (s[1], 1943), (s[1] + 1.3, 1941), (s[2], 1941), (s[2] + 0.6, 1942), (s[8], 1942), (s[8] + 0.5, 1943), (DUR, 1943)]
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1943", l2="THE TIDE TURNS", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1941", GOLD), hd(2, "EARLY 1942", "JAPAN'S BLITZ"),
            hd(3, "4 JUNE 1942", "MIDWAY", CYN), hd(4, "1942", "BATTLE OF THE ATLANTIC", CYN),
            hd(5, "SEPTEMBER 1942", "STALINGRAD"), hd(6, "OCTOBER 1942", "EL ALAMEIN", GOLD),
            hd(7, "19 NOVEMBER 1942", "OPERATION URANUS", GOLD), hd(8, "31 JANUARY 1943", "PAULUS SURRENDERS", GOLD),
            hd(9, "19 APRIL 1943", "THE WARSAW GHETTO RISES", WHITE), hd(10, "MAY 1943", "BLACK MAY", CYN),
            hd(11, "5 JULY 1943", "KURSK")]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
GRY = (120, 120, 132); RA = (200, 40, 40); DAK = (200, 180, 130); JAPR = (225, 90, 70)
GERC = ["rgb:120,120,132"] * 6; SOVF = ["rgb:200,40,40"] * 6
FR = lambda p0, p1, a, b, m0, m1, sa=GERC, sb=SOVF, sc=0.8: dict(type="front", path0=p0, path1=p1, t_in=a, t_out=b, move0=m0, move1=m1,
                                                                  side_a=sa, side_b=sb, by_segment=True, rows=2, scale=sc)
# Stalingrad: the Germans push through the city to the Volga bank
ST0 = [(44.38, 48.92), (44.30, 48.75), (44.34, 48.56)]
ST1 = [(44.56, 48.84), (44.52, 48.71), (44.50, 48.58)]
# Kursk salient: the line of 5 July and where the two German pincers were stopped
K0 = [(37.3, 52.8), (36.9, 52.35), (36.3, 52.2), (35.4, 52.1), (34.7, 52.15), (34.6, 51.8), (34.6, 51.4), (35.0, 50.95), (35.4, 50.6),
      (35.9, 50.55), (36.4, 50.75), (36.8, 50.7), (37.1, 50.3)]
K1 = [(37.3, 52.8), (36.8, 52.2), (36.35, 52.05), (35.4, 52.1), (34.7, 52.15), (34.6, 51.8), (34.6, 51.4), (35.0, 50.95), (35.4, 50.6),
      (36.0, 50.8), (36.5, 51.0), (36.85, 50.95), (37.1, 50.3)]
fx = [
    # hook: the Axis at its height – then the tide turns at Stalingrad
    GL((13.4, 52.5), 3.0, en[0], 380, 20, 70), VH("tank", [(14.0, 52.4), (30.0, 50.0), (44.3, 48.75)], 3.0, 5.2, until=en[0] + 0.2),
    BM((44.5, 48.7), 5.3, 0.3),
    # Japan storms across Asia: Malaya by land and bicycle, landings in the Philippines and the Indies, Singapore falls
    M_([(100.6, 6.4), (101.6, 4.0), (103.0, 2.0), (103.8, 1.45)], s[2] + 0.4, s[2] + 3.0, JAPR, kind="ija", soldiers=6, ships=False, until=en[2] + 0.2),
    VH("warship", [(121.0, 22.5), (120.4, 18.6), (120.3, 16.0)], s[2] + 0.4, s[2] + 2.2, until=s[2] + 2.4),
    VH("warship", [(114.0, 8.0), (110.0, 0.0), (107.0, -5.8)], s[2] + 0.6, s[2] + 2.2, until=s[2] + 2.4),
    VH("bomber", [(107.0, 10.5), (104.5, 4.0), (103.85, 1.4)], s[2] + 2.2, s[2] + 3.2, until=s[2] + 3.8), BM((103.85, 1.35), s[2] + 3.2, 0.3),
    PP("yamashita", "TOMOYUKI YAMASHITA", "GENERAL, 25TH ARMY", s[2] + 2.6, en[2] + 0.2, x=300),
    # Midway: the four Japanese carriers north-west of Midway; US carriers from Pearl Harbor; the dive bombers strike
    *[VH("carrier", [(-178.2 + 0.25 * k, 33.0 - 0.2 * k), (-177.9 + 0.25 * k, 31.4 - 0.2 * k)], s[3] + 0.4, s[3] + 2.2, until=s[3] + 3.4 + 0.3 * k)
      for k in range(4)],
    VH("carrier", [(-164.0, 25.5), (-168.5, 29.5), (-172.5, 31.8)], s[3] + 0.6, s[3] + 2.6, until=en[3] + 0.2),
    *[VH("bomber", [(-172.5, 32.0 - 0.3 * k), (-176.0, 31.8 - 0.2 * k), (-177.9 + 0.25 * k, 31.4 - 0.2 * k)], s[3] + 2.4 + 0.2 * k, s[3] + 3.4 + 0.2 * k,
         until=s[3] + 3.8 + 0.2 * k) for k in range(2)],
    *[BM((-177.9 + 0.25 * k, 31.4 - 0.2 * k), s[3] + 3.4 + 0.3 * k, 0.26) for k in range(4)],
    dict(type="icon", icon="fire", pos=(-177.6, 31.2), t0=s[3] + 4.4, t1=en[3] + 0.2, scale=0.6),
    PP("nimitz", "CHESTER NIMITZ", "ADMIRAL, US PACIFIC FLEET", s[3] + 0.8, en[3] + 0.2, x=780),
    PP("yamamoto", "ISOROKU YAMAMOTO", "ADMIRAL, COMBINED FLEET", s[3] + 1.2, en[3] + 0.2, x=300),
    # Atlantic: a convoy from Halifax to Liverpool, a wolf pack from the French U-boat bases closes in; Bletchley Park
    *[VH("steamer", [(-60.0, 44.0 + 0.5 * k), (-32.0, 51.0 + 0.5 * k), (-6.0, 54.0 + 0.4 * k)], s[4] + 0.2 + 0.25 * k, s[4] + 5.2 + 0.25 * k,
         until=en[4] + 0.2) for k in range(4)],
    VH("warship", [(-59.0, 43.4), (-31.0, 50.4), (-5.5, 53.4)], s[4] + 0.3, s[4] + 5.2, until=en[4] + 0.2),
    *[VH("submarine", [(-3.4 - 0.6 * k, 47.7), (-18.0, 48.5 + 0.8 * k), (-30.0, 50.0 + 0.7 * k)], s[4] + 0.4 + 0.3 * k, s[4] + 2.6 + 0.3 * k,
         until=s[4] + 3.8) for k in range(3)],
    BM((-30.6, 51.6), s[4] + 2.8, 0.26), BM((-27.0, 52.6), s[4] + 3.2, 0.24),
    GL((-0.74, 52.0), s[4] + 2.9, en[4] + 0.2, 70, 60, 170),
    PP("turing", "ALAN TURING", "CODEBREAKER, BLETCHLEY PARK", s[4] + 2.9, en[4] + 0.2, x=780),
    # Stalingrad: the Sixth Army fights into the city; bombers overhead; Chuikov's men cross the Volga and hold the bank
    FR(ST0, ST1, s[5] + 0.2, en[5] + 0.2, s[5] + 0.8, s[5] + 5.0, sc=0.7),
    M_([(43.5, 48.75), (43.9, 48.78), (44.25, 48.76)], s[5] + 0.2, s[5] + 2.2, GRY, kind="wehrmacht", soldiers=6, ships=False, until=s[5] + 2.4),
    VH("bomber", [(43.6, 49.1), (44.1, 48.9), (44.5, 48.72)], s[5] + 0.5, s[5] + 1.7, until=s[5] + 2.3),
    BM((44.5, 48.73), s[5] + 1.7, 0.3), BM((44.46, 48.66), s[5] + 2.1, 0.26),
    M_([(44.72, 48.66), (44.62, 48.68), (44.55, 48.69)], s[5] + 2.9, s[5] + 4.6, RA, kind="redarmy41", soldiers=5, ships=False, until=en[5] + 0.2),
    BM((44.49, 48.76), s[5] + 4.4, 0.22),
    PP("paulus", "FRIEDRICH PAULUS", "COMMANDER, 6TH ARMY", s[5] + 0.6, en[5] + 0.2, x=300),
    PP("chuikov", "VASILY CHUIKOV", "COMMANDER, 62ND ARMY", s[5] + 2.6, en[5] + 0.2, x=780),
    # El Alamein: the barrage along the line, then the British armour breaks out and the Afrika Korps falls back west
    *[BM((28.75 + 0.06 * k, 30.95 - 0.1 * k), s[6] + 0.4 + 0.22 * k, 0.24) for k in range(5)],
    GL((28.9, 30.8), s[6] + 0.3, s[6] + 2.0, 120, 50, 140),
    VH("tank", [(29.3, 30.9), (27.3, 31.2), (25.2, 31.6), (24.0, 32.0)], s[6] + 1.8, s[6] + 5.6, until=en[6] + 0.2),
    VH("tank", [(29.2, 30.55), (27.5, 30.9), (25.6, 31.3)], s[6] + 2.0, s[6] + 5.6, until=en[6] + 0.2),
    M_([(28.6, 30.9), (26.5, 31.3), (24.6, 31.8), (22.5, 32.4)], s[6] + 2.0, s[6] + 5.6, DAK, kind="dak", soldiers=6, ships=False, until=en[6] + 0.2),
    PP("rommel", "ERWIN ROMMEL", "FIELD MARSHAL, AFRIKA KORPS", s[6] + 0.8, en[6] + 0.2, x=300),
    PP("montgomery", "BERNARD MONTGOMERY", "COMMANDER, EIGHTH ARMY", s[6] + 0.5, en[6] + 0.2, x=780),
    # Uranus: tank armies break the Romanian flanks north and south and meet near Kalach
    BM((42.8, 49.5), s[7] + 0.8, 0.28), BM((44.35, 48.15), s[7] + 1.1, 0.28),
    VH("tank", [(42.6, 49.7), (43.0, 49.25), (43.47, 48.78)], s[7] + 0.8, s[7] + 3.2, until=en[7] + 0.2),
    VH("tank", [(44.5, 48.05), (44.0, 48.3), (43.55, 48.68)], s[7] + 1.1, s[7] + 3.2, until=en[7] + 0.2),
    M_([(42.3, 49.75), (42.8, 49.3), (43.3, 48.95)], s[7] + 1.0, s[7] + 3.4, RA, kind="redarmy41", soldiers=6, ships=False, until=en[7] + 0.2),
    M_([(44.6, 47.9), (44.2, 48.2), (43.75, 48.5)], s[7] + 1.3, s[7] + 3.4, RA, kind="redarmy41", soldiers=5, ships=False, until=en[7] + 0.2),
    GL((44.0, 48.85), s[7] + 3.3, en[7] + 0.2, 230, 30, 110),
    PP("zhukov", "GEORGY ZHUKOV", "DEPUTY SUPREME COMMANDER", s[7] + 0.5, en[7] + 0.2, x=780),
    # the surrender; the Red Army rolls west to Rostov and Kharkov over the winter
    GL((44.5, 48.72), s[8] + 0.2, en[8] + 0.2, 120, 40, 110),
    M_([(43.2, 48.4), (41.3, 47.7), (39.8, 47.3)], s[8] + 1.6, s[8] + 4.8, RA, kind="redarmy41", soldiers=6, ships=False, until=en[8] + 0.2),
    M_([(39.6, 50.4), (37.9, 50.7), (36.4, 50.15)], s[8] + 1.8, s[8] + 5.0, RA, kind="redarmy41", soldiers=6, ships=False, until=en[8] + 0.2),
    PP("paulus", "FRIEDRICH PAULUS", "FIELD MARSHAL, 6TH ARMY", s[8] + 0.4, en[8] + 0.2, x=300),
    # the Warsaw Ghetto and the death camps: no effects, only quiet lights
    GL((21.0, 52.25), s[9] + 0.3, en[9] + 0.2, 60, 30, 90), GL((19.2, 50.03), s[9] + 3.4, en[9] + 0.2, 45, 20, 70),
    GL((22.05, 52.63), s[9] + 3.6, en[9] + 0.2, 45, 20, 70),
    # Black May: escort carriers with the convoys, long-range planes from Iceland and Northern Ireland, the U-boats are hunted
    VH("carrier", [(-52.0, 46.5), (-36.0, 51.0), (-24.0, 53.5)], s[10] + 0.3, s[10] + 4.6, until=en[10] + 0.2),
    *[VH("steamer", [(-54.0 - 0.6 * k, 47.5 + 0.5 * k), (-38.0, 52.0 + 0.5 * k), (-26.0, 54.5 + 0.4 * k)], s[10] + 0.3, s[10] + 4.6, until=en[10] + 0.2)
      for k in range(2)],
    VH("bomber", [(-21.9, 64.0), (-26.0, 58.5), (-30.0, 54.4)], s[10] + 0.6, s[10] + 2.4, until=s[10] + 3.4),
    VH("bomber", [(-6.5, 55.0), (-15.0, 54.0), (-24.0, 52.5)], s[10] + 0.8, s[10] + 2.6, until=s[10] + 3.6),
    *[VH("submarine", [(-36.0 + 3.0 * k, 49.5 + 0.6 * k), (-31.0 + 3.0 * k, 52.8 - 0.5 * k)], s[10] + 0.3, s[10] + 2.4, until=s[10] + 2.6 + 0.4 * k)
      for k in range(3)],
    *[BM((-31.0 + 3.0 * k, 52.8 - 0.5 * k), s[10] + 2.6 + 0.4 * k, 0.26) for k in range(3)],
    PP("donitz", "KARL DÖNITZ", "GRAND ADMIRAL, U-BOAT CHIEF", s[10] + 0.5, en[10] + 0.2, x=300),
    # Kursk: the two German pincers from Orel and Belgorod run into the minefields; the tank battle at Prokhorovka
    FR(K0, K1, s[11] + 0.2, en[11] + 0.2, s[11] + 0.8, s[11] + 3.2, sc=0.5),
    VH("tank", [(36.1, 52.85), (36.3, 52.4), (36.38, 52.15)], s[11] + 0.5, s[11] + 2.8, until=en[11] + 0.2),
    VH("tank", [(36.5, 50.45), (36.65, 50.8), (36.75, 51.0)], s[11] + 0.6, s[11] + 3.0, until=en[11] + 0.2),
    VH("tank", [(37.6, 51.35), (37.15, 51.15), (36.85, 51.05)], s[11] + 2.6, s[11] + 4.2, until=en[11] + 0.2),
    BM((36.38, 52.12), s[11] + 2.7, 0.26), BM((36.8, 51.03), s[11] + 3.4, 0.3), BM((36.75, 51.08), s[11] + 3.9, 0.26),
    PP("zhukov", "GEORGY ZHUKOV", "MARSHAL OF THE SOVIET UNION", s[11] + 1.0, en[11] + 0.2, x=780),
]
routes = [dict(pts=[(-164.0, 25.5), (-168.5, 29.5), (-172.5, 31.8)], t0=s[3] + 0.6, t1=s[3] + 2.4, until=en[3] + 0.2, color=(240, 205, 90)),
          dict(pts=[(-60.0, 44.0), (-32.0, 51.0), (-6.0, 54.0)], t0=s[4] + 0.2, t1=s[4] + 2.6, until=en[4] + 0.2, color=(240, 240, 240))]

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
    put(fr, glow_text("YEAR 1945", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("D-DAY, BERLIN, THE ATOMIC BOMBS", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=28, dur=DUR, base_a="/home/claude/shortgen/hd_1941.png", base_b="/home/claude/shortgen/hd_1943.png",
           extra_bases=dict(G="/home/claude/shortgen/hd_1942.png"),
           regions="/home/claude/shortgen/regions_ep28_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWP[0], SWP[1], "A", "G"), (SWB[0], SWB[1], "G", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (5.3, 0.2), (s[2] + 3.2, 0.25), (s[3] + 3.4, 0.3), (s[4] + 2.8, 0.2),
                                              (s[5] + 1.7, 0.2), (s[6] + 0.4, 0.25), (s[7] + 0.8, 0.25), (s[8] + 1.2, 0.2),
                                              (s[10] + 2.6, 0.2), (s[11] + 3.4, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
