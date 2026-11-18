import pickle, sys, os, regions2 as R
import geo
# run one group per process (python3 regions_ep29.py 0|1|2|3|4) – several in one process can run out of memory
OUT = "/home/claude/shortgen/regions_ep29_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
import world_data_1943 as A, world_data_1944 as P, world_data_1945 as B
GER = (110, 110, 122); SOV = (130, 175, 95); JAP = (235, 95, 70); USC = (150, 190, 250)
sh = lambda key, emp, org, col=GER: dict(key=key, empire=emp, origin=org, color=col, mode="shatter")
if G in (-1, 0): grp(P, A, [sh("france_loss", "OCCUPIED FRANCE", (-0.8, 49.3)), sh("belgium_loss", "OCCUPIED BELGIUM", (3.0, 50.8)),
                           sh("lux_loss", "OCCUPIED LUXEMBOURG", (5.9, 49.6)), sh("east_loss", "GERMAN-OCCUPIED USSR", (30.0, 55.0))])
if G in (-1, 1): grp(A, P, [dict(key="pl_gain", empire="SOVIET-HELD POLAND", origin=(23.6, 52.0), color=SOV, src="G")])
if G in (-1, 2): grp(B, P, [sh("ger_loss", "GERMANY", (13.4, 52.5)), sh("nl_loss", "OCCUPIED NETHERLANDS", (5.5, 52.5)),
                           sh("dk_loss", "OCCUPIED DENMARK", (9.5, 56.0)), sh("no_loss", "OCCUPIED NORWAY", (10.7, 59.9)),
                           sh("bm_loss", "BOHEMIA-MORAVIA", (14.4, 50.1)), sh("gpl_loss", "GERMAN-OCCUPIED POLAND", (21.0, 52.2)),
                           sh("kur_loss", "GERMAN-HELD COURLAND", (22.0, 57.0)), sh("it_loss", "GERMAN-OCCUPIED ITALY", (11.0, 44.3)),
                           sh("yu_loss", "OCCUPIED YUGOSLAVIA", (18.4, 44.0))])
if G in (-1, 3): grp(B, P, [sh("man_loss", "MANCHUKUO", (127.0, 46.0), JAP), sh("jc_loss", "JAPANESE CONQUESTS", (112.0, 2.0), JAP),
                           sh("jchina_loss", "JAPANESE-OCCUPIED CHINA", (116.0, 34.0), JAP)])
if G in (-1, 4): grp(P, B, [dict(key="korea_n", empire="SOVIET-OCCUPIED KOREA", origin=(129.5, 42.5), color=SOV, src="B"),
                           dict(key="korea_s", empire="US-OCCUPIED KOREA", origin=(129.0, 35.1), color=USC, src="B")])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
