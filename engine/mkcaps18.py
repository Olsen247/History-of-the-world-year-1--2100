import sys
SEG = [
 (0.30, 5.03, 'One officer|y crowned himself emperor,|g conquered half_of_Europe,|c and then marched into Russia.|r'),
 (5.53, 6.73, ''),
 (6.98, 14.12, 'In 1783,|y Britain accepts|c American_independence,|g and the new United_States|c stretches all the way to the Mississippi.|y'),
 (14.52, 21.89, 'In 1788,|y eleven British_ships|r bring over 700_convicts|y to Sydney_Cove.|c British_Australia|g begins.'),
 (22.29, 29.19, 'In July_1789,|y the people of Paris|c storm the Bastille|r prison. The French_Revolution|y has begun.'),
 (29.59, 38.11, "In 1795,|y Russia, Prussia and Austria|c swallow the rest of Poland.|r It won't be free again|y for 123_years.|r"),
 (38.51, 45.23, 'In 1798,|y the young general Napoleon|c invades Egypt,|y but Nelson|c destroys his fleet|r at the Nile.|y'),
 (45.63, 52.35, 'In 1803,|y Napoleon sells Louisiana|c to the United_States|g for 15_million_dollars,|y doubling its size.|g'),
 (52.75, 59.16, 'In 1804,|y Haiti wins independence|g after a huge slave_revolt,|r and Napoleon|c crowns himself emperor.|y'),
 (59.56, 67.13, 'In 1805,|y Nelson dies|r winning at Trafalgar,|c but on land Napoleon|y crushes Austria and Russia|r at Austerlitz.|y'),
 (67.53, 75.15, 'By 1812,|y Napoleon dominates|c most_of_Europe.|g In June,|y he invades Russia|r with more than 400,000_men.|y'),
 (75.55, 81.71, 'In September,|y he takes Moscow,|c but the city burns,|r and in the freezing_retreat|c most of his army is lost.|r'),
 (82.11, 87.86, 'Next time:|y 1825,|y when Latin_America|g has broken free.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 18: Year 1812", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
