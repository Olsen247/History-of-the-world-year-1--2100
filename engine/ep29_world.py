"""Builds the worlds for Episode 29 (Year 1945: the Second World War, part 4) from the July-1943 world (ep28_world).
1944 = late December 1944 (Battle of the Bulge, Budapest encircled 26 Dec): France, Belgium and Luxembourg liberated, the southern
       Netherlands freed (Sept-Nov 1944); Italy split at the Gothic Line (Ravenna taken 4 Dec 1944), the Germans holding the north;
       the Red Army on the East Prussian border, the Narew and the Vistula (Praga, Magnuszew, Pulawy and Sandomierz bridgeheads),
       the Germans cut off in Courland; Finland out of the war (Moscow armistice 19 Sept 1944: the 1940 border plus Petsamo);
       Bessarabia back to the USSR; northern Transylvania back to Romania; eastern Hungary and Carpathian Ruthenia held by the Red
       Army; Belgrade (20 Oct 1944), Serbia, Macedonia and Montenegro freed by the Partisans; Greece freed (Oct 1944).
1945 = September 1945: Germany split into four occupation zones, Austria re-created, Poland moved west to the Oder-Neisse line,
       northern East Prussia, eastern Poland and Carpathian Ruthenia to the USSR, Czechoslovakia restored, Yugoslavia restored;
       Japan's conquests gone, Manchuria and northern Korea under Soviet occupation, southern Korea under US occupation,
       southern Sakhalin to the USSR.
Country shapes snap to the historical-basemaps dataset world_1930 (A. Ourednik, GPL-3.0); the 1945 zones and new borders use that
dataset's world_1945 shapes as rough polygons. Occupation zones are OVERLAY entries that only replace the victims' land."""
import ep28_world as _W28
import ep27_world as _W27
import ep26_world as _W26

GER = (110, 110, 122); SOV = (130, 175, 95); JAP = (235, 95, 70); ITA = (110, 185, 150); USC = (150, 190, 250)
BRC = (235, 125, 165); FRC = (60, 95, 200); POLC = (225, 80, 90); SLO = (120, 165, 225); YUG = (170, 120, 190)
GRC = (100, 160, 220); AUT = (215, 215, 225)
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]

GOTHIC = [(6.0, 47.3), (15.6, 47.3), (15.6, 44.7), (13.0, 44.7), (12.35, 44.45), (12.2, 44.38), (12.0, 44.33), (11.6, 44.25), (11.3, 44.24),
          (11.0, 44.15), (10.6, 44.08), (10.25, 43.92), (9.5, 43.9), (6.0, 43.5)]
COURLAND = [(20.8, 57.75), (22.7, 57.8), (23.3, 57.1), (23.25, 56.75), (22.9, 56.45), (22.0, 56.35), (20.8, 56.0)]
# Soviet-held Poland west of the Bug, 1 January 1945: Narew bridgeheads, Praga, the Vistula with the Magnuszew, Pulawy and
# Sandomierz bridgeheads, then south to the Carpathians near Jaslo
PL_SOV = [(23.9, 54.45), (22.8, 54.36), (22.4, 53.9), (21.9, 53.3), (21.45, 52.9), (21.05, 52.45), (21.02, 52.2), (21.1, 51.95),
          (20.95, 51.8), (21.3, 51.65), (21.75, 51.45), (21.85, 51.2), (21.35, 50.85), (21.0, 50.55), (21.25, 50.25), (21.4, 49.9),
          (21.5, 49.45), (22.6, 49.0), (24.5, 49.0), (24.5, 54.45)]
HU_SOV = [(22.1, 49.4), (25.5, 49.4), (25.5, 45.5), (17.0, 45.7), (17.2, 46.4), (17.4, 46.8), (18.0, 47.05), (18.4, 47.2), (18.8, 47.45),
          (18.9, 47.7), (19.3, 47.9), (20.0, 48.1), (20.8, 48.35), (21.6, 48.6)]
YU_FREE = [(19.35, 46.2), (23.2, 46.2), (23.2, 40.8), (20.4, 40.8), (19.3, 41.9), (18.9, 42.5), (19.3, 43.2), (19.45, 44.0), (19.3, 44.9)]
PETSAMO = [(27.5, 70.2), (31.8, 70.2), (31.8, 68.9), (28.6, 68.9)]
S_SAKHALIN = BOX(141.4, 45.8, 145.0, 54.5)


def _eu(nm):
    return [r for r in _W26._ds(1930, nm) if -5 < sum(x for x, y in r) / len(r) < 32 and sum(y for x, y in r) / len(r) < 72]


def _box_cut(polys, box):
    from shapely.geometry import Polygon
    out = []
    for pts in polys:
        g = Polygon(pts).buffer(0).intersection(Polygon(box))
        for p in (g.geoms if hasattr(g, "geoms") else [g]):
            if isinstance(p, Polygon) and p.area > 0.002: out.append([(float(x), float(y)) for x, y in p.exterior.coords])
    return out


def build(year):
    """year: 1944 or 1945. Returns (EMPIRES, OVERLAY)."""
    base, ov28 = _W28.build(1943)
    drop = {"OCCUPIED FRANCE", "OCCUPIED BELGIUM", "OCCUPIED LUXEMBOURG", "GERMAN-OCCUPIED USSR", "FINNISH-HELD KARELIA",
            "HUNGARIAN TRANSYLVANIA"}
    if year >= 1945:
        drop |= {"OCCUPIED NORWAY", "OCCUPIED DENMARK", "OCCUPIED NETHERLANDS", "BOHEMIA-MORAVIA", "GERMAN-OCCUPIED POLAND",
                 "JAPANESE CONQUESTS", "JAPANESE-OCCUPIED CHINA", "DANZIG"}
    out = []; ov = {}
    for n, c, p, q in base:
        if n in drop: continue
        if n == "OCCUPIED GREECE": n, c = "GREECE", GRC
        if n == "OCCUPIED NETHERLANDS": p = _box_cut(p, BOX(3.0, 51.8, 8.0, 54.0))   # the south is free by November 1944
        if year >= 1945:
            if n == "OCCUPIED YUGOSLAVIA": n, c = "YUGOSLAVIA", YUG
            if n == "HUNGARIAN RUTHENIA": n, c = "SOVIET RUTHENIA", SOV
            if n == "MANCHUKUO": n, c = "SOVIET-OCCUPIED MANCHURIA", SOV
        out.append((n, c, list(p), q))
        if n in ov28: ov[n] = ov28[n]
    def add(name, col, polys, pos, victims=None):
        out.append((name, col, polys, pos)); ov[name] = victims
    add("SOVIET KARELIA", SOV, [_W27.KARELIA_40, PETSAMO], (30.5, 61.4), ["FINLAND"])
    add("SOVIET BESSARABIA", SOV, [_W27.BESSARABIA], (28.6, 47.0), ["ROMANIA"])
    if year == 1944:
        add("GERMAN-OCCUPIED ITALY", GER, [GOTHIC], (10.5, 45.4), ["ITALY"])
        add("GERMAN-HELD COURLAND", GER, [COURLAND], (22.0, 57.0), ["LATVIA"])
        add("SOVIET-HELD POLAND", SOV, [PL_SOV], (22.6, 51.8), ["GERMAN-OCCUPIED POLAND"])
        add("SOVIET-HELD HUNGARY", SOV, [HU_SOV], (20.6, 46.9), ["HUNGARY", "HUNGARIAN RUTHENIA"])
        add("LIBERATED YUGOSLAVIA", YUG, [YU_FREE], (21.0, 43.6), ["OCCUPIED YUGOSLAVIA"])
    else:
        ger = ["GERMANY", "DANZIG", "GERMAN-OCCUPIED POLAND", "BOHEMIA-MORAVIA"]
        add("SOVIET ZONE", SOV, _W26._ds(1945, "Germany (Soviet)"), (12.5, 52.3), ["GERMANY"])
        add("AMERICAN ZONE", USC, _W26._ds(1945, "Germany (USA)"), (10.8, 49.3), ["GERMANY"])
        add("BRITISH ZONE", BRC, _W26._ds(1945, "Germany (UK)"), (8.7, 52.5), ["GERMANY"])
        add("FRENCH ZONE", FRC, _W26._ds(1945, "Germany (France)") + _W26._ds(1945, "Saar Protectorate"), (7.9, 48.6), ["GERMANY"])
        add("AUSTRIA", AUT, _W26._ds(1945, "Austria"), (14.6, 47.6), ["GERMANY"])
        add("CZECHOSLOVAKIA", SLO, _W26._ds(1945, "Czechoslovakia"), (15.5, 49.8), ger + ["SLOVAKIA", "SOVIET RUTHENIA"])
        add("POSTWAR POLAND", POLC, _W26._ds(1945, "Poland"), (19.1, 52.0), ger + ["SOVIET-OCCUPIED POLAND", "POLAND"])
        add("SOVIET EAST PRUSSIA", SOV, _box_cut(_W26._ds(1945, "USSR"), BOX(19.3, 54.2, 23.0, 55.4)), (21.0, 54.8), ["GERMANY", "LITHUANIA"])
        add("SOVIET-OCCUPIED KOREA", SOV, _W26._ds(1945, "Korea (USSR)"), (126.8, 40.3), ["JAPAN"])
        add("US-OCCUPIED KOREA", USC, _W26._ds(1945, "Korea (USA)"), (127.9, 36.2), ["JAPAN"])
        add("SOVIET SAKHALIN", SOV, [S_SAKHALIN], (142.7, 47.5))
    return out, ov
