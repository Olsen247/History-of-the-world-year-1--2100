"""Episode 3 – Year 220: the fall of the Han dynasty (geography-edit style)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import world_data_117 as A, world_data_220 as B

S = eval(open("/home/claude/shortgen/vo4/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.4, 2)
WIDE = (60, 36, 2950)
CH = (110, 33, 2100)
shots = [CH, (110, 33, 2500), (114.5, 35.5, 1500), (112.5, 34, 1900), (112.45, 34.62, 1050), (113.5, 36, 1800),
         (113.5, 31.2, 1350), (112.45, 34.62, 1500), (110.5, 30.5, 2300), (110, 33, 2000), (16, 41, 2300),
         (48.5, 32, 1150), WIDE]
keys = [(0.0, 110, 33, 2950), (0.3, 110, 33, 2950), (2.4, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *shots[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
keys.append((DUR, *shots[-1]))

SW = s[10] + 0.3
rv = lambda k, a, b, until=SW: dict(key=k, t0=a, t1=b, until=until)
reveals = [rv("wei", s[5] + 0.8, s[5] + 5.0), rv("shu", s[8] + 1.6, s[8] + 4.6), rv("wu", s[8] + 2.4, s[8] + 5.4)]

def emp_entry(data, name, **kw):
    for n, col, polys, lab in data.EMPIRES:
        if n == name:
            disp = {"KUSHAN EMPIRE": "KUSHAN\nEMPIRE", "PARTHIAN EMPIRE": "PARTHIAN\nEMPIRE", "WESTERN SATRAPS": "WESTERN\nSATRAPS",
                    "EASTERN WU": "EASTERN\nWU"}.get(n, n)
            kind = "emp" if n in ("ROMAN EMPIRE", "HAN DYNASTY", "XIANBEI", "CAO WEI") else ("mid" if ("EMPIRE" in n or n in ("SHU HAN", "EASTERN WU")) else "small")
            return dict(text=disp, pos=lab, kind=kind, color=col, **kw)

labels = []
for n in ["ROMAN EMPIRE", "XIANBEI", "KUSHAN EMPIRE", "SATAVAHANA", "KUSH", "KOREA"]: labels.append(emp_entry(B, n, t_in=en[0] - 0.3))
labels += [emp_entry(B, "PARTHIAN EMPIRE", t_in=SW), emp_entry(A, "PARTHIAN EMPIRE", t_in=en[0] - 0.3, t_out=SW)]
labels += [emp_entry(A, "HAN DYNASTY", t_in=s[1] + 0.9, t_out=s[4]), emp_entry(A, "HAN DYNASTY", t_in=s[5], t_out=s[6]), emp_entry(A, "HAN DYNASTY", t_in=s[7], t_out=s[8] + 1.2)]
labels += [emp_entry(B, "CAO WEI", t_in=s[5] + 4.4), emp_entry(B, "SHU HAN", t_in=s[8] + 4.0), emp_entry(B, "EASTERN WU", t_in=s[8] + 4.8)]
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
labels += [ev("LUOYANG", (112.45, 32.4), s[4] + 0.6, en[4] + 0.2), ev("RED CLIFFS", (113.9, 29.0), s[6] + 2.2, en[6] + 0.2),
           ev("CHENGDU", (104.07, 30.0), s[8] + 4.2, en[8] + 0.2), ev("JIANYE", (118.8, 31.4), s[8] + 5.0, en[8] + 0.2),
           ev("CTESIPHON", (44.6, 32.5), s[11] + 3.8, en[11] + 0.3)]

pins = [dict(pos=(112.45, 34.62), t0=s[4] + 0.4, t1=en[4] + 0.3), dict(pos=(112.45, 34.62), t0=s[7] + 0.4, t1=en[7] + 0.3),
        dict(pos=(44.6, 33.1), t0=s[11] + 3.5, t1=en[11] + 0.3)]

ticker = [(0, 220), (s[1], 220), (s[1] + 1.3, 117), (s[2], 117), (s[2] + 0.8, 184), (s[4], 184), (s[4] + 0.6, 190),
          (s[5], 190), (s[5] + 0.6, 196), (s[5] + 5.0, 207), (s[6], 207), (s[6] + 0.6, 208), (s[7], 208), (s[7] + 0.6, 220), (DUR, 220)]
RRED = (232, 64, 72); YEL = (250, 214, 60); WEIC = (110, 150, 240); SHUC = (100, 200, 100); WUC = (240, 110, 80)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2, **kw)
headings = [dict(t0=1.2, t1=en[0], l1="YEAR 220", l2="THE FALL OF THE HAN", c2=RRED, y=620, s1=64, s2=64, gap=95),
            hd(1, "LET'S GO BACK TO", "YEAR 117", GOLD),
            hd(2, "THE YELLOW", "TURBANS", YEL), hd(3, "THE RISE OF THE", "WARLORDS"), hd(4, "LUOYANG", "BURNS"),
            hd(5, "CAO CAO TAKES", "THE NORTH", WEIC), hd(6, "THE BATTLE OF", "RED CLIFFS"),
            hd(7, "YEAR 220", "THE END OF THE HAN", s2=66), hd(8, "THE THREE", "KINGDOMS", GOLD),
            hd(9, "REGISTERED PEOPLE", "56M → 8M", s2=84), hd(10, "YEAR 212", "ROMAN CITIZENS", GOLD),
            hd(11, "THE RISE OF", "ARDASHIR")]
emblems = [dict(pos=(17, 39.2), t0=s[10] + 0.6, t1=en[10], scale=0.6)]

HANC = (200, 70, 50); RBC = (250, 214, 40); SASC = (175, 30, 60)
M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
fx = [
    # 184 – Yellow Turbans rise on the North China Plain
    M([(117.0, 37.6), (115.3, 36.3), (113.2, 34.9)], s[2] + 0.8, s[2] + 4.4, RBC, kind="rebel"),
    M([(117.6, 34.0), (115.4, 34.4), (113.4, 34.6)], s[2] + 1.4, s[2] + 4.8, RBC, kind="rebel"),
    # generals crush them and become warlords
    M([(112.6, 34.6), (114.2, 35.6), (115.8, 36.6)], s[3] + 0.3, s[3] + 3.3, HANC, kind="han", until=en[3] + 0.4),
    M([(112.6, 34.4), (114.4, 34.0), (116.2, 33.6)], s[3] + 0.6, s[3] + 3.6, HANC, kind="han", until=en[3] + 0.4),
    # 190 – Luoyang burns
    IC("fire", (112.45, 35.1), s[4] + 1.0, en[4] + 0.3, scale=1.1),
    # Cao Cao takes the north
    M([(113.8, 34.0), (115.0, 35.8), (116.4, 37.6)], s[5] + 0.5, s[5] + 3.8, WEIC, kind="han"),
    # 208 – Red Cliffs
    M([(113.6, 33.2), (113.6, 31.6), (113.8, 30.2)], s[6] + 0.3, s[6] + 3.2, WEIC, kind="han", until=s[6] + 4.6),
    M([(116.4, 30.0), (115.2, 29.9), (114.3, 29.85)], s[6] + 1.2, s[6] + 3.6, WUC, kind="han"),
    M([(111.0, 30.6), (112.4, 30.2), (113.5, 29.85)], s[6] + 1.4, s[6] + 3.8, SHUC, kind="han"),
    IC("fire", (113.9, 30.1), s[6] + 4.0, en[6] + 0.3, scale=1.1),
    # population collapse
    IC("people", (110.5, 20.5), s[9] + 0.6, s[9] + 4.6, count=3),
    IC("nopeople", (110.5, 20.5), s[9] + 4.6, en[9] + 0.3),
    # Ardashir rises in Persis and heads for the Parthian capital
    M([(52.6, 29.8), (50.5, 30.6), (47.8, 31.6), (45.3, 32.7)], s[11] + 0.8, s[11] + 4.4, SASC, kind="parthian"),
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
    put(fr, glow_text("YEAR 476", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE FALL OF ROME", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=3, dur=DUR, base_a="/home/claude/shortgen/hd_117.png", base_b="/home/claude/shortgen/hd_220.png",
           regions="/home/claude/shortgen/regions_ep03_hd.pkl", keys=keys,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW - 0.8, SW, "A", "B")],
           reveals=reveals, labels=labels, pins=pins, cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=emblems,
           vig_strength=vig, fx=fx, flashes=[(1.2, 0.35), (s[4] + 1.0, 0.2), (s[6] + 4.0, 0.2), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
