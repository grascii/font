import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uk",   ["u", "k"]),
    ("ug",   ["u", "g"]),
    ("ur",   ["u.ur", "r"]),
    ("ul",   ["u.ur", "l"]),
    ("un",   ["u", "n"]),
    ("um",   ["u", "m"]),
    ("ut",   ["u", "t"]),
    ("ud",   ["u", "d"]),
    ("up",   ["u.up", "p"]),
    ("ub",   ["u.up", "b"]),
    ("uf",   ["u.uf", "f"]),
    ("uv",   ["u.uf", "v"]),
    ("ush",  ["u", "sh"]),
    ("uch",  ["u", "ch"]),
    ("uj",   ["u", "j"]),
    ("us)",  ["u.uf", "s.right"]),
    ("us(",  ["u.up", "s.left"]),
    ("uth(", ["u", "th.over.skew30"]),
    ("uth)", ["u", "th.under"]),
    ("ung",  ["u", "ng"]),
    ("unk",  ["u", "nk"]),
])
def test_u_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ku",   ["k", "u"]),
    ("gu",   ["g", "u"]),
    ("ru",   ["r", "u.ru"]),
    ("lu",   ["l", "u.ru"]),
    ("nu",   ["n", "u.nu"]),
    ("mu",   ["m", "u.nu"]),
    ("tu",   ["t", "u.tu"]),
    ("du",   ["d", "u.tu"]),
    ("pu",   ["p", "u"]),
    ("bu",   ["b", "u"]),
    ("fu",   ["f", "u.fu"]),
    ("vu",   ["v", "u.fu"]),
    ("shu",  ["sh", "u"]),
    ("chu",  ["ch", "u"]),
    ("ju",   ["j", "u"]),
    ("su",   ["s.right", "u.fu"]),
    ("s(u",  ["s.left", "u"]),
    ("th(u", ["th.over", "u.tnu"]),
    ("th)u", ["th.under", "u"]),
    ("ngu",  ["ng", "u.ngu"]),
    ("nku",  ["nk", "u.ngu"]),
])
def test_u_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kuk",  ["k", "u", "k"]),
    ("kug",  ["k", "u", "g"]),
    ("kur",  ["k.cut", "u.kur", "r.cut"]),
    ("kul",  ["k.cut", "u.kur", "l.cut"]),
    ("kun",  ["k", "u", "n"]),
    ("kum",  ["k", "u", "m"]),
    ("kut",  ["k", "u", "t"]),
    ("kud",  ["k", "u", "d"]),
    ("kup",  ["k", "u.up", "p"]),
    ("kub",  ["k", "u.up", "b"]),
    ("kuf",  ["k", "u.uf", "f"]),
    ("kuv",  ["k", "u.uf", "v"]),
    ("kush", ["k", "u", "sh"]),
    ("kuch", ["k", "u", "ch"]),
    ("kuj",  ["k", "u", "j"]),
    ("kus)", ["k", "u.uf", "s.right"]),
    ("kus(", ["k", "u.up", "s.left"]),
    ("kuth", ["k", "u", "th.over.skew30"]),
])
def test_k_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("guk",  ["g", "u", "k"]),
    ("gug",  ["g", "u", "g"]),
    ("gur",  ["g.cut", "u.kur", "r.cut"]),
    ("gul",  ["g.cut", "u.kur", "l.cut"]),
    ("gun",  ["g", "u", "n"]),
    ("gum",  ["g", "u", "m"]),
    ("gut",  ["g", "u", "t"]),
    ("gud",  ["g", "u", "d"]),
    ("gup",  ["g", "u.up", "p"]),
    ("gub",  ["g", "u.up", "b"]),
    ("guf",  ["g", "u.uf", "f"]),
    ("guv",  ["g", "u.uf", "v"]),
    ("gush", ["g", "u", "sh"]),
    ("guch", ["g", "u", "ch"]),
    ("guj",  ["g", "u", "j"]),
    ("gus)", ["g", "u.uf", "s.right"]),
    ("gus(", ["g", "u.up", "s.left"]),
    ("guth", ["g", "u", "th.over.skew30"]),
])
def test_g_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ruk",   ["r", "u.ru", "k"]),
    ("rug",   ["r", "u.ru", "g"]),
    ("rur",   ["r", "u.rur", "r"]),
    ("rul",   ["r", "u.rur", "l"]),
    ("run",   ["r", "u.ru", "n"]),
    ("rum",   ["r", "u.ru", "m"]),
    ("rut",   ["r", "u.ru", "t"]),
    ("rud",   ["r", "u.ru", "d"]),
    ("rup",   ["r", "u.rup", "p"]),
    ("rub",   ["r", "u.rup", "b"]),
    ("ruf",   ["r", "u.ru", "f"]),
    ("ruv",   ["r", "u.ru", "v"]),
    ("rush",  ["r", "u.ru", "sh"]),
    ("ruch",  ["r", "u.ru", "ch"]),
    ("ruj",   ["r", "u.ru", "j"]),
    ("rus(",  ["r", "u.rup", "s.left"]),
    ("rus",   ["r", "u.ru", "s.right"]),
    ("ruth",  ["r", "u.ru", "th.over.skew30"]),
])
def test_r_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("luk",   ["l", "u.ru", "k"]),
    ("lug",   ["l", "u.ru", "g"]),
    ("lur",   ["l", "u.rur", "r"]),
    ("lul",   ["l", "u.rur", "l"]),
    ("lun",   ["l", "u.ru", "n"]),
    ("lum",   ["l", "u.ru", "m"]),
    ("lut",   ["l", "u.ru", "t"]),
    ("lud",   ["l", "u.ru", "d"]),
    ("lup",   ["l", "u.rup", "p"]),
    ("lub",   ["l", "u.rup", "b"]),
    ("luf",   ["l", "u.ru", "f"]),
    ("luv",   ["l", "u.ru", "v"]),
    ("lush",  ["l", "u.ru", "sh"]),
    ("luch",  ["l", "u.ru", "ch"]),
    ("luj",   ["l", "u.ru", "j"]),
    ("lus(",  ["l", "u.rup", "s.left"]),
    ("lus",   ["l", "u.ru", "s.right"]),
    ("luth",  ["l", "u.ru", "th.over.skew30"]),
])
def test_l_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nuk",  ["n", "u.nuk", "k"]),
    ("nug",  ["n", "u.nuk", "g"]),
    ("nur",  ["n", "u.nu", "r"]),
    ("nul",  ["n", "u.nu", "l"]),
    ("nun",  ["n", "u.nu", "n"]),
    ("num",  ["n", "u.nu", "m"]),
    ("nut",  ["n", "u.nut", "t"]),
    ("nud",  ["n", "u.nut", "d"]),
    ("nup",  ["n", "u.nup", "p"]),
    ("nub",  ["n", "u.nup", "b"]),
    ("nuf",  ["n", "u.nu", "f"]),
    ("nuv",  ["n", "u.nu", "v"]),
    ("nush", ["n", "u.nu", "sh"]),
    ("nuch", ["n", "u.nu", "ch"]),
    ("nuj",  ["n", "u.nu", "j"]),
    ("nus(", ["n", "u.nup", "s.left"]),
    ("nus",  ["n", "u.nu", "s.right"]),
    ("nuth", ["n", "u.nut", "th.over.skew30"]),
])
def test_n_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("muk",  ["m", "u.nuk", "k"]),
    ("mug",  ["m", "u.nuk", "g"]),
    ("mur",  ["m", "u.nu", "r"]),
    ("mul",  ["m", "u.nu", "l"]),
    ("mun",  ["m", "u.nu", "n"]),
    ("mum",  ["m", "u.nu", "m"]),
    ("mut",  ["m", "u.nut", "t"]),
    ("mud",  ["m", "u.nut", "d"]),
    ("mup",  ["m", "u.nup", "p"]),
    ("mub",  ["m", "u.nup", "b"]),
    ("muf",  ["m", "u.nu", "f"]),
    ("muv",  ["m", "u.nu", "v"]),
    ("mush", ["m", "u.nu", "sh"]),
    ("much", ["m", "u.nu", "ch"]),
    ("muj",  ["m", "u.nu", "j"]),
    ("mus(", ["m", "u.nup", "s.left"]),
    ("mus",  ["m", "u.nu", "s.right"]),
    ("muth", ["m", "u.nut", "th.over.skew30"]),
])
def test_m_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
