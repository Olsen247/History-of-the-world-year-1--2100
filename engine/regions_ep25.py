import pickle, regions2 as R
import geo
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
import world_data_1918n as N, world_data_1920 as M, world_data_1922 as B
grp(N, M, [dict(key="poland", empire="POLAND", origin=(21.0, 52.23), color=(225, 80, 90), src="M"),
           dict(key="czech", empire="CZECHOSLOVAKIA", origin=(14.42, 50.08), color=(100, 150, 215), src="M"),
           dict(key="scs", empire="KINGDOM OF SCS", origin=(20.46, 44.8), color=(170, 90, 90), src="M"),
           dict(key="austria", empire="AUSTRIA", origin=(16.37, 48.2), color=(240, 225, 120), src="M"),
           dict(key="hungary", empire="HUNGARY", origin=(19.04, 47.5), color=(120, 170, 110), src="M"),
           dict(key="estonia", empire="ESTONIA", origin=(24.75, 59.43), color=(90, 130, 200), src="M"),
           dict(key="latvia", empire="LATVIA", origin=(24.1, 56.95), color=(170, 70, 90), src="M"),
           dict(key="lithuania", empire="LITHUANIA", origin=(23.9, 54.9), color=(210, 175, 95), src="M"),
           dict(key="romania", empire="ROMANIA", origin=(23.6, 46.77), color=(220, 190, 80), src="M"),
           dict(key="br_mand", empire="BRITISH MANDATE", origin=(44.4, 33.3), color=(235, 125, 165), clip=box(33.0, 28.0, 49.5, 38.0), src="M"),
           dict(key="fr_mand", empire="FRENCH MANDATE", origin=(35.5, 33.9), color=(60, 95, 200), clip=box(34.0, 31.0, 43.0, 38.0), src="M")])
grp(M, N, [dict(key="ger_loss", empire="GERMAN EMPIRE", origin=(10.0, 51.0), color=(110, 110, 122), src="A")])
grp(B, M, [dict(key="whites", empire="WHITES", origin=(34.0, 45.0), color=(225, 225, 215), src="M")])
grp(M, B, [dict(key="ireland", empire="IRISH FREE STATE", origin=(-6.26, 53.35), color=(60, 150, 80), src="B"),
           dict(key="turkey", empire="OTTOMAN EMPIRE", origin=(32.85, 39.93), color=(200, 60, 60), clip=box(20.0, 34.0, 46.0, 43.0), src="B"),
           dict(key="ussr", empire="SOVIET UNION", origin=(37.6, 55.75), color=(130, 175, 95), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep25_hd.pkl", "wb")); print(list(regs))
