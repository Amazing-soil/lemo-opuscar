// 极简静态服务器（ES module 不能走 file://）
import http from 'http'; import fs from 'fs'; import path from 'path';
const T = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '.css': 'text/css', '.jpg': 'image/jpeg', '.png': 'image/png', '.hdr': 'application/octet-stream', '.bin': 'application/octet-stream', '.gltf': 'model/gltf+json', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.svg': 'image/svg+xml', '.wav': 'audio/wav' };
// 仓库外的片子工程（skill 模式下在用户自己的文件夹里）挂在 /@film/ 下；/core/…、/styles/…、/node_modules/… 仍从仓库根取
const MOUNT = '/@film/'; let filmDir = null;
export function pageURL(root, port, dir) {
  const abs = path.resolve(dir), rel = path.relative(root, abs);
  if (rel.startsWith('..') || path.isAbsolute(rel)) { filmDir = abs; return `http://127.0.0.1:${port}${MOUNT}index.html`; }
  return `http://127.0.0.1:${port}/${rel.split(path.sep).map(encodeURIComponent).join('/')}/index.html`;
}
export function serve(root, port = 0) {
  return new Promise(res => {
    const s = http.createServer((q, r) => {
      const u = decodeURIComponent(q.url.split('?')[0]);
      const p = filmDir && u.startsWith(MOUNT) ? path.join(filmDir, u.slice(MOUNT.length)) : path.join(root, u);
      fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'Content-Type': T[path.extname(p)] || 'application/octet-stream' }); r.end(d); });
    });
    s.listen(port, '127.0.0.1', () => res({ server: s, port: s.address().port }));
  });
}
