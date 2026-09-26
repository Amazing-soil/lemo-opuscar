// 导出音效事件：node core/render/events.mjs styles/<slug>/demo → <dir>/events.json
import fs from 'fs'; import path from 'path';
import { openDemo, closeServer } from './page.mjs';
const dir = process.argv[2];
const { browser, page } = await openDemo(dir);
const ev = await page.evaluate(() => ({ dur: window.DUR, ev: window.EV || [] }));
fs.writeFileSync(path.join(dir, 'events.json'), JSON.stringify(ev, null, 0));
console.log('events', ev.ev.length, 'dur', ev.dur);
await browser.close(); closeServer();
