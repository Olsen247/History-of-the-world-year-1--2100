"""Episode 8 – Year 1347: the road to the Black Death."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_1279 as A, world_data_1347 as B

S = eval(open("/home/claude/shortgen/vo9_v3/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (20, 45, 2950)
shots = [(20, 48, 2300), (40, 40, 2700), (35.0, 32.9, 900), (30, 40, 1100), (12, 22, 2950), (-100, 21, 1300), (79, 22, 1900), (0, 49.5, 1300),
         (60, 45, 2950), (62, 45, 2600), (35.4, 45, 1100), (18, 44, 2600), WIDE]
keys = [(0.0, 20, 48, 2950), (0.3, 20, 48, 2950), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW1 = (s[9] - 0.9, s[9] + 0.3)
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [dict(key="acre", t0=s[2] + 1.4, t1=s[2] + 4.0, mode="shatter", origin=(35.07, 32.92), under="B", piece_src="A"),
           rv("ottoman", s[3] + 0.8, s[3] + 3.4), rv("mali", s[4] + 0.4, s[4] + 3.0), rv("delhi", s[6] + 0.3, s[6] + 3.6),
           dict(key="ilkhan_fall", t0=s[8] + 0.4, t1=s[8] + 3.4, mode="shatter", origin=(48, 35), under="B", piece_src="A"),
           rv("plague_steppe", s[9] + 0.8, s[9] + 5.2), rv("plague_eu", s[11] + 2.4, s[11] + 7.2)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if ("EMPIRE" in n or n in ("GOLDEN HORDE", "YUAN DYNASTY")) else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
labels = [lab(B, n, d, t_out=s[1]) for n, d in [("ENGLAND", None), ("FRANCE", None), ("HOLY ROMAN EMPIRE", "HOLY ROMAN\nEMPIRE"), ("CASTILE", None)]]
labels += [lab(A, "MAMLUK SULTANATE", "MAMLUK\nSULTANATE", t_in=T1), lab(A, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", t_in=T1, t_out=SW1[0]),
           lab(B, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", kind="small", t_in=SW1[1]),
           dict(text="CRUSADER\nSTATES", pos=(34.0, 33.6), kind="small", color=(235, 235, 240), t_in=T1, t_out=s[2] + 3.0),
           lab(A, "GOLDEN HORDE", "GOLDEN\nHORDE", t_in=T1), lab(A, "ILKHANATE", t_in=T1, t_out=s[8] + 2.0), lab(A, "CHAGATAI KHANATE", "CHAGATAI\nKHANATE", t_in=T1),
           lab(A, "YUAN DYNASTY", "YUAN\nDYNASTY", t_in=T1), lab(A, "DELHI SULTANATE", "DELHI\nSULTANATE", t_in=T1, t_out=s[6] + 0.4),
           lab(B, "DELHI SULTANATE", "DELHI\nSULTANATE", t_in=s[6] + 3.2), lab(A, "MALI EMPIRE", "MALI\nEMPIRE", t_in=T1, t_out=s[4] + 0.3),
           lab(B, "MALI EMPIRE", "MALI\nEMPIRE", t_in=s[4] + 2.6), lab(B, "OTTOMANS", t_in=s[3] + 3.0), lab(A, "RUS PRINCIPALITIES", "RUS\nPRINCIPALITIES", t_in=T1),
           lab(B, "ENGLAND", t_in=s[7]), lab(B, "FRANCE", t_in=s[7]), lab(B, "HOLY ROMAN EMPIRE", "HOLY ROMAN\nEMPIRE", t_in=s[7]),
           lab(B, "SERBIAN EMPIRE", "SERBIAN\nEMPIRE", kind="small", t_in=SW1[1]), lab(B, "ARAGON", t_in=s[11]), lab(B, "CASTILE", t_in=s[11]),
           lab(B, "POLAND", t_in=s[11]), lab(B, "HUNGARY", t_in=s[11]), lab(B, "LITHUANIA", t_in=s[11]),
           dict(text="Persian successor states", pos=(52, 33), kind="culture", t_in=s[8] + 3.0),
           dict(text="Anatolian beyliks", pos=(34, 38.5), kind="culture", t_in=s[3] + 3.0)]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("ACRE", (35.07, 32.45), s[2] + 0.4, en[2] + 0.2), ev("BURSA", (29.06, 39.7), s[3] + 2.6, en[3] + 0.2),
           ev("TIMBUKTU", (-3.0, 16.2), s[4] + 1.0, en[4] + 0.2), ev("CAIRO", (31.24, 29.55), s[4] + 3.2, en[4] + 0.2),
           ev("MECCA", (39.83, 20.9), s[4] + 4.4, en[4] + 0.2), ev("TENOCHTITLAN", (-99.13, 18.95), s[5] + 2.4, en[5] + 0.2),
           ev("DELHI", (77.2, 28.1), s[6] + 0.3, en[6] + 0.2), ev("CRECY", (1.93, 49.8), s[7] + 2.4, en[7] + 0.2),
           ev("CAFFA", (35.38, 44.6), s[10] + 0.6, en[10] + 0.2), ev("MESSINA", (15.55, 37.75), s[11] + 2.4, en[11] + 0.2),
           dict(text="BLACK DEATH", pos=(50, 50), kind="event", color=(255, 90, 90), t_in=s[9] + 3.6, t_out=en[9] + 0.3)]

ticker = [(0, 1347), (s[1], 1347), (s[1] + 1.3, 1279), (s[2], 1279), (s[2] + 0.6, 1291), (s[3], 1291), (s[3] + 0.6, 1299), (s[4], 1299),
          (s[4] + 0.6, 1324), (s[5], 1324), (s[5] + 0.6, 1325), (s[6], 1325), (s[6] + 0.6, 1335), (s[7], 1335), (s[7] + 0.6, 1337), (s[8], 1337),
          (s[8] + 0.6, 1340), (s[9], 1340), (s[9] + 0.6, 1343), (s[10], 1343), (s[10] + 0.6, 1346), (s[11], 1346), (s[11] + 0.6, 1347), (DUR, 1347)]
RRED = (232, 64, 72); BRN = (210, 170, 120); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1347", l2="THE BLACK DEATH", c2=RRED),
            hd(1, "LET'S GO BACK TO", "YEAR 1279", GOLD), hd(2, "YEAR 1291", "THE FALL OF ACRE"), hd(3, "YEAR 1299", "THE FIRST OTTOMANS"),
            hd(4, "YEAR 1324", "MANSA MUSA'S GOLD", GOLD), hd(5, "YEAR 1325", "TENOCHTITLAN", GRN), hd(6, "INDIA", "THE DELHI SULTANATE", GRN),
            hd(7, "YEAR 1337", "THE HUNDRED YEARS' WAR"), hd(8, "THE MONGOL EMPIRE", "FALLS APART", BRN), hd(9, "A SILENT KILLER", "THE PLAGUE"),
            hd(10, "YEAR 1346", "THE SIEGE OF CAFFA"), hd(11, "YEAR 1347", "THE BLACK DEATH")]

AYC = (200, 170, 70); OTC = (200, 60, 60); MLC = (210, 160, 60); DLC = (60, 140, 110); ENC = (200, 70, 80); FRC = (70, 110, 200); GHC = (190, 150, 60)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, 1180))
fx = [
    IC("rat", (31, 45.5), 1.6, en[0], scale=0.9),
    M([(34.8, 31.5), (35.0, 32.3), (35.07, 32.85)], s[2] + 0.2, s[2] + 1.6, AYC, kind="arab"),
    M([(30.18, 40.02), (29.5, 40.1), (29.06, 40.18)], s[3] + 1.0, s[3] + 3.0, OTC, kind="arab"),
    PP("osman", "OSMAN I", "FOUNDER OF THE OTTOMANS", s[3] + 0.6, en[3] + 0.2),
    M([(-8.5, 11.5), (-4, 16.8), (5, 20), (15, 23), (25, 27), (31.24, 30.05), (36, 27), (39.83, 21.42)], s[4] + 0.4, s[4] + 5.0, MLC, kind="arab", soldiers=4),
    IC("gold", (31.24, 31.0), s[4] + 3.4, en[4] + 0.2, count=2),
    PP("mansamusa", "MANSA MUSA", "KING OF MALI", s[4] + 0.4, en[4] + 0.2),
    M([(-104, 25.5), (-101.5, 22), (-99.8, 20.2), (-99.13, 19.43)], s[5] + 0.2, s[5] + 2.8, (40, 150, 120), kind="aztec"),
    IC("pyramid", (-99.13, 20.3), s[5] + 3.0, en[5] + 0.3),
    M([(77.2, 28.6), (76, 23), (76, 18), (78, 13)], s[6] + 0.3, s[6] + 3.6, DLC, kind="arab"),
    PP("tughluq", "MUHAMMAD BIN TUGHLUQ", "SULTAN OF DELHI", s[6] + 0.4, en[6] + 0.2),
    M([(-0.5, 51.2), (1.0, 50.5), (1.93, 50.25)], s[7] + 0.4, s[7] + 2.6, ENC, kind="knight"),
    M([(2.35, 48.85), (2.2, 49.6), (2.0, 50.1)], s[7] + 1.0, s[7] + 2.8, FRC, kind="knight"),
    PP("edward3", "EDWARD III", "KING OF ENGLAND", s[7] + 0.4, en[7] + 0.2),
    IC("rat", (68, 46.5), s[9] + 1.2, en[9] + 0.2),
    M([(40, 47.5), (37, 45.8), (35.6, 45.1)], s[10] + 0.3, s[10] + 2.4, GHC, kind="mongol"),
    IC("nopeople", (35.38, 45.6), s[10] + 3.0, en[10] + 0.2),
    PP("janibeg", "JANIBEG", "KHAN OF THE GOLDEN HORDE", s[10] + 0.6, en[10] + 0.2),
    M([(35.38, 44.9), (31, 43.4), (29.0, 41.1), (26.2, 40.0), (24, 37.2), (21, 36.3), (17, 37.0), (15.55, 38.19)], s[11] + 0.2, s[11] + 2.6,
      (200, 40, 60), kind="byzantine"),
    IC("nopeople", (15.55, 38.7), s[11] + 2.8, en[11] + 0.2),
]
routes = [dict(pts=[(116.4, 39.9), (98, 40), (88, 43.8), (76, 42.5), (67, 39.7), (58, 42), (50, 47), (45.5, 48.6), (40, 47.2), (35.38, 45.03),
                    (29, 41.0), (15, 38.5), (8.93, 44.4)], t0=s[8] + 2.6, t1=s[8] + 5.6, until=s[11], color=GOLD)]

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
    put(fr, glow_text("YEAR 1405", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE TREASURE FLEET", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=8, dur=DUR, base_a="/home/claude/shortgen/hd_1279.png", base_b="/home/claude/shortgen/hd_1347.png",
           extra_bases=dict(PL="/home/claude/shortgen/hd_1347p.png"),
           regions="/home/claude/shortgen/regions_ep08_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "PL", "A"), (SW1[0], SW1[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 1.4, 0.2), (s[8] + 0.4, 0.2), (s[11] + 2.4, 0.3), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
