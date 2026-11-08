import sys
SEG = [
 (0.30, 6.41, 'In March 1918,|y Germany nearly_won|r the_war.|c Eight months_later,|y it had_lost.|r'),
 (6.91, 8.11, ''),
 (8.36, 16.67, '1917:|y Germany unleashes|r all-out U-boat_war.|c In April_alone,|y over 850,000_tons|r of ships|c go_down.|r'),
 (17.07, 23.56, 'March 1917:|y riots and mutinies|r in Petrograd|c force Tsar_Nicholas|y the_Second to_abdicate.|r'),
 (23.96, 30.14, 'Britain decodes|c a German offer|r to give Mexico|g three US_states.|y In April,|y America|c declares_war.|r'),
 (30.54, 36.94, 'July 1917:|y Arab fighters|g with T._E._Lawrence|y storm Aqaba|r from its unguarded|c land_side.|y'),
 (37.34, 43.49, "November:|y Lenin's Bolsheviks|r seize power,|y then give_up|c Poland, the_Baltics|y and Ukraine|g for_peace.|c"),
 (43.89, 51.56, 'March 1918:|y after five_hours|r of shelling|y from 6,600_guns,|r stormtroopers|c slip through|y the_fog.|g'),
 (51.96, 58.56, 'They punch|r up to 60_kilometres|y deep and shell_Paris.|r But by_summer,|y 10,000_Americans|c arrive every_day.|g'),
 (58.96, 65.76, "August 8th,|y Amiens:|c over 500_tanks|g break_through.|r Ludendorff calls_it|y the German_Army's|c black_day.|r"),
 (66.16, 72.09, 'Damascus falls.|g German_sailors|y mutiny.|r On November_10th,|y the Kaiser|c flees to the_Netherlands.|y'),
 (72.49, 78.42, 'At 11_a.m.|y on November_11th,|y the guns|r fall_silent.|g Around nine_million|r soldiers|y are_dead.|r'),
 (78.82, 85.73, 'Next time:|y 1922,|y as new_countries|g rise and the|c Ottoman_Empire|r ends.|y Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 24: Year 1918", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
