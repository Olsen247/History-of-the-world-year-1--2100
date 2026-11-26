"""Episode 31 – Year 1960: decolonisation of Africa and Asia.
Dien Bien Phu (13 March - 7 May 1954, Giap's artillery on the hills, about 55 days), Geneva Accords split Vietnam at the 17th parallel
(21 July 1954); the FLN uprising in Algeria (1 November 1954, French forces later over 400,000); the Bandung Conference of 29 Asian and
African countries (18-24 April 1955); Sudan (1 Jan 1956), Morocco (2 Mar 1956), Tunisia (20 Mar 1956); Nasser nationalises the Suez
Canal (26 July 1956), Israel, Britain and France invade (29 Oct - 6 Nov), US and Soviet pressure forces them out; Ghana (6 March 1957,
Nkrumah: "Ghana, your beloved country, is free forever"), Malaya (31 Aug 1957); only Guinea votes No in de Gaulle's referendum
(28 Sept 1958; Toure's "poverty in freedom" speech 25 Aug 1958), independent 2 Oct 1958; Castro's rebels take Cuba (1 Jan 1959);
Macmillan's "wind of change" speech in Cape Town (3 Feb 1960); Sharpeville (21 March 1960, 69 killed); the 17 African states of 1960;
the Congo (independent 30 June 1960): the Force Publique mutiny (from 5 July), Katanga secedes (11 July), UN troops arrive (15 July)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1960)
import world_data_1953 as A_, world_data_1957 as M_D, world_data_1960 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep31/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
shots = [(17.0, 4.0, 2000), (40.0, 15.0, 2950), (103.05, 21.4, 340), (4.0, 34.0, 760), (107.6, -14.0, 2950), (16.0, 25.0, 1700),
         (-1.0, 7.6, 620), (-11.5, 10.2, 650), (-79.5, 22.3, 760), (24.0, -30.0, 820), (13.0, 4.0, 2000), (22.5, -6.5, 950),
         (20.0, 8.0, 2950)]
ZOOM = {2: (s[2] + 5.4, (105.2, 16.8, 760)), 5: (s[5] + 2.6, (32.6, 30.7, 500))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, *shots[0]), (3.0, 16.0, 4.5, 1900)]
for i in range(1, len(shots)):
    a, b = endshot[i - 1], shots[i]
    if i >= 2 and abs(a[0] - b[0]) > 50:     # long jumps: pull far out, then drop in
        keys += [(s[i] - 0.85, *a), (s[i] - 0.2, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 2950), (s[i] + 0.7, *b)]
        continue
    keys.append((s[i] - 0.85, *a))
    keys.append((s[i] + 0.35, *b))
keys.append((DUR, *shots[-1]))
for i, (t, sh) in ZOOM.items(): keys += [(t - 0.6, *shots[i]), (t + 0.6, *sh)]
keys = sorted(keys, key=lambda k: k[0])

SWM = (s[7] - 0.75, s[7] - 0.3)          # 1953 -> 1957 map while flying from Ghana to Guinea
SWB = (s[11] - 0.6, s[11] - 0.15)       # 1957 -> 1960 map while flying from West Africa to the Congo
UM, UB = SWM[1] + 0.1, SWB[1] + 0.1
G = lambda key, a, b, until: dict(key=key, t0=a, t1=b, until=until)
Y60 = ["cameroon_gain", "togo_gain", "madagascar_gain", "congo_gain", "somalia_gain", "dahomey_gain", "niger_gain", "volta_gain",
       "ivory_gain", "chad_gain", "car_gain", "brazza_gain", "gabon_gain", "senegal_gain", "mali_gain", "nigeria_gain", "mauritania_gain"]
reveals = [G("nv_gain", s[2] + 5.6, s[2] + 7.4, UM), G("laos_gain", s[2] + 6.0, s[2] + 7.6, UM), G("camb_gain", s[2] + 6.2, s[2] + 7.8, UM),
           G("sv_gain", s[2] + 6.4, s[2] + 8.0, UM),
           G("sudan_gain", s[5] + 0.3, s[5] + 2.2, UM), G("morocco_gain", s[5] + 0.5, s[5] + 2.0, UM), G("tunisia_gain", s[5] + 0.7, s[5] + 2.0, UM),
           G("ghana_gain", s[6] + 0.6, s[6] + 2.8, UM), G("malaya_gain", s[6] + 0.6, s[6] + 2.8, UM),
           G("guinea_gain", s[7] + 1.2, s[7] + 3.4, UB)]
reveals += [G(k, s[10] + 0.3 + 0.3 * j, s[10] + 1.6 + 0.3 * j, UB) for j, k in enumerate(Y60)]
reveals += [G("cyprus_gain", s[10] + 4.0, s[10] + 5.0, UB), G("katanga_gain", s[11] + 1.6, s[11] + 3.4, DUR)]

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); FRC = (130, 160, 240); BRC = (240, 160, 190)
labels = [
    # Dien Bien Phu, then the split of Indochina
    ev("DIEN BIEN PHU", (102.9, 20.25), s[2] + 0.4, s[2] + 5.2), lb("HANOI", (105.85, 21.2), s[2] + 0.8, s[2] + 5.0, WT, kind="small"),
    lb("NORTH VIETNAM", (105.0, 20.6), s[2] + 6.6, en[2] + 0.2, (240, 160, 110)), lb("SOUTH VIETNAM", (106.2, 10.0), s[2] + 6.8, en[2] + 0.2, (240, 215, 120)),
    lb("LAOS", (102.8, 19.2), s[2] + 6.8, en[2] + 0.2, CYN, kind="small"), lb("CAMBODIA", (104.6, 12.9), s[2] + 7.0, en[2] + 0.2, (150, 210, 150), kind="small"),
    lb("17TH PARALLEL", (108.3, 17.15), s[2] + 6.6, en[2] + 0.2, WT, kind="small"),
    # Algeria
    lb("ALGERIA", (2.5, 30.0), s[3] + 0.4, en[3] + 0.2, FRC, kind="emp"), ev("AURES MOUNTAINS", (7.6, 33.6), s[3] + 0.6, en[3] + 0.2, RRED),
    lb("FRANCE", (2.5, 46.0), s[3] + 2.6, en[3] + 0.2, FRC, kind="small"),
    # Bandung
    ev("BANDUNG", (107.6, -4.0), s[4] + 0.6, en[4] + 0.2), lb("INDIA", (78.5, 22.0), s[4] + 1.0, en[4] + 0.2, (240, 170, 80), kind="small"),
    lb("CHINA", (104.0, 33.0), s[4] + 1.0, en[4] + 0.2, (240, 110, 100), kind="small"), lb("EGYPT", (31.0, 26.5), s[4] + 1.0, en[4] + 0.2, (240, 180, 190), kind="small"),
    # North Africa 1956 and Suez
    lb("SUDAN", (30.0, 15.5), s[5] + 0.8, s[5] + 2.8, (215, 160, 110), kind="small"), lb("MOROCCO", (-6.5, 32.0), s[5] + 0.8, s[5] + 2.8, (235, 130, 120), kind="small"),
    lb("TUNISIA", (9.3, 34.0), s[5] + 0.9, s[5] + 2.8, (240, 150, 140), kind="small"),
    ev("SUEZ CANAL", (30.2, 30.45), s[5] + 3.0, en[5] + 0.2),
    lb("PORT SAID", (31.4, 31.45), s[5] + 3.6, en[5] + 0.2, WT, kind="small"), lb("SINAI", (34.0, 29.0), s[5] + 3.8, en[5] + 0.2, WT, kind="small"),
    # Ghana
    lb("GHANA", (-1.2, 8.0), s[6] + 2.2, en[6] + 0.2, (245, 210, 90), kind="emp"), ev("ACCRA", (-0.2, 5.15), s[6] + 0.5, en[6] + 0.2),
    # Guinea
    lb("GUINEA", (-10.6, 10.6), s[7] + 2.6, en[7] + 0.2, (240, 120, 120), kind="emp"), ev("CONAKRY", (-13.7, 9.15), s[7] + 0.6, en[7] + 0.2),
    lb("FRENCH WEST AFRICA", (-6.0, 14.6), s[7] + 0.6, en[7] + 0.2, FRC, kind="small"),
    # Cuba
    lb("CUBA", (-78.6, 21.2), s[8] + 0.4, en[8] + 0.2, (160, 190, 235), kind="emp"), ev("HAVANA", (-82.37, 23.5), s[8] + 3.6, en[8] + 0.2),
    lb("SIERRA MAESTRA", (-76.6, 19.3), s[8] + 0.6, en[8] + 0.2, WT, kind="small"), lb("FLORIDA", (-81.6, 27.6), s[8] + 0.8, en[8] + 0.2, WT, kind="small"),
    # wind of change, Sharpeville
    lb("SOUTH AFRICA", (23.5, -30.5), s[9] + 0.4, en[9] + 0.2, BRC, kind="emp"), ev("CAPE TOWN", (18.42, -34.4), s[9] + 0.5, en[9] + 0.2),
    ev("SHARPEVILLE", (27.87, -26.25), s[9] + 4.2, en[9] + 0.2, RRED),
    # 1960
    lb("NIGERIA", (8.0, 9.6), s[10] + 5.0, en[10] + 0.2, (140, 210, 140), kind="small"), lb("CONGO", (23.5, -2.5), s[10] + 1.6, en[10] + 0.2, CYN, kind="small"),
    lb("MALI", (-2.5, 18.0), s[10] + 4.8, en[10] + 0.2, (240, 215, 150), kind="small"), lb("CHAD", (18.5, 15.5), s[10] + 3.6, en[10] + 0.2, (150, 175, 240), kind="small"),
    lb("SOMALIA", (46.5, 6.5), s[10] + 2.0, en[10] + 0.2, (160, 215, 240), kind="small"), lb("MADAGASCAR", (46.8, -19.5), s[10] + 1.4, en[10] + 0.2, (240, 160, 175), kind="small"),
    lb("SENEGAL", (-14.6, 14.9), s[10] + 4.6, en[10] + 0.2, (140, 190, 240), kind="small"),
    # the Congo crisis
    lb("CONGO", (21.5, -1.8), s[11] + 0.3, en[11] + 0.2, CYN, kind="emp"), ev("LEOPOLDVILLE", (15.3, -3.8), s[11] + 0.4, en[11] + 0.2),
    ev("KATANGA", (26.5, -9.6), s[11] + 2.4, en[11] + 0.2, (245, 170, 80)), lb("ELISABETHVILLE", (27.5, -12.0), s[11] + 2.6, en[11] + 0.2, WT, kind="small"),
]
labels += WP.labels(A_, 1955, s[1] + 0.8, SWM[0])
labels += WP.labels(M_D, 1958, SWM[1], SWB[0])
labels += WP.labels(B_, 1960, SWB[1], s[12])

ticker = [(0, 1960), (s[1], 1960), (s[1] + 1.3, 1953)]
for i, y in ((2, 1954), (4, 1955), (5, 1956), (6, 1957), (7, 1958), (8, 1959), (9, 1960)):
    ticker += [(s[i], ticker[-1][1]), (s[i] + 0.5, y)]
ticker.append((DUR, 1960))
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1960", l2="THE YEAR OF AFRICA", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1953", GOLD), hd(2, "MARCH 1954", "DIEN BIEN PHU"),
            hd(3, "1 NOVEMBER 1954", "ALGERIA RISES"), hd(4, "APRIL 1955", "BANDUNG", GOLD),
            hd(5, "JULY 1956", "THE SUEZ CRISIS", CYN), hd(6, "6 MARCH 1957", "GHANA IS FREE", GOLD),
            hd(7, "SEPTEMBER 1958", "GUINEA SAYS NO"), hd(8, "1 JANUARY 1959", "CASTRO TAKES CUBA"),
            hd(9, "1960", "WIND OF CHANGE", CYN), hd(10, "1960", "17 NEW NATIONS", GOLD), hd(11, "JULY 1960", "CONGO IN CRISIS")]

MR = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
VM = (200, 80, 60); FRA = (70, 100, 200); FLN = (60, 150, 80); BRI = (200, 90, 120); ISR = (110, 150, 220); CUB = (90, 110, 60); UNB = (90, 160, 230)
DBP = (103.02, 21.39)
CAP60 = [(11.5, 3.87), (1.22, 6.13), (47.52, -18.9), (15.3, -4.32), (45.34, 2.04), (2.63, 6.5), (2.11, 13.51), (-1.52, 12.37), (-4.02, 5.33),
         (15.04, 12.11), (18.56, 4.39), (15.24, -4.26), (9.45, 0.39), (-17.44, 14.69), (-8.0, 12.64), (3.39, 6.45), (-15.98, 18.08)]
BANDUNG = (107.6, -6.9)
fx = [
    # hook: the capitals of the 17 new states light up one after another
    *[dict(type="cities", cities=[(x, y, 1.2)], t0=0.4 + 0.22 * k, t1=0.9 + 0.22 * k, until=en[0] + 0.3, color=(255, 214, 120)) for k, (x, y) in enumerate(CAP60)],
    # Dien Bien Phu: the Viet Minh close in from the hills, guns pound the valley, French supply planes fly in from Hanoi
    MR([(103.05, 22.05), (103.03, 21.62)], s[2] + 0.4, s[2] + 3.2, VM, kind="vietminh", soldiers=5, ships=False, until=s[2] + 5.2),
    MR([(103.62, 21.55), (103.2, 21.42)], s[2] + 0.6, s[2] + 3.4, VM, kind="vietminh", soldiers=5, ships=False, until=s[2] + 5.2),
    MR([(103.2, 20.85), (103.06, 21.2)], s[2] + 0.8, s[2] + 3.6, VM, kind="vietminh", soldiers=5, ships=False, until=s[2] + 5.2),
    *[BM((DBP[0] + dx, DBP[1] + dy), s[2] + 1.6 + 0.55 * k, 0.26) for k, (dx, dy) in enumerate([(0.0, 0.03), (0.04, -0.05), (-0.04, 0.0), (0.02, -0.02), (-0.02, 0.04)])],
    VH("plane", [(105.8, 21.03), (104.4, 21.3), DBP], s[2] + 0.6, s[2] + 2.4, until=s[2] + 2.8),
    GL(DBP, s[2] + 0.4, s[2] + 5.2, 60, 60, 170),
    PP("giap", "VO NGUYEN GIAP", "VIET MINH COMMANDER", s[2] + 0.4, s[2] + 5.4, x=300),
    # Algeria: the FLN strikes at many places on one night; France ships in troops
    *[GL(p, s[3] + 0.5 + 0.25 * k, en[3] + 0.2, 40, 70, 170) for k, p in enumerate([(6.6, 35.4), (3.06, 36.75), (7.0, 36.4), (5.6, 36.2), (0.6, 35.7), (2.9, 35.4)])],
    MR([(6.6, 35.3), (6.2, 35.9), (6.6, 36.35)], s[3] + 0.6, s[3] + 3.0, FLN, kind="fln", soldiers=4, ships=False, until=en[3] + 0.2),
    MR([(4.6, 35.4), (5.0, 36.0), (5.4, 36.4)], s[3] + 0.8, s[3] + 3.2, FLN, kind="fln", soldiers=4, ships=False, until=en[3] + 0.2),
    MR([(5.37, 43.3), (4.4, 40.0), (3.06, 36.8)], s[3] + 2.8, en[3] - 0.2, FRA, kind="para", soldiers=5, until=en[3] + 0.2),
    # Bandung: delegations converge on Java
    dict(type="cities", cities=[(31.2, 30.0, 1.0), (77.2, 28.6, 1.0), (116.4, 39.9, 1.0), (-0.2, 5.6, 0.9), (96.2, 16.8, 0.9), (139.7, 35.7, 0.9),
                                (67.0, 24.9, 0.9), (38.7, 9.0, 0.9), (BANDUNG[0], BANDUNG[1], 1.5)], t0=s[4] + 0.4, t1=s[4] + 1.4, until=en[4] + 0.2),
    GL(BANDUNG, s[4] + 2.6, en[4] + 0.2, 140, 60, 170),
    PP("sukarno", "SUKARNO", "PRESIDENT OF INDONESIA", s[4] + 0.4, en[4] + 0.2, x=780),
    PP("nehru", "JAWAHARLAL NEHRU", "PRIME MINISTER OF INDIA", s[4] + 0.4, en[4] + 0.2, x=300),
    # Suez: Nasser takes the canal; Israeli tanks cross Sinai, the Anglo-French fleet and paratroopers hit Port Said
    GL((32.55, 30.6), s[5] + 2.8, en[5] + 0.2, 70, 70, 190),
    VH("tank", [(34.4, 31.0), (33.6, 30.6), (32.9, 30.35)], s[5] + 3.8, s[5] + 5.6, until=en[5] + 0.2),
    VH("tank", [(34.5, 30.2), (33.7, 30.1), (32.9, 30.0)], s[5] + 3.9, s[5] + 5.7, until=en[5] + 0.2),
    VH("carrier", [(33.3, 34.2), (32.6, 32.0)], s[5] + 3.6, s[5] + 5.4, until=en[5] + 0.2),
    VH("warship", [(32.6, 34.4), (32.35, 31.6)], s[5] + 3.7, s[5] + 5.6, until=en[5] + 0.2),
    VH("plane", [(33.4, 34.9), (32.3, 31.25)], s[5] + 3.4, s[5] + 4.8, until=s[5] + 5.2),
    BM((32.3, 31.26), s[5] + 5.0, 0.28), BM((32.55, 30.4), s[5] + 5.4, 0.24),
    PP("nasser", "GAMAL ABDEL NASSER", "PRESIDENT OF EGYPT", s[5] + 0.4, en[5] + 0.2, x=300),
    PP("eisenhower53", "DWIGHT D. EISENHOWER", "PRESIDENT OF THE UNITED STATES", s[5] + 5.4, en[5] + 0.2, x=780),
    # Ghana: celebration lights in Accra
    dict(type="cities", cities=[(-0.2, 5.6, 1.5), (-1.62, 6.69, 0.9), (-0.85, 9.4, 0.8)], t0=s[6] + 0.4, t1=s[6] + 1.6, until=en[6] + 0.2),
    GL((-0.2, 5.6), s[6] + 2.4, en[6] + 0.2, 90, 60, 170),
    PP("nkrumah", "KWAME NKRUMAH", "PRIME MINISTER OF GHANA", s[6] + 0.4, en[6] + 0.2, x=780),
    # Guinea says No
    GL((-13.7, 9.5), s[7] + 0.6, en[7] + 0.2, 80, 60, 170),
    PP("degaulle", "CHARLES DE GAULLE", "LEADER OF FRANCE", s[7] + 0.4, s[7] + 4.0, x=780),
    PP("toure", "SEKOU TOURE", "LEADER OF GUINEA", s[7] + 0.4, en[7] + 0.2, x=300),
    # Cuba: from the Sierra Maestra to Havana
    MR([(-76.9, 20.05), (-77.9, 21.4), (-79.95, 22.4), (-82.2, 23.05)], s[8] + 0.4, s[8] + 4.6, CUB, kind="barbudo", soldiers=6, ships=False, until=en[8] + 0.2),
    MR([(-75.8, 20.1), (-77.2, 20.4), (-78.4, 21.6)], s[8] + 0.6, s[8] + 3.8, CUB, kind="barbudo", soldiers=4, ships=False, until=en[8] + 0.2),
    GL((-82.37, 23.13), s[8] + 3.8, en[8] + 0.2, 70, 60, 170),
    PP("castro", "FIDEL CASTRO", "CUBAN REVOLUTIONARY LEADER", s[8] + 0.4, en[8] + 0.2, x=780),
    # wind of change in Cape Town; Sharpeville
    GL((18.42, -33.93), s[9] + 0.4, s[9] + 4.2, 90, 60, 160),
    PP("macmillan", "HAROLD MACMILLAN", "BRITISH PRIME MINISTER", s[9] + 0.4, s[9] + 4.4, x=780),
    GL((27.87, -26.67), s[9] + 4.2, en[9] + 0.2, 60, 90, 200),
    # 1960: capitals light up as each state is born
    *[dict(type="cities", cities=[(x, y, 1.0)], t0=s[10] + 0.4 + 0.3 * k, t1=s[10] + 1.0 + 0.3 * k, until=en[10] + 0.2) for k, (x, y) in enumerate(CAP60)],
    # Congo: the mutiny, Katanga breaks away, UN planes and blue helmets arrive
    GL((15.3, -4.32), s[11] + 0.4, en[11] + 0.2, 70, 70, 190), GL((14.9, -5.25), s[11] + 0.5, s[11] + 3.0, 50, 70, 190),
    GL((27.48, -11.66), s[11] + 1.8, en[11] + 0.2, 70, 60, 170),
    *[VH("plane", [(15.0 + 2 * k, 6.0), (15.3, -4.32)], s[11] + 3.0 + 0.4 * k, s[11] + 4.6 + 0.4 * k, until=s[11] + 5.0 + 0.4 * k) for k in range(2)],
    MR([(15.4, -4.4), (17.5, -4.6), (20.5, -5.5)], s[11] + 4.0, en[11] - 0.1, UNB, kind="unblue", soldiers=5, ships=False, until=en[11] + 0.2),
    PP("lumumba", "PATRICE LUMUMBA", "PRIME MINISTER OF THE CONGO", s[11] + 0.4, en[11] + 0.2, x=300),
]
routes = [dict(pts=[p, BANDUNG], t0=s[4] + 0.8 + 0.15 * k, t1=s[4] + 2.8 + 0.15 * k, until=en[4] + 0.2, color=(240, 205, 90))
          for k, p in enumerate([(31.2, 30.0), (77.2, 28.6), (116.4, 39.9), (-0.2, 5.6), (96.2, 16.8), (139.7, 35.7), (67.0, 24.9), (38.7, 9.0)])]

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
    put(fr, glow_text("YEAR 1969", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE MOON LANDING", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=31, dur=DUR, base_a="/home/claude/shortgen/hd_1953.png", base_b="/home/claude/shortgen/hd_1960.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1957.png", K="/home/claude/shortgen/hd_1960k.png"),
           regions="/home/claude/shortgen/regions_ep31_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWM[0], SWM[1], "A", "M"), (SWB[0], SWB[1], "M", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.6, 0.2), (s[3] + 0.5, 0.2), (s[4] + 0.6, 0.2), (s[5] + 5.0, 0.25),
                                              (s[6] + 0.6, 0.25), (s[7] + 1.2, 0.2), (s[8] + 3.8, 0.2), (s[9] + 4.2, 0.2), (s[10] + 0.3, 0.25),
                                              (s[11] + 1.6, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
