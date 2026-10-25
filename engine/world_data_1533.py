"""Year 1533 (late): Sweden + Finland under Gustav Vasa (Kalmar Union ended 1523), Denmark-Norway with Iceland and Greenland; the Mughal
Empire (Humayun) holds Kabul, Punjab and the Delhi-Agra plain to Jaunpur; the Delhi Sultanate is gone; the Ottomans keep Syrmia but
Buda and Iraq are not yet theirs (1541 / 1534); Spain holds a corridor in Peru from Tumbes to Cusco. The Inca Empire still holds the rest."""
from ep14_geo import *
import world_data_1522 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
_drop = ("KALMAR UNION", "DELHI SULTANATE", "KABUL", "OTTOMAN EMPIRE", "SPAIN")
_k = _e["KALMAR UNION"][2]
EMPIRES = [e for e in _P.EMPIRES if e[0] not in _drop] + [
    ("DENMARK-NORWAY", (200, 60, 70), [_k[0], _k[1], _k[2], _k[3]], (9.5, 61.8)),
    ("SWEDEN", (80, 130, 205), [_k[4], _k[5]], (15.8, 61.6)),
    ("MUGHAL EMPIRE", (40, 150, 95), [KABUL, MUGHAL_INDIA], (76.5, 28.6)),
    ("OTTOMAN EMPIRE", (200, 60, 60), _e["OTTOMAN EMPIRE"][2] + [SYRMIA], (33.0, 38.8)),
    ("SPAIN", (235, 180, 40), _e["SPAIN"][2] + [PERU_SP], (-4.0, 40.0))]
CULTURES = _P.CULTURES
