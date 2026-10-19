import sys
SEG = [
 (0.30, 8.82, 'The year|y 1347.|y A deadly disease|r arrives in Europe. Within a few years, it will kill around a third|r of all the people living there.'),
 (9.32, 13.18, "Let's rewind|r to the year 1279,|y and follow its path.|r"),
 (13.58, 21.02, 'In 1291,|y the last crusader city, Acre,|y falls to the Mamluks.|g The age of the Crusades|r is over.'),
 (21.42, 29.01, 'Around 1299,|y a Turkish leader named Osman|r founds a small state in Anatolia.|y It will grow into the Ottoman_Empire.|r'),
 (29.41, 37.75, 'In Africa, Mansa_Musa,|y king of Mali,|y travels to Mecca in 1324,|g with so much gold|y that prices in Cairo crash.|r'),
 (38.15, 44.39, 'In 1325,|y the Aztecs|c found their capital, Tenochtitlan,|y on an island in a lake in Mexico.|c'),
 (44.79, 48.47, 'In India, the Delhi_Sultanate|g conquers its way deep into the south.|y'),
 (48.87, 54.72, 'In 1337,|y England|r and France|c begin a war that will last more than a hundred_years.|y'),
 (55.12, 60.39, 'Meanwhile, the Mongol empire|r is falling apart. But its trade roads|y still connect China to Europe.|c'),
 (60.79, 66.36, 'And along those roads travels a killer:|r the plague,|r carried by fleas|y on rats and people.'),
 (66.76, 74.25, 'In 1346,|y a Mongol army besieges Caffa,|y a trading port on the Black_Sea.|c The disease breaks out among them.|r'),
 (74.65, 82.38, 'Italian ships|c escape from Caffa. In 1347,|y they bring the plague to Sicily,|r and from there, it spreads across Europe.|r'),
 (82.78, 89.59, 'Next time:|y the year 1405,|y when China sends a giant treasure_fleet|y across the ocean. Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 2: Year 117 (deep version)", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
