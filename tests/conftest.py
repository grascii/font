from pathlib import Path

import fontforge
import pytest
import uharfbuzz as hb


@pytest.fixture(scope="session")
def font(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("font") / "Grascii.otf"
    sdfir_path = Path(__file__).joinpath("../../Grascii.sfdir").resolve()
    font = fontforge.open(str(sdfir_path))
    font.generate(str(tmp_path))
    blob = hb.Blob.from_file_path(tmp_path)
    face = hb.Face(blob)
    return hb.Font(face)
