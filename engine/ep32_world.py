"""Builds the world for Episode 32 (Year 1969: the space race and the Moon landing; the Vietnam War escalates) from the
1960 world (ep31_world, without the Katanga secession, which ended in January 1963).
1969 = mid-1969: the states that won independence 1961-68 – Sierra Leone (27 Apr 1961), Kuwait (19 Jun 1961), Tanganyika
       (9 Dec 1961; with Zanzibar = Tanzania, 26 Apr 1964), Algeria (5 Jul 1962), Rwanda and Burundi (1 Jul 1962), Jamaica (6 Aug 1962),
       Trinidad and Tobago (31 Aug 1962), Uganda (9 Oct 1962), Kenya (12 Dec 1963), Malawi (6 Jul 1964), Zambia (24 Oct 1964),
       The Gambia (18 Feb 1965), Guyana (26 May 1966), Botswana (30 Sep 1966), Lesotho (4 Oct 1966), Swaziland (6 Sep 1968),
       Equatorial Guinea (12 Oct 1968). Rhodesia's UDI (1965) was not recognised, so it stays in the British colour.
Country shapes snap to the historical-basemaps dataset world_1960 (A. Ourednik, GPL-3.0)."""
import ep31_world as _W31

D = _W31.D
NEW_1969 = [("SIERRA LEONE", "Sierra Leone", (120, 200, 160)), ("KUWAIT", "Kuwait", (120, 190, 120)),
            ("TANZANIA", "Tanzania, United Republic of", (90, 180, 200)), ("ALGERIA", "Algeria", (70, 160, 95)),
            ("RWANDA", "Rwanda", (220, 120, 90)), ("BURUNDI", "Burundi", (200, 90, 120)), ("JAMAICA", "Jamaica", (240, 200, 60)),
            ("TRINIDAD", "Trinidad", (220, 90, 90)), ("UGANDA", "Uganda", (230, 180, 70)), ("KENYA", "Kenya", (200, 80, 70)),
            ("MALAWI", "Malawi", (160, 110, 200)), ("ZAMBIA", "Zambia", (110, 185, 120)), ("GAMBIA", "Gambia, The", (220, 140, 60)),
            ("GUYANA", "Guyana", (100, 180, 100)), ("BOTSWANA", "Botswana", (130, 180, 230)), ("LESOTHO", "Lesotho", (90, 120, 200)),
            ("SWAZILAND", "Swaziland", (110, 150, 220)), ("EQUATORIAL GUINEA", "Equatorial Guinea", (120, 200, 120))]


def build(year=1969, stage=0):
    out, ov = _W31.build(1960, 0)
    for nm, dsn, col in NEW_1969:
        out.append((nm, col, D(dsn), (0, 0)))
    return out, ov
