import sys
SEG = [
 (0.3, 4.99, 'To watch a planet|y cross the Sun,|c Britain sent one_small_ship|r to the far side|g of the world.'),
 (5.49, 6.69, ''),
 (6.94, 13.95, 'In 1644,|y rebels storm Beijing,|r the last Ming_emperor|y hangs himself, and the Manchu_Qing|g seize the capital.'),
 (14.35, 21.51, "In 1683,|y the Ottomans|r besiege Vienna,|y until Poland's King_Jan_Sobieski|c charges in with his winged_hussars.|p"),
 (21.91, 27.93, 'In 1709,|y Peter_the_Great|g crushes Sweden|c at Poltava,|y and Russia becomes a great_power.|r'),
 (28.33, 36.73, 'In 1722,|y Dutch explorer Jacob_Roggeveen|c reaches an island of giant_stone_statues|y on Easter_Sunday,|p and names it Easter_Island.|g'),
 (37.13, 43.51, "In 1739,|y Persia's Nader_Shah|c sacks Delhi,|r and carries off the jewelled Peacock_Throne.|y"),
 (43.91, 50.76, 'In 1741,|y Vitus_Bering,|c a Dane sailing for Russia,|g reaches Alaska,|y but dies|r on the way home.'),
 (51.16, 57.45, 'In 1757,|y Robert_Clive|c wins at Plassey,|y and the East_India_Company|r starts taking over Bengal.|g'),
 (57.85, 64.7, 'In 1759,|y Britain wins|r at Quebec,|c and both generals,|y Wolfe and Montcalm,|p die of their wounds.|r'),
 (65.1, 71.78, 'In 1769,|y James_Cook|c watches Venus|p cross the Sun|y from Tahiti,|g then sails right around New_Zealand.|g'),
 (72.18, 79.21, 'In 1770,|y Cook lands at Botany_Bay,|g almost sinks|r on the Great_Barrier_Reef,|c and claims the east_coast|y for Britain.'),
 (79.61, 85.94, 'Next time:|y 1776,|y when thirteen_colonies|c declare independence.|r Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 16: Year 1770", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
