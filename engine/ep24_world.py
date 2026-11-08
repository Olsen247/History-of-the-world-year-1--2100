"""Builds the worlds for Episode 24 (Year 1918) from the Year 1916 world (ep23_world).
1917  = spring 1917: Central Powers occupy Wallachia and Dobruja (Dec 1916 - Jan 1917, front on the Siret); Britain holds
        Mesopotamia up to Baghdad/Samarra (Baghdad 11 Mar 1917); the Arab Revolt holds the Hejaz coast (Mecca, Jeddah, Wejh –
        Medina stays Ottoman until 1919); German East Africa is almost all occupied by British/Belgian forces.
1918  = mid-1918: + Aqaba (6 Jul 1917) and the Arab north of the Hejaz; Britain in southern Palestine (Jerusalem 9 Dec 1917,
        line Arsuf - Jordan); Austro-German occupation of Venetia to the Piave (Caporetto, Oct-Nov 1917); Russia is Soviet
        Russia; Finland independent (6 Dec 1917); after Brest-Litovsk (3 Mar 1918) and Operation Faustschlag Germany and
        Austria-Hungary occupy Estonia, Latvia, Belarus to the Narva-Pskov-Orsha-Mogilev line and Ukraine incl. Crimea and Rostov;
        Bessarabia joins Romania (Apr 1918).
1918n = 11 November 1918: German occupation in the west shrunk to the armistice line (Terneuzen - Ghent - Mons - Sedan);
        Palestine, Lebanon and Syria taken by British and Arab forces (Damascus 1 Oct, Aleppo 25 Oct); Serbia and Montenegro
        liberated; Venetia freed (Vittorio Veneto).
Polygons are approximate. EXCLUSIVE = True, later entries win overlaps; occupations are OVERLAY entries on the victim's land."""
from ep20_geo import *
import ep22_world as _W22
import ep23_world as _W

OCC_RED = (190, 50, 55)
ARAB = (70, 145, 75)
BRC = (235, 125, 165)
WALLACHIA = [(22.4, 44.5), (22.7, 44.95), (23.5, 45.3), (24.5, 45.5), (25.5, 45.6), (26.3, 45.85), (27.0, 45.75), (27.4, 45.45), (28.0, 45.42),
             (28.3, 45.4), (29.7, 45.25), (29.7, 44.8), (28.7, 44.0), (28.6, 43.72), (27.5, 44.1), (26.5, 44.05), (25.4, 43.62), (24.3, 43.68),
             (23.0, 43.78), (22.5, 44.2)]
MESOPOTAMIA = [(47.9, 30.0), (48.6, 29.9), (48.0, 31.0), (47.7, 32.0), (46.5, 33.0), (45.6, 33.9), (44.6, 34.35), (43.9, 34.25), (43.6, 33.4),
               (44.0, 32.4), (45.2, 31.2), (46.4, 30.3), (47.2, 29.9)]
HEJAZ_ARAB = [(36.2, 26.4), (37.2, 26.2), (38.0, 24.9), (38.9, 24.0), (39.3, 23.4), (40.6, 21.8), (41.2, 20.6), (41.6, 19.6), (40.8, 19.2),
              (39.9, 20.3), (39.0, 21.4), (38.6, 22.6), (37.6, 24.0), (36.6, 25.3)]
AQABA_ARAB = [(34.95, 29.55), (35.4, 30.2), (36.0, 30.3), (36.6, 29.6), (37.0, 28.4), (37.3, 27.2), (37.2, 26.2), (36.2, 26.4), (35.6, 27.4),
              (34.8, 28.2)]
PALESTINE = [(34.2, 31.3), (34.85, 32.2), (35.2, 32.1), (35.55, 32.0), (35.55, 31.75), (35.45, 31.2), (35.2, 30.6), (34.95, 29.55), (34.25, 31.25)]
VENETIA = [(12.55, 45.5), (12.3, 45.75), (11.85, 45.85), (11.6, 45.95), (11.75, 46.3), (12.4, 46.65), (13.4, 46.55), (13.65, 46.2), (13.6, 45.8),
           (13.1, 45.65)]
FINLAND = [(21.0, 60.4), (21.4, 61.6), (21.2, 63.0), (22.5, 63.9), (24.5, 64.9), (25.4, 65.3), (24.2, 65.8), (23.6, 66.6), (23.9, 67.9),
           (21.0, 69.0), (22.5, 69.1), (25.7, 69.0), (28.6, 68.9), (28.8, 68.4), (29.8, 67.6), (30.0, 66.5), (29.6, 65.0), (30.5, 64.0),
           (31.5, 63.0), (31.0, 62.0), (29.5, 61.2), (28.0, 60.5), (26.0, 60.3), (23.0, 59.75)]
EAST_1918 = [(22.0, 58.5), (23.4, 59.3), (25.0, 59.6), (28.0, 59.45), (28.2, 59.1), (27.8, 58.3), (28.3, 57.8), (28.7, 57.2), (29.6, 56.3),
             (30.2, 55.4), (30.6, 54.6), (30.6, 53.9), (30.9, 53.0), (31.3, 52.3), (32.3, 52.2), (33.6, 52.4), (34.4, 51.8), (35.4, 51.2),
             (36.4, 50.5), (37.8, 50.1), (39.5, 49.7), (40.1, 48.9), (39.9, 47.9), (39.75, 47.25), (38.6, 47.1), (37.4, 46.95), (35.8, 46.6),
             (35.3, 45.9), (36.7, 45.4), (35.4, 44.95), (34.0, 44.35), (33.3, 44.55), (32.4, 45.4), (33.6, 46.0), (32.2, 46.5), (30.8, 46.55),
             (30.1, 45.9), (28.6, 48.2), (26.6, 48.35), (26.1, 48.6), (26.0, 49.5), (25.4, 50.12), (25.7, 50.45), (25.5, 51.0), (25.7, 51.6),
             (26.0, 52.1), (26.0, 52.6), (25.95, 53.1), (26.2, 53.8), (26.35, 54.45), (26.7, 54.8), (26.7, 55.0), (26.4, 55.85), (25.5, 56.2),
             (24.6, 56.6), (23.8, 56.85), (23.15, 57.0), (22.6, 57.75)]
BESSARABIA = [(26.6, 48.3), (27.8, 48.5), (28.5, 48.15), (29.2, 47.9), (29.6, 47.4), (30.1, 46.6), (29.7, 45.6), (28.2, 45.45), (28.1, 46.5),
              (27.4, 47.5)]
OCC_N = [(3.8, 51.32), (3.72, 51.05), (3.85, 50.7), (3.95, 50.45), (4.1, 50.2), (4.5, 49.95), (4.95, 49.7), (5.2, 49.45), (5.45, 49.5),
         (5.9, 49.45), (6.4, 49.45), (6.4, 50.3), (6.0, 50.75), (5.8, 51.15), (5.2, 51.3), (4.5, 51.45)]
LEVANT_BR = [(34.2, 31.3), (34.85, 32.2), (35.0, 33.0), (35.5, 34.0), (35.9, 35.0), (35.8, 35.9), (36.2, 36.1), (36.6, 36.2), (36.5, 35.3),
             (36.4, 34.4), (36.0, 33.5), (35.9, 32.7), (35.55, 32.0), (35.55, 31.75), (35.45, 31.2), (35.2, 30.6), (34.95, 29.55)]
SYRIA_ARAB = [(35.55, 31.2), (35.55, 32.0), (35.9, 32.7), (36.0, 33.5), (36.4, 34.4), (36.5, 35.3), (36.6, 36.2), (37.5, 36.4), (38.0, 35.8),
              (38.6, 34.5), (38.8, 33.0), (38.0, 31.8), (37.0, 30.6), (36.6, 29.6), (36.0, 30.3), (35.4, 30.2), (35.2, 30.6)]


def build(year):
    """year: 1917 (spring 1917), 1918 (mid-1918), 19181 (11 November 1918)."""
    E = _W.build(1916)
    by22 = {e[0]: e for e in _W22.build(19141)}
    late = year >= 1918
    out = []
    for n, col, polys, pos in E:
        if n == "GERMAN EMPIRE": polys = [p for p in polys if p is not GER_EAST]
        if n == "BRITISH EMPIRE": polys = polys + [GER_EAST]
        if n == "RUSSIAN EMPIRE" and late: n = "SOVIET RUSSIA"
        if year == 19181:
            if n in ("AUSTRIAN-OCCUPIED", "BULGARIAN-OCCUPIED"): continue
            if n == "GERMAN-OCCUPIED": polys = [OCC_N]
        out.append((n, col, polys, pos))
    if year == 19181:
        out.append(by22["SERBIA"]); out.append(by22["MONTENEGRO"])
    out.append(("OCCUPIED ROMANIA", OCC_RED, [WALLACHIA], (25.6, 44.6)))
    out.append(("BRITISH MESOPOTAMIA", BRC, [MESOPOTAMIA], (45.5, 32.2)))
    arab = [HEJAZ_ARAB] + ([AQABA_ARAB] if late else []) + ([SYRIA_ARAB] if year == 19181 else [])
    out.append(("ARAB REVOLT", ARAB, arab, (38.5, 23.5)))
    if late:
        out.append(("BRITISH PALESTINE", BRC, [LEVANT_BR] if year == 19181 else [PALESTINE], (34.9, 31.6)))
        if year == 1918: out.append(("OCCUPIED VENETIA", (215, 190, 95), [VENETIA], (12.7, 46.1)))
        out.append(("FINLAND", (215, 225, 240), [FINLAND], (26.0, 63.0)))
        out.append(("OCCUPIED EAST 1918", OCC_RED, [EAST_1918], (31.0, 49.5)))
        out.append(("BESSARABIA", (220, 190, 80), [BESSARABIA], (28.6, 47.0)))
    return out


def overlay(year):
    late = year >= 1918
    ru = "SOVIET RUSSIA" if late else "RUSSIAN EMPIRE"
    ov = {"GERMAN-OCCUPIED": None, "GERMAN-OCCUPIED EAST": [ru], "BRITISH ZONES": None,
          "OCCUPIED ROMANIA": ["ROMANIA"], "BRITISH MESOPOTAMIA": ["OTTOMAN EMPIRE"], "ARAB REVOLT": ["OTTOMAN EMPIRE"]}
    if year != 19181: ov.update({"AUSTRIAN-OCCUPIED": None, "BULGARIAN-OCCUPIED": None})
    if late:
        ov.update({"BRITISH PALESTINE": ["OTTOMAN EMPIRE"], "FINLAND": [ru], "OCCUPIED EAST 1918": [ru], "BESSARABIA": [ru]})
        if year == 1918: ov["OCCUPIED VENETIA"] = ["ITALY"]
    return ov
