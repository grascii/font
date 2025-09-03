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

