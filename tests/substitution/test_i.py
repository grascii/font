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
    ("ui",   ["u.cut", "i.ui"]),
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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pik",   ["p.cut", "i.pik", "k"]),
    ("pig",   ["p.cut", "i.pik", "g"]),
    ("pir",   ["p.cut", "i.pir", "r.cut"]),
    ("pil",   ["p.cut", "i.pir", "l.cut"]),
    ("pin",   ["p.cut", "i.pik", "n"]),
    ("pim",   ["p.cut", "i.pik", "m"]),
    ("pit",   ["p.cut", "i.pik", "t"]),
    ("pid",   ["p.cut", "i.pik", "d"]),
    ("pip",   ["p.cut", "i.pi", "p"]),
    ("pib",   ["p.cut", "i.pi", "b"]),
    ("pis",   ["p.cut", "i.pi", "s.left"]),
])
def test_p_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("bik",   ["b.cut", "i.pik", "k"]),
    ("big",   ["b.cut", "i.pik", "g"]),
    ("bir",   ["b.cut", "i.pir", "r.cut"]),
    ("bil",   ["b.cut", "i.pir", "l.cut"]),
    ("bin",   ["b.cut", "i.pik", "n"]),
    ("bim",   ["b.cut", "i.pik", "m"]),
    ("bit",   ["b.cut", "i.pik", "t"]),
    ("bid",   ["b.cut", "i.pik", "d"]),
    ("bip",   ["b.cut", "i.pi", "p"]),
    ("bib",   ["b.cut", "i.pi", "b"]),
    ("bis",   ["b.cut", "i.pi", "s.left"]),
])
def test_b_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fik",   ["f", "i.fi", "k"]),
    ("fig",   ["f", "i.fi", "g"]),
    ("fir",   ["f", "i.fi", "r"]),
    ("fil",   ["f", "i.fi", "l"]),
    ("fin",   ["f", "i.fi", "n"]),
    ("fim",   ["f", "i.fi", "m"]),
    ("fit",   ["f", "i.fit", "t"]),
    ("fid",   ["f", "i.fit", "d"]),
    ("fip",   ["f", "i.fip", "p"]),
    ("fib",   ["f", "i.fip", "b"]),
    ("fif",   ["f", "i.fi", "f"]),
    ("fiv",   ["f", "i.fi", "v"]),
    ("fis)",  ["f", "i.fi", "s.right"]),
])
def test_f_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("vik",   ["v", "i.fi", "k"]),
    ("vig",   ["v", "i.fi", "g"]),
    ("vir",   ["v", "i.fi", "r"]),
    ("vil",   ["v", "i.fi", "l"]),
    ("vin",   ["v", "i.fi", "n"]),
    ("vim",   ["v", "i.fi", "m"]),
    ("vit",   ["v", "i.fit", "t"]),
    ("vid",   ["v", "i.fit", "d"]),
    ("vip",   ["v", "i.fip", "p"]),
    ("vib",   ["v", "i.fip", "b"]),
    ("vif",   ["v", "i.fi", "f"]),
    ("viv",   ["v", "i.fi", "v"]),
    ("vis)",  ["v", "i.fi", "s.right"]),
])
def test_v_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shik",   ["sh", "i.chik", "k"]),
    ("shig",   ["sh", "i.chik", "g"]),
    ("shir",   ["sh", "i.chir", "r.cut"]),
    ("shil",   ["sh", "i.chir", "l.cut"]),
    ("shin",   ["sh", "i.chik", "n"]),
    ("shim",   ["sh", "i.chik", "m"]),
    ("shit",   ["sh", "i.chik", "t"]),
    ("shid",   ["sh", "i.chik", "d"]),
    ("ship",   ["sh", "i.chip", "p"]),
    ("shib",   ["sh", "i.chip", "b"]),
    ("shif",   ["sh", "i.chif", "f"]),
    ("shiv",   ["sh", "i.chif", "v"]),
    ("shis",   ["sh", "i.chif", "s.right"]),
])
def test_sh_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("chik",   ["ch", "i.chik", "k"]),
    ("chig",   ["ch", "i.chik", "g"]),
    ("chir",   ["ch", "i.chir", "r.cut"]),
    ("chil",   ["ch", "i.chir", "l.cut"]),
    ("chin",   ["ch", "i.chik", "n"]),
    ("chim",   ["ch", "i.chik", "m"]),
    ("chit",   ["ch", "i.chik", "t"]),
    ("chid",   ["ch", "i.chik", "d"]),
    ("chip",   ["ch", "i.chip", "p"]),
    ("chib",   ["ch", "i.chip", "b"]),
    ("chif",   ["ch", "i.chif", "f"]),
    ("chiv",   ["ch", "i.chif", "v"]),
    ("chis",   ["ch", "i.chif", "s.right"]),
])
def test_ch_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("jik",   ["j", "i.chik", "k"]),
    ("jig",   ["j", "i.chik", "g"]),
    ("jir",   ["j", "i.chir", "r.cut"]),
    ("jil",   ["j", "i.chir", "l.cut"]),
    ("jin",   ["j", "i.chik", "n"]),
    ("jim",   ["j", "i.chik", "m"]),
    ("jit",   ["j", "i.chik", "t"]),
    ("jid",   ["j", "i.chik", "d"]),
    ("jip",   ["j", "i.chip", "p"]),
    ("jib",   ["j", "i.chip", "b"]),
    ("jif",   ["j", "i.chif", "f"]),
    ("jiv",   ["j", "i.chif", "v"]),
    ("jis",   ["j", "i.chif", "s.right"]),
])
def test_j_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)ik",   ["s.right", "i.fi", "k"]),
    ("s)ig",   ["s.right", "i.fi", "g"]),
    ("s)ir",   ["s.right", "i.fi", "r"]),
    ("s)il",   ["s.right", "i.fi", "l"]),
    ("s)in",   ["s.right", "i.fi", "n"]),
    ("s)im",   ["s.right", "i.fi", "m"]),
    ("s)it",   ["s.right", "i.fit", "t"]),
    ("s)id",   ["s.right", "i.fit", "d"]),
    ("s)if",   ["s.right", "i.fi", "f"]),
    ("s)iv",   ["s.right", "i.fi", "v"]),
    ("s)is)",  ["s.right", "i.fi", "s.right"]),
])
def test_sR_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s(ir",   ["s.left.cut", "i.pir", "r.cut"]),
    ("s(il",   ["s.left.cut", "i.pir", "l.cut"]),
    ("s(ip",   ["s.left.cut", "i.pi", "p"]),
    ("s(ib",   ["s.left.cut", "i.pi", "b"]),
    ("s(is",   ["s.left.cut", "i.pi", "s.left"]),
])
def test_sL_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("thin",   ["th.over", "i.tni", "n"]),
    ("thim",   ["th.over", "i.tni", "m"]),
    ("thif",   ["th.over", "i.tni", "f"]),
    ("thiv",   ["th.over", "i.tni", "v"]),
    ("this)",  ["th.over", "i.tni", "s.right"]),
])
def test_thO_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("thir",   ["th.under", "i.ntir", "r"]),
    ("thil",   ["th.under", "i.ntir", "l"]),
])
def test_thU_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uir",  ["u.cut", "i.uit", "r.cut"]),
    ("uil",  ["u.cut", "i.uit", "l.cut"]),
    ("uin",  ["u.cut", "i.uit", "n"]),
    ("uim",  ["u.cut", "i.uit", "m"]),
    ("uit",  ["u.cut", "i.uit", "t"]),
    ("uid",  ["u.cut", "i.uit", "d"]),
    ("uip",  ["u.cut", "i.uip", "p"]),
    ("uib",  ["u.cut", "i.uip", "b"]),
    ("uif",  ["u.cut", "i.uit", "f"]),
    ("uiv",  ["u.cut", "i.uit", "v"]),
    ("uis)", ["u.cut", "i.uit", "s.right"]),
])
def test_u_i(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
