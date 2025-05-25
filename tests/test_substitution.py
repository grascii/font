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
    ("kaf", ["k", "a.kaf", "f"]),
    ("kav", ["k", "a.kaf", "v"]),
    ("kash", ["k", "a.kach", "sh"]),
    ("kach", ["k", "a.kach", "ch"]),
    ("kaj", ["k", "a.kach", "j"]),
    ("kang", ["k", "a.kang", "ng"]),
    ("kank", ["k", "a.kang", "nk"]),
    ("kath", ["k", "a.katn", "th.over"]),
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
    ("gaf", ["g", "a.kaf", "f"]),
    ("gav", ["g", "a.kaf", "v"]),
    ("gash", ["g", "a.kach", "sh"]),
    ("gach", ["g", "a.kach", "ch"]),
    ("gaj", ["g", "a.kach", "j"]),
    ("gang", ["g", "a.kang", "ng"]),
    ("gank", ["g", "a.kang", "nk"]),
    ("gath", ["g", "a.katn", "th.over"]),
])
def test_g_a(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
