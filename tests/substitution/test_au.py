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
def test_au_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("kaur",  ["k.cut", "a.kau", "u.kaur", "r.cut"]),
    ("kaul",  ["k.cut", "a.kau", "u.kaur", "l.cut"]),
    ("kaut",  ["k.cut", "a.kau", "u.kau", "t"]),
    ("kaud",  ["k.cut", "a.kau", "u.kau", "d"]),
    ("kaush", ["k.cut", "a.kau", "u.kauch", "sh"]),
    ("kauch", ["k.cut", "a.kau", "u.kauch", "ch"]),
    ("kauj",  ["k.cut", "a.kau", "u.kauch", "j"]),
])
def test_k_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("gaur",  ["g.cut", "a.kau", "u.kaur", "r.cut"]),
    ("gaul",  ["g.cut", "a.kau", "u.kaur", "l.cut"]),
    ("gaut",  ["g.cut", "a.kau", "u.kau", "t"]),
    ("gaud",  ["g.cut", "a.kau", "u.kau", "d"]),
    ("gaush", ["g.cut", "a.kau", "u.kauch", "sh"]),
    ("gauch", ["g.cut", "a.kau", "u.kauch", "ch"]),
    ("gauj",  ["g.cut", "a.kau", "u.kauch", "j"]),
])
def test_g_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("raur",  ["r", "a.rau", "u.raur", "r.cut"]),
    ("raul",  ["r", "a.rau", "u.raur", "l.cut"]),
    ("raut",  ["r", "a.rau", "u.rau", "t"]),
    ("raud",  ["r", "a.rau", "u.rau", "d"]),
    ("raush", ["r", "a.rau", "u.rau", "sh"]),
    ("rauch", ["r", "a.rau", "u.rau", "ch"]),
    ("rauj",  ["r", "a.rau", "u.rau", "j"]),
    ("raus",  ["r", "a.rau", "u.rau", "s.right"]),
])
def test_r_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("laur",  ["l", "a.rau", "u.raur", "r.cut"]),
    ("laul",  ["l", "a.rau", "u.raur", "l.cut"]),
    ("laut",  ["l", "a.rau", "u.rau", "t"]),
    ("laud",  ["l", "a.rau", "u.rau", "d"]),
    ("laush", ["l", "a.rau", "u.rau", "sh"]),
    ("lauch", ["l", "a.rau", "u.rau", "ch"]),
    ("lauj",  ["l", "a.rau", "u.rau", "j"]),
    ("laus",  ["l", "a.rau", "u.rau", "s.right"]),
])
def test_l_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("naut",  ["n", "a.nau", "u.nau", "t"]),
    ("naud",  ["n", "a.nau", "u.nau", "d"]),
    ("naus",  ["n", "a.nau", "u.nau", "s.right"]),
    ("nauth", ["n", "a.nau", "u.nau", "th.over.skew30"]),
])
def test_n_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("maut",  ["m", "a.nau", "u.nau", "t"]),
    ("maud",  ["m", "a.nau", "u.nau", "d"]),
    ("maus",  ["m", "a.nau", "u.nau", "s.right"]),
    ("mauth", ["m", "a.nau", "u.nau", "th.over.skew30"]),
])
def test_m_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("taur",   ["t", "a.tau", "u.taur", "r.cut"]),
    ("taul",   ["t", "a.tau", "u.taur", "l.cut"]),
    ("taut",   ["t", "a.tau", "u.tau", "t"]),
    ("taud",   ["t", "a.tau", "u.tau", "d"]),
    ("tauf",   ["t", "a.tau", "u.tau", "f"]),
    ("tauv",   ["t", "a.tau", "u.tau", "v"]),
    ("taush",  ["t", "a.tau", "u.tauch", "sh"]),
    ("tauch",  ["t", "a.tau", "u.tauch", "ch"]),
    ("tauj",   ["t", "a.tau", "u.tauch", "j"]),
    ("taus",   ["t", "a.tau", "u.tau", "s.right"]),
    ("tauth",  ["t", "a.tau", "u.tau", "th.over.skew30"]),
])
def test_t_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

@pytest.mark.parametrize("text,expected_glyphs", [
    ("daur",   ["d", "a.tau", "u.taur", "r.cut"]),
    ("daul",   ["d", "a.tau", "u.taur", "l.cut"]),
    ("daut",   ["d", "a.tau", "u.tau", "t"]),
    ("daud",   ["d", "a.tau", "u.tau", "d"]),
    ("dauf",   ["d", "a.tau", "u.tau", "f"]),
    ("dauv",   ["d", "a.tau", "u.tau", "v"]),
    ("daush",  ["d", "a.tau", "u.tauch", "sh"]),
    ("dauch",  ["d", "a.tau", "u.tauch", "ch"]),
    ("dauj",   ["d", "a.tau", "u.tauch", "j"]),
    ("daus",   ["d", "a.tau", "u.tau", "s.right"]),
    ("dauth",  ["d", "a.tau", "u.tau", "th.over.skew30"]),
])
def test_d_au(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
