import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uk",   ["u", "k"]),
    ("ug",   ["u", "g"]),
    ("ur",   ["u.ur", "r"]),
    ("ul",   ["u.ur", "l"]),
    ("un",   ["u", "n"]),
    ("um",   ["u", "m"]),
    ("ut",   ["u", "t"]),
    ("ud",   ["u", "d"]),
    ("up",   ["u.up", "p"]),
    ("ub",   ["u.up", "b"]),
    ("uf",   ["u.uf", "f"]),
    ("uv",   ["u.uf", "v"]),
    ("ush",  ["u", "sh"]),
    ("uch",  ["u", "ch"]),
    ("uj",   ["u", "j"]),
    ("us)",  ["u.uf", "s.right"]),
    ("us(",  ["u.up", "s.left"]),
    ("uth(", ["u", "th.over.angled"]),
    ("uth)", ["u", "th.under"]),
    ("ung",  ["u", "ng"]),
    ("unk",  ["u", "nk"]),
    ("utn",  ["u", "tn.angled"]),
    ("udn",  ["u", "tn.angled"]),
    ("utm",  ["u", "tm.angled"]),
    ("udm",  ["u", "tm.angled"]),
    ("unt",  ["u", "nt"]),
    ("und",  ["u", "nt"]),
    ("umt",  ["u", "mt"]),
    ("umd",  ["u", "mt"]),
    ("udf",  ["u", "df.angled"]),
])
def test_u_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ku",   ["k", "u"]),
    ("gu",   ["g", "u"]),
    ("ru",   ["r", "u.ru"]),
    ("lu",   ["l", "u.ru"]),
    ("nu",   ["n", "u.nu"]),
    ("mu",   ["m", "u.nu"]),
    ("tu",   ["t", "u.tu"]),
    ("du",   ["d", "u.tu"]),
    ("pu",   ["p", "u"]),
    ("bu",   ["b", "u"]),
    ("fu",   ["f", "u.fu"]),
    ("vu",   ["v", "u.fu"]),
    ("shu",  ["sh", "u"]),
    ("chu",  ["ch", "u"]),
    ("ju",   ["j", "u"]),
    ("su",   ["s.right", "u.fu"]),
    ("s(u",  ["s.left", "u"]),
    ("th(u", ["th.over", "u.tnu"]),
    ("th)u", ["th.under.angled", "u"]),
    ("ngu",  ["ng", "u.ngu"]),
    ("nku",  ["nk", "u.ngu"]),
    ("tnu",  ["tn", "u.tnu"]),
    ("dnu",  ["tn", "u.tnu"]),
    ("tmu",  ["tm", "u.tnu"]),
    ("dmu",  ["tm", "u.tnu"]),
    ("ntu",  ["nt.angled", "u"]),
    ("ndu",  ["nt.angled", "u"]),
    ("mtu",  ["mt.angled", "u"]),
    ("mdu",  ["mt.angled", "u"]),
])
def test_u_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kuk",  ["k", "u", "k"]),
    ("kug",  ["k", "u", "g"]),
    ("kur",  ["k.cut", "u.kur", "r.cut"]),
    ("kul",  ["k.cut", "u.kur", "l.cut"]),
    ("kun",  ["k", "u", "n"]),
    ("kum",  ["k", "u", "m"]),
    ("kut",  ["k", "u", "t"]),
    ("kud",  ["k", "u", "d"]),
    ("kup",  ["k", "u.up", "p"]),
    ("kub",  ["k", "u.up", "b"]),
    ("kuf",  ["k", "u.uf", "f"]),
    ("kuv",  ["k", "u.uf", "v"]),
    ("kush", ["k", "u", "sh"]),
    ("kuch", ["k", "u", "ch"]),
    ("kuj",  ["k", "u", "j"]),
    ("kus)", ["k", "u.uf", "s.right"]),
    ("kus(", ["k", "u.up", "s.left"]),
    ("kuth", ["k", "u", "th.over.angled"]),
    ("kudf", ["k", "u", "df.angled"]),
])
def test_k_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("guk",  ["g", "u", "k"]),
    ("gug",  ["g", "u", "g"]),
    ("gur",  ["g.cut", "u.kur", "r.cut"]),
    ("gul",  ["g.cut", "u.kur", "l.cut"]),
    ("gun",  ["g", "u", "n"]),
    ("gum",  ["g", "u", "m"]),
    ("gut",  ["g", "u", "t"]),
    ("gud",  ["g", "u", "d"]),
    ("gup",  ["g", "u.up", "p"]),
    ("gub",  ["g", "u.up", "b"]),
    ("guf",  ["g", "u.uf", "f"]),
    ("guv",  ["g", "u.uf", "v"]),
    ("gush", ["g", "u", "sh"]),
    ("guch", ["g", "u", "ch"]),
    ("guj",  ["g", "u", "j"]),
    ("gus)", ["g", "u.uf", "s.right"]),
    ("gus(", ["g", "u.up", "s.left"]),
    ("guth", ["g", "u", "th.over.angled"]),
    ("gudf", ["g", "u", "df.angled"]),
])
def test_g_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ruk",   ["r", "u.ru", "k"]),
    ("rug",   ["r", "u.ru", "g"]),
    ("rur",   ["r", "u.rur", "r"]),
    ("rul",   ["r", "u.rur", "l"]),
    ("run",   ["r", "u.run", "n"]),
    ("rum",   ["r", "u.run", "m"]),
    ("rut",   ["r", "u.ru", "t"]),
    ("rud",   ["r", "u.ru", "d"]),
    ("rup",   ["r", "u.rup", "p"]),
    ("rub",   ["r", "u.rup", "b"]),
    ("ruf",   ["r", "u.ru", "f"]),
    ("ruv",   ["r", "u.ru", "v"]),
    ("rush",  ["r", "u.ru", "sh"]),
    ("ruch",  ["r", "u.ru", "ch"]),
    ("ruj",   ["r", "u.ru", "j"]),
    ("rus(",  ["r", "u.rup", "s.left"]),
    ("rus",   ["r", "u.ru", "s.right"]),
    ("ruth",  ["r", "u.ru", "th.over.angled"]),
    ("rutn",  ["r", "u.ru", "tn.angled"]),
    ("rudn",  ["r", "u.ru", "tn.angled"]),
    ("rutm",  ["r", "u.ru", "tm.angled"]),
    ("rudm",  ["r", "u.ru", "tm.angled"]),
    ("runt",  ["r", "u.run", "nt"]),
    ("rund",  ["r", "u.run", "nt"]),
    ("rumt",  ["r", "u.run", "mt"]),
    ("rumd",  ["r", "u.run", "mt"]),
])
def test_r_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("luk",   ["l", "u.ru", "k"]),
    ("lug",   ["l", "u.ru", "g"]),
    ("lur",   ["l", "u.rur", "r"]),
    ("lul",   ["l", "u.rur", "l"]),
    ("lun",   ["l", "u.run", "n"]),
    ("lum",   ["l", "u.run", "m"]),
    ("lut",   ["l", "u.ru", "t"]),
    ("lud",   ["l", "u.ru", "d"]),
    ("lup",   ["l", "u.rup", "p"]),
    ("lub",   ["l", "u.rup", "b"]),
    ("luf",   ["l", "u.ru", "f"]),
    ("luv",   ["l", "u.ru", "v"]),
    ("lush",  ["l", "u.ru", "sh"]),
    ("luch",  ["l", "u.ru", "ch"]),
    ("luj",   ["l", "u.ru", "j"]),
    ("lus(",  ["l", "u.rup", "s.left"]),
    ("lus",   ["l", "u.ru", "s.right"]),
    ("luth",  ["l", "u.ru", "th.over.angled"]),
    ("lutn",  ["l", "u.ru", "tn.angled"]),
    ("ludn",  ["l", "u.ru", "tn.angled"]),
    ("lutm",  ["l", "u.ru", "tm.angled"]),
    ("ludm",  ["l", "u.ru", "tm.angled"]),
    ("lunt",  ["l", "u.run", "nt"]),
    ("lund",  ["l", "u.run", "nt"]),
    ("lumt",  ["l", "u.run", "mt"]),
    ("lumd",  ["l", "u.run", "mt"]),
])
def test_l_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nuk",  ["n", "u.nuk", "k"]),
    ("nug",  ["n", "u.nuk", "g"]),
    ("nur",  ["n", "u.nu", "r"]),
    ("nul",  ["n", "u.nu", "l"]),
    ("nun",  ["n", "u.nu", "n"]),
    ("num",  ["n", "u.nu", "m"]),
    ("nut",  ["n", "u.nut", "t"]),
    ("nud",  ["n", "u.nut", "d"]),
    ("nup",  ["n", "u.nup", "p"]),
    ("nub",  ["n", "u.nup", "b"]),
    ("nuf",  ["n", "u.nu", "f"]),
    ("nuv",  ["n", "u.nu", "v"]),
    ("nush", ["n", "u.nu", "sh"]),
    ("nuch", ["n", "u.nu", "ch"]),
    ("nuj",  ["n", "u.nu", "j"]),
    ("nus(", ["n", "u.nup", "s.left"]),
    ("nus",  ["n", "u.nu", "s.right"]),
    ("nuth", ["n", "u.nutn", "th.over.skew30"]),
    ("nutn", ["n", "u.nutn", "tn.skew30"]),
    ("nudn", ["n", "u.nutn", "tn.skew30"]),
    ("nutm", ["n", "u.nutn", "tm.skew30"]),
    ("nudm", ["n", "u.nutn", "tm.skew30"]),
])
def test_n_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("muk",  ["m", "u.nuk", "k"]),
    ("mug",  ["m", "u.nuk", "g"]),
    ("mur",  ["m", "u.nu", "r"]),
    ("mul",  ["m", "u.nu", "l"]),
    ("mun",  ["m", "u.nu", "n"]),
    ("mum",  ["m", "u.nu", "m"]),
    ("mut",  ["m", "u.nut", "t"]),
    ("mud",  ["m", "u.nut", "d"]),
    ("mup",  ["m", "u.nup", "p"]),
    ("mub",  ["m", "u.nup", "b"]),
    ("muf",  ["m", "u.nu", "f"]),
    ("muv",  ["m", "u.nu", "v"]),
    ("mush", ["m", "u.nu", "sh"]),
    ("much", ["m", "u.nu", "ch"]),
    ("muj",  ["m", "u.nu", "j"]),
    ("mus(", ["m", "u.nup", "s.left"]),
    ("mus",  ["m", "u.nu", "s.right"]),
    ("muth", ["m", "u.nutn", "th.over.skew30"]),
    ("mutn", ["m", "u.nutn", "tn.skew30"]),
    ("mudn", ["m", "u.nutn", "tn.skew30"]),
    ("mutm", ["m", "u.nutn", "tm.skew30"]),
    ("mudm", ["m", "u.nutn", "tm.skew30"]),
])
def test_m_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tuk",  ["t", "u.tu", "k"]),
    ("tug",  ["t", "u.tu", "g"]),
    ("tur",  ["t", "u.tur", "r"]),
    ("tul",  ["t", "u.tur", "l"]),
    ("tun",  ["t", "u.tu", "n"]),
    ("tum",  ["t", "u.tu", "m"]),
    ("tut",  ["t", "u.tu", "t"]),
    ("tud",  ["t", "u.tu", "d"]),
    ("tup",  ["t", "u.tup", "p"]),
    ("tub",  ["t", "u.tup", "b"]),
    ("tuf",  ["t", "u.tu", "f"]),
    ("tuv",  ["t", "u.tu", "v"]),
    ("tush", ["t", "u.tuch", "sh"]),
    ("tuch", ["t", "u.tuch", "ch"]),
    ("tuj",  ["t", "u.tuch", "j"]),
    ("tus(", ["t", "u.tup", "s.left"]),
    ("tus",  ["t", "u.tu", "s.right"]),
    ("tuth", ["t", "u.tu", "th.over.skew30"]),
    ("tudf", ["t", "u.tu", "df.skew30"]),
])
def test_t_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("duk",  ["d", "u.tu", "k"]),
    ("dug",  ["d", "u.tu", "g"]),
    ("dur",  ["d", "u.tur", "r"]),
    ("dul",  ["d", "u.tur", "l"]),
    ("dun",  ["d", "u.tu", "n"]),
    ("dum",  ["d", "u.tu", "m"]),
    ("dut",  ["d", "u.tu", "t"]),
    ("dud",  ["d", "u.tu", "d"]),
    ("dup",  ["d", "u.tup", "p"]),
    ("dub",  ["d", "u.tup", "b"]),
    ("duf",  ["d", "u.tu", "f"]),
    ("duv",  ["d", "u.tu", "v"]),
    ("dush", ["d", "u.tuch", "sh"]),
    ("duch", ["d", "u.tuch", "ch"]),
    ("duj",  ["d", "u.tuch", "j"]),
    ("dus(", ["d", "u.tup", "s.left"]),
    ("dus",  ["d", "u.tu", "s.right"]),
    ("duth", ["d", "u.tu", "th.over.skew30"]),
    ("dudf", ["d", "u.tu", "df.skew30"]),
])
def test_d_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("puk",  ["p", "u", "k"]),
    ("pug",  ["p", "u", "g"]),
    ("pur",  ["p", "u.ur", "r"]),
    ("pul",  ["p", "u.ur", "l"]),
    ("pun",  ["p", "u", "n"]),
    ("pum",  ["p", "u", "m"]),
    ("put",  ["p", "u", "t"]),
    ("pud",  ["p", "u", "d"]),
    ("pup",  ["p", "u.up", "p"]),
    ("pub",  ["p", "u.up", "b"]),
    ("puf",  ["p", "u.uf", "f"]),
    ("puv",  ["p", "u.uf", "v"]),
    ("push", ["p", "u", "sh"]),
    ("puch", ["p", "u", "ch"]),
    ("puj",  ["p", "u", "j"]),
    ("pus(", ["p", "u.up", "s.left"]),
    ("pus",  ["p", "u.uf", "s.right"]),
    ("puth", ["p", "u", "th.over.angled"]),
    ("putn", ["p", "u", "tn.angled"]),
    ("pudn", ["p", "u", "tn.angled"]),
    ("putm", ["p", "u", "tm.angled"]),
    ("pudm", ["p", "u", "tm.angled"]),
    ("pudf", ["p", "u", "df.angled"]),
])
def test_p_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("buk",  ["b", "u", "k"]),
    ("bug",  ["b", "u", "g"]),
    ("bur",  ["b", "u.ur", "r"]),
    ("bul",  ["b", "u.ur", "l"]),
    ("bun",  ["b", "u", "n"]),
    ("bum",  ["b", "u", "m"]),
    ("but",  ["b", "u", "t"]),
    ("bud",  ["b", "u", "d"]),
    ("bup",  ["b", "u.up", "p"]),
    ("bub",  ["b", "u.up", "b"]),
    ("buf",  ["b", "u.uf", "f"]),
    ("buv",  ["b", "u.uf", "v"]),
    ("bush", ["b", "u", "sh"]),
    ("buch", ["b", "u", "ch"]),
    ("buj",  ["b", "u", "j"]),
    ("bus(", ["b", "u.up", "s.left"]),
    ("bus",  ["b", "u.uf", "s.right"]),
    ("buth", ["b", "u", "th.over.angled"]),
    ("butn", ["b", "u", "tn.angled"]),
    ("budn", ["b", "u", "tn.angled"]),
    ("butm", ["b", "u", "tm.angled"]),
    ("budm", ["b", "u", "tm.angled"]),
    ("budf", ["b", "u", "df.angled"]),
])
def test_b_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fuk",  ["f", "u.fu", "k"]),
    ("fug",  ["f", "u.fu", "g"]),
    ("fur",  ["f", "u.fur", "r"]),
    ("ful",  ["f", "u.fur", "l"]),
    ("fun",  ["f", "u.fu", "n"]),
    ("fum",  ["f", "u.fu", "m"]),
    ("fut",  ["f", "u.fu", "t"]),
    ("fud",  ["f", "u.fu", "d"]),
    ("fup",  ["f", "u.up", "p"]),
    ("fub",  ["f", "u.up", "b"]),
    ("fuf",  ["f", "u.fuf", "f"]),
    ("fuv",  ["f", "u.fuf", "v"]),
    ("fush", ["f", "u.fuch", "sh"]),
    ("fuch", ["f", "u.fuch", "ch"]),
    ("fuj",  ["f", "u.fuch", "j"]),
    ("fus(", ["f", "u.up", "s.left"]),
    ("fus",  ["f", "u.fuf", "s.right"]),
    ("futh", ["f", "u.fu", "th.over.skew30"]),
    ("futn", ["f", "u.fu", "tn.skew30"]),
    ("fudn", ["f", "u.fu", "tn.skew30"]),
    ("futm", ["f", "u.fu", "tm.skew30"]),
    ("fudm", ["f", "u.fu", "tm.skew30"]),
    ("funt", ["f", "u.fu", "nt"]),
    ("fund", ["f", "u.fu", "nt"]),
    ("fumt", ["f", "u.fu", "mt"]),
    ("fumd", ["f", "u.fu", "mt"]),
    ("fudf", ["f", "u.fu", "df.skew30"]),
])
def test_f_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("vuk",  ["v", "u.fu", "k"]),
    ("vug",  ["v", "u.fu", "g"]),
    ("vur",  ["v", "u.fur", "r"]),
    ("vul",  ["v", "u.fur", "l"]),
    ("vun",  ["v", "u.fu", "n"]),
    ("vum",  ["v", "u.fu", "m"]),
    ("vut",  ["v", "u.fu", "t"]),
    ("vud",  ["v", "u.fu", "d"]),
    ("vup",  ["v", "u.up", "p"]),
    ("vub",  ["v", "u.up", "b"]),
    ("vuf",  ["v", "u.fuf", "f"]),
    ("vuv",  ["v", "u.fuf", "v"]),
    ("vush", ["v", "u.fuch", "sh"]),
    ("vuch", ["v", "u.fuch", "ch"]),
    ("vuj",  ["v", "u.fuch", "j"]),
    ("vus(", ["v", "u.up", "s.left"]),
    ("vus",  ["v", "u.fuf", "s.right"]),
    ("vuth", ["v", "u.fu", "th.over.skew30"]),
    ("vutn", ["v", "u.fu", "tn.skew30"]),
    ("vudn", ["v", "u.fu", "tn.skew30"]),
    ("vutm", ["v", "u.fu", "tm.skew30"]),
    ("vudm", ["v", "u.fu", "tm.skew30"]),
    ("vunt", ["v", "u.fu", "nt"]),
    ("vund", ["v", "u.fu", "nt"]),
    ("vumt", ["v", "u.fu", "mt"]),
    ("vumd", ["v", "u.fu", "mt"]),
    ("vudf", ["v", "u.fu", "df.skew30"]),
])
def test_v_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shuk",  ["sh", "u", "k"]),
    ("shug",  ["sh", "u", "g"]),
    ("shur",  ["sh", "u.ur", "r"]),
    ("shul",  ["sh", "u.ur", "l"]),
    ("shun",  ["sh", "u", "n"]),
    ("shum",  ["sh", "u", "m"]),
    ("shut",  ["sh", "u", "t"]),
    ("shud",  ["sh", "u", "d"]),
    ("shup",  ["sh", "u.up", "p"]),
    ("shub",  ["sh", "u.up", "b"]),
    ("shuf",  ["sh", "u.uf", "f"]),
    ("shuv",  ["sh", "u.uf", "v"]),
    ("shush", ["sh", "u", "sh"]),
    ("shuch", ["sh", "u", "ch"]),
    ("shuj",  ["sh", "u", "j"]),
    ("shus(", ["sh", "u.up", "s.left"]),
    ("shus",  ["sh", "u.uf", "s.right"]),
    ("shuth", ["sh", "u", "th.over.angled"]),
    ("shutn", ["sh", "u", "tn.angled"]),
    ("shudn", ["sh", "u", "tn.angled"]),
    ("shutm", ["sh", "u", "tm.angled"]),
    ("shudm", ["sh", "u", "tm.angled"]),
])
def test_sh_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("chuk",  ["ch", "u", "k"]),
    ("chug",  ["ch", "u", "g"]),
    ("chur",  ["ch", "u.ur", "r"]),
    ("chul",  ["ch", "u.ur", "l"]),
    ("chun",  ["ch", "u", "n"]),
    ("chum",  ["ch", "u", "m"]),
    ("chut",  ["ch", "u", "t"]),
    ("chud",  ["ch", "u", "d"]),
    ("chup",  ["ch", "u.up", "p"]),
    ("chub",  ["ch", "u.up", "b"]),
    ("chuf",  ["ch", "u.uf", "f"]),
    ("chuv",  ["ch", "u.uf", "v"]),
    ("chush", ["ch", "u", "sh"]),
    ("chuch", ["ch", "u", "ch"]),
    ("chuj",  ["ch", "u", "j"]),
    ("chus(", ["ch", "u.up", "s.left"]),
    ("chus",  ["ch", "u.uf", "s.right"]),
    ("chuth", ["ch", "u", "th.over.angled"]),
    ("chutn", ["ch", "u", "tn.angled"]),
    ("chudn", ["ch", "u", "tn.angled"]),
    ("chutm", ["ch", "u", "tm.angled"]),
    ("chudm", ["ch", "u", "tm.angled"]),
])
def test_ch_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("juk",  ["j", "u", "k"]),
    ("jug",  ["j", "u", "g"]),
    ("jur",  ["j", "u.ur", "r"]),
    ("jul",  ["j", "u.ur", "l"]),
    ("jun",  ["j", "u", "n"]),
    ("jum",  ["j", "u", "m"]),
    ("jut",  ["j", "u", "t"]),
    ("jud",  ["j", "u", "d"]),
    ("jup",  ["j", "u.up", "p"]),
    ("jub",  ["j", "u.up", "b"]),
    ("juf",  ["j", "u.uf", "f"]),
    ("juv",  ["j", "u.uf", "v"]),
    ("jush", ["j", "u", "sh"]),
    ("juch", ["j", "u", "ch"]),
    ("juj",  ["j", "u", "j"]),
    ("jus(", ["j", "u.up", "s.left"]),
    ("jus",  ["j", "u.uf", "s.right"]),
    ("juth", ["j", "u", "th.over.angled"]),
    ("jutn", ["j", "u", "tn.angled"]),
    ("judn", ["j", "u", "tn.angled"]),
    ("jutm", ["j", "u", "tm.angled"]),
    ("judm", ["j", "u", "tm.angled"]),
])
def test_j_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)uk",  ["s.right", "u.fu", "k"]),
    ("s)ug",  ["s.right", "u.fu", "g"]),
    ("s)ur",  ["s.right", "u.fur", "r"]),
    ("s)ul",  ["s.right", "u.fur", "l"]),
    ("s)un",  ["s.right", "u.fu", "n"]),
    ("s)um",  ["s.right", "u.fu", "m"]),
    ("s)ut",  ["s.right", "u.fu", "t"]),
    ("s)ud",  ["s.right", "u.fu", "d"]),
    ("s)up",  ["s.right", "u.up", "p"]),
    ("s)ub",  ["s.right", "u.up", "b"]),
    ("s)uf",  ["s.right", "u.fuf", "f"]),
    ("s)uv",  ["s.right", "u.fuf", "v"]),
    ("s)ush", ["s.right", "u.fuch", "sh"]),
    ("s)uch", ["s.right", "u.fuch", "ch"]),
    ("s)uj",  ["s.right", "u.fuch", "j"]),
    ("s)us(", ["s.right", "u.up", "s.left"]),
    ("s)us",  ["s.right", "u.fuf", "s.right"]),
    ("s)uth", ["s.right", "u.fu", "th.over.skew30"]),
    ("s)utn", ["s.right", "u.fu", "tn.skew30"]),
    ("s)udn", ["s.right", "u.fu", "tn.skew30"]),
    ("s)utm", ["s.right", "u.fu", "tm.skew30"]),
    ("s)udm", ["s.right", "u.fu", "tm.skew30"]),
    ("s)unt", ["s.right", "u.fu", "nt"]),
    ("s)und", ["s.right", "u.fu", "nt"]),
    ("s)umt", ["s.right", "u.fu", "mt"]),
    ("s)umd", ["s.right", "u.fu", "mt"]),
    ("s)udf", ["s.right", "u.fu", "df.skew30"]),
])
def test_sR_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s(uk",  ["s.left", "u", "k"]),
    ("s(ug",  ["s.left", "u", "g"]),
    ("s(ur",  ["s.left", "u.ur", "r"]),
    ("s(ul",  ["s.left", "u.ur", "l"]),
    ("s(un",  ["s.left", "u", "n"]),
    ("s(um",  ["s.left", "u", "m"]),
    ("s(ut",  ["s.left", "u", "t"]),
    ("s(ud",  ["s.left", "u", "d"]),
    ("s(up",  ["s.left", "u.up", "p"]),
    ("s(ub",  ["s.left", "u.up", "b"]),
    ("s(uf",  ["s.left", "u.uf", "f"]),
    ("s(uv",  ["s.left", "u.uf", "v"]),
    ("s(ush", ["s.left", "u", "sh"]),
    ("s(uch", ["s.left", "u", "ch"]),
    ("s(uj",  ["s.left", "u", "j"]),
    ("s(us(", ["s.left", "u.up", "s.left"]),
    ("s(us",  ["s.left", "u.uf", "s.right"]),
    ("s(uth", ["s.left", "u", "th.over.angled"]),
])
def test_sL_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ngur",   ["ng", "u.ngu", "r"]),
    ("ngul",   ["ng", "u.ngu", "l"]),
    ("ngus",   ["ng", "u.ngu", "s.right"]),
])
def test_ng_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nkur",   ["nk", "u.ngu", "r"]),
    ("nkul",   ["nk", "u.ngu", "l"]),
    ("nkus",   ["nk", "u.ngu", "s.right"]),
])
def test_nk_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th(uk",    ["th.over", "u.tnu", "k"]),
    ("th(ug",    ["th.over", "u.tnu", "g"]),
    ("th(ur",    ["th.over", "u.tnu", "r"]),
    ("th(ul",    ["th.over", "u.tnu", "l"]),
    ("th(un",    ["th.over", "u.tnu", "n"]),
    ("th(um",    ["th.over", "u.tnu", "m"]),
    ("th(ut",    ["th.over", "u.tnut", "t"]),
    ("th(ud",    ["th.over", "u.tnut", "d"]),
    ("th(uf",    ["th.over", "u.tnu", "f"]),
    ("th(uv",    ["th.over", "u.tnu", "v"]),
    ("th(us",    ["th.over", "u.tnu", "s.right"]),
])
def test_thO_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnur",   ["tn", "u.tnu", "r"]),
    ("tnul",   ["tn", "u.tnu", "l"]),
    ("tnun",   ["tn", "u.tnu", "n"]),
    ("tnum",   ["tn", "u.tnu", "m"]),
    ("tnus)",  ["tn", "u.tnu", "s.right"]),
])
def test_tn_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tmur",   ["tm", "u.tnu", "r"]),
    ("tmul",   ["tm", "u.tnu", "l"]),
    ("tmun",   ["tm", "u.tnu", "n"]),
    ("tmum",   ["tm", "u.tnu", "m"]),
    ("tmus)",  ["tm", "u.tnu", "s.right"]),
])
def test_tm_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ntus)",  ["nt.angled", "u", "s.right"]),
    ("ntudf",  ["nt.angled", "u", "df.angled"]),
])
def test_nt_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mtus)",  ["mt.angled", "u", "s.right"]),
    ("mtudf",  ["mt.angled", "u", "df.angled"]),
])
def test_mt_u(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
