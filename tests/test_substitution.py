import pytest
import uharfbuzz as hb


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sh", ["sh"]),
    ("ch", ["ch"]),
    ("th", ["th.over"]),
    ("ng", ["ng"]),
    ("nk", ["nk"]),
])
def test_multichar_ligatures(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pr", ["p.cut", "r"]),
    ("pl", ["p.cut", "l"]),
    ("br", ["b.cut", "r"]),
    ("bl", ["b.cut", "l"]),
])
def test_consonant_blends(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


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
