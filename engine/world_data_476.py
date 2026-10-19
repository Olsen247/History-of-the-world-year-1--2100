from ep4_geo import *
EXCLUSIVE = True
EMPIRES = [("EASTERN ROMAN EMPIRE", EAST, [EAST_BALK, EAST_AS, EGYPT, CYREN], (33, 38.6)),
           ("SASANIAN EMPIRE", SAS, [SASANIAN], (53.5, 33.0)), ("HEPHTHALITES", (150, 120, 190), [HEPHTH], (67, 37)),
           ("GUPTA EMPIRE", (235, 135, 95), [GUPTA], (79.5, 27.0)), ("VAKATAKA", (120, 170, 90), [VAKATAKA], (77.5, 20)),
           ("PALLAVAS", (140, 200, 110), [PALLAVA], (78.6, 12.6)),
           ("VISIGOTHS", (205, 145, 60), [VISIGOTHS], (-3.5, 40)), ("SUEBI", (110, 170, 190), [SUEBI], (-7.6, 42.3)),
           ("FRANKS", (70, 110, 200), [FRANKS], (5.5, 51.2)), ("SOISSONS", ROME, [SOISSONS], (2.3, 48.6)),
           ("BURGUNDIANS", (180, 90, 140), [BURGUNDY], (5.6, 46.6)),
           ("KINGDOM OF ODOACER", (60, 150, 140), [ITALY, SICILY], (12.5, 43.2)),
           ("VANDALS", (95, 95, 175), [VANDAL_AF, SARDINIA, CORSICA, BALEARIC], (6, 34.6))] + ASIA_476 + AFR_476
CULTURES = [('Anglo-Saxons', (0.3, 52.6)), ('Britons', (-3.9, 52.0)), ('Picts', (-4.3, 57.3)), ('Saxons', (9.5, 53.2)), ('Thuringians', (11.5, 51)),
            ('Alamanni', (9.2, 48.4)), ('Slavs', (27, 51.5)), ('Bretons', (-3, 48.1)), ('Berber kingdoms', (-4, 31.8)), ('Arab tribes', (44, 25)),
            ('Ostrogoths', (21.5, 43.6)), ('Yamato Japan', (136, 35)), ('Maya city-states', (-89.5, 17)), ('Teotihuacan', (-99, 20.4)),
            ('Moche', (-79.5, -7.5)), ('Tiwanaku', (-68.7, -16.5)), ('Polynesian voyagers', (-168, -14)), ('Aboriginal Australians', (134, -25)),
            ('Bantu-speaking peoples', (23, -6))]
