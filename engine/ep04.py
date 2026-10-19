"""Episode 4 – Year 476: the fall of the Western Roman Empire."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_220 as A, world_data_476 as B, world_data_271 as C, world_data_330 as C2, world_data_395 as D

S = eval(open("/home/claude/shortgen/vo5/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.3, 2)
WIDE = (40, 38, 2950)
shots = [(10, 44, 1500), (25, 40, 2200), (49, 32, 1300), (40, 36, 1000), (16, 42, 2100), (16, 42, 2000), (29, 40.5, 900),
         (36, 45, 1500), (22, 41, 1900), (13, 43, 1000), (5, 40, 1600), (5, 45, 1450), (80, 21.5, 1400), WIDE]
keys = [(0.0, 10, 44, 2600), (0.3, 10, 44, 2600), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW1 = (s[6] - 0.9, s[6] + 0.3)      # 220/271 map  -> 330 map
SW2 = (s[9] - 0.9, s[9] + 0.2)      # 330 map      -> 395 map
SW3 = (s[13] + 0.2, s[13] + 1.0)    # 395 map      -> 476 map
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("sas", s[2] + 0.8, s[2] + 5.0, SW1[1]),
           rv("gallic", s[4] + 0.5, s[4] + 3.0, SW1[1]), rv("palm", s[4] + 2.8, s[4] + 5.6, SW1[1]),
           rv("regain_g", s[5] + 0.5, s[5] + 3.2, SW1[1]), rv("regain_p", s[5] + 1.4, s[5] + 4.6, SW1[1]),
           rv("huns", s[7] + 0.3, s[7] + 3.0, SW2[1]), rv("east", s[8] + 0.6, s[8] + 4.6, SW2[1]),
           rv("vandals", s[10] + 0.4, s[10] + 3.0, 1e9),
           dict(key="west", t0=s[11] + 0.4, t1=s[11] + 3.6, mode="shatter", origin=(12.5, 41.9), under="B", piece_src="D"),
           rv("gupta", s[12] + 0.4, s[12] + 3.8, 1e9), rv("heph", s[12] + 0.6, s[12] + 3.4, 1e9),
           rv("vaka", s[12] + 1.6, s[12] + 3.6, 1e9), rv("pallava", s[12] + 2.0, s[12] + 3.8, 1e9)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

labels = []
for n, d in [("KINGDOM OF ODOACER", "KINGDOM OF\nODOACER"), ("VISIGOTHS", None), ("FRANKS", None), ("BURGUNDIANS", None), ("VANDALS", None),
             ("SUEBI", None), ("EASTERN ROMAN EMPIRE", "EASTERN ROMAN\nEMPIRE")]:
    labels.append(lab(B, n, d, t_out=s[1]))
labels += [lab(A, "PARTHIAN EMPIRE", "PARTHIAN\nEMPIRE", t_in=s[1] + 0.8, t_out=s[2] + 2.6),
           lab(C, "SASANIAN EMPIRE", "SASANIAN\nEMPIRE", t_in=s[2] + 4.2),
           lab(A, "ROMAN EMPIRE", t_in=s[1] + 0.8, t_out=s[8] + 0.6),
           lab(C, "GALLIC EMPIRE", "GALLIC\nEMPIRE", t_in=s[4] + 2.4, t_out=s[5] + 2.6),
           lab(C, "PALMYRENE EMPIRE", "PALMYRENE\nEMPIRE", t_in=s[4] + 5.0, t_out=s[5] + 4.0),
           lab(D, "HUNS", t_in=s[7] + 2.4, t_out=s[11] + 0.4),
           lab(D, "WESTERN ROMAN EMPIRE", "WESTERN ROMAN\nEMPIRE", t_in=s[8] + 1.0, t_out=s[11] + 0.5),
           lab(D, "EASTERN ROMAN EMPIRE", "EASTERN ROMAN\nEMPIRE", t_in=s[8] + 4.0),
           lab(B, "VANDALS", t_in=s[10] + 2.8)]
for i, (n, d) in enumerate([("VISIGOTHS", None), ("FRANKS", None), ("BURGUNDIANS", None), ("SUEBI", None), ("SOISSONS", "SOISSONS"),
                            ("KINGDOM OF ODOACER", "KINGDOM OF\nODOACER")]):
    labels.append(lab(B, n, d, kind="mid" if n != "SOISSONS" else "small", t_in=s[11] + 2.6 + i * 0.35))
labels += [lab(B, "GUPTA EMPIRE", "GUPTA\nEMPIRE", t_in=s[12] + 3.4), lab(B, "HEPHTHALITES", t_in=s[12] + 3.0, kind="mid"),
           lab(B, "VAKATAKA", t_in=s[12] + 3.4, kind="small"), lab(B, "PALLAVAS", t_in=s[12] + 3.6, kind="small")]
labels += [dict(text="Germanic tribes", pos=(14, 52.8), kind="culture", t_in=s[1] + 0.8, t_out=s[11]),
           dict(text="Sarmatians", pos=(42, 48), kind="culture", t_in=s[1] + 0.8, t_out=s[7] + 1.5)]
for name, pos in B.CULTURES:
    if name in ("Saxons", "Thuringians", "Alamanni", "Bretons", "Britons", "Ostrogoths", "Picts"): continue
    labels.append(dict(text=name, pos=pos, kind="culture", t_in=s[11] + 3.0 if pos[0] > -20 else s[13] + 0.4))
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("EDESSA", (38.8, 36.5), s[3] + 2.6, en[3] + 0.2), ev("PALMYRA", (38.27, 33.9), s[4] + 3.4, en[4] + 0.2),
           ev("CONSTANTINOPLE", (28.97, 40.45), s[6] + 0.8, en[6] + 0.3), ev("ROME", (12.5, 41.35), s[9] + 0.6, en[9] + 0.2),
           ev("CARTHAGE", (10.2, 36.2), s[10] + 2.6, en[10]), ev("RAVENNA", (12.2, 44.0), s[11] + 6.0, en[11] + 0.2),
           ev("PATALIPUTRA", (85.1, 25.0), s[12] + 0.6, en[12] + 0.2)]
pins = [dict(pos=(38.8, 37.15), t0=s[3] + 2.4, t1=en[3] + 0.3), dict(pos=(38.27, 34.55), t0=s[4] + 3.0, t1=en[4] + 0.3),
        dict(pos=(28.97, 41.01), t0=s[6] + 0.5, t1=en[6] + 0.3), dict(pos=(12.5, 41.9), t0=s[9] + 0.4, t1=en[9] + 0.3),
        dict(pos=(12.2, 44.42), t0=s[11] + 5.8, t1=en[11] + 0.3), dict(pos=(85.1, 25.6), t0=s[12] + 0.4, t1=en[12] + 0.3)]

ticker = [(0, 476), (s[1], 476), (s[1] + 1.3, 220), (s[2], 220), (s[2] + 0.6, 224), (s[3], 224), (s[3] + 0.6, 260), (s[4], 260),
          (s[4] + 0.6, 271), (s[5], 271), (s[5] + 0.6, 274), (s[6], 274), (s[6] + 0.6, 330), (s[7], 330), (s[7] + 0.6, 376),
          (s[8], 376), (s[8] + 0.6, 395), (s[9], 395), (s[9] + 0.6, 410), (s[10], 410), (s[10] + 0.6, 439), (s[10] + 2.2, 439),
          (s[10] + 2.8, 451), (s[11], 451), (s[11] + 0.6, 476), (DUR, 476)]
RRED = (232, 64, 72); ORA = (245, 150, 70); PUR = (200, 120, 230)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 476", l2="THE FALL OF ROME", c2=RRED, y=330, s1=64, s2=80, gap=95),
            hd(1, "LET'S GO BACK TO", "YEAR 220", GOLD), hd(2, "A NEW PERSIAN EMPIRE", "THE SASANIANS", ORA),
            hd(3, "YEAR 260", "AN EMPEROR CAPTURED"), hd(4, "THE CRISIS OF THE", "THIRD CENTURY"),
            hd(5, "AURELIAN", "RESTORER OF THE WORLD", GOLD, s2=62), hd(6, "A NEW CAPITAL", "CONSTANTINOPLE", GOLD, s2=66),
            hd(7, "THE HUNS", "ARE COMING"), hd(8, "YEAR 395", "EAST AND WEST", PUR), hd(9, "YEAR 410", "ROME IS SACKED"),
            hd(10, "THE VANDALS AND", "ATTILA THE HUN", s2=66), hd(11, "YEAR 476", "THE END OF THE WEST"),
            hd(12, "INDIA'S", "GOLDEN AGE", GOLD)]

SASC = (222, 120, 48); RC = (196, 52, 62); HC = (150, 105, 60); GC = (205, 145, 60); VC = (110, 110, 200); OC = (60, 160, 150)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, **kw: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, **kw)
fx = [
    M([(52.6, 29.8), (50.2, 31.8), (47.2, 32.8), (44.8, 33.1)], s[2] + 0.6, s[2] + 3.8, SASC, kind="sasanian"),
    PP("ardashir", "ARDASHIR I", "FOUNDER OF THE SASANIANS", s[2] + 1.2, en[2], screen=(780, 1180)),
    M([(44.6, 33.1), (42.5, 35.4), (39.3, 37.0)], s[3] + 0.3, s[3] + 3.0, SASC, kind="sasanian"),
    M([(35.8, 37.0), (37.4, 37.1), (38.4, 37.15)], s[3] + 0.6, s[3] + 2.8, RC, kind="legion"),
    PP("shapur", "SHAPUR I", "KING OF PERSIA", s[3] + 2.9, en[3] + 0.2, screen=(300, 1180)),
    PP("valerian", "VALERIAN", "CAPTURED EMPEROR", s[3] + 3.3, en[3] + 0.2, screen=(780, 1180)),
    PP("zenobia", "ZENOBIA", "QUEEN OF PALMYRA", s[4] + 3.4, en[4] + 0.2, screen=(780, 1180)),
    M([(12.5, 42.2), (9.5, 44.8), (6.5, 46.8), (5.0, 48.8)], s[5] + 0.3, s[5] + 3.0, RC, kind="legion"),
    M([(29.0, 41.0), (32.5, 39.2), (36.4, 36.6), (38.1, 34.8)], s[5] + 1.2, s[5] + 4.4, RC, kind="legion"),
    PP("aurelian", "AURELIAN", "ROMAN EMPEROR", s[5] + 0.6, en[5] + 0.2, screen=(780, 1180)),
    PP("constantine", "CONSTANTINE", "THE GREAT", s[6] + 1.2, en[6] + 0.2, screen=(780, 1180)),
    M([(56.0, 48.0), (48.0, 47.6), (39.0, 47.2), (32.0, 46.8)], s[7] + 0.2, s[7] + 3.0, HC, kind="hun"),
    M([(31.0, 47.4), (29.0, 45.9), (27.2, 43.6)], s[7] + 1.8, s[7] + 3.9, GC, kind="goth"),
    M([(22.5, 42.6), (17.5, 44.6), (13.8, 45.8), (11.7, 44.1), (12.5, 42.0)], s[9] + 0.3, s[9] + 3.5, GC, kind="goth"),
    IC("fire", (12.5, 43.1), s[9] + 3.6, en[9] + 0.3, scale=0.9),
    PP("alaric", "ALARIC", "KING OF THE VISIGOTHS", s[9] + 0.6, s[9] + 3.4, screen=(780, 1180)),
    M([(-5.6, 37.2), (-5.5, 35.6), (-1.0, 35.4), (4.5, 36.4), (10.0, 36.8)], s[10] + 0.2, s[10] + 2.8, VC, kind="goth"),
    PP("gaiseric", "GAISERIC", "KING OF THE VANDALS", s[10] + 0.5, s[10] + 2.6, screen=(300, 1180)),
    M([(19.0, 47.4), (13.0, 48.3), (8.5, 49.2), (4.4, 48.9)], s[10] + 2.0, s[10] + 4.0, HC, kind="hun"),
    M([(16.5, 46.4), (13.6, 45.9), (11.4, 45.4)], s[10] + 2.4, s[10] + 4.0, HC, kind="hun"),
    PP("attila", "ATTILA", "KING OF THE HUNS", s[10] + 2.6, en[10] + 0.2, screen=(780, 1180)),
    M([(16.5, 46.8), (14.5, 46.3), (12.9, 45.7), (12.2, 44.6)], s[11] + 4.0, s[11] + 6.2, OC, kind="goth", ships=False),
    PP("odoacer", "ODOACER", "KING OF ITALY", s[11] + 4.4, en[11] + 0.2, screen=(300, 1180)),
    PP("romulus", "ROMULUS AUGUSTULUS", "LAST WESTERN EMPEROR", s[11] + 5.2, en[11] + 0.2, screen=(780, 1180)),
    PP("aryabhata", "ARYABHATA", "MATHEMATICIAN", s[12] + 4.0, en[12] + 0.2, screen=(780, 1180)),
]

def vig(t):
    if t < en[0] + 0.3 or t > s[13] + 0.2: return 1.0
    return 0.6

def outro(fr, t):
    t0 = s[13] + 0.3
    if t < t0: return
    lt = t - t0
    dim = Image.new("RGBA", (E.W, E.H), (2, 6, 14, int(205 * pr(lt, 0, 0.5)))); fr.paste(dim, (0, 0), dim)
    k = eback(pr(lt, 0, 0.35), 2.2)
    put(fr, glow_text("NEXT EPISODE", 56, WHITE), 540, 640, scale=min(k, 1.1), alpha=min(1, k * 2))
    k2 = eback(pr(lt, 0.3, 0.65), 2.4)
    put(fr, glow_text("YEAR 750", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("FROM SPAIN TO INDIA", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=4, dur=DUR, base_a="/home/claude/shortgen/hd_220.png", base_b="/home/claude/shortgen/hd_476.png",
           extra_bases=dict(C="/home/claude/shortgen/hd_271.png", E2="/home/claude/shortgen/hd_330.png", D="/home/claude/shortgen/hd_395.png"),
           regions="/home/claude/shortgen/regions_ep04_hd.pkl", keys=keys,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1[0], SW1[1], "A", "E2"), (SW2[0], SW2[1], "E2", "D"), (SW3[0], SW3[1], "D", "B")],
           reveals=reveals, labels=labels, pins=pins, cards=[], ticker=ticker, header_in=s[1], header_out=s[13] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[3] + 2.9, 0.2), (s[9] + 3.6, 0.25), (s[11] + 0.4, 0.3), (s[13] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
