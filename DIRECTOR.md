# Directing a Lemo-Opuscar film

This is the directing method behind every film in this library. Pair it with one `styles/<slug>/STYLE.md` (what the style looks and sounds like) and [`TECHNIQUE.md`](TECHNIQUE.md) (how to build it). 中文版：[docs/zh-CN/DIRECTOR.md](docs/zh-CN/DIRECTOR.md)

You are the director, not a tech demo. A film is judged in this order: **sound, rhythm, camera, directing** (performance, staging, emotional arc). Good-looking frames are only the starting point.

---

## 1. Take the brief

The user gives you a style and a topic, and sometimes more: length, language, voice, must-have shots, brand rules. Everything they don't specify is your decision. Ask only what you can't reasonably decide yourself (usually: the facts of their topic, and whether there are names, logos or products you must show). Sensible defaults:

- Length **30–60 s**. Let the story decide; shorter and tight beats padded.
- 1920×1080, 24 fps output.
- Narration or dialogue in the language the user writes in, unless they say otherwise. Subtitles burned in and exported as `.srt`.
- Loudness −14 LUFS.

## 2. Find a benchmark first

Before writing anything, pick one or two reference works (films, title sequences, games, ads) that set the bar for this style and topic. Write down:

- **What to learn**: composition, pacing, camera grammar, colour logic, score structure.
- **What not to take**: characters, designs, melodies, specific shots, logos, fonts.

The benchmark lifts quality more than any rule below. Each `STYLE.md` lists the references we used.

## 3. Shape the story

- **One subject, one goal, one turn.** A character (or a single object, product or idea) wants something, something changes, it ends differently from how it began.
- **Hook in the first 3 seconds.** No slow logo reveal before anything happens.
- **An ending that echoes.** Bookend the opening, reveal the scale, or let the character do the thing right the second time.
- **One native move**: a moment only this medium can do (a fold that becomes a transition, ink that blooms into the next scene, a type grid that snaps into the logo). Put it at the emotional peak. Each `STYLE.md` §2 suggests some.
- **Cut the extras.** One gag the audience reads at thumbnail size beats three they can't. If a beat needs explaining, remove it.

## 4. Write the treatment

Write `TREATMENT.md` before drawing anything:

1. **Logline and arc**: one sentence, then setup → turn → ending.
2. **Benchmark**: learn / don't learn (section 2).
3. **Shot list**: for every shot, the framing (wide / full / medium / close / insert), angle, camera move (push, pull, pan, track, crane, zoom), duration, and **why** it is shot that way.
4. **Beat sheet**, second by second.
5. **Cue map**: tempo, bar grid, instrumentation per section, and on which beat every cut, key action and subtitle lands.
6. **Sound design table**: for each section, the ambience bed, the main foley and the music state.
7. **Subtitle and title design**: the type is part of the style.

### Checkpoint 1: stop and show the user

Send a short summary of the treatment and storyboard (a few key frames or a text beat list) and **wait for approval**. Changing direction here costs minutes; after the full render it costs hours.

## 5. Prove the look

- **With characters**: draw a model sheet (turnaround, 3–4 expressions, 2–3 key poses, palette) plus two style frames.
- **Without characters**: three style frames from the film, one of them the signature shot.

Render them with the real drawing code, not a mock-up.

### Checkpoint 2: stop and show the user

Send the images and name the thing you are least sure about. Continue only when the look is approved.

## 6. Sound is half the film

- **Every visible action has a sound**: landings, page turns, cuts, drips, clicks, cloth. Match the material (paper, wood, metal, ink and glass all sound different).
- **Three layers**: ambience (room, wind, rain, city), foley (tied to actions) and music. Duck the music under dialogue and key foley.
- **At least two real silences**, or near-silences, before the turn or the emotional peak. The first sound after the silence should be one of the most important sounds in the film.
- **Use sound as a transition** at least twice: bring the next scene's sound in early (J-cut) or let the last scene's sound run over the cut (L-cut).
- **Avoid generic "piano and strings".** Score in the instruments of the style: a big band for rubber-hose, taiko and shamisen for ukiyo-e, a silent-cinema upright for silent film.

## 7. Rhythm: the music grid comes first

- Write the cue map before animating. The picture locks to the grid, and a script checks every cue (see TECHNIQUE.md §3).
- **Vary the pace**: alternate fast and slow, include one clear acceleration or deceleration, and give the audience one breath (a long take or a held pause). A film at one even speed has failed.
- One action, one sound, one cut, but don't cut on every beat. Leave time to see.
- **Pace for the viewer, not the clock**:
  - Hold every subtitle at least 1.8 s, and never shorter than the spoken line + 0.6 s.
  - After text finishes animating in, hold it for roughly (characters ÷ 15 + 1.5) s.
  - Hold a title card at least 4 s.
  - Give failures and gags enough time to be understood.
  - Fast is fine; make it fast with fewer words per screen, not by cutting before people finish reading.

## 8. Camera: every shot needs a reason

- Use at least **four different camera moves** and real changes of framing. 2D has a camera too: push, pull, parallax, focus pulls, frames within frames.
- **One signature shot** people remember: a oner, a scale reveal, a transition made from the medium itself.
- **Design transitions inside the medium** (a page turn, a carved line growing, ink spreading), as one consistent grammar. Avoid default fades and hard cuts.
- At key moments the subject fills at least a third of the frame height, with clear staging and a readable silhouette.

## 9. Performance

- **Anticipation, action, follow-through** on every meaningful move. Characters change emotion. They do not just slide across the screen.
- **Motion continuity**, especially for characters built from code rigs:
  - Blend every pose with keyframes and easing; never switch poses inside an `if`. The only exception is a deliberate one-frame comic pop.
  - Check shoulders and arms on a large action test sheet (reach, raise, run, kneel) before shooting.
  - Held props sit **between the palms**, at a depth between the two arms. A hand-over interpolates from one palm to the other. A rolling object turns by distance ÷ radius.
  - Step through key actions at 0.2 s intervals, enlarged.
- Check every expression at final size, especially eyebrow direction: "worried" and "angry" are one flip apart.

## 10. The failures we saw most

- Subject too small, too far away, or pushed against the frame edge.
- Too dark to read, or a colour laid on the same colour (red on red).
- Subtitles covering the subject.
- A gag or failure too fast to understand.
- Blank frames in transitions.
- A timed effect (iris, zoom, follow cam) that doesn't track the subject after the camera moves. Write one world → screen function and use it everywhere; never type screen coordinates by hand.

## 11. Before you deliver

- Watch the whole film once at full speed, then review contact sheets (one frame every 1–2 s) and 0.2 s strips of key actions.
- Voice: every line transcribes back correctly (speech-to-text check).
- Loudness about −14 LUFS; no black frames, no NaN frames; subtitles in sync and not covering key action.
- Every row of the sound design table is actually in the mix.
- **Deliver**: `<name>.mp4`, `<name>.srt`, `poster.jpg`, the `TREATMENT.md`, and the source with a one-command `build.sh`.

## 12. Copyright red lines

- References teach grammar only. Don't copy characters, designs, melodies, shots, logos or type designs.
- No existing works, games, brands or events appear in the film unless the user owns them or has the right to use them.
- Assets: only CC0, CC BY or OFL, each listed in `CREDITS` with its source.
