import math
from functools import reduce

import fontforge
import psMat


def compose(*mats):
    return reduce(psMat.compose, mats, psMat.identity())


flip_vertical = psMat.scale(1, -1)
flip_horizontal = psMat.scale(-1, 1)


transformations = {
    "Identity": {
        "matrix": psMat.identity(),
        "reverse": False,
    },
    "R to K": {
        "matrix": psMat.rotate(math.radians(180)),
        "reverse": True,
    },
    "R to P": {
        "matrix": compose(flip_vertical, psMat.rotate(math.radians(60))),
        "reverse": True,
    },
    "N to T": {
        "matrix": psMat.rotate(math.radians(-30)),
        "reverse": False,
    },
}


def create_from_reference(data, glyph):
    answers = fontforge.askMulti(
        "Select glyph and transformation",
        [
            {
                "type": "string",
                "question": "glyph",
                "default": "",
            },
            {
                "type": "choice",
                "question": "transformation",
                "answers": list({"name": t} for t in transformations.keys())
            },
        ]
    )

    print(answers)


fontforge.registerMenuItem(
    callback=create_from_reference,
    context="Glyph",
    name=("Create from Reference", "grascii_create_from_reference")
)
