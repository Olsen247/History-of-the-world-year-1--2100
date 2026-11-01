import sys
SEG = [
 (0.30, 5.48, 'Two pistol_shots|r in Sarajevo,|y and within six_weeks,|c five great_powers|r are at_war.|y'),
 (5.98, 7.18, ''),
 (7.43, 14.45, 'In 1911,|y Italy|g invades Ottoman_Libya,|r and an Italian_pilot|c carries out the first_air_raid|r in history.|y'),
 (14.85, 19.88, "In 1912,|y six-year-old Puyi,|y China's last_emperor,|r gives up the_throne.|c"),
 (20.28, 26.16, 'That April,|y the Titanic|c sinks on her very first_voyage.|y About fifteen_hundred|r people die.'),
 (26.56, 32.49, 'In October,|y Serbia,|r Bulgaria,|g Greece|c and Montenegro|p drive the Ottomans|r almost out of_Europe.|y'),
 (32.89, 41.52, 'In 1913,|y the winners fight|r over the spoils.|y Bulgaria loses,|g and after two_wars,|c Serbia is nearly twice|y its old size.|r'),
 (41.92, 50.30, 'By 1914,|y Europe is split|r into two_armed_camps:|y Germany and Austria-Hungary,|r against France,|c Russia|g and Britain.|p'),
 (50.70, 57.44, 'On June_28th,|y nineteen-year-old Gavrilo_Princip|r shoots Archduke Franz_Ferdinand,|y heir to Austria-Hungary,|c and his_wife.|r'),
 (57.84, 63.60, 'One month_later,|y Austria-Hungary|y declares_war|r on Serbia,|c and Russia|g mobilises|r to defend the_Serbs.|y'),
 (64.00, 70.77, 'In August,|y Germany|r declares war on Russia|g and France,|c and marches through neutral_Belgium.|y Britain|p answers with_war.|r'),
 (71.17, 77.69, 'In September,|y the Allies|c stop the Germans|r at the_Marne.|y By Christmas,|g trenches|r run from the North_Sea|c to Switzerland.|y'),
 (78.09, 83.98, 'Next time:|y 1922,|y when four_empires|r have fallen.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 22: Year 1914", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
