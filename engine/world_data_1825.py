"""Year 1825: Latin America almost free – Mexico (with Texas, Alta California and Chiapas), the Federal Republic of Central America,
Gran Colombia, Peru, Bolivia (Aug 1825, with the Atacama coast), Chile, the United Provinces of the Rio de la Plata, Paraguay,
the Empire of Brazil (with Cisplatina) and Haiti ruling all of Hispaniola; Spain keeps Cuba, Puerto Rico, the Philippines and
Chiloe. Europe after the Congress of Vienna (1815): France in its old borders, United Kingdom of the Netherlands, German
Confederation, Prussia with the Rhineland/Westphalia/Posen/north Saxony, Austria with Lombardy-Venetia and Illyria, Russia with
Congress Poland and Finland, Sweden-Norway union, Piedmont-Sardinia, Papal States, Tuscany, Two Sicilies. US with Florida.
Britain with the Cape, Ceylon, Malta-less (too small), Singapore, Malacca and most of India (Marathas defeated 1818)."""
from ep19_geo import *
import world_data_1812 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_c = lambda p: (sum(a for a, b in p) / len(p), sum(b for a, b in p) / len(p))
_keep = ("ETHIOPIA", "MOROCCO", "JOSEON", "CAMBODIA", "TOKUGAWA JAPAN", "KHANATE OF BUKHARA", "QING EMPIRE", "SIAM", "KONBAUNG BURMA",
         "DURRANI EMPIRE", "QAJAR PERSIA", "BORNU", "SOKOTO CALIPHATE", "VIETNAM", "MYSORE", "AWADH", "HYDERABAD", "SIKH EMPIRE",
         "SWITZERLAND", "KINGDOM OF HAWAII")
_dn = P_("DENMARK-NORWAY"); _pt = P_("PORTUGAL"); _gb = P_("GREAT BRITAIN"); _sp = P_("SPAIN")
_dutch_lands = [_P._dutch[0], HB_NETHERLANDS]
_dutch_col = [DUTCH_SURINAME, DUTCH_JAVA_1770, DUTCH_AMBON, DUTCH_BANDA]
EMPIRES = [("GERMAN CONFEDERATION", (150, 170, 210), [GERMAN_CONF], (10.0, 50.5))] + \
          [e for e in _P.EMPIRES if e[0] in _keep] + [
    ("OTTOMAN EMPIRE", (200, 60, 60), P_("OTTOMAN EMPIRE") + P_("FUNJ SULTANATE"), (33.0, 38.8)),
    ("DENMARK", (200, 60, 70), [p for p in _dn if p is not NORWAY], (9.3, 56.0)),
    ("SWEDEN", (80, 130, 205), P_("SWEDEN") + [SW_SCANIA], (15.8, 61.6)),
    ("NORWAY", (150, 120, 200), [NORWAY], (9.5, 61.8)),
    ("PORTUGAL", (80, 150, 90), [p for p in _pt if p is not PT_BRAZIL_1770], (-8.1, 39.6)),
    ("GREAT BRITAIN", (200, 70, 80), [p for p in _gb if not any(p is q for q in _dutch_col) and p is not GB_NSW_1812 and p is not GB_VDL]
     + P_("MARATHAS") + [GB_NSW_1825, GB_MORETON, GB_VDL_1825, GB_SINGAPORE], (-1.6, 52.4)),
    ("NETHERLANDS", (240, 140, 40), _dutch_lands + _dutch_col, (5.4, 51.6)),
    ("FRANCE", (70, 110, 200), [P_("FRENCH EMPIRE")[0], CORSICA, FR_EAST, FR_PROVENCE], (2.2, 46.9)),
    ("SPAIN", (235, 180, 40), [p for p in _sp if _c(p)[0] > -30] + [CUBA, PUERTO_RICO, CHILOE], (-4.0, 40.0)),
    ("RUSSIAN EMPIRE", (120, 170, 90), P_("RUSSIAN EMPIRE") + P_("DUCHY OF WARSAW") + [RU_CAUC], (40.0, 57.0)),
    ("PRUSSIA", (60, 70, 90), P_("PRUSSIA") + [POSEN, PR_WEST, PR_SAXONY], (13.4, 52.6)),
    ("AUSTRIAN EMPIRE", (240, 225, 120), P_("HABSBURG MONARCHY") + [LOMBARDY_VENETIA, FR_ILLYRIA], (16.0, 48.6)),
    ("KINGDOM OF SARDINIA", (180, 160, 200), P_("SARDINIA") + [PIEDMONT], (7.8, 45.0)),
    ("ITALIAN DUCHIES", (200, 190, 140), [DUCHIES], (10.4, 44.7)),
    ("TUSCANY", (120, 180, 140), [TUSCANY], (11.1, 43.4)),
    ("PAPAL STATES", (230, 215, 150), [PAPAL], (12.6, 42.9)),
    ("TWO SICILIES", (160, 120, 200), [NAPLES] + P_("KINGDOM OF SICILY"), (15.8, 40.6)),
    ("UNITED STATES", (80, 125, 215), P_("UNITED STATES") + [SP_FLORIDA_1783], (-90.0, 38.5)),
    ("HAITI", (60, 60, 160), [HISPANIOLA, FR_SAINTDOMINGUE], (-71.5, 19.0)),
    ("EMPIRE OF BRAZIL", (50, 150, 70), [PT_BRAZIL_1770, CISPLATINA], (-50.0, -10.0)),
    ("CENTRAL AMERICA", (180, 120, 200), [CENTRAL_AM], (-87.0, 14.2)),
    ("MEXICO", (150, 190, 90), [SP_NEWSPAIN, SP_NM, SP_TEXAS, SP_TEXAS2, SP_NORTHMEX, SP_BAJA, SP_CALIFORNIA, SP_SANFRAN, CHIAPAS], (-102.0, 24.0)),
    ("GRAN COLOMBIA", (40, 160, 190), [GRAN_COLOMBIA], (-72.0, 4.5)),
    ("PERU", (200, 50, 60), [PERU], (-75.0, -10.0)),
    ("BOLIVIA", (230, 140, 60), [BOLIVIA], (-64.5, -17.0)),
    ("PARAGUAY", (170, 110, 170), [PARAGUAY], (-57.0, -23.5)),
    ("UNITED PROVINCES", (120, 180, 230), [UNITED_PROV], (-64.0, -31.0)),
    ("CHILE", (60, 90, 200), [CHILE], (-71.0, -33.0)),
]
CULTURES = []
