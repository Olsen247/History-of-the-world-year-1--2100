"""Re-cut an episode with the new opening (hook line + silent rewind).
usage: TEMPO=1.13 python3 rework.py NN old_cfg.py old_mkcaps.py new_vo_dir "id_hook,SILENT1.2,WAV:...|id,..." "hook caption text with |y markers"
Writes: <new_vo_dir>/spans.txt, epNN_v3.py, mkcapsNN_v3.py"""
import sys, subprocess, os, re
NN, cfg, caps, vo, ids, hook = sys.argv[1:7]
os.makedirs(vo, exist_ok=True)
subprocess.run(["python3", "mkvo.py", vo, ids], check=True)
S = eval(open(f"{vo}/spans.txt").read())
src = open(caps).read(); i = src.index("SEG = ["); j = src.index("]\n", i) + 2
ns = {}; exec(src[i:j], ns); SEG = ns["SEG"]
assert len(SEG) == len(S) == 13, (len(SEG), len(S))
NEW = [(S[0][0], S[0][1], hook), (S[1][0], S[1][1], "")] + [(S[k][0], S[k][1], SEG[k][2]) for k in range(2, 13)]
body = "SEG = [\n" + "".join(f" {t!r},\n" for t in NEW) + "]\n"
open(f"mkcaps{int(NN)}_v3.py", "w").write(src[:i] + body + src[j:])
c = open(cfg).read()
c = re.sub(r'open\("/home/claude/shortgen/[^"]+/spans.txt"\)', f'open("/home/claude/shortgen/{os.path.basename(vo)}/spans.txt")', c)
c = c.replace("dict(t0=1.2, t1=en[0]", "dict(t0=0.15, t1=en[0]").replace("flashes=[(1.2, 0.35)", "flashes=[(0.15, 0.35)")
assert "t0=0.15, t1=en[0]" in c
open(f"ep{NN}_v3.py", "w").write(c)
print("ok", S[-1][1])
