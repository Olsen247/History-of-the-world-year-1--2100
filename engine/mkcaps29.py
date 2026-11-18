import sys
SEG = [
 (0.30, 5.61, 'The_deadliest|y war|r in_history|y is_ending,|c and_one|y bomb|r can_now|y destroy_a|y whole_city.|g'),
 (6.11, 7.31, ''),
 (7.56, 15.43, 'July 1943:|y the_Allies|c land_in|y Sicily,|g Mussolini|r falls,|y and_Italy|c surrenders.|g'),
 (15.83, 25.89, 'D-Day,|r June 1944:|y 156,000|r Allied_troops|c reach|y Normandy|g by_sea|c and_air.|y By_August,|y Paris|g is_free.|c'),
 (26.29, 32.24, 'Operation|y Bagration:|r Soviet_tanks|c smash|r Army_Group|y Centre|c and_race|y 500_kilometres|g to_Warsaw.|c'),
 (32.64, 38.51, 'October:|y at_Leyte|c Gulf,|c Japan\'s_navy|r is_crushed,|y and_the|y first|g kamikaze|r pilots_strike.|y'),
 (38.91, 44.55, 'December:|y Hitler\'s|r last_gamble|y in_the|y Ardennes.|c Bastogne|g holds,|y and_Patton|c breaks_through.|g'),
 (44.95, 53.24, 'January 1945:|y Soviet_soldiers|c reach|y Auschwitz.|p The_Nazis|y murdered|r six_million|p Jews.|y'),
 (53.64, 60.61, 'February:|y US_Marines|c storm|y Iwo_Jima.|g Almost_none|y of_its|y 21,000|r defenders|y surrender.|c'),
 (61.01, 66.81, 'April:|y the_Red|r Army|r storms|y Berlin.|c Hitler|r kills_himself,|y and_Germany|c surrenders.|g'),
 (67.21, 73.12, 'August:|y atomic|r bombs|r destroy|y Hiroshima|c and_Nagasaki,|c and_the|y Soviets|r invade|y Manchuria.|g'),
 (73.52, 78.66, 'September 2:|y Japan|r surrenders.|g More_than|y 70_million|r people|y have_died.|c'),
 (79.06, 86.70, 'Next time:|y Year 1953|r – the_Iron|c Curtain|c and_the|y Korean_War.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 29: Year 1945", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
