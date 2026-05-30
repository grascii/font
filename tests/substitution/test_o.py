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
    ("oth(", ["o", "th.over.angled"]),
    # ("oth)", ["o", "th.under"]),
    ("ong",  ["o.ong", "ng"]),
    ("onk",  ["o.ong", "nk"]),
    ("otn",  ["o", "tn.angled"]),
    ("odn",  ["o", "tn.angled"]),
    ("otm",  ["o", "tm.angled"]),
    ("odm",  ["o", "tm.angled"]),
    ("ont",  ["o.ont", "nt"]),
    ("ond",  ["o.ont", "nt"]),
    ("omt",  ["o.ont", "mt"]),
    ("omd",  ["o.ont", "mt"]),
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
    ("uo",   ["u", "o"]),
    ("tno",  ["tn", "o"]),
    ("dno",  ["tn", "o"]),
    ("tmo",  ["tm", "o"]),
    ("dmo",  ["tm", "o"]),
    ("nto",  ["nt.skew30", "o"]),
    ("ndo",  ["nt.skew30", "o"]),
    ("mto",  ["mt.skew30", "o"]),
    ("mdo",  ["mt.skew30", "o"]),
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
    ("koth", ["k", "o.ont", "th.under"]),
    ("kont", ["k", "o.ont", "nt"]),
    ("kond", ["k", "o.ont", "nt"]),
    ("komt", ["k", "o.ont", "mt"]),
    ("komd", ["k", "o.ont", "mt"]),
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
    ("goth", ["g", "o.ont", "th.under"]),
    ("gont", ["g", "o.ont", "nt"]),
    ("gond", ["g", "o.ont", "nt"]),
    ("gomt", ["g", "o.ont", "mt"]),
    ("gomd", ["g", "o.ont", "mt"]),
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
    ("roth",  ["r", "o.ont", "th.under"]),
    ("rotn",  ["r", "o.op", "tn.skew30"]),
    ("rodn",  ["r", "o.op", "tn.skew30"]),
    ("rotm",  ["r", "o.op", "tm.skew30"]),
    ("rodm",  ["r", "o.op", "tm.skew30"]),
    ("ront",  ["r", "o.ont", "nt"]),
    ("rond",  ["r", "o.ont", "nt"]),
    ("romt",  ["r", "o.ont", "mt"]),
    ("romd",  ["r", "o.ont", "mt"]),
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
    ("loth",  ["l", "o.ont", "th.under"]),
    ("lotn",  ["l", "o.op", "tn.skew30"]),
    ("lodn",  ["l", "o.op", "tn.skew30"]),
    ("lotm",  ["l", "o.op", "tm.skew30"]),
    ("lodm",  ["l", "o.op", "tm.skew30"]),
    ("lont",  ["l", "o.ont", "nt"]),
    ("lond",  ["l", "o.ont", "nt"]),
    ("lomt",  ["l", "o.ont", "mt"]),
    ("lomd",  ["l", "o.ont", "mt"]),
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
    ("noth",  ["n", "o.ont", "th.under"]),
    ("notn",  ["n", "o.op", "tn.skew30"]),
    ("nodn",  ["n", "o.op", "tn.skew30"]),
    ("notm",  ["n", "o.op", "tm.skew30"]),
    ("nodm",  ["n", "o.op", "tm.skew30"]),
    ("nont",  ["n", "o.ont", "nt"]),
    ("nond",  ["n", "o.ont", "nt"]),
    ("nomt",  ["n", "o.ont", "mt"]),
    ("nomd",  ["n", "o.ont", "mt"]),
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
    ("moth",  ["m", "o.ont", "th.under"]),
    ("motn",  ["m", "o.op", "tn.skew30"]),
    ("modn",  ["m", "o.op", "tn.skew30"]),
    ("motm",  ["m", "o.op", "tm.skew30"]),
    ("modm",  ["m", "o.op", "tm.skew30"]),
    ("mont",  ["m", "o.ont", "nt"]),
    ("mond",  ["m", "o.ont", "nt"]),
    ("momt",  ["m", "o.ont", "mt"]),
    ("momd",  ["m", "o.ont", "mt"]),
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
    ("tont",  ["t", "o.ton", "nt"]),
    ("tond",  ["t", "o.ton", "nt"]),
    ("tomt",  ["t", "o.ton", "mt"]),
    ("tomd",  ["t", "o.ton", "mt"]),
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
    ("dont",  ["d", "o.ton", "nt"]),
    ("dond",  ["d", "o.ton", "nt"]),
    ("domt",  ["d", "o.ton", "mt"]),
    ("domd",  ["d", "o.ton", "mt"]),
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
    ("potn",  ["p", "o.po", "tn.angled"]),
    ("podn",  ["p", "o.po", "tn.angled"]),
    ("potm",  ["p", "o.po", "tm.angled"]),
    ("podm",  ["p", "o.po", "tm.angled"]),
    ("pont",  ["p", "o.po", "nt"]),
    ("pond",  ["p", "o.po", "nt"]),
    ("pomt",  ["p", "o.po", "mt"]),
    ("pomd",  ["p", "o.po", "mt"]),
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
    ("botn",  ["b", "o.po", "tn.angled"]),
    ("bodn",  ["b", "o.po", "tn.angled"]),
    ("botm",  ["b", "o.po", "tm.angled"]),
    ("bodm",  ["b", "o.po", "tm.angled"]),
    ("bont",  ["b", "o.po", "nt"]),
    ("bond",  ["b", "o.po", "nt"]),
    ("bomt",  ["b", "o.po", "mt"]),
    ("bomd",  ["b", "o.po", "mt"]),
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
    ("font",  ["f", "o.fo", "nt"]),
    ("fond",  ["f", "o.fo", "nt"]),
    ("fomt",  ["f", "o.fo", "mt"]),
    ("fomd",  ["f", "o.fo", "mt"]),
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
    ("vont",  ["v", "o.fo", "nt"]),
    ("vond",  ["v", "o.fo", "nt"]),
    ("vomt",  ["v", "o.fo", "mt"]),
    ("vomd",  ["v", "o.fo", "mt"]),
])
def test_v_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shok",   ["sh", "o.chok", "k"]),
    ("shog",   ["sh", "o.chok", "g"]),
    ("shor",   ["sh", "o", "r"]),
    ("shol",   ["sh", "o", "l"]),
    ("shon",   ["sh", "o", "n"]),
    ("shom",   ["sh", "o", "m"]),
    ("shot",   ["sh", "o", "t"]),
    ("shod",   ["sh", "o", "d"]),
    ("shop",   ["sh", "o.chop", "p"]),
    ("shob",   ["sh", "o.chop", "b"]),
    ("shof",   ["sh", "o", "f"]),
    ("shov",   ["sh", "o", "v"]),
    ("shosh",  ["sh", "o", "sh"]),
    ("shoch",  ["sh", "o", "ch"]),
    ("shoj",   ["sh", "o", "j"]),
    ("shos)",  ["sh", "o", "s.right"]),
    ("shos(",  ["sh", "o.chop", "s.left"]),
    ("shong",  ["sh", "o", "ng"]),
    ("shonk",  ["sh", "o", "nk"]),
    ("shoth",  ["sh", "o", "th.under"]),
])
def test_sh_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("chok",   ["ch", "o.chok", "k"]),
    ("chog",   ["ch", "o.chok", "g"]),
    ("chor",   ["ch", "o", "r"]),
    ("chol",   ["ch", "o", "l"]),
    ("chon",   ["ch", "o", "n"]),
    ("chom",   ["ch", "o", "m"]),
    ("chot",   ["ch", "o", "t"]),
    ("chod",   ["ch", "o", "d"]),
    ("chop",   ["ch", "o.chop", "p"]),
    ("chob",   ["ch", "o.chop", "b"]),
    ("chof",   ["ch", "o", "f"]),
    ("chov",   ["ch", "o", "v"]),
    ("chosh",  ["ch", "o", "sh"]),
    ("choch",  ["ch", "o", "ch"]),
    ("choj",   ["ch", "o", "j"]),
    ("chos)",  ["ch", "o", "s.right"]),
    ("chos(",  ["ch", "o.chop", "s.left"]),
    ("chong",  ["ch", "o", "ng"]),
    ("chonk",  ["ch", "o", "nk"]),
    ("choth",  ["ch", "o", "th.under"]),
])
def test_ch_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("jok",   ["j", "o.chok", "k"]),
    ("jog",   ["j", "o.chok", "g"]),
    ("jor",   ["j", "o", "r"]),
    ("jol",   ["j", "o", "l"]),
    ("jon",   ["j", "o", "n"]),
    ("jom",   ["j", "o", "m"]),
    ("jot",   ["j", "o", "t"]),
    ("jod",   ["j", "o", "d"]),
    ("jop",   ["j", "o.chop", "p"]),
    ("job",   ["j", "o.chop", "b"]),
    ("jof",   ["j", "o", "f"]),
    ("jov",   ["j", "o", "v"]),
    ("josh",  ["j", "o", "sh"]),
    ("joch",  ["j", "o", "ch"]),
    ("joj",   ["j", "o", "j"]),
    ("jos)",  ["j", "o", "s.right"]),
    ("jos(",  ["j", "o.chop", "s.left"]),
    ("jong",  ["j", "o", "ng"]),
    ("jonk",  ["j", "o", "nk"]),
    ("joth",  ["j", "o", "th.under"]),
])
def test_j_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)ok",   ["s.right", "o.fok", "k"]),
    ("s)og",   ["s.right", "o.fok", "g"]),
    ("s)or",   ["s.right", "o.fo", "r"]),
    ("s)ol",   ["s.right", "o.fo", "l"]),
    ("s)on",   ["s.right", "o.fo", "n"]),
    ("s)om",   ["s.right", "o.fo", "m"]),
    ("s)ot",   ["s.right", "o.fo", "t"]),
    ("s)od",   ["s.right", "o.fo", "d"]),
    ("s)op",   ["s.right", "o.fop", "p"]),
    ("s)ob",   ["s.right", "o.fop", "b"]),
    ("s)of",   ["s.right", "o.fo", "f"]),
    ("s)ov",   ["s.right", "o.fo", "v"]),
    ("s)osh",  ["s.right", "o.fo", "sh"]),
    ("s)och",  ["s.right", "o.fo", "ch"]),
    ("s)oj",   ["s.right", "o.fo", "j"]),
    ("s)os)",  ["s.right", "o.fo", "s.right"]),
    ("s)os(",  ["s.right", "o.fop", "s.left"]),
    ("s)ong",  ["s.right", "o.fo", "ng"]),
    ("s)onk",  ["s.right", "o.fo", "nk"]),
    ("s)oth",  ["s.right", "o.fo", "th.under"]),
    ("s)otn",  ["s.right", "o.fo", "tn.skew30"]),
    ("s)odn",  ["s.right", "o.fo", "tn.skew30"]),
    ("s)otm",  ["s.right", "o.fo", "tm.skew30"]),
    ("s)odm",  ["s.right", "o.fo", "tm.skew30"]),
    ("s)ont",  ["s.right", "o.fo", "nt"]),
    ("s)ond",  ["s.right", "o.fo", "nt"]),
    ("s)omt",  ["s.right", "o.fo", "mt"]),
    ("s)omd",  ["s.right", "o.fo", "mt"]),
])
def test_sR_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s(ok",   ["s.left", "o.po", "k"]),
    ("s(og",   ["s.left", "o.po", "g"]),
    ("s(or",   ["s.left", "o.po", "r"]),
    ("s(ol",   ["s.left", "o.po", "l"]),
    ("s(on",   ["s.left", "o.po", "n"]),
    ("s(om",   ["s.left", "o.po", "m"]),
    ("s(ot",   ["s.left", "o.po", "t"]),
    ("s(od",   ["s.left", "o.po", "d"]),
    ("s(op",   ["s.left", "o.pop", "p"]),
    ("s(ob",   ["s.left", "o.pop", "b"]),
    ("s(of",   ["s.left", "o.po", "f"]),
    ("s(ov",   ["s.left", "o.po", "v"]),
    ("s(osh",  ["s.left", "o.po", "sh"]),
    ("s(och",  ["s.left", "o.po", "ch"]),
    ("s(oj",   ["s.left", "o.po", "j"]),
    ("s(os)",  ["s.left", "o.po", "s.right"]),
    ("s(os(",  ["s.left", "o.pop", "s.left"]),
    ("s(ong",  ["s.left", "o.po", "ng"]),
    ("s(onk",  ["s.left", "o.po", "nk"]),
    ("s(oth",  ["s.left", "o.po", "th.under"]),
    ("s(otn",  ["s.left", "o", "tn.angled"]),
    ("s(odn",  ["s.left", "o", "tn.angled"]),
    ("s(otm",  ["s.left", "o", "tm.angled"]),
    ("s(odm",  ["s.left", "o", "tm.angled"]),
    ("s(ont",  ["s.left", "o.ont", "nt"]),
    ("s(ond",  ["s.left", "o.ont", "nt"]),
    ("s(omt",  ["s.left", "o.ont", "mt"]),
    ("s(omd",  ["s.left", "o.ont", "mt"]),
])
def test_sL_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ngor",   ["ng", "o.or", "r.cut"]),
    ("ngol",   ["ng", "o.ol", "l.cut"]),
    ("ngot",   ["ng", "o.ot", "t"]),
    ("ngod",   ["ng", "o.ot", "d"]),
    ("ngop",   ["ng", "o.op", "p"]),
    ("ngob",   ["ng", "o.op", "b"]),
])
def test_ng_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nkor",   ["nk", "o.or", "r.cut"]),
    ("nkol",   ["nk", "o.ol", "l.cut"]),
    ("nkot",   ["nk", "o.ot", "t"]),
    ("nkod",   ["nk", "o.ot", "d"]),
    ("nkop",   ["nk", "o.op", "p"]),
    ("nkob",   ["nk", "o.op", "b"]),
])
def test_nk_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th(or",   ["th.over", "o.or", "r.cut"]),
    ("th(ol",   ["th.over", "o.ol", "l.cut"]),
    ("th(ot",   ["th.over", "o.ot", "t"]),
    ("th(od",   ["th.over", "o.ot", "d"]),
    ("th(os(",  ["th.over", "o.tnop", "s.left"]),
    ("th(ong",  ["th.over", "o.tnong", "ng"]),
    ("th(onk",  ["th.over", "o.tnong", "nk"]),
])
def test_thO_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    # ("th)or",   ["th.under.skew45", "o.or", "r.cut"]),
    # ("th)ol",   ["th.under.skew45", "o.ol", "l.cut"]),
    # ("th)on",   ["th.under", "o.on", "n"]),
    # ("th)om",   ["th.under", "o.on", "m"]),
    ("th)ot",   ["th.under.skew45", "o.ot", "t"]),
    ("th)od",   ["th.under.skew45", "o.ot", "d"]),
    ("th)op",   ["th.under.skew30", "o.op", "p"]),
    ("th)ob",   ["th.under.skew30", "o.op", "b"]),
    # ("th)os)",  ["th.under", "o.of", "s.right"]),
    ("th)ong",  ["th.under.skew30", "o.ntong", "ng"]),
    ("th)onk",  ["th.under.skew30", "o.ntong", "nk"]),
])
def test_thU_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uok",   ["u", "o.chok", "k"]),
    ("uog",   ["u", "o.chok", "g"]),
    ("uor",   ["u", "o", "r"]),
    ("uol",   ["u", "o", "l"]),
    ("uon",   ["u", "o", "n"]),
    ("uom",   ["u", "o", "m"]),
    ("uot",   ["u", "o", "t"]),
    ("uod",   ["u", "o", "d"]),
    ("uop",   ["u", "o.chop", "p"]),
    ("uob",   ["u", "o.chop", "b"]),
    ("uof",   ["u", "o", "f"]),
    ("uov",   ["u", "o", "v"]),
    ("uosh",  ["u", "o", "sh"]),
    ("uoch",  ["u", "o", "ch"]),
    ("uoj",   ["u", "o", "j"]),
    ("uos",   ["u", "o.chop", "s.left"]),
    ("uos)",  ["u", "o", "s.right"]),
    ("uong",  ["u", "o", "ng"]),
    ("uonk",  ["u", "o", "nk"]),
    ("uoth(", ["u", "o", "th.over.angled"]),
    ("uoth",  ["u", "o", "th.under"]),
])
def test_u_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnor",   ["tn", "o.or", "r.cut"]),
    ("tnol",   ["tn", "o.ol", "l.cut"]),
    ("tnon",   ["tn", "o.on", "n"]),
    ("tnom",   ["tn", "o.on", "m"]),
    ("tnop",   ["tn", "o.tnop", "p"]),
    ("tnob",   ["tn", "o.tnop", "b"]),
    ("tnos(",  ["tn", "o.tnop", "s.left"]),
])
def test_tn_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tmor",   ["tm", "o.or", "r.cut"]),
    ("tmol",   ["tm", "o.ol", "l.cut"]),
    ("tmon",   ["tm", "o.on", "n"]),
    ("tmom",   ["tm", "o.on", "m"]),
    ("tmop",   ["tm", "o.tnop", "p"]),
    ("tmob",   ["tm", "o.tnop", "b"]),
    ("tmos(",  ["tm", "o.tnop", "s.left"]),
])
def test_tm_o(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
