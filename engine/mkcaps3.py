import sys
SEG = [
 (0.30, 7.20, "The year|y 220. China's Han_dynasty,|r which ruled for over four_hundred years,|y has just collapsed.|r"),
 (7.80, 11.85, "Let's rewind|r to the year 117,|y and watch it fall apart."),
 (12.65, 18.28, 'In 184,|y a huge peasant army, the Yellow_Turbans,|y rises up against the emperor.|r'),
 (18.78, 23.55, 'The rebellion is crushed,|r but the generals who crushed it become powerful warlords.|r'),
 (24.00, 28.33, 'In 190,|y the warlord Dong_Zhuo|r burns the capital,|r Luoyang.|y'),
 (28.83, 34.57, 'The strongest warlord, Cao_Cao,|c takes control of the north,|c and of the emperor himself.|y'),
 (35.07, 41.73, 'In 208,|y he marches south. But at the Battle_of_Red_Cliffs,|r his fleet is burned|r by Sun_Quan|y and Liu_Bei.|g'),
 (42.33, 47.29, "In 220,|y Cao_Cao's son|c forces the last Han_emperor|r to give up his throne."),
 (47.79, 53.74, 'China splits into three_kingdoms:|y Wei|c in the north, Shu|g in the west, and Wu|r in the south.'),
 (54.29, 61.98, 'War, famine and disease|r are brutal. The official count drops from 56_million|y people, to only about 8_million.|r'),
 (62.54, 68.26, 'Meanwhile in Rome,|r Emperor Caracalla|y makes almost every free person in the empire a Roman_citizen.|y'),
 (68.76, 74.16, 'And in Persia,|y the Parthians are weakening.|r A rebel named Ardashir|r is about to overthrow them.'),
 (74.76, 80.94, 'Next time: the year 476,|y when the Western_Roman_Empire|r falls. Follow the series!|y'),
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
