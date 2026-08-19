import pytest
from shape import shape


@pytest.mark.parametrize("text,expected_glyphs", [
    ("oe", ["o.oe", "e.oe"]),
])
def test_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("oer",   ["o.oe", "e.oer", "r.cut"]),
    ("oel",   ["o.oe", "e.oer", "l.cut"]),
    ("oen",   ["o.oe", "e.oen", "n"]),
    ("oem",   ["o.oe", "e.oen", "m"]),
    ("oep",   ["o.oep", "e.oep", "p"]),
    ("oeb",   ["o.oep", "e.oep", "b"]),
    ("oef",   ["o.oe", "e.oef", "f.cut"]),
    ("oev",   ["o.oe", "e.oef", "v.cut"]),
    ("oes)",  ["o.oe", "e.oef", "s.right.cut"]),
    ("oes",   ["o.oep", "e.oep", "s.left"]),
    ("oent",  ["o.oe", "e.oen", "nt"]),
    ("oend",  ["o.oe", "e.oen", "nt"]),
    ("oemt",  ["o.oe", "e.oen", "mt"]),
    ("oemd",  ["o.oe", "e.oen", "mt"]),
])
def test_oe_before(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("koe",  ["k.cut", "o.koe", "e.oe"]),
    ("goe",  ["g.cut", "o.koe", "e.oe"]),
    ("roe",  ["r", "o.oe", "e.oe"]),
    ("loe",  ["l", "o.oe", "e.oe"]),
    ("noe",  ["n", "o.oe", "e.oe"]),
    ("moe",  ["m", "o.oe", "e.oe"]),
    ("toe",  ["t", "o.oe", "e.oe"]),
    ("doe",  ["d", "o.oe", "e.oe"]),
    ("poe",  ["p", "o.poe", "e.poe"]),
    ("boe",  ["b", "o.poe", "e.poe"]),
    ("foe",  ["f", "o.foe", "e.oe"]),
    ("voe",  ["v", "o.foe", "e.oe"]),
    ("soe",  ["s.right", "o.foe", "e.oe"]),
    ("s(oe", ["s.left", "o.sLoe", "e.sLoe"]),
    ("shoe", ["sh", "o.choe", "e.choe"]),
    ("choe", ["ch", "o.choe", "e.choe"]),
    ("joe",  ["j", "o.choe", "e.choe"]),
    ("thoe", ["th.over", "o.oe", "e.oe"]),
    ("tnoe", ["tn", "o.oe", "e.oe"]),
    ("dnoe", ["tn", "o.oe", "e.oe"]),
    ("tmoe", ["tm", "o.oe", "e.oe"]),
    ("dmoe", ["tm", "o.oe", "e.oe"]),
    ("dfoe", ["df", "o.foe", "e.oe"]),
])
def test_oe_after(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("koer",  ["k.cut", "o.koer", "e.koer", "r.cut"]),
    ("koel",  ["k.cut", "o.koer", "e.koer", "l.cut"]),
    ("koen",  ["k.cut", "o.koen", "e.koen", "n"]),
    ("koem",  ["k.cut", "o.koen", "e.koen", "m"]),
    ("koet",  ["k.cut", "o.koet", "e.koet", "t"]),
    ("koed",  ["k.cut", "o.koet", "e.koet", "d"]),
    ("koeld", ["k.cut", "o.koer", "e.koer", "ld.head.cut", "ld.tail"]),
])
def test_k_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("goer",  ["g.cut", "o.koer", "e.koer", "r.cut"]),
    ("goel",  ["g.cut", "o.koer", "e.koer", "l.cut"]),
    ("goen",  ["g.cut", "o.koen", "e.koen", "n"]),
    ("goem",  ["g.cut", "o.koen", "e.koen", "m"]),
    ("goet",  ["g.cut", "o.koet", "e.koet", "t"]),
    ("goed",  ["g.cut", "o.koet", "e.koet", "d"]),
    ("goeld", ["g.cut", "o.koer", "e.koer", "ld.head.cut", "ld.tail"]),
])
def test_g_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("roer",  ["r", "o.oe", "e.oer", "r.cut"]),
    ("roel",  ["r", "o.oe", "e.oer", "l.cut"]),
    ("roen",  ["r", "o.oe", "e.oen", "n"]),
    ("roem",  ["r", "o.oe", "e.oen", "m"]),
    ("roet",  ["r", "o.roet", "e.roet", "t"]),
    ("roed",  ["r", "o.roet", "e.roet", "d"]),
    ("roep",  ["r", "o.oep", "e.oep", "p"]),
    ("roeb",  ["r", "o.oep", "e.oep", "b"]),
    ("roes",  ["r", "o.oep", "e.oep", "s.left"]),
    ("roent", ["r", "o.oe", "e.oen", "nt"]),
    ("roend", ["r", "o.oe", "e.oen", "nt"]),
    ("roemt", ["r", "o.oe", "e.oen", "mt"]),
    ("roemd", ["r", "o.oe", "e.oen", "mt"]),
])
def test_r_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("loer",  ["l", "o.oe", "e.oer", "r.cut"]),
    ("loel",  ["l", "o.oe", "e.oer", "l.cut"]),
    ("loen",  ["l", "o.oe", "e.oen", "n"]),
    ("loem",  ["l", "o.oe", "e.oen", "m"]),
    ("loet",  ["l", "o.roet", "e.roet", "t"]),
    ("loed",  ["l", "o.roet", "e.roet", "d"]),
    ("loep",  ["l", "o.oep", "e.oep", "p"]),
    ("loeb",  ["l", "o.oep", "e.oep", "b"]),
    ("loes",  ["l", "o.oep", "e.oep", "s.left"]),
    ("loent", ["l", "o.oe", "e.oen", "nt"]),
    ("loend", ["l", "o.oe", "e.oen", "nt"]),
    ("loemt", ["l", "o.oe", "e.oen", "mt"]),
    ("loemd", ["l", "o.oe", "e.oen", "mt"]),
])
def test_l_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("noen",  ["n", "o.oe", "e.oen", "n"]),
    ("noem",  ["n", "o.oe", "e.oen", "m"]),
    ("noet",  ["n", "o.roet", "e.roet", "t"]),
    ("noed",  ["n", "o.roet", "e.roet", "d"]),
    ("noep",  ["n", "o.noep", "e.noep", "p"]),
    ("noeb",  ["n", "o.noep", "e.noep", "b"]),
    ("noes",  ["n", "o.noep", "e.noep", "s.left"]),
    ("noent", ["n", "o.oe", "e.oen", "nt"]),
    ("noend", ["n", "o.oe", "e.oen", "nt"]),
    ("noemt", ["n", "o.oe", "e.oen", "mt"]),
    ("noemd", ["n", "o.oe", "e.oen", "mt"]),
])
def test_n_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("moen",  ["m", "o.oe", "e.oen", "n"]),
    ("moem",  ["m", "o.oe", "e.oen", "m"]),
    ("moet",  ["m", "o.roet", "e.roet", "t"]),
    ("moed",  ["m", "o.roet", "e.roet", "d"]),
    ("moep",  ["m", "o.noep", "e.noep", "p"]),
    ("moeb",  ["m", "o.noep", "e.noep", "b"]),
    ("moes",  ["m", "o.noep", "e.noep", "s.left"]),
    ("moent", ["m", "o.oe", "e.oen", "nt"]),
    ("moend", ["m", "o.oe", "e.oen", "nt"]),
    ("moemt", ["m", "o.oe", "e.oen", "mt"]),
    ("moemd", ["m", "o.oe", "e.oen", "mt"]),
])
def test_m_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("toer",  ["t", "o.oe", "e.oer", "r.cut"]),
    ("toel",  ["t", "o.oe", "e.oer", "l.cut"]),
    ("toef",  ["t", "o.oe", "e.oef", "f.cut"]),
    ("toev",  ["t", "o.oe", "e.oef", "v.cut"]),
    ("toes)", ["t", "o.oe", "e.oef", "s.right.cut"]),
])
def test_t_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("doer",  ["d", "o.oe", "e.oer", "r.cut"]),
    ("doel",  ["d", "o.oe", "e.oer", "l.cut"]),
    ("doef",  ["d", "o.oe", "e.oef", "f.cut"]),
    ("doev",  ["d", "o.oe", "e.oef", "v.cut"]),
    ("does)", ["d", "o.oe", "e.oef", "s.right.cut"]),
])
def test_d_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("poer",  ["p", "o.poer", "e.poer", "r.cut"]),
    ("poel",  ["p", "o.poer", "e.poer", "l.cut"]),
    ("poen",  ["p", "o.poen", "e.poen", "n"]),
    ("poem",  ["p", "o.poen", "e.poen", "m"]),
    ("poep",  ["p", "o.poep", "e.poep", "p"]),
    ("poeb",  ["p", "o.poep", "e.poep", "b"]),
    ("poef",  ["p", "o.poef", "e.poef", "f.cut"]),
    ("poev",  ["p", "o.poef", "e.poef", "v.cut"]),
    ("poes",  ["p", "o.poep", "e.poep", "s.left"]),
    ("poes)", ["p", "o.poef", "e.poef", "s.right.cut"]),
    ("poent", ["p", "o.poen", "e.poen", "nt"]),
    ("poend", ["p", "o.poen", "e.poen", "nt"]),
    ("poemt", ["p", "o.poen", "e.poen", "mt"]),
    ("poemd", ["p", "o.poen", "e.poen", "mt"]),
    ("poeld", ["p", "o.poer", "e.poer", "ld.head.cut", "ld.tail"]),
])
def test_p_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("boer",  ["b", "o.poer", "e.poer", "r.cut"]),
    ("boel",  ["b", "o.poer", "e.poer", "l.cut"]),
    ("boen",  ["b", "o.poen", "e.poen", "n"]),
    ("boem",  ["b", "o.poen", "e.poen", "m"]),
    ("boep",  ["b", "o.poep", "e.poep", "p"]),
    ("boeb",  ["b", "o.poep", "e.poep", "b"]),
    ("boef",  ["b", "o.poef", "e.poef", "f.cut"]),
    ("boev",  ["b", "o.poef", "e.poef", "v.cut"]),
    ("boes",  ["b", "o.poep", "e.poep", "s.left"]),
    ("boes)", ["b", "o.poef", "e.poef", "s.right.cut"]),
    ("boent", ["b", "o.poen", "e.poen", "nt"]),
    ("boend", ["b", "o.poen", "e.poen", "nt"]),
    ("boemt", ["b", "o.poen", "e.poen", "mt"]),
    ("boemd", ["b", "o.poen", "e.poen", "mt"]),
    ("boeld", ["b", "o.poer", "e.poer", "ld.head.cut", "ld.tail"]),
])
def test_b_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("foer",  ["f", "o.foe", "e.oer", "r.cut"]),
    ("foel",  ["f", "o.foe", "e.oer", "l.cut"]),
    ("foen",  ["f", "o.foe", "e.oen", "n"]),
    ("foem",  ["f", "o.foe", "e.oen", "m"]),
    ("foet",  ["f", "o.foet", "e.foet", "t"]),
    ("foed",  ["f", "o.foet", "e.foet", "d"]),
    ("foep",  ["f", "o.foep", "e.foep", "p"]),
    ("foeb",  ["f", "o.foep", "e.foep", "b"]),
    ("foes",  ["f", "o.foep", "e.foep", "s.left"]),
    ("foesh", ["f", "o.foech", "e.foech", "sh"]),
    ("foech", ["f", "o.foech", "e.foech", "ch"]),
    ("foej",  ["f", "o.foech", "e.foech", "j"]),
])
def test_f_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("voer",  ["v", "o.foe", "e.oer", "r.cut"]),
    ("voel",  ["v", "o.foe", "e.oer", "l.cut"]),
    ("voen",  ["v", "o.foe", "e.oen", "n"]),
    ("voem",  ["v", "o.foe", "e.oen", "m"]),
    ("voet",  ["v", "o.foet", "e.foet", "t"]),
    ("voed",  ["v", "o.foet", "e.foet", "d"]),
    ("voep",  ["v", "o.foep", "e.foep", "p"]),
    ("voeb",  ["v", "o.foep", "e.foep", "b"]),
    ("voes",  ["v", "o.foep", "e.foep", "s.left"]),
    ("voesh", ["v", "o.foech", "e.foech", "sh"]),
    ("voech", ["v", "o.foech", "e.foech", "ch"]),
    ("voej",  ["v", "o.foech", "e.foech", "j"]),
])
def test_v_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("soer",  ["s.right", "o.foe", "e.oer", "r.cut"]),
    ("soel",  ["s.right", "o.foe", "e.oer", "l.cut"]),
    ("soeld", ["s.right", "o.foe", "e.oer", "ld.head.cut", "ld.tail"]),
])
def test_sR_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("shoer",  ["sh", "o.choer", "e.choer", "r.cut"]),
    ("shoel",  ["sh", "o.choer", "e.choer", "l.cut"]),
    ("shoen",  ["sh", "o.choen", "e.choen", "n"]),
    ("shoem",  ["sh", "o.choen", "e.choen", "m"]),
    ("shoep",  ["sh", "o.choep", "e.choep", "p"]),
    ("shoeb",  ["sh", "o.choep", "e.choep", "b"]),
    ("shoef",  ["sh", "o.choef", "e.choef", "f.cut"]),
    ("shoev",  ["sh", "o.choef", "e.choef", "v.cut"]),
    ("shoes",  ["sh", "o.choep", "e.choep", "s.left"]),
    ("shoes)", ["sh", "o.choef", "e.choef", "s.right.cut"]),
    ("shoent", ["sh", "o.choen", "e.choen", "nt"]),
    ("shoend", ["sh", "o.choen", "e.choen", "nt"]),
    ("shoemt", ["sh", "o.choen", "e.choen", "mt"]),
    ("shoemd", ["sh", "o.choen", "e.choen", "mt"]),
])
def test_sh_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("choer",  ["ch", "o.choer", "e.choer", "r.cut"]),
    ("choel",  ["ch", "o.choer", "e.choer", "l.cut"]),
    ("choen",  ["ch", "o.choen", "e.choen", "n"]),
    ("choem",  ["ch", "o.choen", "e.choen", "m"]),
    ("choep",  ["ch", "o.choep", "e.choep", "p"]),
    ("choeb",  ["ch", "o.choep", "e.choep", "b"]),
    ("choef",  ["ch", "o.choef", "e.choef", "f.cut"]),
    ("choev",  ["ch", "o.choef", "e.choef", "v.cut"]),
    ("choes",  ["ch", "o.choep", "e.choep", "s.left"]),
    ("choes)", ["ch", "o.choef", "e.choef", "s.right.cut"]),
    ("choent", ["ch", "o.choen", "e.choen", "nt"]),
    ("choend", ["ch", "o.choen", "e.choen", "nt"]),
    ("choemt", ["ch", "o.choen", "e.choen", "mt"]),
    ("choemd", ["ch", "o.choen", "e.choen", "mt"]),
])
def test_ch_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("joer",  ["j", "o.choer", "e.choer", "r.cut"]),
    ("joel",  ["j", "o.choer", "e.choer", "l.cut"]),
    ("joen",  ["j", "o.choen", "e.choen", "n"]),
    ("joem",  ["j", "o.choen", "e.choen", "m"]),
    ("joep",  ["j", "o.choep", "e.choep", "p"]),
    ("joeb",  ["j", "o.choep", "e.choep", "b"]),
    ("joef",  ["j", "o.choef", "e.choef", "f.cut"]),
    ("joev",  ["j", "o.choef", "e.choef", "v.cut"]),
    ("joes",  ["j", "o.choep", "e.choep", "s.left"]),
    ("joes)", ["j", "o.choef", "e.choef", "s.right.cut"]),
    ("joent", ["j", "o.choen", "e.choen", "nt"]),
    ("joend", ["j", "o.choen", "e.choen", "nt"]),
    ("joemt", ["j", "o.choen", "e.choen", "mt"]),
    ("joemd", ["j", "o.choen", "e.choen", "mt"]),
])
def test_j_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tnoen", ["tn", "o.oe", "e.oen", "n"]),
    ("tnoem", ["tn", "o.oe", "e.oen", "m"]),
])
def test_tn_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs


@pytest.mark.parametrize("text,expected_glyphs", [
    ("tmoen", ["tm", "o.oe", "e.oen", "n"]),
    ("tmoem", ["tm", "o.oe", "e.oen", "m"]),
])
def test_tm_oe(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
