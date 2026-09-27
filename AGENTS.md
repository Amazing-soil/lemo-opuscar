# Lemo-Opuscar: instructions for agents

This repository is a library of film styles. Each style is a prompt (`styles/<slug>/STYLE.md`) with a demo film made entirely in code. People open an agent here, pick a style, and ask for a film about **their own** topic. Your job is to direct and produce that film.

## Read first

1. [`DIRECTOR.md`](DIRECTOR.md): how to direct (story, sound, rhythm, camera, performance, checks).
2. [`TECHNIQUE.md`](TECHNIQUE.md): how to build it (render(t) pages, voice, music, mix, review).
3. `styles/<slug>/STYLE.md` for the chosen style. §1–§8 define the style. §9 shows how our demo was built. The demo is a reference implementation: learn and reuse its techniques, but don't rebuild it or copy its story.

**Finding the style.** Users name a style by its gallery name in English or Chinese ("Impasto Oil Painting", "油画厚涂") or by its folder (`impasto`). Look it up in [`styles/README.md`](styles/README.md), which maps every name to its folder. If nothing matches clearly, show the closest two or three and ask.

If the user hasn't picked a style, show them the list in `styles/README.md` (or the gallery in `styleboard/index.html`) and suggest two or three that fit their topic.

## Workflow

1. **Brief.** Make sure the style and the topic are clear. Then ask the user once, in a single message (DIRECTOR.md §1). If the style is unclear, that question goes in the same message:
   - anything about the topic you can't decide yourself (facts; names, logos or products that must appear);
   - whether they have material of their own: a voice recording or a preferred voice, music, photos, logos, fonts. Whatever they don't provide, you make;
   - whether they want to review a storyboard before production. The default is no: you go straight to the finished film.

   Skip any question their request already answers. Wait for the reply, then fill every other gap with a sensible default, sum up the brief in a few lines, and start. Don't come back with more questions later.
2. **Treatment.** Write `films/<name>/TREATMENT.md` (DIRECTOR.md §4).
3. **Look.** Render a model sheet or style frames with the real drawing code and check them yourself against the `STYLE.md` (DIRECTOR.md §5).
4. **Storyboard, only if the user asked for it.** Show the key shots rendered in the style, with durations and lines, plus the logline (DIRECTOR.md §5).
   **Stop and wait for approval.** If they didn't ask for it, don't stop.
5. **Produce.** Voice → check → score (can run in parallel) → animation → mix → render.
6. **Self-check** (DIRECTOR.md §11), then deliver `films/<name>/<name>.mp4`, `.srt`, `poster.jpg` and the source with `build.sh`.

A user's film carries no LemoLab credit and no watermark. The "LemoLab × Claude Opus 5.5" end card in the `STYLE.md` files belongs to our demos only.

Report progress in the user's language. The film's own language is whatever the user asks for (default: the language they write in).

## Where things go

- Work only in `films/<name>/` (ignored by git), unless the user asks you to work in their own project.
- `core/` has ready-made tools (rendering, TTS, speech check, sampler, sfx, mux). Use them or your own stack, but don't edit `core/` or `styles/` for a user's film.
- Large assets are fetched on demand: `sh tools/fetch.sh voice | instruments | hdri`.
- Never kill processes you didn't start. Don't leave background processes running.

## Maintaining the library (repository owner only)

To add a new style:

1. Make it in `styles/<slug>/`: `STYLE.md` in English, following the §1–§9 structure of an existing one; `TREATMENT.md`; `demo/` with the demo's source (a reference implementation, not a rebuild kit) and `CREDITS`; `<slug>.mp4`, `<slug>.srt`, `poster.jpg`, and `demo/stills/styleframe.jpg`.
2. Add a card to `styleboard/cards.json`: film title, one-line story in English and Chinese, and use cases.
3. Run `sh tools/publish.sh`. It checks the repo (no files over 5 MB, no absolute paths, no secrets), uploads new or changed films to GitHub Releases, and rebuilds the gallery data.
4. Commit and push. The gallery (GitHub Pages) rebuilds itself.

The skill in `plugin/skills/lemo-opuscar/` is a thin wrapper: it fetches this repo and sends the agent to this file. Keep the workflow here, not in `SKILL.md`.

Rules: back up before revising (old versions move out of the repo, not into git); only CC0, CC BY or OFL assets; every film's end card carries "LemoLab × Claude Opus 5.5"; no watermark.
