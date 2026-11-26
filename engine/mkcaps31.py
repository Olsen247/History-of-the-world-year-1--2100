import sys
SEG = [
 (0.3, 4.88, 'In_one|y single|y year,|g seventeen|g African|y nations|c raised|y their_own|y flags.|r'),
 (5.38, 6.58, ''),
 (6.83, 15.37, "1954:|y Giap's|r men|y drag|y heavy_guns|r up_the|y hills|g around|y Dien_Bien_Phu.|c After|y eight|g weeks,|y the_French|c surrender.|r"),
 (15.77, 21.56, 'That|y November,|y the_FLN|g rises|r in_Algeria.|c France|c will_send|y over|y 400,000|r troops.|y'),
 (21.96, 29.11, '1955:|y at_Bandung,|g 29|c Asian_and|y African|y countries|c condemn|r colonialism.|r'),
 (29.51, 38.03, '1956:|y Nasser|g seizes|r the_Suez|c Canal.|c Britain,|r France|r and_Israel|r invade,|y but_America|c and_the|y Soviets|r force|y them_out.|g'),
 (38.43, 45.5, '1957:|y the_Gold|g Coast|g becomes|y free|c Ghana.|g Nkrumah|y cries:|y Ghana|g is_free|c forever!|g'),
 (45.9, 55.47, "1958:|y only|y Guinea|r votes|y No|r in_de_Gaulle's|c referendum.|y Its_leader,|y Sékou_Touré,|g prefers|y poverty|r in_freedom|c to_riches|g in_slavery.|r"),
 (55.87, 61.84, "1959:|y meanwhile,|y Castro's|r bearded|y rebels|g take|y Cuba,|c 90_miles|r from|y Florida.|c"),
 (62.24, 70.18, '1960:|y Macmillan|c warns_of|y a_wind|c of_change|c in_Africa.|g Weeks|y later,|y police_at|y Sharpeville|r kill_69|r protesters.|y'),
 (70.58, 76.11, 'All_year|y long,|y the_dam|c breaks:|r from|y Senegal|g to|y Somalia,|c seventeen|g nations|y win_their|y freedom.|g'),
 (76.51, 82.12, 'But_in|y the_Congo,|c the_army|y mutinies,|r Katanga|p breaks_away,|r and_the|y UN|c sends_blue|c helmets.|c'),
 (82.52, 87.93, 'Next time:|y 1969,|r when_humans|y walk_on|y the_Moon.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 31: Year 1960", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
