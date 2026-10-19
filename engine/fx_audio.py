"""Add battle/icon sound effects on top of an existing episode mix."""
import sys, wave, importlib
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100
rng = np.random.default_rng(3)
def tt(d): return np.arange(int(d * SR)) / SR
def lp(x, f): return sosfilt(butter(2, f, "low", fs=SR, output="sos"), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)
def boom():
    x = tt(2.2)
    sub = np.sin(2 * np.pi * np.cumsum(32 + 70 * np.exp(-x * 9)) / SR) * np.exp(-x * 2.6)
    crack = lp(rng.standard_normal(len(x)), 2500) * np.exp(-x * 9)
    rumble = lp(rng.standard_normal(len(x)), 140) * np.exp(-x * 1.6) * 3
    clang = (np.sin(2 * np.pi * 1850 * x) + np.sin(2 * np.pi * 2630 * x)) * np.exp(-x * 14) * 0.25
    return sub * 1.1 + crack * 0.7 + rumble * 0.5 + np.roll(clang, int(0.2 * SR))
def march(d):
    out = np.zeros(int(d * SR)); step = 0.36; t = 0
    x = tt(0.18); thud = lp(rng.standard_normal(len(x)), 300) * np.exp(-x * 30) * 2.5
    while t < d - 0.2:
        i = int(t * SR); out[i:i + len(thud)] += thud[: len(out) - i] * (0.8 + 0.2 * rng.random())
        t += step
    x = tt(d); drum = np.zeros(len(x))
    for k in range(int(d / 0.72)):
        i = int(k * 0.72 * SR); y = tt(0.4); hit = np.sin(2 * np.pi * np.cumsum(70 + 60 * np.exp(-y * 20)) / SR) * np.exp(-y * 8)
        drum[i:i + len(hit)] += hit[: len(drum) - i]
    env = np.minimum(1, x / 0.4) * np.minimum(1, (d - x) / 0.4)
    return (out + drum * 0.8) * env
def pop():
    x = tt(0.5); return (np.sin(2 * np.pi * (500 + 900 * np.minimum(1, x / 0.08)) * x) * np.exp(-x * 16) +
                         0.5 * np.sin(2 * np.pi * 1568 * x) * np.exp(-x * 6))

def main(epmod, src, dst):
    cfg = importlib.import_module(epmod).CFG
    w = wave.open(src); ch = w.getnchannels(); n = w.getnframes()
    a = np.frombuffer(w.readframes(n), np.int16).astype(np.float32).reshape(-1, ch) / 32768; w.close()
    sfx = np.zeros(len(a))
    def add(sig, at, vol):
        i = int(at * SR); j = min(len(sfx), i + len(sig))
        if i < len(sfx): sfx[i:j] += sig[: j - i] * vol
    for ev in cfg.get("fx", []):
        if ev["type"] == "boom": add(boom(), ev["t0"], 0.55)
        elif ev["type"] == "march": add(march(ev["t1"] - ev["t0"] + 0.3), ev["t0"], 0.22)
        elif ev["type"] == "icon": add(pop(), ev["t0"], 0.18)
    mix = a + sfx[:, None]
    mix = np.tanh(mix * 1.05) * 0.97
    o = wave.open(dst, "wb"); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(SR)
    o.writeframes((mix.clip(-1, 1) * 32767).astype(np.int16).tobytes()); o.close(); print("sfx ok")

if __name__ == "__main__":
    main(*sys.argv[1:4])
