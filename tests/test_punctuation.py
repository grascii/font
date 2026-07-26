import pytest
import fontforge

@pytest.mark.parametrize("glyph_name", [
    "period",
    "question",
    "greater",
])
def test_no_join(ffont: fontforge.font, glyph_name: str):
    assert ffont[glyph_name].left_side_bearing > 50
