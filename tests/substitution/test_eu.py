import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("eu", ["e.eu", "u.eu"]),
])
def test_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("euk",   ["e.eu", "u.eu", "k"]),
    ("eug",   ["e.eu", "u.eu", "g"]),
    ("eur",   ["e.eu", "u.aur", "r.cut"]),
    ("eul",   ["e.eu", "u.aur", "l.cut"]),
    ("eun",   ["e.eu", "u.eu", "n"]),
    ("eum",   ["e.eu", "u.eu", "m"]),
    ("eut",   ["e.eu", "u.eu", "t"]),
    ("eud",   ["e.eu", "u.eu", "d"]),
    ("euf",   ["e.eu", "u.eu", "f"]),
    ("euv",   ["e.eu", "u.eu", "v"]),
    ("eus",   ["e.eu", "u.eu", "s.right"]),
    ("eush",  ["e.euch", "u.euch", "sh"]),
    ("euch",  ["e.euch", "u.euch", "ch"]),
    ("euj",   ["e.euch", "u.euch", "j"]),
    ("euth",  ["e.eu", "u.eu", "th.over.skew30"]),
    ("euth)", ["e.eu", "u.eu", "th.under"]),
])
def test_eu_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("keu",  ["k.cut", "e.keu", "u.keu"]),
    ("geu",  ["g.cut", "e.keu", "u.keu"]),
    ("reu",  ["r", "e.reu", "u.reu"]),
    ("leu",  ["l", "e.reu", "u.reu"]),
    ("neu",  ["n", "e.neu", "u.neu"]),
    ("meu",  ["m", "e.neu", "u.neu"]),
    ("teu",  ["t", "e.teu", "u.teu"]),
    ("deu",  ["d", "e.teu", "u.teu"]),
    ("peu",  ["p.cut", "e.peu", "u.peu"]),
    ("beu",  ["b.cut", "e.peu", "u.peu"]),
    ("feu",  ["f", "e.feu", "u.feu"]),
    ("veu",  ["v", "e.feu", "u.feu"]),
    ("seu",  ["s.right", "e.feu", "u.feu"]),
])
def test_eu_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
