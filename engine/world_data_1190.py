from ep7_geo import *
EXCLUSIVE = True
def europe_1190():
    eu = [e for e in EUROPE_1000 if e[0] in ("SCOTLAND", "KINGDOM OF FRANCE", "HOLY ROMAN EMPIRE", "DENMARK", "NORWAY", "SWEDEN", "POLAND", "HUNGARY",
                                               "KIEVAN RUS", "NAVARRE", "ICELAND", "NORSE GREENLAND")]
    return eu + [("ANGEVIN EMPIRE", (200, 70, 80), [ENGLAND, ANGEVIN_FR], (-1.6, 52.4)), ("KINGDOM OF SICILY", (220, 180, 70), NORMAN_IT, (15.6, 40.0)),
                 ("CASTILE AND LEON", (200, 120, 60), [CASTILE_1100], (-5, 41.5)), ("PORTUGAL", (80, 150, 90), [PORTUGAL], (-8.1, 39.6)),
                 ("ARAGON", (210, 180, 60), [ARAGON], (-0.4, 41.4)), ("NAVARRE", (170, 120, 170), [NAVARRE], (-1.0, 42.7)),
                 ("ALMOHADS", (150, 130, 80), [ALMOHAD_SP, MAGHREB], (-3, 33)),
                 ("BYZANTINE EMPIRE", BYZ, [BYZ_BALK, BYZ_EBULG, BULG1000, BYZ_ANAT1000, CRETE, CYPRUS], (28.5, 40.0)),
                 ("SULTANATE OF RUM", (150, 120, 90), [RUM], (34, 39)), ("GEORGIA", (200, 90, 90), [GEORGIA], (43.6, 42.2))]
MID_1190 = [("AYYUBID SULTANATE", (200, 170, 70), [AYYUBID], (31, 27)), ("ABBASID CALIPHATE", ABB, [ABB_IRAQ], (43.5, 33)),
            ("KHWARAZMIAN EMPIRE", (120, 110, 160), [KHWARAZM], (57, 34)), ("GHURIDS", (180, 120, 70), [GHURID], (67, 33))]
EAST_1190 = [("QARA KHITAI", (100, 150, 150), [KARA_KHITAI], (79, 42)), ("WESTERN XIA", (170, 120, 160), [XIXIA], (101, 39)),
             ("JIN DYNASTY", (110, 150, 200), [JIN], (116, 41)), ("SOUTHERN SONG", (226, 186, 64), [SONG_S], (113, 27.5)),
             ("GORYEO", (90, 140, 220), [GORYEO], (127.6, 37.4)), ("DALI", (190, 120, 150), [DALI], (101.3, 25.3)),
             ("CHOLA EMPIRE", (190, 80, 70), [CHOLA], (78.4, 11.8)), ("WESTERN CHALUKYAS", (120, 170, 90), [CHALUK], (77, 18)),
             ("PALA EMPIRE", (230, 140, 90), [PALA], (87.5, 24.2)), ("ETHIOPIA", (120, 150, 200), [ETHIOPIA], (38, 11.8)),
             ("MAKURIA", (170, 140, 90), [MAKURIA], (33.5, 19.5)), ("KANEM", (180, 120, 80), [KANEM], (15.5, 15.5))]
EMPIRES = europe_1190() + MID_1190 + EAST_1190
CULTURES = [('Mongol tribes', (104, 47.5)), ('Cumans', (40, 47.5))] + CULT_1000[:4]
