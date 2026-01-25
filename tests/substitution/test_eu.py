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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("keuk",  ["k.cut", "e.keu", "u.keu", "k"]),
    ("keuk",  ["k.cut", "e.keu", "u.keu", "k"]),
    ("keur",  ["k.cut", "e.keu", "u.keur", "r.cut"]),
    ("keul",  ["k.cut", "e.keu", "u.keur", "l.cut"]),
    ("keun",  ["k.cut", "e.keu", "u.keu", "n"]),
    ("keum",  ["k.cut", "e.keu", "u.keu", "m"]),
    ("keut",  ["k.cut", "e.keu", "u.keu", "t"]),
    ("keud",  ["k.cut", "e.keu", "u.keu", "d"]),
    ("keup",  ["k.cut", "e.keu", "u.keu", "p"]),
    ("keub",  ["k.cut", "e.keu", "u.keu", "b"]),
    ("keuf",  ["k.cut", "e.keu", "u.keu", "f"]),
    ("keuv",  ["k.cut", "e.keu", "u.keu", "v"]),
    ("keush", ["k.cut", "e.keu", "u.keuch", "sh"]),
    ("keuch", ["k.cut", "e.keu", "u.keuch", "ch"]),
    ("keuj",  ["k.cut", "e.keu", "u.keuch", "j"]),
])
def test_k_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("geuk",  ["g.cut", "e.keu", "u.keu", "k"]),
    ("geuk",  ["g.cut", "e.keu", "u.keu", "k"]),
    ("geur",  ["g.cut", "e.keu", "u.keur", "r.cut"]),
    ("geul",  ["g.cut", "e.keu", "u.keur", "l.cut"]),
    ("geun",  ["g.cut", "e.keu", "u.keu", "n"]),
    ("geum",  ["g.cut", "e.keu", "u.keu", "m"]),
    ("geut",  ["g.cut", "e.keu", "u.keu", "t"]),
    ("geud",  ["g.cut", "e.keu", "u.keu", "d"]),
    ("geup",  ["g.cut", "e.keu", "u.keu", "p"]),
    ("geub",  ["g.cut", "e.keu", "u.keu", "b"]),
    ("geuf",  ["g.cut", "e.keu", "u.keu", "f"]),
    ("geuv",  ["g.cut", "e.keu", "u.keu", "v"]),
    ("geush", ["g.cut", "e.keu", "u.keuch", "sh"]),
    ("geuch", ["g.cut", "e.keu", "u.keuch", "ch"]),
    ("geuj",  ["g.cut", "e.keu", "u.keuch", "j"]),
])
def test_g_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("reush", ["r", "e.reu", "u.reu", "sh"]),
    ("reuch", ["r", "e.reu", "u.reu", "ch"]),
    ("reuj",  ["r", "e.reu", "u.reu", "j"]),
])
def test_r_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("leush", ["l", "e.reu", "u.reu", "sh"]),
    ("leuch", ["l", "e.reu", "u.reu", "ch"]),
    ("leuj",  ["l", "e.reu", "u.reu", "j"]),
])
def test_l_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
