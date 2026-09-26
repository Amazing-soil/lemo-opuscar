#!/bin/sh
# 把各风格 demo 的风格帧收进图鉴：styles/<slug>/demo/stills/styleframe.jpg → img/<slug>_0.jpg
cd "$(dirname "$0")"
for f in ../styles/*/demo/stills/styleframe.jpg; do
  s=$(basename "$(dirname "$(dirname "$(dirname "$f")")")")
  ffmpeg -v error -y -i "$f" -vf scale=1280:-1 -q:v 3 "img/${s}_0.jpg" && echo "$s"
done
python3 - <<'PY'
import json, glob, os
c = json.load(open('img/credits.json'))
for p in glob.glob('../styles/*/demo/stills/styleframe.jpg'):
    s = p.split('/')[2]; c[f'{s}_0.jpg'] = {'frame': True}
json.dump(c, open('img/credits.json', 'w'), ensure_ascii=False, indent=1)
PY
python3 build.py
