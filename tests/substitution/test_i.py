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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nik",   ["n", "i.ni", "k"]),
    ("nig",   ["n", "i.ni", "g"]),
    ("nir",   ["n", "i.nir", "r"]),
    ("nil",   ["n", "i.nir", "l"]),
    ("nin",   ["n", "i.ni", "n"]),
    ("nim",   ["n", "i.ni", "m"]),
    ("nit",   ["n", "i.ni", "t"]),
    ("nid",   ["n", "i.ni", "d"]),
    ("nip",   ["n", "i.nir", "p"]),
    ("nib",   ["n", "i.nir", "b"]),
    ("nif",   ["n", "i.nir", "f.cut"]),
    ("niv",   ["n", "i.nir", "v.cut"]),
    ("nis)",  ["n", "i.nir", "s.right.cut"]),
    ("nis",   ["n", "i.nir", "s.left"]),
])
def test_n_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mik",   ["m", "i.ni", "k"]),
    ("mig",   ["m", "i.ni", "g"]),
    ("mir",   ["m", "i.nir", "r"]),
    ("mil",   ["m", "i.nir", "l"]),
    ("min",   ["m", "i.ni", "n"]),
    ("mim",   ["m", "i.ni", "m"]),
    ("mit",   ["m", "i.ni", "t"]),
    ("mid",   ["m", "i.ni", "d"]),
    ("mip",   ["m", "i.nir", "p"]),
    ("mib",   ["m", "i.nir", "b"]),
    ("mif",   ["m", "i.nir", "f.cut"]),
    ("miv",   ["m", "i.nir", "v.cut"]),
    ("mis)",  ["m", "i.nir", "s.right.cut"]),
    ("mis",   ["m", "i.nir", "s.left"]),
])
def test_m_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tik",   ["t", "i.ti", "k"]),
    ("tig",   ["t", "i.ti", "g"]),
    ("tir",   ["t", "i.tir", "r"]),
    ("til",   ["t", "i.tir", "l"]),
    ("tin",   ["t", "i.tir", "n"]),
    ("tim",   ["t", "i.tir", "m"]),
    ("tit",   ["t", "i.ti", "t"]),
    ("tid",   ["t", "i.ti", "d"]),
    ("tip",   ["t", "i.tip", "p"]),
    ("tib",   ["t", "i.tip", "b"]),
    ("tif",   ["t", "i.tir", "f.cut"]),
    ("tiv",   ["t", "i.tir", "v.cut"]),
    ("tis)",  ["t", "i.tir", "s.right.cut"]),
    ("tis",   ["t", "i.tip", "s.left"]),
    ("tith",  ["t", "i.ti", "th.over"]),
])
def test_t_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("dik",   ["d", "i.ti", "k"]),
    ("dig",   ["d", "i.ti", "g"]),
    ("dir",   ["d", "i.tir", "r"]),
    ("dil",   ["d", "i.tir", "l"]),
    ("din",   ["d", "i.tir", "n"]),
    ("dim",   ["d", "i.tir", "m"]),
    ("dit",   ["d", "i.ti", "t"]),
    ("did",   ["d", "i.ti", "d"]),
    ("dip",   ["d", "i.tip", "p"]),
    ("dib",   ["d", "i.tip", "b"]),
    ("dif",   ["d", "i.tir", "f.cut"]),
    ("div",   ["d", "i.tir", "v.cut"]),
    ("dis)",  ["d", "i.tir", "s.right.cut"]),
    ("dis",   ["d", "i.tip", "s.left"]),
    ("dith",  ["d", "i.ti", "th.over"]),
])
def test_d_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


