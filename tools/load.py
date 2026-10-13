import site
import sys
from pathlib import Path

ENV_DIR = "REPLACE"
version = sys.version_info
site.addsitedir(
    Path(ENV_DIR).joinpath(
        f"./env/lib/python{version.major}.{version.minor}/site-packages/"
    )
)
site.addsitedir(Path(ENV_DIR).joinpath("tools"))


# ruff: disable[F401]
import create_from_reference
import import_base_model
import no_stroke
import view_reference_tree
# ruff: enable[F401]
