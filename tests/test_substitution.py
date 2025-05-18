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
    ("ak", ["a.ak", "k"]),
    ("ag", ["a.ak", "g"]),
    ("ar", ["a.ar", "r"]),
    ("al", ["a.al", "l"]),
    ("an", ["a.an", "n"]),
    ("am", ["a.an", "m"]),
    ("at", ["a.at", "t"]),
    ("ad", ["a.at", "d"]),
    ("ap", ["a.ap", "p"]),
    ("ab", ["a.ap", "b"]),
    ("af", ["a.af", "f"]),
    ("av", ["a.av", "v"]),
    ("ash", ["a.ach", "sh"]),
    ("ach", ["a.ach", "ch"]),
    ("aj", ["a.ach", "j"]),
    ("ath", ["a.ath", "th"]),
    ("ang", ["a.ang", "ng"]),
    ("ank", ["a.ang", "nk"]),
])
def test_a_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ka", ["k", "a.ka"]),
    ("ga", ["g", "a.ka"]),
    ("ra", ["r", "a.ra"]),
    ("la", ["l", "a.ra"]),
    ("na", ["n", "a.na"]),
    ("ma", ["m", "a.na"]),
    ("ta", ["t", "a.ta"]),
    ("da", ["d", "a.ta"]),
    ("pa", ["p", "a.pa"]),
    ("ba", ["b", "a.ba"]),
    ("fa", ["f", "a.fa"]),
    ("va", ["v", "a.fa"]),
    ("sha", ["sh", "a.cha"]),
    ("cha", ["ch", "a.cha"]),
    ("ja", ["j", "a.cha"]),
    ("tha", ["th", "a.tha"]),
    ("nga", ["ng", "a.nga"]),
    ("nka", ["nk", "a.nga"]),
])
def test_a_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
