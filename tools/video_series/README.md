# Video series builder

Builds the four videos in [`assets/videos/`](../../assets/videos/README.md) from text: narration and on-screen content in `content.py`, one page template in `base.html`.

Unlike everything else in `tools/`, this folder needs packages and programs that are not in the standard library. It is not run by `make check` or by CI, and nothing else in the repository depends on it.

## What it needs

| Need | Used for |
|---|---|
| Python packages `piper-tts`, `numpy`, `soundfile`, `pillow`, `playwright` | Voice, sound, logo cut-out, filming |
| `ffmpeg` and Google Chrome (`SAAEA_CHROME` if it is not at `/usr/bin/google-chrome`) | Encoding and filming |
| A Piper Arabic voice (`.onnx` with its `.onnx.json`), path in `SAAEA_VOICE` | The published videos used `ar_JO-kareem-medium` |
| IBM Plex Sans Arabic and IBM Plex Sans `.woff2` files, folder in `SAAEA_FONTS` | From the `@fontsource` npm packages; SIL Open Font License |

None of these is stored in the repository.

## Steps

```bash
cd tools/video_series
SAAEA_FONTS=/path/to/fonts python3 prepare.py          # logo, fonts and music into build/
SAAEA_VOICE=/path/voice.onnx python3 audio.py v1       # voice track and cue timeline
python3 render.py stills v1                            # key frames and an overflow check: look at them first
python3 render.py film v1                              # one file per scene, about 150 ms a frame
python3 render.py mux v1                               # join, add voice and music: build/v1_final.mp4
```

`v1` to `v4` are the four videos. Everything is written to `build/`, which Git ignores.

## How a video is described

Each video in `content.py` is a list of scenes. A scene has the sentences to be spoken (`units`) and its HTML. The spoken text is fully vowelled, because the voice reads unvowelled Arabic badly, and English terms are spelled in Arabic letters. A marker such as `[a]` inside a sentence names the moment that word is spoken; an element with `data-at="a"` appears then. `u0`, `u1` and so on name the start of each sentence, and a plain number is seconds from the start of the scene.

The picture is timed from the voice, and speech synthesis does not give the same length twice. After any run of `audio.py`, film that video again.

## Limits

- Cue times inside a sentence are estimated from letter counts, not measured, so an element can lead or trail its word by a fraction of a second.
- The voice's pronunciation was checked by machine transcription only. Change a sentence, and listen to it.
- Tried on Linux with Chrome 1920 × 1080. Not tried on Windows or macOS.
