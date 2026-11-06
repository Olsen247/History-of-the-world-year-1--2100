"""Year 1916 world for Episode 23 – see ep23_world.py."""
from ep20_geo import *
import ep23_world as _W
YEAR = 1914
EXCLUSIVE = True
EMPIRES = _W.build(1916)
CULTURES = []
OVERLAY = {"GERMAN-OCCUPIED": None, "GERMAN-OCCUPIED EAST": ["RUSSIAN EMPIRE"], "AUSTRIAN-OCCUPIED": None, "BULGARIAN-OCCUPIED": None, "BRITISH ZONES": None}
