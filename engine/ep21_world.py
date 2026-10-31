"""Builds the Year 1911 world for Episode 21 from the Year 1900 world (ep20_world).
1900 -> 1911: Boer republics become British (1902; Union of South Africa 1910), Panama splits from Colombia (1903),
Japan takes the Kwantung lease and southern Sakhalin from Russia (1905) and annexes Korea (1910), Norway leaves the union
with Sweden (1905, already drawn as its own kingdom), Belgium annexes the Congo Free State (1908),
Wuchang uprising (Oct 1911): by December most provinces of central and southern China have broken away from the Qing (incl. Shaanxi and Shanxi), and Outer Mongolia declares independence (1 Dec 1911).
Order matters: EXCLUSIVE = True, later entries win overlaps."""
from ep20_geo import *
import ep20_world as _W

SAKH_S = [(141.6, 45.8), (143.8, 45.8), (144.6, 48.0), (144.3, 50.0), (141.6, 50.0)]
PANAMA = [(-82.9, 8.0), (-82.6, 9.6), (-79.5, 9.9), (-77.4, 8.7), (-77.2, 7.9), (-77.9, 7.2), (-80.0, 7.2), (-81.0, 7.6)]
CN_REVOLT = [(98.0, 28.0), (101.0, 33.0), (104.0, 34.3), (106.5, 35.0), (108.0, 38.0), (110.5, 40.2), (114.0, 40.4), (114.2, 36.2),
             (116.4, 34.6), (119.0, 35.0), (120.6, 34.4), (122.2, 31.0), (121.5, 28.0), (119.8, 25.4), (117.2, 23.5), (114.3, 22.4),
             (112.0, 21.4), (109.5, 20.0), (108.0, 21.5), (106.7, 22.8), (104.0, 22.7), (101.5, 21.2), (98.5, 24.0)]
BEL = (235, 195, 60)
OUTER_MONGOLIA = [(87.8, 49.2), (91.0, 50.5), (98.0, 52.0), (104.0, 50.3), (108.0, 49.5), (113.0, 50.0), (116.5, 49.8), (119.9, 46.7),
                  (116.0, 45.0), (111.9, 43.7), (107.0, 42.4), (103.0, 41.8), (96.3, 42.7), (91.0, 45.0)]


def build(year=1911):
    E = _W.build(1900)
    out = []
    by = {e[0]: e for e in E}
    korea = by["KOREAN EMPIRE"][2]
    for n, col, polys, pos in E:
        if n in ("TRANSVAAL", "ORANGE FREE STATE", "KOREAN EMPIRE"): continue
        if n == "BRITISH EMPIRE": polys = polys + [TRANSVAAL, ORANGE_FS]
        if n == "JAPAN": polys = polys + korea + [KWANTUNG, SAKH_S]
        if n == "RUSSIAN EMPIRE": polys = [p for p in polys if p is not KWANTUNG]
        if n == "CONGO FREE STATE": n, col, pos = "BELGIAN CONGO", BEL, (23.5, -2.5)
        out.append((n, col, polys, pos))
        if n == "QING EMPIRE": qing_i = len(out) - 1
        if n == "COLOMBIA": out.append(("PANAMA", (200, 90, 110), [PANAMA], (-80.2, 8.5)))
    # Japan must win over the Russian Sakhalin polygon: it already comes after Russia in the 1900 order.
    out.append(("MONGOLIA", (90, 150, 190), [OUTER_MONGOLIA], (103.0, 47.0)))   # independence declared 1 Dec 1911
    out.append(("CHINESE REVOLUTION", (205, 45, 55), [CN_REVOLT], (112.0, 28.5)))
    return out
