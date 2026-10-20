"""Intermediate map: the Yuan has collapsed back to Mongolia, China not yet coloured (used under the Yuan shatter)."""
from ep9_geo import *
import world_data_1347 as _P
EXCLUSIVE = True
EMPIRES = [e for e in _P.EMPIRES if e[0] != "YUAN DYNASTY"] + [("NORTHERN YUAN", MONG, [MONGOLIA], (104, 47))]
CULTURES = _P.CULTURES
