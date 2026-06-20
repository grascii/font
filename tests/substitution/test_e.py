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
    ("etn",  ["e.etn", "tn"]),
    ("edn",  ["e.etn", "tn"]),
    ("etm",  ["e.etn", "tm"]),
    ("edm",  ["e.etn", "tm"]),
    ("ent",  ["e.ent", "nt"]),
    ("end",  ["e.ent", "nt"]),
    ("emt",  ["e.ent", "mt"]),
    ("emd",  ["e.ent", "mt"]),
    ("edf",  ["e.etn", "df"]),
    ("ejnt", ["e.ep", "jnt"]),
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
    ("ue",   ["u.cut", "e.ue"]),
    ("tne",  ["tn", "e.tne"]),
    ("dne",  ["tn", "e.tne"]),
    ("tme",  ["tm", "e.tne"]),
    ("dme",  ["tm", "e.tne"]),
    ("nte",  ["nt", "e.nte"]),
    ("nde",  ["nt", "e.nte"]),
    ("mte",  ["mt", "e.nte"]),
    ("mde",  ["mt", "e.nte"]),
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
    ("ketn", ["k", "e.ketn", "tn.skew30"]),
    ("kedn", ["k", "e.ketn", "tn.skew30"]),
    ("ketm", ["k", "e.ketn", "tm.skew30"]),
    ("kedm", ["k", "e.ketn", "tm.skew30"]),
    ("kent", ["k", "e.en", "nt"]),
    ("kend", ["k", "e.en", "nt"]),
    ("kemt", ["k", "e.en", "mt"]),
    ("kemd", ["k", "e.en", "mt"]),
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
    ("getn", ["g", "e.ketn", "tn.skew30"]),
    ("gedn", ["g", "e.ketn", "tn.skew30"]),
    ("getm", ["g", "e.ketn", "tm.skew30"]),
    ("gedm", ["g", "e.ketn", "tm.skew30"]),
    ("gent", ["g", "e.en", "nt"]),
    ("gend", ["g", "e.en", "nt"]),
    ("gemt", ["g", "e.en", "mt"]),
    ("gemd", ["g", "e.en", "mt"]),
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
    ("retn",  ["r", "e.retn", "tn.skew30"]),
    ("redn",  ["r", "e.retn", "tn.skew30"]),
    ("retm",  ["r", "e.retn", "tm.skew30"]),
    ("redm",  ["r", "e.retn", "tm.skew30"]),
    ("rent",  ["r", "e.rent", "nt"]),
    ("rend",  ["r", "e.rent", "nt"]),
    ("remt",  ["r", "e.rent", "mt"]),
    ("remd",  ["r", "e.rent", "mt"]),
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
    ("letn",  ["l", "e.retn", "tn.skew30"]),
    ("ledn",  ["l", "e.retn", "tn.skew30"]),
    ("letm",  ["l", "e.retn", "tm.skew30"]),
    ("ledm",  ["l", "e.retn", "tm.skew30"]),
    ("lent",  ["l", "e.rent", "nt"]),
    ("lend",  ["l", "e.rent", "nt"]),
    ("lemt",  ["l", "e.rent", "mt"]),
    ("lemd",  ["l", "e.rent", "mt"]),
])
def test_l_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nek",  ["n", "e.nek", "k"]),
    ("neg",  ["n", "e.nek", "g"]),
    ("ner",  ["n", "e.ner", "r"]),
    ("nel",  ["n", "e.ner", "l"]),
    ("nen",  ["n", "e.nen", "n"]),
    ("nem",  ["n", "e.nen", "m"]),
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
    ("neth", ["n", "e.netn", "th.over.angled"]),
    ("netn", ["n", "e.netn", "tn.angled"]),
    ("nedn", ["n", "e.netn", "tn.angled"]),
    ("netm", ["n", "e.netn", "tm.angled"]),
    ("nedm", ["n", "e.netn", "tm.angled"]),
    ("nent", ["n", "e.nen", "nt"]),
    ("nend", ["n", "e.nen", "nt"]),
    ("nemt", ["n", "e.nen", "mt"]),
    ("nemd", ["n", "e.nen", "mt"]),
])
def test_n_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mek",  ["m", "e.nek", "k"]),
    ("meg",  ["m", "e.nek", "g"]),
    ("mer",  ["m", "e.ner", "r"]),
    ("mel",  ["m", "e.ner", "l"]),
    ("men",  ["m", "e.nen", "n"]),
    ("mem",  ["m", "e.nen", "m"]),
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
    ("meth", ["m", "e.netn", "th.over.angled"]),
    ("metn", ["m", "e.netn", "tn.angled"]),
    ("medn", ["m", "e.netn", "tn.angled"]),
    ("metm", ["m", "e.netn", "tm.angled"]),
    ("medm", ["m", "e.netn", "tm.angled"]),
    ("ment", ["m", "e.nen", "nt"]),
    ("mend", ["m", "e.nen", "nt"]),
    ("memt", ["m", "e.nen", "mt"]),
    ("memd", ["m", "e.nen", "mt"]),
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
    ("tet",   ["t", "e.tet", "t"]),
    ("ted",   ["t", "e.tet", "d"]),
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
    ("teth",  ["t", "e.tetn", "th.over.angled"]),
    ("teth)", ["t", "e.tent", "th.under"]),
    ("tetn",  ["t", "e.tetn", "tn.angled"]),
    ("tedn",  ["t", "e.tetn", "tn.angled"]),
    ("tetm",  ["t", "e.tetn", "tm.angled"]),
    ("tedm",  ["t", "e.tetn", "tm.angled"]),
    ("tent",  ["t", "e.tent", "nt"]),
    ("tend",  ["t", "e.tent", "nt"]),
    ("temt",  ["t", "e.tent", "mt"]),
    ("temd",  ["t", "e.tent", "mt"]),
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
    ("det",   ["d", "e.tet", "t"]),
    ("ded",   ["d", "e.tet", "d"]),
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
    ("deth",  ["d", "e.tetn", "th.over.angled"]),
    ("deth)", ["d", "e.tent", "th.under"]),
    ("detn",  ["d", "e.tetn", "tn.angled"]),
    ("dedn",  ["d", "e.tetn", "tn.angled"]),
    ("detm",  ["d", "e.tetn", "tm.angled"]),
    ("dedm",  ["d", "e.tetn", "tm.angled"]),
    ("dent",  ["d", "e.tent", "nt"]),
    ("dend",  ["d", "e.tent", "nt"]),
    ("demt",  ["d", "e.tent", "mt"]),
    ("demd",  ["d", "e.tent", "mt"]),
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
    ("petn", ["p.cut", "e.petn", "tn.skew30"]),
    ("pedn", ["p.cut", "e.petn", "tn.skew30"]),
    ("petm", ["p.cut", "e.petn", "tm.skew30"]),
    ("pedm", ["p.cut", "e.petn", "tm.skew30"]),
    ("pent", ["p", "e.pent", "nt"]),
    ("pend", ["p", "e.pent", "nt"]),
    ("pemt", ["p", "e.pent", "mt"]),
    ("pemd", ["p", "e.pent", "mt"]),
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
    ("betn", ["b.cut", "e.petn", "tn.skew30"]),
    ("bedn", ["b.cut", "e.petn", "tn.skew30"]),
    ("betm", ["b.cut", "e.petn", "tm.skew30"]),
    ("bedm", ["b.cut", "e.petn", "tm.skew30"]),
    ("bent", ["b", "e.pent", "nt"]),
    ("bend", ["b", "e.pent", "nt"]),
    ("bemt", ["b", "e.pent", "mt"]),
    ("bemd", ["b", "e.pent", "mt"]),
])
def test_b_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fek",   ["f", "e.fek", "k"]),
    ("feg",   ["f", "e.fek", "g"]),
    ("fer",   ["f", "e.fer", "r"]),
    ("fel",   ["f", "e.fer", "l"]),
    ("fen",   ["f", "e.fen", "n"]),
    ("fem",   ["f", "e.fen", "m"]),
    ("fet",   ["f", "e.fet", "t"]),
    ("fed",   ["f", "e.fet", "d"]),
    ("fep",   ["f", "e.fep", "p"]),
    ("feb",   ["f", "e.fep", "b"]),
    ("fef",   ["f", "e.fef", "f"]),
    ("fev",   ["f", "e.fef", "v"]),
    ("fesh",  ["f", "e.ech", "sh"]),
    ("fech",  ["f", "e.ech", "ch"]),
    ("fej",   ["f", "e.ech", "j"]),
    ("fes",   ["f", "e.fef", "s.right"]),
    ("fes(",  ["f", "e.fep", "s.left"]),
    ("feng",  ["f", "e.feng", "ng"]),
    ("fenk",  ["f", "e.feng", "nk"]),
    ("feth",  ["f", "e.fetn", "th.over.skew45"]),
    ("feth)", ["f", "e.fent", "th.under"]),
    ("fetn",  ["f", "e.fetn", "tn.skew45"]),
    ("fedn",  ["f", "e.fetn", "tn.skew45"]),
    ("fetm",  ["f", "e.fetn", "tm.skew45"]),
    ("fedm",  ["f", "e.fetn", "tm.skew45"]),
    ("fent",  ["f", "e.fent", "nt"]),
    ("fend",  ["f", "e.fent", "nt"]),
    ("femt",  ["f", "e.fent", "mt"]),
    ("femd",  ["f", "e.fent", "mt"]),
])
def test_f_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("vek",   ["v", "e.fek", "k"]),
    ("veg",   ["v", "e.fek", "g"]),
    ("ver",   ["v", "e.fer", "r"]),
    ("vel",   ["v", "e.fer", "l"]),
    ("ven",   ["v", "e.fen", "n"]),
    ("vem",   ["v", "e.fen", "m"]),
    ("vet",   ["v", "e.fet", "t"]),
    ("ved",   ["v", "e.fet", "d"]),
    ("vep",   ["v", "e.fep", "p"]),
    ("veb",   ["v", "e.fep", "b"]),
    ("vef",   ["v", "e.fef", "f"]),
    ("vev",   ["v", "e.fef", "v"]),
    ("vesh",  ["v", "e.ech", "sh"]),
    ("vech",  ["v", "e.ech", "ch"]),
    ("vej",   ["v", "e.ech", "j"]),
    ("ves",   ["v", "e.fef", "s.right"]),
    ("ves(",  ["v", "e.fep", "s.left"]),
    ("veng",  ["v", "e.feng", "ng"]),
    ("venk",  ["v", "e.feng", "nk"]),
    ("veth",  ["v", "e.fetn", "th.over.skew45"]),
    ("veth)", ["v", "e.fent", "th.under"]),
    ("vetn",  ["v", "e.fetn", "tn.skew45"]),
    ("vedn",  ["v", "e.fetn", "tn.skew45"]),
    ("vetm",  ["v", "e.fetn", "tm.skew45"]),
    ("vedm",  ["v", "e.fetn", "tm.skew45"]),
    ("vent",  ["v", "e.fent", "nt"]),
    ("vend",  ["v", "e.fent", "nt"]),
    ("vemt",  ["v", "e.fent", "mt"]),
    ("vemd",  ["v", "e.fent", "mt"]),
])
def test_v_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shek",   ["sh", "e.chek", "k"]),
    ("sheg",   ["sh", "e.chek", "g"]),
    ("sher",   ["sh", "e.cher", "r"]),
    ("shel",   ["sh", "e.cher", "l"]),
    ("shen",   ["sh", "e.chen", "n"]),
    ("shem",   ["sh", "e.chen", "m"]),
    ("shet",   ["sh", "e.chet", "t"]),
    ("shed",   ["sh", "e.chet", "d"]),
    ("shep",   ["sh", "e.ep", "p"]),
    ("sheb",   ["sh", "e.ep", "b"]),
    ("shef",   ["sh", "e.ef", "f"]),
    ("shev",   ["sh", "e.ef", "v"]),
    ("shesh",  ["sh", "e.chech", "sh"]),
    ("shech",  ["sh", "e.chech", "ch"]),
    ("shej",   ["sh", "e.chech", "j"]),
    ("shes",   ["sh", "e.esR", "s.right"]),
    ("shes(",  ["sh", "e.ep", "s.left"]),
    ("sheng",  ["sh", "e.cheng", "ng"]),
    ("shenk",  ["sh", "e.cheng", "nk"]),
    ("sheth",  ["sh", "e.chetn", "th.over.skew30"]),
])
def test_sh_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("chek",   ["ch", "e.chek", "k"]),
    ("cheg",   ["ch", "e.chek", "g"]),
    ("cher",   ["ch", "e.cher", "r"]),
    ("chel",   ["ch", "e.cher", "l"]),
    ("chen",   ["ch", "e.chen", "n"]),
    ("chem",   ["ch", "e.chen", "m"]),
    ("chet",   ["ch", "e.chet", "t"]),
    ("ched",   ["ch", "e.chet", "d"]),
    ("chep",   ["ch", "e.ep", "p"]),
    ("cheb",   ["ch", "e.ep", "b"]),
    ("chef",   ["ch", "e.ef", "f"]),
    ("chev",   ["ch", "e.ef", "v"]),
    ("chesh",  ["ch", "e.chech", "sh"]),
    ("chech",  ["ch", "e.chech", "ch"]),
    ("chej",   ["ch", "e.chech", "j"]),
    ("ches",   ["ch", "e.esR", "s.right"]),
    ("ches(",  ["ch", "e.ep", "s.left"]),
    ("cheng",  ["ch", "e.cheng", "ng"]),
    ("chenk",  ["ch", "e.cheng", "nk"]),
    ("cheth",  ["ch", "e.chetn", "th.over.skew30"]),
])
def test_ch_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("jek",   ["j", "e.chek", "k"]),
    ("jeg",   ["j", "e.chek", "g"]),
    ("jer",   ["j", "e.cher", "r"]),
    ("jel",   ["j", "e.cher", "l"]),
    ("jen",   ["j", "e.chen", "n"]),
    ("jem",   ["j", "e.chen", "m"]),
    ("jet",   ["j", "e.chet", "t"]),
    ("jed",   ["j", "e.chet", "d"]),
    ("jep",   ["j", "e.ep", "p"]),
    ("jeb",   ["j", "e.ep", "b"]),
    ("jef",   ["j", "e.ef", "f"]),
    ("jev",   ["j", "e.ef", "v"]),
    ("jesh",  ["j", "e.chech", "sh"]),
    ("jech",  ["j", "e.chech", "ch"]),
    ("jej",   ["j", "e.chech", "j"]),
    ("jes",   ["j", "e.esR", "s.right"]),
    ("jes(",  ["j", "e.ep", "s.left"]),
    ("jeng",  ["j", "e.cheng", "ng"]),
    ("jenk",  ["j", "e.cheng", "nk"]),
    ("jeth",  ["j", "e.chetn", "th.over.skew30"]),
])
def test_j_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)ek",  ["s.right", "e.fek", "k"]),
    ("s)eg",  ["s.right", "e.fek", "g"]),
    ("s)er",  ["s.right", "e.fer", "r"]),
    ("s)el",  ["s.right", "e.fer", "l"]),
    ("s)en",  ["s.right", "e.fen", "n"]),
    ("s)em",  ["s.right", "e.fen", "m"]),
    ("s)et",  ["s.right", "e.fet", "t"]),
    ("s)ed",  ["s.right", "e.fet", "d"]),
    ("s)ep",  ["s.right", "e.fep", "p"]),
    ("s)eb",  ["s.right", "e.fep", "b"]),
    ("s)ef",  ["s.right", "e.fef", "f"]),
    ("s)ev",  ["s.right", "e.fef", "v"]),
    ("s)esh", ["s.right", "e.ech", "sh"]),
    ("s)ech", ["s.right", "e.ech", "ch"]),
    ("s)ej",  ["s.right", "e.ech", "j"]),
    ("s)es",  ["s.right", "e.fef", "s.right"]),
    ("s)es(", ["s.right", "e.fep", "s.left"]),
    ("s)eng", ["s.right", "e.feng", "ng"]),
    ("s)enk", ["s.right", "e.feng", "nk"]),
    ("s)eth", ["s.right", "e.fetn", "th.over.skew45"]),
    ("s)eth)", ["s.right", "e.fent", "th.under"]),
    ("s)etn",  ["s.right", "e.fetn", "tn.skew45"]),
    ("s)edn",  ["s.right", "e.fetn", "tn.skew45"]),
    ("s)etm",  ["s.right", "e.fetn", "tm.skew45"]),
    ("s)edm",  ["s.right", "e.fetn", "tm.skew45"]),
    ("s)ent",  ["s.right", "e.fent", "nt"]),
    ("s)end",  ["s.right", "e.fent", "nt"]),
    ("s)emt",  ["s.right", "e.fent", "mt"]),
    ("s)emd",  ["s.right", "e.fent", "mt"]),
])
def test_sR_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s(ek",  ["s.left.cut", "e.pek", "k"]),
    ("s(eg",  ["s.left.cut", "e.pek", "g"]),
    ("s(er",  ["s.left.cut", "e.per", "r"]),
    ("s(el",  ["s.left.cut", "e.per", "l"]),
    ("s(en",  ["s.left.cut", "e.pen", "n"]),
    ("s(em",  ["s.left.cut", "e.pen", "m"]),
    ("s(et",  ["s.left", "e.et", "t"]),
    ("s(ed",  ["s.left", "e.et", "d"]),
    ("s(ep",  ["s.left", "e.pep", "p"]),
    ("s(eb",  ["s.left", "e.pep", "b"]),
    ("s(ef",  ["s.left.cut", "e.pef", "f.cut"]),
    ("s(ev",  ["s.left.cut", "e.pef", "v.cut"]),
    ("s(esh", ["s.left", "e.pech", "sh"]),
    ("s(ech", ["s.left", "e.pech", "ch"]),
    ("s(ej",  ["s.left", "e.pech", "j"]),
    ("s(es(",  ["s.left", "e.pep", "s.left"]),
    ("s(es)", ["s.left.cut", "e.pef", "s.right.cut"]),
    ("s(ent",  ["s.left", "e.pent", "nt"]),
    ("s(end",  ["s.left", "e.pent", "nt"]),
    ("s(emt",  ["s.left", "e.pent", "mt"]),
    ("s(emd",  ["s.left", "e.pent", "mt"]),
])
def test_sL_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ngen",   ["ng", "e.ngen", "n"]),
    ("ngem",   ["ng", "e.ngen", "m"]),
    ("nget",   ["ng", "e.nget", "t"]),
    ("nged",   ["ng", "e.nget", "d"]),
    ("ngep",   ["ng", "e.ngep", "p"]),
    ("ngeb",   ["ng", "e.ngep", "b"]),
    ("ngesh",  ["ng", "e.ngech", "sh"]),
    ("ngech",  ["ng", "e.ngech", "ch"]),
    ("ngej",   ["ng", "e.ngech", "j"]),
    ("nges(",  ["ng", "e.ngep", "s.left"]),
    ("ngent",  ["ng", "e.ngen", "nt"]),
    ("ngend",  ["ng", "e.ngen", "nt"]),
    ("ngemt",  ["ng", "e.ngen", "mt"]),
    ("ngemd",  ["ng", "e.ngen", "mt"]),
])
def test_ng_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nken",   ["nk", "e.ngen", "n"]),
    ("nkem",   ["nk", "e.ngen", "m"]),
    ("nket",   ["nk", "e.nget", "t"]),
    ("nked",   ["nk", "e.nget", "d"]),
    ("nkep",   ["nk", "e.ngep", "p"]),
    ("nkeb",   ["nk", "e.ngep", "b"]),
    ("nkesh",  ["nk", "e.ngech", "sh"]),
    ("nkech",  ["nk", "e.ngech", "ch"]),
    ("nkej",   ["nk", "e.ngech", "j"]),
    ("nkes(",  ["nk", "e.ngep", "s.left"]),
    ("nkent",  ["nk", "e.ngen", "nt"]),
    ("nkend",  ["nk", "e.ngen", "nt"]),
    ("nkemt",  ["nk", "e.ngen", "mt"]),
    ("nkemd",  ["nk", "e.ngen", "mt"]),
])
def test_nk_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th(ek",    ["th.over", "e.tnek", "k"]),
    ("th(eg",    ["th.over", "e.tnek", "g"]),
    ("th(en",    ["th.over", "e.tnen", "n"]),
    ("th(em",    ["th.over", "e.tnen", "m"]),
    ("th(et",    ["th.over", "e.tnet", "t"]),
    ("th(ed",    ["th.over", "e.tnet", "d"]),
    ("th(ef",    ["th.over", "e.tnef", "f"]),
    ("th(ev",    ["th.over", "e.tnef", "v"]),
    ("th(es",    ["th.over", "e.tnef", "s.right"]),
    ("th(eth",   ["th.over", "e.tnetn", "th.over.angled"]),
])
def test_thO_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th)er",    ["th.under.skew30", "e.nter", "r"]),
    ("th)el",    ["th.under.skew30", "e.nter", "l"]),
    ("th)en",    ["th.under.angled", "e.nten", "n"]),
    ("th)em",    ["th.under.angled", "e.nten", "m"]),
    ("th)et",    ["th.under.angled", "e.ntet", "t"]),
    ("th)ed",    ["th.under.angled", "e.ntet", "d"]),
])
def test_thU_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uek",   ["u.cut", "e.uek", "k"]),
    ("ueg",   ["u.cut", "e.uek", "g"]),
    ("uer",   ["u.cut", "e.uer", "r.cut"]),
    ("uel",   ["u.cut", "e.uer", "l.cut"]),
    ("uen",   ["u.cut", "e.uen", "n"]),
    ("uem",   ["u.cut", "e.uen", "m"]),
    ("uet",   ["u.cut", "e.uet", "t"]),
    ("ued",   ["u.cut", "e.uet", "d"]),
    ("uep",   ["u.cut", "e.uep", "p"]),
    ("ueb",   ["u.cut", "e.uep", "b"]),
    ("uef",   ["u.cut", "e.uef", "f.cut"]),
    ("uev",   ["u.cut", "e.uef", "v.cut"]),
    ("uesh",  ["u.cut", "e.uech", "sh"]),
    ("uech",  ["u.cut", "e.uech", "ch"]),
    ("uej",   ["u.cut", "e.uech", "j"]),
    ("ues(",  ["u.cut", "e.uep", "s.left"]),
    ("ues",   ["u.cut", "e.uef", "s.right.cut"]),
    ("ueng",  ["u.cut", "e.ueng", "ng"]),
    ("uenk",  ["u.cut", "e.ueng", "nk"]),
    ("ueth",  ["u.cut", "e.uetn", "th.over.skew30"]),
    ("ueth)", ["u.cut", "e.uen", "th.under"]),
    ("uetn",  ["u.cut", "e.uetn", "tn.skew30"]),
    ("uedn",  ["u.cut", "e.uetn", "tn.skew30"]),
    ("uetm",  ["u.cut", "e.uetn", "tm.skew30"]),
    ("uedm",  ["u.cut", "e.uetn", "tm.skew30"]),
    ("uent",  ["u.cut", "e.uen", "nt"]),
    ("uend",  ["u.cut", "e.uen", "nt"]),
    ("uemt",  ["u.cut", "e.uen", "mt"]),
    ("uemd",  ["u.cut", "e.uen", "mt"]),
])
def test_u_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnek", ["tn", "e.tnek", "k"]),
    ("tneg", ["tn", "e.tnek", "g"]),
    ("tnen", ["tn", "e.tnen", "n"]),
    ("tnem", ["tn", "e.tnen", "m"]),
    ("tnet", ["tn", "e.tnet", "t"]),
    ("tned", ["tn", "e.tnet", "d"]),
    ("tnef", ["tn", "e.tnef", "f"]),
    ("tnev", ["tn", "e.tnef", "v"]),
    ("tnes", ["tn", "e.tnef", "s.right"]),
])
def test_tn_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tmek", ["tm", "e.tnek", "k"]),
    ("tmeg", ["tm", "e.tnek", "g"]),
    ("tmen", ["tm", "e.tnen", "n"]),
    ("tmem", ["tm", "e.tnen", "m"]),
    ("tmet", ["tm", "e.tnet", "t"]),
    ("tmed", ["tm", "e.tnet", "d"]),
    ("tmef", ["tm", "e.tnef", "f"]),
    ("tmev", ["tm", "e.tnef", "v"]),
    ("tmes", ["tm", "e.tnef", "s.right"]),
])
def test_tm_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nter", ["nt.skew30", "e.nter", "r"]),
    ("ntel", ["nt.skew30", "e.nter", "l"]),
    ("nten", ["nt.angled", "e.nten", "n"]),
    ("ntem", ["nt.angled", "e.nten", "m"]),
    ("ntet", ["nt.angled", "e.ntet", "t"]),
    ("nted", ["nt.angled", "e.ntet", "d"]),
    ("ntep", ["nt.skew45", "e.ntep", "p"]),
    ("nteb", ["nt.skew45", "e.ntep", "b"]),
    ("ntes", ["nt.skew45", "e.ntep", "s.left"]),
])
def test_nt_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mter", ["mt.skew30", "e.nter", "r"]),
    ("mtel", ["mt.skew30", "e.nter", "l"]),
    ("mten", ["mt.angled", "e.nten", "n"]),
    ("mtem", ["mt.angled", "e.nten", "m"]),
    ("mtet", ["mt.angled", "e.ntet", "t"]),
    ("mted", ["mt.angled", "e.ntet", "d"]),
    ("mtep", ["mt.skew45", "e.ntep", "p"]),
    ("mteb", ["mt.skew45", "e.ntep", "b"]),
    ("mtes", ["mt.skew45", "e.ntep", "s.left"]),
])
def test_mt_e(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
