"""Year 1453 (after 29 May): Constantinople is Ottoman, England keeps only Calais, the early Inca empire, the Timurid west lost to the Qara Qoyunlu."""
from ep10_geo import *
import world_data_1405 as _P
EXCLUSIVE = True
_drop = ("BYZANTINE EMPIRE", "OTTOMAN EMPIRE", "TIMURID EMPIRE")
def _mod(e):
    if e[0] == "ENGLAND": return (e[0], e[1], [p for p in e[2] if p is not GASCONY] + [CALAIS], e[3])
    if e[0] == "PORTUGAL": return (e[0], e[1], e[2] + [CEUTA, MADEIRA, AZORES], e[3])
    if e[0] == "GOLDEN HORDE": return ("GREAT HORDE",) + e[1:]
    return e
EMPIRES = [_mod(e) for e in _P.EMPIRES if e[0] not in _drop] + [
    ("TIMURID EMPIRE", (90, 150, 170), [TIMURID_1453], (63, 36)),
    ("QARA QOYUNLU", (150, 90, 160), [QARA_Q], (48, 34)),
    ("AQ QOYUNLU", (230, 230, 225), [AQ_Q], (40.6, 38.3)),
    ("CRIMEAN KHANATE", (210, 170, 90), [CRIMEA_KH], (34.6, 46.0)),
    ("KAZAN KHANATE", (170, 130, 70), [KAZAN_KH], (50.0, 55.6)),
    ("INCA EMPIRE", (235, 105, 35), [INCA_1453], (-72.5, -14.2)),
    ("OTTOMAN EMPIRE", (200, 60, 60), [OTT_EU_1453, OTT_AN_1453], (31.5, 39.6))]
CULTURES = [c for c in _P.CULTURES if not c[0].startswith("Kingdom of Cusco")] + [("Karaman", (33.4, 37.6))]
CULTURES = [c for c in CULTURES if c[0] != "Anatolian beyliks"]
