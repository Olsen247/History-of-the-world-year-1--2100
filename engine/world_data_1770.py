"""Year 1770 (before the first partition of Poland, 1772): Qing China at its height (Xinjiang 1759, Tibet, Mongolia, Taiwan); Russia
to Kamchatka and the Black Sea steppe; Prussia with Silesia; Habsburg Monarchy; Great Britain with Canada, Florida and everything east
of the Mississippi (1763), Bengal (1765), Madras and the Northern Circars; Spain with Louisiana (1762), Texas and the first missions in
California (San Diego 1769, Monterey 1770); Brazil after the Treaty of Madrid (1750); French Corsica (1768), Saint-Domingue and
Pondicherry; the Dutch at the Cape, in Ceylon and Java; Marathas, Hyderabad, Mysore, Awadh and a tiny Mughal state round Delhi;
the Durrani Empire; Zand Persia; Konbaung Burma; Siam under Taksin."""
from ep16_geo import *
import world_data_1740 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_keep = ("HOLY ROMAN EMPIRE", "PAPAL STATES", "POLISH-LITHUANIAN COMMONWEALTH", "GEORGIA", "BORNU", "ETHIOPIA", "FUNJ SULTANATE", "MOROCCO", "JOSEON",
         "DAI VIET", "CAMBODIA", "TOKUGAWA JAPAN", "CRIMEAN KHANATE", "KHANATE OF BUKHARA", "DENMARK-NORWAY", "SWEDEN")
EMPIRES = [e for e in _P.EMPIRES if e[0] in _keep] + [
    ("FRANCE", (70, 110, 200), P_("FRANCE")[:1] + [CORSICA, FR_SAINTDOMINGUE, FR_GUIANA, FR_PONDICHERRY], (2.2, 46.9)),
    ("RUSSIAN EMPIRE", (120, 170, 90), P_("TSARDOM OF RUSSIA") + [RU_SOUTH], (40.0, 57.0)),
    ("QING EMPIRE", (225, 185, 70), P_("QING EMPIRE") + P_("DZUNGAR KHANATE"), (110, 33)),
    ("SIAM", (190, 120, 170), [SIAM_1770], (100.6, 15.5)),
    ("KONBAUNG BURMA", (180, 130, 90), [KONBAUNG], (95.8, 21.5)),
    ("ZAND PERSIA", (60, 130, 160), P_("AFSHARID PERSIA")[:-1], (53.0, 32.5)),
    ("DURRANI EMPIRE", (130, 110, 170), [DURRANI], (66.0, 32.5)),
    ("MARATHAS", (240, 150, 50), [MARATHA_1770], (77.0, 22.5)),
    ("HYDERABAD", (200, 160, 90), [HYDERABAD], (79.2, 16.8)),
    ("MYSORE", (170, 90, 140), [MYSORE], (76.4, 13.3)),
    ("AWADH", (150, 190, 110), [AWADH], (81.0, 26.8)),
    ("MUGHAL EMPIRE", (40, 150, 95), [MUGHAL_1770], (77.6, 28.2)),
    ("OTTOMAN EMPIRE", (200, 60, 60), P_("OTTOMAN EMPIRE") + [HB_SERBIA], (33.0, 38.8)),
    ("HABSBURG MONARCHY", (240, 225, 120), [HB_AUSTRIA, HB_HUNGARY, HB_CROATIA, HB_NETHERLANDS, HB_MILAN], (16.0, 48.6)),
    ("PRUSSIA", (60, 70, 90), [PRUSSIA_BB, PRUSSIA_POM, PRUSSIA_EAST, SILESIA], (13.4, 52.6)),
    ("SPAIN", (235, 180, 40), [p for p in P_("SPAIN") if p is not SP_FLORIDA] + [SP_LOUISIANA, SP_CALIFORNIA], (-4.0, 40.0)),
    ("PORTUGAL", (80, 150, 90), P_("PORTUGAL")[:4] + [PT_BRAZIL_1770, PT_ANGOLA_1770, PT_MOZ, PT_MACAU], (-8.1, 39.6)),
    ("GREAT BRITAIN", (200, 70, 80), P_("GREAT BRITAIN") + [GB_EAST_MISS, GB_QUEBEC, BENGAL_1740, EIC_MADRAS, EIC_BOMBAY], (-1.6, 52.4)),
    ("DUTCH REPUBLIC", (240, 140, 40), [DUTCH_NL, DUTCH_CAPE_1770, DUTCH_CEYLON, DUTCH_JAVA_1770, DUTCH_AMBON, DUTCH_BANDA, DUTCH_SURINAME, P_("DUTCH REPUBLIC")[-1]], (5.6, 52.4)),
]
CULTURES = []
