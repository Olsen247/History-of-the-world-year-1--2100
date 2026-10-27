"""Year 1776: as 1770, plus the first partition of Poland (1772: Russia takes Polish Livonia and eastern Belarus, Prussia takes Royal
Prussia, Austria takes Galicia), Spanish San Francisco (June 1776) and the thirteen colonies declaring independence as the United States
(4 July 1776; the war with Britain goes on until 1783)."""
from ep16_geo import *
import world_data_1770 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_chg = ("RUSSIAN EMPIRE", "PRUSSIA", "HABSBURG MONARCHY", "SPAIN")
EMPIRES = [e for e in _P.EMPIRES if e[0] not in _chg] + [
    ("RUSSIAN EMPIRE", (120, 170, 90), P_("RUSSIAN EMPIRE") + [RU_PART1], (40.0, 57.0)),
    ("HABSBURG MONARCHY", (240, 225, 120), P_("HABSBURG MONARCHY") + [AT_GALICIA], (16.0, 48.6)),
    ("PRUSSIA", (60, 70, 90), P_("PRUSSIA") + [PR_ROYAL], (13.4, 52.6)),
    ("SPAIN", (235, 180, 40), P_("SPAIN") + [SP_SANFRAN], (-4.0, 40.0)),
    ("UNITED STATES", (80, 125, 215), [GB_COLONIES, EN_VIRGINIA, EN_MARYLAND, EN_NE], (-78.0, 38.5)),
]
CULTURES = []
