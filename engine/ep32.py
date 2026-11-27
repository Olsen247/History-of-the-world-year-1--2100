"""Episode 32 – Year 1969: the space race and the Moon landing; the Vietnam War escalates.
Wright brothers' first flight (17 Dec 1903, Kitty Hawk) -> Moon walk (20/21 July 1969): less than 66 years.
Gagarin, Vostok 1 (12 April 1961, Baikonur/Tyuratam, one orbit, 108-minute flight, lands near Engels, Saratov region);
the Berlin Wall (night of 12-13 August 1961, barbed wire first, concrete from mid-August); the Cuban Missile Crisis
(U-2 photos 14 Oct 1962, naval "quarantine" 22-24 Oct, Khrushchev agrees to remove the missiles 28 Oct; thirteen days 16-28 Oct);
Tereshkova, Vostok 6 (16 June 1963, first woman in space); Kennedy shot in Dallas (22 Nov 1963);
the Gulf of Tonkin incident (2 Aug 1964, the 4 Aug attack is doubtful) and the Tonkin Gulf Resolution (7 Aug 1964);
Operation Rolling Thunder (from 2 March 1965, mostly fighter-bombers from Thailand, Da Nang and carriers) and 3,500 Marines of the
9th MEB at Da Nang (8 March 1965, the first US ground combat troops); the Cultural Revolution (May 1966, Red Guards);
the Warsaw Pact invasion of Czechoslovakia (20-21 August 1968: USSR, Poland, Hungary, Bulgaria) ends the Prague Spring (Dubcek);
about 536,000 US troops in Vietnam at the end of 1968; Apollo 11 (launch 16 July 1969, Kennedy Space Center; Armstrong on the Moon
20 July 1969 US time / 21 July UTC)."""
import sys, math
from PIL import Image, ImageDraw, ImageFilter
import hist_engine3 as E
from hist_engine3 import put, pr, eback, lerp, glow_text, GOLD, WHITE
import fx as FX
FX.set_year(1965)
import world_data_1960 as A_, world_data_1969 as B_
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep32/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
BAIK = (63.34, 45.92); KSC = (-80.60, 28.61); BERLIN = (13.40, 52.52); PRAGUE = (14.42, 50.08); DALLAS = (-96.80, 32.78)
shots = [(-79.0, 31.5, 1000), (40.0, 30.0, 2950), (60.0, 44.0, 1250), (13.3, 52.45, 150), (-80.0, 21.0, 800),
         (60.0, 44.0, 1250), (107.0, 19.2, 300), (106.9, 16.9, 320), (112.0, 33.0, 1500), (17.0, 49.6, 650),
         (107.4, 13.4, 280), (-80.8, 28.6, 700), (20.0, 20.0, 2950)]
ZOOM = {5: (s[5] + 4.7, (-96.0, 33.5, 1100))}
endshot = list(shots)
for i, (t, sh) in ZOOM.items(): endshot[i] = sh
keys = [(0.0, *shots[0]), (3.0, -79.5, 31.0, 920)]
for i in range(1, len(shots)):
    a, b = endshot[i - 1], shots[i]
    if i >= 2 and abs(a[0] - b[0]) > 50:     # long jumps: pull far out, then drop in
        keys += [(s[i] - 0.85, *a), (s[i] - 0.2, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 2950), (s[i] + 0.7, *b)]
        continue
    keys.append((s[i] - 0.85, *a))
    keys.append((s[i] + 0.35, *b))
keys.append((DUR, *shots[-1]))
# Baikonur -> Dallas inside line 5: pull out over the Atlantic, then drop into Texas
keys += [(s[5] + 3.6, *shots[5]), (s[5] + 4.2, -15.0, 45.0, 2950), (s[5] + 4.9, *ZOOM[5][1])]
keys = sorted(keys, key=lambda k: k[0])

SWB = (s[9] - 0.75, s[9] - 0.3)          # 1960 -> 1969 map while flying from China to Central Europe

ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
lb = lambda txt, pos, a, b, col, kind="mid": dict(text=txt, pos=pos, kind=kind, t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200); RRED = (232, 64, 72); USB = (150, 190, 250); SVC = (130, 175, 95)
labels = [
    # hook
    ev("KITTY HAWK 1903", (-75.67, 36.4), 0.3, en[0] + 0.2), ev("CAPE KENNEDY", (KSC[0] + 0.2, KSC[1] - 0.7), 1.0, en[0] + 0.2),
    # Gagarin
    ev("BAIKONUR", (BAIK[0], BAIK[1] - 1.3), s[2] + 0.3, en[2] + 0.2), lb("SOVIET UNION", (56.0, 53.5), s[2] + 0.5, en[2] + 0.2, SVC, kind="emp"),
    lb("LANDING NEAR SARATOV", (45.9, 50.4), s[2] + 3.4, en[2] + 0.2, WT, kind="small"),
    # Berlin
    lb("WEST BERLIN", (13.22, 52.50), s[3] + 0.6, en[3] + 0.2, USB, kind="small"),
    lb("EAST GERMANY", (13.75, 52.25), s[3] + 0.4, en[3] + 0.2, (165, 200, 120)),
    # Cuba
    lb("CUBA", (-78.5, 21.6), s[4] + 0.4, en[4] + 0.2, (160, 190, 235), kind="emp"), lb("FLORIDA", (-81.5, 27.8), s[4] + 0.5, en[4] + 0.2, WT, kind="small"),
    ev("SOVIET MISSILES", (-84.2, 23.7), s[4] + 1.8, en[4] + 0.2, RRED), lb("HAVANA", (-82.37, 23.35), s[4] + 0.8, en[4] + 0.2, WT, kind="small"),
    ev("US NAVY", (-75.6, 26.4), s[4] + 3.4, en[4] + 0.2, CYN),
    # Tereshkova, Dallas
    ev("VOSTOK 6", (BAIK[0], BAIK[1] - 1.3), s[5] + 0.3, s[5] + 3.8), ev("DALLAS", (DALLAS[0], DALLAS[1] - 0.8), s[5] + 5.0, en[5] + 0.2, RRED),
    lb("UNITED STATES", (-98.5, 36.5), s[5] + 5.0, en[5] + 0.2, USB),
    # Tonkin
    ev("GULF OF TONKIN", (108.1, 19.0), s[6] + 0.5, en[6] + 0.2), lb("NORTH VIETNAM", (104.3, 21.9), s[6] + 0.6, en[6] + 0.2, (240, 160, 110)),
    # Rolling Thunder, Da Nang
    ev("DA NANG", (108.0, 15.45), s[7] + 3.4, en[7] + 0.2), lb("17TH PARALLEL", (105.7, 17.5), s[7] + 0.5, en[7] + 0.2, WT, kind="small"),
    lb("NORTH VIETNAM", (104.8, 19.4), s[7] + 0.4, en[7] + 0.2, (240, 160, 110)),
    # Cultural Revolution
    ev("BEIJING", (117.6, 41.4), s[8] + 0.4, en[8] + 0.2, RRED), lb("CHINA", (101.0, 35.0), s[8] + 0.6, en[8] + 0.2, (240, 110, 100), kind="emp"),
    lb("SHANGHAI", (123.2, 31.6), s[8] + 2.6, en[8] + 0.2, WT, kind="small"), lb("WUHAN", (112.4, 29.4), s[8] + 2.6, en[8] + 0.2, WT, kind="small"),
    # Prague
    ev("PRAGUE", (PRAGUE[0] - 0.5, PRAGUE[1] - 0.5), s[9] + 0.4, en[9] + 0.2), lb("CZECHOSLOVAKIA", (16.0, 49.4), s[9] + 0.5, en[9] + 0.2, (120, 165, 225)),
    lb("POLAND", (18.5, 51.8), s[9] + 0.8, en[9] + 0.2, (225, 80, 90), kind="small"), lb("HUNGARY", (19.3, 47.2), s[9] + 0.8, en[9] + 0.2, (120, 170, 110), kind="small"),
    # Vietnam 1968
    lb("SOUTH VIETNAM", (107.5, 12.7), s[10] + 0.4, en[10] + 0.2, (240, 215, 120)), ev("SAIGON", (105.9, 10.25), s[10] + 0.6, en[10] + 0.2),
   
    # Apollo 11
    ev("KENNEDY SPACE CENTER", (KSC[0] + 0.3, KSC[1] - 0.6), s[11] + 0.3, en[11] + 0.2),
]
labels += WP.labels(A_, 1962, s[1] + 0.8, SWB[0])
labels += WP.labels(B_, 1968, SWB[1], s[12])

ticker = [(0, 1969), (s[1], 1969), (s[1] + 1.3, 1960)]
for i, y in ((2, 1961), (4, 1962), (5, 1963), (6, 1964), (7, 1965), (8, 1966), (9, 1968), (11, 1969)):
    ticker += [(s[i], ticker[-1][1]), (s[i] + 0.5, y)]
ticker.append((DUR, 1969))
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1969", l2="THE MOON LANDING", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1960", GOLD), hd(2, "12 APRIL 1961", "FIRST MAN IN SPACE", GOLD),
            hd(3, "13 AUGUST 1961", "BERLIN IS SPLIT"), hd(4, "OCTOBER 1962", "CUBAN MISSILE CRISIS"),
            hd(5, "JUNE 1963", "FIRST WOMAN IN SPACE", GOLD, t1=s[5] + 3.9),
            dict(t0=s[5] + 4.6, t1=en[5] + 0.2, l1="22 NOVEMBER 1963", l2="KENNEDY IS SHOT", c2=RRED),
            hd(6, "AUGUST 1964", "GULF OF TONKIN", CYN), hd(7, "MARCH 1965", "ROLLING THUNDER"),
            hd(8, "1966", "THE CULTURAL REVOLUTION"), hd(9, "AUGUST 1968", "PRAGUE SPRING CRUSHED"),
            hd(10, "END OF 1968", "HALF A MILLION TROOPS"), hd(11, "JULY 1969", "ONE SMALL STEP", GOLD)]

MR = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
BM = lambda pos, t, sc=0.32: dict(type="boom", pos=pos, t0=t, swords=False, scale=sc)
GL = lambda pos, a, b, r=200, a0=40, a1=110: dict(type="glow", pos=pos, t0=a, t1=b, radius=r, a0=a0, a1=a1)
USA = (70, 110, 200); SOV = (200, 50, 50); PLA = (200, 40, 40)
SANCRIS = (-83.05, 22.72)
fx = [
    # hook: the Wright Flyer hops at Kitty Hawk, then a Saturn V climbs from Cape Kennedy
    VH("plane", [(-75.95, 35.95), (-75.45, 36.1)], 0.3, 1.6, until=en[0] + 0.2, scale=0.8),
    dict(type="vehicle", kind="rocket", path=[KSC], t0=1.2, t1=4.0, until=en[0] + 0.3, height=820),
    GL(KSC, 1.0, en[0] + 0.2, 60, 60, 170),
    # Gagarin: Vostok 1 rises from Baikonur, lands near Saratov
    dict(type="vehicle", kind="rocket", path=[BAIK], t0=s[2] + 0.3, t1=s[2] + 3.0, until=en[2] + 0.2, height=700),
    GL(BAIK, s[2] + 0.2, en[2] + 0.2, 60, 60, 170), GL((45.9, 51.27), s[2] + 3.4, en[2] + 0.2, 45, 60, 170),
    PP("gagarin", "YURI GAGARIN", "SOVIET COSMONAUT", s[2] + 0.4, en[2] + 0.2, x=780),
    # Berlin: the sector border is sealed overnight
    GL(BERLIN, s[3] + 0.3, en[3] + 0.2, 70, 50, 140),
    PP("ulbricht", "WALTER ULBRICHT", "LEADER OF EAST GERMANY", s[3] + 0.4, en[3] + 0.2, x=780),
    # Cuba: a U-2 photographs the missile sites; the US Navy ring; Kennedy and Khrushchev
    VH("plane", [(-81.4, 28.4), (-82.2, 25.0), SANCRIS, (-80.6, 22.5), (-80.3, 25.6)], s[4] + 0.3, s[4] + 2.6, until=s[4] + 3.0),
    GL(SANCRIS, s[4] + 1.6, en[4] + 0.2, 55, 70, 190), GL((-79.7, 22.55), s[4] + 1.9, en[4] + 0.2, 45, 70, 190),
    *[VH("warship", [(x0, y0), (x1, y1)], s[4] + 3.0 + 0.2 * k, s[4] + 4.6 + 0.2 * k, until=en[4] + 0.2)
      for k, (x0, y0, x1, y1) in enumerate([(-71.0, 27.5, -73.2, 26.6), (-70.5, 25.0, -72.6, 24.2), (-70.6, 22.6, -72.2, 22.2), (-74.0, 29.0, -75.6, 27.6)])],
    PP("kennedy", "JOHN F. KENNEDY", "PRESIDENT OF THE UNITED STATES", s[4] + 0.4, s[4] + 5.2, x=780),
    PP("khrushchev", "NIKITA KHRUSHCHEV", "SOVIET LEADER", s[4] + 4.4, en[4] + 0.2, x=300),
    # Tereshkova from Baikonur; then Dallas
    dict(type="vehicle", kind="rocket", path=[BAIK], t0=s[5] + 0.3, t1=s[5] + 3.0, until=s[5] + 3.8, height=700),
    PP("tereshkova", "VALENTINA TERESHKOVA", "SOVIET COSMONAUT", s[5] + 0.4, s[5] + 4.0, x=780),
    GL(DALLAS, s[5] + 5.0, en[5] + 0.2, 55, 80, 200),
    PP("kennedy", "JOHN F. KENNEDY", "PRESIDENT OF THE UNITED STATES", s[5] + 5.0, en[5] + 0.2, x=300),
    # Gulf of Tonkin: a US destroyer on patrol, a clash at sea
    VH("warship", [(107.7, 18.6), (107.4, 19.4), (107.0, 19.9)], s[6] + 0.3, s[6] + 2.6, until=en[6] + 0.2),
    VH("warship", [(106.3, 20.5), (106.75, 20.05)], s[6] + 1.2, s[6] + 2.6, until=s[6] + 3.6, scale=0.55),
    BM((106.95, 19.95), s[6] + 2.7, 0.22),
    PP("johnson", "LYNDON B. JOHNSON", "PRESIDENT OF THE UNITED STATES", s[6] + 0.4, en[6] + 0.2, x=780),
    # Rolling Thunder: jets from Thailand, Da Nang and the carriers; the Marines come ashore at Da Nang
    VH("jet", [(102.1, 14.95), (104.2, 16.8), (105.7, 18.7)], s[7] + 0.4, s[7] + 2.4, until=s[7] + 3.4),
    VH("jet", [(108.2, 16.05), (107.3, 16.8), (106.6, 17.5)], s[7] + 0.6, s[7] + 2.2, until=s[7] + 3.2),
    VH("jet", [(110.2, 17.6), (108.2, 18.1), (106.1, 18.4)], s[7] + 0.8, s[7] + 2.6, until=s[7] + 3.6),
    BM((105.7, 18.7), s[7] + 2.5, 0.24), BM((106.6, 17.5), s[7] + 2.3, 0.22), BM((106.1, 18.4), s[7] + 2.7, 0.22),
    MR([(110.0, 16.4), (109.0, 16.2), (108.2, 16.05)], s[7] + 3.2, en[7] - 0.3, USA, kind="usmc65", soldiers=5, until=en[7] + 0.2),
    GL((108.2, 16.05), s[7] + 3.4, en[7] + 0.2, 45, 60, 170),
    # Cultural Revolution: Red Guards stream out of Beijing
    GL((116.4, 39.9), s[8] + 0.3, en[8] + 0.2, 90, 60, 180),
    MR([(116.4, 39.9), (117.2, 36.0), (118.8, 32.0), (121.4, 31.2)], s[8] + 1.0, s[8] + 5.0, PLA, kind="redguard", soldiers=3, ships=False, until=en[8] + 0.2),
    MR([(116.4, 39.9), (114.5, 35.0), (114.3, 30.6)], s[8] + 1.2, s[8] + 5.2, PLA, kind="redguard", soldiers=3, ships=False, until=en[8] + 0.2),
    MR([(116.4, 39.9), (112.0, 37.0), (108.9, 34.3)], s[8] + 1.4, s[8] + 5.4, PLA, kind="redguard", soldiers=3, ships=False, until=en[8] + 0.2),
    PP("mao", "MAO ZEDONG", "CHAIRMAN OF THE COMMUNIST PARTY", s[8] + 0.4, en[8] + 0.2, x=780),
    # Prague: Warsaw Pact tanks from Poland, the Soviet Union and Hungary; Soviet airborne troops fly into Prague
    VH("tank", [(17.0, 51.4), (16.0, 50.6), (14.6, 50.15)], s[9] + 0.5, s[9] + 3.6, until=en[9] + 0.2),
    VH("tank", [(18.9, 50.4), (18.3, 49.85), (17.3, 49.5)], s[9] + 0.6, s[9] + 3.4, until=en[9] + 0.2),
    VH("tank", [(22.6, 48.7), (20.5, 48.8), (17.4, 49.1)], s[9] + 0.7, s[9] + 3.8, until=en[9] + 0.2),
    VH("tank", [(19.0, 47.7), (18.2, 48.3), (17.2, 48.25)], s[9] + 0.8, s[9] + 3.6, until=en[9] + 0.2),
    VH("plane", [(21.5, 51.6), (17.5, 50.9), (14.27, 50.1)], s[9] + 0.4, s[9] + 2.8, until=s[9] + 3.4),
    GL(PRAGUE, s[9] + 2.6, en[9] + 0.2, 60, 70, 190),
    PP("dubcek", "ALEXANDER DUBCEK", "LEADER OF THE PRAGUE SPRING", s[9] + 0.4, en[9] + 0.2, x=300),
    # Vietnam 1968: American troops all over the South
    MR([(109.2, 13.8), (108.6, 13.9), (108.0, 14.0)], s[10] + 0.5, s[10] + 3.2, USA, kind="usmc65", soldiers=4, ships=False, until=en[10] + 0.2),
    MR([(106.7, 10.8), (106.4, 11.25), (106.1, 11.6)], s[10] + 0.7, s[10] + 3.4, USA, kind="gi", soldiers=4, ships=False, until=en[10] + 0.2),
    MR([(107.6, 16.45), (107.1, 16.6), (106.75, 16.65)], s[10] + 0.9, s[10] + 3.6, USA, kind="usmc65", soldiers=4, ships=False, until=en[10] + 0.2),
    VH("jet", [(106.65, 10.8), (107.6, 13.0), (107.4, 16.0)], s[10] + 1.2, s[10] + 3.6, until=s[10] + 4.4),
    PP("johnson", "LYNDON B. JOHNSON", "PRESIDENT OF THE UNITED STATES", s[10] + 0.4, en[10] + 0.2, x=780),
    # Apollo 11
    dict(type="vehicle", kind="rocket", path=[KSC], t0=s[11] + 0.2, t1=s[11] + 3.4, until=en[11] + 0.2, height=950),
    GL(KSC, s[11] + 0.2, en[11] + 0.2, 60, 70, 190),
    PP("armstrong", "NEIL ARMSTRONG", "APOLLO 11 COMMANDER", s[11] + 0.5, en[11] + 0.2, x=300),
]
WB = [(13.09, 52.42), (13.17, 52.39), (13.30, 52.37), (13.42, 52.38), (13.46, 52.42), (13.40, 52.48), (13.42, 52.53), (13.38, 52.58),
      (13.31, 52.65), (13.21, 52.63), (13.12, 52.58), (13.11, 52.50), (13.09, 52.42)]
routes = [dict(pts=WB, t0=s[3] + 0.5, t1=s[3] + 2.6, until=en[3] + 0.2, color=(245, 245, 240))]

# ---- the Moon (screen overlay in the hook and the Apollo 11 line) ----
_MOON = {}
def _moon_img(r=125):
    if r in _MOON: return _MOON[r]
    n = r * 4; im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = n // 2
    for k in range(18):   # soft glow
        rr = r + 60 - k * 3; d.ellipse([c - rr, c - rr, c + rr, c + rr], fill=(250, 240, 210, 6 + k))
    d.ellipse([c - r, c - r, c + r, c + r], fill=(222, 220, 212, 255))
    for (dx, dy, cr, sh) in [(-0.35, -0.3, 0.28, 190), (0.25, -0.1, 0.22, 180), (0.05, 0.35, 0.3, 186), (-0.4, 0.3, 0.14, 175),
                             (0.45, 0.35, 0.12, 178), (0.2, -0.55, 0.12, 182)]:
        x, y, q = c + dx * r, c + dy * r, cr * r
        d.ellipse([x - q, y - q, x + q, y + q], fill=(sh, sh - 2, sh - 8, 255))
    d.ellipse([c - r, c - r, c + r, c + r], outline=(250, 248, 238, 255), width=3)
    # Apollo lunar module: gold descent stage, grey ascent stage, four legs
    lx, ly = c + 0.05 * r, c + 0.62 * r
    d.rectangle([lx - 9, ly - 6, lx + 9, ly + 4], fill=(230, 180, 60, 255)); d.rectangle([lx - 6, ly - 14, lx + 6, ly - 6], fill=(170, 170, 176, 255))
    for sx in (-1, 1): d.line([(lx + sx * 8, ly + 2), (lx + sx * 14, ly + 12)], fill=(220, 200, 150, 255), width=2)
    _MOON[r] = im
    return im

def hook(fr, t):
    for t0, t1, path in ((1.8, en[0] + 0.1, False), (s[11] + 2.6, en[11] + 0.2, True)):
        if t < t0 or t > t1 + 0.4: continue
        a = min(pr(t, t0, t0 + 0.5), 1 - pr(t, t1, t1 + 0.4))
        if path:   # dotted trajectory from the launch towards the Moon
            d = ImageDraw.Draw(fr, "RGBA"); k = pr(t, t0, t0 + 1.2)
            pts = [(300 + (790 - 300) * f, 900 - 420 * math.sin(f * math.pi / 2) ) for f in [j / 40 for j in range(41)]]
            for j in range(0, int(40 * k), 2): d.line([pts[j], pts[j + 1]], fill=(240, 240, 235, int(200 * a)), width=4)
        put(fr, _moon_img(), 790, 560, alpha=a, scale=0.9 + 0.1 * min(1, eback(pr(t, t0, t0 + 0.6), 2.0)))

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
    put(fr, glow_text("YEAR 1975", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE FALL OF SAIGON", 44, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=32, dur=DUR, base_a="/home/claude/shortgen/hd_1960.png", base_b="/home/claude/shortgen/hd_1969.png",
           regions=None, keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=[], labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=hook, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 0.4, 0.2), (s[3] + 0.5, 0.2), (s[4] + 1.8, 0.2), (s[5] + 5.0, 0.25),
                                              (s[6] + 2.7, 0.2), (s[7] + 2.4, 0.2), (s[8] + 0.4, 0.2), (s[9] + 2.6, 0.2), (s[10] + 0.5, 0.2),
                                              (s[11] + 2.6, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
