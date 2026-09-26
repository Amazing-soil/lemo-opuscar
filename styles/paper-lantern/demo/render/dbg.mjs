import fs from 'fs';
import path from 'path';
import { openPage, closeServer, ROOT } from './page.mjs';
const { browser, page } = await openPage();
const r = await page.evaluate(async () => {
  const P = await import(new URL('src/paper.js', location.href).href); const T = await import(new URL('src/shots/s10_pass.js', location.href).href);
  const c = P.finish(P.paint(.11 * 1.45 * 2, .13, x => T.carriage(x, 2, .11 * 1.45, .05 * 1.45, '#1f5140', false), 2000));
  return c.toDataURL('image/png');
});
fs.mkdirSync(path.join(ROOT, 'stills/dbg'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'stills/dbg/carriage.png'), Buffer.from(r.split(',')[1], 'base64'));
await browser.close(); closeServer();
