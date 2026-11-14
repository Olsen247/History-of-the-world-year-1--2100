import pickle, sys, os, regions2 as R
import geo
# run one group per process (python3 regions_ep27.py 0|1) – both in one process can run out of memory
OUT = "/home/claude/shortgen/regions_ep27_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
import world_data_1939 as A, world_data_1940 as G4, world_data_1941 as K
GER = (110, 110, 122); SOV = (130, 175, 95); FIN = (235, 235, 245)
if G in (-1, 0): grp(A, G4, [dict(key="karelia", empire="SOVIET KARELIA", origin=(30.0, 60.2), color=SOV, src="G"),
           dict(key="denmark", empire="OCCUPIED DENMARK", origin=(9.4, 54.9), color=GER, src="G"),
           dict(key="norway", empire="OCCUPIED NORWAY", origin=(10.7, 59.9), color=GER, src="G"),
           dict(key="neth", empire="OCCUPIED NETHERLANDS", origin=(6.9, 52.2), color=GER, src="G"),
           dict(key="belg", empire="OCCUPIED BELGIUM", origin=(6.1, 50.4), color=GER, src="G"),
           dict(key="france_n", empire="OCCUPIED FRANCE", origin=(4.95, 49.7), color=GER, clip=box(-6.0, 48.6, 9.0, 52.0), src="G"),
           dict(key="france_s", empire="OCCUPIED FRANCE", origin=(2.35, 48.86), color=GER, src="G")])
if G in (-1, 1): grp(G4, K, [dict(key="yugo", empire="OCCUPIED YUGOSLAVIA", origin=(15.8, 46.6), color=GER, src="B"),
           dict(key="greece", empire="OCCUPIED GREECE", origin=(23.0, 41.4), color=GER, src="B"),
           dict(key="barb_w", empire="GERMAN-OCCUPIED USSR", origin=(23.6, 52.2), color=GER, clip=box(15.0, 40.0, 31.5, 62.0), src="B"),
           dict(key="barb_e", empire="GERMAN-OCCUPIED USSR", origin=(31.0, 53.5), color=GER, src="B"),
           dict(key="finkar", empire="FINNISH-HELD KARELIA", origin=(29.5, 61.6), color=FIN, src="B")])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
