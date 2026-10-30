"""Episode 20 – Year 1900: the age of empires (Liverpool-Manchester railway + France in Algiers 1830, First Opium War and Hong Kong 1842,
Mexican Cession + California gold 1848, Indian revolt 1857 and Crown rule 1858, Suez Canal 1869, German Empire proclaimed at Versailles 1871,
Berlin Conference 1884-85 and the Scramble for Africa, Adwa 1896, Spanish-American War 1898, Boxer Uprising and the relief of Beijing 1900)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1900)
import world_data_1825 as A, world_data_1882 as M, world_data_1900 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep20/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (10.0, 28.0, 2850)
shots = [(95.0, 5.0, 2850), WIDE, (-2.6, 53.4, 420), (113.8, 23.4, 520), (-106.0, 33.0, 1300), (80.0, 23.0, 1150), (32.4, 30.4, 380),
         (6.0, 50.0, 900), (18.0, 3.0, 2400), (39.0, 13.6, 520), (130.0, 14.0, 1100), (116.9, 39.5, 420), (60.0, 22.0, 2850)]
EXTRA = {2: [(3.0, None), (3.8, (3.0, 41.0, 1150))], 3: [(3.3, None), (4.1, (114.15, 22.35, 260))], 6: [(2.6, None), (3.6, (42.0, 4.0, 2700))],
         7: [(3.6, None), (4.4, (2.2, 48.8, 600))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, 18.0, 4.0, 2000), (3.0, 20.0, 2.0, 1750), (5.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

SWM = s[8] - 0.85; SWB = s[11] - 0.85
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("algeria", s[2] + 4.0, s[2] + 6.0, SWM + 1.2), rv("hk", s[3] + 4.0, s[3] + 5.0, SWM + 1.2),
           rv("uswest", s[4] + 0.8, s[4] + 3.6, SWM + 1.2), rv("india", s[5] + 3.6, s[5] + 6.6, SWM + 1.2),
           rv("germany", s[7] + 0.6, s[7] + 2.8, SWM + 1.2), rv("italy", s[7] + 1.0, s[7] + 3.0, SWM + 1.2), rv("belgium", s[2] + 4.0, s[2] + 5.0, SWM + 1.2),
           rv("af_fr", s[8] + 2.6, s[8] + 5.4, SWB + 1.2), rv("af_gb", s[8] + 2.8, s[8] + 5.6, SWB + 1.2), rv("af_gb2", s[8] + 3.6, s[8] + 5.0, SWB + 1.2),
           rv("af_de", s[8] + 3.2, s[8] + 5.4, SWB + 1.2), rv("af_cg", s[8] + 3.4, s[8] + 5.2, SWB + 1.2),
           rv("af_pt", s[8] + 3.6, s[8] + 5.4, SWB + 1.2), rv("af_it", s[8] + 3.8, s[8] + 5.4, SWB + 1.2),
           rv("af_es", s[8] + 4.0, s[8] + 5.4, SWB + 1.2), rv("phil", s[10] + 2.6, s[10] + 4.6, SWB + 1.2),
           rv("pr", s[10] + 2.6, s[10] + 4.0, SWB + 1.2)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
CYN = (110, 200, 230); WT = (240, 230, 200)
H0 = en[0] + 0.2
GB = "BRITISH EMPIRE"
labels = [lab(B, "FRENCH EMPIRE", "FRENCH\nAFRICA", pos=(0.0, 18.0), t_in=0.5, t_out=3.4),
          lab(B, GB, "BRITISH", kind="mid", pos=(30.0, 14.0), t_in=0.7, t_out=3.4),
          lab(B, GB, "BRITISH", kind="mid", pos=(28.5, -16.0), t_in=0.9, t_out=3.4),
          lab(B, "CONGO FREE STATE", "CONGO\nFREE STATE", kind="mid", pos=(23.5, -3.0), t_in=0.9, t_out=3.4),
          lab(B, "GERMAN EMPIRE", "GERMAN", kind="mid", pos=(35.0, -6.5), t_in=1.1, t_out=3.4),
          lab(B, "ETHIOPIA", kind="small", pos=(39.0, 8.5), t_in=1.3, t_out=3.4),
          lab(B, GB, "BRITISH INDIA", kind="emp", pos=(78.5, 22.0), t_in=4.6, t_out=H0),
          lab(B, GB, "BRITISH\nAUSTRALIA", kind="emp", pos=(134.0, -25.0), t_in=4.8, t_out=H0),
          lab(B, "QING EMPIRE", pos=(104.0, 33.5), t_in=5.0, t_out=H0),
          # 1830
          lab(A, "FRANCE", pos=(2.2, 46.8), t_in=s[2] + 4.0, t_out=en[2] + 0.2),
          lab(B, "FRENCH EMPIRE", "FRENCH\nALGERIA", kind="mid", pos=(2.0, 32.8), t_in=s[2] + 5.0, t_out=en[2] + 0.2),
          lab(A, "MOROCCO", kind="small", pos=(-6.0, 32.5), t_in=s[2] + 4.4, t_out=en[2] + 0.2),
          # 1842
          lab(A, "QING EMPIRE", pos=(112.5, 26.5), t_in=s[3] + 0.6, t_out=s[3] + 3.4),
          # 1848
          lab(B, "UNITED STATES", "UNITED\nSTATES", pos=(-99.0, 39.5), t_in=s[4] + 3.0, t_out=en[4] + 0.2),
          lab(A, "MEXICO", pos=(-101.5, 23.5), t_in=s[4] + 0.4, t_out=en[4] + 0.2),
          # 1857
          lab(B, GB, "BRITISH INDIA", kind="emp", pos=(79.0, 21.0), t_in=s[5] + 5.6, t_out=en[5] + 0.2),
          # 1871
          lab(B, "GERMAN EMPIRE", "GERMAN\nEMPIRE", pos=(10.5, 51.2), t_in=s[7] + 2.4, t_out=s[7] + 3.8),
          lab(B, "ITALY", pos=(12.6, 42.6), t_in=s[7] + 2.6, t_out=s[7] + 3.8),
          lab(B, "AUSTRIA-HUNGARY", "AUSTRIA-\nHUNGARY", kind="mid", pos=(17.5, 47.6), t_in=s[7] + 2.6, t_out=s[7] + 3.8),
          lab(A, "FRANCE", pos=(2.0, 46.6), t_in=s[7] + 2.0, t_out=en[7] + 0.2),
          # 1884: the scramble
          lab(B, "FRENCH EMPIRE", "FRENCH", pos=(1.0, 17.0), t_in=s[8] + 5.0, t_out=en[8] + 0.2),
          lab(B, GB, "BRITISH", kind="mid", pos=(8.0, 9.5), t_in=s[8] + 5.2, t_out=en[8] + 0.2),
          lab(B, GB, "BRITISH", kind="emp", pos=(27.5, -18.0), t_in=s[8] + 5.2, t_out=en[8] + 0.2),
          lab(B, "GERMAN EMPIRE", "GERMAN", kind="mid", pos=(36.0, -8.0), t_in=s[8] + 5.3, t_out=en[8] + 0.2),
          lab(B, "GERMAN EMPIRE", "GERMAN", kind="mid", pos=(17.5, -22.0), t_in=s[8] + 5.3, t_out=en[8] + 0.2),
          lab(B, "CONGO FREE STATE", "CONGO\nFREE STATE", kind="mid", pos=(22.5, -1.5), t_in=s[8] + 5.4, t_out=en[8] + 0.2),
          lab(B, "PORTUGAL", "PORTUGUESE", kind="small", pos=(17.5, -12.0), t_in=s[8] + 5.5, t_out=en[8] + 0.2),
          lab(B, "ETHIOPIA", kind="small", pos=(39.5, 8.0), t_in=s[8] + 5.6, t_out=en[8] + 0.2),
          lab(B, "LIBERIA", kind="small", pos=(-9.4, 6.4), t_in=s[8] + 5.6, t_out=en[8] + 0.2),
          lab(B, "OTTOMAN EMPIRE", "OTTOMAN", kind="small", pos=(18.0, 28.0), t_in=s[8] + 5.6, t_out=en[8] + 0.2),
          # 1896
          lab(B, "ETHIOPIA", pos=(39.6, 11.8), t_in=s[9] + 4.0, t_out=en[9] + 0.2),
          lab(B, "ITALY", "ITALIAN\nERITREA", kind="small", pos=(38.0, 16.4), t_in=s[9] + 0.6, t_out=en[9] + 0.2),
          # 1898
          lab(B, "UNITED STATES", "AMERICAN\nPHILIPPINES", kind="mid", pos=(129.5, 12.0), t_in=s[10] + 4.0, t_out=en[10] + 0.2),
          lab(B, "FRENCH EMPIRE", "FRENCH\nINDOCHINA", kind="small", pos=(105.0, 15.5), t_in=s[10] + 0.8, t_out=en[10] + 0.2),
          # 1900
          lab(B, "QING EMPIRE", pos=(114.5, 37.6), kind="mid", t_in=s[11] + 0.4, t_out=en[11] + 0.2)]
labels += [ev("MANCHESTER", (-2.1, 53.95), s[2] + 0.6, s[2] + 3.0, WT), ev("LIVERPOOL", (-3.1, 52.95), s[2] + 0.6, s[2] + 3.0, WT),
           ev("ALGIERS", (5.6, 36.7), s[2] + 4.0, en[2] + 0.2),
           ev("CANTON", (113.26, 23.4), s[3] + 0.6, s[3] + 3.4, WT), ev("HONG KONG", (114.17, 22.62), s[3] + 4.2, en[3] + 0.2),
           ev("CALIFORNIA", (-118.5, 35.4), s[4] + 3.6, en[4] + 0.2, CYN), ev("MEXICO CITY", (-99.13, 20.2), s[4] + 0.8, s[4] + 3.4, WT),
           ev("DELHI", (77.2, 29.4), s[5] + 0.6, en[5] + 0.2), ev("SUEZ CANAL", (33.3, 30.6), s[6] + 0.4, s[6] + 3.0),
           ev("PARIS", (2.35, 49.2), s[7] + 2.0, s[7] + 4.0, WT), ev("VERSAILLES", (2.13, 48.6), s[7] + 4.4, en[7] + 0.2),
           ev("BERLIN", (13.4, 53.2), s[8] + 0.4, s[8] + 2.8, WT),
           ev("ADWA", (37.9, 13.8), s[9] + 1.6, en[9] + 0.2), ev("MANILA", (121.0, 15.2), s[10] + 2.2, en[10] + 0.2, WT),
           ev("GUAM", (144.8, 14.2), s[10] + 4.4, en[10] + 0.2, WT),
           ev("BEIJING", (116.2, 40.5), s[11] + 0.4, en[11] + 0.2), ev("TIANJIN", (117.7, 38.75), s[11] + 0.6, en[11] + 0.2, WT)]

ticker = [(0, 1900), (s[1], 1900), (s[1] + 1.3, 1825), (s[2], 1825), (s[2] + 0.6, 1830), (s[3], 1830), (s[3] + 0.6, 1842), (s[4], 1842),
          (s[4] + 0.6, 1848), (s[5], 1848), (s[5] + 0.6, 1857), (s[5] + 4.0, 1857), (s[5] + 4.6, 1858), (s[6], 1858), (s[6] + 0.6, 1869),
          (s[7], 1869), (s[7] + 0.6, 1871), (s[8], 1871), (s[8] + 0.6, 1884), (s[8] + 2.6, 1884), (s[8] + 3.2, 1885), (s[8] + 5.0, 1885),
          (s[8] + 6.4, 1890), (s[9], 1890), (s[9] + 0.6, 1896), (s[10], 1896), (s[10] + 0.6, 1898), (s[11], 1898), (s[11] + 0.6, 1900), (DUR, 1900)]
RRED = (232, 64, 72); GRN = (110, 210, 150); ORG = (245, 150, 50); PNK = (240, 140, 175)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1900", l2="THE AGE OF EMPIRES", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1825", GOLD), hd(2, "YEAR 1830", "RAILWAYS AND ALGERIA", CYN), hd(3, "YEAR 1842", "THE OPIUM WAR"),
            hd(4, "YEAR 1848", "GOLD IN CALIFORNIA", GOLD), hd(5, "YEAR 1857", "REVOLT IN INDIA"), hd(6, "YEAR 1869", "THE SUEZ CANAL", CYN),
            hd(7, "YEAR 1871", "ONE GERMANY", GOLD), hd(8, "YEAR 1884", "THE SCRAMBLE FOR AFRICA", PNK), hd(9, "YEAR 1896", "ADWA", GRN),
            hd(10, "YEAR 1898", "AMERICA'S EMPIRE", CYN), hd(11, "YEAR 1900", "THE BOXER UPRISING")]

M_ = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
VH = lambda kind, path, a, b, **kw: dict(type="vehicle", kind=kind, path=path, t0=a, t1=b, **kw)
FRC = (50, 80, 180); GBC = (200, 40, 50); USC = (40, 70, 150); QGC = (220, 180, 40); DEC = (50, 55, 70); ITC = (30, 50, 110); ETC = (200, 40, 40)
KHK = (170, 150, 100)
RAIL = [(-2.98, 53.41), (-2.75, 53.43), (-2.5, 53.47), (-2.24, 53.48)]
TOULON = [(5.9, 43.1), (5.3, 41.0), (4.2, 38.8), (3.1, 37.2), (2.95, 36.85)]
CANTON_GB = [(116.0, 21.2), (114.6, 21.9), (113.9, 22.4), (113.6, 22.8), (113.3, 23.1)]
VERA = [(-96.13, 19.2), (-97.1, 19.3), (-98.2, 19.04), (-98.9, 19.3), (-99.13, 19.43)]
MEERUT = [(77.7, 29.0), (77.5, 28.85), (77.35, 28.7), (77.2, 28.62)]
GB_DELHI = [(75.8, 31.0), (76.5, 30.0), (77.0, 29.2), (77.18, 28.72)]
SUEZ = [(32.3, 31.3), (32.32, 30.8), (32.4, 30.3), (32.55, 29.95), (33.0, 29.0), (34.5, 27.0), (38.0, 21.0), (41.0, 15.5), (43.4, 12.6),
        (46.0, 12.4), (55.0, 15.0), (65.0, 18.0), (72.8, 18.9)]
CAPE = [(-6.0, 36.0), (-12.0, 30.0), (-18.5, 21.0), (-18.0, 13.0), (-14.0, 5.0), (-2.0, 3.0), (8.0, -2.0), (11.5, -14.0), (15.0, -30.0),
        (19.0, -36.5), (26.0, -35.5), (33.0, -30.0), (40.5, -21.0), (42.5, -12.0), (50.0, -2.0), (60.0, 9.0), (72.8, 18.9)]
DE_PARIS = [(8.0, 49.0), (6.5, 48.95), (5.0, 48.9), (3.5, 48.88), (2.6, 48.86)]
DE_PARIS2 = [(7.0, 50.2), (5.5, 49.8), (4.2, 49.3), (2.9, 49.0)]
FR_DEF = [(2.35, 48.86), (3.4, 49.1), (4.4, 49.2)]
ADWA_IT = [(38.93, 15.33), (38.95, 14.95), (38.92, 14.55), (38.9, 14.2)]
ADWA_ET = [(39.5, 13.2), (39.3, 13.6), (39.05, 13.95), (38.92, 14.12)]
DEWEY = [(114.3, 22.2), (116.5, 19.5), (119.0, 16.5), (120.4, 14.6), (120.85, 14.55)]
TJ_BJ = [(117.2, 39.12), (116.95, 39.4), (116.7, 39.65), (116.45, 39.88)]
TJ_BJ2 = [(117.3, 39.0), (117.05, 39.32), (116.75, 39.6), (116.5, 39.86)]
BOXERS = [(115.4, 39.2), (115.8, 39.55), (116.15, 39.8), (116.36, 39.9)]
fx = [
    PP("victoria", "QUEEN VICTORIA", "EMPRESS OF INDIA", 3.6, en[0] + 0.2, x=300),
    VH("train", RAIL, s[2] + 0.5, s[2] + 3.0, until=s[2] + 3.8),
    dict(type="cities", cities=[(-2.24, 53.48, 1.0), (-2.98, 53.41, 0.9)], t0=s[2] + 0.3, t1=s[2] + 1.2, until=s[2] + 3.6),
    M_(TOULON, s[2] + 3.9, s[2] + 5.6, FRC, kind="napoleonic", soldiers=6, ships=True, until=en[2] + 0.3),
    M_(CANTON_GB, s[3] + 0.4, s[3] + 3.0, GBC, kind="redcoat", soldiers=6, sea_only=True, until=s[3] + 3.6),
    M_([(113.0, 23.6), (113.2, 23.3), (113.3, 23.15)], s[3] + 1.6, s[3] + 3.0, QGC, kind="bannerman", soldiers=6, ships=False, until=s[3] + 3.4),
    M_(VERA, s[4] + 0.6, s[4] + 2.6, USC, kind="rifleman", soldiers=6, ships=False, until=s[4] + 3.2),
    IC("gold", (-120.9, 38.8), s[4] + 3.8, en[4] + 0.2),
    M_(MEERUT, s[5] + 0.5, s[5] + 2.6, (200, 40, 40), kind="sepoy", soldiers=6, ships=False, until=s[5] + 3.6),
    M_(GB_DELHI, s[5] + 2.2, s[5] + 3.6, GBC, kind="redcoat", soldiers=6, ships=False, until=s[5] + 4.0),
    PP("victoria", "QUEEN VICTORIA", "QUEEN OF THE UNITED KINGDOM", s[5] + 4.2, en[5] + 0.2),
    VH("steamer", SUEZ, s[6] + 0.6, s[6] + 6.0, until=en[6] + 0.3),
    PP("lesseps", "FERDINAND DE LESSEPS", "BUILDER OF THE CANAL", s[6] + 0.4, s[6] + 3.4, x=300),
    M_(DE_PARIS, s[7] + 0.5, s[7] + 3.0, DEC, kind="pickelhaube", soldiers=6, ships=False, until=s[7] + 4.0),
    M_(DE_PARIS2, s[7] + 0.7, s[7] + 3.0, DEC, kind="pickelhaube", soldiers=6, ships=False, until=s[7] + 4.0),
    M_(FR_DEF, s[7] + 1.2, s[7] + 2.4, FRC, kind="rifleman", soldiers=4, ships=False, until=s[7] + 3.0),
    PP("bismarck", "OTTO VON BISMARCK", "CHANCELLOR", s[7] + 0.4, en[7] + 0.2, x=300),
    PP("wilhelm1", "WILHELM I", "GERMAN EMPEROR", s[7] + 3.8, en[7] + 0.2),
    PP("bismarck", "OTTO VON BISMARCK", "HOST IN BERLIN", s[8] + 0.4, s[8] + 3.0, x=300),
    PP("leopold2", "LEOPOLD II", "KING OF THE BELGIANS", s[8] + 1.0, s[8] + 3.0),
    M_(ADWA_IT, s[9] + 0.6, s[9] + 2.6, ITC, kind="bersagliere", soldiers=6, ships=False, until=s[9] + 3.4),
    M_(ADWA_ET, s[9] + 0.8, s[9] + 3.0, ETC, kind="ethiopian", soldiers=9, ships=False, until=en[9] + 0.3),
    PP("menelik", "MENELIK II", "EMPEROR OF ETHIOPIA", s[9] + 0.4, en[9] + 0.2, x=300),
    M_(DEWEY, s[10] + 0.4, s[10] + 2.6, USC, kind="rifleman", soldiers=3, sea_only=True, until=s[10] + 3.2),
    PP("mckinley", "WILLIAM McKINLEY", "PRESIDENT OF THE UNITED STATES", s[10] + 0.4, en[10] + 0.2, x=300),
    M_(BOXERS, s[11] + 0.4, s[11] + 2.2, (200, 40, 40), kind="boxer", soldiers=6, ships=False, until=s[11] + 2.8),
    M_(TJ_BJ, s[11] + 2.2, s[11] + 4.6, KHK, kind="rifleman", soldiers=6, ships=False, until=en[11] + 0.3),
    M_(TJ_BJ2, s[11] + 2.4, s[11] + 4.8, DEC, kind="pickelhaube", soldiers=6, ships=False, until=en[11] + 0.3),
]
routes = [dict(pts=CAPE, t0=s[6] + 3.6, t1=s[6] + 5.0, until=en[6] + 0.3, color=(200, 200, 210)),
          dict(pts=SUEZ, t0=s[6] + 0.6, t1=s[6] + 6.0, until=en[6] + 0.3, color=GOLD),
          dict(pts=DEWEY, t0=s[10] + 0.4, t1=s[10] + 2.6, until=s[10] + 3.6, color=GOLD)]
labels += WP.labels(A, 1830, s[1] + 0.8, SWM, skip=())
labels += WP.labels(M, 1884, SWM + 1.1, s[8] + 2.6)
labels += WP.labels(B, 1896, s[9], SWB)
labels += WP.labels(B, 1900, SWB + 1.1, s[12])

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
    put(fr, glow_text("YEAR 1911", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE RACE TO THE SOUTH POLE", 46, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=20, dur=DUR, base_a="/home/claude/shortgen/hd_1825.png", base_b="/home/claude/shortgen/hd_1900.png",
           extra_bases=dict(M="/home/claude/shortgen/hd_1882.png"),
           regions="/home/claude/shortgen/regions_ep20_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWM, SWM + 1.1, "A", "M"), (SWB, SWB + 1.1, "M", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 4.0, 0.2), (s[3] + 4.0, 0.2), (s[4] + 0.8, 0.2), (s[5] + 3.6, 0.25),
                                              (s[6] + 0.6, 0.2), (s[7] + 0.6, 0.25), (s[8] + 2.6, 0.25), (s[9] + 2.6, 0.25), (s[10] + 2.6, 0.2),
                                              (s[11] + 2.2, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
