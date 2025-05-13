import sys
from pathlib import Path
import site


version = sys.version_info
site.addsitedir(Path(__file__).joinpath(
    f"../../env/lib/python{version.major}.{version.minor}/site-packages/"
))


import pytest

pytest.main([Path(__file__).parent])
