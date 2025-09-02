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

