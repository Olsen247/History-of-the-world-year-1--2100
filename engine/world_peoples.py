"""Peoples and cultures of the whole world through time, so the map never looks empty or one-sided.
Each entry: (label, lon, lat, start_year, end_year). Shown as small "culture" labels wherever no empire polygon
already covers that spot. Viewer feedback (Ep 6): show the Celtic Britons, Picts and Gaels, not only the Anglo-Saxons.
Use:  import world_peoples as WP
      labels += WP.labels(B, 1453, t_in=s[1] + 0.8, t_out=s[12])     # B = the year module shown on the map
"""
PEOPLES = [
    # ---- Europe ----
    ("Germanic tribes", 10.5, 52.5, -100, 480), ("Sarmatians", 40, 47.5, -300, 370), ("Dacians", 25, 46, -100, 106),
    ("Britons", -3.8, 52.4, 400, 900), ("Welsh kingdoms", -3.8, 52.4, 900, 1282), ("Picts", -4.0, 57.3, 297, 900),
    ("Gaels", -5.6, 56.4, 500, 850), ("Irish kingdoms", -8.0, 53.3, 400, 1171), ("Britons of Strathclyde", -4.4, 55.6, 450, 1030),
    ("Cornish Britons", -4.9, 50.4, 450, 880), ("Basques", -2.2, 43.0, 400, 824), ("Sámi", 22, 68.5, -500, 1700),
    ("Finnic peoples", 26, 62, -500, 1150), ("Balts", 24, 55.5, -500, 1230), ("Old Prussians", 20.6, 54.3, 900, 1283),
    ("Slavs", 28, 52, 500, 880), ("Magyars", 36, 48, 830, 895), ("Volga Bulgars", 49, 55, 700, 1236), ("Avars", 20, 47, 567, 796),
    # ---- Africa ----
    ("Berber tribes", 2, 30, -500, 1900), ("Garamantes", 14, 26, -500, 700), ("Kush", 33, 17, -800, 350),
    ("Bantu peoples", 25, -5, -500, 1885), ("Khoisan peoples", 20, -27, -500, 1800), ("Swahili city-states", 39.6, -6.5, 800, 1500),
    ("Great Zimbabwe", 31, -20, 1100, 1450), ("Yoruba states", 4.3, 7.8, 1000, 1830), ("Benin", 5.8, 6.4, 1180, 1897),
    ("Hausa states", 8.5, 12.0, 1000, 1808), ("Kanem-Bornu", 14.5, 13.5, 700, 1893), ("Malagasy peoples", 46.5, -19, 600, 1895),
    ("Nok culture", 8, 9.5, -1000, 300), ("Tuareg", 5, 21, 600, 1900), ("Somali clans", 46, 6, 900, 1880),
    # ---- Asia ----
    ("Xiongnu", 105, 46, -200, 155), ("Xianbei", 115, 45, 155, 400), ("Rouran", 105, 45, 400, 555), ("Göktürks", 90, 47, 552, 744),
    ("Uyghurs", 100, 47, 744, 840), ("Kyrgyz", 92, 52, 840, 925), ("Tibetans", 90, 32, 1, 600), ("Arab tribes", 45, 23, -500, 630),
    ("Wa (Japan)", 133, 34, 1, 250), ("Emishi", 141, 39.5, 1, 800), ("Ainu", 142.8, 43.3, 800, 1869),
    ("Siberian peoples", 100, 62, -500, 1650), ("Yakuts", 128, 63, 1300, 1630), ("Chukchi", 172, 66, 1, 1800),
    ("Funan", 105, 11, 100, 550), ("Champa", 108.5, 14, 192, 1471), ("Srivijaya", 104, -3, 670, 1290), ("Pyu city-states", 95.5, 19.5, 1, 849),
    ("Dvaravati", 100.5, 14, 600, 1100), ("Rajput kingdoms", 74, 26, 750, 1800), ("Anuradhapura", 80.5, 8.3, -400, 1017),
    ("Tamil kingdoms", 78.5, 10, -300, 300), ("Naga peoples", 94.5, 26, 1, 1800), ("Bedouin tribes", 42, 27, 630, 1900),
    # ---- Americas ----
    ("Maya city-states", -89.5, 17.2, -500, 1697), ("Zapotecs", -96.7, 17.1, -500, 900), ("Teotihuacan", -98.8, 19.7, 100, 550),
    ("Toltecs", -99.3, 20.1, 900, 1150), ("Mixtecs", -97.6, 17.4, 900, 1520), ("Purépecha", -101.6, 19.6, 1300, 1530),
    ("Hopewell culture", -83, 39.3, -100, 500), ("Mississippian culture", -90, 37.5, 800, 1600), ("Ancestral Puebloans", -108, 36.5, 700, 1600),
    ("Plains peoples", -102, 42, -500, 1890), ("Eastern Woodlands peoples", -80, 41, -500, 1450), ("Haudenosaunee", -76, 43, 1450, 1800),
    ("Northwest Coast peoples", -126, 53, -500, 1880), ("Dorset culture", -76, 64, -500, 1300), ("Inuit (Thule)", -95, 68, 1000, 1900),
    ("Taíno", -71, 19, 600, 1520), ("Caribs", -61.2, 13.5, 1000, 1700), ("Muisca", -73.6, 5.3, 600, 1540),
    ("Moche", -79, -8, 100, 700), ("Nazca", -75, -14.8, -100, 700), ("Tiwanaku", -68.7, -16.5, 500, 1000), ("Wari", -74, -13, 600, 1000),
    ("Chimú", -79, -8, 900, 1470), ("Mapuche", -72, -38.5, -500, 1883), ("Tupi peoples", -48, -14, -500, 1700),
    ("Amazonian peoples", -62, -4, -500, 1900), ("Patagonian peoples", -68, -46, -500, 1885),
    # ---- Oceania ----
    ("Aboriginal Australians", 134, -25, -500, 1900), ("Papuan peoples", 143, -6, -500, 1900), ("Lapita / Polynesians", -175, -17, -500, 900),
    ("Tongans & Samoans", -173.5, -15.5, 900, 1900), ("Hawaiians", -157, 20.5, 900, 1898), ("Rapa Nui", -109.4, -27.1, 1100, 1888),
    ("Māori", 174.5, -39, 1280, 1900), ("Chamorro", 144.8, 13.4, 1, 1668),
    # ---- added Ep 13 (Magellan's route) ----
    ("Visayan chiefdoms", 125.6, 12.3, 900, 1565), ("Moluccan sultanates", 127.6, 0.6, 1250, 1680), ("Kingdom of Kongo", 14.5, -6.0, 1390, 1857),
    # ---- added Ep 15 (1533-1642) ----
    ("Gaelic lordships", -7.6, 54.6, 1171, 1607), ("Nogai Horde", 52, 46.8, 1440, 1634), ("Kalmyks", 53, 47.5, 1630, 1771),
    ("Kazakh Khanate", 68, 47.5, 1465, 1847), ("Tibetan kingdoms", 90, 31.5, 1300, 1642), ("Tibet", 90, 31.5, 1642, 1951),
    ("Lan Xang", 102.6, 19.9, 1353, 1707), ("Aceh Sultanate", 96.5, 4.3, 1496, 1903), ("Johor Sultanate", 103.6, 1.9, 1528, 1855),
    ("Brunei", 114.8, 4.5, 1368, 1888), ("Gowa (Makassar)", 119.6, -5.2, 1300, 1669), ("Ndongo", 15.8, -9.6, 1500, 1671),
    ("Mutapa", 31.5, -17.0, 1430, 1760), ("Swahili coast", 39.8, -5.0, 1500, 1890), ("Pashalik of Timbuktu", -2.5, 16.6, 1612, 1833),
    ("Dendi (Songhai)", 3.2, 12.5, 1591, 1901), ("Mande kingdoms", -8.5, 12.3, 1610, 1712), ("Pueblo peoples", -108.8, 35.6, 1600, 1900),
    ("Apache & Navajo", -110.5, 33.8, 1500, 1886), ("Algonquian peoples", -78, 45.5, 1450, 1850), ("Cherokee", -84, 35.3, 1600, 1838),
    ("Guaraní", -54.5, -27.5, 1500, 1900), ("Aboriginal Tasmanians", 146.6, -42.0, -500, 1876), ("Wik peoples", 142.6, -15.0, -500, 1900),
]

def _inside(pt, poly):
    x, y = pt; inside = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / ((y2 - y1) or 1e-9) + x1: inside = not inside
    return inside

def labels(data, year, t_in, t_out, skip=()):
    """Culture labels for `year`, leaving out any spot covered by an empire polygon of the year module `data`
    and any name the module already shows (EMPIRES or CULTURES)."""
    shown = {n.lower() for n, *_ in getattr(data, "EMPIRES", [])} | {c[0].lower() for c in getattr(data, "CULTURES", [])}
    polys = [p for _, _, ps, _ in getattr(data, "EMPIRES", []) for p in ps]
    out = []
    for name, lon, lat, a, b in PEOPLES:
        if not (a <= year < b) or name.lower() in shown or name in skip: continue
        if any(_inside((lon, lat), p) for p in polys): continue
        out.append(dict(text=name, pos=(lon, lat), kind="culture", t_in=t_in, t_out=t_out))
    return out
