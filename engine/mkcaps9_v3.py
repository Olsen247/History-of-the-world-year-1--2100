import sys
SEG = [
 (0.3, 6.17, 'China|y is about to send almost 28,000_men|y across the ocean,|c in one of the biggest_fleets|y in history.'),
 (6.67, 7.87, ''),
 (8.12, 13.61, "In 1351,|y the Red_Turban|r rebels rise up against China's Mongol|y rulers."),
 (14.01, 21.58, 'In 1368,|y a former peasant, Zhu_Yuanzhang,|y founds the Ming_dynasty,|r and drives the Mongols back to the steppe.|y'),
 (21.98, 29.02, 'In Central Asia, a warlord named Timur|c seizes power in 1370,|y and starts building a huge_empire.|c'),
 (29.42, 34.81, 'In 1380,|y Prince Dmitry|g of Moscow defeats the Golden_Horde|y at Kulikovo.|r'),
 (35.21, 43.04, 'In 1389,|y the Ottomans|r fight the Serbs at Kosovo.|y Both rulers are killed,|r but Serbia falls under Ottoman power.|r'),
 (43.44, 49.71, 'In 1397,|y Queen Margaret|p unites Denmark, Norway|c and Sweden in the Kalmar_Union.|c'),
 (50.11, 54.9, 'In 1398,|y Timur|c invades India, and sacks Delhi.|r'),
 (55.3, 60.87, 'In 1402,|y he crushes the Ottomans|r at Ankara, and captures their sultan, Bayezid.|y'),
 (61.27, 68.13, 'That same year, Zhu_Di|y seizes the throne of Ming_China.|r Timur|c marches east to attack him, but dies on the way.|r'),
 (68.53, 75.31, 'In 1405,|y the new emperor sends Admiral Zheng_He|y across the ocean, with a giant treasure_fleet.|y'),
 (75.71, 82.27, 'Next time:|y the year 1453,|y when the Ottomans|r attack Constantinople. Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 9: Year 1405", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
