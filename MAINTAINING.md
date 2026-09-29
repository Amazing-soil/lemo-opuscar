# Maintaining the library

**For the repository owner only.** If you are making a film for a user, go back to [`AGENTS.md`](AGENTS.md): nothing here applies.

## Add a style

Work in `styles/<slug>/` (lowercase letters, digits, hyphens; unique). Start from the templates in `styles/_template/`.

| File | What it holds |
|---|---|
| `style.json` | the only metadata source: `slug`, `num`, `en`, `cn`, `category_en`, `category_cn`, `film`, `line`, `line_cn`, `uses`, `frame_sec`, `dur` |
| `STYLE.md` | the style's invariants only: look, materials and rendering, colour logic, type, motion, camera grammar, sound palette, the medium's pitfalls, native moves, range of variation. No story, arc, beat table, durations or end card. Ends with a link to `DEMO.md` |
| `DEMO.md` | opens with "One example among many. Don't reuse its story, arc, shots, props or timings." Then the demo's story and structure, shot list, score structure, palette and props, end card (the "LemoLab × Claude Opus 5.5" sign-off lives only here, as the library demo's), build notes and code entry points, and for a scene style the `content.json` fields |
| `demo/` | the source, a one-command `build.sh` and `CREDITS` are committed, for agents to read. `TREATMENT.md`, `PRODUCTION_LOG.md`, fonts, audio, textures and models stay local (gitignored); `CREDITS` names every asset so it can be found again |
| `demo/stills/` | stills the docs link (`styleframe.jpg` is the gallery card) |
| `<slug>.mp4`, `<slug>.srt`, `poster.jpg` | the 1080p film, its subtitles when it is spoken, its poster |

Assets are CC0, CC BY or OFL only, each in `demo/CREDITS`. No watermark on any film. Real people, brands and events appear only in an unofficial fan film; its `DEMO.md` says so.

## Gates

- **Human:** approve the style frame before production, and the finished film.
- **Machine:** `asr_check.py` passes on every line; loudness about −14 LUFS; `readcheck.mjs` passes; `python3 tools/release.py check --strict` is clean.

## Register and publish

1. `python3 styleboard/build.py` reads every `styles/*/style.json` and rewrites the gallery data, the README grid and counts, `styles/README.md` and the style list in `AGENTS.md`. Never edit those generated parts by hand. `--frames <slug>` makes the README grid frame at `frame_sec`; `sh styleboard/frames.sh` makes the gallery card images.
2. `sh tools/publish.sh` uploads the full films (`films` release) and the 720p web cuts (`web` release, used by the gallery), then verifies them. Per-demo resource packs are no longer published.
3. `git status --short`, `git add -A`, commit.
4. Push `main`, then watch CI (`gh run watch`): the gallery build fails when a card links a film that isn't on the `web` release.

Don't push before the upload has finished, and don't commit `tools/assets.json` from a failed run.

## Revise a style

Back up first (old versions move out of the repository, not into git). Re-render, replace `<slug>.mp4`, and run `sh tools/publish.sh`: it re-uploads the film and refreshes its web cut.
