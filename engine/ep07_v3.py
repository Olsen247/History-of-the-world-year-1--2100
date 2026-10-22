"""Episode 7 – Year 1279: Normans, Crusades and the Mongol storm."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_1000 as A, world_data_1279 as B, world_data_1100 as C1, world_data_1190 as C2, world_data_1227 as M1, world_data_1259 as M2

S = eval(open("/home/claude/shortgen/vo8_v3/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.3, 2)
WIDE = (75, 42, 2950)
shots = [(95, 42, 2700), (20, 45, 2600), (0, 51, 900), (20, 43, 2300), (35, 31.8, 1000), (104, 46, 1700), (85, 41, 2800), (30, 50, 2000),
         (47, 34, 1500), (35.4, 32.2, 1000), (113, 31, 1900), (64, 39, 2950), WIDE]
keys = [(0.0, 95, 42, 2950), (0.3, 95, 42, 2950), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW1 = (s[5] - 0.9, s[5] + 0.3); SW2 = (s[7] - 0.9, s[7] + 0.3); SW3 = (s[9] - 0.9, s[9] + 0.2); SW4 = (s[11] - 0.9, s[11] + 0.2)
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("normans", s[2] + 2.6, s[2] + 5.2, SW1[1]), rv("crusade", s[3] + 4.4, s[3] + 7.2, SW1[1]),
           rv("ayyubid", s[4] + 0.2, s[4] + 2.4, SW1[1]),
           dict(key="cfall", t0=s[4] + 2.6, t1=s[4] + 5.2, mode="shatter", origin=(35.22, 31.78), under="C2", piece_src="C1", until=SW1[1]),
           rv("mongolia", s[5] + 1.0, s[5] + 4.6, SW2[1]), rv("m_east", s[6] + 0.3, s[6] + 3.0, SW2[1]), rv("m_west", s[6] + 1.2, s[6] + 5.6, SW2[1]),
           rv("horde", s[7] + 0.4, s[7] + 3.4, SW3[1]), rv("ilkhan", s[8] + 0.6, s[8] + 3.4, SW3[1]),
           rv("song", s[10] + 2.6, s[10] + 5.8, 1e9)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if ("EMPIRE" in n or "CALIPHATE" in n or n in ("YUAN DYNASTY", "GOLDEN HORDE")) else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

T1 = s[1] + 0.8
labels = [lab(B, "YUAN DYNASTY", "YUAN\nDYNASTY", t_out=s[1]), lab(B, "GOLDEN HORDE", "GOLDEN\nHORDE", t_out=s[1]),
          lab(B, "CHAGATAI KHANATE", "CHAGATAI\nKHANATE", t_out=s[1]), lab(B, "ILKHANATE", t_out=s[1])]
labels += [lab(A, "KINGDOM OF ENGLAND", "ENGLAND", t_in=T1, t_out=s[2] + 3.2), lab(A, "KINGDOM OF FRANCE", "FRANCE", t_in=T1, t_out=s[5]),
           lab(A, "HOLY ROMAN EMPIRE", "HOLY ROMAN\nEMPIRE", t_in=T1, t_out=s[5]), lab(A, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", t_in=T1, t_out=s[5]),
           lab(A, "FATIMID CALIPHATE", "FATIMID\nCALIPHATE", t_in=T1, t_out=s[4] + 0.4), lab(A, "KIEVAN RUS", "KIEVAN\nRUS", t_in=T1, t_out=s[7] + 3.0),
           dict(text="NORMAN\nENGLAND", pos=(-1.6, 52.4), kind="mid", color=(220, 180, 70), t_in=s[2] + 4.6, t_out=s[5]),
           dict(text="CRUSADER\nSTATES", pos=(37.4, 34.6), kind="mid", color=(235, 235, 240), t_in=s[3] + 6.6, t_out=s[4] + 2.8),
           lab(C2, "AYYUBID SULTANATE", "AYYUBID\nSULTANATE", t_in=s[4] + 2.0, t_out=s[9]),
           dict(text="Mongol tribes", pos=(104, 47.5), kind="culture", t_in=s[5], t_out=s[5] + 3.4),
           lab(C2, "JIN DYNASTY", "JIN\nDYNASTY", t_in=s[5] + 0.2, t_out=s[6] + 2.6), lab(C2, "WESTERN XIA", t_in=s[5] + 0.2, t_out=s[6] + 2.0),
           lab(C2, "SOUTHERN SONG", "SOUTHERN\nSONG", t_in=s[5] + 0.2, t_out=s[10] + 5.4), lab(C2, "QARA KHITAI", t_in=s[5] + 0.2, t_out=s[6] + 3.0),
           lab(C2, "KHWARAZMIAN EMPIRE", "KHWARAZMIAN\nEMPIRE", t_in=s[5] + 0.2, t_out=s[6] + 4.6),
           lab(C2, "ABBASID CALIPHATE", "ABBASID\nCALIPHATE", t_in=s[8], t_out=s[8] + 3.0),
           lab(M1, "MONGOL EMPIRE", "MONGOL\nEMPIRE", t_in=s[5] + 4.2, t_out=s[11]), lab(M1, "JIN DYNASTY", "JIN", kind="small", t_in=s[6] + 3.0, t_out=s[7]),
           lab(B, "RUS PRINCIPALITIES", "RUS\nPRINCIPALITIES", kind="mid", t_in=s[7] + 3.4, t_out=s[8]), lab(B, "POLAND", t_in=s[7]), lab(B, "HUNGARY", t_in=s[7]),
           lab(B, "MAMLUK SULTANATE", "MAMLUK\nSULTANATE", t_in=s[9]), lab(B, "YUAN DYNASTY", "YUAN\nDYNASTY", t_in=s[10] + 5.6),
           lab(B, "GOLDEN HORDE", "GOLDEN\nHORDE", t_in=s[11] + 0.3), lab(B, "CHAGATAI KHANATE", "CHAGATAI\nKHANATE", t_in=s[11] + 0.3),
           lab(B, "ILKHANATE", t_in=s[11] + 0.3), lab(B, "DELHI SULTANATE", "DELHI\nSULTANATE", t_in=s[11] + 0.3)]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("HASTINGS", (0.57, 50.45), s[2] + 2.4, en[2] + 0.2), ev("JERUSALEM", (35.22, 31.35), s[3] + 4.8, en[4] + 0.2),
           ev("KARAKORUM", (102.8, 46.7), s[5] + 1.0, en[5] + 0.2), ev("BEIJING", (116.4, 39.4), s[6] + 2.0, en[6] + 0.2),
           ev("SAMARKAND", (66.97, 39.1), s[6] + 3.4, en[6] + 0.2), ev("KYIV", (30.52, 49.95), s[7] + 2.0, en[7] + 0.2),
           ev("BAGHDAD", (44.36, 32.85), s[8] + 2.4, en[8] + 0.2), ev("AIN JALUT", (35.35, 32.05), s[9] + 2.0, en[9] + 0.2),
           ev("BEIJING", (116.4, 39.4), s[10] + 0.4, en[10] + 0.2), ev("VENICE", (12.33, 45.0), s[11] + 0.2, en[11] + 0.2)]

ticker = [(0, 1279), (s[1], 1279), (s[1] + 1.3, 1000), (s[2], 1000), (s[2] + 0.6, 1066), (s[3], 1066), (s[3] + 0.6, 1096), (s[3] + 4.0, 1096),
          (s[3] + 4.6, 1099), (s[4], 1099), (s[4] + 0.6, 1187), (s[5], 1187), (s[5] + 0.6, 1206), (s[6], 1206), (s[6] + 0.6, 1215), (s[6] + 3.6, 1221),
          (s[7], 1221), (s[7] + 0.6, 1237), (s[7] + 3.4, 1241), (s[8], 1241), (s[8] + 0.6, 1258), (s[9], 1258), (s[9] + 0.6, 1260), (s[10], 1260),
          (s[10] + 0.6, 1271), (s[10] + 5.0, 1279), (DUR, 1279)]
RRED = (232, 64, 72); GLD = (240, 200, 90); BRN = (210, 170, 120)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1279", l2="THE MONGOL EMPIRE", c2=BRN),
            hd(1, "LET'S GO BACK TO", "YEAR 1000", GOLD), hd(2, "YEAR 1066", "THE BATTLE OF HASTINGS", GLD), hd(3, "YEAR 1099", "THE FIRST CRUSADE"),
            hd(4, "YEAR 1187", "SALADIN", GOLD), hd(5, "YEAR 1206", "GENGHIS KHAN", BRN), hd(6, "THE MONGOL", "STORM", BRN),
            hd(7, "YEAR 1241", "INTO EUROPE"), hd(8, "YEAR 1258", "THE FALL OF BAGHDAD"), hd(9, "YEAR 1260", "AIN JALUT", GOLD),
            hd(10, "YEAR 1279", "ALL OF CHINA", BRN), hd(11, "MARCO POLO", "AT THE KHAN'S COURT", GOLD)]

MC = (120, 95, 70); NC = (220, 180, 70); KC = (210, 40, 40); AYC = (200, 170, 70)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, 1180))
fx = [
    M([(108, 46), (95, 44.5), (80, 43.5), (65, 42)], 1.6, 5.6, MC, kind="mongol"),
    M([(0.0, 49.4), (0.2, 50.2), (0.57, 50.85), (0.2, 51.2), (-0.12, 51.5)], s[2] + 0.4, s[2] + 3.6, NC, kind="knight"),
    PP("william", "WILLIAM THE CONQUEROR", "DUKE OF NORMANDY", s[2] + 0.6, en[2] + 0.2),
    M([(2.35, 48.85), (8, 48.5), (16.4, 48.2), (20.5, 44.8), (23.3, 42.7), (28.97, 41.0), (32.5, 37.9), (36.2, 36.2), (35.9, 33.9), (35.22, 31.78)],
      s[3] + 0.3, s[3] + 5.2, KC, kind="knight"),
    M([(31.24, 30.05), (33.0, 30.9), (34.5, 31.6), (35.45, 32.8)], s[4] + 0.4, s[4] + 2.3, AYC, kind="arab"),
    M([(35.45, 32.8), (35.3, 32.2), (35.22, 31.85)], s[4] + 2.4, s[4] + 3.6, AYC, kind="arab"),
    PP("saladin", "SALADIN", "SULTAN OF EGYPT AND SYRIA", s[4] + 0.6, en[4] + 0.2),
    M([(92, 46), (97, 47), (102, 47.2)], s[5] + 0.8, s[5] + 3.4, MC, kind="mongol"),
    M([(118, 48.5), (110, 47.6), (104, 47.3)], s[5] + 1.2, s[5] + 3.6, MC, kind="mongol"),
    PP("genghis", "GENGHIS KHAN", "FOUNDER OF THE MONGOL EMPIRE", s[5] + 1.6, en[5] + 0.2),
    M([(105, 44), (110, 42), (116.4, 39.9)], s[6] + 0.3, s[6] + 2.5, MC, kind="mongol"),
    M([(98, 46), (85, 44), (75, 42.5), (67, 39.65)], s[6] + 1.0, s[6] + 3.8, MC, kind="mongol"),
    M([(67, 39.65), (61.8, 37.6), (56, 36), (51.4, 35.7)], s[6] + 3.0, s[6] + 5.6, MC, kind="mongol"),
    M([(52, 50), (42, 52), (36, 51.5), (30.52, 50.45)], s[7] + 0.3, s[7] + 2.4, MC, kind="mongol"),
    IC("fire", (30.52, 51.0), s[7] + 2.4, s[7] + 4.2, scale=0.9),
    M([(30.52, 50.45), (24, 50.8), (19.9, 50.06), (16.2, 51.2)], s[7] + 2.8, s[7] + 5.0, MC, kind="mongol"),
    M([(30.52, 50.3), (25, 48.3), (22, 48.2), (20.9, 47.98)], s[7] + 3.2, s[7] + 5.2, MC, kind="mongol"),
    PP("batu", "BATU KHAN", "GRANDSON OF GENGHIS", s[7] + 0.8, en[7] + 0.2),
    M([(51.4, 35.7), (48.5, 34.8), (46, 34.2), (44.36, 33.31)], s[8] + 0.3, s[8] + 2.8, MC, kind="mongol"),
    IC("fire", (44.36, 33.9), s[8] + 3.0, en[8] + 0.3, scale=0.9),
    PP("hulagu", "HULAGU KHAN", "CONQUEROR OF BAGHDAD", s[8] + 0.6, en[8] + 0.2),
    M([(38.5, 36.3), (36.8, 34.4), (35.6, 32.8), (35.35, 32.55)], s[9] + 0.2, s[9] + 2.4, MC, kind="mongol"),
    M([(32.3, 30.6), (34.4, 31.5), (35.1, 32.4)], s[9] + 1.0, s[9] + 2.8, AYC, kind="arab"),
    PP("baybars", "BAYBARS", "MAMLUK COMMANDER", s[9] + 0.8, en[9] + 0.2),
    PP("kublai", "KUBLAI KHAN", "EMPEROR OF CHINA", s[10] + 0.4, en[10] + 0.2),
    M([(116.4, 39.9), (114.5, 35.5), (112.1, 32.0), (114.3, 30.6), (115.9, 28.7), (113.3, 23.1), (113.1, 22.2)], s[10] + 2.4, s[10] + 5.6, MC, kind="mongol"),
    IC("fire", (113.1, 22.6), s[10] + 5.8, en[10] + 0.3, scale=0.9),
    PP("marco", "MARCO POLO", "VENETIAN TRAVELLER", s[11] + 0.4, en[11] + 0.2),
]
routes = [dict(pts=[(12.33, 45.44), (19, 38), (28, 36), (35.07, 32.92), (38.5, 36), (44.4, 33.3), (52, 31), (56.3, 27.2), (60, 35), (67, 39.7),
                    (75.99, 39.47), (88, 40), (98, 40), (110, 40.5), (116.4, 39.9)], t0=s[11] + 0.3, t1=s[11] + 4.0, until=DUR, color=GOLD)]

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
    put(fr, glow_text("YEAR 1347", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE BLACK DEATH", 54, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=7, dur=DUR, base_a="/home/claude/shortgen/hd_1000.png", base_b="/home/claude/shortgen/hd_1279.png",
           extra_bases=dict(C1="/home/claude/shortgen/hd_1100.png", C2="/home/claude/shortgen/hd_1190.png",
                            M1="/home/claude/shortgen/hd_1227.png", M2="/home/claude/shortgen/hd_1259.png"),
           regions="/home/claude/shortgen/regions_ep07_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1[0], SW1[1], "A", "C2"), (SW2[0], SW2[1], "C2", "M1"), (SW3[0], SW3[1], "M1", "M2"),
                          (SW4[0], SW4[1], "M2", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 3.6, 0.15), (s[4] + 2.6, 0.25), (s[8] + 3.0, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
