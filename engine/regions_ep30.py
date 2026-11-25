import pickle, sys, os, regions2 as R
import geo
# run one group per process (python3 regions_ep30.py 0|1|2|3) – several in one process can run out of memory
OUT = "/home/claude/shortgen/regions_ep30_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
NKC = (130, 175, 95); SKC = (150, 190, 250); PRC = (205, 60, 60); ROC = (225, 185, 85); FRG = (225, 205, 110)
sh = lambda key, emp, org, col: dict(key=key, empire=emp, origin=org, color=col, mode="shatter")
if G in (-1, 0):
    import world_data_1945 as A, world_data_1950 as W
    grp(A, W, [dict(key="frg_gain", empire="WEST GERMANY", origin=(7.1, 50.7), color=FRG, src="G"),
               dict(key="prc_gain", empire="PEOPLE'S REPUBLIC OF CHINA", origin=(116.4, 39.9), color=PRC, src="G"),
               dict(key="tw_gain", empire="TAIWAN", origin=(121.5, 25.0), color=ROC, src="G")])
if G in (-1, 1):
    import world_data_1950 as W, world_data_1950k1 as K
    grp(W, K, [dict(key="nk_gain", empire="NORTH KOREAN-HELD SOUTH", origin=(127.0, 37.9), color=NKC, src="K"),
               sh("nk_loss", "NORTH KOREAN-HELD SOUTH", (126.6, 37.47), NKC)])
if G in (-1, 2):
    import world_data_1950 as W, world_data_1950k2 as K
    grp(W, K, [dict(key="un_gain", empire="UN-HELD NORTH", origin=(126.9, 37.9), color=SKC, src="K"),
               sh("un_loss", "UN-HELD NORTH", (126.0, 40.6), SKC)])
if G in (-1, 3):
    import world_data_1950 as W, world_data_1950k3 as K
    grp(W, K, [dict(key="red_gain", empire="COMMUNIST-HELD SOUTH", origin=(127.0, 38.3), color=NKC, src="K"),
               sh("red_loss", "COMMUNIST-HELD SOUTH", (127.5, 37.1), NKC)])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
