import sys
SEG = [
 (0.30, 5.41, 'Within five years,|y the_allies|c who_beat|y Hitler|r became|y enemies,|r and_the|y world|g split_in_two.|c'),
 (5.91, 7.11, ''),
 (7.36, 13.07, '1946:|y Churchill|c warns_that|y an_iron|r curtain|r has_come|y down_across|y Europe.|g'),
 (13.47, 20.89, '1947:|y the_Marshall|c Plan|c offers|y 13_billion|g dollars|g to_rebuild|y Europe.|c Stalin|r says_no.|y'),
 (21.29, 30.36, '1948:|y Stalin|r blockades|y West_Berlin.|c Allied|c planes|y fly_in|y food_and_coal,|g at_the_peak|y almost|y one_a_minute.|r'),
 (30.76, 38.32, '1949:|y twelve|g nations,|y Norway|r among_them,|y found|y NATO.|c West_Germany|g is_born.|y'),
 (38.72, 42.01, 'August:|y the_Soviets|r test|y their_own|y atomic|r bomb.|r'),
 (42.41, 48.54, "October:|y Mao_Zedong|r proclaims|y the_People's|y Republic|r of_China.|r Chiang_Kai-shek|g flees_to|y Taiwan.|c"),
 (48.94, 56.15, 'June 1950:|y North_Korean|r T-34|r tanks|y invade|y the_South.|c Seoul|g falls|y in_three|y days.|r'),
 (56.55, 64.47, 'September:|y MacArthur|c lands|y 75,000|g men|y at_Inchon,|c and_by|y October,|y UN_troops|c race|y north|y toward_China.|r'),
 (64.87, 72.09, 'Then|y China|r strikes.|r Hundreds_of|y thousands|r of_soldiers|y cross_the|y Yalu|c and_attack|y at_night,|p in_minus|y 30_degrees.|c'),
 (72.49, 79.39, "In_July|y 1953,|g after|y Stalin's|r death,|y an_armistice|g is_signed.|y Korea|c stays|y divided.|r"),
 (79.79, 87.18, 'Next time:|y Year 1960|r – seventeen|g African|y nations|y win_freedom|c in_one|y year.|g Follow the series!|y'),
]
out = []
for a, b, txt in SEG:
    words = txt.split(); groups = []; cur = []
    for w in words:
        cur.append(w)
        plain = w.split("|")[0]
        if len(cur) >= 3 or plain.endswith((".", ",", "!", ":", "?")) or sum(len(x.split("|")[0]) for x in cur) >= 17:
            groups.append(cur); cur = []
    if cur: groups.append(cur)
    lens = [sum(len(x.split("|")[0]) + 2 for x in g) for g in groups]; tot = sum(lens); t = a
    for g, L in zip(groups, lens):
        d = (b - a) * L / tot
        out.append(f"{t:.2f} {t + d - 0.03:.2f} " + " ".join(g)); t += d
open(sys.argv[1], "w").write("\n".join(out) + "\n")
narr = ["NARRATION SCRIPT – History of the World, Episode 30: Year 1953", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
