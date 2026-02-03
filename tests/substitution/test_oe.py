import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("oe", ["o.oe", "e.oe"]),
])
def test_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("oer",   ["o.oe", "e.oer", "r.cut"]),
    ("oel",   ["o.oe", "e.oer", "l.cut"]),
    ("oen",   ["o.oe", "e.oen", "n"]),
    ("oem",   ["o.oe", "e.oen", "m"]),
    ("oep",   ["o.oep", "e.oep", "p"]),
    ("oeb",   ["o.oep", "e.oep", "b"]),
    ("oef",   ["o.oe", "e.oef", "f.cut"]),
    ("oev",   ["o.oe", "e.oef", "v.cut"]),
    ("oes)",  ["o.oe", "e.oef", "s.right.cut"]),
    ("oes",   ["o.oep", "e.oep", "s.left"]),
])
def test_oe_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
