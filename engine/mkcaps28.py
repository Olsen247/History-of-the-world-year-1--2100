import sys
SEG = [
 (0.30, 6.22, 'By 1942,|y Germany|r and_Japan|r ruled_more|y land_than|y ever.|c Then_the|y tide|g turned.|g'),
 (6.72, 7.92, ''),
 (8.17, 13.28, 'Japan|r storms_across|y Asia.|c At Singapore,|y 80,000|r Allied_troops|y surrender.|c'),
 (13.68, 19.08, 'Midway:|y codebreakers|c read_Japan\'s|y plan,|r and_dive|y bombers_sink|g four_carriers.|c'),
 (19.48, 25.55, 'In_the|y Atlantic,|c U-boat|r wolf_packs|y hunt_the|y convoys,|c while_Alan|y Turing\'s|g codebreakers|c attack_Enigma.|y'),
 (25.95, 32.04, 'At Stalingrad,|r they_fight|y house_by|y house.|c Chuikov\'s_men|y hug_the|g Germans,|y so_their|y bombers|r can\'t_hit_them.|c'),
 (32.44, 38.70, 'October,|y El_Alamein:|c almost_900|r guns_open|y fire,|r and_Montgomery|g drives|y Rommel_back.|c'),
 (39.10, 45.57, 'November:|y Soviet|r tanks_smash|y the_Romanian|c flanks|y and_trap|r nearly|y 300,000|r Axis_soldiers.|c'),
 (45.97, 54.45, 'January 1943:|y Paulus|r surrenders.|c Of_90,000|y prisoners,|c only_about|y 5,000|r come_home.|c'),
 (54.85, 63.26, 'April 1943:|y the_Warsaw|c Ghetto_rises.|g The_Nazis|y have_murdered|r millions_of|y Jews|c in_mass|y shootings|r and_death|y camps.|r'),
 (63.66, 70.85, 'May 1943:|y radar|c and_long-range|y planes_sink|g over_40|r U-boats|y in_a_single|y month.|c'),
 (71.25, 79.17, 'Kursk:|r forewarned,|y the_Soviets|c lay_vast|y minefields.|r Some_6,000|y tanks|r clash,|c and_the|y German_attack|y fails.|g'),
 (79.57, 87.30, 'Next time:|y Year 1945|r – D-Day,|c Berlin|r and_the|y atomic_bombs.|c Follow the series!|y'),
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
narr = ["NARRATION SCRIPT – History of the World, Episode 28: Year 1943", "(read along with the on-screen captions; times in seconds)", ""]
for a, b, txt in SEG:
    narr.append(f"[{a:05.1f}–{b:04.1f}]  " + " ".join(w.split("|")[0] for w in txt.split()).replace("_", " "))
open(sys.argv[2], "w").write("\n".join(narr) + "\n")
