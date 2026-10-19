"""Original cinematic/military music bed + sound design for Country File #1."""
import wave
import numpy as np
from scipy.signal import butter, sosfilt

SR = 44100; import sys as _s; VO = _s.argv[1]; OUT = _s.argv[2]; DUR = float(_s.argv[3]); N = int(DUR * SR)
rng = np.random.default_rng(int(_s.argv[4]))
STATS = []; T_OUT = 39.4
music = np.zeros(N); sfx = np.zeros(N)

def tt(d): return np.arange(int(d * SR)) / SR
def add(buf, sig, at, vol=1.0):
    i = int(at * SR)
    if i >= N or i < 0: return
    j = min(N, i + len(sig)); buf[i:j] += sig[: j - i] * vol
def lp(x, f, o=2): return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "high", fs=SR, output="sos"), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)
def saw(f, d): x = tt(d); return 2 * ((x * f) % 1) - 1

BPM = 92; B = 60 / BPM
x = tt(0.6); TOM = np.sin(2 * np.pi * np.cumsum(70 + 60 * np.exp(-x * 20)) / SR) * np.exp(-x * 6)
x = tt(0.3); SNARE = (bp(rng.standard_normal(len(x)), 1200, 5000) * 1.5 + np.sin(2 * np.pi * 190 * x) * 0.6) * np.exp(-x * 16)
x = tt(0.05); HAT = hp(rng.standard_normal(len(x)), 7000) * np.exp(-x * 80)
roots = [34.65, 29.14, 30.87, 25.96]  # D D C E (low, ominous)

t = 1.9; b = 0
while t < DUR - 0.2:
    bb = b % 8
    if bb in (0, 3, 6): add(music, TOM, t, 0.9)
    if bb in (2, 6) and t > 3.6: add(music, SNARE, t, 0.38)
    if t > 3.6:
        add(music, HAT, t + B / 2, 0.12)
        add(music, HAT, t + B / 4, 0.05); add(music, HAT, t + 3 * B / 4, 0.05)
    if bb == 0:
        f = roots[(b // 8) % 4]
        L = B * 8
        bass = lp(saw(f, L) + 0.6 * saw(f * 1.006, L), 260)
        env = np.minimum(1, tt(L) * 8) * (0.7 + 0.3 * np.exp(-tt(L) * 1.5))
        add(music, bass * env, t, 0.4)
        # string-like stab (fifths)
        for ff in (f * 4, f * 6, f * 8):
            st = lp(saw(ff, B * 2) + saw(ff * 1.004, B * 2), 1400) * np.exp(-tt(B * 2) * 1.8)
            add(music, st, t, 0.045)
    # 16th ostinato pulse
    if t > 3.6:
        for q in range(4):
            f = roots[(b // 8) % 4] * 8
            p = lp(saw(f, B / 4), 1600) * np.exp(-tt(B / 4) * 20)
            add(music, p, t + q * B / 4, 0.05)
    b += 1; t += B

def whoosh(d=0.5, lo=300, hi=3000):
    x = tt(d); return bp(rng.standard_normal(len(x)), lo, hi) * np.sin(np.pi * x / d) ** 2 * 1.6
def impact(big=1.0):
    x = tt(1.4)
    sub = np.sin(2 * np.pi * np.cumsum(28 + 80 * np.exp(-x * 10)) / SR) * np.exp(-x * 3)
    crack = lp(rng.standard_normal(len(x)), 3500) * np.exp(-x * 14)
    return (sub * 1.3 + crack * 0.6) * big
def riser(d=0.8):
    x = tt(d); n = rng.standard_normal(len(x)); out = np.zeros(len(x)); seg = len(x) // 16
    for k in range(16):
        lo = 300 + 3500 * k / 16; out[k * seg:(k + 1) * seg] = bp(n[k * seg:(k + 1) * seg], lo, lo * 2)
    return out * (x / d) ** 2
def tick(): x = tt(0.025); return np.sin(2 * np.pi * 2200 * x) * np.exp(-x * 180)
def ping(f=1200):
    x = tt(0.6); return (np.sin(2 * np.pi * f * x) + 0.4 * np.sin(2 * np.pi * f * 2.01 * x)) * np.exp(-x * 7)
def jet():
    x = tt(2.2); n = rng.standard_normal(len(x))
    f = np.linspace(400, 2500, len(x))
    out = np.zeros(len(x)); seg = len(x) // 20
    for k in range(20): out[k * seg:(k + 1) * seg] = bp(n[k * seg:(k + 1) * seg], f[k * seg] * 0.6, f[k * seg] * 1.4)
    return out * np.sin(np.pi * x / 2.2) ** 2 * 1.4


x = tt(1.9); add(music, lp(saw(36.71, 1.9) + saw(36.9, 1.9), 260) * np.minimum(1, x * 1.5), 0.0, 0.4)
for k in range(14): add(sfx, tick(), 0.2 + k * 0.12, 0.2)
add(sfx, riser(0.6), 0.6, 0.4)
add(sfx, impact(1.4), 1.2, 1.0)
S = eval(open(f"/home/claude/shortgen/{VO}/spans.txt").read()); s = [x for x, y in S]; en = [y for x, y in S]
x = tt(1.3); f = np.linspace(1400, 200, len(x))
add(sfx, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / 1.3) * 0.35, s[1], 0.5)
for k in range(18): add(sfx, tick(), s[1] + k * 0.07, 0.18)
LS = len(s) - 1
for i in range(2, LS): add(sfx, whoosh(1.2, 150, 2200), s[i] - 0.9, 0.5); add(sfx, impact(0.4), s[i] + 0.3, 0.4); add(sfx, ping(1046), s[i] + 0.35, 0.1)
for (a0, a1) in eval(_s.argv[5]):
    L = a1 - a0; x = tt(L)
    rum = lp(rng.standard_normal(len(x)), 180) * 3.0 + lp(saw(55, L), 300) * 0.4
    add(sfx, rum * np.sin(np.pi * x / L) ** 0.7, a0, 0.35)
    add(sfx, riser(L) * 0.5, a0, 0.25)
    add(sfx, impact(0.6), a1, 0.45)
def fire(d=3.0):
    x = tt(d); n = rng.standard_normal(len(x))
    crackle = np.zeros(len(x)); idx = rng.integers(0, len(x) - 400, int(d * 40))
    for i0 in idx: crackle[i0:i0 + 300] += rng.standard_normal(300) * np.exp(-np.arange(300) / 40)
    roar = lp(n, 500) * 2.5
    return (roar + hp(crackle, 2000) * 0.5) * np.sin(np.pi * x / d) ** 0.5
for ft in eval(_s.argv[6]): add(sfx, fire(3.5), ft, 0.45)
add(sfx, riser(1.0), s[LS] - 0.7, 0.45); add(sfx, impact(1.1), s[LS] + 0.3, 0.9)
duck = np.ones(N)
for te in [1.2, s[LS] + 0.3]:
    i = int(te * SR); L = int(0.35 * SR); duck[i:i + L] *= np.linspace(0.4, 1, min(L, N - i))
mix = music * 0.6 * duck + sfx * 0.85
f = int(0.4 * SR); mix[-f:] *= np.linspace(1, 0, f)
mix = np.tanh(mix / (np.max(np.abs(mix)) + 1e-9) * 1.6) * 0.89
# voice
vo = np.zeros(N)
import wave as _w
for i, (a0, a1) in enumerate(S):
    w = _w.open(f"/home/claude/shortgen/{VO}/f{i + 1}.wav"); v = np.frombuffer(w.readframes(w.getnframes()), np.int16) / 32768.0
    add(vo, v, a0, 1.0)
vo = vo / (np.max(np.abs(vo)) + 1e-9) * 0.95
env = np.convolve(np.abs(vo), np.ones(4410) / 4410, "same"); env = np.clip(env / (env.max() + 1e-9) * 4, 0, 1)
out = mix * 0.42 * (1 - 0.62 * env) + vo
out = np.tanh(out * 1.1) * 0.95
st = np.stack([out, out], axis=1)
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print("audio ok")
