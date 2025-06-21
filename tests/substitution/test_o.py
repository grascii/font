import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ok",   ["o.ok", "k"]),
    ("og",   ["o.ok", "g"]),
    ("or",   ["o.or", "r.cut"]),
    ("ol",   ["o.ol", "l.cut"]),
    ("on",   ["o.on", "n"]),
    ("om",   ["o.on", "m"]),
    ("ot",   ["o.ot", "t"]),
    ("od",   ["o.ot", "d"]),
    ("op",   ["o.op", "p"]),
    ("ob",   ["o.op", "b"]),
    ("of",   ["o", "f"]),
    ("ov",   ["o", "v"]),
    ("osh",  ["o", "sh"]),
    ("och",  ["o", "ch"]),
    ("oj",   ["o", "j"]),
    ("os)",  ["o", "s.right"]),
    ("os(",  ["o.op", "s.left"]),
    ("oth(", ["o", "th.over"]),
    # ("oth)", ["o", "th.under"]),
    ("ong",  ["o.ong", "ng"]),
    ("onk",  ["o.ong", "nk"]),
])
def test_o_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
