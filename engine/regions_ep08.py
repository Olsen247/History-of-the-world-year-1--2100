import pickle, numpy as np, regions2 as R
from PIL import Image, ImageDraw
import geo
from regions import make_region
import world_data_1279 as A, world_data_1347 as B
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
grp(B, A, [dict(key="acre", empire="CRUSADER STATES", origin=(35.07, 32.92), color=(235, 235, 240), src="A", mode="retreat"),
           dict(key="ilkhan_fall", empire="ILKHANATE", origin=(48, 35), color=(160, 95, 90), src="A", mode="retreat")])
grp(A, B, [dict(key="ottoman", empire="OTTOMANS", origin=(30.18, 40.02), color=(200, 60, 60), src="B"),
           dict(key="mali", empire="MALI EMPIRE", origin=(-8.5, 11.5), color=(210, 160, 60), src="B"),
           dict(key="delhi", empire="DELHI SULTANATE", origin=(77.2, 28.6), color=(60, 140, 110), src="B")])
land = np.asarray(Image.open("/home/claude/shortgen/hd_land.png").convert("L")) > 110
def pm(pts):
    im = Image.new("L", (geo.W, geo.H), 0); ImageDraw.Draw(im).polygon(geo.P.poly(pts), fill=255); return (np.asarray(im) > 0) & land
area = [(-11, 27), (45, 27), (55, 35), (80, 38), (80, 56), (40, 62), (30, 66), (10, 66), (-11, 60)]
steppe = pm([(33, 40.5), (80, 38), (80, 56), (33, 56)]) & pm(area)
eu = pm(area) & ~steppe
for key, m, org in (("plague_steppe", steppe, (77, 42.5)), ("plague_eu", eu, (15.55, 38.19))):
    r = make_region(m, org, seed=7); r.update(key=key, color=(170, 20, 30), src="PL"); regs[key] = r; print(key, r["bbox"])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep08_hd.pkl", "wb")); print(list(regs))
