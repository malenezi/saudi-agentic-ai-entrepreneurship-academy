# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Voice for the series: a Piper voice file, read through the piper-tts package.

Set SAAEA_VOICE to the path of the voice's .onnx file (its .onnx.json must sit beside it).
The published videos used ar_JO-kareem-medium. See README.md for where it comes from and its limits.
"""
import os

import numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig


def load():
    path = os.environ.get("SAAEA_VOICE")
    if not path or not os.path.exists(path):
        raise SystemExit("Set SAAEA_VOICE to the path of a Piper voice .onnx file")
    return PiperVoice.load(path)


def say(voice, text, length=1.0, noise=0.5, noise_w=0.7):
    """Samples (float32) and sample rate for one sentence. length below 1 speaks faster."""
    cfg = SynthesisConfig(length_scale=length, noise_scale=noise, noise_w_scale=noise_w)
    chunks = list(voice.synthesize(text, cfg))
    return np.concatenate([c.audio_float_array for c in chunks]).astype("float32"), chunks[0].sample_rate
