import sys
SEG = [
 (0.3, 5.45, 'Half_a_million|y American|c troops|y could_not|r win|y this_war|y – and_the|y last|r Americans|c fled_by|y helicopter.|g'),
 (5.95, 7.15, ''),
 (7.4, 16.0, 'Tet,|r 1968:|y some|y 80,000|r communist|r troops|y strike|y over_100|g towns|y at_once|y – even_the|y US_embassy.|c'),
 (16.4, 22.82, 'Hue|y is_retaken|g street_by|y street.|y Tet|r fails|y in_battle|y – but|y Americans|c stop_believing|r in_victory.|y'),
 (23.22, 29.11, 'Supplies|y flow_south|y on_the|y Ho_Chi_Minh|g Trail|g through_Laos|c – despite|y millions_of_tons|r of_American|c bombs.|r'),
 (29.51, 36.1, "America's|c answer:|y Huey|g helicopters,|g dropping|y troops|y straight_into|y the_jungle.|g But_the|y enemy|r hides|y in_tunnels.|r"),
 (36.5, 43.19, 'Nixon|c starts|y bringing|y troops_home.|g Then_the|y world|y learns_of|y My_Lai:|r US_soldiers|c had_murdered|r hundreds_of|y villagers.|y'),
 (43.59, 52.32, '1970:|y troops|y push_into|y Cambodia.|c Protests|r explode|y – at|y Kent_State,|c guardsmen|y shoot_four|r students_dead.|y'),
 (52.72, 59.97, '1973:|y a_peace|g deal|y in_Paris.|c By_March,|y the_last|y US_combat|c troops|y are_gone.|g'),
 (60.37, 67.53, "1975:|y the_North|r attacks.|y Hue_and|y Da_Nang|c fall,|r and_the|y South's|y army|y collapses.|r"),
 (67.93, 73.97, 'In_Cambodia,|y the_Khmer|r Rouge|r seize|y Phnom_Penh.|c Their_regime|y will_cost|y up_to|y two_million|r lives.|y'),
 (74.37, 81.55, '30_April:|y the_last|y helicopters|g leave|y Saigon.|c Hours_later,|y a_North|r Vietnamese|r tank|y smashes|y the_palace|y gate.|g'),
 (81.95, 88.02, 'Next time:|y 1991,|r when_the|y Soviet_Union|c falls_apart.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 33: Year 1975", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
