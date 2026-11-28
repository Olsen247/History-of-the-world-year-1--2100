import pickle, regions2 as R
import world_data_1975a as M, world_data_1975 as B
# North Vietnam's colour spreads south from the DMZ over the South (March-April 1975)
OUT = "/home/claude/shortgen/regions_ep33_hd.pkl"
regs = {}
R.build(M, B, [dict(key="nv_gain", empire="NORTH VIETNAM", origin=(106.9, 17.0), color=(230, 125, 60), src="B")], None, merge=regs)
pickle.dump(regs, open(OUT, "wb")); print(list(regs))
