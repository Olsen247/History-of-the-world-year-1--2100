"""Episode 12 – Year 1498: Vasco da Gama reaches India by sea (Askia Muhammad, Columbus' 2nd voyage, Tordesillas, Charles VIII in Italy,
Savonarola's bonfire, John Cabot, da Gama's voyage round Africa to Calicut)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1498)
import world_data_1492 as A, world_data_1498 as B

S = eval(open("/home/claude/shortgen/vo_ep12/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (0, 25, 2950)
shots = [(21, -30, 1400), (12, 30, 2950), (-1.0, 15.8, 650), (-47, 22, 2300), (-38, 10, 2950), (11.5, 42.8, 800), (11.25, 43.8, 420),
         (-39, 48, 1550), (-14, 25, 1900), (-6, -18, 2600), (37.5, -14, 1500), (60, 3, 2100), WIDE]
keys = [(0.0, 21, -30, 2400), (0.3, 21, -30, 2400), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SWB = (s[8] - 0.85, s[8] + 0.3)
NAP = s[5] + 3.6          # Naples falls (February 1495) – ticker flips to 1495 here
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("naples_fr", NAP - 0.2, NAP + 1.8, until=en[5] + 0.3)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
labels = [lab(A, "PORTUGAL", t_in=T1, t_out=s[2] - 0.6), lab(A, "CASTILE", t_in=T1, t_out=s[2] - 0.6),
          lab(A, "SONGHAI EMPIRE", "SONGHAI\nEMPIRE", t_in=T1, t_out=s[2] - 0.6),
          lab(B, "SONGHAI EMPIRE", "SONGHAI\nEMPIRE", pos=(-1.6, 13.4), t_in=s[2] + 0.4, t_out=en[2]),
          lab(B, "FRANCE", pos=(3.5, 45.6), t_in=s[5], t_out=en[5]),
          lab(B, "KINGDOM OF NAPLES", "NAPLES", pos=(16.6, 40.2), t_in=s[5] + 0.8, t_out=NAP - 0.2)]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("GAO", (0.9, 16.9), s[2] + 0.4, en[2] + 0.2), ev("CÁDIZ", (-6.3, 34.8), s[3] + 0.4, s[3] + 3.0),
           ev("SPAIN", (-62.0, 12.0), s[4] + 2.6, en[4] + 0.2, (240, 160, 90)), ev("PORTUGAL", (-28.0, 12.0), s[4] + 2.6, en[4] + 0.2, (120, 210, 130)),
           ev("NAPLES", (15.6, 39.4), NAP, en[5] + 0.2), ev("FLORENCE", (11.3, 42.9), s[6] + 0.4, en[6] + 0.2),
           ev("BRISTOL", (-2.6, 50.6), s[7] + 0.3, s[7] + 2.6), ev("NEW FOUND\nLAND", (-49.0, 44.6), s[7] + 3.0, en[7] + 0.2),
           ev("LISBON", (-9.1, 37.6), s[8] + 0.3, s[8] + 2.8),
           ev("MALINDI", (43.6, -3.2), s[10] + 2.6, en[10] + 0.2), ev("CALICUT", (70.0, 6.5), s[11] + 2.0, en[11] + 0.2)]

ticker = [(0, 1498), (s[1], 1498), (s[1] + 1.3, 1492), (s[2], 1492), (s[2] + 0.6, 1493), (s[4], 1493), (s[4] + 0.6, 1494), (NAP - 0.6, 1494),
          (NAP, 1495), (s[6], 1495), (s[6] + 0.6, 1497), (s[10], 1497), (s[10] + 0.6, 1498), (DUR, 1498)]
RRED = (232, 64, 72); CYN = (110, 200, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1498", l2="AROUND AFRICA", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1492", GOLD), hd(2, "YEAR 1493", "ASKIA THE GREAT", GOLD), hd(3, "SEPTEMBER 1493", "COLUMBUS RETURNS", CYN),
            hd(4, "YEAR 1494", "SPLITTING THE WORLD", GOLD), hd(5, "YEAR 1494", "FRANCE INVADES ITALY"), hd(6, "YEAR 1497", "BONFIRE OF THE VANITIES"),
            hd(7, "JUNE 1497", "A NEW FOUND LAND", CYN), hd(8, "JULY 1497", "DA GAMA SETS SAIL", GRN), hd(9, "NOVEMBER 1497", "CAPE OF GOOD HOPE", GOLD),
            hd(10, "APRIL 1498", "A PILOT AT MALINDI", CYN), hd(11, "MAY 1498", "INDIA BY SEA", GOLD)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
PTC = (80, 150, 90); COL = (200, 120, 60); FRC = (70, 110, 200); ENC = (200, 70, 80)
HOOK = [(6.0, -31.0), (11.0, -35.0), (16.0, -36.6), (20.0, -36.4), (24.0, -35.2), (28.0, -33.9), (32.5, -31.0)]
COLUMBUS2 = [(-6.3, 36.5), (-9.5, 33.5), (-13.0, 30.0), (-16.3, 28.0), (-25, 24.0), (-35, 20.5), (-45, 17.8), (-55, 16.0), (-61.3, 15.4),
             (-64.5, 17.0), (-67.5, 18.1), (-70.0, 19.9), (-71.1, 19.95)]
TORD = [(-46.6, 50.0), (-46.6, 35.0), (-46.6, 20.0), (-46.6, 0.0), (-46.6, -20.0), (-46.6, -42.0)]
NAPLES = [(5.7, 45.2), (6.7, 44.9), (8.2, 44.9), (9.2, 44.4), (10.4, 43.7), (11.25, 43.77), (11.8, 43.0), (12.1, 42.4), (12.5, 41.9), (13.4, 41.4), (14.25, 40.85)]
CABOT = [(-2.6, 51.45), (-4.5, 51.3), (-10.5, 51.6), (-20, 52.4), (-30, 52.6), (-40, 51.8), (-48, 50.2), (-52.6, 48.9)]
GAMA1 = [(-9.15, 38.7), (-11.0, 35.5), (-15.5, 28.5), (-18.0, 21.0), (-23.5, 14.9), (-22.5, 8.0), (-21.0, 1.0)]
GAMA2 = [(-21.0, 1.0), (-22.5, -8.0), (-25.5, -17.0), (-26.0, -25.0), (-20.0, -31.5), (-8.0, -34.5), (5.0, -33.8), (17.9, -32.7),
         (18.0, -35.0), (20.0, -35.3), (22.2, -34.4)]
GAMA3 = [(22.2, -34.4), (27.0, -34.0), (31.5, -30.5), (33.5, -26.5), (36.2, -23.5), (36.8, -19.0), (41.2, -15.0), (41.2, -10.5), (40.9, -5.5),
         (40.6, -4.1), (40.9, -3.2)]
GAMA4 = [(40.9, -3.2), (45.0, -0.5), (53.0, 3.5), (61.0, 7.5), (68.0, 10.0), (73.0, 11.0), (75.75, 11.25)]
fx = [
    M(HOOK, 0.4, en[0] + 0.2, PTC, kind="knight", soldiers=4, sea_only=True, until=en[0] + 0.5),
    PP("dagama", "VASCO DA GAMA", "PORTUGUESE EXPLORER", 1.6, en[0] + 0.2),
    M([(-2.2, 16.6), (-1.2, 16.4), (-0.3, 16.3)], s[2] + 0.4, s[2] + 3.0, (230, 200, 120), kind="songhai"),
    M([(1.6, 16.0), (0.8, 16.2), (0.15, 16.27)], s[2] + 0.6, s[2] + 3.0, (200, 110, 60), kind="songhai", until=s[2] + 4.0),
    PP("askia", "ASKIA MUHAMMAD", "RULER OF SONGHAI", s[2] + 0.4, en[2] + 0.2),
    M(COLUMBUS2, s[3] + 0.3, en[3] - 0.2, COL, kind="conquistador", soldiers=7, sea_only=True, until=en[3] + 0.3),
    PP("columbus", "CHRISTOPHER COLUMBUS", "SECOND VOYAGE", s[3] + 0.4, en[3] + 0.2),
    M(NAPLES, s[5] + 0.3, NAP + 0.3, FRC, kind="french", soldiers=6, until=en[5] + 0.3),
    PP("charles8", "CHARLES VIII", "KING OF FRANCE", s[5] + 0.4, en[5] + 0.2, x=300),
    IC("fire", (11.1, 44.9), s[6] + 0.8, en[6] + 0.2),
    PP("savonarola", "SAVONAROLA", "PREACHER IN FLORENCE", s[6] + 0.4, en[6] + 0.2, x=300),
    M(CABOT, s[7] + 0.3, en[7] - 0.3, ENC, kind="longbow", soldiers=3, sea_only=True, until=en[7] + 0.3),
    PP("cabot", "JOHN CABOT", "SAILING FOR ENGLAND", s[7] + 0.4, en[7] + 0.2),
    M(GAMA1, s[8] + 0.3, en[8] + 0.2, PTC, kind="knight", soldiers=4, sea_only=True, until=s[9] + 0.6),
    PP("dagama", "VASCO DA GAMA", "PORTUGUESE EXPLORER", s[8] + 0.4, en[8] + 0.2),
    M(GAMA2, s[9] + 0.2, en[9] + 0.1, PTC, kind="knight", soldiers=4, sea_only=True, until=s[10] + 0.6),
    M(GAMA3, s[10] + 0.2, en[10] + 0.1, PTC, kind="knight", soldiers=4, sea_only=True, until=s[11] + 0.6),
    M(GAMA4, s[11] + 0.2, s[11] + 3.0, PTC, kind="knight", soldiers=4, sea_only=True, until=en[11] + 0.3),
    IC("spice", (79.0, 19.5), s[11] + 3.0, en[11] + 0.2),
    PP("dagama", "VASCO DA GAMA", "REACHES INDIA", s[11] + 0.4, en[11] + 0.2, x=300),
]
routes = [dict(pts=COLUMBUS2, t0=s[3] + 0.3, t1=en[3] - 0.2, until=en[3] + 0.3, color=GOLD),
          dict(pts=TORD, t0=s[4] + 0.6, t1=s[4] + 2.6, until=en[4] + 0.3, color=GOLD),
          dict(pts=CABOT, t0=s[7] + 0.3, t1=en[7] - 0.3, until=en[7] + 0.3, color=GOLD),
          dict(pts=GAMA1, t0=s[8] + 0.3, t1=en[8] + 0.2, until=en[11] + 0.3, color=GOLD),
          dict(pts=GAMA2, t0=s[9] + 0.2, t1=en[9] + 0.1, until=en[11] + 0.3, color=GOLD),
          dict(pts=GAMA3, t0=s[10] + 0.2, t1=en[10] + 0.1, until=en[11] + 0.3, color=GOLD),
          dict(pts=GAMA4, t0=s[11] + 0.2, t1=s[11] + 3.0, until=en[11] + 0.3, color=GOLD)]

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
    put(fr, glow_text("YEAR 1522", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("AROUND THE WORLD", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=12, dur=DUR, base_a="/home/claude/shortgen/hd_1492.png", base_b="/home/claude/shortgen/hd_1498.png",
           regions="/home/claude/shortgen/regions_ep12_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[4] + 2.6, 0.2), (NAP, 0.25), (s[6] + 0.8, 0.2), (s[11] + 3.0, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
