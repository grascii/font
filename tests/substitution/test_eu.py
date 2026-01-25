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
    ("keug",  ["k.cut", "e.keu", "u.keu", "g"]),
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
    ("geug",  ["g.cut", "e.keu", "u.keu", "g"]),
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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("neur",  ["n", "e.neu", "u.neur", "r.cut"]),
    ("neul",  ["n", "e.neu", "u.neur", "l.cut"]),
    ("neun",  ["n", "e.neu", "u.neu", "n"]),
    ("neum",  ["n", "e.neu", "u.neu", "m"]),
    ("neut",  ["n", "e.neu", "u.neu", "t"]),
    ("neud",  ["n", "e.neu", "u.neu", "d"]),
    ("neuf",  ["n", "e.neu", "u.neu", "f"]),
    ("neuv",  ["n", "e.neu", "u.neu", "v"]),
    ("neus",  ["n", "e.neu", "u.neu", "s.right"]),
    ("neush", ["n", "e.neu", "u.neuch", "sh"]),
    ("neuch", ["n", "e.neu", "u.neuch", "ch"]),
    ("neuj",  ["n", "e.neu", "u.neuch", "j"]),
])
def test_n_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("meur",  ["m", "e.neu", "u.neur", "r.cut"]),
    ("meul",  ["m", "e.neu", "u.neur", "l.cut"]),
    ("meun",  ["m", "e.neu", "u.neu", "n"]),
    ("meum",  ["m", "e.neu", "u.neu", "m"]),
    ("meut",  ["m", "e.neu", "u.neu", "t"]),
    ("meud",  ["m", "e.neu", "u.neu", "d"]),
    ("meuf",  ["m", "e.neu", "u.neu", "f"]),
    ("meuv",  ["m", "e.neu", "u.neu", "v"]),
    ("meus",  ["m", "e.neu", "u.neu", "s.right"]),
    ("meush", ["m", "e.neu", "u.neuch", "sh"]),
    ("meuch", ["m", "e.neu", "u.neuch", "ch"]),
    ("meuj",  ["m", "e.neu", "u.neuch", "j"]),
])
def test_m_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("teuk",  ["t", "e.teu", "u.teu", "k"]),
    ("teug",  ["t", "e.teu", "u.teu", "g"]),
    ("teut",  ["t", "e.teu", "u.teu", "t"]),
    ("teud",  ["t", "e.teu", "u.teu", "d"]),
    ("teup",  ["t", "e.teu", "u.teup", "p"]),
    ("teub",  ["t", "e.teu", "u.teup", "b"]),
    ("teuf",  ["t", "e.teu", "u.teu", "f"]),
    ("teuv",  ["t", "e.teu", "u.teu", "v"]),
    ("teus",  ["t", "e.teu", "u.teu", "s.right"]),
    ("teush", ["t", "e.teu", "u.teu", "sh"]),
    ("teuch", ["t", "e.teu", "u.teu", "ch"]),
    ("teuj",  ["t", "e.teu", "u.teu", "j"]),
])
def test_t_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("deuk",  ["d", "e.teu", "u.teu", "k"]),
    ("deug",  ["d", "e.teu", "u.teu", "g"]),
    ("deut",  ["d", "e.teu", "u.teu", "t"]),
    ("deud",  ["d", "e.teu", "u.teu", "d"]),
    ("deup",  ["d", "e.teu", "u.teup", "p"]),
    ("deub",  ["d", "e.teu", "u.teup", "b"]),
    ("deuf",  ["d", "e.teu", "u.teu", "f"]),
    ("deuv",  ["d", "e.teu", "u.teu", "v"]),
    ("deus",  ["d", "e.teu", "u.teu", "s.right"]),
    ("deush", ["d", "e.teu", "u.teu", "sh"]),
    ("deuch", ["d", "e.teu", "u.teu", "ch"]),
    ("deuj",  ["d", "e.teu", "u.teu", "j"]),
])
def test_d_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
