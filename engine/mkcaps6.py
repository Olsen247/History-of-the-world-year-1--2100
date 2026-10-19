import sys
SEG = [
 (0.30, 6.18, 'The year|y 1000.|y Viking explorers|c have just become the first Europeans to set foot in America.|r'),
 (6.68, 9.99, "Let's rewind|r to the year 750,|y and follow their journey."),
 (10.39, 17.84, 'In 793,|y raiders from Scandinavia|c attack the monastery of Lindisfarne,|y in England. The Viking_Age|r has begun.'),
 (18.24, 23.89, 'In 800,|y the Frankish king Charlemagne|c is crowned emperor.|y He rules most of Western_Europe.|c'),
 (24.29, 31.58, 'Viking longships|c raid Britain, Ireland and France.|y In 845,|y they even sail up the Seine, and attack Paris.|r'),
 (31.98, 38.23, 'Swedish Vikings|c sail east, down the great rivers of Russia,|y and found a new state: the Kievan_Rus.|g'),
 (38.63, 46.23, 'Others settle Iceland.|c And in 911,|y a Viking chief named Rollo|y is given land in France. It becomes Normandy.|y'),
 (46.63, 52.66, 'In 982,|y Erik_the_Red|r is banished from Iceland. He sails west, and settles Greenland.|c'),
 (53.06, 61.42, "Around the year 1000,|y his son Leif_Erikson|y reaches a land he calls Vinland.|g It's North_America,|r almost 500_years|y before Columbus."),
 (61.82, 66.25, 'Meanwhile, the Byzantine emperor Basil_the_Second|p is at war with the Bulgarians.|r'),
 (66.65, 72.54, 'The Islamic world|g is now split, and Cordoba,|y in Spain, is one of the biggest cities on Earth.|y'),
 (72.94, 79.62, "China's Song_dynasty|y is using gunpowder|r in war. And in Japan, Murasaki_Shikibu|p writes one of the first novels.|y"),
 (80.02, 87.88, 'Next time:|y the year 1279,|y when the Mongols|r build the largest land empire in history.|y Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 2: Year 117 (deep version)", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
