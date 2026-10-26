import sys
SEG = [
 (0.3, 4.99, 'One Dutch_captain|y sailed all the way around_Australia,|g and never once saw|r its mainland.'),
 (5.49, 6.69, ''),
 (6.94, 12.97, 'In 1552,|y Ivan_the_Terrible|r blows up the walls of Kazan,|y and Russia|g turns east.'),
 (13.37, 20.62, 'In 1571,|y at Lepanto,|c over 400_galleys|y clash, and the Ottoman_fleet|r is smashed.'),
 (21.02, 28.82, "In 1588,|y Spain's Armada|y sails for England.|r Fireships|r scatter it, and storms|c wreck many of its ships."),
 (29.22, 36.94, 'In 1600,|y Tokugawa_Ieyasu|c wins at Sekigahara.|r His family will rule Japan|y for over 250_years.|g'),
 (37.34, 43.58, "In 1606,|y Willem_Janszoon's|c ship Duyfken makes the first_recorded|y European landing in Australia.|g"),
 (43.98, 49.94, 'In 1607,|y English settlers|c found Jamestown,|y their first lasting_colony|g in America.'),
 (50.34, 56.85, 'In 1616,|y Dirk_Hartog|c nails a pewter_plate|y to a post, on an island off Western_Australia.|g'),
 (57.25, 64.05, "In 1630,|y Sweden's Gustavus_Adolphus|c joins the Thirty_Years'_War,|r and wins big|y at Breitenfeld.|y"),
 (64.45, 70.43, 'In 1632,|y Shah_Jahan|g begins the Taj_Mahal,|y a tomb for his beloved_wife.|p'),
 (70.83, 79.13, 'In 1642,|y Abel_Tasman|c reaches Tasmania and New_Zealand,|g where a Māori_canoe|p rams his boat, and four sailors die.|r'),
 (79.53, 85.75, "Next time:|y 1770,|y when James_Cook|c maps Australia's east coast.|g Follow the series!|y"),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 15: Year 1642", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
