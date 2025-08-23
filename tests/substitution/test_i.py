import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ik",   ["i.ik", "k"]),
    ("ig",   ["i.ik", "g"]),
    ("ir",   ["i.ir", "r"]),
    ("il",   ["i.ir", "l"]),
    ("in",   ["i.in", "n"]),
    ("im",   ["i.in", "m"]),
    ("it",   ["i.it", "t"]),
    ("id",   ["i.it", "d"]),
    ("ip",   ["i.ip", "p"]),
    ("ib",   ["i.ip", "b"]),
    ("if",   ["i.if", "f.cut"]),
    ("iv",   ["i.if", "v.cut"]),
    ("ish",  ["i.ich", "sh"]),
    ("ich",  ["i.ich", "ch"]),
    ("ij",   ["i.ich", "j"]),
    ("is)",  ["i.if", "s.right.cut"]),
    ("is(",  ["i.ip", "s.left"]),
])
def test_i_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ki",   ["k.cut", "i.ki"]),
    ("gi",   ["g.cut", "i.ki"]),
    ("ri",   ["r", "i.ri"]),
    ("li",   ["l", "i.ri"]),
    ("ni",   ["n", "i.ni"]),
    ("mi",   ["m", "i.ni"]),
    ("ti",   ["t", "i.ti"]),
    ("di",   ["d", "i.ti"]),
    ("pi",   ["p.cut", "i.pi"]),
    ("bi",   ["b.cut", "i.pi"]),
    ("fi",   ["f", "i.fi"]),
    ("vi",   ["v", "i.fi"]),
    ("si",   ["s.right", "i.fi"]),
    ("s(i",  ["s.left.cut", "i.pi"]),
    ("shi",  ["sh", "i.chi"]),
    ("chi",  ["ch", "i.chi"]),
    ("ji",   ["j", "i.chi"]),
    ("thi",  ["th.over", "i.tni"]),
    ("ngi",  ["ng", "i.ngi"]),
    ("nki",  ["nk", "i.ngi"]),
])
def test_i_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
