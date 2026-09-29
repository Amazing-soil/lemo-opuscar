---
name: lemo-opuscar
description: Direct and produce a short film made entirely in code, in one of the 43 styles of the Lemo-Opuscar library (e.g. Impasto Oil Painting 油画厚涂, Watercolor Brush 水彩笔刷, Chinese Ink Wash 中国水墨, Ukiyo-e 浮世绘, Whiteboard Explainer 白板讲解). Use when the user asks for a video, film, short, promo or animation (视频、短片、动画、宣传片) in a named style, or asks which film styles there are.
---

# Lemo-Opuscar

The styles, the directing and building guides, and the tools live in the Lemo-Opuscar library, a local copy of github.com/lemomo-ai/lemo-opuscar. This skill finds that library and hands you over to it.

## 1. Get the library

Run the setup script from this skill's base directory:

```sh
sh "<skill base directory>/scripts/setup.sh"
```

On the first run it downloads the library (about 60 MB: guides, `core/` tools, every `STYLE.md`) to `~/lemo-opuscar`; later runs update it. If the user is standing in a clone of the repo, that clone is used. `LEMO_OPUSCAR_HOME` overrides the location. The last line prints `LIB=<path>`.

Then start `sh "<skill base directory>/scripts/setup.sh" deps` at once, in the background if you can. It installs the Node and Python packages and the headless browser the renderer uses, and takes a few minutes the first time, so it runs while you talk with the user. If either run reports missing system tools (Node 20+, ffmpeg, Python 3.11+), tell the user in your one round of questions. Don't install system software yourself.

## 2. Follow the library's instructions

Read `$LIB/AGENTS.md` and do what it says. It has the full workflow:

- finding the style in `styles/README.md`;
- reading `DIRECTOR.md`, `TECHNIQUE.md` and the chosen `STYLE.md`;
- the one round of questions before you start;
- the optional storyboard.

What changes in skill mode:

- **The project lives in the user's folder.** Make `<name>/` in the folder where the user started. Use lowercase letters, digits and hyphens for the name (`orange-cat`); `#` or `%` in the path breaks ffmpeg. If that name is already taken by something else, pick another. Everything goes there: code, audio, stills, `build.sh`, and the finished `<name>.mp4`, `.srt` and `poster.jpg`. Wherever the library's docs say `films/<name>/`, read this folder.
- **Running tools.** Run the library's tools from `$LIB` and give them the project's absolute path. For example:
  - `cd "$LIB" && node core/render/still.mjs "<project>" 1.5 3`
  - `"$LIB/.venv/bin/python" "$LIB/core/tts/tts.py" "<project>/lines.json" "<project>/voices"`

  The render server serves the project at `/@film/` and the library at `/`.
- **Reaching library files.**
  - In pages, use absolute URLs: `/core/lib.js`, `/node_modules/three/...`, `/styles/<slug>/demo/...`.
  - In Python and Node scripts and in `build.sh`, use `$LIB/...` paths. Never use `../..`, because the project is not inside the library.
  - Put `LIB=<path>` at the top of `build.sh`.
- **Demo source.** A style's demo source isn't downloaded by default. When its `STYLE.md` §9 points to a file you want to study or import, run `sh "<skill base directory>/scripts/setup.sh" demo <slug>`. The demo is a reference implementation: learn and reuse its techniques, but don't rebuild it or copy its story.
- **Delivery.** Tell the user the path of the project folder and the finished film.
