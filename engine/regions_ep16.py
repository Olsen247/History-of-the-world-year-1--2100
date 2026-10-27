import pickle, regions2 as R
import world_data_1642 as A, world_data_1740 as N, world_data_1770 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
ming = [p for n, c, ps, l in A.EMPIRES if n == "MING DYNASTY" for p in ps][0]
grp(A, N, [dict(key="qing_china", empire="QING EMPIRE", origin=(119.7, 40.0), color=(225, 185, 70), src="N", clip=ming),
           dict(key="baltic_ru", empire="TSARDOM OF RUSSIA", origin=(30.3, 59.9), color=(120, 170, 90), src="N", clip=box(20.5, 60.4, 32.5, 56.0))])
from ep16_geo import BENGAL_1740
grp(N, B, [dict(key="bengal_eic", empire="GREAT BRITAIN", origin=(88.25, 23.8), color=(200, 70, 80), src="B", clip=BENGAL_1740),
           dict(key="canada_gb", empire="GREAT BRITAIN", origin=(-71.2, 46.8), color=(200, 70, 80), src="B", clip=box(-100, 62, -55, 24))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep16_hd.pkl", "wb")); print(list(regs))
