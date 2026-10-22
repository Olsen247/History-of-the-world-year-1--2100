"""Cut a short "quick fact" clip (15-30 s) out of a finished episode and add an end card pointing to the full episode.
usage: python3 make_clip.py episode_final.mp4 START END EPISODE_NO out.mp4
START/END in seconds (use the spans of one or two narration lines; start ~0.2 s before the line, end ~0.4 s after)."""
import sys, subprocess, numpy as np, wave
sys.path.insert(0, "/home/claude/shortgen")
from PIL import Image
from hist_engine3 import glow_text, put, eback, pr, GOLD, WHITE
inp, a, b, ep, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
D = "/home/claude/outro/clip_tmp"; subprocess.run(["mkdir", "-p", D])
L = b - a
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-i", inp, "-t", str(L), "-vf", "fps=30,format=yuv420p",
                "-af", f"afade=t=in:d=0.25,afade=t=out:st={L - 0.4}:d=0.4,aresample=44100", "-c:v", "libx264", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", f"{D}/body.mp4"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.05", "-i", f"{D}/body.mp4", "-frames:v", "1", f"{D}/last.png"], check=True)
base = Image.open(f"{D}/last.png").convert("RGB")
dim = Image.new("RGB", base.size, (2, 6, 14))
T = 2.6; FPS = 30
t1 = glow_text("FULL STORY", 56, WHITE); t2 = glow_text("HISTORY OF THE WORLD", 64, GOLD); t3 = glow_text(f"EPISODE {ep}", 92, GOLD)
t4 = glow_text("FOLLOW FOR THE WHOLE SERIES", 40, WHITE)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{base.width}x{base.height}", "-r", str(FPS),
                      "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", f"{D}/card_v.mp4"], stdin=subprocess.PIPE)
for i in range(int(T * FPS)):
    t = i / FPS; fr = Image.blend(base, dim, 0.93 * pr(t, 0, 0.35))
    k = eback(pr(t, 0.1, 0.45), 2.2); put(fr, t1, 540, 720, scale=max(.01, k), alpha=min(1, k * 2))
    k = eback(pr(t, 0.3, 0.65), 2.2); put(fr, t2, 540, 830, scale=max(.01, k), alpha=min(1, k * 2))
    k = eback(pr(t, 0.5, 0.85), 2.4); put(fr, t3, 540, 960, scale=max(.01, k), alpha=min(1, k * 2))
    put(fr, t4, 540, 1240, alpha=pr(t, 1.0, 1.3))
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
SR = 44100; n = int(T * SR); tt = np.arange(n) / SR
pad = sum(np.sin(2 * np.pi * f * tt) * v for f, v in ((110, .05), (164.8, .035), (220, .03))) * np.minimum(1, tt / .2) * np.clip((T - tt) / .8, 0, 1)
x = np.arange(int(SR * 1.2)) / SR; pad[:len(x)] += np.sin(2 * np.pi * 1046 * x) * np.exp(-x * 5) * .12
st = (np.stack([pad, pad], 1).clip(-1, 1) * 32767).astype(np.int16)
w = wave.open(f"{D}/card_a.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/card_v.mp4", "-i", f"{D}/card_a.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-shortest", f"{D}/card.mp4"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/body.mp4", "-i", f"{D}/card.mp4", "-filter_complex",
                "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow",
                "-crf", "20", "-maxrate", "4500k", "-bufsize", "9000k", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print("ok", out)
