import sys
SEG = [
 (0.3, 5.56, 'A 21-year-old_sultan|r is about to end an empire|y that has lasted for more than a thousand_years.|y'),
 (6.06, 7.26, ''),
 (7.51, 12.72, 'In 1410,|y Poland and Lithuania|g crush the Teutonic_Knights|r at Grunwald.|y'),
 (13.12, 18.35, 'In 1415,|y King Henry_the_Fifth|r of England defeats the French|c at Agincourt.|y'),
 (18.75, 23.55, 'That same year, Portugal|g captures Ceuta|y in North Africa, and begins exploring the ocean.|c'),
 (23.95, 30.57, "In 1421,|y the Yongle_Emperor|r moves China's capital to Beijing,|y and his new Forbidden_City.|y"),
 (30.97, 37.0, 'In 1429,|y a teenage girl, Joan_of_Arc,|c leads the French to victory at Orleans.|y'),
 (37.4, 44.52, "In 1433,|y Zheng_He's|y treasure fleet sails home for the last_time,|r and China turns away from the sea.|c"),
 (44.92, 51.93, 'In 1438,|y Pachacuti|y becomes ruler of the Inca,|r and starts building a mighty_empire|y in the Andes.'),
 (52.33, 59.3, 'In 1444,|y the Ottomans|r crush a crusade at Varna,|y and the young king of Poland and Hungary is killed.|r'),
 (59.7, 65.89, 'Around 1450,|y in Mainz, Johannes_Gutenberg|c builds a printing_press|y that will change the world.|g'),
 (66.29, 75.72, 'In 1453,|y after a 53-day siege,|r Mehmed breaks through the walls.|r Constantinople_falls,|y and the Byzantine_Empire|p is gone.|r'),
 (76.12, 82.8, 'Next time:|y the year 1492,|y when Columbus|c sails west across the Atlantic. Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 10: Year 1453", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
