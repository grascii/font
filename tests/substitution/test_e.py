import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ek",   ["e.ek", "k"]),
    ("eg",   ["e.ek", "g"]),
    ("er",   ["e.er", "r"]),
    ("el",   ["e.er", "l"]),
    ("en",   ["e.en", "n"]),
    ("em",   ["e.en", "m"]),
    ("et",   ["e.et", "t"]),
    ("ed",   ["e.et", "d"]),
    ("ep",   ["e.ep", "p"]),
    ("eb",   ["e.ep", "b"]),
    ("ef",   ["e.ef", "f"]),
    ("ev",   ["e.ef", "v"]),
    ("es",   ["e.esR", "s.right"]),
    ("es(",  ["e.ep", "s.left"]),
    ("esh",  ["e.ech", "sh"]),
    ("ech",  ["e.ech", "ch"]),
    ("ej",   ["e.ech", "j"]),
    ("eth",  ["e.ethO", "th.over"]),
    ("eth)", ["e.ethU", "th.under"]),
    ("eng",  ["e.eng", "ng"]),
    ("enk",  ["e.eng", "nk"]),
])
def test_e_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ke",   ["k", "e.ke"]),
    ("ge",   ["g", "e.ke"]),
    ("re",   ["r", "e.re"]),
    ("le",   ["l", "e.re"]),
    ("ne",   ["n", "e.ne"]),
    ("me",   ["m", "e.ne"]),
    ("te",   ["t", "e.te"]),
    ("de",   ["d", "e.te"]),
    ("pe",   ["p", "e.pe"]),
    ("be",   ["b", "e.pe"]),
    ("fe",   ["f", "e.fe"]),
    ("ve",   ["v", "e.fe"]),
    ("se",   ["s.right", "e.fe"]),
    ("s(e",  ["s.left", "e.sLe"]),
    ("she",  ["sh", "e.che"]),
    ("che",  ["ch", "e.che"]),
    ("je",   ["j", "e.che"]),
    ("the",  ["th.over", "e.thOe"]),
    ("th)e", ["th.under", "e.thUe"]),
    ("nge",  ["ng", "e.nge"]),
    ("nke",  ["nk", "e.nge"]),
])
def test_e_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kek",  ["k", "e.kek", "k"]),
    ("keg",  ["k", "e.kek", "g"]),
    ("ker",  ["k", "e.ker", "r"]),
    ("kel",  ["k", "e.ker", "l"]),
    ("ken",  ["k", "e.en", "n"]),
    ("kem",  ["k", "e.en", "m"]),
    ("ket",  ["k", "e.et", "t"]),
    ("ked",  ["k", "e.et", "d"]),
    ("kep",  ["k", "e.ep", "p"]),
    ("keb",  ["k", "e.ep", "b"]),
    ("kef",  ["k", "e.kef", "f.cut"]),
    ("kev",  ["k", "e.kef", "v.cut"]),
    ("kesh", ["k", "e.kech", "sh"]),
    ("kech", ["k", "e.kech", "ch"]),
    ("kej",  ["k", "e.kech", "j"]),
    ("kes",  ["k", "e.kef", "s.right.cut"]),
    ("kes(", ["k", "e.ep", "s.left"]),
    ("keng", ["k", "e.keng", "ng"]),
    ("kenk", ["k", "e.keng", "nk"]),
    ("keth", ["k", "e.ketn", "th.over.skew30"]),
])
def test_k_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("gek",  ["g", "e.kek", "k"]),
    ("geg",  ["g", "e.kek", "g"]),
    ("ger",  ["g", "e.ker", "r"]),
    ("gel",  ["g", "e.ker", "l"]),
    ("gen",  ["g", "e.en", "n"]),
    ("gem",  ["g", "e.en", "m"]),
    ("get",  ["g", "e.et", "t"]),
    ("ged",  ["g", "e.et", "d"]),
    ("gep",  ["g", "e.ep", "p"]),
    ("geb",  ["g", "e.ep", "b"]),
    ("gef",  ["g", "e.kef", "f.cut"]),
    ("gev",  ["g", "e.kef", "v.cut"]),
    ("gesh", ["g", "e.kech", "sh"]),
    ("gech", ["g", "e.kech", "ch"]),
    ("gej",  ["g", "e.kech", "j"]),
    ("ges",  ["g", "e.kef", "s.right.cut"]),
    ("ges(", ["g", "e.ep", "s.left"]),
    ("geng", ["g", "e.keng", "ng"]),
    ("genk", ["g", "e.keng", "nk"]),
    ("geth", ["g", "e.ketn", "th.over.skew30"]),
])
def test_g_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("rek",   ["r", "e.ek", "k"]),
    ("reg",   ["r", "e.ek", "g"]),
    ("rer",   ["r", "e.rer", "r"]),
    ("rel",   ["r", "e.rer", "l"]),
    ("ren",   ["r", "e.ren", "n"]),
    ("rem",   ["r", "e.ren", "m"]),
    ("ret",   ["r", "e.ret", "t"]),
    ("red",   ["r", "e.ret", "d"]),
    ("rep",   ["r", "e.rep", "p"]),
    ("reb",   ["r", "e.rep", "b"]),
    ("ref",   ["r", "e.ref", "f.cut"]),
    ("rev",   ["r", "e.ref", "v.cut"]),
    ("resh",  ["r", "e.rech", "sh"]),
    ("rech",  ["r", "e.rech", "ch"]),
    ("rej",   ["r", "e.rech", "j"]),
    ("res",   ["r", "e.rep", "s.left"]),
    ("res)",  ["r", "e.ref", "s.right.cut"]),
    ("reng",  ["r", "e.reng", "ng"]),
    ("renk",  ["r", "e.reng", "nk"]),
    ("reth(", ["r", "e.retn", "th.over.skew30"]),
    ("reth",  ["r", "e.rent", "th.under"]),
])
def test_r_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("lek",   ["l", "e.ek", "k"]),
    ("leg",   ["l", "e.ek", "g"]),
    ("ler",   ["l", "e.rer", "r"]),
    ("lel",   ["l", "e.rer", "l"]),
    ("len",   ["l", "e.ren", "n"]),
    ("lem",   ["l", "e.ren", "m"]),
    ("let",   ["l", "e.ret", "t"]),
    ("led",   ["l", "e.ret", "d"]),
    ("lep",   ["l", "e.rep", "p"]),
    ("leb",   ["l", "e.rep", "b"]),
    ("lef",   ["l", "e.ref", "f.cut"]),
    ("lev",   ["l", "e.ref", "v.cut"]),
    ("lesh",  ["l", "e.rech", "sh"]),
    ("lech",  ["l", "e.rech", "ch"]),
    ("lej",   ["l", "e.rech", "j"]),
    ("les",   ["l", "e.rep", "s.left"]),
    ("les)",  ["l", "e.ref", "s.right.cut"]),
    ("leng",  ["l", "e.reng", "ng"]),
    ("lenk",  ["l", "e.reng", "nk"]),
    ("leth(", ["l", "e.retn", "th.over.skew30"]),
    ("leth",  ["l", "e.rent", "th.under"]),
])
def test_l_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nek",  ["n", "e.nek", "k"]),
    ("neg",  ["n", "e.nek", "g"]),
    ("ner",  ["n", "e.ner", "r"]),
    ("nel",  ["n", "e.ner", "l"]),
    ("nen",  ["n", "e.en", "n"]),
    ("nem",  ["n", "e.en", "m"]),
    ("net",  ["n", "e.net", "t"]),
    ("ned",  ["n", "e.net", "d"]),
    ("nep",  ["n", "e.nep", "p"]),
    ("neb",  ["n", "e.nep", "b"]),
    ("nef",  ["n", "e.nef", "f.cut"]),
    ("nev",  ["n", "e.nef", "v.cut"]),
    ("nesh", ["n", "e.nech", "sh"]),
    ("nech", ["n", "e.nech", "ch"]),
    ("nej",  ["n", "e.nech", "j"]),
    ("nes",  ["n", "e.nep", "s.left"]),
    ("nes)", ["n", "e.nef", "s.right.cut"]),
    ("neng", ["n", "e.neng", "ng"]),
    ("nenk", ["n", "e.neng", "nk"]),
    ("neth", ["n", "e.netn", "th.over"]),
])
def test_n_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mek",  ["m", "e.nek", "k"]),
    ("meg",  ["m", "e.nek", "g"]),
    ("mer",  ["m", "e.ner", "r"]),
    ("mel",  ["m", "e.ner", "l"]),
    ("men",  ["m", "e.en", "n"]),
    ("mem",  ["m", "e.en", "m"]),
    ("met",  ["m", "e.net", "t"]),
    ("med",  ["m", "e.net", "d"]),
    ("mep",  ["m", "e.nep", "p"]),
    ("meb",  ["m", "e.nep", "b"]),
    ("mef",  ["m", "e.nef", "f.cut"]),
    ("mev",  ["m", "e.nef", "v.cut"]),
    ("mesh", ["m", "e.nech", "sh"]),
    ("mech", ["m", "e.nech", "ch"]),
    ("mej",  ["m", "e.nech", "j"]),
    ("mes",  ["m", "e.nep", "s.left"]),
    ("mes)", ["m", "e.nef", "s.right.cut"]),
    ("meng", ["m", "e.neng", "ng"]),
    ("menk", ["m", "e.neng", "nk"]),
    ("meth", ["m", "e.netn", "th.over"]),
])
def test_m_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tek",   ["t", "e.ek", "k"]),
    ("teg",   ["t", "e.ek", "g"]),
    ("ter",   ["t", "e.ter", "r"]),
    ("tel",   ["t", "e.ter", "l"]),
    ("ten",   ["t", "e.ten", "n"]),
    ("tem",   ["t", "e.ten", "m"]),
    ("tet",   ["t", "e.et", "t"]),
    ("ted",   ["t", "e.et", "d"]),
    ("tep",   ["t", "e.tep", "p"]),
    ("teb",   ["t", "e.tep", "b"]),
    ("tef",   ["t", "e.tef", "f.cut"]),
    ("tev",   ["t", "e.tef", "v.cut"]),
    ("tesh",  ["t", "e.tech", "sh"]),
    ("tech",  ["t", "e.tech", "ch"]),
    ("tej",   ["t", "e.tech", "j"]),
    ("tes",   ["t", "e.tep", "s.left"]),
    ("tes)",  ["t", "e.tef", "s.right.cut"]),
    ("teng",  ["t", "e.teng", "ng"]),
    ("tenk",  ["t", "e.teng", "nk"]),
    ("teth",  ["t", "e.tetn", "th.over"]),
    ("teth)", ["t", "e.tent", "th.under"]),
])
def test_t_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("dek",   ["d", "e.ek", "k"]),
    ("deg",   ["d", "e.ek", "g"]),
    ("der",   ["d", "e.ter", "r"]),
    ("del",   ["d", "e.ter", "l"]),
    ("den",   ["d", "e.ten", "n"]),
    ("dem",   ["d", "e.ten", "m"]),
    ("det",   ["d", "e.et", "t"]),
    ("ded",   ["d", "e.et", "d"]),
    ("dep",   ["d", "e.tep", "p"]),
    ("deb",   ["d", "e.tep", "b"]),
    ("def",   ["d", "e.tef", "f.cut"]),
    ("dev",   ["d", "e.tef", "v.cut"]),
    ("desh",  ["d", "e.tech", "sh"]),
    ("dech",  ["d", "e.tech", "ch"]),
    ("dej",   ["d", "e.tech", "j"]),
    ("des",   ["d", "e.tep", "s.left"]),
    ("des)",  ["d", "e.tef", "s.right.cut"]),
    ("deng",  ["d", "e.teng", "ng"]),
    ("denk",  ["d", "e.teng", "nk"]),
    ("deth",  ["d", "e.tetn", "th.over"]),
    ("deth)", ["d", "e.tent", "th.under"]),
])
def test_d_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pek",  ["p.cut", "e.pek", "k"]),
    ("peg",  ["p.cut", "e.pek", "g"]),
    ("per",  ["p.cut", "e.per", "r"]),
    ("pel",  ["p.cut", "e.per", "l"]),
    ("pen",  ["p.cut", "e.pen", "n"]),
    ("pem",  ["p.cut", "e.pen", "m"]),
    ("pet",  ["p", "e.et", "t"]),
    ("ped",  ["p", "e.et", "d"]),
    ("pep",  ["p", "e.pep", "p"]),
    ("peb",  ["p", "e.pep", "b"]),
    ("pef",  ["p.cut", "e.pef", "f.cut"]),
    ("pev",  ["p.cut", "e.pef", "v.cut"]),
    ("pesh", ["p", "e.pech", "sh"]),
    ("pech", ["p", "e.pech", "ch"]),
    ("pej",  ["p", "e.pech", "j"]),
    ("pes",  ["p", "e.pep", "s.left"]),
    ("pes)", ["p.cut", "e.pef", "s.right.cut"]),
    ("peng", ["p.cut", "e.peng", "ng"]),
    ("penk", ["p.cut", "e.peng", "nk"]),
    ("peth", ["p.cut", "e.petn", "th.over.skew30"]),
])
def test_p_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("bek",  ["b.cut", "e.pek", "k"]),
    ("beg",  ["b.cut", "e.pek", "g"]),
    ("ber",  ["b.cut", "e.per", "r"]),
    ("bel",  ["b.cut", "e.per", "l"]),
    ("ben",  ["b.cut", "e.pen", "n"]),
    ("bem",  ["b.cut", "e.pen", "m"]),
    ("bet",  ["b", "e.et", "t"]),
    ("bed",  ["b", "e.et", "d"]),
    ("bep",  ["b", "e.pep", "p"]),
    ("beb",  ["b", "e.pep", "b"]),
    ("bef",  ["b.cut", "e.pef", "f.cut"]),
    ("bev",  ["b.cut", "e.pef", "v.cut"]),
    ("besh", ["b", "e.pech", "sh"]),
    ("bech", ["b", "e.pech", "ch"]),
    ("bej",  ["b", "e.pech", "j"]),
    ("bes",  ["b", "e.pep", "s.left"]),
    ("bes)", ["b.cut", "e.pef", "s.right.cut"]),
    ("beng", ["b.cut", "e.peng", "ng"]),
    ("benk", ["b.cut", "e.peng", "nk"]),
    ("beth", ["b.cut", "e.petn", "th.over.skew30"]),
])
def test_b_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
