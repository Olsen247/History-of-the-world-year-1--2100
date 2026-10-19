import pickle, regions2 as R
import world_data_476 as A, world_data_750 as B, world_data_565 as C, world_data_610 as D, world_data_740 as U
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
BZ = (150, 50, 130); UM = (60, 140, 80)
grp(A, C, [dict(key="byz_af", empire="EASTERN ROMAN EMPIRE", origin=(10.2, 36.8), color=BZ, src="C", clip=[(-2, 30), (20, 30), (20, 38.5), (-2, 38.5)]),
           dict(key="byz_it", empire="EASTERN ROMAN EMPIRE", origin=(14.5, 37.5), color=BZ, src="C", clip=[(6, 36.3), (19.5, 36.3), (19.5, 47.5), (6, 47.5)]),
           dict(key="byz_sp", empire="EASTERN ROMAN EMPIRE", origin=(-5.5, 36.1), color=BZ, src="C", clip=[(-8, 35.5), (1, 35.5), (1, 39.5), (-8, 39.5)])])
grp(D, U, [dict(key="arabia", empire="UMAYYAD CALIPHATE", origin=(39.6, 24.47), color=UM, src="U",
                clip=[(34.5, 29.0), (36, 31.3), (39.5, 31.8), (47.5, 30), (57, 27), (61, 22), (52, 13), (43, 11.5), (38, 19), (34.5, 27.5)]),
           dict(key="levant", empire="UMAYYAD CALIPHATE", origin=(36.5, 31.5), color=UM, src="U", clip=[(24.5, 20), (42.5, 20), (42.5, 39), (24.5, 39)]),
           dict(key="persia", empire="UMAYYAD CALIPHATE", origin=(44.3, 31.6), color=UM, src="U", clip=[(38, 22), (62.5, 22), (62.5, 44), (38, 44)]),
           dict(key="maghreb", empire="UMAYYAD CALIPHATE", origin=(25, 31.5), color=UM, src="U", clip=[(-12, 27), (25.6, 27), (25.6, 35.85), (-12, 35.85)]),
           dict(key="spain", empire="UMAYYAD CALIPHATE", origin=(-5.4, 36.1), color=UM, src="U", clip=[(-12, 35.85), (6, 35.85), (6, 45), (-12, 45)]),
           dict(key="east", empire="UMAYYAD CALIPHATE", origin=(61.8, 37.6), color=UM, src="U")])
grp(U, B, [dict(key="abbasid", empire="ABBASID CALIPHATE", origin=(61.8, 37.6), color=(78, 78, 96), src="B"),
           dict(key="andalus", empire="AL-ANDALUS", origin=(-4.78, 37.88), color=(70, 160, 100), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep05_hd.pkl", "wb")); print(list(regs))
