"""Year 1740: Qing China with Taiwan, Mongolia and Tibet; Russia from the Baltic (Nystad 1721) to Kamchatka with left-bank Ukraine;
Habsburg Hungary, Transylvania and Belgrade (1718-39); Prussia; Great Britain with thirteen colonies, Jamaica, Nova Scotia, Newfoundland
and Hudson Bay; New France (Canada + Louisiana); Spanish America with Texas and Florida; Portuguese Brazil; Dutch Cape and Ceylon;
the Mughals shrinking before the Marathas and Hyderabad; Nader Shah's Afsharid Persia (with Afghanistan); the Dzungar Khanate."""
from ep16_geo import *
import world_data_1642 as _P, world_data_1533 as _Q
EXCLUSIVE = True
_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_q = {e[0]: e for e in _Q.EMPIRES}
Q_ = lambda n: _q[n][2]
_pt = Q_("PORTUGAL")            # [Portugal, Ceuta, Madeira, Azores, Porto Seguro, Pernambuco, Rio, Goa, Malacca, Hormuz]
EMPIRES = [
    ("FRANCE", (70, 110, 200), Q_("FRANCE")[:1] + [FR_CANADA, FR_LOUISIANA, FR_SAINTDOMINGUE, FR_GUIANA, FR_PONDICHERRY], (2.2, 46.9)),
    ("HOLY ROMAN EMPIRE", (230, 200, 90), P_("HOLY ROMAN EMPIRE"), (10.5, 50.2)),
    ("PAPAL STATES", (240, 230, 200), P_("PAPAL STATES"), (12.6, 42.9)),
    ("POLISH-LITHUANIAN COMMONWEALTH", (220, 100, 100), Q_("POLAND") + Q_("LITHUANIA") + Q_("TEUTONIC ORDER") + [CW_UKRAINE], (24.5, 52.6)),
    ("TSARDOM OF RUSSIA", (120, 170, 90), P_("TSARDOM OF RUSSIA") + [RU_KAMCHATKA, RU_LEFTBANK, CW_SMOLENSK, SW_LIVONIA, SW_INGRIA], (40.0, 57.0)),
    ("GEORGIA", (200, 90, 90), P_("GEORGIA"), (43.6, 42.2)),
    ("GREAT BRITAIN", (200, 70, 80), P_("ENGLAND")[:3] + P_("SCOTLAND") + [GB_COLONIES, GB_HUDSON, GB_NOVASCOTIA, GB_NEWFOUNDLAND, JAMAICA], (-1.6, 52.4)),
    ("BORNU", (180, 120, 80), P_("BORNU"), (14.5, 14.0)),
    ("ETHIOPIA", (120, 150, 200), P_("ETHIOPIA"), (38, 11.8)),
    ("FUNJ SULTANATE", (170, 140, 90), P_("FUNJ SULTANATE"), (33.5, 17.5)),
    ("MOROCCO", (170, 110, 60), P_("MOROCCO"), (-6, 32.0)),
    ("JOSEON", (90, 140, 220), P_("JOSEON"), (127.6, 37.4)),
    ("DAI VIET", (200, 90, 80), P_("DAI VIET") + [CHAMPA_S], (105.4, 20.8)),
    ("CAMBODIA", (210, 150, 70), P_("CAMBODIA"), (104.8, 12.5)),
    ("AYUTTHAYA", (190, 120, 170), [AYUTTHAYA], (100.6, 15.5)),
    ("TOUNGOO BURMA", (180, 130, 90), P_("TOUNGOO BURMA"), (95.5, 21.0)),
    ("MATARAM SULTANATE", (200, 120, 90), P_("MATARAM SULTANATE"), (110.5, -7.4)),
    ("DZUNGAR KHANATE", (165, 120, 80), P_("YARKENT KHANATE") + [DZ_NORTH], (84, 44.5)),
    ("QING EMPIRE", (225, 185, 70), P_("MING DYNASTY") + [QING, TAIWAN, TIBET, QINGHAI] + QING_FILL + P_("KHALKHA MONGOLS"), (110, 33)),
    ("TOKUGAWA JAPAN", (220, 120, 150), [JAPAN], (137.5, 36.2)),
    ("CRIMEAN KHANATE", (210, 170, 90), P_("CRIMEAN KHANATE"), (34.6, 46.0)),
    ("KHANATE OF BUKHARA", (90, 150, 170), P_("KHANATE OF BUKHARA"), (64.5, 40.8)),
    ("AFSHARID PERSIA", (60, 130, 160), P_("SAFAVID EMPIRE") + [AFSHARID_EAST], (53.0, 32.5)),
    ("DENMARK-NORWAY", (200, 60, 70), P_("DENMARK-NORWAY"), (9.5, 61.8)),
    ("SWEDEN", (80, 130, 205), Q_("SWEDEN"), (15.8, 61.6)),
    ("MUGHAL EMPIRE", (40, 150, 95), [MUGHAL_1740], (76.5, 28.0)),
    ("BENGAL", (150, 190, 110), [BENGAL_1740], (88.0, 24.2)),
    ("HYDERABAD", (200, 160, 90), [HYDERABAD_1740], (78.6, 17.6)),
    ("MARATHAS", (240, 150, 50), [MARATHA_1740], (75.6, 21.0)),
    ("OTTOMAN EMPIRE", (200, 60, 60), Q_("OTTOMAN EMPIRE") + [OT_IRAQ, OT_CYPRUS, OT_MAGHREB], (33.0, 38.8)),
    ("HABSBURG MONARCHY", (240, 225, 120), [HB_AUSTRIA, SILESIA, HB_HUNGARY, HB_CROATIA, HB_SERBIA, HB_NETHERLANDS, HB_MILAN], (16.0, 48.6)),
    ("PRUSSIA", (60, 70, 90), [PRUSSIA_BB, PRUSSIA_POM, PRUSSIA_EAST], (13.4, 52.6)),
    ("SPAIN", (235, 180, 40), Q_("SPAIN")[:15] + [SP_NEWSPAIN, SP_NM, SP_CENTRAL, SP_ANDES, SP_PLATA, SP_FLORIDA, SP_LUZON, SP_VISAYAS, SP_TEXAS, SP_NORTHMEX, SP_BAJA], (-4.0, 40.0)),
    ("GREAT BRITAIN ", (200, 70, 80), [JAMAICA], (-77.3, 18.1)),
    ("PORTUGAL", (80, 150, 90), [_pt[0], _pt[2], _pt[3], _pt[7]] + [PT_BRAZIL_1740, PT_ANGOLA, PT_MOZ, PT_MACAU], (-8.1, 39.6)),
    ("DUTCH REPUBLIC", (240, 140, 40), [DUTCH_NL, DUTCH_CAPE_1740, DUTCH_CEYLON, DUTCH_JAVA, DUTCH_AMBON, DUTCH_BANDA, DUTCH_SURINAME, _pt[8]], (5.6, 52.4)),
]
CULTURES = []
