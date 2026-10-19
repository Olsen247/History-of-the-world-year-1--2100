import sys
SEG = [
 (0.30, 7.86, 'The year|y 750.|y A new dynasty, the Abbasids,|c rules an empire that stretches from Africa|y all the way to India.|y'),
 (8.36, 12.20, "Let's rewind|r to the year 476,|y and see how it happened."),
 (12.60, 21.17, 'In 527,|y Justinian|p becomes emperor in Constantinople.|p His general Belisarius|y sails west, and wins back North_Africa|y and Italy.|g'),
 (21.57, 27.37, 'But in 541,|y a terrible plague|r sweeps across the empire, and kills millions.|r'),
 (27.77, 33.63, 'Far to the south, in Arabia,|y a merchant named Muhammad|g begins preaching a new religion:|y Islam.|g'),
 (34.03, 40.76, 'By his death in 632,|y most of Arabia is united.|g Then the Arab armies|g burst out of the desert.|y'),
 (41.16, 46.88, 'In just twenty_years,|y they destroy the Sasanian_Empire,|r and take Syria|y and Egypt|y from the Romans.'),
 (47.28, 51.42, 'In the east, the Arabs reach the Indus_River,|c and the edge of Central_Asia.|y'),
 (51.82, 57.84, 'In 711,|y the general Tariq|g crosses the sea into Spain,|y and the Visigoth kingdom|r collapses.|r'),
 (58.24, 64.09, 'But in 732,|y near Tours in France,|c the Frankish leader Charles_Martel|c stops their advance.|r'),
 (64.49, 72.38, 'Then, in 750,|y the Abbasids|c overthrow the ruling Umayyad|g family. One Umayyad_prince|g escapes, all the way to Spain.|y'),
 (72.78, 79.98, 'Meanwhile, China is reunited under the Tang_dynasty:|y a golden_age|y of poetry, art, and trade on the Silk_Road.|y'),
 (80.38, 86.50, 'Next time:|y the year 1000,|y when Vikings|c sail all the way to America.|r Follow the series!|y'),
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
