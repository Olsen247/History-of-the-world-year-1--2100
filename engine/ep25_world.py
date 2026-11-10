"""Builds the worlds for Episode 25 (Year 1922) from the 11 November 1918 world (ep24_world, world_data_1918n).
1920 = the post-war map of 1920-21: the new states of central and eastern Europe (Poland, Czechoslovakia, the Kingdom of
       Serbs, Croats and Slovenes, Austria, Hungary, Estonia, Latvia, Lithuania, Finland), Versailles Germany (+ East Prussia),
       Greater Romania, the British and French mandates (Iraq, Palestine, Syria/Lebanon), the Ottoman rump state, Soviet Russia
       with the Ukrainian, Belarusian and Caucasus republics, and the last White territory in the south (Wrangel, 1920).
1922 = end of 1922: the Soviet Union (30 Dec 1922), Mustafa Kemal's Turkey (Anatolia + East Thrace after Mudanya),
       the Irish Free State (rough polygon – the dataset keeps Ireland inside the UK shape), Danzig as a Free City.
Country shapes are taken straight from the historical-basemaps dataset (world_1920 / world_1930, A. Ourednik, GPL-3.0),
so they snap exactly; the rest of the world is the 1918n world. EXCLUSIVE = True, later entries win overlaps."""
import json
import world_data_1918n as _N

HB = "/home/claude/shortgen/hb/world_%d.geojson"
SOV = (130, 175, 95)
COL = {"POLAND": (225, 80, 90), "CZECHOSLOVAKIA": (100, 150, 215), "KINGDOM OF SCS": (170, 90, 90), "AUSTRIA": (240, 225, 120),
       "HUNGARY": (120, 170, 110), "ESTONIA": (90, 130, 200), "LATVIA": (150, 110, 185), "LITHUANIA": (210, 175, 95),
       "FINLAND": (215, 225, 240), "GERMAN EMPIRE": (110, 110, 122), "ROMANIA": (220, 190, 80), "GREECE": (100, 160, 220),
       "BULGARIA": (110, 160, 90), "ALBANIA": (240, 145, 60), "OTTOMAN EMPIRE": (200, 60, 60), "BRITISH MANDATE": (235, 125, 165),
       "FRENCH MANDATE": (60, 95, 200), "HEJAZ": (70, 145, 75), "SOVIET UNION": SOV, "SOVIET UKRAINE": (150, 190, 110),
       "SOVIET BELARUS": (145, 185, 120), "CAUCASUS": (165, 195, 105), "FAR EASTERN REPUBLIC": (150, 180, 130),
       "WHITES": (225, 225, 215), "DANZIG": (200, 200, 200), "ITALY": (110, 185, 150), "IRISH FREE STATE": (60, 150, 80)}
POS = {"POLAND": (19.5, 52.2), "CZECHOSLOVAKIA": (17.0, 49.3), "KINGDOM OF SCS": (18.5, 44.3), "AUSTRIA": (14.3, 47.5),
       "HUNGARY": (19.3, 47.1), "ESTONIA": (25.8, 58.7), "LATVIA": (25.0, 56.9), "LITHUANIA": (23.9, 55.3), "FINLAND": (26.0, 63.0),
       "GERMAN EMPIRE": (10.5, 51.0), "SOVIET UNION": (45.0, 56.0), "OTTOMAN EMPIRE": (35.0, 39.0)}
COMMON = {"Poland": "POLAND", "Czechoslovakia": "CZECHOSLOVAKIA", "Yugoslavia": "KINGDOM OF SCS", "Austria": "AUSTRIA",
          "Hungary": "HUNGARY", "Estonia": "ESTONIA", "Latvia": "LATVIA", "Lithuania": "LITHUANIA", "Finland": "FINLAND",
          "Germany": "GERMAN EMPIRE", "East Prussia": "GERMAN EMPIRE", "Romania": "ROMANIA", "Greece": "GREECE",
          "Bulgaria": "BULGARIA", "Albania": "ALBANIA", "Italy": "ITALY",
          "Mandatory Palestine (GB)": "BRITISH MANDATE", "Mesopotamia (GB)": "BRITISH MANDATE", "Syria (France)": "FRENCH MANDATE",
          "Tanzania, United Republic of": "BRITISH MANDATE", "French Cameroons": "FRENCH MANDATE", "Hejaz": "HEJAZ",
          "USSR": "SOVIET UNION"}
Y1920 = dict(COMMON, **{"Ukraine": "SOVIET UKRAINE", "White Russia": "SOVIET BELARUS",
                        "Georgia": "CAUCASUS", "Armenia": "CAUCASUS", "Azerbaijan": "CAUCASUS", "South Russia": "WHITES",
                        "Far Eastern SSR": "FAR EASTERN REPUBLIC"})
Y1922 = dict(COMMON, **{"Republic of Turkey": "OTTOMAN EMPIRE", "Turkey": "OTTOMAN EMPIRE", "Ukraine": "SOVIET UNION",
                        "White Russia": "SOVIET UNION", "Georgia": "SOVIET UNION", "Armenia": "SOVIET UNION",
                        "Azerbaijan": "SOVIET UNION", "Far Eastern SSR": "SOVIET UNION", "Danzig": "DANZIG",
                        "Dodecanese Islands": "ITALY"})
DROP = {"AUSTRIA-HUNGARY", "GERMAN EMPIRE", "GERMAN-OCCUPIED", "GERMAN-OCCUPIED EAST", "BRITISH ZONES", "SERBIA", "MONTENEGRO",
        "OCCUPIED ROMANIA", "BRITISH MESOPOTAMIA", "ARAB REVOLT", "BRITISH PALESTINE", "FINLAND", "OCCUPIED EAST 1918",
        "BESSARABIA", "OTTOMAN THRACE", "OTTOMAN EMPIRE", "SOVIET RUSSIA", "ROMANIA", "GREECE", "BULGARIA", "ALBANIA"}
# Irish Free State (26 counties): the dataset leaves Ireland inside the UK shape, so it gets a rough polygon
IRELAND_FS = [(-10.6, 51.4), (-9.6, 51.45), (-8.2, 51.75), (-6.9, 52.1), (-6.2, 52.2), (-6.0, 53.0), (-6.1, 53.6), (-6.2, 54.02),
              (-6.35, 54.06), (-6.62, 54.05), (-6.72, 54.18), (-6.95, 54.4), (-7.1, 54.33), (-7.23, 54.2), (-7.45, 54.12), (-7.62, 54.15),
              (-7.88, 54.29), (-8.09, 54.48), (-7.83, 54.55), (-7.7, 54.62), (-7.6, 54.72), (-7.48, 54.83), (-7.42, 54.95), (-7.3, 55.05),
              (-7.1, 55.15), (-7.25, 55.4), (-7.6, 55.45), (-8.4, 55.3), (-8.8, 54.8), (-8.7, 54.3), (-10.1, 54.3), (-10.3, 53.4),
              (-10.2, 52.3)]


def _rings(geom):
    t, c = geom["type"], geom["coordinates"]
    rs = [c[0]] if t == "Polygon" else [p[0] for p in c] if t == "MultiPolygon" else []
    return [[(float(x), float(y)) for x, y, *_ in r] for r in rs if len(r) >= 3]


def build(year):
    """year: 1920 or 1922."""
    feats = json.load(open(HB % (1920 if year == 1920 else 1930)))["features"]
    mp = Y1920 if year == 1920 else Y1922
    groups = {}
    for ft in feats:
        nm = (ft.get("properties") or {}).get("NAME")
        if nm in mp and ft.get("geometry"):
            groups.setdefault(mp[nm], []).extend(_rings(ft["geometry"]))
    if year == 1920:
        # the Ottoman state of 1919-21 in Anatolia (Sèvres zones were never really held): the 1930 Turkey shape, with the Greek
        # zone around Smyrna and the French in Cilicia drawn on top; Italy's Sèvres zone in Anatolia is left out
        for ft in json.load(open(HB % 1930))["features"]:
            if (ft.get("properties") or {}).get("NAME") in ("Republic of Turkey", "Turkey") and ft.get("geometry"):
                groups.setdefault("OTTOMAN EMPIRE", []).extend(_rings(ft["geometry"]))
        # Greek-held land before Kemal's Great Offensive (Aug 1922): western Anatolia up to the Eskişehir-Afyon line, and East Thrace
        groups.setdefault("GREECE", []).extend([
            [(26.6, 40.4), (27.5, 40.5), (29.1, 40.45), (29.8, 40.15), (30.6, 39.85), (31.1, 39.3), (30.6, 38.6), (29.9, 38.2), (28.9, 37.9),
             (27.9, 37.7), (27.2, 37.7), (26.2, 38.3), (26.2, 39.4)],
            [(26.0, 40.6), (26.7, 40.45), (27.6, 40.98), (28.4, 41.05), (28.5, 41.5), (28.0, 41.8), (27.5, 42.0), (26.6, 41.9), (26.3, 41.7),
             (26.6, 41.3), (26.1, 40.9)]])
        groups["ITALY"] = [r for r in groups.get("ITALY", []) if sum(x for x, y in r) / len(r) < 20.0]
    out = [e for e in _N.EMPIRES if e[0] not in DROP]
    order = ["SOVIET UNION", "SOVIET UKRAINE", "SOVIET BELARUS", "CAUCASUS", "FAR EASTERN REPUBLIC", "WHITES", "FINLAND", "ESTONIA",
             "LATVIA", "LITHUANIA", "POLAND", "GERMAN EMPIRE", "DANZIG", "CZECHOSLOVAKIA", "AUSTRIA", "HUNGARY", "ROMANIA",
             "OTTOMAN EMPIRE", "KINGDOM OF SCS", "ALBANIA", "BULGARIA", "GREECE", "ITALY", "HEJAZ", "FRENCH MANDATE", "BRITISH MANDATE"]
    old = {e[0]: e for e in _N.EMPIRES}
    for nm in order:
        if nm not in groups: continue
        polys = groups[nm]
        if nm == "ITALY":      # keep Italy where it was in the list, add Trentino, Trieste, Istria (and the Dodecanese)
            out = [(n, c, list(p) + polys, q) if n == "ITALY" else (n, c, p, q) for n, c, p, q in out]
            continue
        out.append((nm, COL[nm], polys, POS.get(nm, old.get(nm, (nm, 0, 0, (0, 0)))[3])))
    if year == 1922:
        uk = [r for ft in feats if (ft.get("properties") or {}).get("NAME") == "United Kingdom of Great Britain and Ireland"
              for r in _rings(ft["geometry"]) if -11.0 < sum(x for x, y in r) / len(r) < 2.5 and sum(y for x, y in r) / len(r) > 49.5]
        out.append(("BRITAIN", (235, 125, 165), uk, (-1.6, 52.4)))
        out.append(("IRISH FREE STATE", COL["IRISH FREE STATE"], [IRELAND_FS], (-8.0, 53.3)))
    return out
