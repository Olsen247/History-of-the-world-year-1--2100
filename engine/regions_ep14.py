import pickle, regions2 as R
import world_data_1522 as A, world_data_1533 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
grp(A, B, [dict(key="sweden", empire="SWEDEN", origin=(18.07, 59.33), color=(80, 130, 205), src="B"),
           dict(key="mughal", empire="MUGHAL EMPIRE", origin=(76.97, 29.39), color=(40, 150, 95), src="B", clip=box(69.0, 35.0, 86.0, 23.0)),
           dict(key="syrmia_ot", empire="OTTOMAN EMPIRE", origin=(20.46, 44.8), color=(200, 60, 60), src="B", clip=box(18.0, 46.0, 22.0, 44.0)),
           dict(key="peru_sp", empire="SPAIN", origin=(-78.5, -7.16), color=(235, 180, 40), src="B", clip=box(-82, -2, -70, -15))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep14_hd.pkl", "wb")); print(list(regs))
