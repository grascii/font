import pytest
from shape import shape

@pytest.mark.parametrize("text,expected_glyphs", [
    ("ka&'", ["k", "a.ka", "eadot"]),
    ("ga&'", ["g", "a.ka", "eadot"]),
    ("ra&'", ["r", "a.ra", "eadot"]),
    ("la&'", ["l", "a.ra", "eadot"]),
    ("na&'", ["n", "a.na", "eadot"]),
    ("ma&'", ["m", "a.na", "eadot"]),
    ("ta&'", ["t", "a.ta", "eadot"]),
    ("da&'", ["d", "a.ta", "eadot"]),
    ("pa&'", ["p", "a.pa", "eadot"]),
    ("ba&'", ["b", "a.ba", "eadot"]),
    ("s(a&'", ["s.left", "a.sLa", "eadot"]),
    ("sha&'", ["sh", "a.cha", "eadot"]),
    ("cha&'", ["ch", "a.cha", "eadot"]),
    ("ja&'", ["j", "a.cha", "eadot"]),
    ("tha&'", ["th.over", "a.thOa", "eadot"]),
    ("th)a&'", ["th.under", "a.thUa", "eadot"]),
])
def test_ea_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ra&'k",  ["r", "a.rak", "eadot", "k"]),
    ("ra&'g",  ["r", "a.rak", "eadot", "g"]),
    ("ra&'r",  ["r", "a.rar", "eadot", "r"]),
    ("ra&'l",  ["r", "a.rar", "eadot", "l"]),
    ("ra&'n",  ["r", "a.ran", "eadot", "n"]),
    ("ra&'m",  ["r", "a.ran", "eadot", "m"]),
    ("ra&'t",  ["r", "a.rat", "eadot", "t"]),
    ("ra&'d",  ["r", "a.rat", "eadot", "d"]),
    ("ra&'p",  ["r", "a.rap", "eadot", "p"]),
    ("ra&'b",  ["r", "a.rap", "eadot", "b"]),
    ("ra&'sh", ["r", "a.rach", "eadot", "sh"]),
    ("ra&'ch", ["r", "a.rach", "eadot", "ch"]),
    ("ra&'j",  ["r", "a.rach", "eadot", "j"]),
    ("ra&'s",  ["r", "a.rap", "eadot", "s.left"]),
])
def test_r_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("la&'k",  ["l", "a.rak", "eadot", "k"]),
    ("la&'g",  ["l", "a.rak", "eadot", "g"]),
    ("la&'r",  ["l", "a.rar", "eadot", "r"]),
    ("la&'l",  ["l", "a.rar", "eadot", "l"]),
    ("la&'n",  ["l", "a.ran", "eadot", "n"]),
    ("la&'m",  ["l", "a.ran", "eadot", "m"]),
    ("la&'t",  ["l", "a.rat", "eadot", "t"]),
    ("la&'d",  ["l", "a.rat", "eadot", "d"]),
    ("la&'p",  ["l", "a.rap", "eadot", "p"]),
    ("la&'b",  ["l", "a.rap", "eadot", "b"]),
    ("la&'sh", ["l", "a.rach", "eadot", "sh"]),
    ("la&'ch", ["l", "a.rach", "eadot", "ch"]),
    ("la&'j",  ["l", "a.rach", "eadot", "j"]),
    ("la&'s", ["l", "a.rap", "eadot", "s.left"]),
])
def test_l_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("na&'k",  ["n", "a.nak", "eadot", "k"]),
    ("na&'g",  ["n", "a.nak", "eadot", "g"]),
    ("na&'r",  ["n", "a.nar", "eadot", "r"]),
    ("na&'l",  ["n", "a.nar", "eadot", "l"]),
    ("na&'n",  ["n", "a.nan", "eadot", "n"]),
    ("na&'m",  ["n", "a.nan", "eadot", "m"]),
    ("na&'t",  ["n", "a.nat", "eadot", "t"]),
    ("na&'d",  ["n", "a.nat", "eadot", "d"]),
    ("na&'sh", ["n", "a.nach", "eadot", "sh"]),
    ("na&'ch", ["n", "a.nach", "eadot", "ch"]),
    ("na&'j",  ["n", "a.nach", "eadot", "j"]),
])
def test_n_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ma&'k",  ["m", "a.nak", "eadot", "k"]),
    ("ma&'g",  ["m", "a.nak", "eadot", "g"]),
    ("ma&'r",  ["m", "a.nar", "eadot", "r"]),
    ("ma&'l",  ["m", "a.nar", "eadot", "l"]),
    ("ma&'n",  ["m", "a.nan", "eadot", "n"]),
    ("ma&'m",  ["m", "a.nan", "eadot", "m"]),
    ("ma&'t",  ["m", "a.nat", "eadot", "t"]),
    ("ma&'d",  ["m", "a.nat", "eadot", "d"]),
    ("ma&'sh", ["m", "a.nach", "eadot", "sh"]),
    ("ma&'ch", ["m", "a.nach", "eadot", "ch"]),
    ("ma&'j",  ["m", "a.nach", "eadot", "j"]),
])
def test_m_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ta&'k",  ["t", "a.tak", "eadot", "k"]),
    ("ta&'g",  ["t", "a.tak", "eadot", "g"]),
    ("ta&'r",  ["t", "a.tar", "eadot", "r"]),
    ("ta&'l",  ["t", "a.tar", "eadot", "l"]),
    ("ta&'n",  ["t", "a.tan", "eadot", "n"]),
    ("ta&'m",  ["t", "a.tan", "eadot", "m"]),
    ("ta&'t",  ["t", "a.tat", "eadot", "t"]),
    ("ta&'d",  ["t", "a.tat", "eadot", "d"]),
    ("ta&'sh", ["t", "a.tach", "eadot", "sh"]),
    ("ta&'ch", ["t", "a.tach", "eadot", "ch"]),
    ("ta&'j",  ["t", "a.tach", "eadot", "j"]),
])
def test_t_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("da&'k",  ["d", "a.tak", "eadot", "k"]),
    ("da&'g",  ["d", "a.tak", "eadot", "g"]),
    ("da&'r",  ["d", "a.tar", "eadot", "r"]),
    ("da&'l",  ["d", "a.tar", "eadot", "l"]),
    ("da&'n",  ["d", "a.tan", "eadot", "n"]),
    ("da&'m",  ["d", "a.tan", "eadot", "m"]),
    ("da&'t",  ["d", "a.tat", "eadot", "t"]),
    ("da&'d",  ["d", "a.tat", "eadot", "d"]),
    ("da&'sh", ["d", "a.tach", "eadot", "sh"]),
    ("da&'ch", ["d", "a.tach", "eadot", "ch"]),
    ("da&'j",  ["d", "a.tach", "eadot", "j"]),
])
def test_d_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pa&'r",  ["p.cut", "a.par", "eadot", "r"]),
    ("pa&'l",  ["p.cut", "a.par", "eadot", "l"]),
    ("pa&'n",  ["p.cut", "a.pan", "eadot", "n"]),
    ("pa&'m",  ["p.cut", "a.pan", "eadot", "m"]),
    ("pa&'t",  ["p", "a.pat", "eadot", "t"]),
    ("pa&'d",  ["p", "a.pat", "eadot", "d"]),
    ("pa&'sh", ["p", "a.pach", "eadot", "sh"]),
    ("pa&'ch", ["p", "a.pach", "eadot", "ch"]),
    ("pa&'j",  ["p", "a.pach", "eadot", "j"]),
    ("pa&'s",  ["p", "a.pap", "eadot", "s.left"]),
])
def test_p_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ba&'r",  ["b.cut", "a.par", "eadot", "r"]),
    ("ba&'l",  ["b.cut", "a.par", "eadot", "l"]),
    ("ba&'n",  ["b.cut", "a.pan", "eadot", "n"]),
    ("ba&'m",  ["b.cut", "a.pan", "eadot", "m"]),
    ("ba&'t",  ["b", "a.pat", "eadot", "t"]),
    ("ba&'d",  ["b", "a.pat", "eadot", "d"]),
    ("ba&'sh", ["b", "a.pach", "eadot", "sh"]),
    ("ba&'ch", ["b", "a.pach", "eadot", "ch"]),
    ("ba&'j",  ["b", "a.pach", "eadot", "j"]),
    ("ba&'s",  ["b", "a.pap", "eadot", "s.left"]),
])
def test_b_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fa&'r",  ["f", "a.far", "eadot", "r"]),
    ("fa&'l",  ["f", "a.far", "eadot", "l"]),
    ("fa&'n",  ["f", "a.fan", "eadot", "n"]),
    ("fa&'m",  ["f", "a.fan", "eadot", "m"]),
    ("fa&'t",  ["f", "a.fat", "eadot", "t"]),
    ("fa&'d",  ["f", "a.fat", "eadot", "d"]),
    ("fa&'sh", ["f", "a.fach", "eadot", "sh"]),
    ("fa&'ch", ["f", "a.fach", "eadot", "ch"]),
    ("fa&'j",  ["f", "a.fach", "eadot", "j"]),
    ("fa&'s",  ["f", "a.faf", "eadot", "s.right"]),
])
def test_f_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("va&'r",  ["v", "a.far", "eadot", "r"]),
    ("va&'l",  ["v", "a.far", "eadot", "l"]),
    ("va&'n",  ["v", "a.fan", "eadot", "n"]),
    ("va&'m",  ["v", "a.fan", "eadot", "m"]),
    ("va&'t",  ["v", "a.fat", "eadot", "t"]),
    ("va&'d",  ["v", "a.fat", "eadot", "d"]),
    ("va&'sh", ["v", "a.fach", "eadot", "sh"]),
    ("va&'ch", ["v", "a.fach", "eadot", "ch"]),
    ("va&'j",  ["v", "a.fach", "eadot", "j"]),
    ("va&'s",  ["v", "a.faf", "eadot", "s.right"]),
])
def test_v_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sha&'n",  ["sh", "a.chan", "eadot", "n"]),
    ("sha&'m",  ["sh", "a.chan", "eadot", "m"]),
    ("sha&'t",  ["sh", "a.chat", "eadot", "t"]),
    ("sha&'d",  ["sh", "a.chat", "eadot", "d"]),
    ("sha&'sh", ["sh", "a.chach", "eadot", "sh"]),
    ("sha&'ch", ["sh", "a.chach", "eadot", "ch"]),
    ("sha&'j",  ["sh", "a.chach", "eadot", "j"]),
])
def test_sh_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("cha&'n",  ["ch", "a.chan", "eadot", "n"]),
    ("cha&'m",  ["ch", "a.chan", "eadot", "m"]),
    ("cha&'t",  ["ch", "a.chat", "eadot", "t"]),
    ("cha&'d",  ["ch", "a.chat", "eadot", "d"]),
    ("cha&'sh", ["ch", "a.chach", "eadot", "sh"]),
    ("cha&'ch", ["ch", "a.chach", "eadot", "ch"]),
    ("cha&'j",  ["ch", "a.chach", "eadot", "j"]),
])
def test_ch_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ja&'n",  ["j", "a.chan", "eadot", "n"]),
    ("ja&'m",  ["j", "a.chan", "eadot", "m"]),
    ("ja&'t",  ["j", "a.chat", "eadot", "t"]),
    ("ja&'d",  ["j", "a.chat", "eadot", "d"]),
    ("ja&'sh", ["j", "a.chach", "eadot", "sh"]),
    ("ja&'ch", ["j", "a.chach", "eadot", "ch"]),
    ("ja&'j",  ["j", "a.chach", "eadot", "j"]),
])
def test_j_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th(a&'n",   ["th.over", "a.tnan", "eadot", "n"]),
    ("th(a&'m",   ["th.over", "a.tnan", "eadot", "m"]),
])
def test_thO_ea(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
