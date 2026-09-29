# Mid-century Cartoon — Style Prompt

> 1950s flat colour and limited animation for "follow along" films: colour printed a few pixels off its broken ink line, bodies that hold still while hands do the work, abstract colour-block rooms, a calm classroom narrator, and a cool-jazz combo with a vibraphone chord on every step.
> Demo: *Meet Pip* (40.0 s) · `midcentury-toon.mp4` · source in `demo/` · a product set-up guide for a fictional robot vacuum. It fits a product page, a QR code on the box, or a help centre.
> **References (grammar only):** UPA studio's early-1950s shorts (*Gerald McBoing-Boing*, *Rooty Toot Toot*): colour and line on separate cels, geometric people and furniture, backgrounds that are only colour planes, limited animation. The Coronet and Encyclopaedia Britannica classroom films of the 1950s: the "Meet ___." opening, one sentence per picture, numbered step cards, a summary card at the end. Charley Harper and Mary Blair: the atomic-age palette of soft complementary colours and the geometry of their figures and objects. 1950s appliance manuals and adverts: numbered medallions, curved pointer arrows, round detail call-outs, sunburst backgrounds. Never copy their characters, drawings, lettering or music, and never write their names in a film.

You are directing a 30–40 second **scene film** in the **Mid-century Cartoon** style. A scene film does not tell a story. It performs a real use: a set-up guide, a how-to, a recipe card, a safety card. The user gives you the thing and its steps. You decide the shots, the timing, the sound and the score, and you deliver a finished film. The viewer should come away able to do the thing.

---

## 1. What this style is

Flat, printed-looking colour with a thin, breathing ink line that never quite closes. **Every fill is a separate "cel" printed about (6, 4) px off its line**, and that offset re-rolls on twos (12 fps, ±1.6 px), so the picture shimmers like hand-registered paint while the camera glides at 24 fps. The fills carry a light dry-brush tooth; paper grain and a warm vignette sit over everything.

People and things are geometric. June, the demo's new homeowner, has an egg head with a long pointed nose that is part of the face's outline, a bob with a mustard headband, a coral turtleneck and navy cigarette trousers. Her **body is a held drawing: only her arms, hands, eyes and mouth animate.** Hands are four-finger cartoon gloves (three fingers and a thumb) in four shapes: open, flat, point and grip. Rooms are not drawn. A scene is one colour plane, a floor band, a horizon line with gaps, and one or two props: a wall edge, a socket, a phone.

It is not the 1930s rubber-hose cartoon: no black-and-white, no bouncing world, no hot jazz. It is not a whiteboard explainer: it shows *how to do*, not *why*. The pictures are printed, not written on.

## 2. Use cases: what this style is for

| Use case | Shot structure | Information layers (in order) | Hold per layer | Length |
|---|---|---|---|---|
| **Product set-up guide** (the demo) | Hook reveal → one scene per step (wide + round detail call-out) → payoff (the product working) → tip → poster lockup | product name → title → step title → step detail on the action beat → payoff caption → tip → CTA | title ≥ 4 s; step title the whole step; detail ≥ chars/12 + 1 s; lockup ≥ 3 s clean | 30–40 s, 2–5 steps |
| **Safety / rules card** (lab, pool, flight) | One held figure; each rule is a medallion stamp, a single hand gesture and a pictogram | rule number → rule → one "why" detail | 3–4 s per rule | 20–40 s, 3–6 rules |
| **Recipe or ritual card** (coffee, plant care) | Tabletop side view; each step a call-out circle on the hands; the payoff is a top view where the result becomes a pattern | step → quantity/time → result | 3–5 s per step | 30–45 s |
| **Onboarding for an app or service** | June with a phone; the screen lives in the call-out circle; signal rings travel to the device | screen action → setting value → confirmation stamp | 3–4 s per action | 20–30 s |
| **Store or event notice** | Colour-block wipes between 3 cards; one character presents | headline → time/place → CTA | ≥ 3 s per card | 15–25 s |

The demo is the first use case. All five use the same engine: `shape()` for any prop, `drawOwner()` for the presenter, `drawHand()` for close-ups, `callout()` / `medallionAt()` / `tag()` for layers, and a top-view plan for the payoff.

**How the native moves serve information (not story):**
- **Off-register colour** makes a flat info card feel hand-made, and warm enough to sit on a product page. Keep it on everything, text included.
- **Limited animation** points the eye. When the body is still, the hand is the only thing moving, and that hand *is* the step. Give every step one hand action with anticipation → action → follow-through, landing on a beat.
- **The round call-out** (a manual's magnifier) is the close-up. The wide stays for context and the hands get big inside the circle. The step's data (50 cm, 2.4 GHz, one second) lands inside or on that circle on the action beat, never as a slide.
- **The numbered medallion** is both a hierarchy marker and a door. It stamps onto the outgoing scene's subject, and the camera goes through it into the next step.
- **The payoff turns function into ornament.** In the demo, the vacuum's real route (wall-follow, then boustrophedon lanes that flow around furniture, with a small curl at every turn, stars and dots between lanes) draws itself room by room, one room per beat. Stepping back, it reads as an atomic-age textile.

## 3. Visual language

**Palette (demo; every value is a content.json field):**

| Role | Hex |
|---|---|
| Paper | `#F4EAD5` (shade `#E6D8BC`, `#D4C29F`) |
| Ink (warm black) | `#2B2420` |
| Coral (accent, June's sweater) | `#E4613F` / dark `#B8452B` |
| Mustard (hook ground, belts, dots) | `#E8B43A` / light `#F3D37F` |
| Turquoise (the product) | `#3FA7A0` / dark `#257A74` |
| Dusty blue / avocado / pink / plum (step grounds) | `#7F9CC0` · `#A7AE5B` · `#F0B4A8` · `#6E4A6B` |
| Navy (trousers) · hair · skin | `#3B4766` · `#3A2621` · `#F2C7A0` |
| Kraft (box) | `#C9955D` / `#A2713F` / `#DDB47F` |

- **One ground colour per scene**, lighter tint for walls (`tint(col, .45)`), darker shade for floors (`shade(col, .16)`). Never place the product on its own colour or June on coral/pink.
- **Line:** 3–5 px ink ribbons with ±40 % width breathing and 12–25 % breaks. Characters: 4 px. Props: 3–4.5 px. Walls in plans: 6–7 px, broken. Hands: one 6 px outline around the union of palm and fingers, 2.4 px finger separations.
- **Shading:** one flat darker plane clipped inside a shape (never a gradient). Drop shadows are a copy of the shape offset (12, 12) in a paper shade at 50 %.
- **Ornaments:** 4-point atomic sparkles, 8–18-point starbursts, sunburst rays (30 wedges, 55 % alpha), boomerang and kidney shapes, polka dots.
- **Type:** Oleo Script Bold for the kicker ("Meet Pip."); Alfa Slab One for titles, numerals and step headers (ink with a cream or colour plate offset 4–7 px); Jost 500/600 for body, details, labels and captions (letter-spaced caps for small labels).
- **Grain:** light (mux grain 4) plus the paper overlay; the look is print, not film.

## 4. Motion language

- **On twos:** character poses, hand shapes and the colour-cel jitter change at 12 fps. The camera, iris wipes, arrows, the plan route and rays move at 24 fps.
- **Held body, moving hands:** switch poses with a single in-between (for example reach → one in-between → ta-da). A hand action has anticipation (pull back or lift 20–60 px), a fast action (0.15–0.25 s, eased out), a follow-through (recoil 6–10 px, settle, hand lifts away) and lands exactly on a beat.
- **Pop-ins:** medallions, tags, labels and titles scale in with a back-ease (0.24–0.3 s, overshoot 1.9).
- **Kneel pose** (`kneel: true`): hips drop 150 units so flat hands can reach floor props. The arms are solved with 2-bone IK (`kneelPose()`) so the hands stay on the object while it moves.
- **Lettering:** the kicker writes on left→right with a clip; headers slide in from the left on twos.

## 5. Camera language

The camera is always "the stand": pushes, trucks, tilts, pull-backs, never handheld. One transition grammar, **the circle**:

| Move | Where in the demo | Why |
|---|---|---|
| Slow push 1.00 → 1.07 | Hook | Collects the eye onto the product on its stage |
| **Iris through the medallion** (circle grows from the stamp to full frame, 0.9 beat) | Every step change | The step number *is* the door |
| Truck right + gentle push | Step 1 wide | Follows the push toward the wall |
| Round detail call-out (frame in frame, with a dashed leader line to its subject) | Every step | Constant line weight at close-up scale; context stays visible |
| Push into the phone, then pan along the signal rings | Step 2 | From person → interface → device |
| Tilt down with the finger | Step 3 | The press is the most important action; the finger leads the frame |
| **Button → iris → top view** | Step 3 → payoff | The start button opens into the plan; circle to circle |
| **Pull-back + counter-rotation, 5.4× → 1.0×, −6° → 0°** (signature) | Payoff | Scale reveal: one lane → a whole flat printed like a textile |
| Colour-block wipe (side for the tip, bottom-up for the lockup) | Tip, lockup | Changes the "page" of the manual |
| Dead still ≥ 3 s | Lockup | Tells the viewer: this frame is the one to screenshot |
| **Iris-out onto the product**, end card inside a circle | End | The classic cartoon ending, and the last circle |

Keep key subjects at ≥ 1/3 frame height and out of the bottom 140 px (the caption card).

## 6. Sound

Three layers, always:
- **Ambience:** a warm room tone (low-passed brown noise, about −42 dB) and a very quiet mantel-clock tick on the half-note grid. In the payoff, the product's motor hum (a band-passed saw with a slow LFO plus brush hiss) takes over.
- **Foley by material:** cardboard (creak, dull flap thumps pitched a semitone apart, a swish into a slap), appliance plastic (a bright knock with a short hollow body; the plug click), wood floor scrapes, rubber stamps (thick and damped) for every medallion, paper swishes for wipes, slide whistles for dimension arrows, rising sine pips for "connected", pen scratches when a room's route draws, the ink line peeling off paper, an iris "shhk".
- **Music:** an original West-Coast cool-jazz combo at 132 BPM: vibraphone (chords, arpeggios, glissandi, motor tremolo), flute (melody), pizzicato upright bass (walking), brushes (a swirl plus 2 and 4, sticks on the ride for the payoff), a celesta colour. **Every step lands on its own vibraphone chord** (F6, B♭maj7, C9), and the lockup brings those chords back one per medallion, transposed. Not ragtime, not a spy big band, not piano and strings.
- **Rhythm arc:** normal → double-time at the payoff (key up a whole step) → half-time for the tip (the breath) → normal for the lockup.
- **Silences:** A (0–1.36 s): no music, only the box. B (the last beat before the press): *everything* off, ambience included, so the first sound after it is the most important one: the start click. C (before the lockup): room tone only. The first sound after silence C is the first medallion stamp.
- **J/L cuts:** music enters before the reveal; each step's line starts half a beat before its iris; the motor starts 0.2 s before the payoff; the last Wi-Fi pip rings into step 3; the payoff's glissando tail rings into the tip.
- **Mix:** narration compressed on top, music ducks 8 dB under it, foley unducked, −14 LUFS, true peak −1.2.

## 7. Subtitles & titles

- **Caption card:** a paper-coloured rounded slab with a thin ink border (its colour cel offset 5 px), a slowly turning coral 8-point star at each end, Jost 500 42 px in ink, centred 60 px above the bottom. It fades in over 0.16 s with a 10 px rise. Hold ≥ max(1.8 s, speech + 0.6 s, chars/12 + 1 s).
- **Step header:** an ink disc with a paper numeral (Alfa Slab), a small letter-spaced "STEP n OF N", and the step title in Alfa Slab 64 px with a cream plate. It slides in on twos.
- **Detail tags:** a paper card with an accent star bullet, Jost 36 px. It pops on the action beat, on or next to the call-out.
- **Narrator:** calm classroom authority. The demo uses Kokoro `am_michael` at 0.94. `bm_george` was tried: whisper heard "dock" as "dark" in his British vowel. Keep lines to one clause: "Step one. Set the dock against a wall."
- **End card** (after the lockup, inside the iris circle): film title, style name, `Lemo-Opuscar`, `LemoLab × Claude Opus 5.5`, asset credits.

## 8. Pitfalls we hit

1. **The route must obey the product.** Our first payoff looped over the sofa. Fix: wall-follow first, then lanes that bend around furniture as **potential-flow streamlines** (`laneY()`): lanes never cross and never enter an obstacle ellipse (furniture + 30 px). Keep obstacles away from walls; a streamline squeezed against a wall piles lanes on top of each other.
2. **Don't lay the whole pattern at once.** Draw it room by room, one room per beat, with the camera pulling back. Then return home on a dotted line that also avoids furniture.
3. **Nose inside the outline.** A nose drawn as a separate wedge looks like a paper cone glued on. Build the head as one open spline from the bridge round the skull to under the nose, then close it at the nose tip (`chain + tip`). In 3/4 view, place the far eye left of the bridge so it shows.
4. **Arms from the shoulders.** Shoulders sit at the torso corners (±40–46, −384). Draw sleeves as a thick ink ribbon with a coral ribbon on top. Thin ink arms read as sticks coming out of the neck.
5. **Glove hands need gaps.** Drawing the fingers as fat blobs turns the hand into a cloud. Stroke every part first and fill every part second (one union outline), with slender fingers (rx 12–13, ry 5) and separation lines.
6. **Floor reach.** A standing figure's hands stop about 190 units under the shoulder. Kneel and solve the arms with IK instead of stretching them.
7. **Line weight in close-ups.** Zooming the world camera 3× triples the ink. Put close-ups in a call-out circle drawn at native scale.
8. **Detail text needs its reading time.** "Against a wall, 50 cm clear each side" did not fit its 3 s window. The data moved into `detail` ("50 cm clear on each side") and the wall into the title and the line.
9. **The payoff route + a caption arrow can collide with labels.** Put room labels *under* the plan and the caption in the top margin.
10. **Iris content at negative local time.** When a transition draws the next scene before its start, clamp `t` to just past the start (otherwise poses and pop-ins are undefined).

## 9. Production recipe (this repo)

1. `demo/content.json` holds every word, number, colour, the voice and the payoff plan. `python3 demo/tools/lines.py` turns it into `lines.json`.
2. Kokoro (`core/tts/tts.py`) → `voices/` + `dur.json`; `asr_check.py` until every line is OK (step numbers are compared as digits).
3. The timeline is built from content: hook 4 bars, each step ≥ 3 bars (from its voice length), the last step 2 bars, then payoff 3, tip 2, lockup 3 and end 2 bars at 132 BPM. Three steps = 22 bars = 40.0 s.
4. The score (`music/score.py`, forked to a sub-agent with the cue map) → `score.wav`, stems and `hits.json`.
5. `core/render/events.mjs` exports the same event times the pictures use. `tools/cuecheck.py` checks every hit against the half-beat grid and the score (0 off in the demo). `mix.py` builds foley, voice, ducking and the three silences.
6. `tools/cues.mjs` → `.srt`; render with `core/render/video.mjs` (960 frames ≈ 30 s with 2 workers); `mux.sh … 24 4`.
7. `sh demo/build.sh` does all of it; `sh demo/build.sh stills` renders the content-swap test.

## 10. Engine usage

`demo/engine/toon.js` (the style), `demo/engine/chars.js` (the presenter, hands and product), `demo/engine/icons.js` (18 icons). All functions draw in the current canvas transform.

| Function | What it draws | Key params |
|---|---|---|
| `setClock(t)` | Sets the clock for the on-twos register jitter; call once per frame | `t` seconds |
| `shape(ctx, pts, o)` | **Any shape in this style**: off-register fill + tooth + broken ink line | `fill`, `line` (px), `off` [dx,dy] (default: jittered `REG`), `grain` 0–1, `breaks` 0–1, `shade` [{pts,color,alpha}], `seed` |
| `ink(ctx, pts, w, o)` | Pressure ink ribbon along a polyline | `closed`, `breaks`, `wob`, `taper`, `color`, `upto` 0–1 (draw-on) |
| `plane(ctx, pts, fill)` | Lineless ground plane | `off`, `grain` |
| `text(ctx, str, x, y, o)` | Two-plate lettering | `font`, `fill`, `plate` (off-register colour plate), `off`, `align`, `rot`, `maxW`, `track` |
| `fit(ctx, str, fam, px, maxW, maxLines, minPx)` | Wraps, then shrinks to fit | returns `{font, px, lines}` |
| `arrow(ctx, from, to, o)` | The moving manual arrow | `u` draw-on, `bob` beat phase, `bend`, `head`, `fill`, `dashedShaft` |
| `star` / `sparkle` / `rays` / `atom` / `kidney` / `boomerang` | Mid-century ornaments | radius, points, rotation, fill |
| `REG` | Global register: `{dx:6, dy:4, jit:1.6, on:true}` | set `REG.on = false` for crisp diagrams |
| `drawOwner(ctx, pose, t)` | The presenter | `x,y,s,dir,view('front'/'q'/'side'/'back'),face('neutral'/'happy'/'wow'/'focus'/'wink'),armF/armB{a1,a2},handF/handB,kneel,blink,look,prop{kind:'phone'/'dock'/'cable'}` |
| `drawHand(ctx, x, y, angle, kind, side, scale)` | Four-finger glove: `'open'`, `'flat'`, `'point'`, `'grip'` | — |
| `drawPip(ctx, x, y, o)` | Round robot product | `view('side'/'top')`, `s`, `light`, `press`, `brush`, `ang`, `colors{product,productD,trim,light}` |
| `icon(ctx, name, cx, cy, size, o)` | Icon library: dock, phone, start, cable, wifi, plug, water, beans, cup, filter, box, clock, check, leaf, key, bulb, spark, gear | `main`, `light`, `dark` |

Film-level helpers in `film.js` you can lift: `callout()` (round detail view with a leader line), `medallionAt()` (numbered stamp), `tag()` (detail card), `stepHeader()`, the potential-flow `laneY()` + `buildPath()` route generator, and the transition block in `renderFilm()` (medallion iris, button iris, colour-block wipe, iris-out).

**Minimal example: a warm-orange four-point spark with a cursor-tail, in this style** (the "only colour" slot: keep `fill` fixed while the scene recolours):
```js
import { setClock, shape, ink, sparkle, starPts, spline, PAL } from './engine/toon.js';
setClock(t);                                   // register jitter on twos
ctx.fillStyle = PAL.paper; ctx.fillRect(0, 0, 1920, 1080);
// the tail: a broken ink stroke that draws on
ink(ctx, spline([[520, 700], [700, 640], [860, 560]], false, 10), 6, { upto: Math.min(1, t / 0.6), breaks: 0.2 });
// the spark: any closed path -> off-register fill + breathing ink line
const pts = [];
for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4 - Math.PI / 2, r = i % 2 ? 26 : 110; pts.push([960 + Math.cos(a) * r, 520 + Math.sin(a) * r]); }
shape(ctx, pts, { fill: '#D97757', line: 4.5, grain: 0.3, breaks: 0.15 });
sparkle(ctx, 1040, 440, 28, { fill: PAL.white });
```

## 11. Swap in your content

Everything readable and every colour comes from `demo/content.json`. The page reads `?content=<file>` for tests.

| Field | Type | Range | If out of range |
|---|---|---|---|
| `product` | string | 1–12 chars | Squeezed to fit on the box label (`maxW`) |
| `kind` | string | free | Only for your own reference |
| `title` / `subtitle` | string | ≤ 36 / ≤ 24 chars | Title wraps to 2 lines in the hook, shrinks to 50 px on the lockup |
| `hook.kicker` / `hook.line` | string | ≤ 14 chars / one sentence | Kicker squeezed to 760 px; the line becomes the first caption |
| `steps[]` | array | **2–5** | Each step adds ≥ 3 bars (5.45 s); the lockup row respaces (R 104 → 88 px beyond 3 steps). 4 steps ≈ 45 s: trim the tip or end card if you need ≤ 40 s |
| `steps[].title` | string | ≤ 22 chars | Shrinks to 40 px (header), wraps to 2 lines (lockup) |
| `steps[].detail` | string | ≤ 30 chars | Wraps to 2 lines; must be readable in its window (chars/12 + 1 s) |
| `steps[].icon` | enum | the 18 icon names | Unknown → `spark` |
| `steps[].action` | enum | `place` (push to a wall + clearance diagram; uses `measure`), `tap` (phone pairing, signal rings to the product), `press` (finger + hold ring); anything else → `show` (icon in hand, finger taps it in the call-out) | — |
| `steps[].measure` | string | e.g. "50 cm" | Only for `place`; empty = arrows without labels |
| `steps[].line` | string | one short sentence | Voice + caption; a long line lengthens its step |
| `payoff.caption` | string | ≤ 40 chars | Shrinks to 26 px |
| `payoff.plan` | object | `y0,y1`, `dock[x,y]`, `zones[]` (name, x0, x1, color, checks), `rug`, `items[]` (shape: sofa, kidney, boomerang, chair, plant, table, bed; x, y, s, rot, color, accent) in 1920×1080 plan px | Zones narrower than 400 px get the wall-follow loop only; items become flow obstacles automatically |
| `tip.label/text/icon/line` | strings | text ≤ 40 chars | Header shrinks; the ribbon widens |
| `outro.line` / `outro.cta` | string | cta ≤ 48 chars | CTA shrinks to 20 px |
| `palette` | object | `paper, ink, product, productDark, accent, hook, steps[], tip` | Missing keys fall back to the demo palette |
| `voice` | object | Kokoro `id`, `speed` | — |
| `film` | object | `name, style, credits` | End card |

**Steps to swap:** edit `content.json` → `sh demo/build.sh` (it rebuilds lines, voice + whisper check, events, mix, captions, video). The score is written for 22 bars; if your step count changes the length, rerun the music sub-agent with the new section table, or keep 3 steps.

**Minimal example** (only what changes):
```json
{
  "product": "Mo", "title": "Your New Robot Mower", "subtitle": "Set Up in 4 Steps",
  "hook": { "kicker": "Meet Mo.", "line": "Meet Mo, your new robot mower." },
  "steps": [
    { "title": "Set the base station", "detail": "Level ground, 1 m clear in front", "icon": "dock", "action": "place", "measure": "1 m", "line": "Step one. Set the base station on level ground." },
    { "title": "Peg the boundary wire", "detail": "30 cm in from the lawn edge", "icon": "cable", "action": "show", "line": "Step two. Peg the wire around the lawn." }
  ],
  "palette": { "product": "#E4613F", "accent": "#3FA7A0", "hook": "#7F9CC0" }
}
```
`demo/content_alt.json` is the full version of that example (a 4-step robot mower on a garden plan); its stills are in `demo/stills/alt_*.jpg`.
