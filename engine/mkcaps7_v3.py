import sys
SEG = [
 (0.3, 5.73, 'Nomads|y on horseback have just conquered all of China,|r and built the largest_land_empire|y in history.'),
 (6.23, 7.43, ''),
 (7.68, 13.51, 'In 1066,|y William_of_Normandy|y crosses the Channel, and conquers England|r at the Battle_of_Hastings.|y'),
 (13.91, 21.85, 'In 1096,|y thousands of European knights|c march east in the First_Crusade,|r and in 1099,|y they capture Jerusalem.|y'),
 (22.25, 27.83, 'But in 1187,|y the sultan Saladin|g crushes the crusaders,|r and takes Jerusalem back.|y'),
 (28.23, 36.29, 'Far to the east, in 1206,|y a warrior named Temujin|y unites the Mongol tribes.|r He takes the name: Genghis_Khan.|r'),
 (36.69, 43.03, 'His horse archers|r sweep across Asia.|y Northern_China, Central_Asia,|y and Persia|y fall, one after another.|r'),
 (43.43, 48.83, 'His grandsons|y push even further. They burn Kyiv,|r and ride all the way into Poland|c and Hungary.|c'),
 (49.23, 55.69, 'In 1258,|y they destroy Baghdad,|r the capital of the Islamic world|g for five_hundred years.|y'),
 (56.09, 61.7, 'But in 1260,|y at Ain_Jalut,|y the Mamluks|g of Egypt finally defeat a Mongol army.|r'),
 (62.1, 70.3, 'Kublai_Khan|y moves his capital to Beijing.|y In 1279,|y the last Song emperor|r dies at sea, and all of China is Mongol.|r'),
 (70.7, 74.92, "Meanwhile, a young Venetian named Marco_Polo|c is serving at Kublai_Khan's court.|y"),
 (75.32, 83.53, 'Next time:|y the year 1347,|y when a deadly plague|r called the Black_Death|r sweeps across the world. Follow the series!|y'),
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
