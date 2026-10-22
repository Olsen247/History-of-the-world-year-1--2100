"""usage: python3 mkaudio.py epNN_v3 vo_dir out_fx.wav seed"""
import sys, subprocess, importlib
mod, vo, out, seed = sys.argv[1:5]
sys.argv = ["x"]; M = importlib.import_module(mod)
rv = sorted((round(r["t0"], 2), round(r["t1"], 2)) for r in M.CFG["reveals"])
keep = []
for a, b in rv:
    if not keep or a > keep[-1][1] + 0.5: keep.append((a, b))
fires = [round(e["t0"], 2) for e in M.CFG["fx"] if e["type"] == "icon" and e.get("icon") == "fire"]
tmp = out.replace(".wav", "_vo.wav")
subprocess.run(["python3", "audio_gen.py", vo, tmp, str(M.DUR), seed, repr(keep[:8]), repr(fires)], check=True)
subprocess.run(["python3", "fx_audio.py", mod, tmp, out], check=True)
print("audio", M.DUR, keep[:8], fires)
