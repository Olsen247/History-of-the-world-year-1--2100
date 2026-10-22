import sys
SEG = [
 (0.3, 5.56, 'Three small_ships|c are about to sail west into the unknown,|y and change the world_forever.|r'),
 (6.06, 7.26, ''),
 (7.51, 12.71, "In 1455,|y England's Wars_of_the_Roses|r begin at St_Albans.|y"),
 (13.11, 19.64, "In 1462,|y Vlad_the_Impaler|r of Wallachia raids Sultan_Mehmed's|y camp in a daring night_attack.|r"),
 (20.04, 27.94, "In 1467,|y Japan's Onin_War|r begins. Kyoto_burns,|r and a century of civil_war|y follows."),
 (28.34, 35.63, 'In 1468,|y Sonni_Ali|y of Songhai captures Timbuktu,|g a great city of trade_and_learning.|c'),
 (36.03, 43.27, 'In 1469,|y Isabella|p of Castile marries Ferdinand|c of Aragon, uniting the crowns that become Spain.|y'),
 (43.67, 50.97, 'In 1480,|y Ivan_the_Third|g of Moscow faces down the Great_Horde|r at the Ugra River, and Moscow breaks_free.|y'),
 (51.37, 57.82, 'In 1488,|y Bartolomeu_Dias|g becomes the first_European|y to sail around the southern end of Africa.|c'),
 (58.22, 65.44, 'In January 1492,|y Granada_surrenders,|r ending almost 800_years|y of Muslim rule in Spain.'),
 (65.84, 70.88, 'In August,|y Christopher_Columbus|c sails from Spain with the Niña,|y the Pinta|y and the Santa_María.|y'),
 (71.28, 76.67, 'On October_12th,|y he lands in the Bahamas|c and meets the Taíno|g people. He thinks he has reached Asia.|r'),
 (77.07, 83.91, 'Next time:|y the year 1498,|y when Vasco_da_Gama|c reaches India|g by sea. Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 11: Year 1492", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
