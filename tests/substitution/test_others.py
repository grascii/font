import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sh", ["sh"]),
    ("ch", ["ch"]),
    ("th", ["th.over"]),
    ("ng", ["ng"]),
    ("nk", ["nk"]),
])
def test_multichar_ligatures(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pr", ["p.cut", "r"]),
    ("pl", ["p.cut", "l"]),
    ("br", ["b.cut", "r"]),
    ("bl", ["b.cut", "l"]),
])
def test_consonant_blends(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
