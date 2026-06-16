import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("a&e", ["ae"]),
])
def test_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("a&en", ["ae.aen", "n"]),
    ("a&em", ["ae.aen", "m"]),
    ("a&et", ["ae.aet", "t"]),
    ("a&ed", ["ae.aet", "d"]),
])
def test_ae_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ka&e",   ["k", "ae.kae"]),
    ("ga&e",   ["g", "ae.kae"]),
    ("ra&e",   ["r", "ae.rae"]),
    ("la&e",   ["l", "ae.rae"]),
    ("ta&e",   ["t", "ae.tae"]),
    ("da&e",   ["d", "ae.tae"]),
    ("s(a&e",  ["s.left", "ae.sLae"]),
    ("nta&e",  ["nt", "ae.ntae"]),
    ("nda&e",  ["nt", "ae.ntae"]),
    ("mta&e",  ["mt", "ae.ntae"]),
    ("mda&e",  ["mt", "ae.ntae"]),
])
def test_ae_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ka&en", ["k", "ae.kaen", "n"]),
    ("ka&em", ["k", "ae.kaen", "m"]),
    ("ka&et", ["k", "ae.kaet", "t"]),
    ("ka&ed", ["k", "ae.kaet", "d"]),
])
def test_k_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ga&en", ["g", "ae.kaen", "n"]),
    ("ga&em", ["g", "ae.kaen", "m"]),
    ("ga&et", ["g", "ae.kaet", "t"]),
    ("ga&ed", ["g", "ae.kaet", "d"]),
])
def test_g_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ra&er",  ["r", "ae.raer", "r"]),
    ("ra&el",  ["r", "ae.raer", "l"]),
    ("ra&en",  ["r", "a.ran", "e.ren", "n"]),
    ("ra&em",  ["r", "a.ran", "e.ren", "m"]),
    ("ra&et",  ["r", "ae.raet", "t"]),
    ("ra&ed",  ["r", "ae.raet", "d"]),
    ("ra&eng", ["r", "a.rang", "e.reng", "ng"]),
    ("ra&enk", ["r", "a.rang", "e.reng", "nk"]),
])
def test_r_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("la&er",  ["l", "ae.raer", "r"]),
    ("la&el",  ["l", "ae.raer", "l"]),
    ("la&en",  ["l", "a.ran", "e.ren", "n"]),
    ("la&em",  ["l", "a.ran", "e.ren", "m"]),
    ("la&et",  ["l", "ae.raet", "t"]),
    ("la&ed",  ["l", "ae.raet", "d"]),
    ("la&eng", ["l", "a.rang", "e.reng", "ng"]),
    ("la&enk", ["l", "a.rang", "e.reng", "nk"]),
])
def test_l_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("na&ep",  ["n", "ae.naep", "p"]),
    ("na&eb",  ["n", "ae.naep", "b"]),
    ("na&ef",  ["n", "ae.naef", "f.cut"]),
    ("na&ev",  ["n", "ae.naef", "v.cut"]),
    ("na&es",  ["n", "ae.naep", "s.left"]),
])
def test_n_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ma&ep",  ["m", "ae.naep", "p"]),
    ("ma&eb",  ["m", "ae.naep", "b"]),
    ("ma&ef",  ["m", "ae.naef", "f.cut"]),
    ("ma&ev",  ["m", "ae.naef", "v.cut"]),
    ("ma&es",  ["m", "ae.naep", "s.left"]),
])
def test_m_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ta&ek",  ["t", "ae.taek", "k"]),
    ("ta&eg",  ["t", "ae.taek", "g"]),
    ("ta&er",  ["t", "ae.taer", "r"]),
    ("ta&el",  ["t", "ae.taer", "l"]),
    ("ta&et",  ["t", "ae.taet", "t"]),
    ("ta&ed",  ["t", "ae.taet", "d"]),
    ("ta&etn", ["t", "ae.taet", "tn.skew45"]),
    ("ta&edn", ["t", "ae.taet", "tn.skew45"]),
    ("ta&etm", ["t", "ae.taet", "tm.skew45"]),
    ("ta&edm", ["t", "ae.taet", "tm.skew45"]),
])
def test_t_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("da&ek",  ["d", "ae.taek", "k"]),
    ("da&eg",  ["d", "ae.taek", "g"]),
    ("da&er",  ["d", "ae.taer", "r"]),
    ("da&el",  ["d", "ae.taer", "l"]),
    ("da&et",  ["d", "ae.taet", "t"]),
    ("da&ed",  ["d", "ae.taet", "d"]),
    ("da&etn", ["d", "ae.taet", "tn.skew45"]),
    ("da&edn", ["d", "ae.taet", "tn.skew45"]),
    ("da&etm", ["d", "ae.taet", "tm.skew45"]),
    ("da&edm", ["d", "ae.taet", "tm.skew45"]),
])
def test_d_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pa&en",  ["p.cut", "a.pan", "e.pen", "n"]),
    ("pa&em",  ["p.cut", "a.pan", "e.pen", "m"]),
    ("pa&et",  ["p.cut", "ae.paet", "t"]),
    ("pa&ed",  ["p.cut", "ae.paet", "d"]),
    ("pa&ep",  ["p", "ae.paep", "p"]),
    ("pa&eb",  ["p", "ae.paep", "b"]),
    ("pa&es",  ["p", "ae.paep", "s.left"]),
    ("pa&eng", ["p.cut", "a.pang", "e.peng", "ng"]),
    ("pa&enk", ["p.cut", "a.pang", "e.peng", "nk"]),
])
def test_p_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ba&en",  ["b.cut", "a.pan", "e.pen", "n"]),
    ("ba&em",  ["b.cut", "a.pan", "e.pen", "m"]),
    ("ba&et",  ["b.cut", "ae.paet", "t"]),
    ("ba&ed",  ["b.cut", "ae.paet", "d"]),
    ("ba&ep",  ["b", "ae.paep", "p"]),
    ("ba&eb",  ["b", "ae.paep", "b"]),
    ("ba&es",  ["b", "ae.paep", "s.left"]),
    ("ba&eng", ["b.cut", "a.pang", "e.peng", "ng"]),
    ("ba&enk", ["b.cut", "a.pang", "e.peng", "nk"]),
])
def test_b_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fa&er",  ["f", "ae.faer", "r.cut"]),
    ("fa&el",  ["f", "ae.faer", "l.cut"]),
    ("fa&en",  ["f", "a.fan", "e.fen", "n"]),
    ("fa&em",  ["f", "a.fan", "e.fen", "m"]),
    ("fa&et",  ["f", "a.fat", "e.fet", "t"]),
    ("fa&ed",  ["f", "a.fat", "e.fet", "d"]),
    ("fa&ent", ["f", "a.fan", "e.fen", "nt"]),
    ("fa&end", ["f", "a.fan", "e.fen", "nt"]),
    ("fa&emt", ["f", "a.fan", "e.fen", "mt"]),
    ("fa&emd", ["f", "a.fan", "e.fen", "mt"]),
])
def test_f_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("va&er",  ["v", "ae.faer", "r.cut"]),
    ("va&el",  ["v", "ae.faer", "l.cut"]),
    ("va&en",  ["v", "a.fan", "e.fen", "n"]),
    ("va&em",  ["v", "a.fan", "e.fen", "m"]),
    ("va&et",  ["v", "a.fat", "e.fet", "t"]),
    ("va&ed",  ["v", "a.fat", "e.fet", "d"]),
    ("va&ent", ["v", "a.fan", "e.fen", "nt"]),
    ("va&end", ["v", "a.fan", "e.fen", "nt"]),
    ("va&emt", ["v", "a.fan", "e.fen", "mt"]),
    ("va&emd", ["v", "a.fan", "e.fen", "mt"]),
])
def test_v_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)a&er",  ["s.right", "ae.faer", "r.cut"]),
    ("s)a&el",  ["s.right", "ae.faer", "l.cut"]),
    ("s)a&en",  ["s.right", "a.fan", "e.fen", "n"]),
    ("s)a&em",  ["s.right", "a.fan", "e.fen", "m"]),
    ("s)a&et",  ["s.right", "a.fat", "e.fet", "t"]),
    ("s)a&ed",  ["s.right", "a.fat", "e.fet", "d"]),
    ("s)a&ent", ["s.right", "a.fan", "e.fen", "nt"]),
    ("s)a&end", ["s.right", "a.fan", "e.fen", "nt"]),
    ("s)a&emt", ["s.right", "a.fan", "e.fen", "mt"]),
    ("s)a&emd", ["s.right", "a.fan", "e.fen", "mt"]),
])
def test_sR_ae(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

