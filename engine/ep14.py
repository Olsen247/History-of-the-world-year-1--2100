"""Episode 14 – Year 1533: Pizarro and the fall of the Inca (Gustav Vasa and the end of the Kalmar Union, Pavia, Panipat and the Mughals,
Mohacs, the Sack of Rome, the siege of Vienna, the Inca civil war, Cajamarca, the ransom room, Atahualpa's execution and Cusco)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1533)
import world_data_1522 as A, world_data_1533 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep14/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
shots = [(-77.5, -8.0, 900), (10, 20, 2850), (16.5, 61.0, 800), (9.4, 45.6, 520), (73.5, 31.0, 800), (19.3, 46.2, 520), (11.4, 43.4, 620),
         (17.6, 47.7, 520), (-76.0, -7.5, 1000), (-79.3, -5.4, 520), (-76.0, -10.0, 800), (-75.0, -10.5, 800), WIDE]
EXTRA = {0: [], 9: [(3.0, None), (4.2, (-78.5, -7.2, 380))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, -78.5, -6.0, 1150), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("sweden", s[2] + 2.0, s[2] + 5.0), rv("mughal", s[4] + 3.0, s[4] + 5.6), rv("syrmia_ot", s[5] + 2.4, s[5] + 3.6),
           rv("peru_sp", s[11] + 2.6, s[11] + 5.4)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
labels = [lab(A, "INCA EMPIRE", "INCA\nEMPIRE", pos=(-70.5, -17.0), t_in=0.6, t_out=en[0]),
          lab(A, "KALMAR UNION", pos=(15.0, 63.5), t_in=s[2] + 0.2, t_out=s[2] + 2.2),
          lab(B, "SWEDEN", pos=(15.6, 62.6), t_in=s[2] + 3.0, t_out=en[2] + 0.2),
          lab(B, "DENMARK-NORWAY", "DENMARK-\nNORWAY", pos=(8.6, 61.4), t_in=s[2] + 3.4, t_out=en[2] + 0.2),
          lab(A, "FRANCE", pos=(5.6, 46.6), t_in=s[3] + 0.3, t_out=en[3]),
          lab(A, "DELHI SULTANATE", "DELHI\nSULTANATE", pos=(77.0, 28.0), t_in=s[4] + 0.3, t_out=s[4] + 3.0),
          lab(B, "MUGHAL EMPIRE", "MUGHAL\nEMPIRE", pos=(82.6, 25.5), t_in=s[4] + 3.6, t_out=en[4] + 0.2),
          lab(A, "HUNGARY", pos=(21.4, 47.3), t_in=s[5] + 0.2, t_out=en[5]),
          lab(A, "PAPAL STATES", "PAPAL\nSTATES", pos=(13.6, 43.7), t_in=s[6] + 0.3, t_out=en[6]),
          lab(A, "INCA EMPIRE", "INCA\nEMPIRE", pos=(-67.5, -20.5), t_in=s[8] + 0.3, t_out=en[8] + 0.2),
          lab(A, "INCA EMPIRE", "INCA\nEMPIRE", pos=(-67.5, -20.5), t_in=s[10] + 0.3, t_out=en[11] + 0.2),
          lab(B, "SPAIN", pos=(-4.0, 40.0), t_in=s[12] - 0.2, t_out=s[12] + 0.2)]
labels += [ev("STOCKHOLM", (18.6, 58.7), s[2] + 0.4, en[2] + 0.2),
           ev("PAVIA", (9.15, 44.55), s[3] + 0.4, en[3] + 0.2), ev("PANIPAT", (75.8, 27.8), s[4] + 2.4, en[4] + 0.2),
           ev("KABUL", (67.4, 33.9), s[4] + 0.3, s[4] + 2.4),
           ev("MOHÁCS", (16.4, 45.5), s[5] + 0.4, en[5] + 0.2), 
           ev("ROME", (12.48, 41.6), s[6] + 0.4, en[6] + 0.2),
           ev("VIENNA", (16.2, 49.0), s[7] + 0.4, en[7] + 0.2),
           ev("QUITO", (-78.5, 0.1), s[8] + 0.3, s[8] + 3.0), 
           ev("CAJAMARCA", (-78.3, -8.4), s[9] + 0.4, en[9] + 0.2),
           ev("CUSCO", (-70.2, -15.3), s[11] + 3.0, en[11] + 0.2)]

ticker = [(0, 1533), (s[1], 1533), (s[1] + 1.3, 1522), (s[2], 1522), (s[2] + 0.6, 1523), (s[3], 1523), (s[3] + 0.6, 1525), (s[4], 1525), (s[4] + 0.6, 1526),
          (s[6], 1526), (s[6] + 0.6, 1527), (s[7], 1527), (s[7] + 0.6, 1529), (s[8], 1529), (s[8] + 0.6, 1532), (s[11], 1532), (s[11] + 0.6, 1533), (DUR, 1533)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1533", l2="THE FALL OF THE INCA", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1522", GOLD), hd(2, "YEAR 1523", "SWEDEN BREAKS FREE", CYN), hd(3, "YEAR 1525", "A KING CAPTURED"),
            hd(4, "YEAR 1526", "THE MUGHAL EMPIRE", GRN), hd(5, "AUGUST 1526", "DISASTER AT MOHÁCS"), hd(6, "MAY 1527", "THE SACK OF ROME"),
            hd(7, "YEAR 1529", "THE SIEGE OF VIENNA"), hd(8, "YEAR 1532", "BROTHER AGAINST BROTHER", GOLD),
            hd(9, "NOVEMBER 1532", "TRAP AT CAJAMARCA"), hd(10, "YEAR 1532", "A ROOM OF GOLD", GOLD), hd(11, "YEAR 1533", "CUSCO FALLS")]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
SPC = (235, 180, 40); SWC = (80, 130, 205); HRE = (230, 200, 90); FRC = (70, 110, 200); MGC = (40, 150, 95); OTC = (200, 60, 60)
HUC = (110, 170, 110); ATC = (40, 140, 160); HUA = (235, 105, 35)
HOOK = [(-80.45, -3.57), (-80.6, -5.2), (-79.9, -6.2), (-79.1, -6.8), (-78.5, -7.16)]
VASA = [(14.5, 60.6), (15.6, 60.1), (16.8, 59.7), (17.6, 59.4), (18.05, 59.33)]
IMP = [(9.9, 45.45), (9.6, 45.3), (9.35, 45.22), (9.17, 45.19)]
FRA = [(8.5, 45.45), (8.8, 45.3), (9.05, 45.2)]
BABUR = [(69.2, 34.5), (70.5, 34.2), (71.6, 34.0), (72.9, 33.6), (74.3, 31.6), (75.8, 30.8), (76.97, 29.39)]
JAN1 = [(20.46, 44.8), (20.0, 45.25), (19.4, 45.4), (18.9, 45.75), (18.68, 45.99)]
HUN = [(19.04, 47.5), (18.95, 47.0), (18.85, 46.5), (18.72, 46.1)]
ROMEM = [(9.6, 45.1), (10.3, 44.6), (11.0, 44.1), (11.6, 43.5), (12.1, 42.7), (12.48, 41.9)]
VIEN = [(19.04, 47.5), (18.3, 47.75), (17.6, 47.7), (17.0, 48.0), (16.45, 48.2)]
BACK = [(16.6, 48.1), (17.6, 47.7), (18.3, 47.6), (19.04, 47.5)]
ATAW = [(-78.5, -0.2), (-79.0, -2.9), (-79.6, -5.5), (-78.5, -7.16), (-77.5, -9.5), (-75.5, -11.8), (-73.5, -13.2), (-72.3, -13.5)]
HUAS = [(-71.97, -13.53), (-72.6, -13.3), (-73.2, -13.2)]
PIZ = [(-80.45, -3.57), (-80.6, -5.2), (-79.9, -6.2), (-79.1, -6.8), (-78.52, -7.16)]
GOLDP = [(-71.97, -13.53), (-74.0, -13.0), (-75.5, -11.8), (-77.0, -9.8), (-78.45, -7.3)]
CUSCO = [(-78.5, -7.16), (-77.5, -9.3), (-76.3, -11.0), (-75.5, -11.8), (-74.0, -13.0), (-72.9, -13.5), (-72.0, -13.53)]
fx = [
    M(HOOK, 0.4, en[0] - 0.4, SPC, kind="conquistador", soldiers=9, ships=False, until=en[0] + 0.4),
    PP("pizarro", "FRANCISCO PIZARRO", "SPANISH CONQUISTADOR", 1.2, en[0] + 0.2, x=300),
    M(VASA, s[2] + 0.4, s[2] + 3.0, SWC, kind="swede", soldiers=8, ships=False, until=en[2] + 0.3),
    PP("gustav", "GUSTAV VASA", "KING OF SWEDEN", s[2] + 0.4, en[2] + 0.2, x=300),
    M(IMP, s[3] + 0.4, s[3] + 3.2, HRE, kind="landsknecht", soldiers=8, ships=False, until=en[3] + 0.3),
    M(FRA, s[3] + 0.6, s[3] + 3.0, FRC, kind="french", soldiers=5, ships=False, until=s[3] + 4.0),
    PP("charlesv", "CHARLES V", "HOLY ROMAN EMPEROR", s[3] + 0.4, en[3] + 0.2, x=300),
    PP("francis", "FRANCIS I", "KING OF FRANCE", s[3] + 3.2, en[3] + 0.2),
    M(BABUR, s[4] + 0.4, s[4] + 3.2, MGC, kind="timurid", soldiers=8, ships=False, until=en[4] + 0.3),
    PP("babur", "BABUR", "FOUNDER OF THE MUGHAL EMPIRE", s[4] + 0.4, en[4] + 0.2, x=300),
    M(JAN1, s[5] + 0.4, s[5] + 2.8, OTC, kind="janissary", soldiers=10, ships=False, until=en[5] + 0.3),
    M(HUN, s[5] + 0.6, s[5] + 2.6, HUC, kind="hussar", soldiers=5, ships=False, until=s[5] + 3.6),
    PP("suleiman", "SULEIMAN THE MAGNIFICENT", "OTTOMAN SULTAN", s[5] + 0.4, en[5] + 0.2),
    M(ROMEM, s[6] + 0.4, s[6] + 3.4, HRE, kind="landsknecht", soldiers=9, ships=False, until=en[6] + 0.3),
    IC("fire", (12.48, 42.35), s[6] + 3.4, en[6] + 0.2),
    PP("charlesv", "CHARLES V", "HIS ARMY SACKS ROME", s[6] + 0.4, en[6] + 0.2),
    M(VIEN, s[7] + 0.4, s[7] + 3.4, OTC, kind="janissary", soldiers=12, ships=False, until=s[7] + 4.6),
    M(BACK, s[7] + 4.6, en[7] - 0.2, OTC, kind="janissary", soldiers=6, ships=False, until=en[7] + 0.3),
    PP("suleiman", "SULEIMAN THE MAGNIFICENT", "OTTOMAN SULTAN", s[7] + 0.4, en[7] + 0.2, x=300),
    M(ATAW, s[8] + 0.4, s[8] + 4.6, ATC, kind="inca", soldiers=8, ships=False, until=en[8] + 0.3),
    M(HUAS, s[8] + 3.0, s[8] + 4.4, HUA, kind="inca", soldiers=4, ships=False, until=s[8] + 5.0),
    PP("atahualpa", "ATAHUALPA", "SAPA INCA", s[8] + 0.4, en[8] + 0.2, x=300),
    M(PIZ, s[9] + 0.3, s[9] + 3.6, SPC, kind="conquistador", soldiers=8, ships=False, until=en[9] + 0.3),
    PP("pizarro", "FRANCISCO PIZARRO", "SPANISH CONQUISTADOR", s[9] + 0.4, en[9] + 0.2, x=300),
    PP("atahualpa", "ATAHUALPA", "TAKEN PRISONER", s[9] + 3.8, en[9] + 0.2),
    M(GOLDP, s[10] + 0.6, s[10] + 4.2, HUA, kind="inca", soldiers=6, ships=False, until=en[10] + 0.3),
    IC("gold", (-79.4, -6.6), s[10] + 1.4, en[10] + 0.2),
    PP("atahualpa", "ATAHUALPA", "SAPA INCA", s[10] + 0.4, en[10] + 0.2, x=300),
    M(CUSCO, s[11] + 2.2, en[11] - 0.4, SPC, kind="conquistador", soldiers=8, ships=False, until=en[11] + 0.3),
    PP("pizarro", "FRANCISCO PIZARRO", "CONQUEROR OF PERU", s[11] + 0.4, en[11] + 0.2, x=300),
]
routes = []
labels += WP.labels(B, 1533, s[1] + 0.8, s[12])

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
    put(fr, glow_text("YEAR 1642", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("TASMAN REACHES NEW ZEALAND", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=14, dur=DUR, base_a="/home/claude/shortgen/hd_1522.png", base_b="/home/claude/shortgen/hd_1533.png",
           regions="/home/claude/shortgen/regions_ep14_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (s[12] - 0.85, s[12] + 0.3, "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 2.0, 0.2), (s[3] + 3.2, 0.2), (s[4] + 3.0, 0.2), (s[5] + 2.8, 0.25),
                                              (s[6] + 3.4, 0.25), (s[9] + 3.6, 0.3), (s[11] + 2.6, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
