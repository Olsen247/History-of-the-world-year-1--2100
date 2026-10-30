"""Builds the Year 1900 world (and an 1882 variant = before the Scramble for Africa and before 1898) for Episode 20.
Order matters: EXCLUSIVE = True, later entries win overlaps."""
from ep20_geo import *
import world_data_1825 as _P

_e = {e[0]: e for e in _P.EMPIRES}
P_ = lambda n: _e[n][2]
_c = lambda p: (sum(a for a, b in p) / len(p), sum(b for a, b in p) / len(p))

BRIT = (235, 125, 165); FRC = (60, 95, 200); DEC = (110, 110, 122); CGC = (170, 120, 200); PTC = (50, 140, 80); ITC = (110, 185, 150)
ESC = (235, 180, 40); NLC = (240, 140, 40); RUC = (130, 175, 95); OTC = (200, 60, 60); USC = (150, 190, 250)

ALG_1882 = [(-2.2, 35.1), (-1.5, 32.1), (2.0, 31.5), (6.0, 31.0), (9.6, 31.0), (7.5, 33.2), (8.3, 34.6), (8.6, 37.5), (-2.2, 37.0)]
CANARIES = box(-18.3, 27.5, -13.2, 29.5)


def build(year):
    late = year >= 1890
    sp_eu = [p for p in P_("SPAIN") if 30 < _c(p)[1] < 45 and -10 < _c(p)[0] < 5]
    pt_eu = [p for p in P_("PORTUGAL") if _c(p)[0] < -5]
    E = [
        ("QING EMPIRE", (225, 185, 70), P_("QING EMPIRE"), (104.0, 33.0)),
        ("RUSSIAN EMPIRE", RUC, [RU_EU_FILL] + P_("RUSSIAN EMPIRE") + [RU_CAUC_1900, RU_TURKESTAN, RU_SIBERIA, SAKHALIN] + ([KWANTUNG] if year >= 1898 else []), (45.0, 56.0)),
        ("KOREAN EMPIRE" if year >= 1897 else "JOSEON", (90, 140, 220), P_("JOSEON"), (127.6, 37.4)),
        ("JAPAN", (235, 95, 70), P_("TOKUGAWA JAPAN") + [HOKKAIDO, RYUKYU] + ([TAIWAN_JP] if year >= 1895 else []), (137.5, 36.2)),
        ("SIAM", (190, 120, 170), P_("SIAM"), (100.6, 15.5)),
        ("PERSIA", (60, 130, 160), [PERSIA_1900], (54.0, 32.5)),
        ("OTTOMAN EMPIRE", OTC, [OT_ASIA, OT_HEJAZ, OT_HASA, OT_EU_1900, OT_LIBYA], (35.0, 38.8)),
        ("AUSTRIA-HUNGARY", (240, 225, 120), P_("AUSTRIAN EMPIRE") + [BOSNIA], (17.0, 48.0)),
        ("ITALY", ITC, P_("KINGDOM OF SARDINIA") + P_("ITALIAN DUCHIES") + P_("TUSCANY") + P_("PAPAL STATES") + P_("TWO SICILIES") + [LOMBARDY_VENETIA]
         + ([IT_ERITREA, IT_SOMALI] if late else []), (12.5, 42.8)),
        ("FRENCH EMPIRE", FRC, [FRANCE14, CORSICA] + ([FR_ALGERIA, FR_WEST, FR_EQ, FR_DJIBOUTI, MADAGASCAR] if late else [ALG_1882, SENEGAL_1882])
         + [FR_TUNISIA, FR_INDOCHINA, NEW_CALEDONIA] + ([KWANGCHOWAN] if year >= 1898 else []), (2.5, 47.0)),
        ("DENMARK", (200, 60, 70), P_("DENMARK"), (9.3, 56.0)),
        ("NETHERLANDS", NLC, [NETH, NL_SUMATRA, NL_JAVA, NL_BORNEO, NL_CELEBES, NL_MOLUCCAS, NL_SUNDAS, NL_NEWGUINEA], (5.6, 52.3)),
        ("GERMAN EMPIRE", DEC, [GERMANY] + ([GER_TOGO, KAMERUN, GER_SWA, GER_EAST, GER_NG, GER_BISMARCK] if late else [])
         + ([KIAUTSCHOU] if year >= 1898 else []), (10.5, 51.0)),
    ]
    if late: E.append(("CONGO FREE STATE", CGC, [CONGO_FS], (23.5, -2.5)))
    E += [
        ("SPAIN", ESC, sp_eu + [CEUTA, CANARIES] + ([RIO_DE_ORO, ES_GUINEA, ES_BIOKO] if late else [ES_BIOKO])
         + ([] if year >= 1898 else [US_PHIL, PUERTO_RICO, CUBA]), (-4.0, 40.0)),
        ("BRITISH EMPIRE", BRIT, [ENGLAND, SCOTLAND, IRE, BR_INDIA, BR_MALAYA, BR_BORNEO, HONGKONG, ADEN, AUSTRALIA, TASMANIA, NEW_ZEALAND, BR_PAPUA,
                                  FIJI, CANADA, GB_NEWFOUNDLAND, BELIZE, JAMAICA, TRINIDAD, SIERRA_LEONE, GAMBIA, BASUTO, NATAL]
         + ([SUDAN_1900, BR_SOMALI, BR_EAST, ZANZIBAR, NIGERIA, GOLD_COAST, CAPE_1900, BECHUANA, NYASA, RHODESIA] if late else [LAGOS_1882, GOLD_1882, CAPE_1882])
         + ([WEIHAIWEI] if year >= 1898 else []), (-1.6, 52.4)),
        ("EGYPT", (225, 150, 160), [EGYPT_1900], (30.0, 26.5)),
        ("UNITED STATES", USC, [US_1900, ALASKA, HAWAII] + ([US_PHIL, PUERTO_RICO] if year >= 1898 else []), (-98.0, 39.0)),
        ("PORTUGAL", PTC, pt_eu + ([ANGOLA_1900, CABINDA, MOZ_1900] if late else [PT_ANGOLA, PT_MOZ]) + [PT_GUINEA, GOA, PT_MACAU, PT_TIMOR], (-8.1, 39.6)),
        ("AFGHANISTAN", (130, 110, 170), [AFGHAN_1900], (66.0, 33.5)),
        ("NEPAL", (170, 90, 140), [NEPAL], (84.0, 28.2)), ("BHUTAN", (200, 150, 90), [BHUTAN], (90.4, 27.4)),
        ("OMAN", (170, 120, 90), [OMAN], (57.0, 22.0)),
        ("ETHIOPIA", (120, 150, 200), [ETHIOPIA_1900], (39.0, 9.0)),
        ("LIBERIA", (150, 110, 180), [LIBERIA], (-9.4, 6.5)),
        ("MOROCCO", (170, 110, 60), [MOROCCO_1900], (-6.0, 32.0)),
        ("TRANSVAAL", (170, 130, 80), [TRANSVAAL], (29.0, -24.5)),
        ("ORANGE FREE STATE", (200, 160, 90), [ORANGE_FS], (26.5, -28.8)),
        ("GREECE", (100, 160, 220), [GREECE_1900], (22.0, 39.0)),
        ("BULGARIA", (110, 160, 90), [BULGARIA_1900], (25.3, 42.7)),
        ("ROMANIA", (220, 190, 80), [ROMANIA_1900], (25.5, 45.0)),
        ("SERBIA", (170, 90, 90), [SERBIA_1900], (21.0, 44.0)),
        ("MONTENEGRO", (150, 120, 180), [MONTENEGRO], (19.2, 42.8)),
        ("BELGIUM", (235, 195, 60), [BELGIUM], (4.6, 50.6)), ("LUXEMBOURG", (150, 170, 210), [LUX], (6.1, 49.8)),
        ("SWITZERLAND", (200, 120, 120), P_("SWITZERLAND"), (8.2, 46.8)),
        ("SWEDEN", (80, 130, 205), P_("SWEDEN"), (15.8, 61.6)), ("NORWAY", (150, 120, 200), P_("NORWAY"), (9.5, 61.8)),
        ("BRAZIL", (50, 150, 70), [PT_BRAZIL_1770], (-50.0, -10.0)),
        ("COLOMBIA", (40, 160, 190), [COLOMBIA_1900], (-73.5, 4.0)), ("VENEZUELA", (230, 150, 60), [VENEZUELA], (-66.0, 7.0)),
        ("PERU", (200, 50, 60), [PERU], (-75.0, -10.0)), ("ECUADOR", (230, 200, 80), [ECUADOR], (-78.3, -1.5)),
        ("BOLIVIA", (230, 140, 60), [BOLIVIA], (-64.5, -17.0)), ("ARGENTINA", (120, 180, 230), [ARGENTINA], (-64.0, -33.0)),
        ("CHILE", (60, 90, 200), [CHILE_1900], (-71.0, -33.0)), ("PARAGUAY", (170, 110, 170), [PARAGUAY_1900], (-58.0, -23.5)),
        ("URUGUAY", (150, 200, 220), [CISPLATINA], (-56.0, -32.8)),
        ("BRITISH GUIANA", BRIT, [BR_GUIANA], (-58.8, 5.5)), ("SURINAME", NLC, [DUTCH_SURINAME], (-56.0, 4.0)),
        ("FRENCH GUIANA", FRC, [FR_GUIANA], (-53.0, 4.0)),
        ("MEXICO", (150, 190, 90), [MEXICO_1900], (-102.0, 24.0)),
        ("GUATEMALA", (110, 170, 200), [GUATEMALA], (-90.3, 15.5)), ("HONDURAS", (90, 110, 200), [HONDURAS], (-86.6, 14.8)),
        ("EL SALVADOR", (200, 120, 160), [SALVADOR], (-88.9, 13.7)), ("NICARAGUA", (120, 200, 160), [NICARAGUA], (-85.0, 12.8)),
        ("COSTA RICA", (220, 170, 90), [COSTA_RICA], (-84.2, 9.9)),
        ("HAITI", (60, 60, 160), [HAITI_W], (-72.6, 19.0)), ("DOMINICAN REPUBLIC", (110, 170, 120), [DOMINICAN], (-70.3, 18.8)),
    ]
    if year >= 1898: E.append(("CUBA", (140, 175, 225), [CUBA], (-79.0, 21.8)))
    return E
