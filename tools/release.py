"""Maintainer tool: keep git small, put films and large assets on GitHub Releases.

  python3 tools/release.py check     what git would commit; fails on big files, local paths, secrets
  python3 tools/release.py pack      build .release/ (asset packs) and tools/assets.json (manifest)
  python3 tools/release.py upload    upload new/changed packs to release "assets" and films to release "films"

Needs the GitHub CLI (`gh auth login`) for upload. Usually run through tools/publish.sh.
"""
import hashlib, json, os, re, subprocess, sys, tarfile, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = 'lemomo-ai/lemo-opuscar'
OUT = os.path.join(ROOT, '.release')
MANIFEST = os.path.join(ROOT, 'tools', 'assets.json')
MAX_MB = 5

# Packs downloaded by tools/fetch.sh. Paths are relative to the repo root.
CORE_PACKS = {
    'voice': ['core/tts/kokoro-v1.0.onnx', 'core/tts/voices-v1.0.bin'],
    'instruments': ['core/audio/instruments'],
    'hdri': ['core/assets/polyhaven/lythwood_lounge_2k.hdr', 'core/assets/polyhaven/photo_studio_loft_hall_2k.hdr'],
}
# Ignored files that are NOT inputs of a demo: render caches, debug frames, films, internal notes, reference images we may not redistribute.
NOT_INPUT = re.compile(r'/(out[^/]*|node_modules|stems[^/]*|music_stems|chk|dbg|stills|ref|__pycache__)/|\.mp4$|\.log$|/HANDOFF\.md$|/PRODUCTION_LOG[^/]*$|/demo/tts/.*\.(onnx|bin)$|\.DS_Store$')
LOCAL_PATH = re.compile(rb'/Users/[A-Za-z0-9_.-]+/|/priv' rb'ate/tmp/|/home/[a-z0-9_-]+/')
SECRET = re.compile(rb'(sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|AIza[0-9A-Za-z_-]{30,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|xox[bp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16})')
TEXT = ('.js', '.mjs', '.cjs', '.py', '.sh', '.json', '.md', '.html', '.css', '.txt', '.yml', '.yaml', '.toml', '.srt')


def git(*a):
    """git in the repo; before `git init` a throwaway index is used so the checks work anyway."""
    if os.path.isdir(os.path.join(ROOT, '.git')):
        cmd = ['git', '-C', ROOT]
    else:
        gd = os.path.join(tempfile.gettempdir(), 'lemo-opuscar-probe.git')
        if not os.path.isdir(gd): subprocess.run(['git', 'init', '-q', '--bare', gd], check=True)
        cmd = ['git', f'--git-dir={gd}', f'--work-tree={ROOT}']
    return subprocess.run(cmd + list(a), cwd=ROOT, capture_output=True, text=True, check=True).stdout.split('\0')


def committed():
    return sorted(f for f in git('ls-files', '-z', '-co', '--exclude-standard') if f and os.path.isfile(os.path.join(ROOT, f)))


def ignored(prefix):
    return sorted(f for f in git('ls-files', '-z', '-o', '-i', '--exclude-standard', '--', prefix) if f)


def check():
    files, bad = committed(), []
    size = 0
    for f in files:
        p = os.path.join(ROOT, f)
        n = os.path.getsize(p); size += n
        if n > MAX_MB * 1e6: bad.append(f'too big ({n / 1e6:.1f} MB): {f}')
        if f.endswith(TEXT) and n < 2e6:
            b = open(p, 'rb').read()
            if LOCAL_PATH.search(b): bad.append(f'local path: {f}')
            if SECRET.search(b): bad.append(f'possible secret: {f}')
    print(f'git would hold {len(files)} files, {size / 1e6:.0f} MB')
    for b in bad: print('  ✗', b)
    if bad: sys.exit(1)
    print('  ✓ no files over %d MB, no local paths, no secrets' % MAX_MB)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()


def tar(name, paths):
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, name)
    with tarfile.open(dst + '.part', 'w') as t:
        for p in paths:
            t.add(os.path.join(ROOT, p), arcname=p, filter=lambda i: None if i.name.endswith('.DS_Store') or '__pycache__' in i.name else i)
    os.replace(dst + '.part', dst)
    return dst


def pack():
    man = {}
    for name, paths in CORE_PACKS.items():
        if all(os.path.exists(os.path.join(ROOT, p)) for p in paths):
            dst = tar(f'{name}.tar', paths); man[name] = dict(file=f'{name}.tar', size=os.path.getsize(dst), sha256=sha(dst))
            print(f'  {name}.tar  {man[name]["size"] / 1e6:.0f} MB')
    for slug in sorted(os.listdir(os.path.join(ROOT, 'styles'))):
        if not os.path.isfile(os.path.join(ROOT, 'styles', slug, 'STYLE.md')): continue
        files = [f for f in ignored(f'styles/{slug}/') if not NOT_INPUT.search(f)]
        if not files: continue
        dst = tar(f'demo-{slug}.tar', files)
        man[f'demo-{slug}'] = dict(file=f'demo-{slug}.tar', size=os.path.getsize(dst), sha256=sha(dst))
        print(f'  demo-{slug}.tar  {man[f"demo-{slug}"]["size"] / 1e6:.0f} MB')
    json.dump(dict(repo=REPO, tag='assets', packs=man), open(MANIFEST, 'w'), indent=1)
    print(f'→ {os.path.relpath(MANIFEST, ROOT)}')


def gh(*a, check=True):
    return subprocess.run(['gh', *a, '--repo', REPO], cwd=ROOT, capture_output=True, text=True, check=check)


def upload():
    state_p = os.path.join(OUT, 'uploaded.json')
    state = json.load(open(state_p)) if os.path.exists(state_p) else {}
    for tag, title in (('assets', 'Assets (fetched by tools/fetch.sh)'), ('films', 'Films (streamed by the gallery)')):
        if gh('release', 'view', tag, check=False).returncode:
            gh('release', 'create', tag, '--title', title, '--notes', 'Rolling release, updated by tools/publish.sh.', '--latest=false')
    todo = [('assets', os.path.join(OUT, p['file']), p['sha256']) for p in json.load(open(MANIFEST))['packs'].values()]
    for slug in sorted(os.listdir(os.path.join(ROOT, 'styles'))):
        mp4 = os.path.join(ROOT, 'styles', slug, slug + '.mp4')
        if os.path.isfile(mp4) and os.path.isfile(os.path.join(ROOT, 'styles', slug, 'STYLE.md')): todo.append(('films', mp4, None))   # unfinished styles stay private
    for tag, path, digest in todo:
        key = f'{tag}/{os.path.basename(path)}'
        digest = digest or sha(path)
        if state.get(key) == digest: continue
        print(f'  ↑ {key}  {os.path.getsize(path) / 1e6:.0f} MB')
        gh('release', 'upload', tag, path, '--clobber')
        state[key] = digest
        json.dump(state, open(state_p, 'w'), indent=1)
    print('  ✓ releases up to date')


if __name__ == '__main__':
    {'check': check, 'pack': pack, 'upload': upload}[sys.argv[1] if len(sys.argv) > 1 else 'check']()
