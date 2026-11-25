# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Step 2. Speak each sentence, join the voice track, and write the cue timeline of each video.

    SAAEA_VOICE=/path/voice.onnx python3 audio.py [v1 v2 ...]

LENGTH (default 0.6) sets the speaking rate. Speech synthesis is not repeatable to the sample, so the
picture must be filmed again after every run of this step.
"""
import sys, re, json, os, unicodedata
import numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, 'build')
from tts import load, say
from content import VIDEOS

LENGTH = float(os.environ.get('LENGTH', '0.6'))
GAP_UNIT, GAP_SCENE, LEAD = 0.22, 0.5, 0.4
only = sys.argv[1:]
v = load()
os.makedirs(OUT, exist_ok=True)


def letters(s):
    return sum(1 for ch in s if unicodedata.category(ch)[0] == 'L')


def trim(a, sr, thr=0.012):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0:
        return a
    return a[max(0, idx[0] - int(0.02 * sr)): min(len(a), idx[-1] + int(0.06 * sr))]


for V in VIDEOS:
    if only and V['id'] not in only:
        continue
    t = LEAD
    track, sr, scenes = [np.zeros(int(LEAD * 22050), 'float32')], 22050, []
    for si, S in enumerate(V['scenes']):
        cues, start = {}, t - (LEAD if si == 0 else GAP_SCENE * 0.75)
        for ui, U in enumerate(S['units']):
            parts = re.split(r'\[(\w+)\]', U)
            plain = ''.join(parts[0::2])
            a, sr = say(v, plain, length=LENGTH)
            a = trim(a, sr)
            dur = len(a) / sr
            cues[f'u{ui}'] = t
            total, acc = letters(plain), 0
            for k in range(1, len(parts), 2):
                acc += letters(parts[k - 1])
                # a spoken phrase starts slightly before its proportional share; lead visuals a touch
                cues[parts[k]] = t + dur * acc / total - 0.12
            last = ui == len(S['units']) - 1
            gap = (S.get('tail', GAP_SCENE) if last else GAP_UNIT)
            track += [a, np.zeros(int(gap * sr), 'float32')]
            t += dur + gap
        end = t - (0 if si == len(V['scenes']) - 1 else GAP_SCENE * 0.75)
        scenes.append(dict(start=round(start, 3), end=round(end, 3), cues={k: round(x, 3) for k, x in cues.items()}))
    audio = np.concatenate(track)
    sf.write(os.path.join(OUT, V['id'] + "_voice.wav"), audio, sr)
    json.dump(dict(dur=round(len(audio) / sr, 3), scenes=scenes), open(os.path.join(OUT, V['id'] + "_tl.json"), 'w'), indent=1)
    print(V['id'], 'duration', round(len(audio) / sr, 1))
