import pickle, regions2 as R
import world_data_1776 as A, world_data_1795 as N, world_data_1812 as B
from ep18_geo import US_1783, GB_NSW, PR_P23, AT_P3, US_LOUISIANA, FR_SAINTDOMINGUE, RU_FINLAND
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
grp(A, N, [dict(key="us1783", empire="UNITED STATES", origin=(-80.0, 40.0), color=(80, 125, 215), src="N", clip=US_1783),
           dict(key="nsw", empire="GREAT BRITAIN", origin=(151.2, -33.86), color=(200, 70, 80), src="N", clip=box(148, -31, 154, -36)),
           dict(key="pol_pr", empire="PRUSSIA", origin=(16.9, 52.4), color=(60, 70, 90), src="N", clip=PR_P23),
           dict(key="pol_at", empire="HABSBURG MONARCHY", origin=(20.0, 50.1), color=(240, 225, 120), src="N", clip=AT_P3),
           dict(key="pol_ru", empire="RUSSIAN EMPIRE", origin=(30.0, 54.0), color=(120, 170, 90), src="N", clip=box(20, 58.5, 33, 48))])
grp(N, B, [dict(key="louisiana", empire="UNITED STATES", origin=(-90.07, 29.95), color=(80, 125, 215), src="B", clip=US_LOUISIANA),
           dict(key="haiti", empire="HAITI", origin=(-72.3, 18.55), color=(60, 60, 160), src="B"),
           dict(key="fr_emp", empire="FRENCH EMPIRE", origin=(2.35, 48.86), color=(55, 95, 200), src="B", clip=box(-6, 56, 20, 40)),
           dict(key="confed", empire="CONFEDERATION OF THE RHINE", origin=(8.0, 50.0), color=(150, 170, 220), src="B"),
           dict(key="swiss", empire="SWITZERLAND", origin=(7.4, 46.9), color=(200, 120, 120), src="B"),
           dict(key="italy", empire="KINGDOM OF ITALY", origin=(9.19, 45.46), color=(110, 170, 120), src="B"),
           dict(key="naples", empire="KINGDOM OF NAPLES", origin=(14.25, 40.85), color=(160, 120, 200), src="B"),
           dict(key="warsaw", empire="DUCHY OF WARSAW", origin=(21.0, 52.23), color=(225, 140, 150), src="B"),
           dict(key="ru_fin", empire="RUSSIAN EMPIRE", origin=(30.0, 61.0), color=(120, 170, 90), src="B", clip=RU_FINLAND)])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep18_hd.pkl", "wb")); print(list(regs))
