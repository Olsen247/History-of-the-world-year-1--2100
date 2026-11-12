#!/bin/bash
# Bootstraps a fresh cloud session so the History of the World engine runs.
set -e
REPO=$(cd "$(dirname "$0")" && pwd)
mkdir -p /home/claude/shortgen /home/claude/geo
cp -r "$REPO"/engine/* /home/claude/shortgen/
# map data (npm/pip need the proxy env cleared, see RUNBOOK)
cd /home/claude/geo
[ -f node_modules/world-atlas/land-50m.json ] || (NO_PROXY= no_proxy= npm_config_noproxy= npm init -y >/dev/null && NO_PROXY= no_proxy= npm_config_noproxy= npm install world-atlas@2.0.2 >/dev/null)
python3 -c "import shapely" 2>/dev/null || NO_PROXY= no_proxy= pip install --break-system-packages shapely >/dev/null   # ep26_world.py clips occupation zones
python3 -c "import mpl_toolkits.basemap_data" 2>/dev/null || NO_PROXY= no_proxy= pip install --break-system-packages basemap-data==2.0.0 >/dev/null
BMD=$(python3 -c "import mpl_toolkits.basemap_data as b; print(list(b.__path__)[0])")
sed -i "s|^BMD = .*|BMD = \"$BMD/\"|" /home/claude/shortgen/geo.py
ls /usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf /usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf >/dev/null || \
  (apt-get install -y fonts-inter fonts-crosextra-caladea >/dev/null 2>&1 || echo "FONTS MISSING")
# real historical borders (historical-basemaps by A. Ourednik, GPL-3.0) used by hb_snap.py
if [ ! -f /home/claude/shortgen/hb/world_1900.geojson ]; then
  rm -rf /tmp/hb_src && git clone -q --depth 1 https://github.com/aourednik/historical-basemaps.git /tmp/hb_src
  mkdir -p /home/claude/shortgen/hb && cp /tmp/hb_src/geojson/world_*.geojson /home/claude/shortgen/hb/ && cp /tmp/hb_src/LICENSE /home/claude/shortgen/hb/LICENSE_historical-basemaps
fi
cd /home/claude/shortgen
# full-resolution terrain + land mask (takes a few minutes, needs ~3 GB RAM)
[ -f hd_terrain.png ] || python3 -c "import geo; t,l=geo.build_terrain(); t.save('hd_terrain.png'); l.save('hd_land.png')"
echo "setup ok"
