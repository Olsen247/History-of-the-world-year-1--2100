"""Year 1795: as 1776, plus the Peace of Paris (1783: the United States to the Mississippi, Florida back to Spain, Canada British);
Russia with the Crimea (1783), the Black Sea coast to the Dniester (1792) and the second and third partitions of Poland (1793, 1795);
Prussia with Greater Poland, Danzig and Warsaw; Austria with Krakow and Lublin (West Galicia); France with the Austrian Netherlands
(Oct 1795); the Batavian Republic (Jan 1795); British Sydney (1788); Qajar Persia."""
from ep18_geo import *
import world_data_1776 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_drop = ("POLISH-LITHUANIAN COMMONWEALTH", "CRIMEAN KHANATE", "RUSSIAN EMPIRE", "HABSBURG MONARCHY", "PRUSSIA", "SPAIN", "UNITED STATES", "FRANCE",
         "ZAND PERSIA", "DUTCH REPUBLIC", "GREAT BRITAIN")
EMPIRES = [e for e in _P.EMPIRES if e[0] not in _drop] + [
    ("QAJAR PERSIA", (60, 130, 160), P_("ZAND PERSIA"), (53.0, 32.5)),
    ("BATAVIAN REPUBLIC", (240, 140, 40), P_("DUTCH REPUBLIC"), (5.6, 52.4)),
    ("GREAT BRITAIN", (200, 70, 80), P_("GREAT BRITAIN") + [GB_NSW], (-1.6, 52.4)),
    ("FRANCE", (70, 110, 200), P_("FRANCE") + [HB_NETHERLANDS], (2.2, 46.9)),
    ("RUSSIAN EMPIRE", (120, 170, 90), P_("RUSSIAN EMPIRE") + P_("POLISH-LITHUANIAN COMMONWEALTH") + P_("CRIMEAN KHANATE") + [RU_YEDISAN], (40.0, 57.0)),
    ("HABSBURG MONARCHY", (240, 225, 120), [p for p in P_("HABSBURG MONARCHY") if p is not HB_NETHERLANDS] + [AT_P3], (16.0, 48.6)),
    ("PRUSSIA", (60, 70, 90), P_("PRUSSIA") + [PR_P23], (13.4, 52.6)),
    ("SPAIN", (235, 180, 40), P_("SPAIN") + [SP_FLORIDA_1783], (-4.0, 40.0)),
    ("UNITED STATES", (80, 125, 215), P_("UNITED STATES") + [US_1783], (-85.0, 38.0)),
]
CULTURES = []
