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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kau",  ["k.cut", "a.kau", "u.kau"]),
    ("gau",  ["g.cut", "a.kau", "u.kau"]),
    ("rau",  ["r", "a.rau", "u.rau"]),
    ("lau",  ["l", "a.rau", "u.rau"]),
    ("nau",  ["n", "a.nau", "u.nau"]),
    ("mau",  ["m", "a.nau", "u.nau"]),
    ("tau",  ["t", "a.tau", "u.tau"]),
    ("dau",  ["d", "a.tau", "u.tau"]),
    ("pau",  ["p.cut", "a.pau", "u.au"]),
    ("bau",  ["b.cut", "a.pau", "u.au"]),
    ("fau",  ["f", "a.fau", "u.fau"]),
    ("vau",  ["v", "a.fau", "u.fau"]),
    ("sau",  ["s.right", "a.fau", "u.fau"]),
    ("shau", ["sh", "a.chau", "u.au"]),
    ("chau", ["ch", "a.chau", "u.au"]),
    ("jau",  ["j", "a.chau", "u.au"]),
    ("thau", ["th.over", "a.tnau", "u.tnau"]),
])
def test_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
