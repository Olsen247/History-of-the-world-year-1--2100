import pickle, regions2 as R
import world_data_1825 as A, world_data_1882 as M, world_data_1900 as B
regs = {}
import numpy as np, geo
from PIL import Image, ImageDraw
_LAND = np.asarray(Image.open("/home/claude/shortgen/hd_land.png").convert("L")) > 110
class _Lazy(dict):
    """Memory-light masks: only the empires a spec asks for (the full set of 65 x 50 MB masks does not fit in 7 GB)."""
    def __init__(self, data): super().__init__(); self.data = data
    def _calc(self, nm):
        names = [e[0] for e in self.data.EMPIRES]
        if nm not in names: return None
        i = names.index(nm); im = Image.new("L", (geo.W, geo.H), 0); d = ImageDraw.Draw(im)
        for pts in self.data.EMPIRES[i][2]: d.polygon(geo.P.poly(pts), fill=255)
        if getattr(self.data, "EXCLUSIVE", False):
            for e2 in self.data.EMPIRES[i + 1:]:
                for pts in e2[2]: d.polygon(geo.P.poly(pts), fill=0)
        return (np.asarray(im) > 0) & _LAND
    def __missing__(self, nm):
        m = self._calc(nm)
        if m is None: raise KeyError(nm)
        self[nm] = m; return m
    def get(self, nm, default=None):
        if nm in self: return self[nm]
        m = self._calc(nm)
        if m is None: return default
        self[nm] = m; return m
R.masks = _Lazy
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
box = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
BRIT = (235, 125, 165); FRC = (60, 95, 200)
# 1830-1871 on the 1825 map
grp(A, B, [dict(key="algeria", empire="FRENCH EMPIRE", origin=(3.06, 36.75), color=FRC, clip=box(-3, 32, 12, 38)),
           dict(key="hk", empire="BRITISH EMPIRE", origin=(114.15, 22.28), color=BRIT, clip=box(113.7, 22.1, 114.5, 22.6)),
           dict(key="uswest", empire="UNITED STATES", origin=(-95.0, 31.0), color=(150, 190, 250), clip=box(-125, 25, -93.5, 49.5)),
           dict(key="india", empire="BRITISH EMPIRE", origin=(77.2, 28.6), color=BRIT, clip=box(60, 5, 93, 37.5)),
           dict(key="germany", empire="GERMAN EMPIRE", origin=(13.4, 52.5), color=(110, 110, 122), clip=box(5, 46, 23, 56)),
           dict(key="belgium", empire="BELGIUM", origin=(4.35, 50.85), color=(235, 195, 60)),
           dict(key="italy", empire="ITALY", origin=(7.68, 45.07), color=(110, 185, 150), clip=box(6, 36, 19, 47.5))])
# 1884-1898 on the 1882 map
AF = box(-20, -36, 53, 38)
grp(M, B, [dict(key="af_fr", empire="FRENCH EMPIRE", origin=(-17.4, 14.7), color=FRC, clip=AF),
           dict(key="af_gb", empire="BRITISH EMPIRE", origin=(18.4, -33.9), color=BRIT,
                clip=[(-20, -36), (53, -36), (53, 4.6), (34, 4.6), (31, 3.7), (27.5, 5.0), (24, 8.7), (22, 11), (20, 24), (-20, 24)]),
           dict(key="af_gb2", empire="BRITISH EMPIRE", origin=(45.0, 10.4), color=BRIT, clip=box(42.5, 8, 50, 12)),
           dict(key="af_de", empire="GERMAN EMPIRE", origin=(39.3, -6.8), color=(110, 110, 122), clip=AF),
           dict(key="af_cg", empire="CONGO FREE STATE", origin=(13.05, -5.85), color=(170, 120, 200), clip=AF),
           dict(key="af_pt", empire="PORTUGAL", origin=(13.23, -8.84), color=(50, 140, 80), clip=AF),
           dict(key="af_it", empire="ITALY", origin=(39.45, 15.6), color=(110, 185, 150), clip=box(35, -3, 53, 19)),
           dict(key="af_es", empire="SPAIN", origin=(-15.9, 23.7), color=(235, 180, 40), clip=box(-18, 0, 12, 28)),
           dict(key="phil", empire="UNITED STATES", origin=(120.98, 14.6), color=(150, 190, 250), clip=box(116, 4, 128, 20)),
           dict(key="pr", empire="UNITED STATES", origin=(-66.1, 18.4), color=(150, 190, 250), clip=box(-68, 17.5, -65, 19))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep20_hd.pkl", "wb")); print(list(regs))
