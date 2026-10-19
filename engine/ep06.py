"""Episode 6 – Year 1000: the Viking Age and the road to America."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_750 as A, world_data_1000 as B, world_data_800 as C, world_data_1000pre as D

S = eval(open("/home/claude/shortgen/vo7/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.3, 2)
WIDE = (10, 48, 2950)
shots = [(-30, 59, 2400), (5, 52, 2400), (0, 57, 1200), (7, 48, 1700), (0, 53, 1700), (28, 54, 1900), (-8, 57, 2000), (-34, 62, 1500),
         (-48, 57, 1900), (25, 41, 1200), (15, 35, 2000), (122, 34, 2300), WIDE]
keys = [(0.0, -30, 59, 2900), (0.3, -30, 59, 2900), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW1 = (s[4] - 0.9, s[4] + 0.2); SW2 = (s[5] - 0.9, s[5] + 0.3); SW3 = (s[12] + 0.2, s[12] + 1.0)
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("caro", s[3] + 0.6, s[3] + 4.0, SW1[1]), rv("rus", s[5] + 1.8, s[5] + 5.4, 1e9), rv("iceland", s[6] + 1.2, s[6] + 2.8, 1e9),
           rv("normandy", s[6] + 4.4, s[6] + 6.0, 1e9), rv("greenland", s[7] + 3.4, s[7] + 5.2, 1e9)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if ("EMPIRE" in n or "CALIPHATE" in n) else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

T1 = s[1] + 0.8; T5 = s[5] + 0.4; T9 = s[9]
labels = [lab(B, "NORWAY", t_out=s[1]), lab(B, "ICELAND", kind="small", t_out=s[1]), lab(B, "NORSE GREENLAND", "NORSE\nGREENLAND", kind="small", t_out=s[1]),
          dict(text="VINLAND", pos=(-55.5, 52.4), kind="event", color=GOLD, t_in=2.0, t_out=s[1])]
labels += [lab(A, "FRANKISH KINGDOM", "FRANKS", t_in=T1, t_out=s[3] + 3.6), lab(C, "CAROLINGIAN EMPIRE", "CAROLINGIAN\nEMPIRE", t_in=s[3] + 3.8, t_out=s[5] + 0.2),
           lab(A, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", t_in=T1), lab(A, "ABBASID CALIPHATE", "ABBASID\nCALIPHATE", t_in=T1, t_out=s[5] + 0.2),
           lab(A, "AL-ANDALUS", t_in=T1, t_out=s[5] + 0.2), lab(A, "KHAZARS", t_in=T1, t_out=s[5] + 0.2),
           dict(text="Vikings", pos=(11, 61), kind="culture", t_in=T1, t_out=s[5]),
           dict(text="Anglo-Saxon kingdoms", pos=(-1.2, 52.6), kind="culture", t_in=T1, t_out=s[5])]
for n, d, tin in [("KINGDOM OF ENGLAND", "ENGLAND", T5), ("SCOTLAND", None, T5), ("KINGDOM OF FRANCE", "FRANCE", T5), ("DENMARK", None, T5),
                  ("NORWAY", None, T5), ("SWEDEN", None, T5), ("LEON", None, T5), ("NAVARRE", None, T5), ("BULGARIA", None, T5),
                  ("CALIPHATE OF CORDOBA", "CALIPHATE OF\nCORDOBA", T5), ("FATIMID CALIPHATE", "FATIMID\nCALIPHATE", T5), ("BUYIDS", None, T5),
                  ("GHAZNAVIDS", None, T5), ("KARAKHANIDS", None, T5), ("HOLY ROMAN EMPIRE", "HOLY ROMAN\nEMPIRE", T9), ("POLAND", None, T9),
                  ("HUNGARY", None, T9), ("SONG DYNASTY", "SONG\nDYNASTY", s[11]), ("LIAO DYNASTY", "LIAO\nDYNASTY", s[11]), ("GORYEO", None, s[11]),
                  ("KIEVAN RUS", "KIEVAN\nRUS", s[5] + 4.8), ("NORMANDY", None, s[6] + 5.6), ("ICELAND", None, s[6] + 2.4),
                  ("NORSE GREENLAND", "NORSE\nGREENLAND", s[7] + 4.8)]:
    k = "small" if n in ("NORMANDY", "ICELAND", "NORSE GREENLAND", "NAVARRE", "LEON", "SCOTLAND") else None
    labels.append(lab(B, n, d, kind=k, t_in=tin))
for name, pos in B.CULTURES:
    if name in ("Irish kingdoms", "Pechenegs", "Heian Japan", "Volga Bulgars"):
        labels.append(dict(text=name, pos=pos, kind="culture", t_in=T5))
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("LINDISFARNE", (-1.8, 55.25), s[2] + 2.8, en[2] + 0.2), ev("AACHEN", (6.08, 50.3), s[3] + 0.5, en[3] + 0.2),
           ev("PARIS", (2.35, 48.35), s[4] + 3.6, en[4] + 0.2), ev("DUBLIN", (-6.26, 52.9), s[4] + 3.4, en[4] + 0.2),
           ev("NOVGOROD", (31.27, 58.05), s[5] + 1.8, en[5] + 0.2), ev("KIEV", (30.52, 49.95), s[5] + 3.8, en[5] + 0.2),
           ev("VINLAND", (-55.5, 52.4), s[8] + 3.6, en[8] + 0.3), ev("CONSTANTINOPLE", (28.97, 40.45), s[9] + 0.3, en[9] + 0.2),
           ev("CORDOBA", (-4.78, 37.3), s[10] + 2.6, en[10] + 0.2), ev("CAIRO", (31.24, 29.5), s[10] + 1.0, en[10] + 0.2),
           ev("KAIFENG", (114.3, 33.9), s[11] + 0.6, en[11] + 0.2), ev("KYOTO", (135.77, 34.2), s[11] + 3.4, en[11] + 0.2)]

ticker = [(0, 1000), (s[1], 1000), (s[1] + 1.3, 750), (s[2], 750), (s[2] + 0.6, 793), (s[3], 793), (s[3] + 0.6, 800), (s[4], 800), (s[4] + 0.6, 845),
          (s[5], 845), (s[5] + 0.6, 862), (s[6], 862), (s[6] + 0.6, 874), (s[6] + 3.0, 874), (s[6] + 3.6, 911), (s[7], 911), (s[7] + 0.6, 982),
          (s[8], 982), (s[8] + 0.6, 1000), (DUR, 1000)]
RRED = (232, 64, 72); BLU = (120, 170, 240); PUR = (200, 120, 230); GRN = (110, 210, 150)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 1000", l2="VIKINGS IN AMERICA", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 750", GOLD), hd(2, "YEAR 793", "THE VIKING AGE BEGINS"), hd(3, "YEAR 800", "EMPEROR CHARLEMAGNE", BLU),
            hd(4, "YEAR 845", "VIKINGS ATTACK PARIS"), hd(5, "VIKINGS IN THE EAST", "THE KIEVAN RUS", GRN), hd(6, "YEAR 911", "NORMANDY", GOLD),
            hd(7, "YEAR 982", "ERIK THE RED"), hd(8, "500 YEARS BEFORE COLUMBUS", "VINLAND", GOLD), hd(9, "BASIL II", "THE BULGAR SLAYER", PUR),
            hd(10, "THE ISLAMIC WORLD", "DIVIDED", GRN), hd(11, "SONG CHINA", "GUNPOWDER", GOLD)]

VK = (60, 110, 190); FC = (70, 110, 200); BC = (150, 50, 130); RUSC = (120, 170, 90)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, 1180))
fx = [
    M([(-30, 63.5), (-42, 60.5), (-50, 58), (-55.53, 51.6)], 1.4, 5.4, VK, kind="viking"),
    M([(5.3, 60.4), (2, 58.8), (-1.0, 56.4), (-1.8, 55.67)], s[2] + 0.4, s[2] + 3.4, VK, kind="viking"),
    IC("fire", (-1.8, 56.1), s[2] + 3.6, en[2] + 0.3, scale=0.9),
    M([(6.1, 50.8), (9, 52.2), (10.5, 53.2)], s[3] + 0.8, s[3] + 3.2, FC, kind="frank"),
    M([(6.1, 50.6), (8, 47.6), (9.2, 45.5)], s[3] + 1.2, s[3] + 3.6, FC, kind="frank"),
    PP("charlemagne", "CHARLEMAGNE", "EMPEROR OF THE FRANKS", s[3] + 0.6, en[3] + 0.2),
    M([(9.5, 57.0), (6.0, 54.3), (2.0, 51.5), (0.2, 49.6), (1.2, 49.25), (2.35, 48.85)], s[4] + 0.3, s[4] + 4.4, VK, kind="viking"),
    M([(5.0, 61.0), (-1.5, 59.6), (-5.5, 58.9), (-7, 56), (-6.26, 53.35)], s[4] + 0.6, s[4] + 3.6, VK, kind="viking"),
    IC("fire", (2.35, 49.3), s[4] + 4.5, en[4] + 0.3, scale=0.9),
    M([(18.1, 59.3), (22, 59.6), (27.5, 59.8), (30, 59.9), (31.27, 58.52)], s[5] + 0.3, s[5] + 2.2, (90, 150, 210), kind="viking"),
    M([(31.27, 58.52), (31.0, 55.0), (30.5, 50.45)], s[5] + 2.0, s[5] + 4.0, (90, 150, 210), kind="viking"),
    M([(30.5, 50.45), (32, 47), (31.5, 44.5), (29.5, 42.2), (28.97, 41.3)], s[5] + 4.2, en[5] + 0.2, (90, 150, 210), kind="viking"),
    M([(5.0, 61.0), (-3, 62.3), (-12, 63.5), (-21.9, 64.1)], s[6] + 0.2, s[6] + 2.0, VK, kind="viking"),
    M([(8.6, 56.5), (4, 53.5), (0.6, 50.5), (0.2, 49.6), (1.1, 49.44)], s[6] + 3.0, s[6] + 5.0, VK, kind="viking"),
    PP("rollo", "ROLLO", "FIRST RULER OF NORMANDY", s[6] + 3.4, en[6] + 0.2),
    M([(-21.9, 64.6), (-30, 64.5), (-38, 62.5), (-43, 60.3), (-45.5, 61.15)], s[7] + 0.8, s[7] + 3.6, VK, kind="viking"),
    PP("erik", "ERIK THE RED", "SETTLER OF GREENLAND", s[7] + 0.6, en[7] + 0.2),
    M([(-45.5, 61.15), (-52, 61.5), (-58, 58), (-56.5, 54), (-55.53, 51.6)], s[8] + 0.4, s[8] + 3.8, VK, kind="viking"),
    PP("leif", "LEIF ERIKSON", "EXPLORER", s[8] + 0.6, en[8] + 0.2),
    M([(28.97, 41.1), (26.5, 42.0), (24.5, 42.2), (22.5, 41.6)], s[9] + 0.4, s[9] + 3.0, BC, kind="byzantine"),
    PP("basil", "BASIL II", "BYZANTINE EMPEROR", s[9] + 0.6, en[9] + 0.2),
    IC("fire", (114.3, 34.9), s[11] + 0.8, s[11] + 3.4, scale=0.9),
    IC("scroll", (135.77, 36.8), s[11] + 3.6, en[11] + 0.2, scale=0.9),
    PP("murasaki", "MURASAKI SHIKIBU", "THE TALE OF GENJI", s[11] + 3.6, en[11] + 0.2),
]

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
    put(fr, glow_text("YEAR 1279", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE MONGOL EMPIRE", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=6, dur=DUR, base_a="/home/claude/shortgen/hd_750.png", base_b="/home/claude/shortgen/hd_1000.png",
           extra_bases=dict(C="/home/claude/shortgen/hd_800.png", D="/home/claude/shortgen/hd_1000pre.png"),
           regions="/home/claude/shortgen/regions_ep06_hd.pkl", keys=keys,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1[0], SW1[1], "A", "C"), (SW2[0], SW2[1], "C", "D"), (SW3[0], SW3[1], "D", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[2] + 3.6, 0.2), (s[4] + 4.5, 0.2), (s[8] + 3.8, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
