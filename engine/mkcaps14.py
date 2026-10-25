import sys
SEG = [
 (0.3, 5.87, 'With just 168_men,|y one Spaniard brought_down|r the largest_empire|g in the Americas.|y'),
 (6.37, 7.57, ''),
 (7.82, 15.31, 'In 1523,|y Gustav_Vasa|c is elected king of Sweden.|c The Kalmar_Union|y with Denmark and Norway falls_apart.|r'),
 (15.71, 23.13, 'In 1525,|y at Pavia|y in Italy, the army of Emperor Charles_V|c captures|r King Francis_I|c of France.'),
 (23.53, 31.19, 'In 1526,|y Babur,|g a descendant of Timur and Genghis_Khan,|y wins at Panipat|r and founds the Mughal_Empire.|g'),
 (31.59, 38.17, 'That August,|y Suleiman|r the Magnificent crushes Hungary|r at Mohács.|y Young King Louis_II|c drowns as he flees.'),
 (38.57, 45.66, "In 1527,|y Charles's unpaid soldiers|y mutiny and sack_Rome.|r The Pope|c flees to his fortress."),
 (46.06, 53.98, 'In 1529,|y Suleiman|r besieges Vienna,|y but rain, cold|c and stubborn defenders|g force the Ottomans to turn_back.|y'),
 (54.38, 60.83, "In the Andes,|g a civil_war|r ends in 1532:|y Atahualpa's armies|c defeat his brother Huáscar.|p"),
 (61.23, 67.75, "That November,|y Francisco Pizarro's|c 168 Spaniards|y ambush Atahualpa|r at Cajamarca|y and take him prisoner.|r"),
 (68.15, 73.34, 'To buy his freedom,|y Atahualpa|c promises a room full of gold,|y and twice as much silver.|c'),
 (73.74, 79.52, 'But Pizarro|c has him executed anyway.|r In November,|y the Spaniards|y march into Cusco,|r the Inca capital.|g'),
 (79.92, 86.87, 'Next time:|y the year 1642,|y when Abel_Tasman|c reaches Tasmania and New_Zealand.|g Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 14: Year 1533", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
