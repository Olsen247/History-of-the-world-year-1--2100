"""Append a 'comment below' outro tail to a finished episode video.
usage: python3 make_tail.py in.mp4 out.mp4 vo.wav"""
import sys, subprocess, wave, numpy as np
sys.path.insert(0, "/home/claude/shortgen")
from PIL import Image
from hist_engine3 import glow_text, put, eback, pr, GOLD, WHITE
inp, out, vo = sys.argv[1:4]
D = "/home/claude/outro/tmp"; subprocess.run(["mkdir", "-p", D])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.05", "-i", inp, "-frames:v", "1", f"{D}/last.png"], check=True)
base = Image.open(f"{D}/last.png").convert("RGB")
w = wave.open(vo); vdur = w.getnframes() / w.getframerate(); w.close()
TD = round(vdur + 0.9, 2); FPS = 30
t1 = glow_text("TELL ME IN THE COMMENTS", 50, WHITE)
t2 = glow_text("WHAT'S MISSING?  WHAT COULD BE BETTER?", 34, GOLD)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", f"{D}/tail_v.mp4"], stdin=subprocess.PIPE)
for i in range(int(TD * FPS)):
    t = i / FPS; fr = base.copy()
    k = eback(pr(t, 0.05, 0.4), 2.2); put(fr, t1, 540, 1370, scale=max(0.01, k), alpha=min(1, k * 2))
    k2 = eback(pr(t, 0.6, 0.95), 2.2); put(fr, t2, 540, 1440, scale=max(0.01, k2), alpha=min(1, k2 * 2))
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
# audio: VO + soft pad + ping
SR = 44100; n = int(TD * SR); tt = np.arange(n) / SR
pad = sum(np.sin(2 * np.pi * f * tt) * a for f, a in ((110, .05), (164.8, .035), (220, .03), (261.6, .02)))
pad *= np.minimum(1, tt / 0.3) * np.clip((TD - tt) / 1.2, 0, 1)
ping = np.zeros(n); L = int(1.2 * SR); x = np.arange(L) / SR; ping[:L] = np.sin(2 * np.pi * 1046 * x) * np.exp(-x * 5) * 0.12
w = wave.open(vo); v = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32).reshape(-1, w.getnchannels()).mean(1) / 32768; w.close()
mix = pad + ping; i0 = int(0.15 * SR); mix[i0:i0 + len(v)] += v[: n - i0] * 1.0
mix = np.clip(mix, -1, 1); st = (np.stack([mix, mix], 1) * 32767).astype(np.int16)
w = wave.open(f"{D}/tail_a.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/tail_v.mp4", "-i", f"{D}/tail_a.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac",
                "-b:a", "192k", "-ar", "44100", "-shortest", f"{D}/tail_nocap.mp4"], check=True)
# captions for the new line, same style as the episodes
words = [("And tell me", 0.15), ("in the comments:|y", 0.85), ("what's missing,|r", 1.75), ("and what could", 2.55), ("be better?|y", 3.15)]
caps = [f"{a:.2f} {(words[j + 1][1] if j + 1 < len(words) else vdur + 0.25) - 0.03:.2f} {txt}" for j, (txt, a) in enumerate(words)]
open(f"{D}/tail_caps.txt", "w").write("\n".join(caps) + "\n")
subprocess.run(["python3", "/home/claude/shortgen/caption_burn.py", f"{D}/tail_nocap.mp4", f"{D}/tail_caps.txt", f"{D}/tail.mp4", "0.80"], check=True,
               cwd="/home/claude/shortgen")
# join: re-encode main + tail together
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", inp, "-i", f"{D}/tail.mp4", "-filter_complex",
                "[0:v]fps=30,format=yuv420p[v0];[1:v]fps=30,format=yuv420p[v1];[0:a]aresample=44100[a0];[1:a]aresample=44100[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-maxrate", "4500k", "-bufsize", "9000k",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print("ok", out)
