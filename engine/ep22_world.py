"""Builds the worlds for Episode 22 (Year 1914) from the Year 1911 world (ep21_world).
1913 = after the First Balkan War (Treaty of London, May 1913) + Italian Libya (Treaty of Ouchy, Oct 1912) + Republic of China (1912)
       + French Morocco (Treaty of Fez, 1912; Spanish zone in the north).
1914 = after the Second Balkan War (Treaty of Bucharest, Aug 1913; Constantinople, Sep 1913): Ottomans back in Edirne (Maritsa border),
       Greece to the Nestos (Kavala), Romania takes Southern Dobruja, Bulgaria keeps Pirin and Western Thrace.
1914w = December 1914: German-occupied Belgium, Luxembourg and north-eastern France (the Western Front line).
Polygons are approximate. EXCLUSIVE = True, later entries win overlaps."""
from ep20_geo import *
import ep21_world as _W
from world_data_1914occ import OCC

OT_EU_1913A = [(26.05, 40.75), (26.2, 40.05), (27.0, 40.6), (28.0, 41.0), (29.1, 41.0), (29.2, 41.25), (28.1, 41.62)]       # Enos-Midia line
OT_EU_1913B = [(26.05, 40.75), (26.35, 41.3), (26.3, 41.75), (26.6, 41.95), (27.6, 42.0), (28.0, 41.98), (29.2, 41.25), (29.1, 41.0),
               (28.0, 41.0), (27.0, 40.6), (26.2, 40.05)]                                                                 # Maritsa border, Edirne Ottoman
BG_THRACE_A = [(23.6, 41.3), (24.1, 41.5), (25.0, 41.4), (26.4, 41.7), (28.0, 41.95), (28.1, 41.62), (26.05, 40.75), (24.75, 40.85), (23.75, 40.75)]
BG_THRACE_B = [(24.6, 41.45), (25.0, 41.4), (26.4, 41.7), (26.3, 41.75), (26.35, 41.3), (26.05, 40.75), (24.75, 40.85)]
BG_PIRIN = [(23.0, 41.4), (23.6, 41.3), (24.0, 41.38), (24.6, 41.38), (24.6, 41.45), (24.0, 41.8), (23.0, 41.8)]
SR_GAIN = [(20.3, 43.25), (20.7, 43.2), (22.0, 42.3), (22.4, 42.3), (23.0, 41.4), (22.6, 41.15), (21.6, 41.1), (20.75, 40.9), (20.5, 41.4),
           (20.5, 42.2), (20.1, 42.55), (20.0, 43.0)]
MN_GAIN = [(19.2, 43.5), (19.9, 43.2), (20.3, 43.1), (20.3, 42.8), (20.1, 42.55), (19.7, 42.45), (19.4, 41.9), (19.0, 43.0)]
ALBANIA = [(19.35, 41.9), (19.7, 42.5), (20.05, 42.55), (20.5, 42.2), (20.5, 41.4), (20.75, 40.9), (21.0, 40.6), (20.7, 40.1), (20.1, 39.65),
           (19.95, 39.9), (19.3, 40.4), (19.4, 41.0)]
GR_GAIN_A = [(20.1, 39.65), (20.7, 40.1), (21.0, 40.6), (20.75, 40.9), (21.6, 41.1), (22.6, 41.15), (23.0, 41.35), (23.6, 41.3), (23.75, 40.75),
             (24.4, 40.15), (23.3, 39.9), (22.7, 39.9), (21.0, 39.1), (19.9, 39.6)]
GR_GAIN_B = [(23.6, 41.3), (24.0, 41.38), (24.6, 41.38), (24.75, 40.85), (23.75, 40.75)]
CRETE = box(23.4, 34.8, 26.4, 35.75)
S_DOBRUJA = [(26.5, 44.05), (27.5, 44.12), (28.6, 43.75), (28.2, 43.38), (27.0, 43.8)]
SP_MOROCCO = [(-6.3, 35.9), (-2.2, 35.2), (-2.9, 34.9), (-4.5, 34.9), (-6.0, 34.9), (-6.3, 35.2)]


def build(year):
    """year: 1913 (after the 1st Balkan War), 1914 (pre-war, after the 2nd), 19141 (December 1914, occupied west)."""
    E = _W.build(1911)
    out = []
    late = year >= 1914
    for n, col, polys, pos in E:
        if n == "CHINESE REVOLUTION": continue
        if n == "QING EMPIRE":
            rev = [e for e in E if e[0] == "CHINESE REVOLUTION"][0]
            n, col, polys, pos = "REPUBLIC OF CHINA", (205, 45, 55), polys + rev[2], (104.0, 33.0)
        if n == "OTTOMAN EMPIRE":
            polys = [p for p in polys if p is not OT_LIBYA and p is not OT_EU_1900] + [OT_EU_1913B if late else OT_EU_1913A]
        if n == "ITALY": polys = polys + [OT_LIBYA]
        if n == "FRENCH EMPIRE": polys = polys + [MOROCCO_1900]
        if n == "SPAIN": polys = polys + [SP_MOROCCO]
        if n == "MOROCCO": continue
        if n == "GREECE": polys = polys + [GR_GAIN_A, CRETE] + ([GR_GAIN_B] if late else [])
        if n == "BULGARIA": polys = polys + ([BG_THRACE_B, BG_PIRIN] if late else [BG_THRACE_A, BG_PIRIN])
        if n == "ROMANIA" and late: polys = polys + [S_DOBRUJA]
        if n == "SERBIA": polys = polys + [SR_GAIN]
        if n == "MONTENEGRO": polys = polys + [MN_GAIN]
        out.append((n, col, polys, pos))
        if n == "MONTENEGRO": out.append(("ALBANIA", (240, 145, 60), [ALBANIA], (20.0, 41.0)))
    # Spain must win its Moroccan zone over France: move SPAIN after FRENCH EMPIRE (it already is in the 1900 order).
    # Ottoman Edirne must beat Bulgaria (Bulgaria comes later): re-add the Ottoman Thrace polygon at the end in 1914.
    if late: out.append(("OTTOMAN THRACE", (200, 60, 60), [OT_EU_1913B], (27.5, 41.3)))
    if year == 19141: out.append(("GERMAN-OCCUPIED", (190, 50, 55), [OCC], (4.2, 50.0)))
    return out
