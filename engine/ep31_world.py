"""Builds the worlds for Episode 31 (Year 1960: decolonisation of Africa and Asia) from the 1953 world (ep30_world).
1957 = end of 1957: Indochina split by the Geneva Accords (July 1954) – North Vietnam, South Vietnam (17th parallel), Laos, Cambodia;
       Sudan (1 Jan 1956), Morocco (2 Mar 1956), Tunisia (20 Mar 1956), Ghana (6 Mar 1957), Malaya (31 Aug 1957).
       Algeria is still French (until 1962).
1960 = end of 1960: Guinea (2 Oct 1958) and the 17 African states of 1960 – Cameroon, Togo, Madagascar, Congo (Leopoldville),
       Somalia, Dahomey, Niger, Upper Volta, Ivory Coast, Chad, Central African Republic, Congo (Brazzaville), Gabon, Senegal,
       Mali, Nigeria, Mauritania – plus Cyprus (16 Aug 1960).
1960k = 1960 with the Katanga secession (11 July 1960) as an overlay on the Congo.
Country shapes snap to the historical-basemaps dataset world_1960 (A. Ourednik, GPL-3.0)."""
import ep30_world as _W30
import ep26_world as _W26

_ds = _W26._ds
BOX = lambda a, b, c, d: [(a, b), (c, b), (c, d), (a, d)]
D = lambda nm: _ds(1960, nm)

# new states: (map name, dataset name, colour, label anchor or (0, 0))
NEW_1957 = [("NORTH VIETNAM", "Vietnam", (230, 125, 60), (105.3, 21.0)), ("LAOS", "Laos", (110, 170, 200), (0, 0)),
            ("CAMBODIA", "Cambodia", (120, 190, 130), (0, 0)), ("SUDAN", "Sudan", (175, 115, 70), (30.0, 15.0)),
            ("MOROCCO", "Morocco", (200, 90, 80), (-6.5, 32.0)), ("TUNISIA", "Tunisia", (230, 120, 110), (0, 0)),
            ("GHANA", "Ghana", (240, 200, 60), (0, 0))]
NEW_1960 = [("GUINEA", "Guinea", (230, 90, 90)), ("CAMEROON", "Cameroon", (225, 105, 105)), ("TOGO", "Togo", (230, 100, 150)),
            ("MADAGASCAR", "Madagascar", (220, 120, 140)), ("CONGO", "Zaire", (90, 170, 220)), ("SOMALIA", "Somalia", (120, 190, 230)),
            ("DAHOMEY", "Benin", (200, 120, 190)), ("NIGER", "Niger", (230, 160, 70)), ("UPPER VOLTA", "Burkina Faso", (150, 200, 110)),
            ("IVORY COAST", "Ivory Coast", (240, 140, 60)), ("CHAD", "Chad", (110, 140, 210)),
            ("CENTRAL AFRICAN REPUBLIC", "Central African Republic", (190, 160, 230)), ("CONGO-BRAZZAVILLE", "Congo", (100, 190, 150)),
            ("GABON", "Gabon", (220, 210, 90)), ("SENEGAL", "Senegal", (90, 160, 215)), ("MALI", "Mali", (230, 200, 120)),
            ("NIGERIA", "Nigeria", (90, 175, 95)), ("MAURITANIA", "Mauritania", (170, 200, 130)), ("CYPRUS", "Cyprus", (230, 170, 80))]
# Katanga (rough outline of the province, clipped to the Congo)
KATANGA = [(21.8, -7.2), (23.0, -6.6), (24.5, -6.0), (26.0, -5.5), (27.6, -5.0), (29.2, -5.6), (30.8, -8.0), (30.8, -14.0), (21.8, -14.0)]


def build(year, stage=0):
    """year: 1957 or 1960; stage 1 (1960 only) adds the Katanga secession."""
    out, ov = _W30.build(1953, 0)
    out = [e for e in out if e[0] != "SAAR"]; ov.pop("SAAR", None)      # the Saar rejoined West Germany on 1 Jan 1957
    def add(name, col, polys, pos=(0, 0), victims="-"):
        out.append((name, col, polys, pos))
        if victims != "-": ov[name] = victims
    for nm, dsn, col, pos in NEW_1957:
        add(nm, col, D(dsn), pos)
    add("SOUTH VIETNAM", (235, 200, 80), _W26._clip([BOX(100.0, 7.0, 110.0, 17.0)], 1960, ["Vietnam"]), (106.5, 13.0),
        victims=["NORTH VIETNAM"])
    add("MALAYA", (90, 120, 210), _W26._clip([BOX(99.0, 0.8, 105.0, 7.0)], 1960, ["Malaysia"]), (102.0, 4.0))
    if year >= 1960:
        for nm, dsn, col in NEW_1960:
            add(nm, col, D(dsn))
    if year >= 1960 and stage == 1:
        add("KATANGA", (240, 150, 60), _W26._clip([KATANGA], 1960, ["Zaire"]), victims=["CONGO"])
    return out, ov
