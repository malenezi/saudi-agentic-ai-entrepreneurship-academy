# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Step 1. Put what the pages and the sound mix need into build/: the logo, the fonts and the music bed.

    SAAEA_FONTS=/path/to/woff2/files python3 prepare.py

The logo is cut from the Academy's banner. The music is a calm pad written here as numbers, so there
is no recording to license. Fonts are not in the repository: point SAAEA_FONTS at a folder holding the
IBM Plex Sans Arabic and IBM Plex Sans .woff2 files (weights 400 to 700) from the @fontsource packages.
"""
import glob, os, shutil, subprocess
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, 'build')
os.makedirs(OUT, exist_ok=True)


def logo():
    im = Image.open(os.path.join(ROOT, 'assets', 'brand', 'saaea-banner.jpg')).convert('RGB')
    c = im.crop((396, 26, 668, 160))
    c = c.resize((c.width * 3, c.height * 3), Image.LANCZOS)
    m = Image.new('L', c.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((36, 36, c.width - 36, c.height - 36), radius=90, fill=255)
    c.putalpha(m.filter(ImageFilter.GaussianBlur(26)))  # soft edge, so the cut-out sits on the end card
    c.save(os.path.join(OUT, 'logo.png'))


def fonts():
    src = os.environ.get('SAAEA_FONTS', '')
    found = [p for w in (400, 500, 600, 700) for p in glob.glob(os.path.join(src, f'ibm-plex-sans*-{w}-normal.woff2'))
             if '-arabic-arabic-' in p or 'ibm-plex-sans-latin-' in os.path.basename(p)]
    for p in found:
        shutil.copy(p, OUT)
    print(len(found), 'font files copied (8 expected)')


def music(seconds=124, sr=48000):
    t = np.arange(int(sr * seconds)) / sr
    rng = np.random.default_rng(7)
    hz = lambda n: 440 * 2 ** ((n - 69) / 12)

    def note(f, t0, dur, amp):
        x = np.zeros_like(t)
        i0, i1 = int(t0 * sr), min(len(t), int((t0 + dur) * sr))
        tt = t[i0:i1] - t0
        env = np.sin(np.clip(tt / 3.0, 0, 1) * np.clip((dur - tt) / 3.5, 0, 1) * np.pi / 2) ** 2
        s = np.zeros_like(tt)
        for det in (-0.35, 0, 0.4):
            ff = f * (1 + det / 100)
            s += (np.sin(2 * np.pi * ff * tt + rng.uniform(0, 6.28)) + 0.28 * np.sin(2 * np.pi * 2 * ff * tt + rng.uniform(0, 6.28))
                  + 0.07 * np.sin(2 * np.pi * 3 * ff * tt))
        x[i0:i1] = amp * env * s / 3
        return x

    # Dmaj9, Bm7, Gmaj7, Asus4: eight seconds each, overlapping, with one soft bell per chord
    chords = [[38, 50, 57, 61, 64, 66], [35, 47, 54, 57, 62, 66], [31, 43, 50, 54, 59, 62], [33, 45, 52, 57, 62, 64]]
    L, R, k, t0 = np.zeros_like(t), np.zeros_like(t), 0, 0
    while t0 < seconds:
        for j, n in enumerate(chords[k % 4]):
            y = note(hz(n), t0, 10.5, 0.5 if j < 2 else 0.32)
            pan = 0.5 + 0.28 * np.sin(j * 1.7 + k)
            L += y * (1 - pan)
            R += y * pan
        tb = t0 + 2 + (k % 2) * 2.5
        i0 = int(tb * sr)
        tt = t[i0:] - tb
        bell = 0.10 * np.exp(-tt / 2.2) * np.sin(2 * np.pi * hz(chords[k % 4][3 + (k % 3)] + 12) * tt)
        L[i0:] += bell * 0.6
        R[i0:] += bell * 0.4
        t0 += 8
        k += 1
    m = np.stack([L, R], 1)
    dry = os.path.join(OUT, 'music_dry.wav')
    sf.write(dry, (m / np.abs(m).max() * 0.7).astype('float32'), sr)
    subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-i', dry, '-af',
                           'lowpass=f=2600,aecho=0.8:0.7:90|180|310:0.35|0.25|0.18,aecho=0.8:0.6:520|830:0.25|0.18,highpass=f=60,loudnorm=I=-20:TP=-3',
                           '-ar', '48000', os.path.join(OUT, 'music.wav')])


if __name__ == '__main__':
    logo()
    fonts()
    music()
    print('build/ is ready')
