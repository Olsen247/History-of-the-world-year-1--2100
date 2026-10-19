import json,base64,subprocess,sys,wave
import glob as _g
TR=None
out=sys.argv[1]; ids=sys.argv[2].split(',')
t=0.3; spans=[]
for i,idd in enumerate(ids,1):
    _f=_g.glob('/root/.claude/projects/*/*/tool-results/mcp-Speko-audio_synthesize-%s.txt'%idd)+_g.glob('/root/.claude/projects/*/tool-results/mcp-Speko-audio_synthesize-%s.txt'%idd)
    d=json.load(open(_f[0])); open(f"{out}/seg{i}.wav","wb").write(base64.b64decode(d['audio_base64']))
    subprocess.run(["ffmpeg","-v","error","-y","-i",f"{out}/seg{i}.wav","-af","silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo="+__import__("os").environ.get("TEMPO","1.11"),"-ar","44100","-ac","1",f"{out}/f{i}.wav"],check=True)
    w=wave.open(f"{out}/f{i}.wav"); dur=w.getnframes()/44100
    spans.append((round(t,2),round(t+dur,2))); print(i,d['duration_seconds'],round(dur,2))
    t+=dur+(0.5 if i in (1,) else 0.4)
open(f"{out}/spans.txt","w").write(repr(spans)); print(spans[-1][1])
