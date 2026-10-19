from ep5_geo import *
EXCLUSIVE = True
EMPIRES = europe_750() + [("AL-ANDALUS", (70, 160, 100), [UMA_SPAIN], (-4, 39.5)), ("ABBASID CALIPHATE", ABB, [IFRIQIYA, UMA_EAST], (44, 30))] + \
          asia_750() + INDIA_750 + [("AKSUM", (120, 150, 200), [AKSUM], (39, 13.5))]
CULTURES = CULT_750
