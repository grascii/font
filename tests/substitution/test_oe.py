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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("koe",  ["k.cut", "o.koe", "e.oe"]),
    ("goe",  ["g.cut", "o.koe", "e.oe"]),
    ("roe",  ["r", "o.oe", "e.oe"]),
    ("loe",  ["l", "o.oe", "e.oe"]),
    ("noe",  ["n", "o.oe", "e.oe"]),
    ("moe",  ["m", "o.oe", "e.oe"]),
    ("toe",  ["t", "o.oe", "e.oe"]),
    ("doe",  ["d", "o.oe", "e.oe"]),
    ("poe",  ["p", "o.poe", "e.poe"]),
    ("boe",  ["b", "o.poe", "e.poe"]),
    ("foe",  ["f", "o.foe", "e.oe"]),
    ("voe",  ["v", "o.foe", "e.oe"]),
    ("soe",  ["s.right", "o.foe", "e.oe"]),
    ("s(oe", ["s.left", "o.sLoe", "e.sLoe"]),
    ("shoe", ["sh", "o.choe", "e.choe"]),
    ("choe", ["ch", "o.choe", "e.choe"]),
    ("joe",  ["j", "o.choe", "e.choe"]),
    ("thoe", ["th.over", "o.oe", "e.oe"]),
])
def test_oe_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("koer",  ["k.cut", "o.koer", "e.koer", "r.cut"]),
    ("koel",  ["k.cut", "o.koer", "e.koer", "l.cut"]),
    ("koen",  ["k.cut", "o.koen", "e.koen", "n"]),
    ("koem",  ["k.cut", "o.koen", "e.koen", "m"]),
    ("koet",  ["k.cut", "o.koet", "e.koet", "t"]),
    ("koed",  ["k.cut", "o.koet", "e.koet", "d"]),
])
def test_k_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("goer",  ["g.cut", "o.koer", "e.koer", "r.cut"]),
    ("goel",  ["g.cut", "o.koer", "e.koer", "l.cut"]),
    ("goen",  ["g.cut", "o.koen", "e.koen", "n"]),
    ("goem",  ["g.cut", "o.koen", "e.koen", "m"]),
    ("goet",  ["g.cut", "o.koet", "e.koet", "t"]),
    ("goed",  ["g.cut", "o.koet", "e.koet", "d"]),
])
def test_g_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("roer",  ["r", "o.oe", "e.oer", "r.cut"]),
    ("roel",  ["r", "o.oe", "e.oer", "l.cut"]),
    ("roen",  ["r", "o.oe", "e.oen", "n"]),
    ("roem",  ["r", "o.oe", "e.oen", "m"]),
    ("roet",  ["r", "o.roet", "e.roet", "t"]),
    ("roed",  ["r", "o.roet", "e.roet", "d"]),
    ("roep",  ["r", "o.oep", "e.oep", "p"]),
    ("roeb",  ["r", "o.oep", "e.oep", "b"]),
    ("roes",  ["r", "o.oep", "e.oep", "s.left"]),
])
def test_r_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("loer",  ["l", "o.oe", "e.oer", "r.cut"]),
    ("loel",  ["l", "o.oe", "e.oer", "l.cut"]),
    ("loen",  ["l", "o.oe", "e.oen", "n"]),
    ("loem",  ["l", "o.oe", "e.oen", "m"]),
    ("loet",  ["l", "o.roet", "e.roet", "t"]),
    ("loed",  ["l", "o.roet", "e.roet", "d"]),
    ("loep",  ["l", "o.oep", "e.oep", "p"]),
    ("loeb",  ["l", "o.oep", "e.oep", "b"]),
    ("loes",  ["l", "o.oep", "e.oep", "s.left"]),
])
def test_l_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs

