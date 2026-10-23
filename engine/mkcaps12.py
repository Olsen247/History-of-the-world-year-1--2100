import sys
SEG = [
 (0.3, 5.38, 'Europe wanted spices|g so badly that one_captain|c sailed around the tip_of_Africa|y to get them.'),
 (5.88, 7.08, ''),
 (7.33, 16.36, 'In 1493,|y the general Askia_Muhammad|y seizes the throne of Songhai,|r and turns it into the largest_empire|g in West African history.'),
 (16.76, 23.3, 'That September,|y Columbus|c sails back across the Atlantic with 17_ships|y and about 1,200_settlers.|g'),
 (23.7, 31.87, 'In 1494,|y Spain_and_Portugal|y sign the Treaty_of_Tordesillas,|c dividing all new lands between them with one_line.|r'),
 (32.27, 38.27, 'That same year, Charles_the_Eighth|c of France invades_Italy,|r and within six_months|y he takes Naples.|r'),
 (38.67, 47.48, 'In 1497,|y the preacher Savonarola|p holds a Bonfire_of_the_Vanities|r in Florence, burning books,|y mirrors and paintings.'),
 (47.88, 52.21, 'In June,|y John_Cabot,|c sailing for England, reaches North_America.|g'),
 (52.61, 57.26, 'In July,|y Vasco_da_Gama|g leaves Lisbon with four_ships,|y bound for India.|c'),
 (57.66, 62.04, 'He sails three_months|r without seeing land,|y then rounds the Cape_of_Good_Hope.|g'),
 (62.44, 68.46, 'In April_1498,|y the ruler of Malindi|c gives him a pilot|y to cross the Indian_Ocean.|c'),
 (68.86, 74.94, 'In May,|y he reaches Calicut|g in India. Europe finally has a sea_road|y to the spices_of_the_East.|g'),
 (75.34, 82.66, "Next time:|y the year 1522,|y when Magellan's|c expedition sails around_the_world.|g Follow the series!|y"),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 12: Year 1498", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
