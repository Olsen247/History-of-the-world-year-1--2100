import sys; sys.path.insert(0, "/home/claude/shortgen")
import hist_engine3 as E, fx as FX
FX.set_year(1700)
DUR = 8.0
keys = [(0, 2.5, 49.5, 520), (DUR, 2.5, 49.5, 520)]
fx = [dict(type="march", path=[(-1.0, 51.3), (0.5, 51.0), (1.8, 50.9), (2.8, 50.6)], t0=0.5, t1=4.0, color=(200, 40, 50), kind="line"),
      dict(type="march", path=[(7.5, 49.0), (6.0, 48.8), (4.5, 48.6)], t0=0.5, t1=4.0, color=(40, 70, 170), kind="napoleonic"),
      dict(type="march", path=[(-2, 47.5), (-0.5, 47.5), (1, 47.8)], t0=0.5, t1=4.0, color=(30, 120, 60), kind="conquistador"),
      dict(type="vehicle", kind="train", path=[(2.35, 48.86), (3.5, 47.8), (4.4, 46.9), (4.85, 45.76)], t0=0.5, t1=5.0),
      dict(type="vehicle", kind="jet", path=[(-4, 49), (0, 49.6), (6, 50.5)], t0=1.0, t1=5.0),
      dict(type="vehicle", kind="rocket", path=[(-1.5, 46.5)], t0=1.0, t1=6.0, until=8.0, height=500),
      dict(type="vehicle", kind="steamer", path=[(-5, 48.0), (-3.0, 49.0), (-1.5, 49.9)], t0=0.5, t1=5.0),
      dict(type="cities", cities=[(2.35, 48.86, 1.4), (-0.12, 51.5, 1.5), (4.85, 45.76, .8), (4.35, 50.85, .8), (5.37, 43.3, .8)], t0=0.3, t1=2.0)]
CFG = dict(episode=0, dur=DUR, base_a="/home/claude/shortgen/hd_1914a.png", base_b="/home/claude/shortgen/hd_1914a.png", regions=None,
           keys=keys, routes=[], base_switches=[], reveals=[], labels=[], pins=[], cards=[], ticker=[(0, 1914), (DUR, 1914)], header_in=0.3,
           header_out=DUR, rewind=[], hook=lambda fr, t: None, outro=lambda fr, t: None, headings=[], emblems=[], vig_strength=lambda t: 0.7,
           fx=fx, flashes=[])
E.setup(CFG)
if __name__ == "__main__": E.main(sys.argv)
