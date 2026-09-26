"""Kokoro 本地配音：python core/tts/tts.py lines.json out_dir
lines.json = [{"id":..., "text":..., "voice":"bm_george", "speed":0.92}, ...]
输出 out_dir/<id>.wav（24kHz，去首尾静音）与 out_dir/dur.json
模型：kokoro-v1.0.onnx / voices-v1.0.bin（github.com/thewh1teagle/kokoro-onnx releases）放在本目录
"""
import sys, json, os, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
HERE = os.path.dirname(os.path.abspath(__file__))
k = Kokoro(os.path.join(HERE, 'kokoro-v1.0.onnx'), os.path.join(HERE, 'voices-v1.0.bin'))
lines, out = json.load(open(sys.argv[1])), sys.argv[2]
os.makedirs(out, exist_ok=True); dur = {}
for L in lines:
    a, sr = k.create(L['text'], voice=L.get('voice', 'af_bella'), speed=L.get('speed', .92), lang=L.get('lang', 'en-us'))
    thr = np.abs(a).max() * .02; nz = np.where(np.abs(a) > thr)[0]
    a = a[max(0, nz[0] - int(.03 * sr)): nz[-1] + int(.08 * sr)]
    sf.write(os.path.join(out, L['id'] + '.wav'), a, sr); dur[L['id']] = round(len(a) / sr, 3)
    print(L['id'], dur[L['id']], L['text'])
json.dump(dur, open(os.path.join(out, 'dur.json'), 'w'), indent=1)
