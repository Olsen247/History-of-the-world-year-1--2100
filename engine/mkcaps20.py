import sys
SEG = [
 (0.3, 6.44, "By 1900,|y Europe had carved_up|r most of Africa.|g And on Britain's_empire,|p the sun never_set.|y"),
 (6.94, 8.14, ''),
 (8.39, 14.81, 'In 1830,|y the first steam_railway|c between two_cities opens in England,|y and France|c invades Algeria.|r'),
 (15.21, 21.39, 'In 1842,|y Britain wins|r the First_Opium_War,|r and China must hand_over|y the island of Hong_Kong.|c'),
 (21.79, 28.78, 'In 1848,|y a beaten Mexico|g signs away half|r its land to the United_States,|c just as gold|y is found in California.|y'),
 (29.18, 37.4, "In 1857,|y a great_revolt|r breaks out against British_rule|p in India.|y A year later,|c Queen_Victoria's|p government takes direct_control.|r"),
 (37.8, 44.49, 'In 1869,|y the Suez_Canal|c opens. Ships from Europe|y no longer have to sail around_Africa|r to reach Asia.|g'),
 (44.89, 52.06, 'In 1871,|y Bismarck|c unites Germany,|y and Wilhelm_the_First|y is proclaimed German_Emperor|r at Versailles,|c in France.'),
 (52.46, 59.76, "In 1884,|y Europe's_powers|r meet in Berlin|c to set the rules for dividing_Africa.|y Not one_African|r is invited."),
 (60.16, 66.89, 'In 1896,|y Emperor Menelik_the_Second|g crushes Italy\'s_army|r at Adwa,|y and Ethiopia|g stays free.'),
 (67.29, 72.82, 'In 1898,|y the United_States|c beats Spain|r and takes the Philippines,|y Puerto_Rico|c and Guam.|g'),
 (73.22, 78.73, "In 1900,|y China's Boxers|r rise against foreigners,|y and eight foreign_armies|c march into Beijing.|y"),
 (79.13, 87.53, 'Next time:|y 1911,|y when Amundsen|c races to the South_Pole,|c and revolution|r breaks out against China\'s last_dynasty.|y Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 20: Year 1900", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
