"""Episode 18 – Year 1812: Napoleon's empire and the march on Moscow (Peace of Paris 1783, First Fleet at Sydney 1788, the Bastille 1789,
third partition of Poland 1795, Napoleon in Egypt and the Battle of the Nile 1798, Louisiana Purchase 1803, Haiti and Napoleon's
coronation 1804, Trafalgar and Austerlitz 1805, the invasion of Russia June 1812, Moscow burns September 1812, the retreat)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1812)
import world_data_1776 as A, world_data_1795 as N, world_data_1812 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep18/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
shots = [(19.0, 52.0, 1700), WIDE, (-82.0, 39.0, 1300), (149.0, -36.0, 560), (2.35, 48.9, 450), (22.0, 52.5, 1050), (30.2, 31.0, 400),
         (-94.0, 38.0, 1500), (-72.6, 19.0, 320), (-7.0, 36.6, 420), (14.0, 50.0, 1500), (34.0, 55.2, 900), WIDE]
EXTRA = {8: [(3.2, None), (4.0, (2.35, 48.9, 500))], 9: [(3.0, None), (3.9, (16.8, 49.0, 520))], 10: [(3.0, None), (3.8, (30.5, 54.8, 1100))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, 5.0, 47.0, 2300), (2.2, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("us1783", s[2] + 2.6, s[2] + 5.6), rv("nsw", s[3] + 3.4, s[3] + 5.0),
           rv("pol_pr", s[5] + 1.6, s[5] + 4.0), rv("pol_at", s[5] + 2.0, s[5] + 4.2), rv("pol_ru", s[5] + 2.4, s[5] + 4.6),
           rv("louisiana", s[7] + 2.0, s[7] + 5.2), rv("haiti", s[8] + 0.8, s[8] + 2.8),
           rv("fr_emp", s[10] + 0.3, s[10] + 2.6), rv("confed", s[10] + 0.6, s[10] + 2.6), rv("swiss", s[10] + 0.8, s[10] + 2.2),
           rv("italy", s[10] + 0.8, s[10] + 2.4), rv("naples", s[10] + 1.0, s[10] + 2.6), rv("warsaw", s[10] + 1.2, s[10] + 2.8),
           rv("ru_fin", s[10] + 1.4, s[10] + 3.0)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
CYN = (110, 200, 230); WT = (240, 230, 200)
labels = [lab(B, "FRENCH EMPIRE", "FRENCH\nEMPIRE", kind="emp", pos=(2.0, 47.0), t_in=0.6, t_out=en[0] + 0.2),
          lab(B, "RUSSIAN EMPIRE", "RUSSIAN\nEMPIRE", pos=(40.0, 62.5), t_in=0.6, t_out=en[0] + 0.2),
          lab(N, "UNITED STATES", "UNITED\nSTATES", pos=(-84.5, 38.5), t_in=s[2] + 4.0, t_out=en[2] + 0.2),
          lab(N, "GREAT BRITAIN", "BRITISH\nCANADA", kind="mid", pos=(-79.0, 47.2), t_in=s[2] + 0.3, t_out=en[2] + 0.2),
          lab(N, "SPAIN", "SPANISH\nFLORIDA", kind="mid", pos=(-82.6, 28.4), t_in=s[2] + 0.3, t_out=en[2] + 0.2),
          lab(A, "SPAIN", "SPANISH\nLOUISIANA", kind="mid", pos=(-97.0, 40.5), t_in=s[2] + 0.3, t_out=en[2] + 0.2),
          lab(A, "POLISH-LITHUANIAN COMMONWEALTH", "POLAND-\nLITHUANIA", kind="mid", pos=(22.5, 52.0), t_in=s[5] + 0.3, t_out=s[5] + 2.6),
          lab(N, "RUSSIAN EMPIRE", "RUSSIA", pos=(33.5, 56.6), t_in=s[5] + 0.3, t_out=en[5] + 0.2),
          lab(N, "PRUSSIA", pos=(13.8, 53.3), t_in=s[5] + 0.3, t_out=en[5] + 0.2),
          lab(N, "HABSBURG MONARCHY", "AUSTRIA", pos=(17.0, 48.0), t_in=s[5] + 0.3, t_out=en[5] + 0.2),
          lab(B, "UNITED STATES", "UNITED\nSTATES", pos=(-84.0, 37.0), t_in=s[7] + 0.3, t_out=en[7] + 0.2),
          lab(B, "HAITI", pos=(-72.9, 19.35), t_in=s[8] + 2.6, t_out=s[8] + 3.5),
          lab(B, "FRENCH EMPIRE", pos=(2.0, 47.0), t_in=s[10] + 1.6, t_out=s[10] + 3.2),
          lab(B, "CONFEDERATION OF THE RHINE", "RHINE\nCONFEDERATION", kind="mid", pos=(9.6, 50.7), t_in=s[10] + 1.8, t_out=s[10] + 3.2),
          lab(B, "DUCHY OF WARSAW", "WARSAW", kind="mid", pos=(20.6, 52.3), t_in=s[10] + 2.0, t_out=s[10] + 3.2),
          lab(B, "KINGDOM OF ITALY", "ITALY", kind="mid", pos=(11.3, 45.1), t_in=s[10] + 2.0, t_out=s[10] + 3.2),
          lab(B, "KINGDOM OF NAPLES", "NAPLES", kind="mid", pos=(15.9, 40.7), t_in=s[10] + 2.0, t_out=s[10] + 3.2),
          lab(B, "RUSSIAN EMPIRE", "RUSSIAN\nEMPIRE", pos=(31.0, 57.5), t_in=s[10] + 1.6, t_out=s[10] + 3.2)]
labels += [ev("MISSISSIPPI", (-91.8, 36.2), s[2] + 4.4, en[2] + 0.2, CYN), ev("SYDNEY COVE", (146.0, -32.5), s[3] + 3.2, en[3] + 0.2),
           ev("BASTILLE", (2.35, 47.75), s[4] + 2.0, en[4] + 0.2),
           ev("WARSAW", (21.0, 52.5), s[5] + 3.2, en[5] + 0.2, WT),
           ev("ALEXANDRIA", (27.0, 31.0), s[6] + 0.4, s[6] + 3.0, WT), ev("CAIRO", (30.0, 29.3), s[6] + 1.4, s[6] + 3.0),
           ev("BATTLE OF THE NILE", (32.2, 33.9), s[6] + 4.4, en[6] + 0.2, CYN),
           ev("NEW ORLEANS", (-90.0, 29.3), s[7] + 0.6, en[7] + 0.2, WT), ev("LOUISIANA", (-99.0, 42.0), s[7] + 3.4, en[7] + 0.2),
           ev("PARIS", (2.35, 49.25), s[8] + 4.0, en[8] + 0.2, WT),
           ev("TRAFALGAR", (-7.0, 35.3), s[9] + 1.2, s[9] + 3.3, CYN), ev("VIENNA", (16.37, 47.4), s[9] + 3.9, en[9] + 0.2, WT),
           ev("AUSTERLITZ", (13.0, 49.7), s[9] + 4.6, en[9] + 0.2),
           ev("BORODINO", (36.5, 57.8), s[10] + 5.4, en[10] + 0.2), ev("MOSCOW", (44.8, 55.75), s[11] + 0.4, en[11] + 0.2, WT),
           ev("BEREZINA", (27.5, 52.4), s[11] + 4.2, en[11] + 0.2, CYN)]

ticker = [(0, 1812), (s[1], 1812), (s[1] + 1.3, 1776), (s[2], 1776), (s[2] + 0.6, 1783), (s[3], 1783), (s[3] + 0.6, 1788), (s[4], 1788),
          (s[4] + 0.6, 1789), (s[5], 1789), (s[5] + 0.6, 1795), (s[6], 1795), (s[6] + 0.6, 1798), (s[7], 1798), (s[7] + 0.6, 1803), (s[8], 1803),
          (s[8] + 0.6, 1804), (s[9], 1804), (s[9] + 0.6, 1805), (s[10], 1805), (s[10] + 0.6, 1812), (DUR, 1812)]
RRED = (232, 64, 72); GRN = (110, 210, 150); ORG = (245, 150, 50)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1812", l2="NAPOLEON'S EMPIRE", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1776", GOLD), hd(2, "YEAR 1783", "PEACE OF PARIS", CYN), hd(3, "YEAR 1788", "THE FIRST FLEET", CYN),
            hd(4, "JULY 1789", "THE BASTILLE FALLS"), hd(5, "YEAR 1795", "POLAND VANISHES", GRN), hd(6, "YEAR 1798", "NAPOLEON IN EGYPT", ORG),
            hd(7, "YEAR 1803", "LOUISIANA PURCHASE", GOLD), hd(8, "YEAR 1804", "FREEDOM AND A CROWN", GOLD),
            hd(9, "YEAR 1805", "TRAFALGAR & AUSTERLITZ", CYN), hd(10, "JUNE 1812", "INVASION OF RUSSIA"), hd(11, "SEPTEMBER 1812", "MOSCOW BURNS", ORG)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
FRC = (50, 80, 180); GBC = (200, 40, 50); RUC = (40, 120, 60); PRC = (40, 50, 100); ATC = (240, 240, 240); HTC = (40, 50, 140); MMC = (200, 60, 60)
COC = (150, 30, 40); SCC = (60, 60, 140)
HOOK = [(2.35, 48.86), (7.0, 50.0), (13.0, 52.0), (19.0, 53.0), (24.0, 54.8), (30.0, 54.8), (37.6, 55.75)]
GBLEAVE = [(-74.0, 40.55), (-72.0, 40.4), (-69.0, 40.6), (-65.0, 41.2)]
FLEET = [(140.0, -40.5), (146.0, -40.0), (150.5, -38.0), (151.3, -34.6), (151.25, -33.86)]
SANS1 = [(1.2, 49.6), (1.8, 49.2), (2.33, 48.88)]
SANS2 = [(3.6, 49.3), (3.0, 49.05), (2.4, 48.87)]
RUP = [(31.0, 54.5), (28.5, 54.0), (26.5, 53.5), (24.5, 53.0)]
PRP = [(17.5, 52.6), (18.7, 52.4), (19.8, 52.3), (21.0, 52.23)]
ATP = [(19.9, 50.06), (21.0, 50.6), (22.0, 51.0), (22.6, 51.25)]
FREG = [(29.9, 31.2), (30.4, 30.8), (30.9, 30.4), (31.13, 30.05)]
MAM = [(31.6, 29.7), (31.4, 29.88), (31.2, 30.0)]
NEL = [(27.5, 34.0), (28.6, 33.0), (29.6, 32.0), (30.07, 31.38)]
HAIT = [(-73.3, 18.4), (-72.8, 18.9), (-72.4, 19.4)]
FRLEAVE = [(-72.2, 19.85), (-72.0, 20.4), (-71.5, 21.2)]
GBF = [(-8.6, 37.0), (-7.4, 36.5), (-6.3, 36.15)]
FRF = [(-6.3, 36.5), (-6.6, 36.3), (-6.45, 36.12)]
AUSF = [(16.37, 48.21), (16.5, 48.6), (16.65, 48.95), (16.76, 49.12)]
AUSR = [(17.6, 49.6), (17.2, 49.35), (16.9, 49.18)]
AUSA = [(17.4, 48.85), (17.1, 49.02), (16.88, 49.13)]
GA = [(23.9, 54.9), (26.0, 54.9), (28.0, 54.8), (30.4, 54.8), (32.0, 54.9), (34.0, 55.2), (35.82, 55.52)]
RUD = [(37.6, 55.75), (37.0, 55.65), (36.2, 55.55)]
RET = [(37.4, 55.7), (35.8, 55.5), (33.0, 55.0), (30.4, 54.6), (28.5, 54.3), (26.5, 54.5)]
COS = [(36.5, 54.6), (33.5, 54.3), (30.8, 54.2), (28.7, 54.1)]
fx = [
    M(HOOK, 0.4, en[0] - 0.1, FRC, kind="napoleonic", soldiers=6, ships=False, until=en[0] + 0.4),
    PP("napoleon", "NAPOLEON BONAPARTE", "EMPEROR OF THE FRENCH", 1.6, en[0] + 0.2),
    M(GBLEAVE, s[2] + 0.4, s[2] + 2.6, GBC, kind="line", soldiers=2, sea_only=True, until=en[2] + 0.3),
    PP("washington", "GEORGE WASHINGTON", "CONTINENTAL ARMY", s[2] + 0.4, en[2] + 0.2, x=300),
    M(FLEET, s[3] + 0.4, s[3] + 3.4, GBC, kind="line", soldiers=3, sea_only=True, until=en[3] + 0.3),
    PP("phillip", "ARTHUR PHILLIP", "GOVERNOR OF NEW SOUTH WALES", s[3] + 0.4, en[3] + 0.2),
    M(SANS1, s[4] + 0.4, s[4] + 2.2, SCC, kind="sansculotte", soldiers=6, ships=False, until=en[4] + 0.3),
    M(SANS2, s[4] + 0.6, s[4] + 2.2, SCC, kind="sansculotte", soldiers=6, ships=False, until=en[4] + 0.3),
    M(RUP, s[5] + 0.4, s[5] + 2.2, RUC, kind="line", soldiers=6, ships=False, until=en[5] + 0.3),
    M(PRP, s[5] + 0.8, s[5] + 2.4, PRC, kind="grenadier", soldiers=6, ships=False, until=en[5] + 0.3),
    M(ATP, s[5] + 1.2, s[5] + 2.8, ATC, kind="line", soldiers=6, ships=False, until=en[5] + 0.3),
    PP("catherine", "CATHERINE THE GREAT", "EMPRESS OF RUSSIA", s[5] + 0.4, en[5] + 0.2),
    M(FREG, s[6] + 0.4, s[6] + 2.6, FRC, kind="napoleonic", soldiers=6, ships=False, until=en[6] + 0.3),
    M(MAM, s[6] + 1.0, s[6] + 2.6, MMC, kind="mamluk", soldiers=5, ships=False, until=s[6] + 3.4),
    M(NEL, s[6] + 3.0, s[6] + 5.0, GBC, kind="napoleonic", soldiers=3, sea_only=True, until=en[6] + 0.3),
    IC("fire", (30.1, 31.33), s[6] + 5.0, en[6] + 0.2),
    PP("napoleon", "NAPOLEON BONAPARTE", "FRENCH GENERAL", s[6] + 0.4, s[6] + 3.1, x=300),
    PP("nelson", "HORATIO NELSON", "BRITISH ADMIRAL", s[6] + 3.0, en[6] + 0.2),
    IC("gold", (-90.1, 30.6), s[7] + 0.8, s[7] + 3.2),
    PP("jefferson", "THOMAS JEFFERSON", "PRESIDENT OF THE UNITED STATES", s[7] + 0.4, en[7] + 0.2, x=300),
    M(HAIT, s[8] + 0.4, s[8] + 2.0, HTC, kind="haitian", soldiers=6, ships=False, until=s[8] + 3.2),
    M(FRLEAVE, s[8] + 1.6, s[8] + 3.1, FRC, kind="napoleonic", soldiers=2, sea_only=True, until=s[8] + 3.3),
    PP("dessalines", "JEAN-JACQUES DESSALINES", "LEADER OF HAITI", s[8] + 0.4, s[8] + 3.4, x=300),
    PP("napoleon_emp", "NAPOLEON I", "EMPEROR OF THE FRENCH", s[8] + 3.8, en[8] + 0.2),
    M(GBF, s[9] + 0.4, s[9] + 2.2, GBC, kind="napoleonic", soldiers=3, sea_only=True, until=s[9] + 3.2),
    M(FRF, s[9] + 0.6, s[9] + 2.2, FRC, kind="napoleonic", soldiers=3, sea_only=True, until=s[9] + 3.2),
    PP("nelson", "HORATIO NELSON", "KILLED AT TRAFALGAR", s[9] + 0.4, s[9] + 3.2, x=300),
    M(AUSF, s[9] + 4.0, s[9] + 5.8, FRC, kind="napoleonic", soldiers=9, ships=False, until=en[9] + 0.3),
    M(AUSR, s[9] + 4.2, s[9] + 5.8, RUC, kind="napoleonic", soldiers=6, ships=False, until=en[9] + 0.3),
    M(AUSA, s[9] + 4.3, s[9] + 5.8, ATC, kind="napoleonic", soldiers=6, ships=False, until=en[9] + 0.3),
    PP("napoleon_emp", "NAPOLEON I", "EMPEROR OF THE FRENCH", s[9] + 4.0, en[9] + 0.2),
    M(GA, s[10] + 3.8, en[10] - 0.2, FRC, kind="napoleonic", soldiers=9, ships=False, until=en[10] + 0.3),
    M(RUD, s[10] + 5.0, en[10] - 0.1, RUC, kind="napoleonic", soldiers=6, ships=False, until=en[10] + 0.3),
    PP("napoleon", "NAPOLEON I", "EMPEROR OF THE FRENCH", s[10] + 3.6, en[10] + 0.2, x=300),
    IC("fire", (37.6, 55.75), s[11] + 0.8, en[11] + 0.2),
    M(RET, s[11] + 2.4, en[11] - 0.2, FRC, kind="napoleonic", soldiers=3, ships=False, until=en[11] + 0.3),
    M(COS, s[11] + 3.0, en[11] - 0.1, COC, kind="cossack", soldiers=4, ships=False, until=en[11] + 0.3),
    PP("napoleon", "NAPOLEON I", "EMPEROR OF THE FRENCH", s[11] + 0.4, s[11] + 2.5, x=300),
    PP("kutuzov", "MIKHAIL KUTUZOV", "RUSSIAN COMMANDER", s[11] + 2.4, en[11] + 0.2),
]
routes = [dict(pts=FLEET, t0=s[3] + 0.4, t1=s[3] + 3.4, until=en[3] + 0.3, color=GOLD),
          dict(pts=NEL, t0=s[6] + 3.0, t1=s[6] + 5.0, until=en[6] + 0.3, color=GOLD),
          dict(pts=GBF, t0=s[9] + 0.4, t1=s[9] + 2.2, until=s[9] + 3.2, color=GOLD)]
SW1 = s[6] - 0.85; SW2 = s[12] - 0.85
labels += WP.labels(N, 1795, T1, s[12])

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
    put(fr, glow_text("YEAR 1825", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("A FREE LATIN AMERICA", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=18, dur=DUR, base_a="/home/claude/shortgen/hd_1776.png", base_b="/home/claude/shortgen/hd_1812.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1795.png"),
           regions="/home/claude/shortgen/regions_ep18_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1, SW1 + 1.1, "A", "N"), (SW2, SW2 + 1.1, "N", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 2.6, 0.2), (s[4] + 2.2, 0.25), (s[5] + 1.6, 0.2), (s[6] + 2.6, 0.25),
                                              (s[6] + 5.0, 0.2), (s[8] + 3.8, 0.25), (s[9] + 2.2, 0.2), (s[9] + 5.8, 0.25), (s[10] + 0.4, 0.2),
                                              (s[11] + 0.8, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
