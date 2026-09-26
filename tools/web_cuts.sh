#!/bin/sh
# 720p web cuts for the gallery (served by GitHub Pages as video/mp4, which Safari needs)
cd "$(dirname "$0")/.."
mkdir -p .release/web
for f in styles/*/STYLE.md; do
  s=$(basename "$(dirname "$f")"); src=styles/$s/$s.mp4; out=.release/web/$s.mp4
  [ -f "$src" ] || continue; [ -f "$out" ] && continue
  ffmpeg -v error -y -i "$src" -vf "scale=-2:720:flags=lanczos" -c:v libx264 -preset slow -crf 24 -maxrate 2M -bufsize 4M -pix_fmt yuv420p \
    -c:a aac -b:a 128k -movflags +faststart "$out.part.mp4" && mv "$out.part.mp4" "$out" && echo "$s $(du -h "$out" | cut -f1)"
done
du -sh .release/web
