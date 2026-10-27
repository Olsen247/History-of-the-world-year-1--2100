import sys
SEG = [
 (0.3, 3.65, 'A fight|r over tea|g is about to give birth|y to a brand_new_nation.|c'),
 (4.15, 5.35, ''),
 (5.6, 12.59, 'In 1770,|y British_soldiers|r fire into a crowd in Boston|c and kill five_people:|r the Boston_Massacre.|y'),
 (12.99, 19.87, 'In 1772,|y Russia, Prussia and Austria|c carve up Poland,|r taking almost a third|y of its land.'),
 (20.27, 26.73, 'In January_1773,|y James_Cook|c becomes the first known_explorer|g to cross the Antarctic_Circle.|c'),
 (27.13, 34.39, 'In 1773,|y the Cossack Pugachev|r pretends to be the dead_tsar,|p and leads a huge_revolt|r against Catherine_the_Great.|c'),
 (34.79, 41.55, 'That December,|y Boston_colonists,|c some disguised as Mohawks,|p dump 342_chests|y of tea into the harbor.|g'),
 (41.95, 49.28, 'In April_1775,|y the first_shots|r ring out at Lexington_and_Concord.|c The American_Revolution|y has begun.'),
 (49.68, 56.83, 'In June_1775,|y the British win|r at Bunker_Hill,|c but over a thousand|y of their soldiers are killed or wounded.|r'),
 (57.23, 64.11, 'In March_1776,|y George_Washington|c puts cannons|r on the hills above Boston,|y and the British sail away.|g'),
 (64.51, 70.88, 'In June_1776,|y on the far side|c of the continent,|y Spanish settlers|g arrive to found San_Francisco.|y'),
 (71.28, 80.6, 'On July_4th,_1776,|y Congress adopts|c the Declaration_of_Independence,|y written mostly by Thomas_Jefferson.|c The United_States|g is born.|y'),
 (81.0, 86.57, 'Next time:|y 1812,|y when Napoleon|c marches on Moscow.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 17: Year 1776", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
