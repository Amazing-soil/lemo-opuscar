// 阅读时长自检：node core/render/readcheck.mjs styles/<slug>/demo [--q 'k=v'] [--step 0.04] [--cps 12] [--min 1.5]
// 页面提供 window.TEXTS(t) → [{id, text, x0, y0, x1, y1}]：t 秒时画面上看得见的每段文字和它的屏幕框（像素）。
// 每段文字从第一次出现起，连续完整在画框内、而且还在 TEXTS 里的时长，要 ≥ 字符数 / cps + 1 s（且 ≥ min）。
// 页面没有 TEXTS 就直接跳过。字幕条另算：它的停留由 .srt 决定。
import { openDemo, closeServer } from './page.mjs';
const args = process.argv.slice(2), opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const dir = args[0], Q = opt('--q', ''), STEP = +opt('--step', 0.04), CPS = +opt('--cps', 12), MIN = +opt('--min', 1.5);
const { browser, page } = await openDemo(dir, { q: Q });
const res = await page.evaluate(({ STEP }) => {
  if (typeof window.TEXTS !== 'function') return null;
  const W = innerWidth, H = innerHeight, seen = {};
  for (let t = 0; t <= window.DUR; t += STEP) {
    window.render(t);
    const vis = new Set();
    for (const b of window.TEXTS(t) || []) {
      if (!(b.x0 >= 0 && b.y0 >= 0 && b.x1 <= W && b.y1 <= H)) continue;
      vis.add(b.id);
      const s = seen[b.id] ??= { text: b.text, t0: t, run: 0, done: false };
      if (!s.done) s.run = t - s.t0 + STEP;
    }
    for (const id in seen) if (!vis.has(id)) seen[id].done = true;   // 只算第一次连续在画的时长
  }
  return seen;
}, { STEP });
let bad = 0;
if (!res) console.log('readcheck: page has no window.TEXTS(t); skipped');
else for (const [id, s] of Object.entries(res)) {
  const need = Math.max(MIN, s.text.length / CPS + 1), ok = s.run >= need - 1e-6;
  if (!ok) bad++;
  console.log(`${ok ? 'OK ' : 'BAD'} ${id.padEnd(18)} at ${s.t0.toFixed(2)}s  ${String(s.text.length).padStart(3)} chars  need ${need.toFixed(2)}s  got ${s.run.toFixed(2)}s`);
}
await browser.close(); closeServer();
process.exit(bad ? 1 : 0);
