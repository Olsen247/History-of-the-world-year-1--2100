"""Builds the worlds for Episode 27 (Year 1941: the Second World War, part 2) from the end-September-1939 world (ep26_world).
1940 = autumn 1940: Finland has ceded the Karelian Isthmus and Ladoga Karelia (Moscow peace, 13 March 1940); Denmark and Norway
       occupied (9 April - 10 June 1940); the Netherlands, Belgium and Luxembourg occupied (May 1940); northern and western France
       occupied (armistice 22 June 1940, demarcation line), Vichy keeps the south; the Baltic states annexed by the USSR (June-Aug 1940),
       Bessarabia and northern Bukovina taken by the USSR (28 June 1940), northern Transylvania to Hungary (30 Aug 1940).
1941 = early December 1941: Yugoslavia and Greece under Axis occupation (April-May 1941); Ethiopia freed (Haile Selassie back in
       Addis Ababa 5 May 1941) and the rest of Italian East Africa held by the British (Gondar fell 27 Nov 1941); the German front
       deep in the USSR (Leningrad besieged, Kalinin, outside Moscow, Tula, Kursk, Kharkov, Taganrog, most of Crimea) on 5 Dec 1941,
       Finland back on the Karelian Isthmus and in East Karelia up to the Svir; Bessarabia back to Romania.
Country shapes snap to the historical-basemaps dataset world_1930 (A. Ourednik, GPL-3.0). Occupation zones are approximate rough
polygons drawn as OVERLAY entries that only replace the victims' land."""
import ep26_world as _W26

GER = (110, 110, 122); SOV = (130, 175, 95); FIN = (235, 235, 245); HUN = (120, 170, 110); ROM = None
FRA = None
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]

FR_OCC = [(6.1, 46.15), (5.5, 46.6), (5.45, 47.05), (4.85, 46.78), (4.0, 46.6), (3.33, 46.56), (2.5, 46.9), (2.07, 47.22), (1.2, 47.2),
          (0.7, 46.9), (0.35, 46.3), (0.16, 45.65), (-0.2, 45.0), (-0.5, 43.9), (-1.24, 43.16), (-1.6, 43.0), (-6.0, 43.6), (-6.0, 49.8),
          (2.5, 51.6), (8.6, 49.5), (7.6, 47.55), (7.0, 47.4), (6.4, 46.5)]
KARELIA_40 = [(27.75, 60.5), (28.6, 61.0), (29.6, 61.3), (30.6, 61.9), (31.6, 62.4), (32.4, 62.9), (33.5, 62.9), (33.5, 59.8), (29.0, 59.8),
              (28.0, 60.2)]
BESSARABIA = [(25.0, 48.9), (25.0, 48.05), (25.9, 48.0), (26.7, 47.85), (27.4, 47.4), (28.05, 46.7), (28.15, 45.9), (28.2, 45.45),
              (29.9, 45.0), (31.5, 46.0), (31.5, 48.9)]
N_TRANSYLVANIA = [(21.9, 48.0), (22.0, 47.2), (22.5, 46.75), (23.2, 46.55), (23.8, 46.5), (24.5, 46.35), (25.4, 46.2), (26.1, 45.85),
                  (26.4, 46.4), (26.0, 47.0), (25.4, 47.5), (24.6, 47.95), (23.3, 48.2)]
# German front of 5 December 1941 (Leningrad besieged, Tikhvin, Volkhov, Ilmen, Demyansk, Kalinin, outside Moscow, Tula, Yelets,
# Kursk, Kharkov, Mius / Taganrog, Crimea except Sevastopol) – everything west of it inside the USSR is occupied
OSTFRONT = [(29.6, 59.9), (30.25, 59.82), (30.6, 59.86), (31.0, 59.95), (32.2, 59.95), (33.3, 59.7), (33.6, 59.5), (32.3, 59.0), (31.8, 58.6),
            (31.6, 58.3), (32.3, 57.9), (32.9, 57.5), (33.3, 57.0), (34.6, 56.8), (35.9, 56.9), (36.8, 56.6), (37.2, 56.3), (37.45, 56.05),
            (37.1, 55.75), (36.75, 55.45), (36.9, 55.1), (37.3, 54.85), (37.4, 54.3), (37.9, 54.1), (38.3, 53.6), (38.2, 53.1), (38.5, 52.6),
            (37.9, 52.2), (37.3, 51.7), (36.8, 51.1), (36.9, 50.5), (36.8, 50.0), (37.4, 49.4), (37.9, 48.7), (38.6, 48.0), (38.9, 47.3)]
OCC_USSR = [(20.0, 61.0), (27.8, 61.0), (28.6, 60.4), (29.3, 60.05)] + OSTFRONT + [(38.9, 46.9), (36.5, 45.6), (36.6, 45.1), (34.0, 44.4),
            (33.7, 44.65), (33.4, 44.5), (32.4, 45.3), (32.0, 46.0), (30.0, 45.6), (25.0, 44.0), (20.0, 44.0)]
SEVASTOPOL = [(33.35, 44.45), (33.95, 44.4), (33.95, 44.8), (33.45, 44.8)]
E_KARELIA = [(27.75, 60.5), (29.25, 60.2), (29.9, 60.15), (30.5, 60.45), (31.0, 60.75), (31.6, 61.6), (32.9, 60.85), (33.6, 60.9),
             (35.3, 61.1), (35.5, 61.8), (34.4, 62.9), (34.2, 63.5), (32.0, 64.0), (30.0, 64.2), (28.5, 63.0)]
# Barbarossa split for the reveals: summer advance (to the Dnieper / Smolensk) vs autumn advance (to Leningrad, Moscow, Rostov)
WEST_PART = BOX(15.0, 40.0, 31.5, 62.0)


def _occ():
    """Occupied-USSR polygon minus the neighbours (Finland, Romania with Bessarabia, Hungary, Germany, German-held Poland ...),
    so the rough shape never claims a neighbour's dataset shape."""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    nb = [Polygon(r).buffer(0) for nm in ("Finland", "Romania", "Hungary", "Czechoslovakia", "Germany", "East Prussia", "Danzig", "Bulgaria",
                                         "Yugoslavia", "Sweden", "Turkey") for r in _W26._ds(1930, nm)]
    nb.append(Polygon(_W26.POL_DE).buffer(0))
    g = Polygon(OCC_USSR).buffer(0).difference(unary_union(nb).buffer(0.03))
    return [[(float(x), float(y)) for x, y in p.exterior.coords] for p in (g.geoms if hasattr(g, "geoms") else [g]) if p.area > 0.01]


def build(year):
    """year: 1940 or 1941. Returns (EMPIRES, OVERLAY)."""
    base, ov26 = _W26.build(1939)
    out = []; ov = dict(ov26)
    def add(name, col, polys, pos, victims=None):
        out.append((name, col, polys, pos)); ov[name] = victims
    for n, c, p, q in base:
        if n in ("ESTONIA", "LATVIA", "LITHUANIA"): c = SOV
        if n == "DANZIG": c = GER
        if year >= 1941 and n == "KINGDOM OF SCS": n, c = "OCCUPIED YUGOSLAVIA", GER
        if year >= 1941 and n == "GREECE": n, c = "OCCUPIED GREECE", GER
        if year >= 1941 and n == "ITALIAN EAST AFRICA": n, c = "ETHIOPIA", (120, 190, 110)
        out.append((n, c, list(p), q))
    if year >= 1941:
        add("BRITISH-HELD EAST AFRICA", (235, 125, 165), _W26._ds(1930, "Eritrea") + _W26._ds(1930, "Italian Somaliland"), (45.0, 4.0), ["ITALY"])
    # only the European homelands (not Greenland, Iceland, Svalbard or the Dutch East Indies)
    eu = lambda nm: [r for r in _W26._ds(1930, nm) if -5 < sum(x for x, y in r) / len(r) < 32 and sum(y for x, y in r) / len(r) < 72]
    for nm in ("Denmark", "Norway", "Netherlands", "Belgium", "Luxembourg"):
        add("OCCUPIED " + nm.upper(), GER, eu(nm), dict(Denmark=(9.5, 56.0), Norway=(9.0, 61.0), Netherlands=(5.5, 52.2),
                                                         Belgium=(4.6, 50.6), Luxembourg=(6.1, 49.7))[nm], [nm.upper()])
    add("OCCUPIED FRANCE", GER, [FR_OCC], (1.0, 48.3), ["FRENCH EMPIRE"])
    if year == 1940:
        add("SOVIET KARELIA", SOV, [KARELIA_40], (31.0, 61.5), ["FINLAND"])
        add("SOVIET BESSARABIA", SOV, [BESSARABIA], (28.6, 47.0), ["ROMANIA"])
    add("HUNGARIAN TRANSYLVANIA", HUN, [N_TRANSYLVANIA], (24.0, 47.2), ["ROMANIA"])
    if year >= 1941:
        vic = ["SOVIET UNION", "POLAND", "ESTONIA", "LATVIA", "LITHUANIA", "SOVIET-OCCUPIED POLAND"]
        add("FINNISH-HELD KARELIA", FIN, [E_KARELIA], (32.5, 62.3), ["SOVIET UNION"])
        add("GERMAN-OCCUPIED USSR", GER, _occ(), (30.0, 53.0), vic)
        add("SEVASTOPOL", SOV, [SEVASTOPOL], (33.6, 44.6), ["GERMAN-OCCUPIED USSR", "SOVIET UNION"])
    return out, ov
