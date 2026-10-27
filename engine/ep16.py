"""Episode 16 – Year 1770: James Cook in the Pacific (the Qing take Beijing 1644, Vienna 1683, Poltava 1709, Easter Island 1722,
Nader Shah sacks Delhi 1739, Bering reaches Alaska 1741, Plassey 1757, Quebec 1759, Tahiti and New Zealand 1769, Botany Bay 1770)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1770)
import world_data_1642 as A, world_data_1740 as N, world_data_1770 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep16/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10, 20, 2850)
shots = [(-95, -18, 2900), WIDE, (114.5, 38.0, 950), (17.6, 47.6, 700), (29.0, 54.5, 1150), (-96, -33, 1500), (73.5, 30.0, 1050),
         (-158, 56.5, 1300), (88.3, 23.4, 650), (-69.6, 47.6, 620), (-155, -22, 1100), (151.5, -30.0, 1350), WIDE]
EXTRA = {5: [(3.4, None), (4.4, (-109.4, -27.1, 330))], 7: [(4.0, None), (4.9, (168.5, 56.0, 1000))], 9: [(3.0, None), (3.9, (-80, 41, 2000))],
         10: [(2.6, None), (3.5, (172.5, -40.5, 1050))], 11: [(3.6, None), (4.5, (146.5, -17.5, 1250))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, -30, 10, 3000), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("qing_china", s[2] + 2.8, s[2] + 5.6), rv("baltic_ru", s[4] + 3.4, s[4] + 5.6),
           rv("bengal_eic", s[8] + 3.4, s[8] + 5.6), rv("canada_gb", s[9] + 3.9, s[9] + 6.2)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
labels = [lab(A, "MING DYNASTY", "MING\nDYNASTY", pos=(112.0, 33.5), t_in=s[2] + 0.3, t_out=s[2] + 3.2),
          lab(N, "QING EMPIRE", "QING\nEMPIRE", pos=(112.0, 33.5), t_in=s[2] + 4.2, t_out=en[2] + 0.2),
          lab(A, "OTTOMAN EMPIRE", "OTTOMAN\nEMPIRE", pos=(21.0, 45.7), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(A, "POLISH-LITHUANIAN COMMONWEALTH", "POLAND-\nLITHUANIA", kind="mid", pos=(21.5, 51.2), t_in=s[3] + 0.3, t_out=en[3] + 0.2),
          lab(A, "SWEDEN", pos=(16.0, 60.0), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(N, "TSARDOM OF RUSSIA", "RUSSIA", pos=(38.5, 56.0), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(N, "AFSHARID PERSIA", "PERSIA", pos=(64.5, 33.0), t_in=s[6] + 0.3, t_out=en[6] + 0.2),
          lab(N, "MUGHAL EMPIRE", "MUGHAL\nEMPIRE", pos=(81.0, 24.6), t_in=s[6] + 0.3, t_out=en[6] + 0.2),
          lab(N, "BENGAL", pos=(91.2, 25.3), t_in=s[8] + 0.3, t_out=s[8] + 3.6),
          lab(N, "FRANCE", "NEW FRANCE", pos=(-75.5, 49.6), t_in=s[9] + 0.3, t_out=s[9] + 3.8),
          lab(B, "GREAT BRITAIN", "BRITISH\nAMERICA", pos=(-80.0, 38.0), t_in=s[9] + 5.0, t_out=en[9] + 0.2),
          lab(B, "SPAIN", pos=(-100.0, 22.0), t_in=s[12] - 0.2, t_out=s[12] + 0.2)]
labels += [ev("BEIJING", (116.4, 40.5), s[2] + 0.4, en[2] + 0.2), ev("SHANHAI PASS", (121.6, 39.3), s[2] + 2.4, en[2] + 0.2, (240, 230, 200)),
           ev("VIENNA", (14.6, 48.3), s[3] + 0.4, en[3] + 0.2),
           ev("POLTAVA", (32.6, 48.5), s[4] + 1.6, en[4] + 0.2), ev("ST PETERSBURG", (31.0, 60.4), s[4] + 3.6, en[4] + 0.2, (240, 230, 200)),
           ev("EASTER ISLAND", (-109.4, -26.0), s[5] + 4.4, en[5] + 0.2),
           ev("DELHI", (77.2, 28.1), s[6] + 3.0, en[6] + 0.2),
           ev("ALASKA", (-150.0, 62.5), s[7] + 2.2, s[7] + 4.2), ev("BERING ISLAND", (166.2, 56.8), s[7] + 5.0, en[7] + 0.2),
           ev("PLASSEY", (86.5, 23.9), s[8] + 1.6, en[8] + 0.2), ev("CALCUTTA", (88.6, 22.3), s[8] + 0.4, en[8] + 0.2, (240, 230, 200)),
           ev("QUEBEC", (-72.4, 45.9), s[9] + 0.4, s[9] + 3.4),
           ev("TAHITI", (-149.4, -16.2), s[10] + 0.4, s[10] + 3.0), ev("NEW ZEALAND", (172.5, -36.5), s[10] + 4.0, en[10] + 0.2),
           ev("BOTANY BAY", (147.0, -34.5), s[11] + 2.0, s[11] + 3.8), ev("GREAT BARRIER REEF", (151.6, -18.0), s[11] + 4.6, en[11] + 0.2, WHITE),
           ev("NEW SOUTH WALES", (141.0, -31.0), s[11] + 5.4, en[11] + 0.2)]

ticker = [(0, 1770), (s[1], 1770), (s[1] + 1.3, 1642), (s[2], 1642), (s[2] + 0.6, 1644), (s[3], 1644), (s[3] + 0.6, 1683), (s[4], 1683),
          (s[4] + 0.6, 1709), (s[5], 1709), (s[5] + 0.6, 1722), (s[6], 1722), (s[6] + 0.6, 1739), (s[7], 1739), (s[7] + 0.6, 1741), (s[8], 1741),
          (s[8] + 0.6, 1757), (s[9], 1757), (s[9] + 0.6, 1759), (s[10], 1759), (s[10] + 0.6, 1769), (s[11], 1769), (s[11] + 0.6, 1770), (DUR, 1770)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150); ORG = (245, 150, 50)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1770", l2="CAPTAIN COOK", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1642", GOLD), hd(2, "YEAR 1644", "THE MING FALL", GOLD), hd(3, "SEPTEMBER 1683", "SIEGE OF VIENNA"),
            hd(4, "YEAR 1709", "POLTAVA", GRN), hd(5, "APRIL 1722", "EASTER ISLAND", ORG), hd(6, "YEAR 1739", "DELHI SACKED", GOLD),
            hd(7, "YEAR 1741", "BERING REACHES ALASKA", CYN), hd(8, "JUNE 1757", "PLASSEY"), hd(9, "SEPTEMBER 1759", "BATTLE OF QUEBEC", CYN),
            hd(10, "JUNE 1769", "TRANSIT OF VENUS", ORG), hd(11, "APRIL 1770", "BOTANY BAY", ORG)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
GBC = (200, 40, 50); NLC = (240, 140, 40); REB = (150, 60, 40); QGC = (225, 185, 70); OTC = (200, 60, 60); PLC = (220, 60, 60)
SWC = (60, 110, 200); RUC = (50, 130, 70); PSC = (60, 130, 160); MGC = (40, 150, 95); BGC = (150, 190, 110); FRC = (235, 235, 240)
ENDV1 = [(-4.1, 50.0), (-12, 42), (-17.5, 32), (-25, 15), (-32, 0), (-38, -15), (-43.2, -23.3), (-52, -36), (-62, -48), (-66.5, -55.3),
         (-75, -54.5), (-90, -45), (-110, -33), (-130, -24), (-149.4, -17.6)]
REBEL = [(108.9, 34.3), (110.5, 35.3), (112.5, 36.6), (113.8, 37.8), (115.0, 38.8), (116.1, 39.7)]
BANNER = [(122.5, 41.6), (121.0, 40.7), (119.8, 40.05), (118.6, 39.9), (117.4, 39.9), (116.6, 39.9)]
OTT = [(20.46, 44.82), (19.6, 45.9), (19.04, 47.5), (17.8, 47.9), (16.9, 48.1), (16.55, 48.2)]
HUS = [(19.94, 50.06), (19.0, 49.7), (18.0, 49.3), (17.0, 48.75), (16.4, 48.3)]
OTFLEE = [(16.6, 48.15), (17.6, 47.8), (18.9, 47.4), (19.5, 46.4)]
SWE = [(21.0, 52.2), (24.0, 53.3), (27.5, 53.9), (30.5, 52.8), (32.5, 51.2), (34.0, 50.0), (34.45, 49.62)]
RUS = [(37.6, 55.75), (36.8, 53.8), (36.2, 52.0), (35.4, 50.6), (34.7, 49.68)]
ROGG = [(-70, -54.5), (-77, -46), (-79.5, -37), (-80.0, -33.8), (-88, -31), (-97, -28.8), (-104, -27.6), (-109.2, -27.1)]
NADER = [(65.7, 31.6), (68.0, 33.5), (69.2, 34.5), (71.6, 34.0), (73.0, 33.6), (74.3, 31.5), (75.8, 30.6), (76.95, 29.75)]
NADER2 = [(76.95, 29.6), (77.1, 29.1), (77.2, 28.7)]
MUG = [(77.2, 28.6), (77.1, 29.1), (77.0, 29.55)]
GOLDBACK = [(77.2, 28.7), (75.8, 30.6), (74.3, 31.5), (71.6, 34.0), (69.2, 34.5)]
BER1 = [(-179.9, 52.6), (-173, 52.4), (-166, 53.8), (-158, 55.6), (-151, 57.8), (-146.5, 59.4), (-144.4, 59.9)]
BER2 = [(-145.2, 59.3), (-152, 57.0), (-162, 54.3), (-172, 52.6), (-179.9, 52.9)]
BER3 = [(179.9, 54.0), (175, 54.5), (170.5, 54.9), (167.2, 55.05), (166.3, 55.0)]
EIC = [(88.36, 22.57), (88.4, 22.95), (88.35, 23.3), (88.27, 23.62), (88.25, 23.76)]
NAW = [(88.27, 24.18), (88.28, 24.0), (88.27, 23.86)]
GBQ = [(-60.0, 46.6), (-63.5, 48.6), (-66.8, 49.25), (-69.0, 48.4), (-70.2, 47.5), (-70.9, 47.0), (-71.15, 46.82)]
FRQ = [(-71.35, 46.95), (-71.28, 46.86), (-71.24, 46.81)]
TAHITI = [(-149.4, -17.6), (-158, -24), (-168, -30), (-176, -35), (-179.9, -37.0)]
NZ = [(179.9, -37.6), (178.3, -38.7), (178.6, -37.6), (176.2, -37.3), (175.0, -36.0), (173.5, -34.3), (172.6, -34.5), (173.4, -35.6), (174.1, -37.2),
      (174.3, -39.3), (174.9, -41.2), (174.0, -41.8), (172.0, -42.2), (170.5, -43.3), (168.5, -44.4), (166.5, -45.7), (167.0, -47.3), (168.9, -46.8),
      (170.6, -45.9), (171.4, -44.3), (173.2, -43.4), (174.2, -41.7), (173.6, -40.9), (172.7, -40.5)]
COOK = [(172.7, -40.5), (165, -39.5), (157, -38.5), (150.6, -37.9), (150.4, -36.0), (151.2, -34.4), (151.25, -34.0)]
LAND = [(151.25, -34.0), (151.2, -34.0), (151.17, -34.0)]
REEF = [(151.3, -33.7), (153.2, -31.0), (153.6, -28.0), (153.0, -25.0), (151.0, -23.0), (149.5, -20.6), (147.5, -18.8), (146.3, -16.8), (145.6, -15.75)]
CLAIM = [(145.6, -15.75), (145.4, -14.5), (144.0, -13.0), (143.3, -11.6), (142.4, -10.7)]
fx = [
    M(ENDV1, 0.4, en[0] - 0.1, GBC, kind="line", soldiers=1, sea_only=True, until=en[0] + 0.4),
    PP("cook", "JAMES COOK", "BRITISH NAVY CAPTAIN", 2.4, en[0] + 0.2, x=300),
    M(REBEL, s[2] + 0.4, s[2] + 2.4, REB, kind="rebel", soldiers=9, ships=False, until=s[2] + 3.2),
    M(BANNER, s[2] + 2.2, s[2] + 4.2, QGC, kind="bannerman", soldiers=9, ships=False, until=en[2] + 0.3),
    M(OTT, s[3] + 0.4, s[3] + 2.6, OTC, kind="janissary", soldiers=9, ships=False, until=s[3] + 3.4),
    M(HUS, s[3] + 2.6, s[3] + 4.4, PLC, kind="wingedhussar", soldiers=6, ships=False, until=en[3] + 0.3),
    M(OTFLEE, s[3] + 4.2, en[3] - 0.2, OTC, kind="janissary", soldiers=6, ships=False, until=en[3] + 0.3),
    PP("sobieski", "JAN III SOBIESKI", "KING OF POLAND", s[3] + 0.4, en[3] + 0.2, x=300),
    M(SWE, s[4] + 0.4, s[4] + 2.6, SWC, kind="carolean", soldiers=9, ships=False, until=s[4] + 3.4),
    M(RUS, s[4] + 0.8, s[4] + 2.8, RUC, kind="line", soldiers=9, ships=False, until=en[4] + 0.3),
    PP("peter1", "PETER THE GREAT", "TSAR OF RUSSIA", s[4] + 0.4, en[4] + 0.2, x=300),
    M(ROGG, s[5] + 0.4, s[5] + 3.4, NLC, kind="dutch", soldiers=1, sea_only=True, until=en[5] + 0.3),
    M(NADER, s[6] + 0.4, s[6] + 2.6, PSC, kind="afsharid", soldiers=6, ships=False, until=s[6] + 3.0),
    M(MUG, s[6] + 1.0, s[6] + 2.6, MGC, kind="mughal", soldiers=6, ships=False, until=s[6] + 3.0),
    M(NADER2, s[6] + 2.6, s[6] + 3.4, PSC, kind="afsharid", soldiers=6, ships=False, until=s[6] + 4.0),
    IC("gold", (69.0, 33.6), s[6] + 3.6, en[6] + 0.2),
    PP("nader", "NADER SHAH", "SHAH OF PERSIA", s[6] + 0.4, en[6] + 0.2, x=300),
    M(BER1, s[7] + 0.4, s[7] + 2.6, RUC, kind="line", soldiers=1, sea_only=True, until=s[7] + 3.0),
    M(BER2, s[7] + 2.8, s[7] + 4.2, RUC, kind="line", soldiers=1, sea_only=True, until=s[7] + 4.4),
    M(BER3, s[7] + 4.6, s[7] + 5.8, RUC, kind="line", soldiers=1, sea_only=True, until=en[7] + 0.3),
    M(EIC, s[8] + 0.4, s[8] + 2.4, GBC, kind="sepoy", soldiers=6, ships=False, until=en[8] + 0.3),
    M(NAW, s[8] + 1.0, s[8] + 2.6, BGC, kind="mughal", soldiers=6, ships=False, until=s[8] + 3.2),
    PP("clive", "ROBERT CLIVE", "EAST INDIA COMPANY", s[8] + 0.4, en[8] + 0.2),
    M(GBQ, s[9] + 0.4, s[9] + 2.4, GBC, kind="line", soldiers=3, sea_only=True, until=s[9] + 2.6),
    M(FRQ, s[9] + 1.6, s[9] + 2.8, FRC, kind="line", soldiers=4, ships=False, until=s[9] + 3.2),
    PP("wolfe", "JAMES WOLFE", "BRITISH GENERAL", s[9] + 0.4, en[9] + 0.2),
    M(TAHITI, s[10] + 1.2, s[10] + 2.8, GBC, kind="line", soldiers=1, sea_only=True, until=s[10] + 3.0),
    M(NZ, s[10] + 3.6, en[10] - 0.1, GBC, kind="line", soldiers=1, sea_only=True, until=en[10] + 0.3),
    PP("cook", "JAMES COOK", "BRITISH NAVY CAPTAIN", s[10] + 0.4, en[10] + 0.2, x=300),
    M(COOK, s[11] + 0.3, s[11] + 2.0, GBC, kind="line", soldiers=1, sea_only=True, until=s[11] + 2.2),
    M(LAND, s[11] + 2.0, s[11] + 2.8, GBC, kind="line", soldiers=3, ships=False, until=s[11] + 3.6),
    M(REEF, s[11] + 3.0, s[11] + 4.8, GBC, kind="line", soldiers=1, sea_only=True, until=s[11] + 5.0),
    M(CLAIM, s[11] + 5.0, en[11] - 0.2, GBC, kind="line", soldiers=1, sea_only=True, until=en[11] + 0.3),
    PP("cook", "JAMES COOK", "BRITISH NAVY CAPTAIN", s[11] + 0.4, en[11] + 0.2),
]
routes = [dict(pts=ENDV1, t0=0.4, t1=en[0] - 0.1, until=en[0] + 0.5, color=GOLD),
          dict(pts=ROGG, t0=s[5] + 0.4, t1=s[5] + 3.4, until=en[5] + 0.3, color=GOLD),
          dict(pts=BER1, t0=s[7] + 0.4, t1=s[7] + 2.6, until=s[7] + 4.4, color=GOLD),
          dict(pts=BER3, t0=s[7] + 4.6, t1=s[7] + 5.8, until=en[7] + 0.3, color=GOLD),
          dict(pts=TAHITI, t0=s[10] + 1.2, t1=s[10] + 2.8, until=s[10] + 3.0, color=GOLD),
          dict(pts=NZ, t0=s[10] + 3.6, t1=en[10] - 0.1, until=en[10] + 0.3, color=GOLD),
          dict(pts=COOK + REEF[1:] + CLAIM[1:], t0=s[11] + 0.3, t1=en[11] - 0.2, until=en[11] + 0.3, color=GOLD)]
SW1, SW2 = s[5] - 0.85, s[10] - 0.85
labels += WP.labels(A, 1650, T1, SW1 + 0.4) + WP.labels(N, 1740, SW1 + 0.4, SW2 + 0.4) + WP.labels(B, 1770, SW2 + 0.4, s[12])

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
    put(fr, glow_text("YEAR 1776", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE UNITED STATES IS BORN", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=16, dur=DUR, base_a="/home/claude/shortgen/hd_1642.png", base_b="/home/claude/shortgen/hd_1770.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1740.png"),
           regions="/home/claude/shortgen/regions_ep16_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1, SW1 + 1.1, "A", "N"), (SW2, SW2 + 1.1, "N", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 4.2, 0.25), (s[3] + 4.4, 0.25), (s[4] + 2.8, 0.25), (s[6] + 3.4, 0.25),
                                              (s[8] + 2.6, 0.2), (s[9] + 2.8, 0.25), (s[11] + 2.8, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
