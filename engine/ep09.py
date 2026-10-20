"""Episode 9 – Year 1405: Zheng He's treasure fleet (Ming China, Timur, the end of the Yuan)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1405)
import world_data_1347 as A, world_data_1405 as B

S = eval(open("/home/claude/shortgen/vo_ep09/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (40, 40, 2950)
shots = [(114, 26, 2300), (75, 40, 2950), (115, 33, 1200), (113, 36, 1900), (63, 38, 1900), (38.5, 53, 1100), (23.5, 42, 1150),
         (14, 61, 2300), (72, 31, 1900), (36, 40, 1300), (92, 38, 2800), (98, 14, 2900), WIDE]
keys = [(0.0, 116, 28, 2600), (0.3, 116, 28, 2600), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SWB = (s[10] - 0.85, s[10] + 0.3)
rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
reveals = [dict(key="yuan_fall", t0=s[3] + 0.3, t1=s[3] + 2.8, mode="shatter", origin=(116.4, 39.9), under="N", piece_src="A"),
           rv("ming", s[3] + 1.6, s[3] + 5.0), rv("timurid", s[4] + 0.6, s[4] + 5.0), rv("ottoman", s[6] + 0.4, s[6] + 3.0),
           dict(key="serbia_fall", t0=s[6] + 3.0, t1=s[6] + 5.0, mode="shatter", origin=(21.0, 42.0), under="B", piece_src="A"),
           rv("kalmar", s[7] + 0.3, s[7] + 4.5),
           dict(key="delhi_fall", t0=s[8] + 2.6, t1=s[8] + 5.0, mode="shatter", origin=(77.2, 28.6), under="B", piece_src="A"),
           rv("vijaya", s[8] + 2.8, s[8] + 4.8)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if ("EMPIRE" in n or n in ("GOLDEN HORDE", "YUAN DYNASTY", "MING DYNASTY")) else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
labels = [lab(B, "MING DYNASTY", "MING\nDYNASTY", t_out=s[1]), lab(B, "JOSEON", kind="small", t_out=s[1])]
labels += [lab(A, "YUAN DYNASTY", "YUAN\nDYNASTY", t_in=T1, t_out=s[3] + 0.4), lab(A, "CHAGATAI KHANATE", "CHAGATAI\nKHANATE", t_in=T1, t_out=s[4] + 0.5),
           lab(A, "GOLDEN HORDE", "GOLDEN\nHORDE", t_in=T1), lab(A, "DELHI SULTANATE", "DELHI\nSULTANATE", t_in=T1, t_out=s[4]), lab(A, "DELHI SULTANATE", "DELHI\nSULTANATE", t_in=en[4], t_out=s[8] + 2.6),
           lab(A, "MAMLUK SULTANATE", "MAMLUK\nSULTANATE", t_in=T1, t_out=s[6]), lab(A, "MAMLUK SULTANATE", "MAMLUK\nSULTANATE", t_in=en[7]), lab(A, "GORYEO", kind="small", t_in=T1, t_out=s[7]),
           lab(A, "RUS PRINCIPALITIES", "RUS\nPRINCIPALITIES", t_in=T1, t_out=s[5]), lab(A, "LITHUANIA", t_in=s[5], t_out=en[6]),
           lab(A, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", kind="small", t_in=s[6], t_out=s[6] + 1.2),
           lab(A, "SERBIAN EMPIRE", "SERBIAN\nEMPIRE", kind="small", t_in=s[6], t_out=s[6] + 3.0),
           lab(A, "HUNGARY", t_in=s[6], t_out=en[6]),
           lab(A, "DENMARK", t_in=s[7], t_out=s[7] + 0.6), lab(A, "NORWAY", t_in=s[7], t_out=s[7] + 0.6), lab(A, "SWEDEN", t_in=s[7], t_out=s[7] + 0.6),
           dict(text="Persian successor states", pos=(53, 33), kind="culture", t_in=T1, t_out=s[4] + 1.0),
           lab(B, "NORTHERN YUAN", "NORTHERN\nYUAN", t_in=s[3] + 3.0), lab(B, "MING DYNASTY", "MING\nDYNASTY", t_in=s[3] + 4.2),
           lab(B, "TIMURID EMPIRE", "TIMURID\nEMPIRE", t_in=s[4] + 5.2), lab(B, "MOGHULISTAN", t_in=s[4] + 3.8),
           dict(text="OTTOMAN\nEMPIRE", pos=(28.3, 41.3), kind="emp", color=(200, 60, 60), t_in=s[6] + 4.2, t_out=s[9]), dict(text="OTTOMAN\nEMPIRE", pos=(28.3, 41.3), kind="emp", color=(200, 60, 60), t_in=en[9]), lab(B, "SERBIAN DESPOTATE", "SERBIA", kind="small", t_in=s[6] + 4.6, t_out=s[9]),
           lab(B, "KALMAR UNION", "KALMAR\nUNION", t_in=s[7] + 3.0), lab(B, "BAHMANI SULTANATE", "BAHMANI\nSULTANATE", kind="small", t_in=s[8] + 4.6, t_out=s[10]),
           lab(B, "VIJAYANAGARA", kind="small", t_in=s[8] + 4.6, t_out=s[10]), lab(B, "DELHI SULTANATE", "DELHI", kind="small", t_in=s[8] + 4.8, t_out=s[11]),
           lab(B, "JOSEON", kind="small", t_in=s[10])]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [dict(text="RED TURBANS", pos=(116, 31.0), kind="event", color=(255, 90, 90), t_in=s[2] + 1.6, t_out=en[2] + 0.2),
           ev("NANJING", (118.8, 31.2), s[3] + 0.6, en[3] + 0.2), ev("KHANBALIQ", (116.4, 40.9), s[3] + 0.6, en[3] + 0.2),
           ev("SAMARKAND", (66.97, 40.6), s[4] + 0.4, en[4] + 0.2), ev("MOSCOW", (37.62, 56.4), s[5] + 0.3, en[5] + 0.2),
           ev("KULIKOVO", (41.0, 54.2), s[5] + 2.4, en[5] + 0.2), ev("KOSOVO", (21.1, 43.2), s[6] + 2.4, s[6] + 4.0),
           ev("KALMAR", (16.36, 56.0), s[7] + 0.3, en[7] + 0.2), ev("DELHI", (77.2, 27.6), s[8] + 2.0, en[8] + 0.2),
           ev("ANKARA", (34.0, 37.7), s[9] + 2.2, en[9] + 0.2), ev("OTRAR", (68.3, 43.9), s[10] + 3.6, en[10] + 0.2),
           ev("NANJING", (119.8, 30.0), s[10] + 1.8, en[10] + 0.2), ev("MALACCA", (102.25, 1.4), s[11] + 3.2, en[11] + 0.2),
           ev("CALICUT", (75.78, 12.2), s[11] + 5.0, en[11] + 0.3)]

ticker = [(0, 1405), (s[1], 1405), (s[1] + 1.3, 1347), (s[2], 1347), (s[2] + 0.6, 1351), (s[3], 1351), (s[3] + 0.6, 1368), (s[4], 1368),
          (s[4] + 0.6, 1370), (s[5], 1370), (s[5] + 0.6, 1380), (s[6], 1380), (s[6] + 0.6, 1389), (s[7], 1389), (s[7] + 0.6, 1397), (s[8], 1397),
          (s[8] + 0.6, 1398), (s[9], 1398), (s[9] + 0.6, 1402), (s[10] + 3.4, 1402), (s[10] + 4.0, 1405), (DUR, 1405)]
RRED = (232, 64, 72); BRN = (210, 170, 120); GRN = (110, 210, 150); CYN = (110, 200, 230)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 1405", l2="THE TREASURE FLEET", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1347", GOLD), hd(2, "YEAR 1351", "THE RED TURBANS"), hd(3, "YEAR 1368", "THE MING DYNASTY", GOLD),
            hd(4, "YEAR 1370", "TIMUR RISES", CYN), hd(5, "YEAR 1380", "BATTLE OF KULIKOVO"), hd(6, "YEAR 1389", "BATTLE OF KOSOVO"),
            hd(7, "YEAR 1397", "THE KALMAR UNION", CYN), hd(8, "YEAR 1398", "THE SACK OF DELHI"), hd(9, "YEAR 1402", "BATTLE OF ANKARA"),
            hd(10, "YEAR 1402", "A NEW EMPEROR", GOLD), hd(11, "YEAR 1405", "ZHENG HE SETS SAIL", GOLD)]

MNC = (215, 70, 60); MONGC = (150, 105, 60); TMC = (90, 150, 170); OTC = (200, 60, 60); RUC = (120, 170, 90); GHC = (190, 150, 60); SRC = (180, 70, 90)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
SAM = (66.97, 39.65)
FLEET = [(121.1, 31.5), (122.6, 29.5), (120.5, 25.5), (117.5, 22.6), (113, 19.5), (111.0, 15.5), (110.0, 11.5), (107.5, 7.0), (105.0, 3.2), (104.4, 1.3),
         (103.2, 1.15), (101.5, 2.4), (100.8, 2.9), (98.5, 5.0), (96.2, 6.4), (94, 6.6), (87, 6.0), (82, 5.3), (80.5, 5.4), (78.5, 7.2), (76.2, 8.6), (75.6, 11.3)]
fx = [
    M(FLEET[:7], 0.5, en[0] - 0.2, MNC, kind="han", ship="junk", soldiers=6, until=en[0] + 0.4),
    M([(116.5, 32.9), (115.5, 33.9), (114.4, 34.8)], s[2] + 0.3, s[2] + 2.8, (210, 50, 50), kind="redturban"),
    M([(116.5, 32.9), (117.6, 32.4), (118.6, 32.1)], s[2] + 0.8, s[2] + 3.3, (210, 50, 50), kind="redturban"),
    M([(118.8, 32.05), (117.2, 35), (116.4, 39.6)], s[3] + 0.8, s[3] + 3.6, MNC, kind="han"),
    M([(116.4, 40.3), (114, 42.3), (111, 44.8)], s[3] + 2.6, s[3] + 4.8, MONGC, kind="mongol"),
    PP("hongwu", "ZHU YUANZHANG", "FIRST MING EMPEROR", s[3] + 0.5, en[3] + 0.2),
    M([SAM, (61, 37), (57, 36.3), (53, 35.7)], s[4] + 0.6, s[4] + 4.0, TMC, kind="timurid"),
    PP("timur", "TIMUR", "CONQUEROR OF CENTRAL ASIA", s[4] + 0.4, en[4] + 0.2),
    M([(37.62, 55.75), (38.0, 54.8), (38.55, 53.85)], s[5] + 0.3, s[5] + 2.8, RUC, kind="rus"),
    M([(40.5, 49.0), (39.6, 51.5), (38.85, 53.4)], s[5] + 0.3, s[5] + 2.8, GHC, kind="mongol"),
    PP("dmitry", "DMITRY DONSKOY", "GRAND PRINCE OF MOSCOW", s[5] + 0.4, en[5] + 0.2),
    M([(26.56, 41.68), (23.4, 42.05), (21.35, 42.6)], s[6] + 0.3, s[6] + 2.8, OTC, kind="janissary"),
    M([(21.33, 43.58), (21.2, 43.2), (21.15, 42.85)], s[6] + 0.8, s[6] + 2.8, SRC, kind="serb"),
    PP("murad", "MURAD I", "OTTOMAN SULTAN", s[6] + 0.4, en[6] + 0.2, x=300),
    PP("lazar", "PRINCE LAZAR", "RULER OF SERBIA", s[6] + 0.7, en[6] + 0.2),
    PP("margaret", "MARGARET I", "QUEEN OF THE UNION", s[7] + 0.4, en[7] + 0.2, x=300),
    M([SAM, (69.2, 34.5), (71.6, 33.6), (74.4, 31.5), (77.0, 28.8)], s[8] + 0.2, s[8] + 2.6, TMC, kind="timurid"),
    IC("fire", (79.0, 30.0), s[8] + 2.6, en[8] + 0.2),
    M([(44, 39.6), (38.5, 39.7), (33.4, 39.95)], s[9] + 0.3, s[9] + 2.6, TMC, kind="timurid"),
    M([(29.06, 40.18), (31.0, 40.0), (32.3, 39.93)], s[9] + 0.6, s[9] + 2.6, OTC, kind="janissary"),
    PP("bayezid", "BAYEZID I", "OTTOMAN SULTAN, CAPTURED", s[9] + 0.4, en[9] + 0.2),
    M([(116.4, 39.9), (117.2, 35.5), (118.6, 32.4)], s[10] + 0.3, s[10] + 2.4, MNC, kind="han"),
    PP("yongle", "ZHU DI", "THE YONGLE EMPEROR", s[10] + 0.4, en[10] + 0.2),
    M([SAM, (67.5, 41.3), (68.2, 42.6)], s[10] + 2.4, s[10] + 4.4, TMC, kind="timurid", until=en[10] + 0.2),
    M(FLEET, s[11] + 0.3, en[11] + 0.2, MNC, kind="han", ship="junk", soldiers=6, until=DUR),
    PP("zhenghe", "ZHENG HE", "ADMIRAL OF THE FLEET", s[11] + 0.4, en[11] + 0.2, x=820, y=1480),
    IC("gold", (65, 6.5), s[11] + 5.2, en[11] + 0.3),
]
routes = [dict(pts=FLEET, t0=s[11] + 0.3, t1=en[11] + 0.2, until=DUR, color=GOLD)]

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
    put(fr, glow_text("YEAR 1453", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("CONSTANTINOPLE", 52, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=9, dur=DUR, base_a="/home/claude/shortgen/hd_1347.png", base_b="/home/claude/shortgen/hd_1405.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1368.png"),
           regions="/home/claude/shortgen/regions_ep09_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SWB[0], SWB[1], "A", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[3] + 0.3, 0.2), (s[6] + 3.0, 0.2), (s[8] + 2.6, 0.25), (s[9] + 2.4, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
