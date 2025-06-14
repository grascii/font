import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ek",   ["e.ek", "k"]),
    ("eg",   ["e.ek", "g"]),
    ("er",   ["e.er", "r"]),
    ("el",   ["e.er", "l"]),
    ("en",   ["e.en", "n"]),
    ("em",   ["e.en", "m"]),
    ("et",   ["e.et", "t"]),
    ("ed",   ["e.et", "d"]),
    ("ep",   ["e.ep", "p"]),
    ("eb",   ["e.ep", "b"]),
    ("ef",   ["e.ef", "f"]),
    ("ev",   ["e.ef", "v"]),
    ("es",   ["e.esR", "s.right"]),
    ("es(",  ["e.ep", "s.left"]),
    ("esh",  ["e.ech", "sh"]),
    ("ech",  ["e.ech", "ch"]),
    ("ej",   ["e.ech", "j"]),
    ("eth",  ["e.ethO", "th.over"]),
    ("eth)", ["e.ethU", "th.under"]),
    ("eng",  ["e.eng", "ng"]),
    ("enk",  ["e.eng", "nk"]),
])
def test_e_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ke",   ["k", "e.ke"]),
    ("ge",   ["g", "e.ke"]),
    ("re",   ["r", "e.re"]),
    ("le",   ["l", "e.re"]),
    ("ne",   ["n", "e.ne"]),
    ("me",   ["m", "e.ne"]),
    ("te",   ["t", "e.te"]),
    ("de",   ["d", "e.te"]),
    ("pe",   ["p", "e.pe"]),
    ("be",   ["b", "e.pe"]),
    ("fe",   ["f", "e.fe"]),
    ("ve",   ["v", "e.fe"]),
    ("se",   ["s.right", "e.fe"]),
    ("s(e",  ["s.left", "e.sLe"]),
    ("she",  ["sh", "e.che"]),
    ("che",  ["ch", "e.che"]),
    ("je",   ["j", "e.che"]),
    ("the",  ["th.over", "e.thOe"]),
    ("th)e", ["th.under", "e.thUe"]),
    ("nge",  ["ng", "e.nge"]),
    ("nke",  ["nk", "e.nge"]),
])
def test_e_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kek",  ["k", "e.kek", "k"]),
    ("keg",  ["k", "e.kek", "g"]),
    ("ker",  ["k", "e.ker", "r"]),
    ("kel",  ["k", "e.ker", "l"]),
    ("ken",  ["k", "e.en", "n"]),
    ("kem",  ["k", "e.en", "m"]),
    ("ket",  ["k", "e.et", "t"]),
    ("ked",  ["k", "e.et", "d"]),
    ("kep",  ["k", "e.ep", "p"]),
    ("keb",  ["k", "e.ep", "b"]),
    ("kef",  ["k", "e.kef", "f.cut"]),
    ("kev",  ["k", "e.kef", "v.cut"]),
    ("kesh", ["k", "e.kech", "sh"]),
    ("kech", ["k", "e.kech", "ch"]),
    ("kej",  ["k", "e.kech", "j"]),
    ("kes",  ["k", "e.kef", "s.right.cut"]),
    ("kes(", ["k", "e.ep", "s.left"]),
    ("keng", ["k", "e.keng", "ng"]),
    ("kenk", ["k", "e.keng", "nk"]),
    ("keth", ["k", "e.ketn", "th.over.skew30"]),
])
def test_k_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("gek",  ["g", "e.kek", "k"]),
    ("geg",  ["g", "e.kek", "g"]),
    ("ger",  ["g", "e.ker", "r"]),
    ("gel",  ["g", "e.ker", "l"]),
    ("gen",  ["g", "e.en", "n"]),
    ("gem",  ["g", "e.en", "m"]),
    ("get",  ["g", "e.et", "t"]),
    ("ged",  ["g", "e.et", "d"]),
    ("gep",  ["g", "e.ep", "p"]),
    ("geb",  ["g", "e.ep", "b"]),
    ("gef",  ["g", "e.kef", "f.cut"]),
    ("gev",  ["g", "e.kef", "v.cut"]),
    ("gesh", ["g", "e.kech", "sh"]),
    ("gech", ["g", "e.kech", "ch"]),
    ("gej",  ["g", "e.kech", "j"]),
    ("ges",  ["g", "e.kef", "s.right.cut"]),
    ("ges(", ["g", "e.ep", "s.left"]),
    ("geng", ["g", "e.keng", "ng"]),
    ("genk", ["g", "e.keng", "nk"]),
    ("geth", ["g", "e.ketn", "th.over.skew30"]),
])
def test_g_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
