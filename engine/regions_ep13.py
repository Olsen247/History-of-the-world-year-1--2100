import pickle, regions2 as R
import world_data_1498 as A, world_data_1522 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
grp(A, B, [dict(key="brazil_pt", empire="PORTUGAL", origin=(-39.1, -16.4), color=(80, 150, 90), src="B", clip=box(-50, -30, -30, 0)),
           dict(key="safavid", empire="SAFAVID EMPIRE", origin=(46.3, 38.1), color=(60, 150, 120), src="B"),
           dict(key="india_pt", empire="PORTUGAL", origin=(74.0, 15.5), color=(80, 150, 90), src="B", clip=box(50, -5, 110, 30)),
           dict(key="carib_sp", empire="SPAIN", origin=(-69.9, 18.5), color=(235, 180, 40), src="B", clip=box(-86, 6, -64, 24)),
           dict(key="ottoman", empire="OTTOMAN EMPIRE", origin=(37.3, 36.5), color=(200, 60, 60), src="B"),
           dict(key="mexico_sp", empire="SPAIN", origin=(-96.1, 19.2), color=(235, 180, 40), src="B", clip=box(-106, 14, -90, 24))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep13_hd.pkl", "wb")); print(list(regs))
