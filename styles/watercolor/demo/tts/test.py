# 声线试听（选定 af_heart）
import soundfile as sf, time, os
from kokoro_onnx import Kokoro
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
CORE = os.path.join(HERE, '..', '..', '..', '..', 'core', 'tts')
k = Kokoro(os.path.join(CORE, "kokoro-v1.0.onnx"), os.path.join(CORE, "voices-v1.0.bin"))
txt = "Australia begins with a single line. At its heart, the red centre, where less than two hundred and fifty millimetres of rain falls in a year."
for v in ["af_heart", "bf_emma", "bm_george", "af_bella"]:
    t=time.time(); s, sr = k.create(txt, voice=v, speed=0.95, lang="en-us" if v[0]=='a' else "en-gb")
    sf.write(f"test_{v}.wav", s, sr); print(v, sr, len(s)/sr, round(time.time()-t,1))
