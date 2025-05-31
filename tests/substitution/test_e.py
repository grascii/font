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
