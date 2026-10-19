import sys
SEG = [
 (0.30, 7.83, 'The year|y 476. The last emperor|r of the Western_Roman_Empire|r has just been removed. Rome has fallen.|r'),
 (8.33, 11.42, "Let's rewind|r to the year 220,|y and watch it happen."),
 (11.82, 18.71, 'In 224,|y Ardashir|y crushes the Parthians,|r and builds a new Persian superpower:|y the Sasanian_Empire.|y'),
 (19.11, 25.12, 'In 260,|y the Persians do the unthinkable.|r They capture a Roman emperor,|r Valerian.|y'),
 (25.52, 31.70, 'Rome starts breaking apart.|r Gaul|c splits off in the west, and Queen_Zenobia|p of Palmyra seizes the east.|p'),
 (32.10, 37.27, 'But Emperor Aurelian|y fights back, and by 274,|y he has won it all back.|g'),
 (37.67, 42.68, 'In 330,|y Constantine|y builds a new capital in the east: Constantinople.|p'),
 (43.08, 47.09, 'Then the Huns|r storm out of the steppe, and push the Goths|y into Roman land.|r'),
 (47.49, 53.48, 'In 395,|y the empire splits for good,|r into a Western half,|r and an Eastern half.|p'),
 (53.88, 59.97, 'In 410,|y the Visigoths|y sack the city of Rome,|r for the first time in 800_years.|y'),
 (60.37, 64.58, 'The Vandals|p seize North_Africa,|y and Attila_the_Hun|r invades Gaul and Italy.'),
 (64.98, 73.36, 'Piece by piece, Germanic kingdoms|y carve up the West.|r Until, in 476,|y the general Odoacer|c removes the last emperor.|r'),
 (73.76, 81.29, 'Meanwhile in India,|y the Gupta_Empire|y is in a golden_age.|y And this very year, the great mathematician Aryabhata|c is born.'),
 (81.69, 88.39, 'Next time:|y the year 750,|y when one empire stretches from Spain to India.|g Follow the series!|y'),
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
