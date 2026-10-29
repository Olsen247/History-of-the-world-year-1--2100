import sys
SEG = [
 (0.3, 6.22, 'Spain ruled half_the_Americas|y for 300_years.|r Then rebel_armies|c crossed the Andes.|g'),
 (6.72, 7.92, ''),
 (8.17, 14.8, 'In 1815,|y Napoleon falls|r at Waterloo,|c and is sent to a tiny_island,|y Saint_Helena.|c'),
 (15.2, 23.21, 'In 1816,|y Europe gets a year without_a_summer,|c after the biggest_eruption|r in recorded history:|y Mount_Tambora.|r'),
 (23.61, 29.13, "That July,|y the United_Provinces,|c the heart of today's Argentina,|g declare independence.|y"),
 (29.53, 36.26, 'In 1817,|y San_Martín|c leads about 5,000_men|y over the frozen_Andes|c to free Chile.|g'),
 (36.66, 43.58, 'In 1819,|y Bolívar|y crosses the Andes too,|c wins at Boyacá,|r and Gran_Colombia|g is born.'),
 (43.98, 50.2, 'In July_1821,|y San_Martín|c marches into Lima|y and declares Peru|r independent.|g'),
 (50.6, 55.34, 'Two months later,|y Mexico|g is free,|y after eleven_years|r of war.'),
 (55.74, 62.87, 'In 1822,|y Prince_Pedro|c shouts: Independence_or_death!|r And becomes emperor|y of Brazil.|g'),
 (63.27, 69.81, 'In 1823,|y US President_Monroe|c warns Europe:|r no new_colonies|y in the Americas.|c'),
 (70.21, 78.6, "In 1824,|y Sucre crushes|c Spain's last_big_army|r at Ayacucho,|y and a new country|g takes Bolívar's_name:|y Bolivia.|p"),
 (79.0, 85.57, 'Next time:|y 1900,|y when a few_empires|r rule much of the world.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 19: Year 1825", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
