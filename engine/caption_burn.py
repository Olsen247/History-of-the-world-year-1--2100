"""Burn "viral Shorts"-style captions into any vertical video.

Style: 2-3 words at a time, bold white uppercase with dark edge + drop shadow,
key words in colour with a matching glow, quick pop-in.

Usage:  python3 caption_burn.py input.mp4 captions.txt output.mp4 [y_position 0-1]

captions.txt, one phrase per line:
    0.05 0.75 TESLA|r VS BYD|c
    start end words  (mark a word with |r |c |p |y |g for red/cyan/purple/yellow/green)
"""
import sys, json, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
COLORS = {"r": (255, 62, 74), "c": (64, 222, 255), "p": (186, 118, 255), "y": (255, 214, 36), "g": (60, 230, 120)}


def probe(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=width,height,r_frame_rate", "-of", "json", path])
    s = json.loads(out)["streams"][0]
    n, d = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d)


def parse(path):
    caps = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"): continue
        a, b, rest = line.split(" ", 2)
        words = []
        for w in rest.split():
            if "|" in w:
                t, c = w.rsplit("|", 1); words.append((t.upper().replace("_", " "), COLORS.get(c, (255, 255, 255))))
            else:
                words.append((w.upper().replace("_", " "), None))
        caps.append((float(a), float(b), words))
    return caps


def phrase_image(words, W):
    size = int(W * 0.078)
    while True:
        f = ImageFont.truetype(FONT, size)
        space = f.getlength(" ") * 0.9
        widths = [f.getlength(w) for w, _ in words]
        total = sum(widths) + space * (len(words) - 1)
        if total <= W * 0.88 or size < 30: break
        size -= 4
    asc, desc = f.getmetrics()
    pad = int(size * 0.6)
    w_img, h_img = int(total + 2 * pad), int(asc + desc + 2 * pad)
    full = Image.new("L", (w_img, h_img), 0)
    glow = Image.new("RGBA", (w_img, h_img), (0, 0, 0, 0))
    fill = Image.new("RGBA", (w_img, h_img), (0, 0, 0, 0))
    df, dfl = ImageDraw.Draw(full), ImageDraw.Draw(fill)
    stroke = max(3, size // 16)
    x = pad
    for (w, col), ww in zip(words, widths):
        df.text((x, pad), w, font=f, fill=255, stroke_width=stroke)
        m = Image.new("L", (w_img, h_img), 0)
        ImageDraw.Draw(m).text((x, pad), w, font=f, fill=255, stroke_width=stroke)
        gcol, ga, gr = (col, 235, size * 0.22) if col else ((255, 255, 255), 70, size * 0.12)
        m = m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(gr))
        layer = Image.new("RGBA", (w_img, h_img), gcol + (255,))
        layer.putalpha(m.point(lambda v: int(v * ga / 255)))
        glow.alpha_composite(layer)
        dfl.text((x, pad), w, font=f, fill=(col or (255, 255, 255)) + (255,),
                 stroke_width=stroke, stroke_fill=(12, 12, 16, 255))
        x += ww + space
    shadow_m = full.filter(ImageFilter.GaussianBlur(size * 0.06))
    shadow = Image.new("RGBA", (w_img, h_img), (0, 0, 0, 255))
    shadow.putalpha(shadow_m.point(lambda v: int(v * 0.85)))
    out = Image.new("RGBA", (w_img, h_img), (0, 0, 0, 0))
    out.alpha_composite(shadow, (0, int(size * 0.07)))
    out.alpha_composite(glow)
    out.alpha_composite(fill)
    return out


def ease_pop(x):
    x = max(0.0, min(1.0, x)); s = 2.2; c3 = s + 1
    return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2


def main():
    src, capf, dst = sys.argv[1:4]
    ypos = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
    W, H, fps = probe(src)
    caps = [(a, b, phrase_image(words, W)) for a, b, words in parse(capf)]
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps),
                            "-i", "-", "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "18",
                            "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", dst],
                           stdin=subprocess.PIPE)
    fsz = W * H * 3; i = 0
    while True:
        buf = dec.stdout.read(fsz)
        if len(buf) < fsz: break
        t = i / fps
        frame = Image.frombuffer("RGB", (W, H), buf, "raw", "RGB", 0, 1).copy()
        for a, b, img in caps:
            if a <= t < b:
                k = ease_pop((t - a) / 0.14)
                sc = 0.78 + 0.22 * k
                im = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BICUBIC) if abs(sc - 1) > 0.01 else img
                alpha = min(1.0, (t - a) / 0.05)
                if alpha < 1:
                    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
                frame.paste(im, (int(W / 2 - im.width / 2), int(H * ypos - im.height / 2)), im)
                break
        enc.stdin.write(frame.tobytes()); i += 1
    enc.stdin.close(); enc.wait(); dec.wait()
    print("done", i, "frames")


if __name__ == "__main__":
    main()
