"""Year 1642: Russia reaches the Sea of Okhotsk (1639); Sweden holds Finland, Estonia, Livonia and Ingria (+ New Sweden 1638); Poland-Lithuania
holds Smolensk; Portugal independent again (Dec 1640) but the Dutch hold Malacca and Luanda (1641), Pernambuco, Batavia, Ambon, Banda,
south-west Formosa, Galle and New Netherland; English Virginia, Maryland, New England and Ireland; New France on the St Lawrence;
the Qing in Manchuria and Inner Mongolia (1636); Shah Jahan's Mughal Empire with Kandahar (1638) and Ahmadnagar (1636); the Ottomans
have lost Yemen (1635) but keep Baghdad (1638); Tokugawa Japan. Tasman reaches Tasmania and New Zealand."""
from ep15_geo import *
import world_data_1533 as _P
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_pt = P_("PORTUGAL")            # [Portugal, Ceuta, Madeira, Azores, Porto Seguro, Pernambuco, Rio, Goa, Malacca, Hormuz]
EMPIRES = [
    ("SCOTLAND", (110, 150, 200), P_("SCOTLAND"), (-4.2, 57.0)),
    ("FRANCE", (70, 110, 200), P_("FRANCE") + [FR_NF, FR_ACADIA], (2.2, 46.9)),
    ("HOLY ROMAN EMPIRE", (230, 200, 90), P_("HOLY ROMAN EMPIRE"), (10.5, 50.2)),
    ("PAPAL STATES", (240, 230, 200), P_("PAPAL STATES"), (12.6, 42.9)),
    ("ROYAL HUNGARY", (110, 170, 110), P_("HUNGARY"), (18.6, 48.4)),
    ("TSARDOM OF RUSSIA", (120, 170, 90), P_("MUSCOVY") + [RU_VOLGA, RU_NORTH, RU_KOLA, RU_PATCH, RU_BASHKIR, RU_SIB1642], (40.0, 57.0)),
    ("POLISH-LITHUANIAN COMMONWEALTH", (220, 100, 100), P_("POLAND") + P_("LITHUANIA") + P_("TEUTONIC ORDER") + [CW_UKRAINE, CW_SMOLENSK], (24.5, 52.6)),
    ("GEORGIA", (200, 90, 90), P_("GEORGIA"), (43.6, 42.2)),
    ("ENGLAND", (200, 70, 80), P_("ENGLAND")[:2] + [EN_IRELAND, EN_VIRGINIA, EN_MARYLAND, EN_NE], (-1.6, 52.4)),
    ("BORNU", (180, 120, 80), P_("KANEM"), (14.5, 14.0)),
    ("ETHIOPIA", (120, 150, 200), P_("ETHIOPIA"), (38, 11.8)),
    ("FUNJ SULTANATE", (170, 140, 90), P_("MAKURIA"), (33.5, 17.5)),
    ("MOROCCO", (170, 110, 60), P_("WATTASIDS"), (-6, 32.0)),
    ("JOSEON", (90, 140, 220), P_("JOSEON"), (127.6, 37.4)),
    ("DAI VIET", (200, 90, 80), P_("DAI VIET") + [DAIVIET_S], (105.4, 20.8)),
    ("CAMBODIA", (210, 150, 70), P_("KHMER EMPIRE"), (104.8, 12.5)),
    ("AYUTTHAYA", (190, 120, 170), [AYUTTHAYA], (100.6, 15.5)),
    ("CHAMPA", (150, 110, 190), [CHAMPA_S], (108.6, 12.0)),
    ("TOUNGOO BURMA", (180, 130, 90), P_("PAGAN"), (95.5, 21.0)),
    ("MATARAM SULTANATE", (200, 120, 90), P_("MAJAPAHIT"), (110.5, -7.4)),
    ("KHALKHA MONGOLS", (150, 105, 60), P_("NORTHERN YUAN"), (102, 48.5)),
    ("YARKENT KHANATE", (165, 120, 80), P_("MOGHULISTAN"), (80, 40.5)),
    ("MING DYNASTY", (215, 70, 60), P_("MING DYNASTY"), (112, 31)),
    ("QING", (225, 185, 70), [QING], (125.5, 45.5)),
    ("TOKUGAWA JAPAN", (220, 120, 150), [JAPAN], (137.5, 36.2)),
    ("DECCAN SULTANATES", (120, 170, 90), P_("BAHMANI SULTANATE"), (77, 17.5)),
    ("VIJAYANAGARA", (190, 80, 70), P_("VIJAYANAGARA"), (77.6, 13.2)),
    ("CRIMEAN KHANATE", (210, 170, 90), P_("CRIMEAN KHANATE"), (34.6, 46.0)),
    ("KHANATE OF BUKHARA", (90, 150, 170), P_("UZBEK KHANATE"), (64.5, 40.8)),
    ("SAFAVID EMPIRE", (60, 150, 120), P_("SAFAVID EMPIRE"), (53.0, 32.5)),
    ("DENMARK-NORWAY", (200, 60, 70), P_("DENMARK-NORWAY"), (9.5, 61.8)),
    ("SWEDEN", (80, 130, 205), P_("SWEDEN") + [SW_LIVONIA, SW_INGRIA, SW_NEWSWEDEN], (15.8, 61.6)),
    ("MUGHAL EMPIRE", (40, 150, 95), [MG_1600, MG_DECCAN], (77.5, 26.5)),
    ("OTTOMAN EMPIRE", (200, 60, 60), P_("OTTOMAN EMPIRE") + [OT_HUNGARY, OT_IRAQ, OT_CYPRUS, OT_LAHSA, OT_MAGHREB], (33.0, 38.8)),
    ("TRANSYLVANIA", (170, 120, 200), [TRANSYLVANIA], (24.2, 46.6)),
    ("SPAIN", (235, 180, 40), P_("SPAIN")[:15] + [SP_NEWSPAIN, SP_NM, SP_CENTRAL, SP_ANDES, SP_PLATA, SP_FLORIDA, SP_LUZON, SP_VISAYAS], (-4.0, 40.0)),
    ("PORTUGAL", (80, 150, 90), [_pt[0], _pt[2], _pt[3], _pt[7]] + [PT_BRAZIL, PT_MARANHAO, PT_ANGOLA, PT_MOZ, PT_CEYLON, PT_MACAU], (-8.1, 39.6)),
    ("DUTCH REPUBLIC", (240, 140, 40), [DUTCH_NL, DUTCH_BRAZIL, DUTCH_LUANDA, DUTCH_JAVA, DUTCH_AMBON, DUTCH_BANDA, DUTCH_FORMOSA, DUTCH_GALLE, DUTCH_NN, _pt[8]], (5.6, 52.4)),
]
CULTURES = []
