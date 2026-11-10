import sys
SEG = [
 (0.30, 5.67, 'The Great_War|r tore apart|y four_empires,|c while a_flu|g killed more_people|r than the_war_itself.|y'),
 (6.17, 7.37, ''),
 (7.62, 14.82, 'Autumn 1918:|y the Spanish_flu|g rides the_troopships|c around the_globe.|y Tens_of_millions|r die.|r'),
 (15.22, 23.11, 'As the_empires|y collapse,|r new_nations|g rise:|y Poland|r returns after|y 123_years,|c beside Czechoslovakia|p and the_Baltic_states.|c'),
 (23.51, 32.41, 'June 1919,|y Versailles:|c Germany|r loses its_colonies,|y 13_percent|r of_its_land,|y and all_but|c 100,000_soldiers.|g'),
 (32.81, 39.20, '1920:|y the League_of_Nations|c is_born,|y without_America.|r Britain_and_France|p take the|y Ottoman_Arab_lands.|g'),
 (39.60, 46.88, 'August 1920:|y the Red_Army|r reaches_Warsaw,|c but_Piłsudski|y hits its|r open_flank.|g The Miracle|y on_the_Vistula!|c'),
 (47.28, 54.42, "November 1920:|y the last|r White_army|c flees_Crimea|y by_ship.|c Trotsky's_Reds|r have all_but|y won the_civil_war.|g"),
 (54.82, 61.71, 'December 1921:|y a treaty|c with_Britain|y creates the|g Irish_Free_State.|g Six_northern_counties|p stay_British.|c'),
 (62.11, 68.12, "October 1922:|y Mussolini's|r Blackshirts|p march_on_Rome,|y and the_king|c makes_him|y prime_minister.|r"),
 (68.52, 74.21, 'Mustafa_Kemal|r drives_the_Greeks|c out_of_Anatolia,|y and the|y Ottoman_sultanate|r ends after|y over_600_years.|g'),
 (74.61, 81.83, 'And on|y December_30th,|c Russia,_Ukraine,|r Belarus_and|y Transcaucasia|p unite as|y one_new_giant:|g the_Soviet_Union.|r'),
 (82.23, 87.45, 'Next time:|y 1939,|r and an|y even_bigger_war.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 25: Year 1922", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
