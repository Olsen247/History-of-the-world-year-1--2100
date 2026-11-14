import sys
SEG = [
 (0.30, 6.74, 'In_under|y two_years,|c Hitler|r conquered|y most_of_Europe.|r Then he|y turned_east,|c and Japan|r struck_America.|y'),
 (7.24, 8.44, ''),
 (8.69, 16.86, 'November 1939:|y the_Soviets|r attack_Finland.|c Finnish|y ski_troops|c in_white|y hold_out|g for_over|y three_months.|c'),
 (17.26, 25.38, 'April 1940:|y Germany|r invades|y Denmark|c and_Norway.|r Oscarsborg|g fortress|y sinks_the|y cruiser_Blücher.|c'),
 (25.78, 30.90, 'May:|y panzers|r race_through|y the_Ardennes|c forest,|y and_reach|y the_Channel|c in_just|y ten_days.|r'),
 (31.30, 38.26, 'At Dunkirk,|y destroyers|c and_little|y boats|c rescue|g 338,000|y soldiers.|g In_June,|y France|c falls.|r'),
 (38.66, 45.46, 'Battle_of_Britain:|y radar|c spots_the|y raids,|r RAF_fighters|c meet_the|y bombers,|r and_Hitler|y postpones|c his_invasion.|y'),
 (45.86, 52.69, '1941:|y Rommel|r lands_in|y Libya,|c and_Germany|y overruns|r Yugoslavia|c and_Greece.|y'),
 (53.09, 59.07, '22 June:|y three_million|r Germans|y and_three|y thousand|c tanks|r invade_the|y Soviet_Union.|c'),
 (59.47, 67.63, 'Panzer|y pincers|r trap_whole|y Soviet_armies.|c At Babi_Yar,|y German|y killing_squads|r murder_over|y 33,000_Jews|c in_two_days.|y'),
 (68.03, 72.26, 'In_freezing|c cold,|y the_Germans|y stall|r before_Moscow,|c and_Zhukov|y strikes_back.|g'),
 (72.66, 79.33, '7 December:|y over_350|r Japanese|y planes|c from_six|y carriers|c hit_Pearl|y Harbor,|r and_America|y joins_the_war.|c'),
 (79.73, 87.13, 'Next time:|y Year 1943|r – Midway,|c Stalingrad|r and Kursk.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 27: Year 1941", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
