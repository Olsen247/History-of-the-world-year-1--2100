"""Demo: modern-war overlay (WWI western front 1914) on our normal map."""
import sys
import hist_engine3 as E
from hist_engine3 import GOLD, WHITE
DUR = 15.0
keys = [(0.0, 4.0, 50.0, 900), (1.2, 4.0, 50.0, 900), (3.0, 5.0, 50.0, 380), (8.0, 4.0, 49.6, 380), (9.6, 2.0, 51.2, 520),
        (12.6, 2.4, 50.6, 440), (DUR, 2.4, 50.6, 440)]
P0 = [(6.05, 51.0), (6.1, 50.6), (6.35, 50.15), (6.3, 49.5), (6.4, 49.0), (6.9, 48.5), (7.1, 47.7)]
P1 = [(2.8, 51.1), (2.85, 50.5), (2.8, 49.95), (3.3, 49.38), (4.6, 49.25), (5.6, 48.95), (7.0, 47.75)]
DE = ["de1914"]; AL = ["be", "uk", "fr", "fr", "fr", "fr", "fr"]
fx = [dict(type="front", path0=P0, path1=P1, t_in=1.4, t_out=DUR, move0=2.6, move1=7.8, side_a=DE, side_b=AL, by_segment=True, rows=2),
      dict(type="boom", pos=(5.57, 50.63), t0=3.0, swords=False, scale=0.36),
      dict(type="boom", pos=(4.87, 50.47), t0=4.1, swords=False, scale=0.32),
      dict(type="boom", pos=(3.3, 50.3), t0=5.4, swords=False, scale=0.32),
      dict(type="boom", pos=(3.4, 49.0), t0=7.0, swords=False, scale=0.45),
      dict(type="boom", pos=(2.9, 50.85), t0=12.2, swords=False, scale=0.36),
      dict(type="vehicle", kind="plane", path=[(7.5, 50.2), (5.5, 49.9), (3.6, 49.6), (2.35, 48.86)], t0=3.2, t1=7.4),
      dict(type="vehicle", kind="plane", path=[(1.0, 50.4), (2.5, 50.0), (4.0, 49.75)], t0=5.0, t1=8.2, scale=0.9),
      dict(type="vehicle", kind="airship", path=[(8.0, 53.6), (5.0, 53.2), (2.0, 52.4), (-0.12, 51.5)], t0=8.6, t1=12.4),
      dict(type="vehicle", kind="warship", path=[(-1.0, 50.6), (0.6, 50.3), (1.5, 50.6), (2.2, 51.05)], t0=9.0, t1=13.5, scale=0.9),
      dict(type="vehicle", kind="warship", path=[(4.5, 54.6), (3.0, 53.6), (2.4, 52.6)], t0=9.4, t1=13.8, scale=0.9),
      dict(type="glow", pos=(4.6, 51.6), t0=8.0, t1=11.0, radius=300, a0=50, a1=120)]
labels = [dict(text="GERMAN\nEMPIRE", pos=(9.0, 51.3), kind="emp", color=(190, 50, 55), t_in=0.6),
          dict(text="FRANCE", pos=(2.0, 47.6), kind="emp", color=(70, 110, 200), t_in=0.6),
          dict(text="BELGIUM", pos=(4.7, 50.7), kind="small", color=(235, 195, 60), t_in=0.6, t_out=2.6),
          dict(text="BRITAIN", pos=(-1.6, 52.6), kind="mid", color=(210, 90, 120), t_in=0.6),
          dict(text="LIÈGE", pos=(5.9, 51.35), kind="event", color=GOLD, t_in=2.8, t_out=4.4),
          dict(text="THE MARNE", pos=(3.3, 48.55), kind="event", color=GOLD, t_in=6.8, t_out=9.0),
          dict(text="LONDON", pos=(-0.12, 51.85), kind="event", color=GOLD, t_in=11.0, t_out=13.5),
          dict(text="YPRES", pos=(2.0, 50.75), kind="event", color=GOLD, t_in=12.0, t_out=DUR)]
RRED = (232, 64, 72)
headings = [dict(t0=0.4, t1=5.6, l1="YEAR 1914", l2="THE GREAT WAR", c2=RRED),
            dict(t0=5.8, t1=9.6, l1="SEPTEMBER 1914", l2="THE MARNE", c2=RRED),
            dict(t0=9.8, t1=DUR, l1="THE WESTERN FRONT", l2="ZEPPELINS OVER LONDON", c2=GOLD)]
CFG = dict(episode=0, dur=DUR, base_a="/home/claude/shortgen/hd_1914a.png", base_b="/home/claude/shortgen/hd_1914b.png",
           regions="/home/claude/shortgen/regions_demo1914.pkl", keys=keys, routes=[], base_switches=[(8.0, 8.4, "A", "B")],
           reveals=[dict(key="occ", t0=2.6, t1=7.8, until=1e9)], labels=labels, pins=[], cards=[],
           ticker=[(0, 1914), (DUR, 1914)], header_in=0.3, header_out=DUR, rewind=[], hook=lambda fr, t: None, outro=lambda fr, t: None,
           headings=headings, emblems=[], vig_strength=lambda t: 0.7, fx=fx, flashes=[(3.0, 0.15), (7.0, 0.2)])
E.setup(CFG)
if __name__ == "__main__":
    E.main(sys.argv)
