import pickle, regions2 as R
import world_data_1812 as A, world_data_1815 as N, world_data_1825 as B
from ep19_geo import CENTRAL_AM, SP_FLORIDA_1783
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
# Napoleon's system breaks apart (1814-15): shattered pieces fall away and the Vienna map (N) shows underneath
grp(B, A, [dict(key="fr_fall", empire="FRENCH EMPIRE", origin=(2.35, 48.86), color=(55, 95, 200), src="A", mode="retreat"),
           dict(key="rh_fall", empire="CONFEDERATION OF THE RHINE", origin=(9.0, 50.0), color=(150, 170, 220), src="A", mode="retreat"),
           dict(key="wa_fall", empire="DUCHY OF WARSAW", origin=(21.0, 52.2), color=(225, 140, 150), src="A", mode="retreat"),
           dict(key="it_fall", empire="KINGDOM OF ITALY", origin=(9.19, 45.46), color=(110, 170, 120), src="A", mode="retreat")])
grp(N, B, [dict(key="up", empire="UNITED PROVINCES", origin=(-65.2, -26.8), color=(120, 180, 230), src="B"),
           dict(key="chile", empire="CHILE", origin=(-70.65, -33.45), color=(60, 90, 200), src="B"),
           dict(key="gcol", empire="GRAN COLOMBIA", origin=(-73.4, 5.5), color=(40, 160, 190), src="B"),
           dict(key="peru", empire="PERU", origin=(-77.03, -12.05), color=(200, 50, 60), src="B"),
           dict(key="mexico", empire="MEXICO", origin=(-99.13, 19.43), color=(150, 190, 90), src="B"),
           dict(key="centam", empire="CENTRAL AMERICA", origin=(-90.5, 14.6), color=(180, 120, 200), src="B"),
           dict(key="haiti_e", empire="HAITI", origin=(-72.3, 18.55), color=(60, 60, 160), src="B"),
           dict(key="brazil", empire="EMPIRE OF BRAZIL", origin=(-46.6, -23.55), color=(50, 150, 70), src="B"),
           dict(key="florida", empire="UNITED STATES", origin=(-84.3, 30.4), color=(80, 125, 215), src="B", clip=box(-92, 24, -79, 31.5)),
           dict(key="bolivia", empire="BOLIVIA", origin=(-65.26, -19.05), color=(230, 140, 60), src="B")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep19_hd.pkl", "wb")); print(list(regs))
