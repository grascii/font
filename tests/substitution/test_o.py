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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ko",   ["k", "o.ko"]),
    ("go",   ["g", "o.ko"]),
    ("ro",   ["r", "o"]),
    ("lo",   ["l", "o"]),
    ("no",   ["n", "o"]),
    ("mo",   ["m", "o"]),
    ("to",   ["t", "o"]),
    ("do",   ["d", "o"]),
    ("po",   ["p", "o.po"]),
    ("bo",   ["b", "o.po"]),
    ("fo",   ["f", "o.fo"]),
    ("vo",   ["v", "o.fo"]),
    ("sho",  ["sh", "o"]),
    ("cho",  ["ch", "o"]),
    ("jo",   ["j", "o"]),
    ("so",   ["s.right", "o.fo"]),
    ("s(o",  ["s.left", "o.po"]),
    ("th(o", ["th.over", "o"]),
    ("th)o", ["th.under.skew30", "o"]),
    ("ngo",  ["ng", "o"]),
    ("nko",  ["nk", "o"]),
])
def test_o_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kok",  ["k", "o.kok", "k"]),
    ("kog",  ["k", "o.kok", "g"]),
    ("kor",  ["k", "o.or", "r.cut"]),
    ("kol",  ["k", "o.ol", "l.cut"]),
    ("kon",  ["k", "o.on", "n"]),
    ("kom",  ["k", "o.on", "m"]),
    ("kot",  ["k", "o.kot", "t"]),
    ("kod",  ["k", "o.kot", "d"]),
    ("kop",  ["k", "o.kop", "p"]),
    ("kob",  ["k", "o.kop", "b"]),
    ("kof",  ["k", "o.ko", "f"]),
    ("kov",  ["k", "o.ko", "v"]),
    ("kosh", ["k", "o.ko", "sh"]),
    ("koch", ["k", "o.ko", "ch"]),
    ("koj",  ["k", "o.ko", "j"]),
    ("kos)", ["k", "o.ko", "s.right"]),
    ("kos(", ["k", "o.kop", "s.left"]),
    ("kong", ["k", "o.ong", "ng"]),
    ("konk", ["k", "o.ong", "nk"]),
    # ("koth", ["k", "o", "th.under"]),
])
def test_g_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("gok",  ["g", "o.kok", "k"]),
    ("gog",  ["g", "o.kok", "g"]),
    ("gor",  ["g", "o.or", "r.cut"]),
    ("gol",  ["g", "o.ol", "l.cut"]),
    ("gon",  ["g", "o.on", "n"]),
    ("gom",  ["g", "o.on", "m"]),
    ("got",  ["g", "o.kot", "t"]),
    ("god",  ["g", "o.kot", "d"]),
    ("gop",  ["g", "o.kop", "p"]),
    ("gob",  ["g", "o.kop", "b"]),
    ("gof",  ["g", "o.ko", "f"]),
    ("gov",  ["g", "o.ko", "v"]),
    ("gosh", ["g", "o.ko", "sh"]),
    ("goch", ["g", "o.ko", "ch"]),
    ("goj",  ["g", "o.ko", "j"]),
    ("gos)", ["g", "o.ko", "s.right"]),
    ("gos(", ["g", "o.kop", "s.left"]),
    ("gong", ["g", "o.ong", "ng"]),
    ("gonk", ["g", "o.ong", "nk"]),
    # ("goth", ["g", "o", "th.under"]),
])
def test_g_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
