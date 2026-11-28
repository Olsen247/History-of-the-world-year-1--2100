"""Episode 33 – Year 1975: the Vietnam War ends (rewinds to 1968, because the episode starts with Tet).
Tet Offensive (night of 30-31 Jan 1968): some 80,000-85,000 VC/PAVN troops hit over 100 cities and towns, incl. 36 of 44 provincial
capitals, and the US embassy compound in Saigon; Battle of Hue (31 Jan - 2/3 Mar 1968), US Marines + ARVN (Citadel/palace by ARVN);
Johnson's 31 Mar 1968 speech. Ho Chi Minh Trail through Laos (and Cambodia); about 2 million tons of bombs fell on Laos 1964-73.
About 7,000 UH-1 Hueys served in Vietnam; Cu Chi tunnels ~250 km. Nixon's first withdrawal (June 1969, 25,000 men);
My Lai (16 Mar 1968, 347-504 villagers killed) made public by Seymour Hersh on 12-13 Nov 1969.
Cambodian incursion (29 Apr - 1 May 1970), Kent State (4 May 1970, 4 students killed by the Ohio National Guard).
Paris Peace Accords (27 Jan 1973); the last US combat troops leave on 29 Mar 1973.
1975 offensive: Ban Me Thuot attacked 10 Mar, Hue falls 25-26 Mar, Da Nang 29-30 Mar; Khmer Rouge take Phnom Penh 17 Apr 1975
(their regime 1975-79: est. 1.5-2 million dead); Operation Frequent Wind 29-30 Apr (about 7,000 lifted out by helicopter, last
helicopter off the embassy roof ~07:53 on 30 Apr); tanks 843/390 at the Independence Palace gate ~11:30 on 30 Apr 1975."""
import sys, math
from PIL import Image, ImageDraw
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1970)
import world_data_1969 as A_, world_data_1975a as M_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep33/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
SAIGON = (106.70, 10.78); HUE = (107.58, 16.46); DANANG = (108.21, 16.05); BMT = (108.05, 12.67); PNH = (104.92, 11.56)
CUCHI = (106.50, 11.05); KENT = (-81.34, 41.15); PARIS = (2.35, 48.86); PALACE = (106.695, 10.777); FLEET = (107.75, 10.05)
MYLAI = (108.87, 15.18); HANOI = (105.85, 21.03)
shots = [(107.05, 10.6, 210), (100.0, 20.0, 2950), (106.9, 13.4, 330), (107.5, 16.4, 180), (106.2, 15.4, 360),
         (106.6, 11.0, 200), (108.0, 13.6, 330), (106.0, 11.25, 230), (2.35, 48.6, 300), (107.3, 14.0, 320),
         (104.92, 11.62, 200), (107.05, 10.65, 200), (100.0, 18.0, 2950)]
ZOOM = {7: (s[7] + 3.4, (-81.6, 40.9, 230)), 8: (s[8] + 3.7, (107.2, 11.2, 260))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, *shots[0]), (s[0] + 4.0, 107.1, 10.55, 195)]
for i in range(1, len(shots)):
    a, b = endshot[i - 1], shots[i]
    if i >= 2 and abs(a[0] - b[0]) > 50:     # long jumps: pull far out, then drop in
        keys += [(s[i] - 0.85, *a), (s[i] - 0.2, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 2950), (s[i] + 0.7, *b)]
        continue
    keys.append((s[i] - 0.85, *a))
    keys.append((s[i] + 0.35, *b))
keys.append((DUR, *shots[-1]))
# line 7: Cambodia -> Ohio (pull out over the Pacific/Atlantic); line 8: Paris -> Saigon
keys += [(s[7] + 2.6, *shots[7]), (s[7] + 3.0, 20.0, 35.0, 2950), (s[7] + 3.4, *ZOOM[7][1])]
keys += [(s[8] + 3.0, *shots[8]), (s[8] + 3.4, 55.0, 30.0, 2950), (s[8] + 4.0, *ZOOM[8][1])]
keys = sorted(keys, key=lambda k: k[0])

SWM = (s[7] + 2.85, s[7] + 3.15)          # 1969 -> 1975a map while far out between Cambodia and Ohio
UG = DUR

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250)
NVC = (240, 160, 110); SVC = (240, 215, 120)
labels = [
    # hook
    ev("SAIGON", (SAIGON[0] - 0.1, SAIGON[1] + 0.25), 0.3, en[0] + 0.2), ev("US FLEET", (FLEET[0] + 0.05, FLEET[1] - 0.2), 1.6, en[0] + 0.2, CYN),
    # Tet
    lb("SOUTH VIETNAM", (107.9, 14.3), s[2] + 0.4, en[2] + 0.2, SVC, kind="emp"), lb("NORTH VIETNAM", (105.6, 18.4), s[2] + 0.4, en[2] + 0.2, NVC),
    ev("SAIGON", (SAIGON[0] + 0.2, SAIGON[1] - 0.75), s[2] + 0.5, en[2] + 0.2), ev("HUE", (HUE[0] + 0.9, HUE[1] + 0.2), s[2] + 2.0, en[2] + 0.2),
    # Hue
    ev("HUE", (HUE[0] + 0.05, HUE[1] + 0.5), s[3] + 0.3, en[3] + 0.2), 
    # trail
    ev("HO CHI MINH TRAIL", (105.4, 15.6), s[4] + 0.6, en[4] + 0.2), lb("LAOS", (104.6, 17.2), s[4] + 0.4, en[4] + 0.2, WT),
    lb("NORTH VIETNAM", (105.0, 19.3), s[4] + 0.4, en[4] + 0.2, NVC, kind="small"), lb("SOUTH VIETNAM", (108.0, 14.0), s[4] + 0.4, en[4] + 0.2, SVC, kind="small"),
    lb("CAMBODIA", (105.2, 13.1), s[4] + 0.4, en[4] + 0.2, WT, kind="small"),
    # helicopters, Cu Chi
    ev("CU CHI TUNNELS", (CUCHI[0] - 0.3, CUCHI[1] + 0.4), s[5] + 3.6, en[5] + 0.2, RRED), lb("SAIGON", (SAIGON[0] + 0.05, SAIGON[1] - 0.12), s[5] + 0.3, en[5] + 0.2, WT, kind="small"),
    # Nixon, My Lai
    ev("MY LAI", (MYLAI[0], MYLAI[1] + 0.3), s[6] + 3.0, en[6] + 0.2, RRED), lb("SOUTH VIETNAM", (107.3, 13.0), s[6] + 0.4, en[6] + 0.2, SVC),
    # Cambodia, Kent State
    lb("CAMBODIA", (104.9, 12.0), s[7] + 0.3, s[7] + 2.7, WT), ev("PARROT'S BEAK", (105.85, 10.55), s[7] + 0.6, s[7] + 2.7),
    ev("KENT STATE", (KENT[0], KENT[1] - 0.55), s[7] + 3.6, en[7] + 0.2, RRED), lb("OHIO", (-82.9, 40.0), s[7] + 3.6, en[7] + 0.2, WT, kind="small"),
    # Paris; troops leave
    ev("PARIS", (PARIS[0], PARIS[1] - 0.6), s[8] + 0.3, s[8] + 3.0), ev("SAIGON", (SAIGON[0] - 0.2, SAIGON[1] - 0.45), s[8] + 4.1, en[8] + 0.2),
    # 1975 offensive
    ev("BAN ME THUOT", (BMT[0] + 0.4, BMT[1] - 0.75), s[9] + 0.8, en[9] + 0.2), ev("HUE", (HUE[0] + 1.0, HUE[1] + 0.45), s[9] + 2.6, en[9] + 0.2),
    ev("DA NANG", (DANANG[0] + 0.95, DANANG[1] - 0.3), s[9] + 3.4, en[9] + 0.2), lb("SAIGON", (SAIGON[0], SAIGON[1] - 0.35), s[9] + 0.5, en[9] + 0.2, WT, kind="small"),
    # Phnom Penh
    ev("PHNOM PENH", (PNH[0], PNH[1] - 0.9), s[10] + 0.3, en[10] + 0.2, RRED), lb("CAMBODIA", (104.0, 12.4), s[10] + 0.4, en[10] + 0.2, WT),
    # Saigon falls
    ev("SAIGON", (SAIGON[0] - 0.25, SAIGON[1] + 0.35), s[11] + 0.3, en[11] + 0.2), lb("US FLEET", (FLEET[0] + 0.1, FLEET[1] - 0.18), s[11] + 1.0, en[11] + 0.2, CYN, kind="small"),
    lb("PRESIDENTIAL PALACE", (PALACE[0] - 0.05, PALACE[1] - 0.22), s[11] + 3.6, en[11] + 0.2, RRED, kind="small"),
]
labels += WP.labels(A_, 1970, s[1] + 0.8, SWM[0])
labels += WP.labels(M_, 1975, SWM[1], s[12])

ticker = [(0, 1975), (s[1], 1975), (s[1] + 1.3, 1968)]
for i, y in ((4, 1969), (7, 1970), (8, 1973), (9, 1975)):
    ticker += [(s[i], ticker[-1][1]), (s[i] + 0.5, y)]
ticker.append((DUR, 1975))
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1975", l2="THE FALL OF SAIGON", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1968", GOLD), hd(2, "JANUARY 1968", "THE TET OFFENSIVE"),
            hd(3, "FEBRUARY 1968", "THE BATTLE OF HUE"), hd(4, "1969", "THE HO CHI MINH TRAIL", GOLD),
            hd(5, "1969", "THE HELICOPTER WAR", CYN), hd(6, "1969", "MY LAI REVEALED"),
            hd(7, "MAY 1970", "INTO CAMBODIA", t1=s[7] + 3.0),
            dict(t0=s[7] + 3.4, t1=en[7] + 0.2, l1="4 MAY 1970", l2="KENT STATE", c2=RRED),
            hd(8, "JANUARY 1973", "PEACE IN PARIS", GOLD), hd(9, "MARCH 1975", "THE FINAL OFFENSIVE"),
            hd(10, "17 APRIL 1975", "THE KHMER ROUGE"), hd(11, "30 APRIL 1975", "SAIGON FALLS", GOLD)]

MR = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.3: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
USA = (70, 110, 200); NVA = (200, 60, 50); VC = (170, 40, 40); KR = (120, 30, 30)
HELI = lambda path, a, b, **kw: VH("helicopter", path, a, b, **kw)
TET = [(106.70, 10.78), (107.58, 16.46), (108.21, 16.05), (109.19, 13.78), (108.05, 12.67), (105.78, 10.03), (108.43, 11.94),
       (107.08, 10.35), (106.37, 10.36), (109.2, 12.25), (108.0, 14.0), (106.0, 9.6)]
fx = [
    # hook: helicopters lift off from Saigon and fly out to the fleet
    *[HELI([(SAIGON[0] + dx, SAIGON[1] + dy), (107.2 + dx, 10.4 + dy), (FLEET[0] + dx, FLEET[1] + dy)], 0.4 + 0.5 * k, 3.6 + 0.5 * k, until=en[0] + 0.2)
      for k, (dx, dy) in enumerate([(0.0, 0.0), (-0.05, 0.08), (0.04, -0.07)])],
    *[VH("warship", [(FLEET[0] + dx, FLEET[1] + dy), (FLEET[0] + dx + 0.12, FLEET[1] + dy - 0.05)], 0.3, 5.0, until=en[0] + 0.2, scale=0.8)
      for dx, dy in ((0.15, -0.05), (-0.1, -0.15))],
    # Tet: VC and NVA strike towns all over the South at once; the US embassy in Saigon
    *[GL(p, s[2] + 0.8 + 0.25 * k, en[2] + 0.2, 30, 70, 190) for k, p in enumerate(TET)],
    *[BM(p, s[2] + 1.0 + 0.25 * k, 0.2) for k, p in enumerate(TET[:8])],
    MR([(106.1, 11.5), (106.4, 11.1), (106.65, 10.82)], s[2] + 1.0, s[2] + 4.0, VC, kind="vietcong", soldiers=3, ships=False, until=en[2] + 0.2),
    MR([(106.8, 17.1), (107.2, 16.8), (107.55, 16.5)], s[2] + 1.6, s[2] + 4.4, NVA, kind="nva", soldiers=3, ships=False, until=en[2] + 0.2),
    MR([(107.3, 12.4), (107.7, 12.6), (108.0, 12.67)], s[2] + 2.0, s[2] + 4.8, VC, kind="vietcong", soldiers=3, ships=False, until=en[2] + 0.2),
    BM(SAIGON, s[2] + 5.6, 0.3),
    PP("hochiminh", "HO CHI MINH", "PRESIDENT OF NORTH VIETNAM", s[2] + 0.4, en[2] + 0.2, x=780),
    # Hue: US Marines (south bank) and South Vietnamese troops fight back into the Citadel
    MR([(107.64, 16.36), (107.61, 16.42), (107.585, 16.455)], s[3] + 0.5, s[3] + 3.6, USA, kind="usmc65", soldiers=4, ships=False, until=en[3] + 0.2),
    MR([(107.50, 16.52), (107.54, 16.49), (107.565, 16.475)], s[3] + 0.7, s[3] + 3.8, (230, 190, 70), kind="gi69", soldiers=3, ships=False, until=en[3] + 0.2),
    BM((107.575, 16.47), s[3] + 2.4, 0.22), BM((107.56, 16.475), s[3] + 3.4, 0.2), GL(HUE, s[3] + 0.3, en[3] + 0.2, 60, 60, 160),
    PP("johnson", "LYNDON B. JOHNSON", "PRESIDENT OF THE UNITED STATES", s[3] + 3.0, en[3] + 0.2, x=780),
    # the trail: trucks roll south through Laos while bombers strike it
    *[VH("truck", [(105.6, 18.7), (105.8, 17.7), (106.2, 16.6), (106.8, 15.2), (107.1, 13.8), (106.9, 12.5)], s[4] + 0.4 + 0.7 * k, en[4] - 0.3 + 0.1 * k,
         until=en[4] + 0.2, scale=0.8) for k in range(3)],
    VH("bomber", [(110.0, 17.0), (107.5, 16.4), (105.5, 15.8)], s[4] + 2.0, s[4] + 4.4, until=s[4] + 5.0, scale=0.8),
    BM((106.2, 16.6), s[4] + 3.2, 0.22), BM((106.6, 15.6), s[4] + 3.6, 0.22), BM((106.0, 17.2), s[4] + 4.0, 0.2),
    # helicopters: Hueys fly troops from Saigon into the jungle; the enemy is in tunnels at Cu Chi
    *[HELI([(SAIGON[0] + 0.1 * k, SAIGON[1] + 0.05 * k), (106.6 + 0.08 * k, 11.15 + 0.06 * k), (106.35 + 0.1 * k, 11.35 + 0.05 * k)],
           s[5] + 0.4 + 0.3 * k, s[5] + 2.8 + 0.3 * k, until=en[5] + 0.2) for k in range(3)],
    GL(CUCHI, s[5] + 3.4, en[5] + 0.2, 40, 70, 190),
    MR([(106.45, 11.12), (106.48, 11.08), (106.5, 11.05)], s[5] + 3.6, en[5] - 0.2, VC, kind="vietcong", soldiers=2, ships=False, until=en[5] + 0.2),
    # Nixon brings troops home (airliners leave); My Lai
    *[VH("jet", [SAIGON, (108.5, 11.8), (111.5, 13.6)], s[6] + 0.4 + 0.5 * k, s[6] + 3.0 + 0.5 * k, until=s[6] + 3.8 + 0.5 * k) for k in range(2)],
    GL(MYLAI, s[6] + 3.0, en[6] + 0.2, 35, 60, 170),
    PP("nixon", "RICHARD NIXON", "PRESIDENT OF THE UNITED STATES", s[6] + 0.4, en[6] + 0.2, x=780),
    # Cambodia 1970
    MR([(106.3, 11.0), (106.05, 11.15), (105.8, 11.25)], s[7] + 0.4, s[7] + 2.6, USA, kind="gi69", soldiers=4, ships=False, until=s[7] + 2.9),
    *[HELI([(106.6 + 0.1 * k, 10.95), (106.2, 11.2 + 0.05 * k), (105.9, 11.3 + 0.05 * k)], s[7] + 0.5 + 0.3 * k, s[7] + 2.4 + 0.3 * k, until=s[7] + 2.9) for k in range(2)],
    GL(KENT, s[7] + 3.6, en[7] + 0.2, 45, 70, 190),
    # Paris 1973; the last combat troops fly out of Saigon
    GL(PARIS, s[8] + 0.3, s[8] + 3.1, 50, 70, 190),
    PP("kissinger", "HENRY KISSINGER", "US NEGOTIATOR", s[8] + 0.4, s[8] + 3.3, x=780),
    PP("leductho", "LE DUC THO", "NORTH VIETNAMESE NEGOTIATOR", s[8] + 0.6, s[8] + 3.3, x=300),
    *[VH("jet", [SAIGON, (108.0, 11.6), (110.5, 13.0)], s[8] + 4.2 + 0.6 * k, s[8] + 6.4 + 0.6 * k, until=en[8] + 0.2) for k in range(2)],
    # 1975: the final offensive – tanks and infantry from the west and the north
    VH("tank", [(107.3, 12.9), (107.7, 12.75), (BMT[0] - 0.05, BMT[1])], s[9] + 0.5, s[9] + 2.4, until=en[9] + 0.2),
    MR([(107.25, 12.55), (107.6, 12.6), (107.95, 12.65)], s[9] + 0.6, s[9] + 2.6, NVA, kind="nva", soldiers=3, ships=False, until=en[9] + 0.2),
    BM(BMT, s[9] + 2.4, 0.26),
    MR([(107.0, 17.0), (107.3, 16.7), (107.55, 16.5)], s[9] + 2.2, s[9] + 4.0, NVA, kind="nva", soldiers=3, ships=False, until=en[9] + 0.2),
    VH("tank", [(107.6, 16.4), (107.9, 16.2), (DANANG[0] - 0.05, DANANG[1])], s[9] + 3.0, s[9] + 4.8, until=en[9] + 0.2),
    GL(HUE, s[9] + 3.4, en[9] + 0.2, 40, 60, 170), GL(DANANG, s[9] + 4.6, en[9] + 0.2, 40, 60, 170),
    # Khmer Rouge close in on Phnom Penh
    *[MR(p, s[10] + 0.4 + 0.3 * k, s[10] + 3.6 + 0.3 * k, KR, kind="khmerrouge", soldiers=3, ships=False, until=en[10] + 0.2)
      for k, p in enumerate([[(104.55, 11.95), (104.75, 11.72), (104.88, 11.6)], [(105.3, 11.85), (105.1, 11.7), (104.96, 11.6)],
                             [(104.6, 11.2), (104.78, 11.4), (104.9, 11.52)]])],
    GL(PNH, s[10] + 2.8, en[10] + 0.2, 45, 70, 190),
    PP("polpot", "POL POT", "KHMER ROUGE LEADER", s[10] + 0.4, en[10] + 0.2, x=300),
    # Saigon falls: the last helicopters fly out to the fleet, then a tank rolls through the palace gate
    *[HELI([(SAIGON[0] + dx, SAIGON[1] + dy), (107.2 + dx, 10.45 + dy), (FLEET[0] + dx, FLEET[1] + dy)], s[11] + 0.3 + 0.4 * k, s[11] + 2.9 + 0.4 * k, until=s[11] + 3.6 + 0.4 * k)
      for k, (dx, dy) in enumerate([(0.0, 0.0), (0.05, 0.06), (-0.04, -0.05)])],
    VH("warship", [(FLEET[0] + 0.15, FLEET[1] - 0.05), (FLEET[0] + 0.3, FLEET[1] - 0.12)], s[11] + 0.3, en[11], until=en[11] + 0.2, scale=0.8),
    VH("tank", [(106.62, 10.92), (106.66, 10.84), (PALACE[0] - 0.005, PALACE[1] + 0.01)], s[11] + 3.2, s[11] + 5.6, until=en[11] + 0.2, scale=0.9),
    GL(PALACE, s[11] + 5.4, en[11] + 0.2, 35, 80, 210),
]
TRAIL = [(105.6, 18.7), (105.8, 17.7), (106.2, 16.6), (106.8, 15.2), (107.1, 13.8), (106.9, 12.5), (106.5, 11.7)]
DMZ = [(106.55, 17.1), (106.9, 17.0), (107.15, 17.0)]
routes = [dict(pts=TRAIL, t0=s[4] + 0.4, t1=s[4] + 3.0, until=en[4] + 0.2, color=(250, 210, 120)),
          dict(pts=DMZ, t0=s[2] + 0.3, t1=s[2] + 1.0, until=en[4] + 0.2, color=(245, 245, 240))]
reveals = [dict(key="nv_gain", t0=s[9] + 0.6, t1=s[11] + 5.4, until=UG)]

def hook(fr, t): pass

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
    put(fr, glow_text("YEAR 1991", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE SOVIET UNION FALLS", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=33, dur=DUR, base_a="/home/claude/shortgen/hd_1969.png", base_b="/home/claude/shortgen/hd_1975.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1975a.png"),
           regions="/home/claude/shortgen/regions_ep33_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWM[0], SWM[1], "A", "M")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=hook, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.0, 0.2), (s[3] + 2.4, 0.2), (s[4] + 3.2, 0.2), (s[5] + 3.4, 0.2),
                                              (s[6] + 3.0, 0.2), (s[7] + 3.6, 0.25), (s[8] + 0.4, 0.2), (s[9] + 2.4, 0.2), (s[10] + 2.8, 0.2),
                                              (s[11] + 5.4, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
