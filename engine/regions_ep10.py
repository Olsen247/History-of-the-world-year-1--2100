import pickle, regions2 as R
import world_data_1405 as A, world_data_1420 as N, world_data_1453 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
FRANCE_BOX = [(-2.6, 42.8), (6.0, 42.8), (6.0, 50.7), (-2.6, 50.7)]
NOT_CONST = [(18, 34), (40, 34), (40, 46), (29.25, 46), (29.25, 40.97), (27.95, 40.97), (27.95, 46), (18, 46)]
grp(A, N, [dict(key="england_fr", empire="ENGLAND", origin=(0.11, 49.49), color=(200, 70, 80), src="N", clip=FRANCE_BOX)])
grp(B, N, [dict(key="eng_loss", empire="ENGLAND", origin=(1.9, 47.9), color=(200, 70, 80), src="N", mode="retreat", clip=FRANCE_BOX)])
grp(B, A, [dict(key="byz_fall", empire="BYZANTINE EMPIRE", origin=(28.95, 41.02), color=(150, 50, 130), src="A", mode="retreat")])
grp(A, B, [dict(key="inca", empire="INCA EMPIRE", origin=(-71.97, -13.53), color=(235, 105, 35), src="B"),
           dict(key="ottoman", empire="OTTOMAN EMPIRE", origin=(26.56, 41.68), color=(200, 60, 60), src="B", clip=NOT_CONST)])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep10_hd.pkl", "wb")); print(list(regs))
