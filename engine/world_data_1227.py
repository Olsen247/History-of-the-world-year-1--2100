from world_data_1190 import *
EXCLUSIVE = True
EMPIRES = europe_1190() + [e for e in MID_1190 if e[0] not in ("KHWARAZMIAN EMPIRE", "GHURIDS")] + \
          [("MONGOL EMPIRE", MONG, [MONGOLIA, XIXIA, JIN, KARA_KHITAI, KHWARAZM], (90, 44)), ("JIN DYNASTY", (110, 150, 200), [JIN_S], (113, 34.5)),
           ("DELHI SULTANATE", (60, 140, 110), [DELHI], (79, 26.5))] + \
          [e for e in EAST_1190 if e[0] not in ("QARA KHITAI", "WESTERN XIA", "JIN DYNASTY")]
CULTURES = [('Cumans', (40, 47.5))]
