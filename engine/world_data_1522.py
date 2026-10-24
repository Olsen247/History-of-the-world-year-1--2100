"""Year 1522: Spain (Castile + Aragon + Naples under Charles V) holds the big Caribbean islands, Panama and – since August 1521 – the Aztec
heartland; Portugal has posts in Brazil, Hormuz, Goa and Malacca; the Safavids rule Iran and Iraq; the Ottomans have swallowed the
Mamluk Sultanate (1516-17) and east Anatolia; the Timurids are gone (Uzbeks in Transoxiana, Babur in Kabul). The Inca Empire still stands."""
from ep13_geo import *
import world_data_1498 as _P
EXCLUSIVE = True
_drop = ("CASTILE", "ARAGON", "KINGDOM OF NAPLES", "NAVARRE", "MAMLUK SULTANATE", "AQ QOYUNLU", "TIMURID EMPIRE", "AZTEC EMPIRE", "OTTOMAN EMPIRE", "PORTUGAL")
_e = {e[0]: e for e in _P.EMPIRES}
_spain = _e["CASTILE"][2] + _e["ARAGON"][2] + _e["KINGDOM OF NAPLES"][2] + _e["NAVARRE"][2] + CARIB + [NEW_SPAIN]
_port = _e["PORTUGAL"][2] + BRAZIL_POSTS + [GOA, MALACCA, HORMUZ]
EMPIRES = [e for e in _P.EMPIRES if e[0] not in _drop] + [
    ("UZBEK KHANATE", (90, 150, 170), [UZBEK], (64.5, 40.8)),
    ("KABUL", (150, 170, 80), [KABUL], (68.5, 33.6)),
    ("SAFAVID EMPIRE", (60, 150, 120), [SAFAVID_1522], (53.0, 32.5)),
    ("OTTOMAN EMPIRE", (200, 60, 60), _e["OTTOMAN EMPIRE"][2] + _e["MAMLUK SULTANATE"][2] + [OTT_EAST_1522], (33.0, 38.8)),
    ("SPAIN", (235, 180, 40), _spain, (-4.0, 40.0)),
    ("PORTUGAL", (80, 150, 90), _port, (-8.1, 39.6))]
CULTURES = _P.CULTURES
