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


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tok",   ["t", "o.ok", "k"]),
    ("tog",   ["t", "o.ok", "g"]),
    ("tor",   ["t", "o.or", "r.cut"]),
    ("tol",   ["t", "o.ol", "l.cut"]),
    ("ton",   ["t", "o.ton", "n"]),
    ("tom",   ["t", "o.ton", "m"]),
    ("tot",   ["t", "o.ot", "t"]),
    ("tod",   ["t", "o.ot", "d"]),
    ("top",   ["t", "o.op", "p"]),
    ("tob",   ["t", "o.op", "b"]),
    ("tof",   ["t", "o", "f"]),
    ("tov",   ["t", "o", "v"]),
    ("tosh",  ["t", "o", "sh"]),
    ("toch",  ["t", "o", "ch"]),
    ("toj",   ["t", "o", "j"]),
    ("tos)",  ["t", "o", "s.right"]),
    ("tos(",  ["t", "o.op", "s.left"]),
    ("tong",  ["t", "o.tong", "ng"]),
    ("tonk",  ["t", "o.tong", "nk"]),
])
def test_t_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("dok",   ["d", "o.ok", "k"]),
    ("dog",   ["d", "o.ok", "g"]),
    ("dor",   ["d", "o.or", "r.cut"]),
    ("dol",   ["d", "o.ol", "l.cut"]),
    ("don",   ["d", "o.ton", "n"]),
    ("dom",   ["d", "o.ton", "m"]),
    ("dot",   ["d", "o.ot", "t"]),
    ("dod",   ["d", "o.ot", "d"]),
    ("dop",   ["d", "o.op", "p"]),
    ("dob",   ["d", "o.op", "b"]),
    ("dof",   ["d", "o", "f"]),
    ("dov",   ["d", "o", "v"]),
    ("dosh",  ["d", "o", "sh"]),
    ("doch",  ["d", "o", "ch"]),
    ("doj",   ["d", "o", "j"]),
    ("dos)",  ["d", "o", "s.right"]),
    ("dos(",  ["d", "o.op", "s.left"]),
    ("dong",  ["d", "o.tong", "ng"]),
    ("donk",  ["d", "o.tong", "nk"]),
])
def test_d_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pok",   ["p", "o.po", "k"]),
    ("pog",   ["p", "o.po", "g"]),
    ("por",   ["p", "o.po", "r"]),
    ("pol",   ["p", "o.po", "l"]),
    ("pon",   ["p", "o.po", "n"]),
    ("pom",   ["p", "o.po", "m"]),
    ("pot",   ["p", "o.po", "t"]),
    ("pod",   ["p", "o.po", "d"]),
    ("pop",   ["p", "o.pop", "p"]),
    ("pob",   ["p", "o.pop", "b"]),
    ("pof",   ["p", "o.po", "f"]),
    ("pov",   ["p", "o.po", "v"]),
    ("posh",  ["p", "o.po", "sh"]),
    ("poch",  ["p", "o.po", "ch"]),
    ("poj",   ["p", "o.po", "j"]),
    ("pos)",  ["p", "o.po", "s.right"]),
    ("pos(",  ["p", "o.pop", "s.left"]),
    ("pong",  ["p", "o.po", "ng"]),
    ("ponk",  ["p", "o.po", "nk"]),
    ("poth",  ["p", "o.po", "th.under"]),
])
def test_p_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("bok",   ["b", "o.po", "k"]),
    ("bog",   ["b", "o.po", "g"]),
    ("bor",   ["b", "o.po", "r"]),
    ("bol",   ["b", "o.po", "l"]),
    ("bon",   ["b", "o.po", "n"]),
    ("bom",   ["b", "o.po", "m"]),
    ("bot",   ["b", "o.po", "t"]),
    ("bod",   ["b", "o.po", "d"]),
    ("bop",   ["b", "o.pop", "p"]),
    ("bob",   ["b", "o.pop", "b"]),
    ("bof",   ["b", "o.po", "f"]),
    ("bov",   ["b", "o.po", "v"]),
    ("bosh",  ["b", "o.po", "sh"]),
    ("boch",  ["b", "o.po", "ch"]),
    ("boj",   ["b", "o.po", "j"]),
    ("bos)",  ["b", "o.po", "s.right"]),
    ("bos(",  ["b", "o.pop", "s.left"]),
    ("bong",  ["b", "o.po", "ng"]),
    ("bonk",  ["b", "o.po", "nk"]),
    ("both",  ["b", "o.po", "th.under"]),
])
def test_b_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fok",   ["f", "o.fok", "k"]),
    ("fog",   ["f", "o.fok", "g"]),
    ("for",   ["f", "o.fo", "r"]),
    ("fol",   ["f", "o.fo", "l"]),
    ("fon",   ["f", "o.fo", "n"]),
    ("fom",   ["f", "o.fo", "m"]),
    ("fot",   ["f", "o.fo", "t"]),
    ("fod",   ["f", "o.fo", "d"]),
    ("fop",   ["f", "o.fop", "p"]),
    ("fob",   ["f", "o.fop", "b"]),
    ("fof",   ["f", "o.fo", "f"]),
    ("fov",   ["f", "o.fo", "v"]),
    ("fosh",  ["f", "o.fo", "sh"]),
    ("foch",  ["f", "o.fo", "ch"]),
    ("foj",   ["f", "o.fo", "j"]),
    ("fos)",  ["f", "o.fo", "s.right"]),
    ("fos(",  ["f", "o.fop", "s.left"]),
    ("fong",  ["f", "o.fo", "ng"]),
    ("fonk",  ["f", "o.fo", "nk"]),
    ("foth",  ["f", "o.fo", "th.under"]),
])
def test_f_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("vok",   ["v", "o.fok", "k"]),
    ("vog",   ["v", "o.fok", "g"]),
    ("vor",   ["v", "o.fo", "r"]),
    ("vol",   ["v", "o.fo", "l"]),
    ("von",   ["v", "o.fo", "n"]),
    ("vom",   ["v", "o.fo", "m"]),
    ("vot",   ["v", "o.fo", "t"]),
    ("vod",   ["v", "o.fo", "d"]),
    ("vop",   ["v", "o.fop", "p"]),
    ("vob",   ["v", "o.fop", "b"]),
    ("vof",   ["v", "o.fo", "f"]),
    ("vov",   ["v", "o.fo", "v"]),
    ("vosh",  ["v", "o.fo", "sh"]),
    ("voch",  ["v", "o.fo", "ch"]),
    ("voj",   ["v", "o.fo", "j"]),
    ("vos)",  ["v", "o.fo", "s.right"]),
    ("vos(",  ["v", "o.fop", "s.left"]),
    ("vong",  ["v", "o.fo", "ng"]),
    ("vonk",  ["v", "o.fo", "nk"]),
    ("voth",  ["v", "o.fo", "th.under"]),
])
def test_v_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
