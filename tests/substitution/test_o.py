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
def test_k_o(font, text, expected_glyphs):
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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("rok",   ["r", "o.ok", "k"]),
    ("rog",   ["r", "o.ok", "g"]),
    ("ror",   ["r", "o.or", "r.cut"]),
    ("rol",   ["r", "o.ol", "l.cut"]),
    ("ron",   ["r", "o.ron", "n"]),
    ("rom",   ["r", "o.ron", "m"]),
    ("rot",   ["r", "o.ot", "t"]),
    ("rod",   ["r", "o.ot", "d"]),
    ("rop",   ["r", "o.op", "p"]),
    ("rob",   ["r", "o.op", "b"]),
    ("rof",   ["r", "o", "f"]),
    ("rov",   ["r", "o", "v"]),
    ("rosh",  ["r", "o", "sh"]),
    ("roch",  ["r", "o", "ch"]),
    ("roj",   ["r", "o", "j"]),
    ("ros)",  ["r", "o", "s.right"]),
    ("ros(",  ["r", "o.op", "s.left"]),
    ("rong",  ["r", "o.rong", "ng"]),
    ("ronk",  ["r", "o.rong", "nk"]),
    # ("roth",  ["r", "o.ront", "th.under"]),
])
def test_r_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("lok",   ["l", "o.ok", "k"]),
    ("log",   ["l", "o.ok", "g"]),
    ("lor",   ["l", "o.or", "r.cut"]),
    ("lol",   ["l", "o.ol", "l.cut"]),
    ("lon",   ["l", "o.ron", "n"]),
    ("lom",   ["l", "o.ron", "m"]),
    ("lot",   ["l", "o.ot", "t"]),
    ("lod",   ["l", "o.ot", "d"]),
    ("lop",   ["l", "o.op", "p"]),
    ("lob",   ["l", "o.op", "b"]),
    ("lof",   ["l", "o", "f"]),
    ("lov",   ["l", "o", "v"]),
    ("losh",  ["l", "o", "sh"]),
    ("loch",  ["l", "o", "ch"]),
    ("loj",   ["l", "o", "j"]),
    ("los)",  ["l", "o", "s.right"]),
    ("los(",  ["l", "o.op", "s.left"]),
    ("long",  ["l", "o.rong", "ng"]),
    ("lonk",  ["l", "o.rong", "nk"]),
    # ("loth",  ["l", "o.ront", "th.under"]),
])
def test_l_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nok",   ["n", "o.ok", "k"]),
    ("nog",   ["n", "o.ok", "g"]),
    ("nor",   ["n", "o.or", "r.cut"]),
    ("nol",   ["n", "o.ol", "l.cut"]),
    ("non",   ["n", "o.on", "n"]),
    ("nom",   ["n", "o.on", "m"]),
    ("not",   ["n", "o.ot", "t"]),
    ("nod",   ["n", "o.ot", "d"]),
    ("nop",   ["n", "o.op", "p"]),
    ("nob",   ["n", "o.op", "b"]),
    ("nof",   ["n", "o", "f"]),
    ("nov",   ["n", "o", "v"]),
    ("nosh",  ["n", "o", "sh"]),
    ("noch",  ["n", "o", "ch"]),
    ("noj",   ["n", "o", "j"]),
    ("nos)",  ["n", "o", "s.right"]),
    ("nos(",  ["n", "o.op", "s.left"]),
    # ("noth",  ["n", "o.nont", "th.under"]),
])
def test_n_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mok",   ["m", "o.ok", "k"]),
    ("mog",   ["m", "o.ok", "g"]),
    ("mor",   ["m", "o.or", "r.cut"]),
    ("mol",   ["m", "o.ol", "l.cut"]),
    ("mon",   ["m", "o.on", "n"]),
    ("mom",   ["m", "o.on", "m"]),
    ("mot",   ["m", "o.ot", "t"]),
    ("mod",   ["m", "o.ot", "d"]),
    ("mop",   ["m", "o.op", "p"]),
    ("mob",   ["m", "o.op", "b"]),
    ("mof",   ["m", "o", "f"]),
    ("mov",   ["m", "o", "v"]),
    ("mosh",  ["m", "o", "sh"]),
    ("moch",  ["m", "o", "ch"]),
    ("moj",   ["m", "o", "j"]),
    ("mos)",  ["m", "o", "s.right"]),
    ("mos(",  ["m", "o.op", "s.left"]),
    # ("noth",  ["n", "o.nont", "th.under"]),
])
def test_m_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
