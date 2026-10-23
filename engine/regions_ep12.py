import pickle, regions2 as R
import world_data_1492 as A, world_data_1495 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
SOUTH_ITALY = [(13.0, 37.8), (19.2, 37.8), (19.2, 42.6), (13.0, 42.6)]
grp(A, B, [dict(key="naples_fr", empire="FRANCE", origin=(13.9, 41.6), color=(70, 110, 200), src="B", clip=SOUTH_ITALY)])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep12_hd.pkl", "wb")); print(list(regs))
