import sys
SEG = [
 (0.3, 4.44, 'Less_than|y 66_years|r after_the|y first|y airplane,|c humans|y walked_on|y the_Moon.|g'),
 (4.94, 6.14, ''),
 (6.39, 12.22, 'April_1961:|y Yuri_Gagarin|r becomes|y the_first|g human|y in_space.|c'),
 (12.62, 17.04, 'That_August,|y East_Germany|r seals_off|y West_Berlin|c overnight|y with|y barbed_wire.|r'),
 (17.44, 26.49, 'October_1962:|y Soviet|r nuclear|r missiles|y are_found|y in_Cuba.|c After|y thirteen|g days|y on_the|y brink,|r Khrushchev|r agrees|y to_remove|y them.|g'),
 (26.89, 34.7, '1963:|y Valentina|p Tereshkova|p becomes|y the_first|g woman|y in_space,|c and_Kennedy|c is_shot|r in_Dallas.|y'),
 (35.1, 41.95, '1964:|y after_the|y Gulf_of|c Tonkin|c incident,|y Congress|y gives|y Johnson|c a_free|g hand|y in_Vietnam.|r'),
 (42.35, 49.83, 'March_1965:|y American|c jets|y start|y bombing|r North|y Vietnam,|y and_Marines|c land_at|y Da_Nang.|g'),
 (50.23, 57.61, '1966:|y Mao|r unleashes|y the_Cultural|r Revolution.|r Millions_of|y Red_Guards|r attack|y anything|y old.|g'),
 (58.01, 64.08, 'August_1968:|y Soviet-led|r tanks|y crush|r the_Prague|c Spring|g in|y Czechoslovakia.|c'),
 (64.48, 70.51, 'By_the_end|y of_1968,|y over|y 530,000|r Americans|c are_fighting|y in_Vietnam.|g'),
 (70.91, 80.61, 'July_1969:|y Neil_Armstrong|c steps_onto|y the_Moon.|g One_small|y step|g for_man,|y one_giant|y leap|g for_mankind.|c'),
 (81.01, 87.24, 'Next time:|y 1975,|r the_fall|y of_Saigon.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 32: Year 1969", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
