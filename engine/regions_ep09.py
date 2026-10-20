import pickle, regions2 as R
import world_data_1347 as A, world_data_1405 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
NOT_MONGOLIA = [(70, 10), (145, 10), (145, 56), (124, 49), (122.5, 44), (118, 42.6), (112, 41.6), (106, 41.4), (100, 41.6), (92, 42.6), (70, 42.6)]
grp(B, A, [dict(key="yuan_fall", empire="YUAN DYNASTY", origin=(116.4, 39.9), color=(150, 105, 60), src="A", mode="retreat", clip=NOT_MONGOLIA),
           dict(key="serbia_fall", empire="SERBIAN EMPIRE", origin=(21.0, 42.0), color=(180, 70, 90), src="A", mode="retreat"),
           dict(key="delhi_fall", empire="DELHI SULTANATE", origin=(77.2, 28.6), color=(60, 140, 110), src="A", mode="retreat")])
grp(A, B, [dict(key="ming", empire="MING DYNASTY", origin=(118.8, 32.05), color=(215, 70, 60), src="B"),
           dict(key="timurid", empire="TIMURID EMPIRE", origin=(66.97, 39.65), color=(90, 150, 170), src="B"),
           dict(key="ottoman", empire="OTTOMAN EMPIRE", origin=(26.67, 40.41), color=(200, 60, 60), src="B"),
           dict(key="kalmar", empire="KALMAR UNION", origin=(16.36, 56.66), color=(200, 60, 70), src="B"),
           dict(key="vijaya", empire="VIJAYANAGARA", origin=(76.46, 15.33), color=(190, 80, 70), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep09_hd.pkl", "wb")); print(list(regs))
