import pytest
import uharfbuzz as hb


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]


def create_map_direction(first, second):
    def map_glyph(glyph):
        if glyph == first:
            return -1
        elif glyph == second:
            return 1
        else:
            return 0

    def map_direction(glyphs):
        return list(map(map_glyph, glyphs))

    return map_direction


map_s_direction = create_map_direction("s.left", "s.right")


@pytest.mark.parametrize("text,expected", [
    ("s", [1]),
    ("s)", [1]),
    ("s(", [-1]),
])
def test_lone_s(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("spra", [-1, 0, 0, 0]),
    ("reps", [0, 0, 0, -1]),
    ("pas", [0, 0, -1]),
    ("sfer", [1, 0, 0, 0]),
    ("saf", [1, 0, 0]),
    ("fas", [0, 0, 1]),
    ("skat", [1, 0, 0, 0]),
    ("sek", [1, 0, 0]),
    ("maks", [0, 0, 0, 1]),
    ("kas", [0, 0, 1]),
    ("sla", [-1, 0, 0]),
    ("sals", [-1, 0, 0, -1]),
])
def test_s_joined_to_curves(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("sta", [1, 0, 0]),
    ("set", [1, 0, 0]),
    ("nets", [0, 0, 0, -1]),
    ("sed", [1, 0, 0]),
    ("ods", [0, 0, -1]),
    ("das", [0, 0, -1]),
    ("sno", [1, 0, 0]),
    ("sen", [1, 0, 0]),
    ("smak", [1, 0, 0, 0]),
    ("sam", [1, 0, 0]),
    ("lens", [0, 0, 0, -1]),
    ("nes", [0, 0, -1]),
])
def test_s_joined_to_forward_lines(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("sash", [1, 0, 0]),
    ("saj", [1, 0, 0]),
    ("ches", [0, 0, 1]),
])
def test_s_joined_to_downward_lines(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("so", [1, 0]),
    ("soro", [1, 0, 0, 0]),
    ("sol", [1, 0, 0]),
    ("sofa", [1, 0, 0, 0]),
    ("sop", [1, 0, 0]),
    ("sod", [1, 0, 0]),
])
def test_s_o(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("us", [0, 1]),
    ("bus", [0, 0, 1]),
    ("fus", [0, 0, 1]),
    ("gust", [0, 0, 1, 0]),
    ("grashus", [0, 0, 0, 0, 0, 1]),
    ("veshus", [0, 0, 0, 0, 1]),
    ("sut", [1, 0, 0]),
    ("sup", [1, 0, 0]),
    ("us", [0, 1]),
])
def test_s_u(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("uosp", [0, 0, -1, 0]),
    ("past", [0, 0, -1, 0]),
    ("uesp", [0, 0, -1, 0]),
    ("uestf", [0, 0, 1, 0, 0]),
    ("gosep", [0, 0, -1, 0, 0]),
    ("trespas", [0, 0, 0, -1, 0, 0, -1]),
    ("tresl", [0, 0, 0, -1, 0]),
    ("vest", [0, 0, 1, 0]),
    ("kask", [0, 0, 1, 0]),
    ("kasm", [0, 0, 1, 0]),
    ("resk", [0, 0, -1, 0]),
    ("asal", [0, -1, 0, 0]),
    ("dosel", [0, 0, -1, 0, 0]),
    ("flask", [0, 0, 0, -1, 0]),
    ("klasp", [0, 0, 0, -1, 0]),
])
def test_sandwiched_s(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("vestre", [0, 0, 1, 0, 0, 0]),
    ("ofset", [0, 0, 1, 0, 0]),
    ("bost", [0, 0, -1, 0]),
    ("tast", [0, 0, -1,  0]),
    ("desk", [0, 0, -1, 0]),
    ("mask", [0, 0, -1, 0]),
])
def test_sandwiched_s2(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected


@pytest.mark.parametrize("text,expected", [
    ("isi", [0, -1, 0]),
    ("isberg", [0, -1, 0, 0, 0, 0]),
    ("iskrem", [0, -1, 0, 0, 0, 0]),
    ("isola", [0, -1, 0, 0, 0]),
    ("nis", [0, 0, -1]),
    ("vis", [0, 0, 1]),
    ("uis", [0, 0, 1]),
])
def test_s_after_i(font, text, expected):
    assert map_s_direction(shape(text, font)) == expected
