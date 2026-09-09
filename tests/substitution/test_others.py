import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sh", ["sh"]),
    ("ch", ["ch"]),
    ("th", ["th.over"]),
])
def test_multichar_ligatures(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("pr", ["p.cut", "r"]),
    ("pl", ["p.cut", "l"]),
    ("br", ["b.cut", "r"]),
    ("bl", ["b.cut", "l"]),
    ("kf", ["k", "f.cut"]),
    ("kv", ["k", "v.cut"]),
    ("gf", ["g", "f.cut"]),
    ("gv", ["g", "v.cut"]),
    ("fr", ["f", "r.fr"]),
    ("fl", ["f", "l.fl"]),
    ("vr", ["v", "r.fr"]),
    ("vl", ["v", "l.fl"]),
    ("dfr", ["df", "r.fr"]),
    ("dfl", ["df", "l.fl"]),
])
def test_consonant_blends(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("ng", ["ng"]),
    ("nk", ["nk"]),
    ("tn", ["tn"]),
    ("dn", ["tn"]),
    ("tm", ["tm"]),
    ("dm", ["tm"]),
    ("nt", ["nt"]),
    ("nd", ["nt"]),
    ("mt", ["mt"]),
    ("md", ["mt"]),
    ("df", ["df"]),
    ("dv", ["df"]),
    ("tv", ["df"]),
    ("jnt", ["jnt"]),
    ("jnd", ["jnt"]),
    ("pnt", ["jnt"]),
    ("pnd", ["jnt"]),
    ("mn", ["m", "n"]),
    ("mm", ["m", "n"]),
    ("td", ["t", "d"]),
    ("dt", ["t", "d"]),
    ("dd", ["t", "d"]),
    ("ss", ["s.left", "s.right"]),
    ("ld", ["ld.head", "ld.tail"]),
])
def test_blended_consonants(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnt", ["tn", "t"]),
    ("dnd", ["tn", "d"]),
    ("tmd", ["tm", "d"]),
    ("dmt", ["tm", "t"]),
    ("ntn", ["n", "tn"]),
    ("ndm", ["n", "tm"]),
    ("mtm", ["m", "tm"]),
    ("mdn", ["m", "tn"]),
    ("nth", ["n", "th.over"]),
    ("mth", ["m", "th.over"]),
    ("ntd", ["nt", "d"]),
    ("mdt", ["mt", "t"]),
    ("jntd", ["jnt", "d"]),
    ("pndt", ["jnt", "t"]),
    ("jntm", ["jnt", "m"]),
    ("pndn", ["jnt", "n"]),
    ("tnk", ["tn", "k"]),
    ("dng", ["tn", "g"]),
    ("ldn", ["ld.head", "ld.tail", "n"]),
])
def test_blended_consonants_priority(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("t-n", ["t", "boundary", "n"]),
    ("d-m", ["d", "boundary", "m"]),
    ("n-d", ["n", "boundary", "d"]),
    ("m-t", ["m", "boundary", "t"]),
    ("d-f", ["d", "boundary", "f"]),
    ("t-v", ["t", "boundary", "v"]),
    ("j-nt", ["j", "boundary", "nt"]),
    ("pn-t", ["p", "n", "boundary", "t"]),
    ("l-d", ["l", "boundary", "d"]),
])
def test_boundary(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("n-n",  ["n", "jog.n", "n"]),
    ("n-m",  ["n", "jog.n", "m"]),
    ("m-n",  ["m", "jog.n", "n"]),
    ("m-m",  ["m", "jog.n", "m"]),
    ("tn-n", ["tn", "jog.n", "n"]),
    ("tn-m", ["tn", "jog.n", "m"]),
    ("tm-n", ["tm", "jog.n", "n"]),
    ("tm-m", ["tm", "jog.n", "m"]),
    ("n-nt", ["n", "jog.n", "nt"]),
    ("n-mt", ["n", "jog.n", "mt"]),
    ("m-nt", ["m", "jog.n", "nt"]),
    ("m-mt", ["m", "jog.n", "mt"]),
    ("t-t",  ["t", "jog.t", "t"]),
    ("t-d",  ["t", "jog.t", "d"]),
    ("d-t",  ["d", "jog.t", "t"]),
    ("d-d",  ["d", "jog.t", "d"]),
])
def test_jog(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("'a", ["a", "aspirate"]),
    ("'i", ["i", "aspirate"]),
    ("'nd", ["nt", "aspirate"]),
    ("'eu", ["e.eu", "u.eu", "aspirate"]),
    ("'edn", ["e.etn", "aspirate", "tn"]),
    ("en'ospt", ["e.en", "n", "o.op", "aspirate", "s.left", "p", "t"]),
])
def test_aspirate(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("'", ["an"]),
    ("'-g", ["an", "boundary", "g"]),
    ("'-d", ["an", "boundary", "d"]),
    ("''ed", ["an", "e.et", "aspirate", "d"]),
])
def test_an(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("n'", ["n", "ing"]),
    ("sa'", ["s.right", "a.sRa", "ing"]),
    ("ge'", ["g", "e.ke", "ing"]),
    ("sto'", ["s.right", "t", "o", "ing"]),
    ("di'", ["d", "i.ti", "ing"]),
])
def test_ing(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("th''", ["th.over", "ing", "inging"]),
])
def test_inging(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("A", ["a"]),
    ("B", ["b"]),
    ("C", ["c"]),
    ("D", ["d"]),
    ("E", ["e"]),
    ("F", ["f"]),
    ("G", ["g"]),
    ("H", ["h"]),
    ("I", ["i"]),
    ("J", ["j"]),
    ("K", ["k"]),
    ("L", ["l"]),
    ("M", ["m"]),
    ("N", ["n"]),
    ("O", ["o"]),
    ("P", ["p"]),
    ("Q", ["q"]),
    ("R", ["r"]),
    ("S", ["s.right"]),
    ("T", ["t"]),
    ("U", ["u"]),
    ("V", ["v"]),
    ("W", ["w"]),
    ("Y", ["y"]),
])
def test_lowercase(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


def test_grascii(font):
    assert shape("grascii", font) == ["g", "r", "a.rap", "s.left", "k", "e.ke"]


@pytest.mark.parametrize("text,expected_glyphs", [
    ("a_", ["a", "wunderbar"]),
    ("e_", ["e", "wunderbar"]),
    ("o_", ["o", "wunderbar"]),
    ("u_", ["u", "wunderbar"]),
    ("i_", ["i", "wunderbar"]),
    ("a&e_", ["ae", "wunderbar"]),
    ("oe_", ["o.oe", "e.oe", "wunderbar"]),
    ("eu_", ["e.eu", "u.eu", "wunderbar"]),
    ("'a_", ["a", "aspirate", "wunderbar"]),
    ("ba_r", ["b.cut", "a.par", "wunderbar", "r"]),
    ("na_", ["n", "a.na", "wunderbar"]),
])
def test_wunderbar(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("z", ["s.right"]),
    ("x", ["s.right"]),
    ("Z", ["s.right"]),
    ("X", ["s.right"]),
])
def test_aliases(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
