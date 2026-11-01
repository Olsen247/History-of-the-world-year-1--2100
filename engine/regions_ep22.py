import pickle, types, regions2 as R
import numpy as np, geo
from PIL import Image, ImageDraw
regs = {}
_LAND = np.asarray(Image.open("/home/claude/shortgen/hd_land.png").convert("L")) > 110
class _Lazy(dict):
    """Memory-light masks: only the empires a spec asks for."""
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
import world_data_1911 as A, world_data_1913 as M, world_data_1914 as B, world_data_1914w as W
ITC = (110, 185, 150)
grp(A, M, [dict(key="libya_coast", empire="ITALY", origin=(13.18, 32.89), color=ITC, clip=box(9.0, 30.6, 26.0, 34.0), src="M"),
           dict(key="libya_rest", empire="ITALY", origin=(15.0, 31.0), color=ITC, clip=box(9.0, 18.0, 26.0, 30.7), src="M"),
           dict(key="china", empire="REPUBLIC OF CHINA", origin=(118.8, 32.05), color=(205, 45, 55), src="M"),
           dict(key="serbia", empire="SERBIA", origin=(21.9, 43.3), color=(170, 90, 90), src="M"),
           dict(key="montenegro", empire="MONTENEGRO", origin=(19.26, 42.44), color=(150, 120, 180), src="M"),
           dict(key="greece", empire="GREECE", origin=(22.4, 39.6), color=(100, 160, 220), src="M"),
           dict(key="bulgaria", empire="BULGARIA", origin=(25.6, 42.2), color=(110, 160, 90), src="M"),
           dict(key="albania", empire="ALBANIA", origin=(19.45, 41.32), color=(240, 145, 60), src="M"),
           dict(key="morocco", empire="FRENCH EMPIRE", origin=(-7.6, 33.6), color=(60, 95, 200), clip=box(-14.0, 27.0, -1.0, 36.0), src="M")])
grp(M, B, [dict(key="greece2", empire="GREECE", origin=(23.0, 40.8), color=(100, 160, 220), src="B"),
           dict(key="edirne", empire="OTTOMAN THRACE", origin=(28.9, 41.05), color=(200, 60, 60), src="B"),
           dict(key="dobruja", empire="ROMANIA", origin=(27.0, 44.3), color=(220, 190, 80), src="B")])
grp(B, W, [dict(key="occ", empire="GERMAN-OCCUPIED", origin=(6.1, 50.6), color=(190, 50, 55), src="W")])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep22_hd.pkl", "wb")); print(list(regs))
