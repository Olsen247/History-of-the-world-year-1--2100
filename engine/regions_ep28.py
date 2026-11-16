import pickle, sys, os, regions2 as R
import geo
# run one group per process (python3 regions_ep28.py 0|1) – both in one process can run out of memory
OUT = "/home/claude/shortgen/regions_ep28_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
import world_data_1941 as A, world_data_1942 as P, world_data_1943 as B
GER = (110, 110, 122); JAP = (235, 95, 70); ITA = (110, 185, 150)
if G in (-1, 0): grp(A, P, [dict(key="japan", empire="JAPANESE CONQUESTS", origin=(106.0, 11.0), color=JAP, src="G"),
           dict(key="east42", empire="GERMAN-OCCUPIED USSR", origin=(37.5, 49.5), color=GER, src="G"),
           dict(key="egypt", empire="AXIS-HELD EGYPT", origin=(25.0, 31.5), color=ITA, src="G")])
if G in (-1, 1): grp(B, P, [dict(key="east_loss", empire="GERMAN-OCCUPIED USSR", origin=(44.5, 48.7), color=GER, src="G"),
           dict(key="egypt_loss", empire="AXIS-HELD EGYPT", origin=(29.0, 30.9), color=ITA, src="G")])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
