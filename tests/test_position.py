import pytest
import uharfbuzz as hb


def position_of_first(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return buf.glyph_positions[0]


@pytest.mark.parametrize("text,moved", [
    ("ab", True),
    ("ach", True),
    ("ad", False),
    ("af", True),
    ("ag", False),
    ("aj", True),
    ("ak", False),
    ("al", False),
    ("am", False),
    ("an", False),
    ("ang", True),
    ("ank", True),
    ("ap", True),
    ("ar", False),
    ("as)", True),
    ("as(", True),
    ("ash", True),
    ("at", False),
    ("ath", False),
    ("av", True),
])
def test_starts_with_a(font, text, moved):
    did_move = position_of_first(text, font).y_offset != 0
    assert did_move == moved


@pytest.mark.parametrize("text,moved", [
    ("eb", True),
    ("ech", True),
    ("ed", False),
    ("ef", True),
    ("eg", False),
    ("ej", True),
    ("ek", False),
    ("el", False),
    ("em", False),
    ("en", False),
    ("eng", True),
    ("enk", True),
    ("ep", True),
    ("er", False),
    ("es)", True),
    ("es(", True),
    ("esh", True),
    ("et", False),
    ("eth", False),
    ("ev", True),
])
def test_starts_with_e(font, text, moved):
    did_move = position_of_first(text, font).y_offset != 0
    assert did_move == moved


@pytest.mark.parametrize("text,moved", [
    ("ob", True),
    ("och", True),
    ("od", False),
    ("of", True),
    ("og", False),
    ("oj", True),
    ("ok", False),
    ("ol", False),
    ("om", False),
    ("on", False),
    ("ong", True),
    ("onk", True),
    ("op", True),
    ("or", False),
    ("os)", True),
    ("os(", True),
    ("osh", True),
    ("ot", False),
    ("oth", False),
    ("ov", True),
])
def test_starts_with_o(font, text, moved):
    did_move = position_of_first(text, font).y_offset != 0
    assert did_move == moved
