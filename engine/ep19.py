"""Episode 19 – Year 1825: Latin American independence (Waterloo 1815, Tambora and the year without a summer 1816, Tucuman 1816,
San Martin crosses the Andes 1817, Bolivar at Boyaca 1819, San Martin in Lima July 1821, Mexico free September 1821, Pedro I and the
Empire of Brazil 1822, the Monroe Doctrine 1823, Ayacucho December 1824, Bolivia August 1825)."""
import sys, math
from PIL import Image
import hist_engine3 as E
from hist_engine3 import put, pr, eo, eback, lerp, glow_text, GOLD, WHITE, RED
import fx as FX
FX.set_year(1825)
import world_data_1812 as A, world_data_1815 as N, world_data_1825 as B
import world_peoples as WP

S = eval(open("/home/claude/shortgen/vo_ep19/spans.txt").read())
s = [a for a, b in S]; en = [b for a, b in S]
DUR = round(en[-1] + 1.1, 2)
WIDE = (-25, 15, 2850)
shots = [(-66.0, -18.0, 1600), WIDE, (6.0, 49.5, 1300), (118.0, -8.3, 650), (-63.0, -29.0, 1200), (-69.6, -32.9, 620), (-71.0, 6.0, 900),
         (-76.5, -12.6, 650), (-98.0, 19.2, 1100), (-46.5, -19.0, 1300), (-78.0, 22.0, 2300), (-73.6, -13.6, 650), (-65.0, -5.0, 2850)]
EXTRA = {2: [(3.0, None), (3.8, (4.4, 50.7, 560))], 3: [(3.2, None), (4.2, (9.0, 50.0, 1500))], 6: [(3.4, None), (4.2, (-72.0, 4.0, 1400))],
         8: [(2.4, None), (3.2, (-95.0, 18.0, 1900))], 11: [(3.8, None), (4.6, (-66.5, -18.5, 1300))]}
endshot = list(shots)
for i, ex in EXTRA.items():
    if ex: endshot[i] = ex[-1][1]
keys = [(0.0, -60.0, -12.0, 2400), (2.2, *shots[0])]
for i in range(1, len(shots)):
    keys.append((s[i] - 0.85, *endshot[i - 1]))
    keys.append((s[i] + 0.35, *shots[i]))
    for dt, pos in EXTRA.get(i, []): keys.append((s[i] + dt, *(pos or shots[i])))
keys.append((DUR, *shots[-1]))

rv = lambda k, a, b, until=1e9: dict(key=k, t0=a, t1=b, until=until)
sh = lambda k, a, b, org: dict(key=k, t0=a, t1=b, mode="shatter", origin=org, under="N", piece_src="A", until=s[4])
reveals = [sh("fr_fall", s[2] + 0.5, s[2] + 2.9, (2.35, 48.86)), sh("rh_fall", s[2] + 0.7, s[2] + 2.9, (9.0, 50.0)),
           sh("wa_fall", s[2] + 0.9, s[2] + 2.9, (21.0, 52.2)), sh("it_fall", s[2] + 0.9, s[2] + 2.9, (9.19, 45.46)),
           rv("up", s[4] + 1.2, s[4] + 3.8), rv("chile", s[5] + 3.6, s[5] + 6.0), rv("gcol", s[6] + 3.8, s[6] + 6.2),
           rv("peru", s[7] + 2.4, s[7] + 4.8), rv("mexico", s[8] + 1.4, s[8] + 3.8), rv("centam", s[8] + 2.8, s[8] + 4.4),
           rv("haiti_e", s[9] + 0.1, s[9] + 1.0), rv("brazil", s[9] + 2.2, s[9] + 5.2), rv("florida", s[10] + 1.0, s[10] + 2.8),
           rv("bolivia", s[11] + 4.6, s[11] + 7.0)]

def lab(data, name, disp=None, kind=None, **kw):
    for n, col, polys, pos in data.EMPIRES:
        if n == name:
            k = kind or ("emp" if "EMPIRE" in n else "mid")
            return dict(dict(text=disp or n, pos=pos, kind=k, color=col), **kw)
    raise KeyError(name)
ev = lambda txt, pos, a, b, col=GOLD: dict(text=txt, pos=pos, kind="event", t_in=a, t_out=b, color=col)
T1 = s[1] + 0.8
CYN = (110, 200, 230); WT = (240, 230, 200)
H0 = en[0] + 0.2
labels = [lab(B, "GRAN COLOMBIA", "GRAN\nCOLOMBIA", pos=(-71.0, 2.0), t_in=0.6, t_out=H0),
          lab(B, "PERU", pos=(-74.5, -9.5), t_in=0.8, t_out=H0), lab(B, "BOLIVIA", pos=(-64.5, -17.0), t_in=1.0, t_out=H0),
          lab(B, "EMPIRE OF BRAZIL", "EMPIRE OF\nBRAZIL", pos=(-50.0, -11.0), t_in=0.8, t_out=H0),
          # Waterloo: Europe after the fall
          lab(N, "FRANCE", pos=(2.0, 47.0), t_in=s[2] + 2.0, t_out=s[2] + 3.4), lab(N, "PRUSSIA", pos=(13.3, 52.6), t_in=s[2] + 2.2, t_out=s[2] + 3.4),
          lab(N, "AUSTRIAN EMPIRE", "AUSTRIAN\nEMPIRE", pos=(16.5, 48.3), t_in=s[2] + 2.2, t_out=s[2] + 3.4),
          lab(N, "GERMAN CONFEDERATION", "GERMAN\nCONFEDERATION", kind="small", pos=(10.0, 49.8), t_in=s[2] + 2.4, t_out=s[2] + 3.4),
          lab(N, "NETHERLANDS", kind="small", pos=(5.6, 52.5), t_in=s[2] + 2.4, t_out=s[2] + 3.4),
          # 1816
          lab(N, "SPAIN", "SPANISH EMPIRE", pos=(-69.0, -21.5), kind="mid", t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(N, "PORTUGAL", "PORTUGUESE\nBRAZIL", kind="mid", pos=(-53.0, -18.0), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(N, "PARAGUAY", kind="small", pos=(-57.0, -23.2), t_in=s[4] + 0.3, t_out=en[4] + 0.2),
          lab(B, "UNITED PROVINCES", "UNITED\nPROVINCES", pos=(-63.5, -32.0), t_in=s[4] + 3.0, t_out=en[4] + 0.2),
          lab(B, "CHILE", pos=(-71.9, -34.6), kind="small", t_in=s[5] + 5.0, t_out=en[5] + 0.2),
          lab(B, "GRAN COLOMBIA", "GRAN\nCOLOMBIA", pos=(-65.5, 2.5), t_in=s[6] + 5.0, t_out=en[6] + 0.2),
          lab(B, "PERU", pos=(-73.5, -9.0), t_in=s[7] + 3.8, t_out=en[7] + 0.2),
          lab(B, "MEXICO", pos=(-104.0, 26.5), t_in=s[8] + 3.4, t_out=en[8] + 0.2),
          lab(B, "CENTRAL AMERICA", "CENTRAL\nAMERICA", kind="small", pos=(-87.5, 14.0), t_in=s[8] + 4.0, t_out=en[8] + 0.2),
          lab(B, "EMPIRE OF BRAZIL", "EMPIRE OF\nBRAZIL", pos=(-49.0, -14.5), t_in=s[9] + 4.2, t_out=en[9] + 0.2),
          lab(B, "UNITED STATES", "UNITED\nSTATES", pos=(-90.0, 37.5), t_in=s[10] + 0.3, t_out=en[10] + 0.2),
          lab(B, "MEXICO", pos=(-102.0, 24.0), t_in=s[10] + 0.4, t_out=en[10] + 0.2),
          lab(B, "GRAN COLOMBIA", "GRAN\nCOLOMBIA", pos=(-71.0, 5.5), t_in=s[10] + 0.5, t_out=en[10] + 0.2),
          lab(B, "SPAIN", "SPANISH\nCUBA", kind="small", pos=(-79.0, 23.4), t_in=s[10] + 0.6, t_out=en[10] + 0.2),
          lab(B, "HAITI", kind="small", pos=(-70.8, 19.9), t_in=s[10] + 0.6, t_out=en[10] + 0.2),
          lab(B, "BOLIVIA", pos=(-64.5, -17.5), t_in=s[11] + 6.0, t_out=en[11] + 0.2),
          lab(B, "PERU", kind="mid", pos=(-73.6, -10.0), t_in=s[11] + 5.0, t_out=en[11] + 0.2),
          lab(B, "EMPIRE OF BRAZIL", "BRAZIL", kind="mid", pos=(-58.0, -13.0), t_in=s[11] + 5.0, t_out=en[11] + 0.2)]
labels += [ev("WATERLOO", (4.4, 49.6), s[2] + 4.2, en[2] + 0.2), ev("BRUSSELS", (5.0, 51.95), s[2] + 4.2, en[2] + 0.2, WT),
           ev("MOUNT TAMBORA", (118.0, -12.6), s[3] + 0.8, s[3] + 3.4), ev("EUROPE", (9.0, 44.3), s[3] + 4.4, en[3] + 0.2, CYN),
           ev("TUCUMÁN", (-65.2, -26.1), s[4] + 0.8, en[4] + 0.2),
           ev("MENDOZA", (-67.6, -34.3), s[5] + 0.4, s[5] + 4.1, WT), ev("ANDES", (-69.9, -31.3), s[5] + 0.8, s[5] + 3.2, CYN),
           ev("CHACABUCO", (-71.2, -31.4), s[5] + 3.8, en[5] + 0.2), ev("SANTIAGO", (-71.4, -34.9), s[5] + 4.4, en[5] + 0.2, WT),
           ev("BOYACÁ", (-73.2, 5.9), s[6] + 2.4, en[6] + 0.2), ev("BOGOTÁ", (-74.6, 4.0), s[6] + 2.0, s[6] + 2.8, WT),
           ev("LIMA", (-80.6, -12.0), s[7] + 1.4, en[7] + 0.2, WT), ev("MEXICO CITY", (-99.13, 21.3), s[8] + 1.2, en[8] + 0.2, WT),
           ev("IPIRANGA", (-46.6, -24.3), s[9] + 0.8, en[9] + 0.2),
           ev("FLORIDA", (-82.0, 28.0), s[10] + 2.6, en[10] + 0.2, CYN),
           ev("AYACUCHO", (-74.2, -15.4), s[11] + 1.6, s[11] + 4.2)]

ticker = [(0, 1825), (s[1], 1825), (s[1] + 1.3, 1812), (s[2], 1812), (s[2] + 0.6, 1815), (s[3], 1815), (s[3] + 0.6, 1816), (s[5], 1816),
          (s[5] + 0.6, 1817), (s[6], 1817), (s[6] + 0.6, 1819), (s[7], 1819), (s[7] + 0.6, 1821), (s[9], 1821), (s[9] + 0.6, 1822),
          (s[10], 1822), (s[10] + 0.6, 1823), (s[11], 1823), (s[11] + 0.6, 1824), (s[11] + 4.0, 1824), (s[11] + 4.6, 1825), (DUR, 1825)]
RRED = (232, 64, 72); GRN = (110, 210, 150); ORG = (245, 150, 50)
hd = lambda i, l1, l2, c2=RRED, **kw: dict(dict(t0=s[i] + 0.1, t1=en[i] + 0.2, l1=l1, l2=l2, c2=c2), **kw)
headings = [dict(t0=0.15, t1=en[0], l1="YEAR 1825", l2="LATIN AMERICA RISES", c2=GOLD),
            hd(1, "LET'S GO BACK TO", "YEAR 1812", GOLD), hd(2, "JUNE 1815", "WATERLOO"), hd(3, "YEAR 1816", "NO SUMMER", CYN),
            hd(4, "JULY 1816", "THE UNITED PROVINCES", GRN), hd(5, "YEAR 1817", "ACROSS THE ANDES", CYN), hd(6, "YEAR 1819", "BOLÍVAR STRIKES", GOLD),
            hd(7, "JULY 1821", "PERU IS FREE"), hd(8, "SEPTEMBER 1821", "MEXICO IS FREE", GRN), hd(9, "YEAR 1822", "EMPIRE OF BRAZIL", GRN),
            hd(10, "YEAR 1823", "THE MONROE DOCTRINE", CYN), dict(t0=s[11] + 0.1, t1=s[11] + 4.3, l1="DECEMBER 1824", l2="AYACUCHO", c2=RRED),
            dict(t0=s[11] + 4.4, t1=en[11] + 0.2, l1="YEAR 1825", l2="BOLIVIA IS BORN", c2=ORG)]

M = lambda path, a, b, col, **kw: dict(type="march", path=path, t0=a, t1=b, color=col, **kw)
IC = lambda icon, pos, a, b, **kw: dict(type="icon", icon=icon, pos=pos, t0=a, t1=b, **kw)
PP = lambda who, name, sub, a, b, x=780, y=1180: dict(type="person", who=who, name=name, sub=sub, t0=a, t1=b, screen=(x, y))
FRC = (50, 80, 180); GBC = (200, 40, 50); PRC = (40, 45, 70); SPC = (220, 170, 40); ARC = (40, 60, 140); GCC = (220, 180, 40); MXC = (60, 130, 70)
ANDES = [(-68.84, -32.89), (-69.4, -32.8), (-70.0, -32.85), (-70.5, -33.0), (-70.65, -33.3)]
SPCH = [(-70.66, -33.6), (-70.68, -33.35), (-70.7, -33.1)]
LLANOS = [(-67.5, 7.6), (-69.0, 6.6), (-70.6, 6.0), (-72.0, 5.7), (-73.0, 5.5), (-73.4, 5.45)]
SPBOG = [(-74.07, 4.71), (-73.8, 5.0), (-73.5, 5.3)]
PISCO = [(-76.4, -16.0), (-76.6, -15.0), (-76.4, -13.9)]
TOLIMA = [(-76.2, -13.7), (-76.6, -13.0), (-76.9, -12.5), (-77.03, -12.06)]
IGUALA = [(-99.54, 18.35), (-99.5, 18.8), (-99.3, 19.15), (-99.13, 19.43)]
WAT_FR = [(3.6, 50.25), (4.0, 50.45), (4.38, 50.66)]
WAT_GB = [(4.36, 50.88), (4.4, 50.78), (4.41, 50.7)]
WAT_PR = [(5.3, 50.62), (4.9, 50.66), (4.5, 50.69)]
AYA_P = [(-73.5, -12.9), (-73.9, -13.05), (-74.15, -13.15)]
AYA_S = [(-74.9, -13.45), (-74.55, -13.3), (-74.28, -13.18)]
HOOK1 = [(-68.84, -32.89), (-69.6, -32.8), (-70.3, -32.95), (-70.65, -33.45)]
HOOK2 = [(-67.0, -10.0), (-70.5, -12.0), (-74.2, -13.16)]
fx = [
    M(HOOK1, 0.5, en[0] - 0.3, ARC, kind="granadero", soldiers=4, ships=False, until=en[0] + 0.4),
    M(HOOK2, 0.9, en[0] - 0.2, GCC, kind="llanero", soldiers=4, ships=False, until=en[0] + 0.4),
    PP("bolivar", "SIMÓN BOLÍVAR", "THE LIBERATOR", 1.6, en[0] + 0.2, x=300),
    PP("napoleon", "NAPOLEON", "FORMER EMPEROR", s[2] + 0.4, s[2] + 3.4, x=300),
    M(WAT_FR, s[2] + 3.8, s[2] + 5.4, FRC, kind="napoleonic", soldiers=6, ships=False, until=en[2] + 0.3),
    M(WAT_GB, s[2] + 3.9, s[2] + 5.4, GBC, kind="redcoat", soldiers=6, ships=False, until=en[2] + 0.3),
    M(WAT_PR, s[2] + 4.3, s[2] + 5.8, PRC, kind="landwehr", soldiers=6, ships=False, until=en[2] + 0.3),
    PP("wellington", "DUKE OF WELLINGTON", "BRITISH COMMANDER", s[2] + 3.6, en[2] + 0.2),
    PP("blucher", "GEBHARD VON BLÜCHER", "PRUSSIAN COMMANDER", s[2] + 3.8, en[2] + 0.2, x=300),
    IC("fire", (118.0, -8.25), s[3] + 0.6, s[3] + 3.6),
    IC("snow", (9.0, 50.0), s[3] + 4.4, en[3] + 0.2),
    M(ANDES, s[5] + 0.5, s[5] + 3.6, ARC, kind="granadero", soldiers=6, ships=False, until=en[5] + 0.3),
    M(SPCH, s[5] + 2.4, s[5] + 3.6, SPC, kind="napoleonic", soldiers=6, ships=False, until=s[5] + 4.4),
    PP("sanmartin", "JOSÉ DE SAN MARTÍN", "ARMY OF THE ANDES", s[5] + 0.4, en[5] + 0.2),
    M(LLANOS, s[6] + 0.4, s[6] + 3.0, GCC, kind="llanero", soldiers=6, ships=False, until=s[6] + 4.0),
    M(SPBOG, s[6] + 1.6, s[6] + 3.0, SPC, kind="napoleonic", soldiers=6, ships=False, until=s[6] + 3.6),
    PP("bolivar", "SIMÓN BOLÍVAR", "THE LIBERATOR", s[6] + 0.4, en[6] + 0.2),
    M(PISCO, s[7] + 0.3, s[7] + 1.6, ARC, kind="patriot", soldiers=3, sea_only=True, until=s[7] + 2.0),
    M(TOLIMA, s[7] + 1.2, s[7] + 3.4, ARC, kind="patriot", soldiers=9, ships=False, until=en[7] + 0.3),
    PP("sanmartin", "JOSÉ DE SAN MARTÍN", "PROTECTOR OF PERU", s[7] + 0.4, en[7] + 0.2, x=300),
    M(IGUALA, s[8] + 0.3, s[8] + 2.2, MXC, kind="insurgente", soldiers=9, ships=False, until=s[8] + 2.4),
    PP("iturbide", "AGUSTÍN DE ITURBIDE", "ARMY OF THE THREE GUARANTEES", s[8] + 0.4, en[8] + 0.2),
    PP("pedro1", "PEDRO I", "EMPEROR OF BRAZIL", s[9] + 0.4, en[9] + 0.2, x=300),
    PP("monroe", "JAMES MONROE", "PRESIDENT OF THE UNITED STATES", s[10] + 0.4, en[10] + 0.2, x=300),
    M(AYA_P, s[11] + 0.4, s[11] + 2.4, ARC, kind="patriot", soldiers=9, ships=False, until=s[11] + 4.2),
    M(AYA_S, s[11] + 0.6, s[11] + 2.4, SPC, kind="napoleonic", soldiers=6, ships=False, until=s[11] + 3.2),
    PP("sucre", "ANTONIO JOSÉ DE SUCRE", "VICTOR OF AYACUCHO", s[11] + 0.4, s[11] + 4.3),
    PP("bolivar", "SIMÓN BOLÍVAR", "THE LIBERATOR", s[11] + 4.4, en[11] + 0.2, x=300),
]
routes = [dict(pts=PISCO, t0=s[7] + 0.3, t1=s[7] + 1.6, until=s[7] + 2.4, color=GOLD)]
SW1 = s[3] - 0.85; SW2 = s[12] - 0.85
labels += WP.labels(N, 1820, s[3], s[12], skip=("Charrúa",))

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
    put(fr, glow_text("YEAR 1900", 130, GOLD), 540, 790, scale=lerp(1.5, 1, k2) if k2 < 1 else k2, alpha=min(1, k2 * 2))
    put(fr, glow_text("THE AGE OF EMPIRES", 50, WHITE), 540, 930, alpha=pr(lt, 0.8, 1.1))
    put(fr, glow_text("FOLLOW THE SERIES", 44, GOLD), 540, 1260, alpha=pr(lt, 1.3, 1.6))

CFG = dict(episode=19, dur=DUR, base_a="/home/claude/shortgen/hd_1812.png", base_b="/home/claude/shortgen/hd_1825.png",
           extra_bases=dict(N="/home/claude/shortgen/hd_1815.png"),
           regions="/home/claude/shortgen/regions_ep19_hd.pkl", keys=keys, routes=routes,
           base_switches=[(s[1], s[1] + 1.0, "B", "A"), (SW1, SW1 + 1.1, "A", "N"), (SW2, SW2 + 1.1, "N", "B")],
           reveals=reveals, labels=labels, pins=[], cards=[], ticker=ticker, header_in=s[1], header_out=s[12] + 0.2,
           rewind=[(s[1], s[1] + 1.4)], hook=lambda fr, t: None, outro=outro, headings=headings, emblems=[],
           vig_strength=vig, fx=fx, flashes=[(0.15, 0.35), (s[2] + 0.5, 0.25), (s[2] + 5.4, 0.2), (s[3] + 0.6, 0.25), (s[4] + 1.2, 0.2),
                                              (s[5] + 3.6, 0.25), (s[6] + 3.8, 0.25), (s[7] + 2.4, 0.2), (s[8] + 1.4, 0.25), (s[9] + 2.2, 0.25),
                                              (s[11] + 2.4, 0.25), (s[11] + 4.6, 0.25), (s[12] + 0.6, 0.25)])
E.setup(CFG)

if __name__ == "__main__":
    E.main(sys.argv)
