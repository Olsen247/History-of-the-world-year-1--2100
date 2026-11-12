import sys
SEG = [
 (0.30, 5.03, 'Less_than|y twenty-one_years|c after the|y war_to_end_all_wars,|r the_world|y was at_war|r again.|y'),
 (5.53, 6.73, ''),
 (6.98, 14.43, 'October 1929:|y Wall_Street|c crashes.|r By 1932,|y six_million|r Germans|y are out_of_work.|c'),
 (14.83, 21.65, '1931:|y Japanese_officers|r bomb_their|y own_railway|c in_Manchuria,|y blame_China,|p and within_months|y seize_it_all.|r'),
 (22.05, 28.44, '1933:|y Hitler|r takes_power|y in_Germany.|c Other_parties|y are_banned,|r and the|y persecution|r of_Jews|c begins.|y'),
 (28.84, 37.91, "1936:|y Spain's_generals|r revolt,|y and civil_war|r begins.|y In 1937,|c German_and|y Italian_bombers|r devastate|y Guernica.|g"),
 (38.31, 45.99, '1937:|y Japan|r goes_to|y full_war|r with_China.|c Shanghai|y falls,|r and at|y Nanjing,|c Japanese_troops|y massacre|r civilians.|y'),
 (46.39, 53.81, '1938:|y German_troops|c enter_Austria|y unopposed.|g In_November,|y Nazi_mobs|r burn_synagogues:|y Kristallnacht.|r'),
 (54.21, 60.46, 'At Munich,|y Britain_and_France|c hand_Hitler|y the_Sudetenland.|r In 1939,|y he_takes|c Prague_too.|r'),
 (60.86, 66.64, 'August 1939:|y Hitler_and_Stalin|r make_a_pact,|y and secretly|c agree_to|y split_Poland.|r'),
 (67.04, 74.92, 'September_1st:|y Germany|r invades_Poland.|c Panzers|y punch_through,|r Stukas|y hit_roads|c and_towns,|r radio|y links_it_all:|c Blitzkrieg.|r'),
 (75.32, 81.37, 'Britain_and_France|c declare_war.|r The_Soviets|y invade|r from_the_east,|c and Warsaw|y falls_after|r a_three-week_siege.|y'),
 (81.77, 87.10, 'Next time:|y 1941,|r from_Dunkirk|c to_Pearl_Harbor.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 26: Year 1939", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
