import sys
SEG = [
 (0.3, 5.83, 'Five_ships|y sailed west for the Spice_Islands.|g Three_years_later,|y one came home,|c from the east.|r'),
 (6.33, 7.53, ''),
 (7.78, 13.83, 'In 1500,|y Pedro_Álvares_Cabral,|c sailing for India,|y swings west and lands in Brazil.|g'),
 (14.23, 21.52, 'In 1501,|y the teenage Ismail|g is crowned shah in Tabriz.|y His Safavid_Empire|g soon rules all_of_Iran.|y'),
 (21.92, 28.88, 'In 1511,|y Albuquerque|c takes Malacca,|r the gateway to the spice_trade.|y A young Magellan|c is among his men.'),
 (29.28, 35.85, 'In 1513,|y Balboa|c crosses Panama|y and sees a vast_ocean,|c later named the Pacific.|c'),
 (36.25, 44.08, "In 1517,|y Sultan_Selim|r takes Cairo,|r and in Germany, Martin_Luther's|p Ninety-five_Theses|y spark the Reformation.|g"),
 (44.48, 52.11, 'In September_1519,|y the Portuguese captain Ferdinand_Magellan|c leaves Spain with five_ships|y and about 270_men.|g'),
 (52.51, 59.73, 'In 1520,|y he finds a strait|c at the tip of South_America.|y Crossing the Pacific,|c his starving_men|r eat leather.|r'),
 (60.13, 66.73, 'In April_1521,|y Magellan|c is killed|r in the Philippines, fighting the warriors of Lapulapu|g on Mactan.|y'),
 (67.13, 73.12, 'That August,|y Hernán_Cortés|c and his native_allies|y capture Tenochtitlan.|r The Aztec_Empire|g falls.|r'),
 (73.52, 80.91, 'In September_1522,|y the Victoria|c limps home with just 18_men:|r the first_voyage|g around_the_world.|y'),
 (81.31, 87.86, 'Next time:|y the year 1533,|y when Pizarro|c topples the Inca_Empire.|g Follow the series!|y'),
]
out = []
for a, b, txt in SEG:
    words = txt.split(); groups = []; cur = []
    for w in words:
        cur.append(w)
        plain = w.split("|")[0]
        if len(cur) >= 3 or plain.endswith((".", ",", "!", ":", "?")):
            groups.append(cur); cur = []
    if cur: groups.append(cur)
    lens = [sum(len(x.split("|")[0]) + 2 for x in g) for g in groups]; tot = sum(lens); t = a
    for g, L in zip(groups, lens):
        d = (b - a) * L / tot
        out.append(f"{t:.2f} {t + d - 0.03:.2f} " + " ".join(g)); t += d
open(sys.argv[1], "w").write("\n".join(out) + "\n")
narr = ["NARRATION SCRIPT – History of the World, Episode 13: Year 1522", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
