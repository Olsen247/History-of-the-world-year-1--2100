from ep7_geo import *
EXCLUSIVE = True
EMPIRES = [e for e in EUROPE_1279 if e[0] not in ("CRUSADER STATES",)] + [e for e in AFR_1279] + \
          [("MONGOL EMPIRE", MONG, [MONGOLIA, XIXIA, JIN, TIBET, DALI, CHAGATAI, GOLDEN_HORDE, ILKHAN], (90, 44)),
           ("SOUTHERN SONG", (226, 186, 64), [SONG_S], (113, 27.5)), ("CRUSADER STATES", (235, 235, 240), CRUSADER_1279, (34.0, 33.6))] + \
          [e for e in ASIA_1279 if e[0] not in ("YUAN DYNASTY", "CHAGATAI KHANATE", "GOLDEN HORDE", "ILKHANATE")]
CULTURES = CULT_1279
