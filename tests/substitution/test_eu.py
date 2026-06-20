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
    ("dfeu", ["df", "e.feu", "u.feu"]),
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
    ("keutn", ["k.cut", "e.keu", "u.keu", "tn.skew30"]),
    ("keudn", ["k.cut", "e.keu", "u.keu", "tn.skew30"]),
    ("keutm", ["k.cut", "e.keu", "u.keu", "tm.skew30"]),
    ("keudm", ["k.cut", "e.keu", "u.keu", "tm.skew30"]),
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
    ("geutn", ["g.cut", "e.keu", "u.keu", "tn.skew30"]),
    ("geudn", ["g.cut", "e.keu", "u.keu", "tn.skew30"]),
    ("geutm", ["g.cut", "e.keu", "u.keu", "tm.skew30"]),
    ("geudm", ["g.cut", "e.keu", "u.keu", "tm.skew30"]),
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
    ("neutn", ["n", "e.neu", "u.neu", "tn.skew30"]),
    ("neudn", ["n", "e.neu", "u.neu", "tn.skew30"]),
    ("neutm", ["n", "e.neu", "u.neu", "tm.skew30"]),
    ("neudm", ["n", "e.neu", "u.neu", "tm.skew30"]),
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
    ("meutn", ["m", "e.neu", "u.neu", "tn.skew30"]),
    ("meudn", ["m", "e.neu", "u.neu", "tn.skew30"]),
    ("meutm", ["m", "e.neu", "u.neu", "tm.skew30"]),
    ("meudm", ["m", "e.neu", "u.neu", "tm.skew30"]),
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
    ("peutn", ["p.cut", "e.peu", "u.peu", "tn.skew30"]),
    ("peudn", ["p.cut", "e.peu", "u.peu", "tn.skew30"]),
    ("peutm", ["p.cut", "e.peu", "u.peu", "tm.skew30"]),
    ("peudm", ["p.cut", "e.peu", "u.peu", "tm.skew30"]),
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
    ("beutn", ["b.cut", "e.peu", "u.peu", "tn.skew30"]),
    ("beudn", ["b.cut", "e.peu", "u.peu", "tn.skew30"]),
    ("beutm", ["b.cut", "e.peu", "u.peu", "tm.skew30"]),
    ("beudm", ["b.cut", "e.peu", "u.peu", "tm.skew30"]),
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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tneur",   ["tn", "e.neu", "u.neur", "r.cut"]),
    ("tneul",   ["tn", "e.neu", "u.neur", "l.cut"]),
    ("tneun",   ["tn", "e.neu", "u.neu", "n"]),
    ("tneum",   ["tn", "e.neu", "u.neu", "m"]),
    ("tneut",   ["tn", "e.neu", "u.neu", "t"]),
    ("tneud",   ["tn", "e.neu", "u.neu", "d"]),
    ("tneush",  ["tn", "e.neu", "u.neuch", "sh"]),
    ("tneuch",  ["tn", "e.neu", "u.neuch", "ch"]),
    ("tneuj",   ["tn", "e.neu", "u.neuch", "j"]),
    ("tneus",   ["tn", "e.neu", "u.neu", "s.right"]),
    ("tneuth",  ["tn", "e.neu", "u.neu", "th.over.skew30"]),
])
def test_tn_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tmeur",   ["tm", "e.neu", "u.neur", "r.cut"]),
    ("tmeul",   ["tm", "e.neu", "u.neur", "l.cut"]),
    ("tmeun",   ["tm", "e.neu", "u.neu", "n"]),
    ("tmeum",   ["tm", "e.neu", "u.neu", "m"]),
    ("tmeut",   ["tm", "e.neu", "u.neu", "t"]),
    ("tmeud",   ["tm", "e.neu", "u.neu", "d"]),
    ("tmeush",  ["tm", "e.neu", "u.neuch", "sh"]),
    ("tmeuch",  ["tm", "e.neu", "u.neuch", "ch"]),
    ("tmeuj",   ["tm", "e.neu", "u.neuch", "j"]),
    ("tmeus",   ["tm", "e.neu", "u.neu", "s.right"]),
    ("tmeuth",  ["tm", "e.neu", "u.neu", "th.over.skew30"]),
])
def test_tm_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nteuk",   ["nt.skew30", "e.teu", "u.teu", "k"]),
    ("nteug",   ["nt.skew30", "e.teu", "u.teu", "g"]),
    ("nteush",  ["nt.skew30", "e.teu", "u.teu", "sh"]),
    ("nteuch",  ["nt.skew30", "e.teu", "u.teu", "ch"]),
    ("nteuj",   ["nt.skew30", "e.teu", "u.teu", "j"]),
])
def test_nt_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mteuk",   ["mt.skew30", "e.teu", "u.teu", "k"]),
    ("mteug",   ["mt.skew30", "e.teu", "u.teu", "g"]),
    ("mteush",  ["mt.skew30", "e.teu", "u.teu", "sh"]),
    ("mteuch",  ["mt.skew30", "e.teu", "u.teu", "ch"]),
    ("mteuj",   ["mt.skew30", "e.teu", "u.teu", "j"]),
])
def test_mt_eu(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
