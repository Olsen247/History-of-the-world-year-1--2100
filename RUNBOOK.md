# RUNBOOK – daily episode of «History of the World»

This repo is the production line for the YouTube Shorts series **History of the World** (channel owner: Sebastian, Norway).
A scheduled task runs every night after 03:00 Oslo time. Each run makes **exactly one new episode**, uploads it and
schedules it in Metricool. Follow every step. Speak Norwegian in anything written to the owner; the videos are in English.

## 0. Ground rules (the owner's wishes – never break these)
- Series: world history from Year 1 to 2026, one key year per episode, with the exciting events *between* the years.
  Usable in schools, but exciting. Up to **90 seconds** (aim 85–90 s).
- Write years as "Year 1405" / "In 1405". Use BCE/CE only for ranges before Year 1.
- Visual style = "geography edit" (like VeraMellua's «The Fall of the Macedonian Empire"): detailed satellite map,
  empire colours spread when they conquer and retreat or shatter when they lose. **No text boxes / fact cards.**
  Big glowing headings at the top, empire names on the map.
- Attacks: marching soldiers + arrow. **Different soldier kinds per people** (see `fx.py`: legion, han, rebel, goth,
  viking, frank, byzantine, aztec, parthian, kushan, xianbei, hun, sasanian, arab, mongol, knight, rus, timurid, serb, redturban, teutonic, polish, french; foot in fx_eras: longbow, janissary …). Add a new kind when a
  new people fights. **No crossed swords. No explosions before 1914** (see «Modern wars» below).
- Sea crossings automatically become ships (`ships=True` default); land travel = marching.
- Icons only for gold, silk/trade, fire and other truly important things (plague = rat). **No icons just because Rome
  is mentioned.**
- Important people appear as animated portrait medallions with name + short title (`fx_people.py`). Make them as
  recognisable as possible from well-known depictions (crowns, hats, beards, clothing). **Never depict the Prophet
  Muhammad.** Avoid depicting other religious founders.
- English narration via the **Speko** connector, English viral captions, original synthesized music (no copyrighted
  audio, no downloaded clips/memes/images).
- Avoid ongoing wars and current political conflicts. For modern episodes stay factual and neutral.
- Every fact must be correct. Check dates and claims with WebSearch before writing the script.

## The animation evolves through the series (owner's wish: more detail the closer we get to today)
Each era adds new layers on top of the old ones. Always use the level for the episode's year – never older, never newer.
Put `import fx as FX; FX.set_year(<YEAR>)` at the top of the episode config so ships match the era automatically
(override per march with `ship="junk"` etc.). Reference: `engine/demo_eras.py`.

| Years | Soldiers (march `kind=`) | Ships at sea | Extra layers |
|---|---|---|---|
| 1–1400 | legion, han, goth, viking, frank, byzantine, hun, arab, mongol, knight, aztec … | classic sail boat | portraits, icons |
| 1400–1550 | janissary (Ottomans), conquistador (Spain), inca, knight, aztec | carrack; **junk** for Chinese fleets (Zheng He) | dotted sea routes for explorers (`routes`), portraits |
| 1550–1700 | musketeer, janissary, conquistador | galleon | + trade routes, gold/silk icons |
| 1700–1800 | line (tricorne; coat in the nation's colour) | galleon | + `cities` lights for big capitals |
| 1795–1870 | napoleonic (shako) | galleon → steamer from 1830 | + railways from 1830: `vehicle kind="train"` (lays the track as it goes) |
| 1850–1913 | rifleman | steamer | + trains, `cities` lights grow, steamer routes |
| 1914–1945 | flag fronts (see «Modern wars»); `ww1` soldiers only if a march is needed | modern warship | + planes, airships, blasts (silent), glow sweep |
| 1945–2026 | flag fronts / plain colour chips | modern warship | + `jet` (contrail), `rocket` launch (space race), dense `cities` lights |

Effect syntax:
- `dict(type="vehicle", kind="train"|"steamer"|"jet"|"rocket"|"plane"|"airship"|"warship", path=[(lon,lat),...], t0, t1, until=…)`
  (rocket uses `path=[(lon,lat)]` as launch site and `height=` in pixels).
- `dict(type="cities", cities=[(lon, lat, weight 0.5–1.5), ...], t0, t1, until=…)` – glowing city lights.
Detail should grow gradually: early episodes stay clean; from ~1700 more labels/cities; from 1914 the full modern overlay.

## Modern wars (from about Year 1914 and later) – overlay style approved by the owner
Same satellite map as always – only the war overlay changes (`fx_modern.py`, reference: `engine/demo_ww1.py`):
- **Front lines of flags** instead of marching soldiers: `dict(type="front", path0=[...], path1=[...], t_in, t_out, move0, move1,
  side_a=["de1914"], side_b=["be","uk","fr",...], by_segment=True, rows=2)`. path0 and path1 must have the same number of points;
  the front slides from path0 to path1 between move0 and move1. Flag codes: de1914, fr, be, it, ru, ah, nl, ot, us, uk.
  **Never draw the Nazi flag or any hate symbol** – for Germany 1933–45 use a plain colour chip `"rgb:r,g,b"`.
- Conquered land turns red with a normal `gain` reveal synced with the front; a `glow` sweep (`type="glow"`) over the conquered area.
- Planes, airships and warships on dotted routes: `dict(type="vehicle", kind="plane"|"airship"|"warship", path=[...], t0, t1)`.
- Explosions: `dict(type="boom", pos, t0, swords=False, scale≈0.3–0.45)` – **no explosion sound** (fx_audio skips booms with swords=False).
- Close camera (view width ≈ 380–520) so the flags are readable. Keep event labels away from the front line.
- For modern wars stay neutral and factual; never cover ongoing wars.

## 1. Set up the session
```bash
# the repo is cloned at /home/claude/history-of-the-world-year-1--2100 (use add_repo with access "push" if needed)
bash /home/claude/history-of-the-world-year-1--2100/setup.sh      # copies engine to /home/claude/shortgen, builds terrain
```
npm/pip only work with the proxy variables cleared (setup.sh does this). Read `state.json`:
`next_episode`, `previous_year`, `previous_year_module`, `next_publish_date`, and the `plan` entry for the episode.
Build the previous year's base map: `cd /home/claude/shortgen && python3 geo.py <previous_year_module> /home/claude/shortgen/hd_<previous_year>.png`

## 2. Research and script (13 narration lines)
Research the period between `previous_year` and the new year. Pick the ~9 most exciting events. Structure:
0 **hook** – a surprising claim or stakes that make people stay, NOT "The year X." (the big heading already shows the year
from the first frame). Examples: "In just 100 years, one empire grew from the desert all the way to India." /
"One man walked to Mecca with so much gold that he crashed a whole economy." Max ~6 s.
1 **silent rewind** – no narration any more (it cost 4–5 s where viewers swipe away). Use `SILENT1.2` for this line in
mkvo; the rewind effect, ticker spin and "LET'S GO BACK TO / YEAR <previous_year>" heading still play for 1.2 s. In the
captions file give line 1 the text "".
2–11 events in chronological order (the ticker must never run backwards), 12 outro "Next time: the year <next plan year>,
when … Follow the series!".
Name the key people. Keep each line short (≈ 5–8 s spoken).
**"Meanwhile" lines (side stories in other parts of the world) must not mislead:** say the year in the narration
("Back in 212, Emperor Caracalla …") and place them in chronological order so the ticker shows that year. Never let a
person appear to rule in a year when they were already dead (a viewer caught this in Ep 3: Caracalla died in 217, not 220).

**Viewer feedback log (keep the map honest):**
- Ep 6 (Oct 2026): a viewer said "Britain was Celtic in the 700s". England was Anglo-Saxon by then, but Wales, Cornwall
  and Strathclyde were Celtic Britons, Scotland was Pictish and Gaelic (Dál Riata), and Ireland was Gaelic. For the British
  Isles c. 400–900 always label these Celtic peoples too ("Britons", "Picts", "Gaels"), not only "Anglo-Saxon kingdoms".

## 2b. Fact check before recording (viewers check our facts – take this seriously)
Before any voice is recorded, check the finished 13-line script line by line:
1. Every year, name, number and "first/biggest/last" claim is confirmed with WebSearch (two sources for anything surprising).
2. Every person is alive and in that role in the year the ticker shows during their line.
3. Words like "now", "meanwhile", "reunited", "just", "founds", "becomes" are true *for that year* – not years earlier or later.
4. Then give the script, ticker years and headings to a fresh agent (Agent tool, subagent_type "general-purpose") that has not
   seen your work, and ask it to find factual or chronology errors. Fix everything it finds before recording.
Write the result of the check in the commit message ("Fact check: 0 issues" or what was fixed).

## 3. Voice (Speko)
Call `mcp__Speko__audio_synthesize` once per line with
`{"text": LINE, "intent": {"language": "en-US", "optimizeFor": "balanced"}, "instructions": "Deep, calm, cinematic documentary narrator. Confident and slightly dramatic.", "spokenForm": true}`.
Each result is saved to a tool-results file whose name ends in `mcp-Speko-audio_synthesize-<ID>.txt`. Collect the IDs
in line order and run `TEMPO=1.13 python3 mkvo.py voN <id_hook>,SILENT1.2,<id_line2>,…,<id_line12>` (creates `voN/f*.wav` + `voN/spans.txt`).
If the last span ends after ~88.5 s, raise TEMPO (max 1.20) or shorten lines.

## 4. Map data
Write `epN_geo.py` (new polygons) and year modules `world_data_<year>.py` (and intermediate years when borders change a
lot). Copy the pattern from `ep7_geo.py`, `world_data_1279.py`, `world_data_1347.py`. Set `EXCLUSIVE = True` (later
entries win overlaps). Render each map: `python3 geo.py world_data_<year> /home/claude/shortgen/hd_<year>.png`.
Build reveal regions like `regions_ep08.py` (gain = new territory spreading from an origin; retreat + `mode="shatter"`
for collapses). Never run two heavy jobs at once (7 GB RAM).

## 5. Episode config
Write `epNN.py` modelled on `ep08.py` / `ep07.py`: camera shots per line (view width 900–2000 for close-ups, 2950 wide),
base_switches (switch maps during camera moves), reveals, labels (avoid clutter; event labels in gold), ticker,
**peoples of the whole world** – the map must never look as if only the big empires existed (viewer feedback Ep 6).
Always add `import world_peoples as WP` and `labels += WP.labels(B, <YEAR>, s[1] + 0.8, s[12])` just before `CFG = dict(`
(B = the year module on the map). It adds small culture labels (Celtic Britons, Picts, Bantu peoples, Maya city-states,
Aboriginal Australians, Inuit, Polynesians …) wherever no empire polygon covers that spot. When the episode's period is
missing a people that should be there, ADD it to `engine/world_peoples.py` (name, lon, lat, start, end – check the dates)
and commit it, so the list grows with the series. Then headings (2 lines; avoid the letter Q in headings – the font renders it oddly; the first heading starts at `t0=0.15` so the
year and a punchy title are on screen from the very first frame, and the first flash is at 0.15), fx (marches, icons, persons with
`screen=(780,1180)` or `(300,1180)` – never lower than y=1250, the captions sit below), outro with next episode. Render preview stills:
`python3 epNN.py stills 4,15,25,… /tmp/sN.png` and **look at them** (Read the png). Fix overlaps (also small labels like SERBIA vs OTTOMAN EMPIRE – drop or move the smaller one), empty frames, wrong maps.

## 6. Captions and audio
- Captions: copy `mkcaps8.py` to `mkcapsN.py`, put the 13 lines with colour markers (`word|y`, `|r`, `|c`, `|p`, `|g`;
  `_` joins words) → `python3 mkcapsN.py captions_epNN.txt /tmp/narr.txt`.
- Music + voice: `python3 audio_gen.py voN audio_epNN_vo.wav <DUR> <seed> "<rumble list>" "<fire times>"`
  then `python3 fx_audio.py epNN audio_epNN_vo.wav audio_epNN_fx.wav`.

## 7. Render
```bash
python3 epNN.py video epNN_clean.mp4 audio_epNN_fx.wav            # ~40–60 min, run in background
python3 caption_burn.py epNN_clean.mp4 captions_epNN.txt /home/claude/history_epNN_year<YEAR>.mp4 0.80
```
Then add the "comment below" ending (owner's wish – viewers are asked for their opinion after "Follow the series!"):
```bash
python3 make_tail.py /home/claude/history_epNN_year<YEAR>.mp4 /home/claude/history_epNN_year<YEAR>_final.mp4 /home/claude/shortgen/outro_comment_vo.wav
```
It adds ~4 s: narrator says "And tell me in the comments: what's missing, and what could be better?" with on-screen text.
Use the `_final.mp4` file in step 8. Check duration (main part ≤ ~89 s, final ≤ ~94 s) and look at 8–10 frames spread over the video.

## 8. Upload and schedule
```bash
cd /home/claude/history-of-the-world-year-1--2100
ffmpeg -i /home/claude/history_epNN_year<YEAR>_final.mp4 -c:v libx264 -preset slow -crf 20 -maxrate 4500k -bufsize 9000k -c:a copy -movflags +faststart videos/epNN_year<YEAR>.mp4
git add videos engine && git commit -m "Episode NN – Year <YEAR>" && git push
```
Public URL: `https://raw.githubusercontent.com/Olsen247/History-of-the-world-year-1--2100/main/videos/epNN_year<YEAR>.mp4`
Schedule with `mcp__Metricool_Social_Media_Management__createScheduledPost` (blogId `7508489`) on `next_publish_date`
at `next_publish_time` Europe/Oslo (publishing plan: **Mon–Sat one episode at 10:00, Sunday two episodes at 10:00 and 11:00**): providers `[{"network":"youtube"}, {"network":"instagram"}]` (Instagram account @atlasofagesx, posted as a Reel at the same time),
`"instagramData": {"type": "REEL", "showReelOnFeed": true, "isAiGenerated": false}`,
`"firstCommentText"`: one short question that invites answers about this episode (e.g. "Who was the bigger conqueror: Timur or Genghis Khan? 👇" / "What should we cover in more detail?"), youtubeData
`{"title": "History of the World Ep NN", "type": "short", "privacy": "public", "category": "EDUCATION", "madeForKids": false, "isAiGeneratedContent": false, "tags": [...]}`,
text = "History of the World Ep NN <emoji>\nYear <YEAR> – <topic>. <one or two sentence summary>\nEpisode NN of History of the World, from Year 1 to 2026.\n#history #geography #shorts …".
Before scheduling, call getScheduledPosts for that date so you never double-book a slot.

## 8b. Daily quick-fact clip (extra reach, but the series stays tidy)
Every run also makes ONE short clip (15–30 s) from an episode that is **already published** (episode `next_episode − 4`,
skip if it does not exist or is already in `clips_done` in state.json).
1. Pick the most surprising/shareable 1–2 narration lines of that episode (gold, a famous battle, a "first", a shocking
   number). Get their times from the captions script that matches the video you cut: `videos/epNN_year<YEAR>_v3.mp4` ↔ `engine/mkcapsN_v3.py`;
   otherwise the newest `epNN_year<YEAR>[_v2].mp4` ↔ `engine/mkcapsN.py` (v2 only added an ending, timings unchanged).
2. `python3 make_clip.py videos/epNN_year<YEAR>[_vX].mp4 <start−0.2> <end+0.4> NN /home/claude/clip_epNN.mp4`
   (adds a 2.6 s end card "FULL STORY – HISTORY OF THE WORLD – EPISODE NN").
3. Commit to `videos/clips/`, schedule at **17:00** on `next_publish_date` (Sunday too, one clip only),
   providers youtube + instagram. Keep it tidy so the main series is easy to follow:
   - YouTube title: "<short fact headline> 🗺️ | History of the World" – never "Ep N" (that title belongs to full episodes only).
   - Text: "<one-sentence fact>\nFull story: Episode NN of History of the World – watch the whole series from Year 1 on the channel.\n#history #shorts …"
   - Instagram: `"instagramData": {"type": "REEL", "showReelOnFeed": false, …}` so clips live in the Reels tab only and the
     profile grid shows just the numbered episodes.
4. Append `{"from_ep": NN, "start": …, "end": …, "date": …}` to `clips_done` in state.json.

## 9. Save state
Copy every new engine file into `engine/`, update `state.json` (next_episode+1, previous_year, previous_year_module,
previous_base_map, next publish slot, append to `done`). Next slot: if the slot just used was a **Sunday 10:00**, the next slot is the
same Sunday at **11:00**; otherwise it is the next day at **10:00**.
**Two episodes on one night:** if the next slot is a Sunday 11:00 slot, go back to step 2 and make one more episode in the same run
(so the Sunday gets both its episodes, and production keeps up with 8 episodes a week), append the title/description to `docs/upload_tekster.md`,
commit and push. Finish with a short Norwegian summary: episode, publish date, anything that went wrong.

If something fails that you cannot fix (Speko, Metricool, push), do NOT publish a broken video. Commit what you have,
leave state.json unchanged and report the problem in Norwegian.
