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

