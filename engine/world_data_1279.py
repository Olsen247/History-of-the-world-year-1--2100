from ep7_geo import *
EXCLUSIVE = True
_cr = [e for e in EUROPE_1279 if e[0] == "CRUSADER STATES"]
EMPIRES = [e for e in EUROPE_1279 if e[0] != "CRUSADER STATES"] + AFR_1279 + ASIA_1279 + _cr
CULTURES = CULT_1279
