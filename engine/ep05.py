"""Episode 5 – Year 750: from Justinian to the Abbasid caliphate."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_476 as A, world_data_750 as B, world_data_565 as C, world_data_610 as D, world_data_740 as U

S = eval(open("/home/claude/shortgen/vo6/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.3, 2)
WIDE = (40, 35, 2950)
shots = [(35, 31, 2300), (20, 38, 2300), (19, 39, 1600), (28.97, 40.5, 900), (40, 23, 1500), (40, 26, 1600), (40, 30, 1900),
         (62, 32, 1700), (-4, 37.5, 1200), (0, 45, 1300), (25, 33, 2600), (100, 35, 2000), WIDE]
keys = [(0.0, 35, 31, 2900), (0.3, 35, 31, 2900), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW1 = (s[3] - 0.9, s[3] + 0.2); SW2 = (s[4] - 0.9, s[4] + 0.3); SW3 = (s[10] - 0.9, s[10] + 0.2); SW4 = (s[12] + 0.2, s[12] + 1.0)
rv = lambda k, a, b, until: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("byz_af", s[2] + 2.6, s[2] + 4.6, SW1[1]), rv("byz_it", s[2] + 4.9, s[2] + 7.9, SW1[1]), rv("byz_sp", s[2] + 6.8, s[2] + 8.3, SW1[1]),
           rv("arabia", s[5] + 0.3, s[5] + 3.6, SW3[1]), rv("levant", s[6] + 0.4, s[6] + 3.6, SW3[1]), rv("persia", s[6] + 1.8, s[6] + 5.4, SW3[1]),
           rv("east", s[7] + 0.3, s[7] + 3.6, SW3[1]), rv("maghreb", s[8] - 0.4, s[8] + 1.2, SW3[1]), rv("spain", s[8] + 1.6, s[8] + 4.8, SW3[1]),
           rv("abbasid", s[10] + 0.4, s[10] + 4.4, 1e9), rv("andalus", s[10] + 6.0, s[10] + 7.6, 1e9)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if ("EMPIRE" in n or "CALIPHATE" in n) else "mid")
            return dict(text=disp or n, pos=pos, kind=k, color=col, **kw)
    raise KeyError(name)

labels = [lab(B, "ABBASID CALIPHATE", "ABBASID\nCALIPHATE", t_out=s[1]), lab(B, "AL-ANDALUS", t_out=s[1]),
          lab(B, "BYZANTINE EMPIRE", "BYZANTINE\nEMPIRE", t_out=s[1]), lab(B, "FRANKISH KINGDOM", "FRANKS", t_out=s[1])]
T1 = s[1] + 0.8
labels += [lab(A, "EASTERN ROMAN EMPIRE", "EASTERN ROMAN\nEMPIRE", t_in=T1),
           lab(A, "KINGDOM OF ODOACER", "OSTROGOTHS", t_in=T1, t_out=s[2] + 6.0), lab(A, "VANDALS", t_in=T1, t_out=s[2] + 3.8),
           lab(A, "VISIGOTHS", t_in=T1, t_out=s[8] + 3.4), lab(A, "FRANKS", t_in=T1, t_out=s[3]), lab(C, "FRANKS", t_in=s[3] + 0.4),
           lab(A, "SASANIAN EMPIRE", "SASANIAN\nEMPIRE", t_in=T1, t_out=s[6] + 4.0),
           lab(D, "LOMBARDS", t_in=s[4] + 0.4), lab(D, "AVARS", t_in=s[4] + 0.4),
           lab(U, "UMAYYAD CALIPHATE", "UMAYYAD\nCALIPHATE", t_in=s[6] + 3.0, t_out=s[10] + 3.6),
           lab(B, "ABBASID CALIPHATE", "ABBASID\nCALIPHATE", t_in=s[10] + 4.0), lab(B, "AL-ANDALUS", t_in=s[10] + 7.2),
           lab(B, "TANG DYNASTY", "TANG\nDYNASTY", t_in=s[11] + 0.2), lab(B, "TIBETAN EMPIRE", "TIBETAN\nEMPIRE", t_in=s[11] + 0.6),
           lab(B, "UYGHUR KHAGANATE", "UYGHURS", t_in=s[11] + 0.6), lab(B, "SILLA", t_in=s[11] + 0.8, kind="small"),
           lab(B, "BALHAE", t_in=s[11] + 0.8, kind="small"), lab(U, "KHAZARS", t_in=s[10] + 0.5), lab(U, "BULGARIA", t_in=s[10] + 0.5, kind="small"),
           dict(text="Arab tribes", pos=(44, 25), kind="culture", t_in=T1, t_out=s[5] + 0.4)]
for name, pos in B.CULTURES:
    if name in ("Berber tribes", "Slavs", "Vikings", "Anglo-Saxon kingdoms", "Nara Japan"):
        labels.append(dict(text=name, pos=pos, kind="culture", t_in=s[4]))
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("CONSTANTINOPLE", (28.97, 40.45), s[2] + 0.3, en[3] + 0.2), ev("CARTHAGE", (10.2, 36.2), s[2] + 3.0, s[2] + 5.5),
           ev("ROME", (12.5, 41.35), s[2] + 7.6, en[2] + 0.2), ev("MECCA", (39.83, 20.8), s[4] + 0.8, en[5] + 0.2),
           ev("MEDINA", (39.6, 23.9), s[5] + 0.4, en[5] + 0.2), ev("DAMASCUS", (36.3, 32.9), s[6] + 1.6, en[6] + 0.2),
           ev("CTESIPHON", (44.6, 32.5), s[6] + 3.4, en[6] + 0.2), ev("SAMARKAND", (66.97, 39.05), s[7] + 2.6, en[7] + 0.2),
           ev("INDUS RIVER", (69.5, 26.8), s[7] + 3.0, en[7] + 0.2), ev("TOLEDO", (-4.03, 39.3), s[8] + 3.2, en[8] + 0.2),
           ev("TOURS", (0.69, 46.8), s[9] + 2.4, en[9] + 0.2), ev("CORDOBA", (-4.78, 37.3), s[10] + 7.0, en[10] + 0.2),
           ev("CHANG'AN", (108.94, 33.7), s[11] + 0.8, en[11] + 0.2)]

ticker = [(0, 750), (s[1], 750), (s[1] + 1.3, 476), (s[2], 476), (s[2] + 0.6, 527), (s[2] + 3.0, 527), (s[2] + 3.6, 533), (s[2] + 4.8, 535),
          (s[3], 535), (s[3] + 0.6, 541), (s[4], 541), (s[4] + 0.6, 610), (s[5], 610), (s[5] + 0.6, 632), (s[6], 632), (s[6] + 0.6, 636),
          (s[6] + 4.2, 651), (s[7], 651), (s[7] + 0.6, 705), (s[7] + 3.0, 710), (s[8], 710), (s[8] + 0.4, 711), (s[9], 711), (s[9] + 0.6, 732),
          (s[10], 732), (s[10] + 0.6, 750), (DUR, 750)]
RRED = (232, 64, 72); GRN = (110, 210, 130); PUR = (200, 120, 230); SLATE = (190, 195, 215)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 750", l2="THE ABBASID CALIPHATE", c2=GOLD, s2=66),
            hd(1, "LET'S GO BACK TO", "YEAR 476", GOLD), hd(2, "JUSTINIAN", "WINS IT BACK", PUR), hd(3, "YEAR 541", "THE GREAT PLAGUE"),
            hd(4, "ARABIA", "THE BIRTH OF ISLAM", GRN), hd(5, "YEAR 632", "ARABIA UNITED", GRN), hd(6, "THE ARAB", "EXPANSION", GRN),
            hd(7, "ALL THE WAY TO", "THE INDUS RIVER", GOLD, s2=66), hd(8, "YEAR 711", "INTO SPAIN", GRN), hd(9, "YEAR 732", "THE BATTLE OF TOURS", s2=66),
            hd(10, "YEAR 750", "THE ABBASIDS", SLATE), hd(11, "TANG CHINA", "A GOLDEN AGE", GOLD)]

BC = (150, 50, 130); AC = (60, 140, 80); FC = (70, 110, 200); ANC = (70, 160, 100)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, 1180))
fx = [
    PP("justinian", "JUSTINIAN I", "EASTERN ROMAN EMPEROR", s[2] + 0.5, s[2] + 4.2),
    M([(28.97, 41.0), (26.0, 38.6), (22.5, 36.2), (16, 35.6), (11.5, 36.9), (10.2, 36.8)], s[2] + 0.6, s[2] + 3.0, BC, kind="byzantine"),
    PP("belisarius", "BELISARIUS", "GENERAL", s[2] + 3.4, en[2] + 0.2, x=300),
    M([(11.0, 37.2), (12.6, 37.7), (14.0, 37.6), (15.6, 38.2), (16.0, 39.5), (15.0, 40.6), (14.2, 40.9), (12.5, 41.9)], s[2] + 4.8, s[2] + 7.8, BC, kind="byzantine"),
    IC("people", (28.97, 41.6), s[3] + 0.6, s[3] + 3.0, count=3), IC("nopeople", (28.97, 41.6), s[3] + 3.0, en[3] + 0.3),
    M([(39.6, 24.5), (38.6, 28.0), (36.8, 31.2)], s[5] + 3.6, s[5] + 6.2, AC, kind="arab"),
    M([(36.8, 31.2), (36.2, 32.6), (36.3, 33.5)], s[6] + 0.3, s[6] + 2.0, AC, kind="arab"),
    M([(42.5, 29.2), (44.3, 31.6), (44.6, 33.1)], s[6] + 1.6, s[6] + 3.6, AC, kind="arab"),
    M([(34.4, 31.2), (32.4, 30.9), (31.2, 30.0)], s[6] + 2.4, s[6] + 4.4, AC, kind="arab"),
    M([(61.8, 37.6), (63.6, 39.1), (66.9, 39.65)], s[7] + 0.3, s[7] + 2.8, AC, kind="arab"),
    M([(60.5, 26.2), (64.5, 26.0), (67.3, 25.6), (68.4, 25.4)], s[7] + 0.8, s[7] + 3.2, AC, kind="arab", ships=False),
    M([(-5.6, 35.5), (-5.45, 36.3), (-5.2, 37.2), (-4.6, 38.5), (-4.03, 39.86)], s[8] + 0.4, s[8] + 3.4, AC, kind="arab"),
    PP("tariq", "TARIQ IBN ZIYAD", "UMAYYAD GENERAL", s[8] + 0.9, en[8] + 0.2),
    M([(-1.0, 42.8), (0.0, 44.8), (0.5, 46.6), (0.69, 47.2)], s[9] + 0.3, s[9] + 2.8, AC, kind="arab"),
    M([(3.2, 49.4), (1.8, 48.3), (0.9, 47.5)], s[9] + 1.0, s[9] + 2.8, FC, kind="frank"),
    PP("charles", "CHARLES MARTEL", "LEADER OF THE FRANKS", s[9] + 1.4, en[9] + 0.2),
    PP("saffah", "AS-SAFFAH", "FIRST ABBASID CALIPH", s[10] + 0.6, s[10] + 4.4),
    M([(36.3, 33.5), (33.5, 31.2), (25, 31.6), (15, 32.3), (10, 35.5), (3, 36.6), (-1, 35.6), (-4.0, 36.4), (-4.78, 37.88)], s[10] + 4.2, s[10] + 7.0,
      ANC, kind="arab", soldiers=2),
    PP("abdalrahman", "ABD AL-RAHMAN", "THE PRINCE WHO ESCAPED", s[10] + 4.6, en[10] + 0.2, x=300),
    IC("camel", (88, 41.2), s[11] + 1.5, en[11] + 0.2),
    PP("xuanzong", "XUANZONG", "TANG EMPEROR", s[11] + 0.8, en[11] + 0.2, x=300),
    PP("libai", "LI BAI", "POET", s[11] + 2.2, en[11] + 0.2),
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
    put(fr, glow_text("YEAR 1000", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("VIKINGS REACH AMERICA", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=5, dur=DUR, base_a="/home/claude/shortgen/hd_476.png", base_b="/home/claude/shortgen/hd_750.png",
           extra_bases=dict(C="/home/claude/shortgen/hd_565.png", D="/home/claude/shortgen/hd_610.png", U="/home/claude/shortgen/hd_740.png"),
           regions="/home/claude/shortgen/regions_ep05_hd.pkl", keys=keys,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1[0], SW1[1], "A", "C"), (SW2[0], SW2[1], "C", "D"), (SW3[0], SW3[1], "D", "U"),
                          (SW4[0], SW4[1], "U", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[6] + 0.3, 0.15), (s[8] + 1.6, 0.15), (s[10] + 0.4, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
