import sys
SEG = [
 (0.30, 6.08, 'In one_day in 1916,|y almost twenty_thousand|r British soldiers|c are killed.|r'),
 (6.58, 7.78, ''),
 (8.03, 13.83, "Christmas 1914:|y enemy soldiers|r leave their_trenches|c and meet in no_man's_land.|y"),
 (14.23, 20.92, 'April 1915,|y Ypres:|c Germany opens|r nearly six_thousand|y cylinders of chlorine_gas.|g'),
 (21.32, 28.30, "Days later,|y Allied troops,|c many of them Anzacs,|g land at Gallipoli.|r Mustafa_Kemal's men|y hold the heights.|r"),
 (28.70, 35.56, 'In May,|y a U-boat|r sinks the Lusitania.|c Almost twelve_hundred|r die,|y 128 of them American.|c'),
 (35.96, 42.50, 'Ottoman authorities|r force Armenians|y on death_marches.|r Around a_million|y or more die|r in the Armenian_genocide.|y'),
 (42.90, 51.22, 'February 1916:|y Germany hits Verdun|r with over twelve_hundred|y guns.|r The battle will last|c 303 days.|y'),
 (51.62, 56.93, "Pétain's trucks|c roll day_and_night|y up one_road,|r the Sacred_Way,|g to keep Verdun|y alive.|c"),
 (57.33, 64.88, 'At Jutland,|c 250 warships|y clash.|r Britain loses|p more ships,|y but the German_fleet|r never risks|c a full battle|y again.'),
 (65.28, 70.88, 'July 1st,|y the Somme:|r after a week|y of shelling,|r British troops|c walk into|y machine_guns.|r'),
 (71.28, 78.33, 'In September|y come the first_tanks|g in battle.|y By November:|c over a million|r casualties,|y for about ten_kilometres.|g'),
 (78.73, 86.15, 'Next time:|y the road to 1918,|y as America|c joins|g and Russia|r has a revolution.|y Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 23: Year 1916", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
