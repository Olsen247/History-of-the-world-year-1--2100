import sys
SEG = [
 (0.30, 7.87, 'The year|y 1405.|y China launches one of the biggest fleets|r in history, with almost 28,000|y men on board.'),
 (8.37, 12.75, "Let's rewind|r to the year 1347,|y and see how we got here.|r"),
 (13.15, 18.62, "In 1351,|y the Red_Turban|r rebels rise up against China's Mongol|y rulers."),
 (19.02, 26.59, 'In 1368,|y a former peasant, Zhu_Yuanzhang,|y founds the Ming_dynasty,|r and drives the Mongols back to the steppe.|y'),
 (26.99, 34.09, 'In Central Asia, a warlord named Timur|c seizes power in 1370,|y and starts building a huge_empire.|c'),
 (34.49, 39.98, 'In 1380,|y Prince Dmitry|g of Moscow defeats the Golden_Horde|y at Kulikovo.|r'),
 (40.38, 48.20, 'In 1389,|y the Ottomans|r fight the Serbs at Kosovo.|y Both rulers are killed,|r but Serbia falls under Ottoman power.|r'),
 (48.60, 54.82, 'In 1397,|y Queen Margaret|p unites Denmark, Norway|c and Sweden in the Kalmar_Union.|c'),
 (55.22, 60.05, 'In 1398,|y Timur|c invades India, and sacks Delhi.|r'),
 (60.45, 66.09, 'In 1402,|y he crushes the Ottomans|r at Ankara, and captures their sultan, Bayezid.|y'),
 (66.49, 73.18, 'That same year, Zhu_Di|y seizes the throne of Ming_China.|r Timur|c marches east to attack him, but dies on the way.|r'),
 (73.58, 80.29, 'In 1405,|y the new emperor sends Admiral Zheng_He|y across the ocean, with a giant treasure_fleet.|y'),
 (80.69, 87.19, 'Next time:|y the year 1453,|y when the Ottomans|r attack Constantinople. Follow the series!|y'),
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
