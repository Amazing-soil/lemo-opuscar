#!/bin/sh
# Lemo-Opuscar skill: find or install the style library, then print its path.
#   sh setup.sh              library ready? (clone on first run, update later) → prints LIB=<path>
#   sh setup.sh deps         also install Node and Python packages and the headless browser
#   sh setup.sh demo <slug>  add one style's demo source to the library (reference only)
# The library is a sparse clone of github.com/lemomo-ai/lemo-opuscar: guides, core/ tools and
# every STYLE.md (~60 MB). Demo sources come one style at a time; big assets via tools/fetch.sh.
set -e
REPO=https://github.com/lemomo-ai/lemo-opuscar.git

# 1. Which library: $LEMO_OPUSCAR_HOME, else the clone we are standing in, else ~/lemo-opuscar
is_lib() { [ -f "$1/AGENTS.md" ] && [ -d "$1/core/render" ]; }
if [ -n "$LEMO_OPUSCAR_HOME" ]; then LIB=$LEMO_OPUSCAR_HOME
elif top=$(git rev-parse --show-toplevel 2>/dev/null) && is_lib "$top"; then LIB=$top
else LIB=$HOME/lemo-opuscar
fi
case "$LIB" in /*) ;; *) LIB=$(pwd)/$LIB ;; esac

if [ "$(git -C "$LIB" config --get lemo.managed 2>/dev/null)" = true ]; then
  # our own clone: keep it current (nothing of the user's lives in it)
  if [ -n "$(git -C "$LIB" status --porcelain --untracked-files=no 2>/dev/null)" ]; then
    echo "! $LIB has local edits, so it was not updated"
  else
    git -C "$LIB" pull --quiet --ff-only 2>/dev/null || echo "! could not update $LIB (offline?); using the local copy"
  fi
elif ! is_lib "$LIB"; then
  [ -e "$LIB" ] && [ -n "$(ls -A "$LIB" 2>/dev/null)" ] && { echo "✗ $LIB exists but is not the Lemo-Opuscar library. Set LEMO_OPUSCAR_HOME to another folder."; exit 1; }
  command -v git >/dev/null || { echo "✗ git is needed to download the library"; exit 1; }
  echo "↓ downloading the style library into $LIB"
  git clone --quiet --depth 1 --filter=blob:none --sparse "$REPO" "$LIB" || { rm -rf "$LIB"; echo "✗ download failed (offline?)"; exit 1; }
  # git < 2.35 has no --no-cone: fall back to the full checkout
  git -C "$LIB" sparse-checkout set --no-cone '/*' '!/styles/*/demo/' '!/styleboard/' 2>/dev/null \
    || git -C "$LIB" sparse-checkout disable
  git -C "$LIB" config lemo.managed true
fi
LIB=$(cd "$LIB" && pwd -P)

node_ok() { [ -f "$LIB/node_modules/.lemo-ok" ]; }
py_ok() { [ -f "$LIB/.venv/.lemo-ok" ]; }

case "$1" in
  deps)
    cd "$LIB"
    if ! node_ok; then
      npm install --no-audit --no-fund --silent
      node node_modules/playwright-core/cli.js install chromium-headless-shell   # the renderer's browser
      touch node_modules/.lemo-ok
    fi
    if ! py_ok; then
      if command -v uv >/dev/null; then uv venv --quiet --allow-existing --python 3.12 && uv pip install --quiet -r requirements.txt
      else
        python3 -c 'import sys; sys.exit(sys.version_info < (3, 11))' || { echo "✗ Python 3.11+ is needed (or install uv, which fetches it)"; exit 1; }
        python3 -m venv .venv && .venv/bin/pip install --quiet -r requirements.txt
      fi
      touch .venv/.lemo-ok
    fi
    ;;
  demo)
    [ -n "$2" ] && [ -f "$LIB/styles/$2/STYLE.md" ] || { echo "usage: sh setup.sh demo <slug>  (slugs: $LIB/styles/README.md)"; exit 1; }
    if git -C "$LIB" sparse-checkout list >/dev/null 2>&1 && [ ! -d "$LIB/styles/$2/demo" ]; then
      git -C "$LIB" sparse-checkout add "/styles/$2/demo/"
    fi
    echo "demo source: $LIB/styles/$2/demo"
    ;;
esac

# 2. Tools the pipeline needs (report only; installing them is up to the user)
miss=""
if command -v node >/dev/null; then
  [ "$(node -p 'process.versions.node.split(".")[0]')" -ge 20 ] || miss="$miss node20+(found $(node -v))"
else miss="$miss node20+"; fi
command -v ffmpeg >/dev/null || miss="$miss ffmpeg"
command -v uv >/dev/null || python3 -c 'import sys; sys.exit(sys.version_info < (3, 11))' 2>/dev/null || miss="$miss python3.11+(or uv)"
[ -n "$miss" ] && echo "! missing:$miss"
node_ok && py_ok || echo "! packages not installed yet: run 'sh setup.sh deps' (a few minutes) before the first render"
echo "LIB=$LIB"
