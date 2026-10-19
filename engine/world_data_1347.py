from ep7_geo import *
EXCLUSIVE = True
WALES = [(-3.0, 53.3), (-4.6, 53.3), (-4.2, 52.4), (-5.3, 51.8), (-4, 51.6), (-3, 51.4), (-2.8, 51.6), (-3.1, 52.3)]
DELHI_1347 = [(70.5, 30.2), (73.5, 32.5), (75, 32.5), (77, 31), (80, 28.5), (84, 27), (88, 26.8), (89, 25.5), (88, 22), (86, 20.5), (84.5, 18.5),
              (82.3, 16.6), (80.2, 15.3), (80.3, 13), (79.5, 11), (78, 10.5), (76.5, 11.5), (75, 14), (73.5, 16), (72.9, 19), (72.6, 21.4), (70, 22.5),
              (69, 22.5), (68.3, 23.6), (70, 24.5), (71.2, 26.5), (71.6, 28.5)]
VIJAYA = [(74, 14.8), (77.5, 15.2), (78.5, 13.5), (77.8, 11.6), (76, 11.5), (74.8, 13)]
_drop = ("CRUSADER STATES", "BYZANTINE EMPIRE", "SERBIA", "KINGDOM OF SICILY", "ARAGON", "LITHUANIA", "ENGLAND")
EUROPE_1347 = [e for e in EUROPE_1279 if e[0] not in _drop] + [
    ("ENGLAND", (200, 70, 80), [ENGLAND, WALES, GASCONY], (-1.6, 52.4)),
    ("ARAGON", (210, 180, 60), [ARAGON, BALEARIC, SICILY, SARDINIA], (-0.4, 41.4)), ("KINGDOM OF NAPLES", (220, 140, 70), [CALABRIA, APULIA, BENEV], (15.6, 40.6)),
    ("SERBIAN EMPIRE", (180, 70, 90), [SERBIA_1347], (21.2, 42.4)), ("BYZANTINE EMPIRE", BYZ, [BYZ_1347], (26.8, 41.4)),
    ("OTTOMANS", (200, 60, 60), [OTTOMAN], (29.6, 40.2)), ("LITHUANIA", (170, 200, 110), [LITHUANIA_1347], (27, 53.8))]
AFR_1347 = [e for e in AFR_1279 if e[0] != "MALI EMPIRE"] + [("MALI EMPIRE", (210, 160, 60), [MALI_1347], (-8, 14.5))]
ASIA_1347 = [e for e in ASIA_1279 if e[0] not in ("ILKHANATE", "DELHI SULTANATE", "PANDYAS", "HOYSALAS", "YADAVAS")] + [
    ("DELHI SULTANATE", (60, 140, 110), [DELHI_1347], (78, 22.5)), ("VIJAYANAGARA", (190, 80, 70), [VIJAYA], (76.4, 13.4)),
    ("MAJAPAHIT", (200, 120, 90), [JAVA_MAJ], (110.5, -7.4))]
EMPIRES = EUROPE_1347 + AFR_1347 + ASIA_1347
CULTURES = [c for c in CULT_1279 if "Mexica" not in c[0]] + [('Anatolian beyliks', (34, 38.5)), ('Persian successor states', (52, 33)),
                                                             ('Ashikaga Japan', (136, 36))]
