"""Around 1420-1429: Lancastrian England holds northern France; Portugal holds Ceuta and Madeira."""
from ep10_geo import *
import world_data_1405 as _P
EXCLUSIVE = True
def _mod(e):
    if e[0] == "ENGLAND": return (e[0], e[1], e[2] + [ENG_FR, CALAIS], e[3])
    if e[0] == "PORTUGAL": return (e[0], e[1], e[2] + [CEUTA, MADEIRA], e[3])
    return e
EMPIRES = [_mod(e) for e in _P.EMPIRES]
CULTURES = _P.CULTURES
