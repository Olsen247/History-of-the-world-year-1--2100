import pickle, regions2 as R
import world_data_1770 as A, world_data_1776 as B
from ep16_geo import RU_PART1, PR_ROYAL, AT_GALICIA, GB_COLONIES, SP_SANFRAN
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
grp(A, B, [dict(key="part_ru", empire="RUSSIAN EMPIRE", origin=(31.0, 54.8), color=(120, 170, 90), src="B", clip=RU_PART1),
           dict(key="part_pr", empire="PRUSSIA", origin=(17.0, 54.0), color=(60, 70, 90), src="B", clip=PR_ROYAL),
           dict(key="part_at", empire="HABSBURG MONARCHY", origin=(20.0, 49.6), color=(240, 225, 120), src="B", clip=AT_GALICIA),
           dict(key="sf_sp", empire="SPAIN", origin=(-122.0, 36.95), color=(235, 180, 40), src="B", clip=box(-123, 38.2, -121.4, 36.7)),
           dict(key="usa", empire="UNITED STATES", origin=(-75.16, 39.95), color=(80, 125, 215), src="B", clip=box(-85, 47.5, -66, 30))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep17_hd.pkl", "wb")); print(list(regs))
