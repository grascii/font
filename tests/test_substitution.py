import pytest
import uharfbuzz as hb


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sh", ["sh"]),
    ("ch", ["ch"]),
    ("th", ["th"]),
    ("ng", ["ng"]),
    ("nk", ["nk"]),
])
def test_multichar_ligatures(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ash", ["a.ach", "sh"]),
    ("ach", ["a.ach", "ch"]),
    ("aj", ["a.ach", "j"]),
    ("af", ["a.af", "f"]),
    ("av", ["a.av", "v"]),
    ("ak", ["a.ak", "k"]),
    ("ag", ["a.ak", "g"]),
    ("an", ["a.an", "n"]),
    ("am", ["a.an", "m"]),
    ("ap", ["a.ap", "p"]),
    ("ab", ["a.ap", "b"]),
    ("ar", ["a.ar", "r"]),
    ("al", ["a.al", "l"]),
    ("ath", ["a.ath", "th"]),
    ("at", ["a.at", "t"]),
    ("ad", ["a.at", "d"]),
    ("ang", ["a.ang", "ng"]),
    ("ank", ["a.ang", "nk"]),
])
def test_a_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
