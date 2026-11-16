"""Builds the worlds for Episode 28 (Year 1943: the Second World War, part 3) from the December-1941 world (ep27_world).
1942 = mid-November 1942, the Axis at its greatest extent: Japan holds Malaya and Singapore (15 Feb 1942), Hong Kong, the
       Philippines (Corregidor 6 May 1942), the Dutch East Indies (8 Mar 1942), Burma (May 1942), French Indochina (occupied
       1940-41), north-east New Guinea and New Britain (Rabaul); Germany holds all of France (Case Anton, 11 Nov 1942); the Axis
       holds western Egypt up to El Alamein; the German front runs from Leningrad past Rzhev and Voronezh along the Don to
       Stalingrad and into the Caucasus (Elista, Mozdok, Nalchik, Novorossiysk); Sevastopol fell in July 1942.
1943 = early July 1943 (eve of Kursk): North Africa in Allied hands (Tunisia surrendered 13 May 1943; Libya British-held); the
       German front after the winter retreats: Velikiye Luki and Rzhev lost, the Orel bulge, the Kursk salient held by the Red
       Army, Belgorod and Kharkov German, the Donets and the Mius; the Kuban bridgehead with Novorossiysk; Crimea German.
Country shapes snap to the historical-basemaps dataset world_1930 (A. Ourednik, GPL-3.0). Occupation zones are approximate rough
polygons drawn as OVERLAY entries that only replace the victims' land."""
import ep27_world as _W27
import ep26_world as _W26

GER = (110, 110, 122); SOV = (130, 175, 95); JAP = (235, 95, 70); ITA = (110, 185, 150); BRC = (235, 125, 165)
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]

NORTH = [(29.6, 59.9), (30.25, 59.82), (30.6, 59.86), (31.0, 59.9), (31.6, 59.45), (32.1, 59.35), (31.7, 58.9), (31.5, 58.5), (31.6, 58.05)]
FRONT_42 = NORTH + [(32.2, 58.0), (33.0, 57.6), (32.6, 57.1), (31.7, 57.0), (31.0, 56.6), (30.7, 56.2), (31.3, 55.8), (32.4, 56.2),
            (33.5, 56.6), (34.3, 56.4), (35.0, 56.0), (35.2, 55.5), (34.9, 55.1), (35.3, 54.6), (36.2, 53.9), (36.3, 53.4), (37.0, 53.1),
            (37.6, 52.5), (38.1, 52.0), (38.7, 51.7), (39.2, 51.7), (39.9, 51.0), (40.5, 50.2), (41.2, 49.75), (42.4, 49.65),
            (43.1, 49.4), (44.0, 49.05), (44.45, 48.85), (44.6, 48.7), (44.45, 48.45), (44.1, 47.9), (44.2, 47.0), (44.5, 46.3),
            (44.9, 45.9), (44.8, 45.2), (44.6, 44.2), (44.6, 43.7), (44.0, 43.4), (43.4, 43.35), (42.5, 43.3), (41.5, 43.5), (40.5, 43.7),
            (39.6, 44.05), (39.0, 44.35), (38.3, 44.55), (37.9, 44.6), (37.8, 44.5)]
FRONT_43 = NORTH + [(31.75, 57.2), (31.0, 56.7), (30.15, 56.45), (30.3, 56.0), (31.1, 55.6), (32.4, 55.3), (33.5, 54.9), (34.6, 54.3),
            (35.4, 53.95), (36.0, 53.8), (36.5, 53.5), (37.0, 53.2), (37.3, 52.8), (36.9, 52.35), (36.3, 52.2), (35.4, 52.1),
            (34.7, 52.15), (34.6, 51.8), (34.6, 51.4), (35.0, 50.95), (35.4, 50.6), (35.9, 50.55), (36.4, 50.75), (36.8, 50.7),
            (37.1, 50.3), (37.2, 49.9), (37.4, 49.4), (37.6, 49.1), (38.3, 48.85), (38.8, 48.5), (39.0, 48.1), (38.9, 47.6), (38.95, 47.25)]
COAST_42 = [(37.3, 44.3), (36.0, 44.6), (34.0, 44.3), (33.3, 44.35), (32.4, 45.3), (32.0, 46.0), (30.0, 45.6), (25.0, 44.0), (20.0, 44.0)]
COAST_43 = [(38.5, 46.9), (36.5, 45.6), (35.5, 45.3), (34.0, 44.3), (33.3, 44.35), (32.4, 45.3), (32.0, 46.0), (30.0, 45.6), (25.0, 44.0),
            (20.0, 44.0)]
KUBAN_43 = [(36.55, 45.45), (37.9, 45.45), (38.3, 45.1), (38.0, 44.75), (37.5, 44.55), (36.6, 44.95)]
HEAD = [(20.0, 61.0), (27.8, 61.0), (28.6, 60.4), (29.3, 60.05)]
AXIS_EGYPT = [(24.6, 31.9), (29.0, 31.0), (28.95, 30.85), (28.6, 29.4), (26.0, 29.0), (24.6, 29.0)]
BURMA = [(92.0, 28.5), (98.8, 28.5), (99.8, 21.0), (99.4, 15.0), (98.8, 9.8), (97.5, 9.8), (94.0, 15.5), (92.2, 20.5), (93.4, 22.0)]
NE_GUINEA = [(141.0, -2.4), (145.5, -3.8), (147.6, -5.9), (148.6, -8.6), (148.0, -9.2), (146.6, -7.6), (145.0, -6.2), (141.0, -4.6)]
NEW_BRITAIN = [(148.0, -6.5), (153.8, -6.5), (153.8, -2.2), (148.0, -2.2)]


def _occ(front, coast):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    nb = [Polygon(r).buffer(0) for nm in ("Finland", "Romania", "Hungary", "Czechoslovakia", "Germany", "East Prussia", "Danzig", "Bulgaria",
                                         "Yugoslavia", "Sweden", "Turkey") for r in _W26._ds(1930, nm)]
    nb.append(Polygon(_W26.POL_DE).buffer(0))
    g = Polygon(HEAD + front + coast).buffer(0).difference(unary_union(nb).buffer(0.03))
    return [[(float(x), float(y)) for x, y in p.exterior.coords] for p in (g.geoms if hasattr(g, "geoms") else [g]) if p.area > 0.01]


def build(year):
    """year: 1942 or 1943. Returns (EMPIRES, OVERLAY)."""
    base, ov27 = _W27.build(1941)
    out = []; ov = {}
    for n, c, p, q in base:
        if n in ("GERMAN-OCCUPIED USSR", "SEVASTOPOL"): continue
        if n == "OCCUPIED FRANCE":
            eu = [r for r in _W26._ds(1930, "France") if -6 < sum(x for x, y in r) / len(r) < 10 and 41 < sum(y for x, y in r) / len(r) < 52]
            p = eu
        out.append((n, c, list(p), q))
        if n in ov27: ov[n] = ov27[n]
    def add(name, col, polys, pos, victims=None):
        out.append((name, col, polys, pos)); ov[name] = victims
    jap = (_W26._ds(1930, "Malaysia") + _W26._ds(1930, "Brunei") + _W26._ds(1930, "Hong Kong") + _W26._ds(1930, "Dutch East Indies")
           + _W26._ds(1930, "Philippines") + _W26._ds(1930, "French Indo-China") + _W26._ds(1930, "Cochin China") + _W26._ds(1930, "Annam")
           + _W26._clip([BURMA], 1930, ["British Raj"]) + _W26._clip([NE_GUINEA, NEW_BRITAIN], 1930, ["Papua New Guinea"]))
    add("JAPANESE CONQUESTS", JAP, jap, (112.0, 2.0), ["BRITISH EMPIRE", "NETHERLANDS", "UNITED STATES", "FRENCH EMPIRE", "BRITAIN"])
    vic = ["SOVIET UNION", "POLAND", "ESTONIA", "LATVIA", "LITHUANIA", "SOVIET-OCCUPIED POLAND"]
    if year == 1942:
        add("AXIS-HELD EGYPT", ITA, _W26._clip([AXIS_EGYPT], 1930, ["Egypt"]), (26.5, 30.3), ["EGYPT"])
        add("GERMAN-OCCUPIED USSR", GER, _occ(FRONT_42, COAST_42), (32.0, 52.0), vic)
    else:
        add("BRITISH-HELD LIBYA", BRC, _W26._ds(1930, "Libya (IT)"), (18.0, 27.5), ["ITALY"])
        add("GERMAN-OCCUPIED USSR", GER, _occ(FRONT_43, COAST_43) + [KUBAN_43], (31.0, 52.5), vic)
    # Finnish-held Karelia stays Finnish (drawn after the German zone so it wins)
    fk = [e for e in out if e[0] == "FINNISH-HELD KARELIA"]
    out = [e for e in out if e[0] != "FINNISH-HELD KARELIA"] + fk
    return out, ov
