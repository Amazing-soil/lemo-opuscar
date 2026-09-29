# Sci-fi Hologram HUD — Style Prompt

> A hardware product is scanned into a glowing wireframe. Target boxes lock onto parts one at a time; each part splits into a local exploded view, a leader line pulls out, and its number rolls from garbage glyphs into the real value. At the end, the wireframe lights up into a solid hologram and settles into a spec sheet you could use as a poster.
> Demo: *Volt · Spec Scan* (39 s: a 34 s scene plus a 5 s end card) · `hologram-hud.mp4` · source in `demo/`. It is the spec walkthrough of a fictional city e-bike.
> References (grammar only): the HUD and holo-table language of the *Iron Man* / *Avengers* films (Territory Studio, Perception): target boxes, leader-line callouts, rolling numbers, layered depth. The *Oblivion* interfaces: one restrained colour, hairlines, lots of empty space. Industrial CAD wireframes and exploded views. Never copy their layouts, icons, fonts, colours or props.

You are directing a 30–40 second **scene film** in the **Sci-fi Hologram HUD** style. The user gives you a product, a device or any object with parts, plus the facts to show. You decide the model, the order, the timing, the sound and the look, and you deliver a finished film. Follow this guide.

---

## 1. What this style is

The subject is always a **line wireframe made of light**, projected in perspective above a round projector pad on a near-black stage. It is never a rendered object. Everything reads as *scanned data*. A scan plane rises and the model grows under it. Parts can be pulled apart along their assembly axes. Numbers are *computed* on screen and roll into place.

Three depth layers are always present: a **background dot grid** (slow parallax), the **subject** (with its perspective pad and floor), and the **foreground HUD** (corner brackets, rulers that parallax faster, status text).

The palette is **one cold hue plus one warm accent**. The hue carries the lines, the HUD and the fills. The accent (amber in the demo) is spent on **locked values only**. A number turns amber at the frame it becomes true. Nothing else is amber.

It is *not* a font-driven keynote (dark-keynote), a paper drafting sheet (blueprint) or a realistic product render (glass-product). Keep the subject a wireframe the whole time. Only at the high point does it gain translucent faces, and even then the lines stay on top.

## 2. Use cases: what this style is for

| Use case | Shot structure | Information layers (in order) | Hold per layer | Length |
|---|---|---|---|---|
| **Product spec walkthrough** (the demo: product page hero, spec section of a crowdfunding video) | Scan-in → title → N × (lock → camera move → local explode → leader → value) → regroup → solid-hologram turn → spec-sheet lockup → end card | Name + category + tagline → key spec per part (label + value + unit + one detail line) → weight / price → call to action | Title ≥ 5 s. Each part: value visible ≥ 2.5 s on the big card, then it **stays** as a chip in the left rail until the end (so every spec is on screen for 10–25 s). Lockup ≥ 3 s with everything present | 30–40 s, 2–5 parts |
| **Trade-show loop screen** | The same engine with no VO. Callouts cycle, and the last frame matches the first scan frame so the film loops | Name → 3–5 specs → CTA | 3 s per spec, lockup 5 s | 20–30 s loop |
| **"What's inside" teardown** (repair guide, component story) | One part per shot. Deeper explode (internals flagged `internal` so they appear only when opened). The loupe mode is used for small parts | Part name → what it does → one number | 4–6 s per part | 40–60 s |
| **Before / after upgrade (v1 → v2)** | Two models in the same pad position. Scan v1, lock a part, scan-erase it top-down, scan-in the v2 part in the same place, then roll the old number to the new one | Part → old value (dim) → new value (amber) | 3 s per upgrade | 20–30 s |
| **Assembly / unboxing order** | Parts start fully exploded and snap home one by one on the bar. The target box leads each one in | Step number → part name | 1 bar (2 s) per part | 20–40 s |

The demo shows the first row. Every other row uses the same `Holo.draw` options (`scan`, `scanDown`, `explode`, `focus`, `solid`, `keep`) plus the HUD functions. Only the timeline in `film.js` changes.

**How the native moves serve information (not story):**
- **Scan growth = "this is real data."** The object is built in front of you, so it is believable before a word is said. It is also the hook: frame 1 already shows the plane at wheel height.
- **Target box lock = "look here now."** One box at a time, landing on a bar downbeat. The eye is taken to exactly one place, and the box *is* the camera: the camera follows it from part to part (the whip transition).
- **Local explode = "why the number is true."** Show the thing that makes the spec possible (the cells in the tube, the stator in the hub, the caliper halves) before the number rolls in.
- **Rolling digits = the payoff beat.** Each value is a small reveal. It locks right-to-left and turns amber on a downbeat.
- **Chip accumulation = reading time.** A spec never disappears. It docks into the left rail, name + value + detail, and stays there until the poster frame.
- **Solid hologram + beam = "the whole is ready."** It happens once only, after a true silence.
- **Controlled glitch = the power surge.** Three frames at ignition and never again.

## 3. Visual language

- **Stage**: background `hsl(hue+12, 70%, 2.4%)` with a radial lift `hsl(hue+6, 65%, 7%)` behind the subject. A 48 px dot grid fades with distance from the centre (parallax 0.2). Vignette 0.5.
- **Projector pad** (on the floor, in true perspective): rings at r = 0.7 / 1.05 (bright) / 1.12 (dashed) / 1.45 / 2.1, 120 ticks (every 10th long), 24 faint radial rays. It rotates slowly (0.12 rad/s) and spins with the turntable.
- **Wireframe**: additive (`lighter`) strokes, 1.3 px, in 7 alpha levels driven by **depth fog** (near = bright, far = 25 %). Two glow passes: ¼-res blur 3 px ×0.85 and ⅛-res blur 4 px ×0.7. Colour `hsla(hue, 100%, 50–80%, a)`.
- **Hot edges** (near-white `hsla(hue, 70%, 92%)`): the 7 cm under the scan front, pieces flagged `hot` when opened (battery cells, motor cores), the travelling light wave, and a part at the moment its hotspot pings.
- **Tubes are real CAD wireframes**: rings every few cm plus 3–6 longitudinal lines, never a single line. Wheels have a tyre (3 rings plus cross ribs), rim, spokes and hub. **Every part must be physically connected**: brackets, clamps, stays. A floating light or saddle reads as a modelling error.
- **Solid hologram**: every quad of the mesh is filled with a **screen-space Fresnel** (`0.3 + 0.7·(1 − facing)^1.6`, where facing = projected area / edge product), multiplied by an **interlace pattern** (2 px full, 2 px at 38 %) that scrolls 1 px per frame. Line width goes up ×1.5 at ignition and eases back to ×1.12. A **light wave** (±7 cm band) climbs the model at ignition and again on the chord change.
- **Beam**: the union of the pad ellipse, the top ellipse and the side trapezoid, filled once with nonzero winding (so there are no double-bright seams). Gradient 10 % → 0, 26 faint vertical rays, 70 rising dust motes.
- **Colour**: `hue` 188 (cyan) and `accent` 38 (amber) in the demo, both set in content.json. The alternate content uses 204 / 18 (blue / orange), and the whole film re-themes.
- **Type**: Rajdhani (300 for big numbers and the product name with 26 px tracking; 500/600 for labels with 2–3 px tracking; all caps) and Share Tech Mono 20–22 px for micro data (coordinates, frame counter, zoom). Numbers are laid out **monospaced digit by digit** so rolling never jitters. The decimal point is drawn as a small square, because a light-weight "." glowing reads as a comma.
- **Text never sits on the wireframe**: every text block (rail chips, the big spec card, the price column, hotspot numbers, subtitles) has its own **dark plate**: `rgba(1,8,12,.72)`, a 1 px border at 28 % and 10 px corner ticks (`plate()` in hud.js). Also move the camera so the subject clears the rail where you can. In the demo's wide loupe shot, the target sits at x 0.49 → 0.475 of the frame.
- **HUD furniture**: 46 px corner brackets 44 px from the frame edge. Side rulers tick every 24 px (every 5th long) and parallax with the camera yaw. Top-left: product // SPEC SCAN. Top-right: live status (SCANNING 042% → SCAN COMPLETE · 3 SYSTEMS → TARGET 2/3 · MOTOR → HOLO SOLID · 360° → SPEC SHEET · READY). Bottom: frame counter, scan height, camera yaw / pitch / distance.

## 4. Motion language

- **Everything runs on ones at 24 fps.** The only stepped element is glyph scrambling, which changes every frame.
- **Target box lock**: it starts 1.9× the part's rest-pose bounding box, rotated 45°, at 30 % alpha, and snaps to fit in 0.22 s (cubic ease-out). It flashes white for 3 frames on the downbeat, then the tag `TGT 0N · LOCK` appears. The box is sized from the **rest pose** (no explode offsets, no internal pieces), so it doesn't balloon when the part opens.
- **Explode**: every piece has its own vector along its assembly axis. The e-bike battery cover slides *along the down tube*, out of the way, while the cells stay in place and turn hot, so the relationship reads at a glance. The motor splits axially (cap / rotor / stator / cap) while the rotor and stator counter-rotate. The brake caliper halves part on either side of the rotor. It opens over 1 beat (long part: 2 beats) and closes over 0.5 s at the end of the segment.
- **Leader**: an anchor ring, then a diagonal to the elbow, then a horizontal to the card, drawn out over 0.5 s. The anchor pulses once when the value locks.
- **Rolling value**: characters lock right-to-left over 0.5 s (long part: 1 s) and turn amber on the downbeat, with a one-frame white flash and a full progress bar under the number. The detail line rolls in **on the same beat**.
- **Chip dock**: at the end of each segment the big card fades (0.35 s) while its chip slides into the left rail (x 140 → 110). The rail step is `min(112, 410 / (n − 1))` px, so 5 chips still fit.
- **Camera follows the box (the transition grammar)**: going from part N to part N+1, the camera interpolates over 0.5 s with a cubic ease in-out. The move starts 0.45 s *before* the next lock, still inside the previous segment. It gets **real motion blur**: 5 sub-frames averaged over a 180° shutter (1/48 s), only inside the whip window, plus faint horizontal speed streaks. Static HUD stays sharp because it doesn't move between sub-frames. There are no cuts or fades anywhere in the scene. The only other transitions are the scan plane itself (in at the start, erase top-down at the end) and the loupe iris.

## 5. Camera language

The camera orbits a target point: yaw, pitch, distance, fov 0.6, and a screen position for the target (so the subject can sit left or right of the text).

| Beat | Camera | Why |
|---|---|---|
| Hook (0–2.6 s) | 3/4 front, pitch 14°, slow **orbit** yaw 57° → 24° while it **cranes down** | From above, the scan plane reads as an ellipse, a plane that is rising. Then it drops to near eye level and leaves room for the title on the left |
| Part 1 (slow) | **Push-in** 2.85 → 1.6 (1.5 s ease-out), then drift | The first spec gets the most time. 3/4 so internals come out towards the lens |
| Part 2 | **Whip** (following the box) + **orbit** around the hub axis, yaw −11° → 46° | An axial explode only reads when you orbit around the axis |
| Part 3 (fast) | **Pull back** to full + **loupe** (frame in frame, ×4.3, its own counter-orbit) | Small parts: the wide shot shows *where*, the loupe shows *what*. Both scales are on screen at once |
| Regroup | **Pull back + crane down** to pitch 0 | A low angle makes the object stand up before the light-up |
| High point | **Turntable 360°** + **crane up** 0 → 13° + slight push | The only moment the viewer sees every side |
| Lockup | Nearly static, a slow **dolly** 3.5 → 3.4 | The viewer reads, and the frame doesn't die |
| End | **Scan-erase** top-down, then the end card | Mirrors the hook |

Framing rules: the subject is ≥ ⅓ of frame height in every key moment. Big cards live at x ≥ 1240. The rail lives at x 110–470. Subtitles are fixed at the bottom centre (baseline y 962), and the loupe stays above y 580 so the three never collide. Keep exploded pieces out of the rail (reduce explode vectors rather than let a cap fly into the text).

**Signature shot**: part 1 as one move. Lock, push, the cover slides, the cells glow, the leader pulls out, and "80 km" rolls amber.

## 6. Sound

- **Music first, 120 BPM** (1 bar = 2 s). Locks and value locks land on bar downbeats. `tools/cuecheck.py` checks every key event against `music/score.json` (all on the 1/16 grid, 0 ms offset in the demo).
- **Score** (original, numpy synthesis, D minor with Dorian colour; chords Dm9 → B♭maj7 → Fmaj9 → G6): a 16-step saw/square arpeggio with a ping-pong delay, 1–4 kHz scooped for the voice. A D1 square pulse on quarters, an 8th-note bass, synthesised hats and claps, detuned saw pads. **Density follows the info arc**: no drums on part 1, + hats on part 2, + claps and the arpeggio up an octave on part 3. Regroup **decelerates** (16ths → 8ths → one quarter gliding down). Then a **true digital silence** for one beat. **Drop** at ignition (808-style sine glide + 7-voice wide saw chord). Half-time breathing under the lockup. The arpeggio is removed note by note under the end card.
- **Silences**: (1) the half beat before the first lock, where only the room hum remains and the lock hit is the first sound after it. (2) One full beat before ignition, which is true zero, so the ignition is the loudest moment in the film.
- **Foley follows the material**: light = clean sines and FM blips *in the key* (detect blips D–F–A, amber confirm = D6 + A6 + E7). Machines = servo slides (filtered saw), pneumatic "pff", hydraulic hiss, metal tinks, a low thump + clack + two-tone beep for every lock. Number rolls tick at 24 fps.
- **Ambience**: projector hum (40/80/120 Hz), a low room tone, and after ignition a band-passed "light" noise with a slow tremolo.
- **J/L-cuts**: the motor whine starts 0.4 s before the whip lands on the motor. The hydraulic hiss starts 0.4 s before the brake lock. The hum and the chord tail carry over the scan-erase into the end card.
- **Voice**: Kokoro `af_heart`, speed 1.0: calm and confident. (`af_nicole` was tested and was too breathy and slow: 7.0 s against 4.4 s for the same line.) The music ducks −16.5 dB and the foley −15 dB under the voice, using a **held** envelope (0.5 s max-filter) so the bed doesn't pump between words. Only the first 0.2 s of lock / confirm hits escape the duck.

## 7. Subtitles & titles

- Subtitles are part of the HUD: a dark translucent plate (`rgba(1,8,12,.62)`), two diagonal cyan corner brackets and four "voiceprint" bars that move with the speech. Rajdhani Medium 38 px in near-white. Fixed at the bottom centre, with a wrap width of 1180 px.
- Timing: they appear 0.1 s before the voice, hold ≥ max(1.8 s, speech + 0.6 s) and end 0.12 s before the next line starts.
- The product title is part of the first scene (no separate title card): the name rolls in on the downbeat after the scan, then the model code and category, then the tagline. It returns in the same position in the lockup, which is also the poster.
- End card (after the lockup): film title, SCI-FI HOLOGRAM HUD, Lemo-Opuscar, LemoLab × Claude Opus 5.5, and credits, each line rolling in.

## 8. Pitfalls we hit

- **A light-weight period under glow reads as a comma** ("17,4"). Draw the decimal point as a square.
- **Scrolling a pattern with `setTransform(…, offset)` and then `destination-in`** clears everything outside the shifted rect. Use `offset % patternHeight`, or the fills vanish after the first second.
- **Target boxes sized from the live bounding box** balloon when the part explodes, or when a long piece (the brake hose) is included. Use the rest pose, skip `internal` pieces, and flag long attachments `box:false`.
- **Hotspot labels read as pointing to the wrong part** when they sit on a long diagonal leader. Put the ring on the part body and the number chip right next to the ring. Flash the part white on the ping.
- **Floating components** (the light with no bracket, the saddle with no clamp) are the first thing a viewer notices in a wireframe. Model every connector.
- **Two parallel boxes** (cover and cells both moved) don't read as an explode. Move the shell along its own axis and leave the contents in place, glowing.
- **Voice masked by foley, not music**: in-band (300–4 kHz), rolls, servos and the confirm chord were only 3 dB under the voice. Duck the foley too, and hold the duck through word gaps.
- **Detect blips inside a silence** break the silence. Run cuecheck with the silence windows.
- **The beam polygon** drawn from separate shapes gave dark wedges or double-bright seams. Fill one path with three subpaths using nonzero winding.
- **Text over wireframe** fights with the lines, even when the lines are dim. Put every text block on a plate, and still move the camera so the subject clears the rail.
- **A caliper built from two boxes doesn't read as a caliper.** You need an arc-shaped body that hugs the rotor edge, round piston faces, pads that follow the rotor curve, and vent holes on the rotor. On the explode, the pistons separate *less* than the body, so they appear to extend towards the rotor.
- **Whip written inside the next segment** only starts at that segment's first frame, so it plays as a hard cut. Start the interpolation in the previous segment. Check with a 0.1 s frame strip.
- **Floating parts in a swap model** (the drone's landing legs started outside the hull) break the same rule as the demo. Every connector gets modelled: belly mounts, fold hinges at the arm roots.
- **Scan-erase** has to clip faces as well as edges. Otherwise translucent faces linger after the lines are gone.

## 9. Production recipe (this repo)

```
styles/hologram-hud/demo/
  content.json          all text, numbers, colours, model path, voice lines   content_alt.json   the swap test (drone)
  engine/holo.js        wireframe engine (projection, scan, explode, Fresnel faces, glow, pad, scan plane, normalise, modelFromPath)
  engine/hud.js         HUD layer (target box, leader, rolling text, spec card, chip, marker, beam, subtitle, chrome, glitch)
  models/mkmodel.mjs    primitive builder (tube, ring, disc, box, saddle, fender, wheel, cells, stator, rotor, caliper…)
  models/gen_volt.mjs   the e-bike    models/gen_kite.mjs   the drone
  film.js               timeline + cameras + states (only calls the engine)    frames.js   engine demo scene (?scene=star)
  music/score.py        original score from timeline.json    mix.py   UI + mechanical foley + ambience + voice + ducking
  tools/                make_lines.mjs export.mjs cuecheck.py final_asr.py
```
1. Write the model generator (parts → pieces with explode vectors; `internal`, `hot`, `box:false`, `anchor`, `center`, `tagDir`), then `content.json`.
2. `tools/export.mjs` dumps `events.json` / `timeline.json` / subtitles. Hand `timeline.json` and the cue map to a music sub-agent while you animate.
3. Review stills (`node core/render/still.mjs <demo> t… [--q content=…]`) and 1 s contact sheets, twice, plus strips around every lock, whip, silence and ignition.
4. `sh demo/build.sh` rebuilds everything: model → TTS → whisper → export → score → cuecheck → mix → srt → render (~45 s for 936 frames with 2 workers; whip frames cost 5×) → mux (−14 LUFS, grain 0) → final whisper check.

## 10. Engine usage

The engine draws **any shape** in this style. Give it a wireframe (vertices, edges, optional quads), or build one from a 2D path with `modelFromPath`.

**`engine/holo.js`**
| Function | Purpose |
|---|---|
| `loadModel(url, {normalize=true, diag=2.3117})` | Load a model JSON, prepare typed arrays, and **normalise** it to the demo's stage size (bounding-box diagonal) so cameras work for any product |
| `prepModel(json)` / `normalizeModel(m, diag)` | The same for in-memory models |
| `modelFromPath(pts2d, {depth, id, slices, explode})` | Extrude any closed 2D path into a wireframe body with side faces |
| `makeCamera(cam, W, H)` | `{project(x,y,z,out)}` for cam `{target, yaw, pitch, dist, fov, cx, cy, roll}` |
| `new Holo(W,H).draw(ctx, model, cam, opts)` | Draw with glow. opts: `hue`, `spin` (turntable), `scan:{y,band}` (grow up to y), `scanDown:{y}` (erase down to y), `explode:{partOrPiece:0–1}`, `angle:{piece:rad}` (spin about piece.axis), `solid:0–1`, `wave:{y,w}`, `focus`+`dim`, `flash:{part:0–1}`, `keep:{piece:'#hex'}` (**the single-colour exception**: that piece keeps its own colour), `lineWidth`, `gain`, `glow`, `only`. Returns `{bbox:{part:[x0,y0,x1,y1]}, anchor:{part:[sx,sy,z]}}` |
| `drawPad(ctx, cam, W, H, {hue, rot, alpha})` / `drawScanPlane(ctx, cam, W, H, y, {hue, r, rot, alpha})` | The projector pad and the scan plane |

Model JSON: `{parts:[{id, anchor, center?, tagDir?, pieces:[{id, v:[x,y,z…], e:[a,b…], q:[a,b,c,d…], explode:[dx,dy,dz], axis?:{c,d}, internal?, hot?, box?}]}]}`.

**`engine/hud.js`**: `theme(hue, accent)`, `background`, `vignette`, `chrome`, `plate(ctx,T,x,y,w,h,a)` (dark text plate), `targetBox(ctx,T,bbox,k,{flash,tag,lockK})`, `leader(ctx,T,from,elbow,to,prog,{pulse})`, `rollText(str,k,frame)`, `monoText`, `specCard(ctx,T,x,y,{label,value,unit,detail},{reveal,roll,detail,frame,flash})`, `chip`, `marker(ctx,T,p,label,a,pulse,dir)`, `beam(ctx,T,project,a,t,{y1})`, `subtitle`, `glitch`, `fitFont`, `wrap`.

Minimal example: a warm-orange `#D97757` four-point star with a cursor tail, scanned in and then locked (`demo/frames.js`, `?scene=star`):
```js
import { Holo, modelFromPath, normalizeModel } from './engine/holo.js';
import * as U from './engine/hud.js';
const P = []; for (let i = 0; i < 8; i++) { const a = Math.PI/2 + i*Math.PI/4, r = i % 2 ? .16 : .5; P.push([Math.cos(a)*r, Math.sin(a)*r + .6]); }
const star = modelFromPath(P, { depth: .12, id: 'star' });
const tail = modelFromPath([[.62,.1],[.7,.1],[.7,.55],[.62,.55]], { depth: .06, id: 'caret' });
const m = { parts: [...star.parts, ...tail.parts] }; m.byId = Object.fromEntries(m.parts.map(p => [p.id, p])); normalizeModel(m, 1.6);
const T = U.theme(188, 38), cam = { target:[0,.55,0], yaw:.6, pitch:.18, dist:2.6, fov:.6, cx:960, cy:540 };
const info = new Holo(1920,1080).draw(ctx, m, cam, { hue: T.hue, scan: { y: .8 }, keep: { star: '#D97757' } });
U.targetBox(ctx, T, info.bbox.star, 1, { tag: 'TGT 01 · LOCK' });
```

## 11. Swap in your content

Every word, number, colour and the model come from `demo/content.json`. The code holds no copy text.

| Field | Type | Allowed | If out of range |
|---|---|---|---|
| `product` | string | 1–10 chars | Longer names still roll, but 176 px type will overflow the 410 px column: keep it short or lower the size in `titleBlock` |
| `model_code`, `category` | string | ≤ 30 chars together | Shown in mono 22 px on one line |
| `tagline` | string | ≤ 60 chars | Auto-wraps at 420 px and shrinks to 20 px |
| `model` | path | a model JSON (see §10) | Any size: it is normalised. Parts named in `callouts[].part` must exist |
| `hue`, `accent` | 0–360 | any | The whole film re-themes |
| `voice` | `{id, speed}` | a Kokoro voice | Check with whisper |
| `intro_vo`, `outro_vo`, `callouts[].vo` | string | intro ≤ 5 s spoken; part 1 ≤ 4.8 s; other parts ≤ 3.5 s | Subtitles are clamped to the next line; longer lines overlap the next lock: shorten them or raise speed |
| `*_vo_asr` / `callouts[].vo_asr` | string | optional | What whisper should hear (digits etc.) |
| `callouts[]` | array | **2–5** items: `part`, `label` (≤ 24 chars), `value` (≤ 6 chars), `unit` (≤ 4), `detail` (≤ 40, optional), `vo` | Part 1 gets 3 bars, the others 2 bars each. The timeline, music, cues and rail spacing all re-flow. More than 5 won't fit the rail |
| `footer.weight`, `footer.price` | `{label, value, unit}` | value ≤ 7 chars | Auto-fits down to 40 px |
| `footer.cta` | string | ≤ 34 chars | Auto-fits down to 14 px |
| `film_title`, `credits[]` | strings | | End card |

Parts in the model can set `tagDir: -1` so the lockup hotspot chip sits to the left of its ring.

**One command** (from the repo root; it redoes voice, whisper check, score, cue check, mix, subtitles, render and mux for the new content):
```
CONTENT=content_alt.json NAME=kite sh styles/hologram-hud/demo/build.sh
```
The outputs go to `demo/out/kite/`: `kite.mp4`, `kite.srt`, `poster.jpg`. The swap test in this repo was built exactly this way: 43 s, 4 parts, −14.0 LUFS, cue check 0 mismatches. Preview any content without building with `node core/render/still.mjs styles/hologram-hud/demo 12 --q content=<file>.json`.

**Steps for your own product**: 1) Write `models/gen_<yours>.mjs` with the primitives in `models/mkmodel.mjs` (or convert a CAD export into the format below) and run `node … > models/<yours>.json`. 2) Copy `content.json`, point `"model"` at your JSON and name your parts in `callouts[].part`. 3) Run the one command above.

**Model data format** (one JSON file, metres, **y up**, x = the product's front, z = towards the viewer's side. Any scale works, because it is normalised on load):
```json
{ "name": "VOLT CE-01",
  "parts": [                                   // part = one thing a callout can target (battery, motor, brakes…)
    { "id": "brakes",                          // referenced by content.json callouts[].part
      "anchor": [0.527, 0.416, 0.09],          // hotspot: where leader lines and the lockup ring land (ON the part's surface)
      "center": [0.524, 0.428, 0.08],          // optional: what the close-up / loupe camera looks at (defaults to anchor)
      "tagDir": -1,                            // optional: lockup number chip left (-1) or right (1) of the ring
      "pieces": [                              // piece = a rigid sub-assembly that moves on its own in the explode
        { "id": "brake-caliperA",
          "v": [x0,y0,z0, x1,y1,z1, …],        // vertices, flat
          "e": [0,1, 1,2, …],                  // edges: index pairs into v (the wireframe lines)
          "q": [0,1,5,4, …],                   // optional quads: 4 indices each (the translucent solid-hologram faces + Fresnel)
          "explode": [0, 0, 0.10],             // offset at explode = 1, along the assembly axis
          "axis": { "c": [x,y,z], "d": [0,0,1] }, // optional spin axis (rotors, fans)
          "internal": true,                    // optional: hidden until the part opens (cells, stator)
          "hot": true,                         // optional: glows near-white while open (the thing that makes the number true)
          "box": false }                       // optional: excluded from the target-box bounds (long hoses, cables)
      ] } ] }
```
Rules: every piece must physically touch its neighbour (no floating parts). Tubes are rings plus longitudinal lines, not single lines. Keep the total around 5k vertices / 6k edges for fast renders. Give the part that carries the key number a `hot` inner piece and a shell that slides *along its own axis*.

Minimal example (two parts):
```json
{ "product": "ORBIT", "model_code": "S1", "category": "Smart speaker", "tagline": "Room-filling sound.",
  "model": "models/orbit.json", "hue": 170, "accent": 40,
  "voice": { "id": "af_heart", "speed": 1.0 }, "intro_vo": "This is Orbit.",
  "callouts": [
    { "part": "driver", "label": "Woofer", "value": "4", "unit": "in", "vo": "A four inch woofer." },
    { "part": "mics", "label": "Far-field mics", "value": "6", "unit": "", "vo": "Six microphones hear you across the room." } ],
  "footer": { "weight": { "label": "Weight", "value": "1.2", "unit": "kg" }, "price": { "label": "From", "value": "199", "unit": "USD" }, "cta": "Available now" },
  "outro_vo": "Orbit. Available now.", "film_title": "Orbit · Spec Scan", "credits": ["…"] }
```
The swap test in this repo is `content_alt.json`: a four-part folding drone in blue / orange. Its stills are `demo/stills/alt_title.jpg`, `alt_signature.jpg` and `alt_lockup.jpg`.
