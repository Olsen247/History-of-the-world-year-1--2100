import pickle, sys, os, regions2 as R
import ep31_world as W31
# run one group per process (python3 regions_ep31.py 0|1|2) – several in one process can run out of memory
OUT = "/home/claude/shortgen/regions_ep31_hd.pkl"
G = int(sys.argv[1]) if len(sys.argv) > 1 else -1
regs = pickle.load(open(OUT, "rb")) if os.path.exists(OUT) and G > 0 else {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
COL = {n: c for n, d, c, *_ in W31.NEW_1957 + W31.NEW_1960}
COL.update({"SOUTH VIETNAM": (235, 200, 80), "MALAYA": (90, 120, 210), "KATANGA": (240, 150, 60)})
g = lambda key, emp, org, src: dict(key=key, empire=emp, origin=org, color=COL[emp], src=src)
# origins = capitals / where it started
O57 = [("nv_gain", "NORTH VIETNAM", (103.0, 21.4)), ("sv_gain", "SOUTH VIETNAM", (106.7, 10.8)), ("laos_gain", "LAOS", (102.6, 17.97)),
       ("camb_gain", "CAMBODIA", (104.9, 11.55)), ("sudan_gain", "SUDAN", (32.5, 15.6)), ("morocco_gain", "MOROCCO", (-6.8, 34.0)),
       ("tunisia_gain", "TUNISIA", (10.2, 36.8)), ("ghana_gain", "GHANA", (-0.2, 5.6)), ("malaya_gain", "MALAYA", (101.7, 3.1))]
O60 = [("guinea_gain", "GUINEA", (-13.7, 9.5)), ("cameroon_gain", "CAMEROON", (11.5, 3.9)), ("togo_gain", "TOGO", (1.2, 6.2)),
       ("madagascar_gain", "MADAGASCAR", (47.5, -18.9)), ("congo_gain", "CONGO", (15.3, -4.35)), ("somalia_gain", "SOMALIA", (45.3, 2.05)),
       ("dahomey_gain", "DAHOMEY", (2.6, 6.5)), ("niger_gain", "NIGER", (2.1, 13.5)), ("volta_gain", "UPPER VOLTA", (-1.5, 12.4)),
       ("ivory_gain", "IVORY COAST", (-4.0, 5.4)), ("chad_gain", "CHAD", (15.0, 12.1)), ("car_gain", "CENTRAL AFRICAN REPUBLIC", (18.6, 4.4)),
       ("brazza_gain", "CONGO-BRAZZAVILLE", (15.24, -4.2)), ("gabon_gain", "GABON", (9.45, 0.4)), ("senegal_gain", "SENEGAL", (-17.3, 14.7)),
       ("mali_gain", "MALI", (-8.0, 12.65)), ("nigeria_gain", "NIGERIA", (3.4, 6.5)), ("mauritania_gain", "MAURITANIA", (-15.9, 18.1)),
       ("cyprus_gain", "CYPRUS", (33.4, 35.2))]
if G in (-1, 0):
    import world_data_1953 as A, world_data_1957 as M
    grp(A, M, [g(k, e, o, "M") for k, e, o in O57])
if G in (-1, 1):
    import world_data_1957 as M, world_data_1960 as B
    grp(M, B, [g(k, e, o, "B") for k, e, o in O60])
if G in (-1, 2):
    import world_data_1960 as B, world_data_1960k as K
    grp(B, K, [g("katanga_gain", "KATANGA", (27.5, -11.7), "K")])
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
