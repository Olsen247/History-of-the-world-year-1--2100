import pickle, regions2 as R
import geo
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
import world_data_1917 as M, world_data_1918 as B, world_data_1918n as N
grp(M, B, [dict(key="aqaba", empire="ARAB REVOLT", origin=(36.4, 29.9), color=(70, 145, 75), clip=box(33.5, 26.0, 39.0, 31.0), src="B"),
           dict(key="finland", empire="FINLAND", origin=(24.94, 60.17), color=(215, 225, 240), src="B"),
           dict(key="east", empire="OCCUPIED EAST 1918", origin=(24.5, 52.5), color=(190, 50, 55), src="B")])
grp(B, N, [dict(key="syria", empire="ARAB REVOLT", origin=(36.3, 33.5), color=(70, 145, 75), src="N"),
           dict(key="levant", empire="BRITISH PALESTINE", origin=(35.0, 32.3), color=(235, 125, 165), src="N")])
grp(N, B, [dict(key="occ_loss", empire="GERMAN-OCCUPIED", origin=(3.0, 49.8), color=(190, 50, 55), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep24_hd.pkl", "wb")); print(list(regs))
