import pickle, regions2 as R
import world_data_1000 as A, world_data_1279 as B, world_data_1100 as C1, world_data_1190 as C2, world_data_1227 as M1, world_data_1259 as M2
regs = {}
def grp(a, b, specs):
    R._mc.clear(); R.build(a, b, specs, None, merge=regs)
MG = (95, 85, 70)
grp(A, C1, [dict(key="normans", empire="ANGLO-NORMAN REALM", origin=(0.57, 50.91), color=(220, 180, 70), src="C1", clip=[(-7, 49.9), (2.5, 49.9), (2.5, 56), (-7, 56)]),
            dict(key="crusade", empire="CRUSADER STATES", origin=(36.2, 36.2), color=(235, 235, 240), src="C1")])
grp(A, C1, [dict(key="cfall", empire="CRUSADER STATES", origin=(35.22, 31.78), color=(235, 235, 240), src="C1", mode="retreat")])
grp(A, C2, [dict(key="ayyubid", empire="AYYUBID SULTANATE", origin=(31.24, 30.05), color=(200, 170, 70), src="C2")])
grp(C2, M1, [dict(key="mongolia", empire="MONGOL EMPIRE", origin=(110.5, 48.5), color=MG, src="M1", clip=[(86, 41.5), (126, 41.5), (126, 55), (86, 55)]),
             dict(key="m_east", empire="MONGOL EMPIRE", origin=(106, 41.5), color=MG, src="M1", clip=[(94, 20), (140, 20), (140, 56), (94, 56)]),
             dict(key="m_west", empire="MONGOL EMPIRE", origin=(88, 45), color=MG, src="M1")])
grp(M1, M2, [dict(key="horde", empire="MONGOL EMPIRE", origin=(52, 50), color=MG, src="M2", clip=[(20, 42.3), (80, 42.3), (80, 62), (20, 62)]),
             dict(key="ilkhan", empire="MONGOL EMPIRE", origin=(55, 35), color=MG, src="M2", clip=[(29, 20), (62, 20), (62, 42.3), (29, 42.3)])])
grp(M2, B, [dict(key="song", empire="YUAN DYNASTY", origin=(112.1, 32.0), color=MG, src="B", clip=[(103, 18), (123, 18), (123, 34.6), (103, 34.6)])])
pickle.dump(regs, open("/home/claude/shortgen/regions_ep07_hd.pkl", "wb")); print(list(regs))
