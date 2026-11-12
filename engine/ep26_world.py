"""Builds the worlds for Episode 26 (Year 1939: the road to the Second World War) from the end-1922 world (ep25_world).
1931 = the world of 1929-31 (before Manchuria): the 1922 world, Republic of China recoloured so it differs from Japan.
1937 = end of 1937: Manchukuo (1932), Italian East Africa (Ethiopia, May 1936), Spain split into the Nationalist zone and the
       Republic (front of autumn 1937, after the fall of the north), Japanese-occupied north China and Shanghai-Nanjing.
1938 = after Munich (Oct 1938): Austria inside Germany (12-13 March 1938), the Sudetenland (1-10 Oct 1938), the Republic
       cut in two (April 1938), Japan holding Wuhan and Canton (Oct 1938).
1939 = end of September 1939: Bohemia-Moravia occupied (15 March 1939), Slovakia, Carpathian Ruthenia to Hungary,
       Albania under Italy (April 1939), all of Spain under Franco (1 April 1939), Poland divided between Germany and the
       USSR along the Pisa-Narew-Bug-San line (28 September 1939).
Country shapes snap to the historical-basemaps dataset world_1930 (A. Ourednik, GPL-3.0).
Front lines and occupation zones are approximate rough polygons drawn as OVERLAY entries on the victim's land."""
import ep25_world as _W25

GER = (110, 110, 122); SOV = (130, 175, 95); JAP = (235, 95, 70); CHN = (225, 185, 85); ITA = (110, 185, 150)
NAT = (140, 110, 70); REP = (170, 60, 110); SLO = (120, 165, 225)
HB = "/home/claude/shortgen/hb/world_%d.geojson"

def _ds(year, name):
    import json
    for ft in json.load(open(HB % year))["features"]:
        if (ft.get("properties") or {}).get("NAME") == name and ft.get("geometry"):
            return _W25._rings(ft["geometry"])
    return []

# --- Spain -------------------------------------------------------------------------------------------------------------------
SPAIN_CUT = [(-12.0, 44.5), (5.0, 44.5), (5.0, 35.0), (-12.0, 35.0)]
REP_1937 = [(3.4, 42.5), (1.5, 42.7), (0.7, 42.85), (0.0, 42.75), (-0.2, 42.3), (-0.4, 41.6), (-0.8, 41.0), (-1.1, 40.45),
            (-1.8, 40.15), (-2.5, 40.5), (-2.8, 40.9), (-3.5, 40.95), (-4.0, 40.6), (-3.85, 40.35), (-4.4, 40.0), (-4.6, 39.3),
            (-5.3, 38.9), (-5.0, 38.4), (-4.6, 38.3), (-4.4, 37.9), (-4.2, 37.4), (-3.4, 37.4), (-3.3, 37.0), (-2.9, 36.6),
            (-2.0, 36.4), (-0.6, 37.4), (0.0, 38.6), (0.4, 39.5), (0.8, 40.6), (1.6, 40.9), (2.6, 41.3), (3.6, 41.9)]
REP_1938 = [[(3.4, 42.5), (1.5, 42.7), (0.7, 42.85), (0.65, 42.0), (0.5, 41.4), (0.6, 41.0), (1.0, 40.7), (1.6, 40.9), (2.6, 41.3), (3.6, 41.9)],
            [(0.3, 39.75), (-0.8, 40.0), (-1.5, 40.2), (-2.5, 40.5), (-2.8, 40.9), (-3.5, 40.95), (-4.0, 40.6), (-3.85, 40.35), (-4.4, 40.0),
             (-4.6, 39.3), (-4.9, 38.9), (-4.6, 38.3), (-4.4, 37.9), (-4.2, 37.4), (-3.4, 37.4), (-3.3, 37.0), (-2.9, 36.6), (-2.0, 36.4),
             (-0.6, 37.4), (0.0, 38.6), (0.4, 39.4)]]
# --- China ---------------------------------------------------------------------------------------------------------------------
JC_1937 = [[(109.8, 40.6), (111.7, 41.6), (115.0, 42.2), (117.8, 41.0), (119.8, 40.0), (118.6, 38.9), (117.9, 38.2), (118.9, 37.6),
            (117.6, 37.0), (116.6, 36.4), (115.4, 36.0), (114.3, 36.2), (113.5, 37.1), (112.6, 37.5), (111.5, 38.3), (110.6, 39.5)],
           [(122.0, 31.6), (121.0, 32.1), (119.5, 32.4), (118.5, 32.4), (118.3, 31.7), (119.0, 31.0), (119.8, 30.5), (120.2, 30.0),
            (121.0, 30.5), (122.0, 30.8)]]
JC_1938 = [[(109.5, 41.0), (112.0, 41.9), (115.5, 42.3), (119.8, 40.0), (118.6, 38.9), (118.8, 37.6), (122.8, 37.4), (120.5, 35.9),
            (119.5, 35.0), (120.6, 33.4), (122.0, 31.6), (122.0, 30.8), (120.6, 29.9), (119.5, 30.5), (118.3, 30.7), (117.0, 30.4),
            (116.0, 29.7), (115.4, 29.6), (114.2, 29.6), (113.2, 29.4), (112.5, 30.3), (112.5, 31.4), (113.4, 32.0), (114.4, 32.9),
            (114.8, 33.6), (114.5, 34.7), (113.0, 35.2), (112.0, 35.3), (111.0, 35.7), (111.2, 37.2), (111.0, 38.4), (110.6, 39.4)],
           [(112.8, 23.7), (114.3, 23.7), (114.6, 22.7), (113.7, 22.1), (112.8, 22.5)]]
HAINAN = [(108.5, 19.3), (109.6, 20.2), (110.7, 20.2), (111.2, 19.6), (110.6, 18.6), (109.5, 18.1), (108.6, 18.5)]
# --- Central Europe ------------------------------------------------------------------------------------------------------------
SUDETEN = [(16.95, 48.65), (16.0, 48.7), (15.0, 48.9), (14.6, 48.55), (14.0, 48.55), (13.4, 48.85), (12.7, 49.3), (12.3, 49.7),
           (12.0, 50.2), (12.4, 50.45), (13.0, 50.55), (13.8, 50.8), (14.4, 51.1), (15.0, 51.15), (15.5, 50.85), (16.3, 50.75),
           (16.9, 50.3), (17.4, 50.45), (17.8, 50.15), (18.1, 49.95),
           (17.9, 49.8), (17.5, 49.8), (17.1, 49.95), (16.6, 49.85), (16.1, 50.15), (15.7, 50.45), (15.0, 50.6), (14.4, 50.45),
           (13.8, 50.25), (13.25, 50.05), (13.05, 49.8), (13.35, 49.4), (13.9, 49.05), (14.6, 48.9), (15.1, 49.1), (15.9, 48.95), (16.9, 48.9)]
BOHEMIA_MORAVIA = [(11.5, 51.6), (19.2, 51.6), (18.85, 49.5), (18.2, 49.3), (17.9, 48.95), (17.4, 48.75), (16.95, 48.5), (11.5, 48.3)]
RUTHENIA = [(22.15, 49.3), (25.5, 49.3), (25.5, 47.6), (22.15, 47.6)]
POL_DE = [(13.0, 55.5), (21.9, 55.5), (21.9, 53.45), (21.6, 52.9), (22.0, 52.6), (23.0, 52.3), (23.65, 52.08), (23.55, 51.55),
          (23.75, 51.0), (24.1, 50.6), (23.4, 50.3), (22.8, 49.8), (22.7, 49.0), (13.0, 49.0)]
POL_SU = [(21.0, 57.0), (33.0, 57.0), (33.0, 47.0), (21.0, 47.0)]


def _clip(polys, year, names):
    """Intersect rough polygons with the dataset shapes of the victim(s), so overlays never cut into neighbours."""
    from shapely.geometry import Polygon, MultiPolygon
    from shapely.ops import unary_union
    vic = unary_union([Polygon(r).buffer(0) for nm in names for r in _ds(year, nm)]).buffer(0.02)
    out = []
    for pts in polys:
        g = Polygon(pts).buffer(0).intersection(vic)
        for p in (g.geoms if hasattr(g, "geoms") else [g]):
            if isinstance(p, Polygon) and p.area > 0.002: out.append([(float(x), float(y)) for x, y in p.exterior.coords])
    return out


def build(year):
    """year: 1931, 1937, 1938 or 1939. Returns (EMPIRES, OVERLAY)."""
    base = _W25.build(1922)
    out = []
    for n, c, p, q in base:
        if n == "GERMAN EMPIRE": n, c = "GERMANY", GER
        if n == "OTTOMAN EMPIRE": n = "TURKEY"
        if n == "REPUBLIC OF CHINA":   # rough polygons have gaps; add the exact 1930 shape + the Jiangsu coast the dataset misses
            c = CHN; p = list(p) + _ds(1930, "Chinese Warlords") + [[(118.8, 35.2), (120.2, 34.6), (121.2, 33.0), (122.2, 31.6), (121.9, 30.7),
                                                                       (120.5, 30.2), (119.6, 31.5), (119.2, 33.5)]]
        if n == "SPAIN" and year >= 1937: c = NAT if year == 1939 else (235, 180, 40)
        out.append((n, c, list(p), q))
    ov = {}
    D = 1930      # all four maps use the 1930 dataset (the 1938 file leaves holes in China and north of Korea)
    def add(name, col, polys, pos, victims=None):
        out.append((name, col, polys, pos)); ov[name] = victims
    if year >= 1937:
        out.append(("MANCHUKUO", JAP, _ds(1930, "Manchuria"), (125.0, 45.0)))
        out = [(("ITALIAN EAST AFRICA", ITA, p, q) if n == "ETHIOPIA" else (n, c, p, q)) for n, c, p, q in out]
    if year in (1937, 1938):
        # Nationalist zone = Spain minus the Republic (Republic is drawn last so it wins)
        add("NATIONALISTS", NAT, _clip([SPAIN_CUT], D, ["Spain"]), (-5.5, 39.5), ["SPAIN"])
        add("REPUBLIC", (235, 180, 40), _clip(REP_1938 if year == 1938 else [REP_1937], D, ["Spain"]), (-1.5, 39.2), ["SPAIN", "NATIONALISTS"])
    if year == 1937:
        add("JAPANESE-OCCUPIED CHINA", JAP, JC_1937, (116.0, 38.0), ["REPUBLIC OF CHINA"])
    if year >= 1938:
        add("JAPANESE-OCCUPIED CHINA", JAP, JC_1938 + ([HAINAN] if year == 1939 else []), (116.0, 35.0), ["REPUBLIC OF CHINA"])
        out = [(n, c, p + (_ds(1930, "Austria") if n == "GERMANY" else []), q) for n, c, p, q in out if n != "AUSTRIA"]
    if year == 1938:
        add("SUDETENLAND", GER, _clip([SUDETEN], D, ["Czechoslovakia"]), (14.0, 50.5), ["CZECHOSLOVAKIA"])
    if year == 1939:
        out = [(("SLOVAKIA", SLO, p, (19.5, 48.7)) if n == "CZECHOSLOVAKIA" else (n, c, p, q)) for n, c, p, q in out]
        out = [((n, ITA, p, q) if n == "ALBANIA" else (n, c, p, q)) for n, c, p, q in out]
        add("BOHEMIA-MORAVIA", GER, _clip([BOHEMIA_MORAVIA], D, ["Czechoslovakia"]), (15.3, 49.8), ["SLOVAKIA"])
        add("HUNGARIAN RUTHENIA", (120, 170, 110), _clip([RUTHENIA], D, ["Czechoslovakia"]), (23.3, 48.4), ["SLOVAKIA"])
        add("SOVIET-OCCUPIED POLAND", SOV, _clip([POL_SU], D, ["Poland"]), (26.0, 52.0), ["POLAND"])
        add("GERMAN-OCCUPIED POLAND", GER, _clip([POL_DE], D, ["Poland"]), (19.5, 52.0), ["POLAND", "SOVIET-OCCUPIED POLAND"])
    return out, ov
