import pytest
import uharfbuzz as hb


def position_of_first(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return buf.glyph_positions[0]


@pytest.mark.parametrize("text,moved_x,moved_y", [
    ("ab", True, True),
    ("ach", True, True),
    ("ad", False, False),
    ("af", True, True),
    ("ag", False, False),
    ("aj", True, True),
    ("ak", False, False),
    ("al", False, False),
    ("am", False, False),
    ("an", False, False),
    ("ang", False, True),
    ("ank", False, True),
    ("ap", True, True),
    ("ar", False, False),
    ("as)", False, True),
    ("as(", True, True),
    ("ash", False, True),
    ("at", False, False),
    ("ath", False, False),
    ("av", True, True),
])
def test_starts_with_a(font, text, moved_x, moved_y):
    did_move_x = position_of_first(text, font).x_offset != 0
    did_move_y = position_of_first(text, font).y_offset != 0
    assert did_move_x == moved_x
    assert did_move_y == did_move_y


@pytest.mark.parametrize("text,moved_x,moved_y", [
    ("eb", True, True),
    ("ech", True, True),
    ("ed", False, False),
    ("ef", True, True),
    ("eg", False, False),
    ("ej", True, True),
    ("ek", False, False),
    ("el", False, False),
    ("em", False, False),
    ("en", False, False),
    ("eng", False, True),
    ("enk", False, True),
    ("ep", True, True),
    ("er", False, False),
    ("es)", True, True),
    ("es(", True, True),
    ("esh", True, True),
    ("et", False, False),
    ("eth", False, False),
    ("ev", True, True),
])
def test_starts_with_e(font, text, moved_x, moved_y,):
    did_move_x = position_of_first(text, font).x_offset != 0
    did_move_y = position_of_first(text, font).y_offset != 0
    assert did_move_x == moved_x
    assert did_move_y == did_move_y


@pytest.mark.parametrize("text,moved_x,moved_y", [
    ("ob", True, True),
    ("och", True, True),
    ("od", False, False),
    ("of", True, True),
    ("og", False, False),
    ("oj", True, True),
    ("ok", False, False),
    ("ol", False, False),
    ("om", False, False),
    ("on", False, False),
    ("ong", False, True),
    ("onk", False, True),
    ("op", True, True),
    ("or", False, False),
    ("os)", False, True),
    ("os(", False, True),
    ("osh", False, True),
    ("ot", False, False),
    ("oth", False, False),
    ("ov", True, True),
])
def test_starts_with_o(font, text, moved_x, moved_y):
    did_move_x = position_of_first(text, font).x_offset != 0
    did_move_y = position_of_first(text, font).y_offset != 0
    assert did_move_x == moved_x
    assert did_move_y == did_move_y


@pytest.mark.parametrize("text,moved_x,moved_y", [
    ("ub", True, True),
    ("uch", True, True),
    ("ud", False, False),
    ("uf", True, True),
    ("ug", False, False),
    ("uj", True, True),
    ("uk", False, False),
    ("ul", False, False),
    ("um", False, False),
    ("un", False, False),
    ("ung", False, True),
    ("unk", False, True),
    ("up", True, True),
    ("ur", False, False),
    ("us)", True, True),
    ("us(", True, True),
    ("ush", True, True),
    ("ut", False, False),
    ("uth", False, False),
    ("uv", True, True),
])
def test_starts_with_u(font, text, moved_x, moved_y):
    did_move_x = position_of_first(text, font).x_offset != 0
    did_move_y = position_of_first(text, font).y_offset != 0
    assert did_move_x == moved_x
    assert did_move_y == did_move_y
