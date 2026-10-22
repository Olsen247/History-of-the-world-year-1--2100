"""Year 1492 (late): Granada is Castilian, Muscovy has swallowed Novgorod, the Ottomans hold the Balkans to the Danube, Songhai rules the Niger bend,
the Aq Qoyunlu rule Persia, and the Inca and Aztec empires are at their height."""
from ep11_geo import *
import world_data_1453b as _P
EXCLUSIVE = True
_drop = ("GRANADA", "NOVGOROD", "SERBIAN DESPOTATE", "TREBIZOND", "QARA QOYUNLU", "AQ QOYUNLU", "OTTOMAN EMPIRE", "INCA EMPIRE", "AZTEC EMPIRE")
def _mod(e):
    if e[0] == "CASTILE": return (e[0], e[1], e[2] + [GRANADA], e[3])
    if e[0] == "RUS PRINCIPALITIES": return ("MUSCOVY", (120, 170, 90), e[2] + [NOVGOROD], (38, 57))
    if e[0] == "MARINIDS": return ("WATTASIDS",) + e[1:]
    return e
EMPIRES = [_mod(e) for e in _P.EMPIRES if e[0] not in _drop] + [
    ("AQ QOYUNLU", (230, 230, 225), [AQ_Q, QARA_Q], (48, 34)),
    ("SONGHAI EMPIRE", (200, 110, 60), [SONGHAI], (-1.0, 15.6)),
    ("AZTEC EMPIRE", (60, 160, 150), [AZTEC_1492], (-98.6, 18.6)),
    ("INCA EMPIRE", (235, 105, 35), [INCA_1492], (-71.0, -17.0)),
    ("OTTOMAN EMPIRE", (200, 60, 60), [OTT_EU_1492, OTT_AN_1492], (31.5, 39.6))]
CULTURES = [c for c in _P.CULTURES if c[0] not in ("Karaman", "Chimor")]
