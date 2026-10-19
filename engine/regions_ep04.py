import pickle, regions2 as R
import world_data_220 as A, world_data_476 as B, world_data_271 as C, world_data_330 as C2, world_data_395 as D
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
grp(A, C, [dict(key="sas", empire="SASANIAN EMPIRE", origin=(52.9, 29.9), color=(222, 120, 48), src="C"),
           dict(key="gallic", empire="GALLIC EMPIRE", origin=(6.64, 49.75), color=(60, 140, 190), src="C"),
           dict(key="palm", empire="PALMYRENE EMPIRE", origin=(38.27, 34.55), color=(150, 90, 180), src="C")])
grp(A, C, [dict(key="regain_g", empire="GALLIC EMPIRE", origin=(7.5, 45.5), color=(196, 52, 62), src="A", mode="retreat"),
           dict(key="regain_p", empire="PALMYRENE EMPIRE", origin=(31, 39), color=(196, 52, 62), src="A", mode="retreat")])
grp(C2, D, [dict(key="huns", empire="HUNS", origin=(52, 47.5), color=(130, 95, 60), src="D"),
            dict(key="east", empire="EASTERN ROMAN EMPIRE", origin=(28.97, 41.0), color=(150, 50, 130), src="D"),
            dict(key="west", empire="WESTERN ROMAN EMPIRE", origin=(12.5, 41.9), color=(196, 52, 62), src="D", mode="retreat",
                 clip=[(-12, 36.6), (20, 36.6), (20, 60), (-12, 60)])])
grp(D, B, [dict(key="vandals", empire="VANDALS", origin=(-5.4, 35.9), color=(95, 95, 175), src="B"),
           dict(key="gupta", empire="GUPTA EMPIRE", origin=(85.1, 25.6), color=(235, 135, 95), src="B"),
           dict(key="heph", empire="HEPHTHALITES", origin=(68, 38.5), color=(150, 120, 190), src="B"),
           dict(key="vaka", empire="VAKATAKA", origin=(78, 20.5), color=(120, 170, 90), src="B"),
           dict(key="pallava", empire="PALLAVAS", origin=(79.8, 12.8), color=(140, 200, 110), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep04_hd.pkl", "wb")); print(list(regs))
