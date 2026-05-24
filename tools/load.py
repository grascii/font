import sys
from pathlib import Path
import site

ENV_DIR = "REPLACE"
version = sys.version_info
site.addsitedir(Path(ENV_DIR).joinpath(
    f"./env/lib/python{version.major}.{version.minor}/site-packages/"
))
site.addsitedir(Path(ENV_DIR).joinpath("tools"))


import import_base_model
import create_from_reference
import recalculate_line_of_writing_positions
import view_reference_tree
