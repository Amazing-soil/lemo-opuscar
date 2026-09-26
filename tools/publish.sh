#!/bin/sh
# Publish local changes: refresh the gallery data, check the repo, upload films and asset packs.
# After it passes: git add -A && git commit -m "…" && git push   (the gallery on GitHub Pages rebuilds itself)
set -e
cd "$(dirname "$0")/.."
python3 styleboard/build.py
sh tools/web_cuts.sh
python3 tools/release.py check
python3 tools/release.py pack
python3 tools/release.py upload
echo
git status --short 2>/dev/null | head -30 || true
echo "Ready: git add -A && git commit && git push"
