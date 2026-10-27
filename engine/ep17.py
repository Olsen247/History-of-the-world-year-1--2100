"""Episode 17 – Year 1776: the United States declares independence (Boston Massacre 1770, first partition of Poland 1772, Cook crosses
the Antarctic Circle 1773, Pugachev's revolt 1773, Boston Tea Party 1773, Lexington and Concord 1775, Bunker Hill 1775, the British leave
Boston March 1776, Spanish settlers reach San Francisco June 1776, Declaration of Independence 4 July 1776)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1776)
import world_data_1770 as A, world_data_1776 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep17/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
BOS = (-71.06, 42.36)
shots = [(-72.5, 41.0, 1000), WIDE, (-71.1, 42.4, 330), (23.0, 52.5, 1050), (28.0, -44.0, 1700), (52.0, 53.0, 1200), (-71.0, 42.35, 330),
         (-71.25, 42.45, 330), (-71.08, 42.38, 300), (-69.0, 43.2, 700), (-121.0, 36.6, 700), (-76.5, 39.0, 1150), WIDE]
EXTRA = {11: [(2.8, None), (3.6, (-78.0, 38.0, 1600))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, -62, 36, 2400), (2.2, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("part_ru", s[3] + 1.6, s[3] + 4.0), rv("part_pr", s[3] + 2.0, s[3] + 4.2), rv("part_at", s[3] + 2.4, s[3] + 4.6),
           rv("sf_sp", s[10] + 2.6, s[10] + 4.4), rv("usa", s[11] + 3.4, s[11] + 6.4)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
CYN = (110, 200, 230)
labels = [lab(B, "UNITED STATES", "THIRTEEN\nCOLONIES", pos=(-77.5, 40.6), t_in=0.6, t_out=en[0] + 0.2),
          lab(A, "POLISH-LITHUANIAN COMMONWEALTH", "POLAND-\nLITHUANIA", kind="mid", pos=(24.0, 52.6), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(B, "RUSSIAN EMPIRE", "RUSSIA", pos=(33.5, 56.4), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(B, "PRUSSIA", pos=(14.2, 52.9), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(B, "HABSBURG MONARCHY", "AUSTRIA", pos=(17.0, 48.0), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(A, "RUSSIAN EMPIRE", "RUSSIAN\nEMPIRE", pos=(60.0, 58.6), t_in=s[5] + 0.3, t_out=en[5] + 0.2),
          lab(B, "SPAIN", pos=(-118.6, 35.4), t_in=s[10] + 0.3, t_out=en[10] + 0.2),
          lab(B, "UNITED STATES", "UNITED\nSTATES", pos=(-77.8, 36.8), t_in=s[11] + 5.0, t_out=s[12] + 0.2),
          lab(B, "SPAIN", pos=(-100.0, 22.0), t_in=s[12] - 0.2, t_out=s[12] + 0.2)]
labels += [ev("BOSTON", (-71.5, 42.75), s[2] + 0.4, en[2] + 0.2), ev("BOSTON HARBOR", (-70.85, 42.18), s[6] + 0.4, en[6] + 0.2),
           ev("LEXINGTON & CONCORD", (-71.4, 43.05), s[7] + 0.6, en[7] + 0.2), ev("BUNKER HILL", (-71.1, 42.8), s[8] + 0.4, en[8] + 0.2),
           ev("BOSTON", (-71.8, 41.95), s[9] + 0.4, en[9] + 0.2, (240, 230, 200)), ev("HALIFAX", (-63.6, 45.0), s[9] + 3.4, en[9] + 0.2),
           ev("ANTARCTIC CIRCLE", (34.0, -50.5), s[4] + 2.6, en[4] + 0.2, CYN), ev("CAPE TOWN", (18.4, -33.2), s[4] + 0.4, s[4] + 2.6, (240, 230, 200)),
           ev("ORENBURG", (55.1, 51.2), s[5] + 1.8, en[5] + 0.2), ev("KAZAN", (49.1, 56.3), s[5] + 3.6, en[5] + 0.2, (240, 230, 200)),
           ev("SAN FRANCISCO", (-122.2, 38.2), s[10] + 2.4, en[10] + 0.2), ev("MONTEREY", (-121.4, 36.25), s[10] + 0.4, en[10] + 0.2, (240, 230, 200)),
           ev("PHILADELPHIA", (-72.6, 39.6), s[11] + 0.4, en[11] + 0.2)]

ticker = [(0, 1776), (s[1], 1776), (s[1] + 1.3, 1770), (s[2], 1770), (s[3], 1770), (s[3] + 0.6, 1772), (s[4], 1772), (s[4] + 0.6, 1773),
          (s[7], 1773), (s[7] + 0.6, 1775), (s[9], 1775), (s[9] + 0.6, 1776), (DUR, 1776)]
RRED = (232, 64, 72); GRN = (110, 210, 150); ORG = (245, 150, 50)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1776", l2="A NEW NATION", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1770", GOLD), hd(2, "MARCH 1770", "BOSTON MASSACRE"), hd(3, "YEAR 1772", "POLAND CARVED UP", GRN),
            hd(4, "JANUARY 1773", "ANTARCTIC CIRCLE", CYN), hd(5, "YEAR 1773", "PUGACHEV'S REVOLT", ORG), hd(6, "DECEMBER 1773", "BOSTON TEA PARTY", GOLD),
            hd(7, "APRIL 1775", "LEXINGTON"), hd(8, "JUNE 1775", "BUNKER HILL"), hd(9, "MARCH 1776", "BOSTON FREED", CYN),
            hd(10, "JUNE 1776", "SAN FRANCISCO", ORG), hd(11, "JULY 1776", "INDEPENDENCE", GOLD)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
GBC = (200, 40, 50); USC = (120, 90, 55); RUC = (50, 130, 70); PRC = (40, 50, 100); ATC = (240, 240, 240); COC = (150, 30, 40); SPC = (235, 180, 40)
HOOK = [(-62.0, 38.5), (-66.0, 40.6), (-69.0, 41.9), (-70.4, 42.3), (-70.95, 42.35)]
RED1 = [(-71.18, 42.25), (-71.12, 42.31), (-71.07, 42.355)]
COL1 = [(-70.95, 42.47), (-71.0, 42.41), (-71.05, 42.365)]
RUP = [(36.5, 55.5), (33.5, 55.2), (31.5, 54.9), (29.8, 54.5)]
PRP = [(13.5, 53.8), (15.5, 54.1), (17.2, 53.9), (18.3, 53.7)]
ATP = [(16.4, 48.2), (18.0, 49.0), (19.6, 49.7), (21.5, 49.9)]
COOK = [(18.4, -33.9), (21.0, -38.0), (25.0, -44.0), (30.0, -50.0), (36.0, -55.9)]
PUG = [(51.37, 51.2), (53.0, 51.45), (55.0, 51.7)]
PUG2 = [(55.1, 51.9), (56.5, 53.8), (54.5, 55.2), (51.5, 55.7), (49.4, 55.8)]
TEA = [(-71.12, 42.42), (-71.08, 42.39), (-71.05, 42.36)]
LEX1 = [(-71.06, 42.36), (-71.15, 42.40), (-71.23, 42.445), (-71.35, 42.46)]
MIN1 = [(-71.6, 42.7), (-71.48, 42.58), (-71.37, 42.48)]
LEX2 = [(-71.34, 42.45), (-71.24, 42.43), (-71.15, 42.39), (-71.07, 42.37)]
BUNKB = [(-71.05, 42.355), (-71.055, 42.368), (-71.06, 42.374)]
BUNKA = [(-71.16, 42.43), (-71.1, 42.4), (-71.065, 42.38)]
WASH = [(-71.3, 42.25), (-71.15, 42.3), (-71.06, 42.32)]
EVAC = [(-71.0, 42.35), (-70.4, 42.4), (-69.0, 42.9), (-67.2, 43.5), (-65.6, 44.0), (-63.6, 44.6)]
SF = [(-121.9, 36.6), (-121.75, 36.95), (-121.95, 37.3), (-122.25, 37.6), (-122.42, 37.78)]
fx = [
    M(HOOK, 0.4, en[0] - 0.1, GBC, kind="line", soldiers=2, sea_only=True, until=en[0] + 0.4),
    PP("washington", "GEORGE WASHINGTON", "CONTINENTAL ARMY", 1.6, en[0] + 0.2, x=300),
    M(RED1, s[2] + 0.4, s[2] + 2.2, GBC, kind="line", soldiers=6, ships=False, until=en[2] + 0.3),
    M(COL1, s[2] + 0.8, s[2] + 2.4, USC, kind="minuteman", soldiers=6, ships=False, until=en[2] + 0.3),
    M(RUP, s[3] + 0.4, s[3] + 2.2, RUC, kind="line", soldiers=6, ships=False, until=en[3] + 0.3),
    M(PRP, s[3] + 0.8, s[3] + 2.4, PRC, kind="grenadier", soldiers=6, ships=False, until=en[3] + 0.3),
    M(ATP, s[3] + 1.2, s[3] + 2.8, ATC, kind="line", soldiers=6, ships=False, until=en[3] + 0.3),
    PP("catherine", "CATHERINE THE GREAT", "EMPRESS OF RUSSIA", s[3] + 0.4, en[3] + 0.2),
    M(COOK, s[4] + 0.4, s[4] + 3.4, GBC, kind="line", soldiers=2, sea_only=True, until=en[4] + 0.3),
    PP("cook", "JAMES COOK", "BRITISH NAVY CAPTAIN", s[4] + 0.4, en[4] + 0.2),
    M(PUG, s[5] + 0.4, s[5] + 2.0, COC, kind="cossack", soldiers=6, ships=False, until=s[5] + 2.6),
    M(PUG2, s[5] + 2.4, en[5] - 0.2, COC, kind="cossack", soldiers=6, ships=False, until=en[5] + 0.3),
    PP("pugachev", "YEMELYAN PUGACHEV", "COSSACK REBEL", s[5] + 0.4, en[5] + 0.2, x=300),
    PP("catherine", "CATHERINE THE GREAT", "EMPRESS OF RUSSIA", s[5] + 1.6, en[5] + 0.2),
    M(TEA, s[6] + 0.4, s[6] + 2.4, USC, kind="minuteman", soldiers=6, ships=False, until=en[6] + 0.3),
    M(LEX1, s[7] + 0.4, s[7] + 2.4, GBC, kind="line", soldiers=9, ships=False, until=s[7] + 3.0),
    M(MIN1, s[7] + 1.2, s[7] + 2.8, USC, kind="minuteman", soldiers=9, ships=False, until=en[7] + 0.3),
    M(LEX2, s[7] + 3.2, en[7] - 0.2, GBC, kind="line", soldiers=6, ships=False, until=en[7] + 0.3),
    M(BUNKB, s[8] + 0.4, s[8] + 2.2, GBC, kind="line", soldiers=9, sea_only=True, until=en[8] + 0.3),
    M(BUNKA, s[8] + 0.6, s[8] + 2.4, USC, kind="minuteman", soldiers=9, ships=False, until=en[8] + 0.3),
    M(WASH, s[9] + 0.4, s[9] + 2.2, (40, 60, 130), kind="minuteman", soldiers=9, ships=False, until=en[9] + 0.3),
    M(EVAC, s[9] + 2.6, en[9] - 0.2, GBC, kind="line", soldiers=3, sea_only=True, until=en[9] + 0.3),
    PP("washington", "GEORGE WASHINGTON", "CONTINENTAL ARMY", s[9] + 0.4, en[9] + 0.2),
    M(SF, s[10] + 0.4, s[10] + 2.6, SPC, kind="musketeer", soldiers=6, ships=False, until=en[10] + 0.3),
    PP("jefferson", "THOMAS JEFFERSON", "AUTHOR OF THE DECLARATION", s[11] + 0.4, en[11] + 0.2),
]
routes = [dict(pts=COOK, t0=s[4] + 0.4, t1=s[4] + 3.4, until=en[4] + 0.3, color=GOLD),
          dict(pts=EVAC, t0=s[9] + 2.6, t1=en[9] - 0.2, until=en[9] + 0.3, color=GOLD)]
SW = s[12] - 0.85
labels += WP.labels(A, 1770, T1, s[12])

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
    put(fr, glow_text("YEAR 1812", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("NAPOLEON MARCHES ON MOSCOW", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=17, dur=DUR, base_a="/home/claude/shortgen/hd_1770.png", base_b="/home/claude/shortgen/hd_1776.png",
           regions="/home/claude/shortgen/regions_ep17_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW, SW + 1.1, "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 2.2, 0.25), (s[3] + 2.8, 0.2), (s[6] + 2.4, 0.2), (s[7] + 2.4, 0.25),
                                              (s[8] + 2.2, 0.25), (s[11] + 3.4, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
