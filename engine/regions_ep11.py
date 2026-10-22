import pickle, regions2 as R
import world_data_1453b as A, world_data_1492 as B
from ep11_geo import NOVGOROD
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
SERBIA = [(18.5, 42.2), (23.0, 42.2), (23.0, 45.2), (18.5, 45.2)]
MOREA = [(20.8, 36.0), (23.8, 36.0), (23.8, 38.45), (20.8, 38.45)]
TREB = [(36.8, 39.8), (42.0, 39.8), (42.0, 41.8), (36.8, 41.8)]
grp(A, B, [dict(key="ott_serbia", empire="OTTOMAN EMPIRE", origin=(21.6, 42.4), color=(200, 60, 60), src="B", clip=SERBIA),
           dict(key="ott_morea", empire="OTTOMAN EMPIRE", origin=(22.8, 38.3), color=(200, 60, 60), src="B", clip=MOREA),
           dict(key="ott_treb", empire="OTTOMAN EMPIRE", origin=(37.0, 40.9), color=(200, 60, 60), src="B", clip=TREB),
           dict(key="songhai", empire="SONGHAI EMPIRE", origin=(-0.04, 16.27), color=(200, 110, 60), src="B"),
           dict(key="muscovy", empire="MUSCOVY", origin=(37.6, 55.75), color=(120, 170, 90), src="B", clip=NOVGOROD),
           dict(key="granada", empire="CASTILE", origin=(-3.7, 37.9), color=(200, 120, 60), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep11_hd.pkl", "wb")); print(list(regs))
