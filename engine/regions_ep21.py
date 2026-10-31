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
import types
import world_data_1911 as B1
del A, M, B
import world_data_1900 as A
B = B1
JPC = (235, 95, 70)
grp(A, B, [dict(key="boer", empire="BRITISH EMPIRE", origin=(29.0, -29.6), color=BRIT, clip=box(23.5, -31.5, 33.5, -21.5)),
           dict(key="kwantung", empire="JAPAN", origin=(121.3, 38.85), color=JPC, clip=box(120.0, 38.0, 123.0, 40.2)),
           dict(key="sakh", empire="JAPAN", origin=(142.7, 46.6), color=JPC, clip=box(141.0, 45.5, 146.0, 50.5)),
           dict(key="korea", empire="JAPAN", origin=(129.0, 35.1), color=JPC, clip=box(124.0, 33.0, 131.5, 43.5)),
           dict(key="congo", empire="BELGIAN CONGO", origin=(13.05, -5.85), color=(235, 195, 60)),
           dict(key="china_rev", empire="CHINESE REVOLUTION", origin=(114.3, 30.55), color=(205, 45, 55)),
           dict(key="mongolia", empire="MONGOLIA", origin=(106.9, 47.9), color=(90, 150, 190))])
A_noNO = types.SimpleNamespace(EMPIRES=[e for e in A.EMPIRES if e[0] != "NORWAY"], EXCLUSIVE=True, __name__="wd1900_noNO")
grp(A_noNO, B, [dict(key="norway", empire="NORWAY", origin=(10.75, 59.91), color=(150, 120, 200))])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep21_hd.pkl", "wb")); print(list(regs))
