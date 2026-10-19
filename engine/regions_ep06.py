import pickle, regions2 as R
import world_data_750 as A, world_data_1000 as B, world_data_800 as C, world_data_1000pre as D
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
grp(A, C, [dict(key="caro", empire="CAROLINGIAN EMPIRE", origin=(6.08, 50.78), color=(70, 110, 200), src="C")])
grp(D, B, [dict(key="rus", empire="KIEVAN RUS", origin=(31.27, 58.52), color=(120, 170, 90), src="B"),
           dict(key="iceland", empire="ICELAND", origin=(-21.9, 64.1), color=(60, 110, 190), src="B"),
           dict(key="normandy", empire="NORMANDY", origin=(1.1, 49.44), color=(220, 180, 70), src="B"),
           dict(key="greenland", empire="NORSE GREENLAND", origin=(-45.5, 61.15), color=(60, 110, 190), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep06_hd.pkl", "wb")); print(list(regs))
