import pickle, sys, os, regions2 as R
import geo
# run one group per process (python3 regions_ep26.py 0|1|2) – all three in one process run out of memory
OUT = "/home/claude/shortgen/regions_ep26_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
import world_data_1931 as C, world_data_1937 as E, world_data_1938 as F, world_data_1939 as B
GER = (110, 110, 122); JAP = (235, 95, 70); NAT = (140, 110, 70); SOV = (130, 175, 95)
if G in (-1, 0): grp(C, E, [dict(key="manchukuo", empire="MANCHUKUO", origin=(123.4, 41.8), color=JAP, src="E"),
           dict(key="nationalists", empire="NATIONALISTS", origin=(-5.98, 37.39), color=NAT, src="E"),
           dict(key="jc37n", empire="JAPANESE-OCCUPIED CHINA", origin=(116.2, 39.85), color=JAP, clip=box(105.0, 34.6, 125.0, 43.5), src="E"),
           dict(key="jc37s", empire="JAPANESE-OCCUPIED CHINA", origin=(121.47, 31.23), color=JAP, clip=box(115.0, 28.0, 125.0, 34.6), src="E")])
if G in (-1, 1): grp(E, F, [dict(key="austria", empire="GERMANY", origin=(13.0, 48.3), color=GER, clip=box(9.0, 46.0, 17.5, 49.2), src="F"),
           dict(key="sudeten", empire="SUDETENLAND", origin=(12.4, 50.1), color=GER, src="F")])
if G in (-1, 2): grp(F, B, [dict(key="prague", empire="BOHEMIA-MORAVIA", origin=(13.3, 50.3), color=GER, src="B"),
           dict(key="slovakia", empire="SLOVAKIA", origin=(17.1, 48.15), color=(120, 165, 225), src="B"),
           dict(key="ruthenia", empire="HUNGARIAN RUTHENIA", origin=(22.3, 48.6), color=(120, 170, 110), src="B"),
           dict(key="poland_de", empire="GERMAN-OCCUPIED POLAND", origin=(16.8, 52.3), color=GER, src="B"),
           dict(key="poland_su", empire="SOVIET-OCCUPIED POLAND", origin=(27.5, 52.0), color=SOV, src="B")])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
