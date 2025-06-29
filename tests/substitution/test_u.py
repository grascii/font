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
