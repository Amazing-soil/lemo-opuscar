"""导出字幕：python core/render/srt.py cues.json out.srt
cues.json = [{"t0": 1.2, "t1": 3.4, "text": "..."}, ...]（通常由 events.mjs 从页面的字幕时间线导出，与画面显示区间一致）
重叠的相邻字幕自动截断到下一条开始"""
import sys, json
cues = sorted(json.load(open(sys.argv[1])), key=lambda c: c['t0'])
for k in range(len(cues) - 1): cues[k]['t1'] = min(cues[k]['t1'], cues[k + 1]['t0'])
fmt = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(round(s % 1 * 1000)) % 1000:03d}"
out = '\n'.join(f"{k + 1}\n{fmt(c['t0'])} --> {fmt(c['t1'])}\n{c['text']}\n" for k, c in enumerate(cues))
open(sys.argv[2], 'w').write(out); print(sys.argv[2], len(cues), 'cues')
