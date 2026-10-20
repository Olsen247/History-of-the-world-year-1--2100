from ep9_geo import *
import world_data_1347 as _P
EXCLUSIVE = True
_dropE = ("DENMARK", "NORWAY", "SWEDEN", "BULGARIA", "SERBIAN EMPIRE", "BYZANTINE EMPIRE", "OTTOMANS")
_dropA = ("YUAN DYNASTY", "CHAGATAI KHANATE", "DELHI SULTANATE", "VIJAYANAGARA")
EMPIRES = [(("JOSEON",) + e[1:]) if e[0] == "GORYEO" else e for e in _P.EMPIRES if e[0] not in _dropE + _dropA] + [
    ("KALMAR UNION", (200, 60, 70), [DENMARK, NORWAY, ICELAND, NGREEN, SWEDEN, FINLAND], (14.5, 61.5)),
    ("SERBIAN DESPOTATE", (180, 70, 90), [SERB_DESP], (20.8, 43.8)),
    ("OTTOMAN EMPIRE", (200, 60, 60), [OTT_EU, OTT_AN], (25.5, 42.3)),
    ("BYZANTINE EMPIRE", BYZ, [BYZ_1405], (28.6, 41.25)),
    ("NORTHERN YUAN", MONG, [MONGOLIA], (104, 47)),
    ("MOGHULISTAN", (165, 120, 80), [CHAGATAI], (82, 43)),
    ("TIMURID EMPIRE", (90, 150, 170), [TIMURID], (60, 36)),
    ("MING DYNASTY", (215, 70, 60), [MING], (112, 31)),
    ("DELHI SULTANATE", (60, 140, 110), [DELHI_1405], (76.8, 29.2)),
    ("BAHMANI SULTANATE", (120, 170, 90), [BAHMANI], (77, 18.2)),
    ("VIJAYANAGARA", (190, 80, 70), [VIJAYA_1405], (77.6, 13.2)),
    ("BENGAL SULTANATE", (200, 140, 70), [BENGAL], (89.5, 24))]
CULTURES = [c for c in _P.CULTURES if c[0] not in ("Persian successor states",)] + [("Jurchens", (128, 46))]
