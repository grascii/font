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
    ("eutn",  ["e.eu", "u.eu", "tn.skew30"]),
    ("eudn",  ["e.eu", "u.eu", "tn.skew30"]),
    ("eutm",  ["e.eu", "u.eu", "tm.skew30"]),
    ("eudm",  ["e.eu", "u.eu", "tm.skew30"]),
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
    ("tneu", ["tn", "e.neu", "u.neu"]),
    ("dneu", ["tn", "e.neu", "u.neu"]),
    ("tmeu", ["tm", "e.neu", "u.neu"]),
    ("dmeu", ["tm", "e.neu", "u.neu"]),
    ("nteu", ["nt.skew30", "e.teu", "u.teu"]),
    ("ndeu", ["nt.skew30", "e.teu", "u.teu"]),
    ("mteu", ["mt.skew30", "e.teu", "u.teu"]),
    ("mdeu", ["mt.skew30", "e.teu", "u.teu"]),
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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("peuk",  ["p.cut", "e.peu", "u.peu", "k"]),
    ("peug",  ["p.cut", "e.peu", "u.peu", "g"]),
    ("peur",  ["p.cut", "e.peu", "u.peur", "r.cut"]),
    ("peul",  ["p.cut", "e.peu", "u.peur", "l.cut"]),
    ("peun",  ["p.cut", "e.peu", "u.peu", "n"]),
    ("peum",  ["p.cut", "e.peu", "u.peu", "m"]),
    ("peut",  ["p.cut", "e.peu", "u.peu", "t"]),
    ("peud",  ["p.cut", "e.peu", "u.peu", "d"]),
    ("peuf",  ["p.cut", "e.peu", "u.peu", "f"]),
    ("peuv",  ["p.cut", "e.peu", "u.peu", "v"]),
    ("peus",  ["p.cut", "e.peu", "u.peu", "s.right"]),
    ("peush", ["p.cut", "e.peu", "u.peuch", "sh"]),
    ("peuch", ["p.cut", "e.peu", "u.peuch", "ch"]),
    ("peuj",  ["p.cut", "e.peu", "u.peuch", "j"]),
])
def test_p_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("beuk",  ["b.cut", "e.peu", "u.peu", "k"]),
    ("beug",  ["b.cut", "e.peu", "u.peu", "g"]),
    ("beur",  ["b.cut", "e.peu", "u.peur", "r.cut"]),
    ("beul",  ["b.cut", "e.peu", "u.peur", "l.cut"]),
    ("beun",  ["b.cut", "e.peu", "u.peu", "n"]),
    ("beum",  ["b.cut", "e.peu", "u.peu", "m"]),
    ("beut",  ["b.cut", "e.peu", "u.peu", "t"]),
    ("beud",  ["b.cut", "e.peu", "u.peu", "d"]),
    ("beuf",  ["b.cut", "e.peu", "u.peu", "f"]),
    ("beuv",  ["b.cut", "e.peu", "u.peu", "v"]),
    ("beus",  ["b.cut", "e.peu", "u.peu", "s.right"]),
    ("beush", ["b.cut", "e.peu", "u.peuch", "sh"]),
    ("beuch", ["b.cut", "e.peu", "u.peuch", "ch"]),
    ("beuj",  ["b.cut", "e.peu", "u.peuch", "j"]),
])
def test_b_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("feur",  ["f", "e.feu", "u.feur", "r.cut"]),
    ("feul",  ["f", "e.feu", "u.feur", "l.cut"]),
    ("feun",  ["f", "e.feu", "u.feu", "n"]),
    ("feum",  ["f", "e.feu", "u.feu", "m"]),
    ("feut",  ["f", "e.feu", "u.feu", "t"]),
    ("feud",  ["f", "e.feu", "u.feu", "d"]),
    ("feup",  ["f", "e.feu", "u.feu", "p"]),
    ("feub",  ["f", "e.feu", "u.feu", "b"]),
    ("feuf",  ["f", "e.feu", "u.feu", "f"]),
    ("feuv",  ["f", "e.feu", "u.feu", "v"]),
    ("feus",  ["f", "e.feu", "u.feu", "s.right"]),
    ("feush", ["f", "e.feu", "u.feuch", "sh"]),
    ("feuch", ["f", "e.feu", "u.feuch", "ch"]),
    ("feuj",  ["f", "e.feu", "u.feuch", "j"]),
])
def test_f_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("veur",  ["v", "e.feu", "u.feur", "r.cut"]),
    ("veul",  ["v", "e.feu", "u.feur", "l.cut"]),
    ("veun",  ["v", "e.feu", "u.feu", "n"]),
    ("veum",  ["v", "e.feu", "u.feu", "m"]),
    ("veut",  ["v", "e.feu", "u.feu", "t"]),
    ("veud",  ["v", "e.feu", "u.feu", "d"]),
    ("veup",  ["v", "e.feu", "u.feu", "p"]),
    ("veub",  ["v", "e.feu", "u.feu", "b"]),
    ("veuf",  ["v", "e.feu", "u.feu", "f"]),
    ("veuv",  ["v", "e.feu", "u.feu", "v"]),
    ("veus",  ["v", "e.feu", "u.feu", "s.right"]),
    ("veush", ["v", "e.feu", "u.feuch", "sh"]),
    ("veuch", ["v", "e.feu", "u.feuch", "ch"]),
    ("veuj",  ["v", "e.feu", "u.feuch", "j"]),
])
def test_v_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("seur",  ["s.right", "e.feu", "u.feur", "r.cut"]),
    ("seul",  ["s.right", "e.feu", "u.feur", "l.cut"]),
    ("seun",  ["s.right", "e.feu", "u.feu", "n"]),
    ("seum",  ["s.right", "e.feu", "u.feu", "m"]),
    ("seut",  ["s.right", "e.feu", "u.feu", "t"]),
    ("seud",  ["s.right", "e.feu", "u.feu", "d"]),
    ("seup",  ["s.right", "e.feu", "u.feu", "p"]),
    ("seub",  ["s.right", "e.feu", "u.feu", "b"]),
    ("seuf",  ["s.right", "e.feu", "u.feu", "f"]),
    ("seuv",  ["s.right", "e.feu", "u.feu", "v"]),
    ("seus",  ["s.right", "e.feu", "u.feu", "s.right"]),
    ("seush", ["s.right", "e.feu", "u.feuch", "sh"]),
    ("seuch", ["s.right", "e.feu", "u.feuch", "ch"]),
    ("seuj",  ["s.right", "e.feu", "u.feuch", "j"]),
])
def test_sR_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
