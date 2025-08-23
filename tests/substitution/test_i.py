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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kir",  ["k.cut", "i.kir", "r"]),
    ("kil",  ["k.cut", "i.kir", "l"]),
    ("kin",  ["k.cut", "i.kin", "n"]),
    ("kim",  ["k.cut", "i.kin", "m"]),
    ("kit",  ["k.cut", "i.kin", "t"]),
    ("kid",  ["k.cut", "i.kin", "d"]),
    ("kif",  ["k.cut", "i.kin", "f"]),
    ("kiv",  ["k.cut", "i.kin", "v"]),
    ("kis)", ["k.cut", "i.kin", "s.right"]),
])
def test_k_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("gir",  ["g.cut", "i.kir", "r"]),
    ("gil",  ["g.cut", "i.kir", "l"]),
    ("gin",  ["g.cut", "i.kin", "n"]),
    ("gim",  ["g.cut", "i.kin", "m"]),
    ("git",  ["g.cut", "i.kin", "t"]),
    ("gid",  ["g.cut", "i.kin", "d"]),
    ("gif",  ["g.cut", "i.kin", "f"]),
    ("giv",  ["g.cut", "i.kin", "v"]),
    ("gis)", ["g.cut", "i.kin", "s.right"]),
])
def test_g_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("rik",   ["r", "i.rik", "k"]),
    ("rig",   ["r", "i.rik", "g"]),
    ("rir",   ["r", "i.ri", "r"]),
    ("ril",   ["r", "i.ri", "l"]),
    ("rin",   ["r", "i.ri", "n"]),
    ("rim",   ["r", "i.ri", "m"]),
    ("rit",   ["r", "i.ri", "t"]),
    ("rid",   ["r", "i.ri", "d"]),
    ("rip",   ["r", "i.ri", "p"]),
    ("rib",   ["r", "i.ri", "b"]),
    ("rif",   ["r", "i.ri", "f.cut"]),
    ("riv",   ["r", "i.ri", "v.cut"]),
    ("rish",  ["r", "i.ri", "sh"]),
    ("rich",  ["r", "i.ri", "ch"]),
    ("rij",   ["r", "i.ri", "j"]),
    ("ris)",  ["r", "i.ri", "s.right.cut"]),
    ("ris",   ["r", "i.ri", "s.left"]),
    ("rith",  ["r", "i.ri", "th.under"]),
])
def test_r_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("lik",   ["l", "i.rik", "k"]),
    ("lig",   ["l", "i.rik", "g"]),
    ("lir",   ["l", "i.ri", "r"]),
    ("lil",   ["l", "i.ri", "l"]),
    ("lin",   ["l", "i.ri", "n"]),
    ("lim",   ["l", "i.ri", "m"]),
    ("lit",   ["l", "i.ri", "t"]),
    ("lid",   ["l", "i.ri", "d"]),
    ("lip",   ["l", "i.ri", "p"]),
    ("lib",   ["l", "i.ri", "b"]),
    ("lif",   ["l", "i.ri", "f.cut"]),
    ("liv",   ["l", "i.ri", "v.cut"]),
    ("lish",  ["l", "i.ri", "sh"]),
    ("lich",  ["l", "i.ri", "ch"]),
    ("lij",   ["l", "i.ri", "j"]),
    ("lis)",  ["l", "i.ri", "s.right.cut"]),
    ("lis",   ["l", "i.ri", "s.left"]),
    ("lith",  ["l", "i.ri", "th.under"]),
])
def test_l_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


