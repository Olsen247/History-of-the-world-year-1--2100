"""Intermediate map for Ep 19: Europe after the Congress of Vienna (as 1825), but the Americas as in 1812 (Spanish and
Portuguese empires, US without Florida, Haiti only in the west of Hispaniola) plus Paraguay (self-ruling since 1811)."""
from ep19_geo import *
import world_data_1812 as _O, world_data_1825 as _N
EXCLUSIVE = True
_o = {e[0]: e for e in _O.EMPIRES}
_c = lambda p: (sum(a for a, b in p) / len(p), sum(b for a, b in p) / len(p))
_latin = ("EMPIRE OF BRAZIL", "CENTRAL AMERICA", "MEXICO", "GRAN COLOMBIA", "PERU", "BOLIVIA", "UNITED PROVINCES", "CHILE", "HAITI")
EMPIRES = []
for e in _N.EMPIRES:
    n, col, ps, pos = e
    if n in _latin: continue
    if n == "SPAIN": ps = [p for p in ps if p is not CHILOE] + [p for p in _o["SPAIN"][2] if _c(p)[0] < -30]
    if n == "PORTUGAL": ps = ps + [PT_BRAZIL_1770]
    if n == "UNITED STATES": ps = _o["UNITED STATES"][2]
    if n == "PARAGUAY": continue
    EMPIRES.append((n, col, ps, pos))
EMPIRES += [("PARAGUAY", (170, 110, 170), [PARAGUAY], (-57.0, -23.5)), ("HAITI", (60, 60, 160), [FR_SAINTDOMINGUE], (-72.6, 19.0))]
CULTURES = []
