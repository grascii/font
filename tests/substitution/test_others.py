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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tn", ["tn"]),
    ("dn", ["tn"]),
    ("tm", ["tm"]),
    ("dm", ["tm"]),
    ("nt", ["nt"]),
    ("nd", ["nt"]),
    ("mt", ["mt"]),
    ("md", ["mt"]),
    ("df", ["df"]),
    ("dv", ["df"]),
    ("tv", ["df"]),
    ("jnt", ["jnt"]),
    ("jnd", ["jnt"]),
    ("pnt", ["jnt"]),
    ("pnd", ["jnt"]),
])
def test_blended_consonants(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnt", ["tn", "t"]),
    ("dnd", ["tn", "d"]),
    ("tmd", ["tm", "d"]),
    ("dmt", ["tm", "t"]),
    ("ntn", ["n", "tn"]),
    ("ndm", ["n", "tm"]),
    ("mtm", ["m", "tm"]),
    ("mdn", ["m", "tn"]),
    ("nth", ["n", "th.over"]),
    ("mth", ["m", "th.over"]),
])
def test_blended_consonants_priority(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
