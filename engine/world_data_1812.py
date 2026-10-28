"""Year 1812 (June, before the invasion of Russia): Napoleon's French Empire (with the Netherlands, the Rhineland, the North Sea coast to
Lubeck, Piedmont, Tuscany, Rome and the Illyrian Provinces) and its client states: Confederation of the Rhine, Switzerland, Kingdom of
Italy, Kingdom of Naples, Duchy of Warsaw; Prussia and Austria cut down; Russia with Finland (1809), Georgia (1801) and Bessarabia
(May 1812); the United States with Louisiana (1803); Haiti (1804); Britain with the Cape (1806), Ceylon, Java (1811), the Dutch
islands and much of India (south, Orissa, Delhi and the Doab 1803); Sikh Empire; Vietnam (1802); Sokoto Caliphate; Kingdom of Hawaii
(1810). The Holy Roman Empire (1806) and the Papal States (1809) are gone; Spain is ruled by Joseph Bonaparte but fights on."""
from ep18_geo import *
import world_data_1795 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_c = lambda p: (sum(a for a, b in p) / len(p), sum(b for a, b in p) / len(p))
_italy = lambda p: 8 < _c(p)[0] < 19 and 36 < _c(p)[1] < 43
_drop = ("HOLY ROMAN EMPIRE", "PAPAL STATES", "GEORGIA", "DAI VIET", "MUGHAL EMPIRE", "BATAVIAN REPUBLIC", "GREAT BRITAIN", "FRANCE", "RUSSIAN EMPIRE",
         "HABSBURG MONARCHY", "PRUSSIA", "SPAIN", "UNITED STATES", "SWEDEN", "MYSORE", "AWADH", "HYDERABAD", "BORNU")
_sicily = [p for p in P_("SPAIN") if _italy(p) and _c(p)[1] < 38.5 and _c(p)[0] > 12]
_sardinia = [p for p in P_("SPAIN") if _italy(p) and _c(p)[0] < 10]
_dutch = P_("BATAVIAN REPUBLIC")
EMPIRES = [("CONFEDERATION OF THE RHINE", (150, 170, 220), P_("HOLY ROMAN EMPIRE"), (10.0, 50.0))] + \
          [e for e in _P.EMPIRES if e[0] not in _drop] + [
    ("BORNU", (180, 120, 80), P_("BORNU"), (14.5, 14.0)),
    ("SOKOTO CALIPHATE", (200, 170, 110), [SOKOTO], (7.0, 11.8)),
    ("VIETNAM", (200, 90, 80), P_("DAI VIET"), (105.4, 20.8)),
    ("SWEDEN", (80, 130, 205), P_("SWEDEN")[:1], (15.8, 61.6)),
    ("GREAT BRITAIN", (200, 70, 80), [p for p in P_("GREAT BRITAIN") if p is not GB_NSW] + [GB_NSW_1812, GB_VDL, GB_DOAB, GB_SOUTH] + _dutch[1:],
     (-1.6, 52.4)),
    ("MYSORE", (170, 90, 140), P_("MYSORE"), (76.4, 13.3)),
    ("AWADH", (150, 190, 110), P_("AWADH"), (81.0, 26.8)),
    ("HYDERABAD", (200, 160, 90), P_("HYDERABAD"), (79.2, 16.8)),
    ("SIKH EMPIRE", (230, 150, 60), [SIKH], (73.6, 31.8)),
    ("SPAIN", (235, 180, 40), [p for p in P_("SPAIN") if not _italy(p) and p is not SP_LOUISIANA] + [SP_TEXAS2], (-4.0, 40.0)),
    ("KINGDOM OF SICILY", (230, 200, 120), _sicily, (14.2, 37.6)),
    ("SARDINIA", (180, 160, 200), _sardinia, (9.0, 40.1)),
    ("RUSSIAN EMPIRE", (120, 170, 90), P_("RUSSIAN EMPIRE") + _e["GEORGIA"][2] + [RU_FINLAND, BESSARABIA], (40.0, 57.0)),
    ("HABSBURG MONARCHY", (240, 225, 120), [p for p in P_("HABSBURG MONARCHY") if p is not AT_P3 and p is not HB_MILAN], (16.0, 48.6)),
    ("PRUSSIA", (60, 70, 90), [PRUSSIA_BB, PRUSSIA_POM, PRUSSIA_EAST, SILESIA, PR_ROYAL], (13.4, 52.6)),
    ("SWITZERLAND", (200, 120, 120), [SWISS], (8.2, 46.8)),
    ("DUCHY OF WARSAW", (225, 140, 150), [PR_P23, AT_P3], (19.5, 52.0)),
    ("KINGDOM OF ITALY", (110, 170, 120), [IT_KINGDOM], (11.3, 45.3)),
    ("KINGDOM OF NAPLES", (160, 120, 200), [NAPLES], (15.8, 40.6)),
    ("FRENCH EMPIRE", (55, 95, 200), [P_("FRANCE")[0], CORSICA, HB_NETHERLANDS, _dutch[0], FR_RHINE, FR_NWGER, FR_ITALY, FR_ILLYRIA], (2.2, 46.9)),
    ("HAITI", (60, 60, 160), [FR_SAINTDOMINGUE], (-72.6, 19.0)),
    ("UNITED STATES", (80, 125, 215), P_("UNITED STATES") + [US_LOUISIANA], (-90.0, 38.5)),
    ("KINGDOM OF HAWAII", (200, 90, 60), [HAWAII], (-157.0, 20.5)),
]
CULTURES = []
