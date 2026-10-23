"""Helper for Ep 12: early 1495, Charles VIII of France holds the Kingdom of Naples (used only for the France-takes-Naples reveal)."""
import world_data_1492 as _P
EXCLUSIVE = True
_nap = [e for e in _P.EMPIRES if e[0] == "KINGDOM OF NAPLES"][0]
EMPIRES = [(e[0], e[1], e[2] + _nap[2], e[3]) if e[0] == "FRANCE" else e for e in _P.EMPIRES if e[0] != "KINGDOM OF NAPLES"]
CULTURES = _P.CULTURES
