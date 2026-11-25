"""Builds the worlds for Episode 30 (Year 1953: the Cold War begins) from the September-1945 world (ep29_world).
1950 = June 1950 (eve of the Korean War): West Germany (23 May 1949) and East Germany (7 Oct 1949), the Saar under France,
       Austria still occupied (shown as Austria), the People's Republic of China (1 Oct 1949) without Tibet (taken 1950-51),
       the Nationalists on Taiwan (Dec 1949), Korea split at the 38th parallel (two states since 1948), India and Pakistan (1947),
       Burma and Ceylon (1948), Indonesia (Dec 1949), the Philippines (1946), Jordan, Syria, Lebanon, Iraq and Israel independent.
       Libya still under British/French administration (independent 24 Dec 1951).
1950k1 = early September 1950: North Korea holds all of the South except the Pusan Perimeter (Naktong river line, Masan-Waegwan-Pohang).
1950k2 = late November 1950: UN forces hold most of the North (Chongchon river in the west, Chosin, X Corps up to Hyesanjin and the NE).
1950k3 = mid-January 1951: after the Chinese Third Phase Offensive the line runs near the 37th parallel (Pyongtaek - Wonju - Samchok).
1953 = after the armistice (27 July 1953): Korea divided along the armistice line (DMZ), Tibet inside the PRC, Libya independent.
Country shapes snap to the historical-basemaps dataset world_1960 (A. Ourednik, GPL-3.0); the new states use that dataset's shapes as
rough polygons, the 38th-parallel split uses the world_1945 Korea shapes as OVERLAY entries."""
import ep29_world as _W29
import ep26_world as _W26

SOV = (130, 175, 95); PRC = (205, 60, 60); ROC = (225, 185, 85); NKC = (130, 175, 95); SKC = (150, 190, 250)
FRC = (60, 95, 200)
_ds = _W26._ds
# the dataset leaves the Jiangsu-Zhejiang-Fujian coast blank
CHINA_COAST = [(118.8, 35.2), (120.3, 34.8), (121.3, 33.0), (122.3, 31.6), (122.3, 30.0), (121.9, 28.5), (120.9, 27.0), (119.8, 25.5),
               (118.5, 24.4), (117.5, 24.8), (118.6, 27.0), (119.5, 29.5), (119.6, 31.5), (119.2, 33.5)]
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]

DROP = {"GERMANY", "POLAND", "SOVIET-OCCUPIED POLAND", "SOVIET UNION", "ESTONIA", "LATVIA", "LITHUANIA", "SLOVAKIA", "HUNGARY",
        "ROMANIA", "YUGOSLAVIA", "ALBANIA", "BULGARIA", "FINLAND", "SOVIET KARELIA", "SOVIET BESSARABIA", "SOVIET ZONE", "AMERICAN ZONE",
        "BRITISH ZONE", "FRENCH ZONE", "AUSTRIA", "CZECHOSLOVAKIA", "POSTWAR POLAND", "SOVIET EAST PRUSSIA", "SOVIET RUTHENIA",
        "SOVIET SAKHALIN", "SOVIET-OCCUPIED MANCHURIA", "SOVIET-OCCUPIED KOREA", "US-OCCUPIED KOREA", "REPUBLIC OF CHINA", "JAPAN",
        "MONGOLIA"}

# Korean War front lines (approximate rough polygons, clipped to Korea by the OVERLAY victims)
PUSAN = [(128.3, 34.6), (128.35, 35.2), (128.45, 35.6), (128.4, 36.0), (128.7, 36.2), (129.0, 36.15), (129.4, 36.1), (129.8, 36.1), (129.8, 34.6)]
UN_NORTH = [(123.8, 39.68), (125.0, 39.66), (125.6, 39.75), (126.3, 39.9), (126.9, 40.4), (127.4, 40.9), (128.2, 41.45), (129.0, 41.6),
            (129.8, 41.9), (130.6, 41.9), (130.6, 37.5), (123.8, 37.5)]
RED_SOUTH = [(124.0, 38.8), (130.0, 38.8), (130.0, 37.35), (129.2, 37.35), (128.6, 37.25), (127.95, 37.3), (127.5, 37.1), (127.0, 37.0),
             (126.5, 36.95), (124.0, 36.95)]


def build(year, stage=0):
    """year: 1950 or 1953; stage (1950 only): 0 = June 1950, 1 = Pusan Perimeter, 2 = UN at the Yalu, 3 = January 1951."""
    base, ov29 = _W29.build(1945)
    out = []; ov = {}
    for n, c, p, q in base:
        if n in DROP: continue
        if year >= 1953 and n in ("BRITISH-HELD LIBYA", "BRITISH-HELD EAST AFRICA"): continue
        out.append((n, c, list(p), q))
        if n in ov29 and ov29[n]: ov[n] = [v for v in ov29[n] if v not in DROP] or None
    def add(name, col, polys, pos=(0, 0), victims="-"):
        out.append((name, col, polys, pos))
        if victims != "-": ov[name] = victims
    D = lambda nm: _ds(1960, nm)
    # Europe: the Iron Curtain world
    add("SOVIET UNION", SOV, D("USSR"), (45.0, 56.0)); add("FINLAND", (215, 225, 240), D("Finland"), (26.0, 63.0))
    add("POLAND", (225, 80, 90), D("Poland"), (19.4, 52.1)); add("CZECHOSLOVAKIA", (120, 165, 225), D("Czechoslovakia"), (15.5, 49.8))
    add("HUNGARY", (120, 170, 110), D("Hungary"), (19.3, 47.1)); add("ROMANIA", (220, 190, 80), D("Romania"), (25.0, 45.8))
    add("BULGARIA", (110, 160, 90), D("Bulgaria"), (25.3, 42.7)); add("YUGOSLAVIA", (170, 120, 190), D("Yugoslavia"), (18.5, 44.3))
    add("ALBANIA", (110, 185, 150), D("Albania"), (20.0, 41.0)); add("AUSTRIA", (215, 215, 225), D("Austria"), (14.6, 47.6))
    add("EAST GERMANY", (165, 200, 120), D("East Germany"), (12.6, 52.3)); add("WEST GERMANY", (225, 205, 110), D("West Germany"), (9.2, 50.6))
    add("SAAR", FRC, _ds(1945, "Saar Protectorate"), victims=["WEST GERMANY"])
    # Asia
    add("JAPAN", (235, 95, 70), D("Japan"), (138.5, 37.0)); add("MONGOLIA", (90, 150, 190), D("Mongolia"), (103.0, 47.0))
    add("PEOPLE'S REPUBLIC OF CHINA", PRC, D("China") + [CHINA_COAST] + (D("Tibet") if year >= 1953 else []), (104.0, 33.0))
    if year < 1953: add("TIBET", (190, 150, 120), D("Tibet"), (88.0, 31.5))
    add("TAIWAN", ROC, D("Taiwan"), (121.0, 23.7))
    add("INDIA", (240, 160, 60), D("India"), (79.0, 22.0)); add("PAKISTAN", (70, 150, 90), D("Pakistan"), (69.0, 29.0))
    add("BURMA", (200, 160, 90), D("Burma"), (96.0, 21.0)); add("CEYLON", (220, 120, 100), D("Sri Lanka"), (80.7, 7.8))
    add("INDONESIA", (215, 70, 80), D("Indonesia"), (114.0, -1.0)); add("PHILIPPINES", (90, 130, 210), D("Philippines"), (122.0, 12.5))
    # Middle East (shown without labels)
    for nm, col in (("Israel", (170, 190, 230)), ("Jordan", (200, 160, 110)), ("Syria", (190, 120, 110)), ("Lebanon", (230, 180, 160)),
                    ("Iraq", (160, 140, 90))):
        add(nm.upper(), col, D(nm))
    if year >= 1953:
        add("LIBYA", (200, 170, 110), D("Libya"), (17.0, 27.0))
        add("ERITREA", (120, 190, 110), D("Eritrea"))      # federated with Ethiopia, Sept 1952
        add("NORTH KOREA", NKC, D("Korea, Democratic People's Republic of"), (127.0, 40.3))
        add("SOUTH KOREA", SKC, D("Korea, Republic of"), (128.0, 36.3))
    else:
        nk, sk = D("Korea, Democratic People's Republic of"), D("Korea, Republic of")
        add("NORTH KOREA", NKC, nk, (127.0, 40.3)); add("SOUTH KOREA", SKC, sk, (128.0, 36.3))
        # the 1948-50 border was the 38th parallel, not the later armistice line
        add("NORTH OF 38", NKC, _ds(1945, "Korea (USSR)"), victims=["SOUTH KOREA"])
        add("SOUTH OF 38", SKC, _ds(1945, "Korea (USA)"), victims=["NORTH KOREA"])
        if stage == 1:
            south = _W26._clip([BOX(124.0, 33.0, 130.5, 38.7)], 1945, ["Korea (USA)"])
            from shapely.geometry import Polygon
            pus = Polygon(PUSAN)
            keep = []
            for r in south:
                g = Polygon(r).buffer(0).difference(pus)
                for pp in (g.geoms if hasattr(g, "geoms") else [g]):
                    if pp.area > 0.002: keep.append([(float(x), float(y)) for x, y in pp.exterior.coords])
            add("NORTH KOREAN-HELD SOUTH", NKC, keep, victims=["SOUTH KOREA", "NORTH KOREA"])
        if stage == 2:
            add("UN-HELD NORTH", SKC, _W26._clip([UN_NORTH], 1960, ["Korea, Democratic People's Republic of", "Korea, Republic of"]), victims=["SOUTH KOREA", "NORTH KOREA"])
        if stage == 4:   # colour source for all Korean War reveals: the whole South in the North's colour, the whole North in UN blue
            add("SOUTH IN RED HANDS", NKC, sk + _ds(1945, "Korea (USA)"), victims=["SOUTH KOREA", "NORTH KOREA"])
            add("NORTH IN UN HANDS", SKC, nk + _ds(1945, "Korea (USSR)"), victims=["SOUTH KOREA", "NORTH KOREA"])
        if stage == 3:
            add("COMMUNIST-HELD SOUTH", NKC, _W26._clip([RED_SOUTH], 1960, ["Korea, Democratic People's Republic of", "Korea, Republic of"]), victims=["SOUTH KOREA", "NORTH KOREA"])
    return out, ov
