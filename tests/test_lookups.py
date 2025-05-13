from pathlib import Path

import fontforge
import pytest
import uharfbuzz as hb


@pytest.fixture(scope="module")
def font(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("font") / "Grascii.otf"
    sdfir_path = Path(__file__).joinpath("../../Grascii.sfdir").resolve()
    font = fontforge.open(str(sdfir_path))
    font.generate(str(tmp_path))
    blob = hb.Blob.from_file_path(tmp_path)
    face = hb.Face(blob)
    return hb.Font(face)


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]


@pytest.mark.parametrize("text,expected_glyphs", [
    ("sh", ["sh"]),
    ("ch", ["ch"]),
    ("th", ["th"]),
    ("ng", ["ng"]),
    ("nk", ["nk"]),
])
def test_multichar_ligatures(font, text, expected_glyphs):
    assert shape(text, font) == expected_glyphs
