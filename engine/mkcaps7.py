import sys
SEG = [
 (0.30, 8.33, 'The year|y 1279.|y The Mongols|r have just conquered all of China,|y completing the largest land empire|r the world has ever seen.'),
 (8.83, 11.92, "Let's rewind|r to the year 1000,|y and see how it happened."),
 (12.32, 18.15, 'In 1066,|y William_of_Normandy|y crosses the Channel, and conquers England|r at the Battle_of_Hastings.|y'),
 (18.55, 26.49, 'In 1096,|y thousands of European knights|c march east in the First_Crusade,|r and in 1099,|y they capture Jerusalem.|y'),
 (26.89, 32.47, 'But in 1187,|y the sultan Saladin|g crushes the crusaders,|r and takes Jerusalem back.|y'),
 (32.87, 40.93, 'Far to the east, in 1206,|y a warrior named Temujin|y unites the Mongol tribes.|r He takes the name: Genghis_Khan.|r'),
 (41.33, 47.67, 'His horse archers|r sweep across Asia.|y Northern_China, Central_Asia,|y and Persia|y fall, one after another.|r'),
 (48.07, 53.47, 'His grandsons|y push even further. They burn Kyiv,|r and ride all the way into Poland|c and Hungary.|c'),
 (53.87, 60.34, 'In 1258,|y they destroy Baghdad,|r the capital of the Islamic world|g for five_hundred years.|y'),
 (60.74, 66.35, 'But in 1260,|y at Ain_Jalut,|y the Mamluks|g of Egypt finally defeat a Mongol army.|r'),
 (66.75, 74.95, 'Kublai_Khan|y moves his capital to Beijing.|y In 1279,|y the last Song emperor|r dies at sea, and all of China is Mongol.|r'),
 (75.35, 79.56, "Meanwhile, a young Venetian named Marco_Polo|c is serving at Kublai_Khan's court.|y"),
 (79.96, 88.17, 'Next time:|y the year 1347,|y when a deadly plague|r called the Black_Death|r sweeps across the world. Follow the series!|y'),
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
