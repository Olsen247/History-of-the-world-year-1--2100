"""Builds the Year 1916 world for Episode 23 from the December 1914 world (ep22_world, year 19141).
1914w -> 1916 (spring/summer 1916, before Brusilov):
- Western Front unchanged (German-occupied Belgium, Luxembourg, north-eastern France).
- Eastern Front after the Gorlice-Tarnow breakthrough and the Great Retreat (May-Sep 1915): Germany and Austria-Hungary occupy
  Russian Poland, Lithuania and Courland; front Riga - Dvinsk - Baranovichi - Pinsk - Dubno.
- Serbia (Oct-Dec 1915) and Montenegro (Jan 1916) occupied: Austria-Hungary in the north and west, Bulgaria (joined the Central
  Powers Oct 1915) in Serbian Macedonia and eastern Serbia.
- German colonies taken: Togo (Aug 1914, split Britain/France), Kiautschou (Japan, Nov 1914), German New Guinea (Australia, 1914),
  German South West Africa (South Africa, Jul 1915), Kamerun (Britain/France, Feb 1916). German East Africa still fighting.
Polygons are approximate. EXCLUSIVE = True, later entries win overlaps."""
from ep20_geo import *
import ep22_world as _W

EAST_OCC = [(21.05, 56.05), (21.0, 56.5), (21.55, 57.4), (22.6, 57.75), (23.15, 57.0), (23.8, 56.85), (24.6, 56.6), (25.5, 56.2),
            (26.4, 55.85), (26.7, 55.0), (26.7, 54.8), (26.35, 54.45), (26.2, 53.8), (25.95, 53.1), (26.0, 52.6), (26.0, 52.1),
            (25.7, 51.6), (25.5, 51.0), (25.7, 50.45), (25.4, 50.12), (24.3, 50.45), (23.4, 50.42), (22.6, 50.55), (21.8, 50.55),
            (21.0, 50.4), (19.9, 50.0), (18.9, 50.1), (18.0, 51.0), (17.3, 51.7), (17.9, 52.6), (18.6, 53.3), (19.5, 53.6),
            (20.6, 53.6), (21.6, 53.9), (22.3, 54.0), (22.4, 54.35), (22.5, 54.8), (21.8, 55.0), (21.0, 55.25), (20.9, 55.75)]
SR_NORTH = [(18.9, 45.0), (19.4, 44.9), (20.3, 44.85), (21.4, 44.8), (22.6, 44.6), (22.6, 43.6), (21.7, 43.5), (20.6, 43.1),
            (19.6, 43.3), (19.2, 44.0)]
SR_SOUTHEAST = [(21.7, 43.5), (22.6, 43.6), (22.9, 43.2), (22.5, 42.3), (23.0, 41.4), (22.6, 41.15), (21.6, 41.1), (20.75, 40.9),
                (20.5, 41.4), (20.6, 42.2), (21.3, 42.7), (21.6, 43.2)]
TOGO_BR = [(0.6, 6.9), (0.6, 8.3), (0.2, 10.0), (-0.1, 11.1), (0.9, 11.1), (0.9, 8.0), (1.0, 6.9)]
KAM_BR = [(8.6, 4.6), (9.8, 4.0), (10.6, 6.5), (12.0, 8.0), (13.5, 10.0), (14.0, 12.5), (13.4, 12.6), (12.6, 9.0), (11.0, 7.0), (9.4, 6.4)]
OCC_RED = (190, 50, 55)


def build(year=1916):
    E = _W.build(19141)
    out = []
    for n, col, polys, pos in E:
        if n in ("SERBIA", "MONTENEGRO"): continue
        if n == "GERMAN EMPIRE": polys = [p for p in polys if p is GERMANY or p is GER_EAST]
        if n == "FRENCH EMPIRE": polys = polys + [KAMERUN, GER_TOGO]
        if n == "BRITISH EMPIRE": polys = polys + [GER_SWA, GER_NG, GER_BISMARCK]
        if n == "JAPAN": polys = polys + [KIAUTSCHOU]
        out.append((n, col, polys, pos))
    by = {e[0]: e for e in E}
    out.append(("BRITISH ZONES", (235, 125, 165), [TOGO_BR, KAM_BR], (11.5, 7.5)))
    out.append(("GERMAN-OCCUPIED EAST", OCC_RED, [EAST_OCC], (23.0, 53.2)))
    out.append(("AUSTRIAN-OCCUPIED", (215, 190, 95), by["SERBIA"][2] + by["MONTENEGRO"][2] + [SR_NORTH], (20.6, 44.0)))
    out.append(("BULGARIAN-OCCUPIED", (110, 160, 90), [SR_SOUTHEAST], (21.9, 42.0)))
    return out
