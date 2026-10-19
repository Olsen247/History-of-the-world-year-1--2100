import numpy as np, pickle, sys
from PIL import Image, ImageDraw, ImageFilter
import geo
from regions import make_region
Image.MAX_IMAGE_PIXELS = None
W, H = geo.W, geo.H
land = np.asarray(Image.open("hd_land.png").convert("L")) > 110
EU = [(-11, 36.5), (-10, 30), (0, 31.5), (10, 31.5), (20, 30.5), (29, 30.5), (31, 27), (32, 24.5), (33.5, 26), (35, 30), (40, 31.5), (45, 30.5),
      (48, 30.5), (50, 33), (48, 38), (44, 41), (40, 43.5), (33, 44), (33, 47), (38, 49), (40, 53), (36, 60), (30, 66), (10, 66), (-11, 60)]
ST = [(33, 44), (40, 45.5), (47, 45.5), (52, 43.5), (60, 41.5), (70, 40.5), (78, 41), (80, 44), (70, 46.5), (60, 48.5), (52, 50.5), (45, 51.5),
      (38, 49), (33, 47)]
def ragged(pts, seed):
    im = Image.new("L", (W, H), 0); ImageDraw.Draw(im).polygon(geo.P.poly(pts), fill=255)
    soft = np.asarray(im.filter(ImageFilter.GaussianBlur(30)), np.float32) / 255
    rng = np.random.default_rng(seed)
    nz = Image.fromarray((rng.random((H // 40 + 1, W // 40 + 1)) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
    nz = np.asarray(nz, np.float32) / 255
    return ((soft + (nz - 0.5) * 0.5) > 0.5) & land
meu = ragged(EU, 1); mst = ragged(ST, 2) & ~meu
B = np.asarray(Image.open("hd_1347.png").convert("RGB")).copy()
m = meu | mst
rng = np.random.default_rng(3)
for r in range(0, H, 500):
    mm = m[r:r + 500]
    if not mm.any(): continue
    blk = B[r:r + 500].astype(np.float32)
    tint = blk * 0.42 + np.array([110, 10, 22], np.float32) * 0.58
    tint *= (0.85 + 0.3 * rng.random(mm.shape)[..., None])
    blk[mm] = tint[mm]; B[r:r + 500] = np.clip(blk, 0, 255).astype(np.uint8)
Image.fromarray(B).save("hd_1347p.png")
p = "regions_ep08_hd.pkl"; regs = pickle.load(open(p, "rb"))
for key, mk, org in (("plague_steppe", mst, (77, 42.5)), ("plague_eu", meu, (15.55, 38.19))):
    r = make_region(mk, org, seed=7); r.update(key=key, color=(170, 20, 30), src="PL"); regs[key] = r
pickle.dump(regs, open(p, "wb")); print("ok", list(regs))
