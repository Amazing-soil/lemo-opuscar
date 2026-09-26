# Technique: how the films are built

Every film in this library is made from code: no video generation, no stock footage. This page explains the pipeline, so you can reproduce it with our tools in `core/` or rebuild it in your own stack. Pair it with [`DIRECTOR.md`](DIRECTOR.md) and one `styles/<slug>/STYLE.md`. 中文版：[docs/zh-CN/TECHNIQUE.md](docs/zh-CN/TECHNIQUE.md)

```
timeline (single source of truth)
   ├─► picture:  web page with render(t) ──► headless Chrome, frame by frame ──► video.mp4
   ├─► voice:    TTS per line ──► speech-to-text check ──► word timings
   ├─► music:    score from the same timeline (samples + synthesis) ──► stems
   ├─► sound:    procedural foley at event times
   └─► subtitles: .srt + burned-in captions
mix (duck, compress, balance) ──► mux with ffmpeg, two-pass loudnorm −14 LUFS ──► film.mp4
```

## 1. Requirements

| Tool | Used for |
|---|---|
| Node 20+ and Google Chrome | page rendering (`npm install` pulls `playwright-core` and `three`) |
| ffmpeg | encoding, muxing, loudness, black-frame checks |
| Python 3.11+ (we use [uv](https://docs.astral.sh/uv/)) | `uv venv && uv pip install -r requirements.txt` (numpy, scipy, soundfile, soxr, librosa, pillow, kokoro-onnx, faster-whisper) |

Large assets are not in git. Fetch them when a step needs them:

```sh
sh tools/fetch.sh voice          # Kokoro TTS model (~340 MB) → core/tts/
sh tools/fetch.sh instruments    # CC0 / CC BY sample libraries (~1.35 GB) → core/audio/instruments/
sh tools/fetch.sh hdri           # Poly Haven HDRIs for 3D styles → core/assets/polyhaven/
sh tools/fetch.sh demo <slug>    # fonts, music and other inputs to rebuild one of our demos
```

## 2. The picture is a function of time

Each film is a static web page that exposes:

```js
window.DUR = 54.2;                 // seconds
window.render = (t) => { ... };    // draw the frame at time t, deterministic
window.READY = true;               // set once fonts and images are loaded
window.EV = [{t, type, ...}];      // optional: sound / cue events for the mixer
```

Rules that keep it reliable:

- **Deterministic.** No `Date.now()`, no `Math.random()` without a seed (`core/lib.js` has `mulberry` and `hash`), no state carried from the previous frame. Any frame can be rendered alone, in any order, by any worker.
- **Canvas 2D** covers most 2D styles; **three.js** for 3D (`core/three/post.js`: physical depth of field, GTAO, bloom, colour grade, 2× supersampling); **WebGL2** shaders for post passes (film damage, CRT, ink redraw).
- **Animate on twos where the style wants it** (12 fps stepping for stop-motion, pixel or cel looks), but keep the camera and light smooth every frame. A stepped camera reads as lag.
- **One world → screen function.** Any effect that follows a subject (iris, zoom, spotlight) goes through it. Never hand-type screen coordinates.

Capture (`core/render/`):

```sh
node core/render/still.mjs <demo> 1.5 12 --range 0:50:2   # review stills; exits on page errors
node core/render/video.mjs <demo> --fps 24 --workers 3     # all frames → out/video24.mp4
node core/render/events.mjs <demo>                         # export DUR + EV → events.json
```

What made capture fast: **JPEG screenshots** (about 8× faster than PNG), **one browser per worker** (pages sharing a browser barely parallelise), and **film grain added in ffmpeg**, not drawn in the page: grain makes every frame incompressible and slow.

## 3. One timeline drives everything

Keep sections, tempo, beats and hit points in one file (`timeline.js`). Export it to JSON and let the score, the mixer, the subtitles and the checks read the same numbers:

```js
export const SECS = [{ id: 'chase', t: 12.0, bpm: 144, beats: 12 }, ...];
export const HIT  = { pratfall: ['chase', 6], ... };   // section + beat
```

A small script (`tools/cuecheck.py` in several demos) compares every visual hit with the music cue it should land on. Aim for 0 ms.

## 4. Voice

- **TTS**: [Kokoro](https://github.com/thewh1teagle/kokoro-onnx) runs locally with good English voices (`af_heart`, `bm_george`, `am_michael`, and others). `core/tts/tts.py lines.json out/` writes one WAV per line and a durations file. Spell numbers out in the TTS text and write them as digits in the subtitles.
- **Check every line**: `core/tts/asr_check.py` transcribes each WAV with faster-whisper and compares it with the script. Re-generate until every line passes. It also writes word timestamps, which you use to place lines and subtitles.
- **Before mixing**: TTS has a high peak-to-average ratio. Compress the voice first, then balance by RMS: voice about 10 dB above the music.

## 5. Music

Write an original score from the cue map. Don't reach for generic piano and strings; each style has its own band (see `STYLE.md` §6).

- **Samples**: `core/audio/sampler.py` plays real instruments from free libraries: [VSCO 2 CE](https://github.com/sgossner/VSCO-2-CE) and [VCSL](https://github.com/sgossner/VCSL) (CC0), [FreePats](https://freepats.zenvoid.org) (CC0), [Karoryfer](https://github.com/sfzinstruments) (CC0), Salamander Grand Piano (CC BY 3.0), MuldjordKit drums (CC BY 4.0). Write the score as events `(time, instrument, pitch, duration, velocity, pan)`. Long notes are extended seamlessly, and round-robins avoid the machine-gun effect. The full list is in `core/audio/INSTRUMENTS.md`.
- **Plucked and folk strings** (guqin, pipa, shamisen, banjo…): `core/audio/pluck.py`, physical modelling (Karplus–Strong) with bends and vibrato.
- **Synthesis** with numpy for chip tunes, drones and effects.
- **Balance the low end.** Synthetic scores get bass-heavy quickly. Measure energy per band after mixing; keep 20–120 Hz around −3 dB relative to the rest, skip pad notes below MIDI 48, and give the bass some 2nd and 3rd harmonics so it speaks on small speakers.

## 6. Sound effects and mix

- `core/audio/sfx.py` synthesises foley procedurally (click, whoosh, thump, ding, paper, noise beds…) with filters, envelopes and `add(buffer, sound, at, gain, pan)`. Drive it from `window.EV`, so every sound sits exactly on its frame.
- Three layers: ambience, foley, music. Duck the music under voice and key foley. Plan the silences.
- **Master**: `sh core/render/mux.sh video.mp4 mix.wav out.mp4 24 [grain]` muxes, runs a two-pass loudnorm to −14 LUFS with a true-peak limit, adds grain in ffmpeg, and prints the measured loudness. On light backgrounds use less grain.
- Films with grain baked into the picture compress badly; re-encode with `-tune grain` and a higher CRF.

## 7. Subtitles

- Export `.srt` with `core/render/srt.py cues.json out.srt` (cues = `[{t0, t1, text}]`), and burn styled captions into the page itself: the caption design is part of the style.
- Timing rules are in DIRECTOR.md §7 (minimum 1.8 s, line + 0.6 s).

## 8. Review loop

1. Contact sheets: render a frame every 1–2 s with `still.mjs --range`, then tile them with `core/render/sheet.py`. Do at least two full passes.
2. Frame strips at 0.2 s for every key action: hand-overs, falls, hits.
3. On the final file: `ffmpeg -af ebur128` (loudness), `blackdetect` (blank frames), whisper again on the final mix if it has voice.
4. Watch it once, at full speed, with sound.

## 9. 3D notes

- three.js r170 rendered headless through WebGL2 on the GPU; physical depth of field and GTAO from `core/three/post.js`, rendered at 2× and downsampled.
- Lighting: soft area lights plus a Poly Haven HDRI at low intensity reads more "real" than bright ambient light.
- The orthographic camera needs `orthographicDepthToViewZ` for depth effects (the perspective version silently breaks DOF).

## 10. Characters drawn in code

- A 2.5D rig (torso, head, limbs solved per frame) is enough for pantomime. Blend poses with keyframes and easing.
- Order the shoulder rotation as abduction, then flexion; the reverse order crosses raised arms into an X.
- Let the shoulder girdle rise and move forward as the arm lifts, and don't outline the part of the arm that overlaps the torso: that line is what makes a joint look like a puppet seam.
- Draw an action test sheet (reach, raise, run, kneel) at large size before animating shots.

## 11. Assets and credits

Only CC0, CC BY or OFL material, each listed in the film's `CREDITS` file with its source and licence. `core/audio/sampler.py credits(names)` writes the lines required for the instruments you used. Fonts: Google Fonts (OFL), self-hosted in the project and subset for CJK.

## 12. Where to look in our demos

| If you need… | Look at |
|---|---|
| 2D character animation and lip sync | `styles/scifi-toon/`, `styles/cel-anime-80s/` |
| a timeline-driven score with cue checking | `styles/microgame/`, `styles/silent-film/` |
| an image-to-ink redraw and film-damage post pass | `styles/silent-film/demo/engine/` |
| a brush or stroke engine | `styles/watercolor/`, `styles/ink-wash/`, `styles/impasto/` |
| 3D with depth of field and real materials | `styles/brick-toy/`, `styles/paper-popup/` |
| a CRT or VHS look | `core/post/crt.js`, `styles/ascii-crt/`, `styles/backrooms/` |

Each style's `STYLE.md` §9 is the exact recipe for its demo, and `demo/build.sh` rebuilds it end to end.
