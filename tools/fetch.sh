#!/bin/sh
# Download large assets that are not in git, from the "assets" release on GitHub.
#   sh tools/fetch.sh voice          Kokoro TTS model → core/tts/
#   sh tools/fetch.sh instruments    sample libraries → core/audio/instruments/
#   sh tools/fetch.sh hdri           Poly Haven HDRIs → core/assets/polyhaven/
#   sh tools/fetch.sh demo <slug>    inputs to rebuild one of our demos (fonts, music, voices…)
set -e
cd "$(dirname "$0")/.."
case "$1" in
  voice|instruments|hdri) PACK="$1" ;;
  demo) [ -n "$2" ] || { echo "usage: sh tools/fetch.sh demo <slug>"; exit 1; }; PACK="demo-$2" ;;
  *) sed -n '2,7p' "$0"; exit 1 ;;
esac
python3 - "$PACK" <<'PY'
import hashlib, json, os, sys, tarfile, urllib.request
pack = sys.argv[1]
man = json.load(open('tools/assets.json'))
p = man['packs'].get(pack)
if not p: sys.exit(f"nothing to fetch for {pack}: everything it needs is already in git" if pack.startswith("demo-") else f"no pack {pack} (see tools/assets.json)")
url = f'https://github.com/{man["repo"]}/releases/download/{man["tag"]}/{p["file"]}'
tmp = os.path.join('.release', p['file'] + '.download')
os.makedirs('.release', exist_ok=True)
print(f'↓ {p["file"]} ({p["size"] / 1e6:.0f} MB)')
hs = hashlib.sha256()
with urllib.request.urlopen(url) as r, open(tmp, 'wb') as f:
    done = 0
    while chunk := r.read(1 << 20):
        f.write(chunk); hs.update(chunk); done += len(chunk)
        print(f'\r  {done / p["size"] * 100:5.1f} %', end='', flush=True)
print()
if hs.hexdigest() != p['sha256']: sys.exit('checksum mismatch, try again')
with tarfile.open(tmp) as t: t.extractall('.', filter='data')
os.remove(tmp)
# demos that keep their own copy of the TTS model use the shared one
if pack.startswith('demo-'):
    d = os.path.join('styles', pack[5:], 'demo', 'tts')
    for m in ('kokoro-v1.0.onnx', 'voices-v1.0.bin'):
        if os.path.isdir(d) and not os.path.exists(os.path.join(d, m)) and os.path.exists(os.path.join('core/tts', m)):
            os.link(os.path.join('core/tts', m), os.path.join(d, m))
print('✓ done')
PY
