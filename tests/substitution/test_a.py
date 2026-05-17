import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ak", ["a.ak", "k"]),
    ("ag", ["a.ak", "g"]),
    ("ar", ["a.ar", "r"]),
    ("al", ["a.al", "l"]),
    ("an", ["a.an", "n"]),
    ("am", ["a.an", "m"]),
    ("at", ["a.at", "t"]),
    ("ad", ["a.at", "d"]),
    ("ap", ["a.ap", "p"]),
    ("ab", ["a.ap", "b"]),
    ("af", ["a.af", "f"]),
    ("av", ["a.av", "v"]),
    ("as", ["a.asR", "s.right"]),
    ("as(", ["a.ap", "s.left"]),
    ("ash", ["a.ach", "sh"]),
    ("ach", ["a.ach", "ch"]),
    ("aj", ["a.ach", "j"]),
    ("ath", ["a.athO", "th.over"]),
    ("ath)", ["a.athU", "th.under"]),
    ("ang", ["a.ang", "ng"]),
    ("ank", ["a.ang", "nk"]),
    ("atn", ["a.atn", "tn"]),
    ("adn", ["a.atn", "tn"]),
    ("atm", ["a.atm", "tm"]),
    ("adm", ["a.atm", "tm"]),
])
def test_a_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ka", ["k", "a.ka"]),
    ("ga", ["g", "a.ka"]),
    ("ra", ["r", "a.ra"]),
    ("la", ["l", "a.ra"]),
    ("na", ["n", "a.na"]),
    ("ma", ["m", "a.na"]),
    ("ta", ["t", "a.ta"]),
    ("da", ["d", "a.ta"]),
    ("pa", ["p", "a.pa"]),
    ("ba", ["b", "a.ba"]),
    ("fa", ["f", "a.fa"]),
    ("va", ["v", "a.fa"]),
    ("sa", ["s.right", "a.sRa"]),
    ("s(a", ["s.left", "a.sLa"]),
    ("sha", ["sh", "a.cha"]),
    ("cha", ["ch", "a.cha"]),
    ("ja", ["j", "a.cha"]),
    ("tha", ["th.over", "a.thOa"]),
    ("th)a", ["th.under", "a.thUa"]),
    ("nga", ["ng", "a.nga"]),
    ("nka", ["nk", "a.nga"]),
    ("ua", ["u.cut", "a.ua"]),
    ("tna", ["tn", "a.tna"]),
    ("dna", ["tn", "a.tna"]),
    ("tma", ["tm", "a.tna"]),
    ("dma", ["tm", "a.tna"]),
    ("nta", ["nt", "a.nta"]),
    ("nda", ["nt", "a.nta"]),
    ("mta", ["mt", "a.mta"]),
    ("mda", ["mt", "a.mta"]),
])
def test_a_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("kak", ["k", "a.kak", "k"]),
    ("kag", ["k", "a.kak", "g"]),
    ("kar", ["k", "a.kar", "r"]),
    ("kal", ["k", "a.kar", "l"]),
    ("kan", ["k", "a.kan", "n"]),
    ("kam", ["k", "a.kan", "m"]),
    ("kat", ["k", "a.kat", "t"]),
    ("kad", ["k", "a.kat", "d"]),
    ("kap", ["k", "a.kap", "p"]),
    ("kab", ["k", "a.kap", "b"]),
    ("kaf", ["k", "a.kaf", "f.cut"]),
    ("kav", ["k", "a.kaf", "v.cut"]),
    ("kash", ["k", "a.kach", "sh"]),
    ("kach", ["k", "a.kach", "ch"]),
    ("kaj", ["k", "a.kach", "j"]),
    ("kas", ["k", "a.kaf", "s.right.cut"]),
    ("kas(", ["k", "a.kap", "s.left"]),
    ("kang", ["k", "a.kang", "ng"]),
    ("kank", ["k", "a.kang", "nk"]),
    ("kath", ["k", "a.katn", "th.over.skew30"]),
])
def test_k_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("gak", ["g", "a.kak", "k"]),
    ("gag", ["g", "a.kak", "g"]),
    ("gar", ["g", "a.kar", "r"]),
    ("gal", ["g", "a.kar", "l"]),
    ("gan", ["g", "a.kan", "n"]),
    ("gam", ["g", "a.kan", "m"]),
    ("gat", ["g", "a.kat", "t"]),
    ("gad", ["g", "a.kat", "d"]),
    ("gap", ["g", "a.kap", "p"]),
    ("gab", ["g", "a.kap", "b"]),
    ("gaf", ["g", "a.kaf", "f.cut"]),
    ("gav", ["g", "a.kaf", "v.cut"]),
    ("gash", ["g", "a.kach", "sh"]),
    ("gach", ["g", "a.kach", "ch"]),
    ("gaj", ["g", "a.kach", "j"]),
    ("gas", ["g", "a.kaf", "s.right.cut"]),
    ("gas(", ["g", "a.kap", "s.left"]),
    ("gang", ["g", "a.kang", "ng"]),
    ("gank", ["g", "a.kang", "nk"]),
    ("gath", ["g", "a.katn", "th.over.skew30"]),
])
def test_g_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("rak",  ["r", "a.rak", "k"]),
    ("rag",  ["r", "a.rak", "g"]),
    ("rar",  ["r", "a.rar", "r"]),
    ("ral",  ["r", "a.rar", "l"]),
    ("ran",  ["r", "a.ran", "n"]),
    ("ram",  ["r", "a.ran", "m"]),
    ("rat",  ["r", "a.rat", "t"]),
    ("rad",  ["r", "a.rat", "d"]),
    ("rap",  ["r", "a.rap", "p"]),
    ("rab",  ["r", "a.rap", "b"]),
    ("raf",  ["r", "a.raf", "f.cut"]),
    ("rav",  ["r", "a.raf", "v.cut"]),
    ("rash", ["r", "a.rach", "sh"]),
    ("rach", ["r", "a.rach", "ch"]),
    ("raj",  ["r", "a.rach", "j"]),
    ("ras",  ["r", "a.rap", "s.left"]),
    ("ras)", ["r", "a.raf", "s.right.cut"]),
    ("rang", ["r", "a.rang", "ng"]),
    ("rank", ["r", "a.rang", "nk"]),
    ("rath", ["r", "a.rant", "th.under"]),
])
def test_r_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("lak",  ["l", "a.rak", "k"]),
    ("lag",  ["l", "a.rak", "g"]),
    ("lar",  ["l", "a.rar", "r"]),
    ("lal",  ["l", "a.rar", "l"]),
    ("lan",  ["l", "a.ran", "n"]),
    ("lam",  ["l", "a.ran", "m"]),
    ("lat",  ["l", "a.rat", "t"]),
    ("lad",  ["l", "a.rat", "d"]),
    ("lap",  ["l", "a.rap", "p"]),
    ("lab",  ["l", "a.rap", "b"]),
    ("laf",  ["l", "a.raf", "f.cut"]),
    ("lav",  ["l", "a.raf", "v.cut"]),
    ("lash", ["l", "a.rach", "sh"]),
    ("lach", ["l", "a.rach", "ch"]),
    ("laj",  ["l", "a.rach", "j"]),
    ("las",  ["l", "a.rap", "s.left"]),
    ("las)", ["l", "a.raf", "s.right.cut"]),
    ("lang", ["l", "a.rang", "ng"]),
    ("lank", ["l", "a.rang", "nk"]),
    ("lath", ["l", "a.rant", "th.under"]),
])
def test_l_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nak",  ["n", "a.nak", "k"]),
    ("nag",  ["n", "a.nak", "g"]),
    ("nar",  ["n", "a.nar", "r"]),
    ("nal",  ["n", "a.nar", "l"]),
    ("nan",  ["n", "a.nan", "n"]),
    ("nam",  ["n", "a.nan", "m"]),
    ("nat",  ["n", "a.nat", "t"]),
    ("nad",  ["n", "a.nat", "d"]),
    ("nap",  ["n", "a.nap", "p"]),
    ("nab",  ["n", "a.nap", "b"]),
    ("naf",  ["n", "a.naf", "f.cut"]),
    ("nav",  ["n", "a.naf", "v.cut"]),
    ("nash", ["n", "a.nach", "sh"]),
    ("nach", ["n", "a.nach", "ch"]),
    ("naj",  ["n", "a.nach", "j"]),
    ("nas",  ["n", "a.nap", "s.left"]),
    ("nas)", ["n", "a.naf", "s.right.cut"]),
    ("nang", ["n", "a.nang", "ng"]),
    ("nank", ["n", "a.nang", "nk"]),
    ("nath", ["n", "a.natn", "th.over"]),
])
def test_n_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("mak",  ["m", "a.nak", "k"]),
    ("mag",  ["m", "a.nak", "g"]),
    ("mar",  ["m", "a.nar", "r"]),
    ("mal",  ["m", "a.nar", "l"]),
    ("man",  ["m", "a.nan", "n"]),
    ("mam",  ["m", "a.nan", "m"]),
    ("mat",  ["m", "a.nat", "t"]),
    ("mad",  ["m", "a.nat", "d"]),
    ("map",  ["m", "a.nap", "p"]),
    ("mab",  ["m", "a.nap", "b"]),
    ("maf",  ["m", "a.naf", "f.cut"]),
    ("mav",  ["m", "a.naf", "v.cut"]),
    ("mash", ["m", "a.nach", "sh"]),
    ("mach", ["m", "a.nach", "ch"]),
    ("maj",  ["m", "a.nach", "j"]),
    ("mas",  ["m", "a.nap", "s.left"]),
    ("mas)", ["m", "a.naf", "s.right.cut"]),
    ("mang", ["m", "a.nang", "ng"]),
    ("mank", ["m", "a.nang", "nk"]),
    ("math", ["m", "a.natn", "th.over"]),
])
def test_m_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tak",  ["t", "a.tak", "k"]),
    ("tag",  ["t", "a.tak", "g"]),
    ("tar",  ["t", "a.tar", "r"]),
    ("tal",  ["t", "a.tar", "l"]),
    ("tan",  ["t", "a.tan", "n"]),
    ("tam",  ["t", "a.tan", "m"]),
    ("tat",  ["t", "a.tat", "t"]),
    ("tad",  ["t", "a.tat", "d"]),
    ("tap",  ["t", "a.tap", "p"]),
    ("tab",  ["t", "a.tap", "b"]),
    ("taf",  ["t", "a.taf", "f.cut"]),
    ("tav",  ["t", "a.taf", "v.cut"]),
    ("tash", ["t", "a.tach", "sh"]),
    ("tach", ["t", "a.tach", "ch"]),
    ("taj",  ["t", "a.tach", "j"]),
    ("tas",  ["t", "a.tap", "s.left"]),
    ("tas)", ["t", "a.taf", "s.right.cut"]),
    ("tang", ["t", "a.tang", "ng"]),
    ("tank", ["t", "a.tang", "nk"]),
])
def test_t_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("dak",  ["d", "a.tak", "k"]),
    ("dag",  ["d", "a.tak", "g"]),
    ("dar",  ["d", "a.tar", "r"]),
    ("dal",  ["d", "a.tar", "l"]),
    ("dan",  ["d", "a.tan", "n"]),
    ("dam",  ["d", "a.tan", "m"]),
    ("dat",  ["d", "a.tat", "t"]),
    ("dad",  ["d", "a.tat", "d"]),
    ("dap",  ["d", "a.tap", "p"]),
    ("dab",  ["d", "a.tap", "b"]),
    ("daf",  ["d", "a.taf", "f.cut"]),
    ("dav",  ["d", "a.taf", "v.cut"]),
    ("dash", ["d", "a.tach", "sh"]),
    ("dach", ["d", "a.tach", "ch"]),
    ("daj",  ["d", "a.tach", "j"]),
    ("das",  ["d", "a.tap", "s.left"]),
    ("das)", ["d", "a.taf", "s.right.cut"]),
    ("dang", ["d", "a.tang", "ng"]),
    ("dank", ["d", "a.tang", "nk"]),
])
def test_d_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pak",  ["p.cut", "a.pak", "k"]),
    ("pag",  ["p.cut", "a.pak", "g"]),
    ("par",  ["p.cut", "a.par", "r"]),
    ("pal",  ["p.cut", "a.par", "l"]),
    ("pan",  ["p.cut", "a.pan", "n"]),
    ("pam",  ["p.cut", "a.pan", "m"]),
    ("pat",  ["p", "a.pat", "t"]),
    ("pad",  ["p", "a.pat", "d"]),
    ("pap",  ["p", "a.pap", "p"]),
    ("pab",  ["p", "a.pap", "b"]),
    ("paf",  ["p.cut", "a.paf", "f.cut"]),
    ("pav",  ["p.cut", "a.paf", "v.cut"]),
    ("pash", ["p", "a.pach", "sh"]),
    ("pach", ["p", "a.pach", "ch"]),
    ("paj",  ["p", "a.pach", "j"]),
    ("pas",  ["p", "a.pap", "s.left"]),
    ("pas)", ["p.cut", "a.paf", "s.right.cut"]),
    ("pang", ["p.cut", "a.pang", "ng"]),
    ("pank", ["p.cut", "a.pang", "nk"]),
    ("path", ["p.cut", "a.patn", "th.over.skew30"]),
])
def test_p_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("bak",  ["b.cut", "a.pak", "k"]),
    ("bag",  ["b.cut", "a.pak", "g"]),
    ("bar",  ["b.cut", "a.par", "r"]),
    ("bal",  ["b.cut", "a.par", "l"]),
    ("ban",  ["b.cut", "a.pan", "n"]),
    ("bam",  ["b.cut", "a.pan", "m"]),
    ("bat",  ["b", "a.pat", "t"]),
    ("bad",  ["b", "a.pat", "d"]),
    ("bap",  ["b", "a.pap", "p"]),
    ("bab",  ["b", "a.pap", "b"]),
    ("baf",  ["b.cut", "a.paf", "f.cut"]),
    ("bav",  ["b.cut", "a.paf", "v.cut"]),
    ("bash", ["b", "a.pach", "sh"]),
    ("bach", ["b", "a.pach", "ch"]),
    ("baj",  ["b", "a.pach", "j"]),
    ("bas",  ["b", "a.pap", "s.left"]),
    ("bas)", ["b.cut", "a.paf", "s.right.cut"]),
    ("bang", ["b.cut", "a.pang", "ng"]),
    ("bank", ["b.cut", "a.pang", "nk"]),
    ("bath", ["b.cut", "a.patn", "th.over.skew30"]),
])
def test_b_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("fak",  ["f", "a.fak", "k"]),
    ("fag",  ["f", "a.fak", "g"]),
    ("far",  ["f", "a.far", "r"]),
    ("fal",  ["f", "a.far", "l"]),
    ("fan",  ["f", "a.fan", "n"]),
    ("fam",  ["f", "a.fan", "m"]),
    ("fat",  ["f", "a.fat", "t"]),
    ("fad",  ["f", "a.fat", "d"]),
    ("fap",  ["f", "a.fap", "p"]),
    ("fab",  ["f", "a.fap", "b"]),
    ("faf",  ["f", "a.faf", "f"]),
    ("fav",  ["f", "a.faf", "v"]),
    ("fash", ["f", "a.fach", "sh"]),
    ("fach", ["f", "a.fach", "ch"]),
    ("faj",  ["f", "a.fach", "j"]),
    ("fas",  ["f", "a.faf", "s.right"]),
    ("fas(", ["f", "a.fap", "s.left"]),
    ("fang", ["f", "a.fang", "ng"]),
    ("fank", ["f", "a.fang", "nk"]),
    ("fath", ["f", "a.fatn", "th.over.skew45"]),
    ("fath)", ["f", "a.fant", "th.under"]),
])
def test_f_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("vak",  ["v", "a.fak", "k"]),
    ("vag",  ["v", "a.fak", "g"]),
    ("var",  ["v", "a.far", "r"]),
    ("val",  ["v", "a.far", "l"]),
    ("van",  ["v", "a.fan", "n"]),
    ("vam",  ["v", "a.fan", "m"]),
    ("vat",  ["v", "a.fat", "t"]),
    ("vad",  ["v", "a.fat", "d"]),
    ("vap",  ["v", "a.fap", "p"]),
    ("vab",  ["v", "a.fap", "b"]),
    ("vaf",  ["v", "a.faf", "f"]),
    ("vav",  ["v", "a.faf", "v"]),
    ("vash", ["v", "a.fach", "sh"]),
    ("vach", ["v", "a.fach", "ch"]),
    ("vaj",  ["v", "a.fach", "j"]),
    ("vas",  ["v", "a.faf", "s.right"]),
    ("vas(", ["v", "a.fap", "s.left"]),
    ("vang", ["v", "a.fang", "ng"]),
    ("vank", ["v", "a.fang", "nk"]),
    ("vath", ["v", "a.fatn", "th.over.skew45"]),
    ("vath)", ["v", "a.fant", "th.under"]),
])
def test_v_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shak",  ["sh", "a.chak", "k"]),
    ("shag",  ["sh", "a.chak", "g"]),
    ("shar",  ["sh", "a.char", "r"]),
    ("shal",  ["sh", "a.char", "l"]),
    ("shan",  ["sh", "a.chan", "n"]),
    ("sham",  ["sh", "a.chan", "m"]),
    ("shat",  ["sh", "a.chat", "t"]),
    ("shad",  ["sh", "a.chat", "d"]),
    ("shap",  ["sh", "a.chap", "p"]),
    ("shab",  ["sh", "a.chap", "b"]),
    ("shaf",  ["sh", "a.chaf", "f"]),
    ("shav",  ["sh", "a.chaf", "v"]),
    ("shash", ["sh", "a.chach", "sh"]),
    ("shach", ["sh", "a.chach", "ch"]),
    ("shaj",  ["sh", "a.chach", "j"]),
    ("shas",  ["sh", "a.chaf", "s.right"]),
    ("shas(", ["sh", "a.chap", "s.left"]),
    ("shang", ["sh", "a.chang", "ng"]),
    ("shank", ["sh", "a.chang", "nk"]),
])
def test_sh_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("chak",  ["ch", "a.chak", "k"]),
    ("chag",  ["ch", "a.chak", "g"]),
    ("char",  ["ch", "a.char", "r"]),
    ("chal",  ["ch", "a.char", "l"]),
    ("chan",  ["ch", "a.chan", "n"]),
    ("cham",  ["ch", "a.chan", "m"]),
    ("chat",  ["ch", "a.chat", "t"]),
    ("chad",  ["ch", "a.chat", "d"]),
    ("chap",  ["ch", "a.chap", "p"]),
    ("chab",  ["ch", "a.chap", "b"]),
    ("chaf",  ["ch", "a.chaf", "f"]),
    ("chav",  ["ch", "a.chaf", "v"]),
    ("chash", ["ch", "a.chach", "sh"]),
    ("chach", ["ch", "a.chach", "ch"]),
    ("chaj",  ["ch", "a.chach", "j"]),
    ("chas",  ["ch", "a.chaf", "s.right"]),
    ("chas(", ["ch", "a.chap", "s.left"]),
    ("chang", ["ch", "a.chang", "ng"]),
    ("chank", ["ch", "a.chang", "nk"]),
])
def test_ch_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("jak",  ["j", "a.chak", "k"]),
    ("jag",  ["j", "a.chak", "g"]),
    ("jar",  ["j", "a.char", "r"]),
    ("jal",  ["j", "a.char", "l"]),
    ("jan",  ["j", "a.chan", "n"]),
    ("jam",  ["j", "a.chan", "m"]),
    ("jat",  ["j", "a.chat", "t"]),
    ("jad",  ["j", "a.chat", "d"]),
    ("jap",  ["j", "a.chap", "p"]),
    ("jab",  ["j", "a.chap", "b"]),
    ("jaf",  ["j", "a.chaf", "f"]),
    ("jav",  ["j", "a.chaf", "v"]),
    ("jash", ["j", "a.chach", "sh"]),
    ("jach", ["j", "a.chach", "ch"]),
    ("jaj",  ["j", "a.chach", "j"]),
    ("jas",  ["j", "a.chaf", "s.right"]),
    ("jas(", ["j", "a.chap", "s.left"]),
    ("jang", ["j", "a.chang", "ng"]),
    ("jank", ["j", "a.chang", "nk"]),
])
def test_j_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s)ak",  ["s.right", "a.fak", "k"]),
    ("s)ag",  ["s.right", "a.fak", "g"]),
    ("s)ar",  ["s.right", "a.far", "r"]),
    ("s)al",  ["s.right", "a.far", "l"]),
    ("s)an",  ["s.right", "a.fan", "n"]),
    ("s)am",  ["s.right", "a.fan", "m"]),
    ("s)at",  ["s.right", "a.fat", "t"]),
    ("s)ad",  ["s.right", "a.fat", "d"]),
    ("s)ap",  ["s.right", "a.fap", "p"]),
    ("s)ab",  ["s.right", "a.fap", "b"]),
    ("s)af",  ["s.right", "a.faf", "f"]),
    ("s)av",  ["s.right", "a.faf", "v"]),
    ("s)ash", ["s.right", "a.fach", "sh"]),
    ("s)ach", ["s.right", "a.fach", "ch"]),
    ("s)aj",  ["s.right", "a.fach", "j"]),
    ("s)as",  ["s.right", "a.faf", "s.right"]),
    ("s)as(", ["s.right", "a.fap", "s.left"]),
    ("s)ang", ["s.right", "a.fang", "ng"]),
    ("s)ank", ["s.right", "a.fang", "nk"]),
    ("s)ath", ["s.right", "a.fatn", "th.over.skew45"]),
    ("s)ath)", ["s.right", "a.fant", "th.under"]),
])
def test_sR_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("s(ak",  ["s.left.cut", "a.pak", "k"]),
    ("s(ag",  ["s.left.cut", "a.pak", "g"]),
    ("s(ar",  ["s.left.cut", "a.par", "r"]),
    ("s(al",  ["s.left.cut", "a.par", "l"]),
    ("s(an",  ["s.left.cut", "a.pan", "n"]),
    ("s(am",  ["s.left.cut", "a.pan", "m"]),
    ("s(at",  ["s.left", "a.pat", "t"]),
    ("s(ad",  ["s.left", "a.pat", "d"]),
    ("s(ap",  ["s.left", "a.pap", "p"]),
    ("s(ab",  ["s.left", "a.pap", "b"]),
    ("s(af",  ["s.left.cut", "a.paf", "f.cut"]),
    ("s(av",  ["s.left.cut", "a.paf", "v.cut"]),
    ("s(ash", ["s.left", "a.pach", "sh"]),
    ("s(ach", ["s.left", "a.pach", "ch"]),
    ("s(aj",  ["s.left", "a.pach", "j"]),
    ("s(as(",  ["s.left", "a.pap", "s.left"]),
    ("s(as)", ["s.left.cut", "a.paf", "s.right.cut"]),
])
def test_sL_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ngar",  ["ng", "a.ngar", "r.cut"]),
    ("ngal",  ["ng", "a.ngar", "l.cut"]),
    ("ngan",  ["ng", "a.ngan", "n"]),
    ("ngam",  ["ng", "a.ngan", "m"]),
    ("ngat",  ["ng", "a.ngat", "t"]),
    ("ngad",  ["ng", "a.ngat", "d"]),
])
def test_ng_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("nkar",  ["nk", "a.ngar", "r.cut"]),
    ("nkal",  ["nk", "a.ngar", "l.cut"]),
    ("nkan",  ["nk", "a.ngan", "n"]),
    ("nkam",  ["nk", "a.ngan", "m"]),
    ("nkat",  ["nk", "a.ngat", "t"]),
    ("nkad",  ["nk", "a.ngat", "d"]),
])
def test_nk_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th(ak",   ["th.over", "a.tnak", "k"]),
    ("th(ag",   ["th.over", "a.tnak", "g"]),
    ("th(an",   ["th.over", "a.tnan", "n"]),
    ("th(am",   ["th.over", "a.tnan", "m"]),
    ("th(ash",  ["th.over", "a.tnach", "sh"]),
    ("th(ach",  ["th.over", "a.tnach", "ch"]),
    ("th(aj",   ["th.over", "a.tnach", "j"]),
])
def test_thO_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th)af", ["th.under.skew30", "a.ntaf", "f.cut"]),
    ("th)av", ["th.under.skew30", "a.ntaf", "v.cut"]),
])
def test_thU_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("uak",  ["u.cut", "a.uak", "k"]),
    ("uag",  ["u.cut", "a.uak", "g"]),
    ("uar",  ["u.cut", "a.uar", "r.cut"]),
    ("ual",  ["u.cut", "a.uar", "l.cut"]),
    ("uan",  ["u.cut", "a.uan", "n"]),
    ("uam",  ["u.cut", "a.uan", "m"]),
    ("uat",  ["u.cut", "a.uat", "t"]),
    ("uad",  ["u.cut", "a.uat", "d"]),
    ("uap",  ["u.cut", "a.ap", "p"]),
    ("uab",  ["u.cut", "a.ap", "b"]),
    ("uaf",  ["u.cut", "a.uaf", "f.cut"]),
    ("uav",  ["u.cut", "a.uaf", "v.cut"]),
    ("uash", ["u.cut", "a.uach", "sh"]),
    ("uach", ["u.cut", "a.uach", "ch"]),
    ("uaj",  ["u.cut", "a.uach", "j"]),
    ("uas",  ["u.cut", "a.uaf", "s.right.cut"]),
])
def test_u_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
