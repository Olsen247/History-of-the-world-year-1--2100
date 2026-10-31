import sys
SEG = [
 (0.30, 5.95, 'A Norwegian|r wins the race to the bottom_of_the_world,|c and two_thousand_years|y of Chinese_emperors|r start to crumble.'),
 (6.45, 7.65, ''),
 (7.90, 15.78, 'In 1901,|y Australia|p unites into one_nation,|g and weeks later, Queen_Victoria|p dies after sixty-three_years|y on the throne.'),
 (16.18, 22.45, 'In 1902,|y Britain wins|r the brutal Boer_War,|r and the two Boer_republics|y are forced to accept British_rule.|p'),
 (22.85, 29.30, 'In 1903,|y the Wright_brothers|c make the first powered|y airplane_flight|c at Kitty_Hawk.|y It lasts just twelve_seconds.|r'),
 (29.70, 38.37, "In 1905,|y Japan|r destroys Russia's_fleet|c at Tsushima.|y For the first_time|y in modern history, an Asian_nation|g defeats a European great_power.|r"),
 (38.77, 44.52, 'That same_year,|y Norway|r breaks free|g from its union with Sweden,|c and a Danish_prince|y becomes King_Haakon_the_Seventh.|r'),
 (44.92, 51.06, 'In 1908,|y after reports of horrific_abuse,|r Belgium|y takes the Congo|g away from King_Leopold_the_Second.|p'),
 (51.46, 57.54, 'In 1910,|y Japan|r annexes Korea.|c Korea will stay under Japanese_rule|r for thirty-five_years.|y'),
 (57.94, 64.24, 'Months later, the Mexican_Revolution|g erupts against Porfirio_Díaz,|y who has dominated Mexico|g for over thirty_years.|r'),
 (64.64, 72.44, "In October_1911,|y soldiers rise_up|r in Wuchang,|y and province_after_province|r breaks away from China's Qing_dynasty.|y"),
 (72.84, 79.63, "On December_14th,|y Roald_Amundsen|r plants Norway's_flag|r at the South_Pole,|c thirty-four_days|y before Britain's Robert_Scott|c arrives."),
 (80.03, 87.06, 'Next time:|y 1914,|y when two_shots|r in Sarajevo|c drag the world|y into war.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 21: Year 1911", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
