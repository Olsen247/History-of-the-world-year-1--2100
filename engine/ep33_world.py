"""Builds the worlds for Episode 33 (Year 1975: the Vietnam War ends) from the 1969 world (ep32_world).
1975a = 29 April 1975, before Saigon falls: Fiji (10 Oct 1970), Bangladesh (declared 26 Mar 1971, war won 16 Dec 1971),
        Bahrain (15 Aug 1971), Qatar (3 Sep 1971), United Arab Emirates (2 Dec 1971), the Bahamas (10 Jul 1973),
        Guinea-Bissau (recognised by Portugal 10 Sep 1974). Angola, Mozambique, Cape Verde, Papua New Guinea and Suriname
        only become independent later in 1975, so they keep their colonial colours. Vietnam is still split at the 17th parallel.
1975  = 30 April 1975: North Vietnam's colour takes the South (formal reunification follows on 2 July 1976).
Country shapes snap to the historical-basemaps dataset world_1960 (A. Ourednik, GPL-3.0)."""
import ep32_world as _W32
import ep26_world as _W26

D = _W32.D
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
NEW_1975 = [("FIJI", "Fiji", (110, 190, 230)), ("BAHRAIN", "Bahrain", (220, 90, 90)), ("QATAR", "Qatar", (170, 70, 110)),
            ("UNITED ARAB EMIRATES", "United Arab Emirates", (110, 180, 120)), ("BAHAMAS", "Bahamas", (90, 200, 210)),
            ("GUINEA-BISSAU", "Guinea-Bissau", (230, 190, 70))]
BANGLADESH_COL = (60, 160, 100)


def build(year=1975, stage=0):
    """stage 0 = 1975a (Vietnam still split); stage 1 = after the fall of Saigon (the North's colour covers all Vietnam)."""
    out, ov = _W32.build(1969, 0)
    for nm, dsn, col in NEW_1975:
        out.append((nm, col, D(dsn), (0, 0)))
    out.append(("BANGLADESH", BANGLADESH_COL, _W26._clip([BOX(87.5, 20.0, 93.0, 27.0)], 1960, ["Pakistan"]), (90.2, 23.9)))
    if stage == 1:
        out = [e for e in out if e[0] != "SOUTH VIETNAM"]; ov.pop("SOUTH VIETNAM", None)
        nv = [e for e in out if e[0] == "NORTH VIETNAM"][0]
        out = [e for e in out if e[0] != "NORTH VIETNAM"] + [("NORTH VIETNAM", nv[1], D("Vietnam"), (106.0, 16.0))]
    return out, ov
