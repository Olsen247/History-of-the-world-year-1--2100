"""Year 1453 base for Ep 11: the 1453 map plus the Aztec Triple Alliance (founded 1428), which earlier maps left out."""
from ep11_geo import *
import world_data_1453 as _P
EXCLUSIVE = True
EMPIRES = list(_P.EMPIRES) + [("AZTEC EMPIRE", (60, 160, 150), [AZTEC_1453], (-99.2, 19.4))]
CULTURES = _P.CULTURES
