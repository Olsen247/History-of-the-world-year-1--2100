import pickle, regions2 as R
import world_data_1533 as A, world_data_1600 as N, world_data_1642 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
grp(A, N, [dict(key="kazan_ru", empire="TSARDOM OF RUSSIA", origin=(49.1, 55.8), color=(120, 170, 90), src="N", clip=[p for n, c, ps, l in A.EMPIRES if n == "KAZAN KHANATE" for p in ps][0])])
grp(N, B, [dict(key="virginia_en", empire="ENGLAND", origin=(-76.78, 37.21), color=(200, 70, 80), src="B", clip=box(-78, 39.6, -75.4, 36.5)),
           dict(key="livonia_sw", empire="SWEDEN", origin=(24.1, 57.0), color=(80, 130, 205), src="B", clip=box(20.5, 62.5, 32.5, 56.0))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep15_hd.pkl", "wb")); print(list(regs))
