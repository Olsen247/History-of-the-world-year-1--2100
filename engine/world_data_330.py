from ep4_geo import *
EXCLUSIVE = True
EMPIRES = [("SASANIAN EMPIRE", SAS, [SASANIAN], (53.5, 33.0))] + rome_unified() + \
          [e for e in W220.EMPIRES if e[0] not in ("PARTHIAN EMPIRE", "ROMAN EMPIRE")]
CULTURES = W220.CULTURES
