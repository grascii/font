import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("au", ["a.au", "u.au"]),
])
def test_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("auk",   ["a.au", "u.au", "k"]),
    ("aug",   ["a.au", "u.au", "g"]),
    ("aur",   ["a.au", "u.aur", "r.cut"]),
    ("aul",   ["a.au", "u.aur", "l.cut"]),
    ("aun",   ["a.au", "u.au", "n"]),
    ("aum",   ["a.au", "u.au", "m"]),
    ("aut",   ["a.au", "u.au", "t"]),
    ("aud",   ["a.au", "u.au", "d"]),
    ("auf",   ["a.au", "u.au", "f"]),
    ("auv",   ["a.au", "u.au", "v"]),
    ("aus",   ["a.au", "u.au", "s.right"]),
    ("aush",  ["a.auch", "u.auch", "sh"]),
    ("auch",  ["a.auch", "u.auch", "ch"]),
    ("auj",   ["a.auch", "u.auch", "j"]),
    ("auth",  ["a.au", "u.au", "th.over.skew30"]),
])
def test_au_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
