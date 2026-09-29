// 整机渲染限流：同一时间最多 RENDER_SLOTS 个整片渲染（默认 3），空闲内存低于 RENDER_MIN_FREE%（默认 30）时排队等。
// video.mjs 自动调用；也可以包住任何命令：node core/render/slot.mjs -- <command…>
// 一个槽位 = 仓库根 .render_slots/ 下的一个目录，里面记着占用者的 pid；占用进程已不在的槽位会被接管。
import fs from 'fs'; import path from 'path'; import { spawn, execFileSync } from 'child_process'; import { fileURLToPath } from 'url';

const LOCKS = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../.render_slots');
const alive = pid => { try { process.kill(pid, 0); return true; } catch { return false; } };
const freePct = () => {   // macOS memory_pressure；其它系统拿不到就不设门槛
  try { return +(/free percentage:\s*(\d+)/.exec(execFileSync('memory_pressure', { encoding: 'utf8' }))?.[1] ?? 100); } catch { return 100; }
};

export async function acquire({ slots = +(process.env.RENDER_SLOTS || 3), minFree = +(process.env.RENDER_MIN_FREE || 30) } = {}) {
  fs.mkdirSync(LOCKS, { recursive: true });
  for (let waited = 0; ; waited++) {
    if (freePct() >= minFree) {
      for (let i = 0; i < slots; i++) {
        const d = path.join(LOCKS, `slot${i}`);
        try { if (!alive(+fs.readFileSync(path.join(d, 'pid'), 'utf8'))) fs.rmSync(d, { recursive: true, force: true }); } catch {}
        try {
          fs.mkdirSync(d); fs.writeFileSync(path.join(d, 'pid'), String(process.pid));
          const release = () => { try { fs.rmSync(d, { recursive: true, force: true }); } catch {} };
          process.on('exit', release);
          return release;
        } catch {}
      }
    }
    if (waited % 30 === 0) console.log(`waiting for a render slot (max ${slots}, free memory ≥ ${minFree}%)…`);
    await new Promise(r => setTimeout(r, 2000));
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const i = process.argv.indexOf('--'), cmd = i >= 0 ? process.argv.slice(i + 1) : [];
  if (!cmd.length) { console.error('usage: node core/render/slot.mjs -- <command…>'); process.exit(2); }
  const release = await acquire();
  const child = spawn(cmd[0], cmd.slice(1), { stdio: 'inherit', env: { ...process.env, RENDER_SLOT_HELD: '1' } });
  for (const sig of ['SIGINT', 'SIGTERM']) process.on(sig, () => child.kill(sig));
  child.on('exit', (code, sig) => { release(); process.exit(code ?? (sig ? 1 : 0)); });
}
