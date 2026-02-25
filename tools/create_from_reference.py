import math
from functools import reduce
from typing import TypedDict

import fontforge
import psMat


def compose(*mats: tuple[float, float, float, float, float, float]):
    return reduce(psMat.compose, mats, psMat.identity())


flip_vertical = psMat.scale(1, -1)
flip_horizontal = psMat.scale(-1, 1)

class Transformation(TypedDict):
    matrix: tuple[float, float, float, float, float, float]
    reverse: bool

transformations: dict[str, Transformation] = {
    "Identity": {
        "matrix": psMat.identity(),
        "reverse": False,
    },
    "R to F": {
        "matrix": compose(flip_horizontal, psMat.rotate(math.radians(60))),
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
        "matrix": psMat.rotate(math.radians(30)),
        "reverse": False,
    },
    "N to NG": {
        "matrix": psMat.rotate(math.radians(-15)),
        "reverse": False,
    },
    "N to CH": {
        "matrix": psMat.rotate(math.radians(-120)),
        "reverse": False,
    },
    "Skew 30": {
        "matrix": psMat.skew(math.radians(30)),
        "reverse": False,
    },
    "Skew 45": {
        "matrix": psMat.skew(math.radians(45)),
        "reverse": False,
    },
    "Skew 30 Rotate 30": {
        "matrix": compose(
             psMat.skew(math.radians(30)),
             psMat.rotate(math.radians(-30))
        ),
        "reverse": False,
    },
    "Skew 30 Rotate 40": {
        "matrix": compose(
             psMat.skew(math.radians(30)),
             psMat.rotate(math.radians(-40))
        ),
        "reverse": False,
    },
    "Rotate 90": {
        "matrix": psMat.rotate(math.radians(-90)),
        "reverse": False,
    },
    "TH to TN": {
        "matrix": psMat.scale(2.25),
        "reverse": False,
    },
    "TH to TM": {
        "matrix": psMat.scale(4),
        "reverse": False,
    },
}


def create_from_reference(data: None, glyph: fontforge.glyph):
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
                "answers": list({"name": t, "default": t == "Identity"} for t in transformations.keys())
            },
            {
                "type": "choice",
                "question": "transformation2",
                "answers": list({"name": t, "default": t == "Identity"} for t in transformations.keys())
            },
        ]
    )

    if not answers:
        return

    reference_glyph = glyph.font[answers["glyph"]]

    entry_anchor = None
    exit_anchor = None
    for anchor in reference_glyph.anchorPoints:
        if anchor[0] == "Join":
            if anchor[1] == "entry":
                entry_anchor = (anchor[2], anchor[3])
            else:
                exit_anchor = (anchor[2], anchor[3])

    transformation = transformations[answers["transformation"]]
    transformation2 = transformations[answers["transformation2"]]

    if transformation["reverse"]:
        entry_anchor, exit_anchor = exit_anchor, entry_anchor

    if transformation2["reverse"]:
        entry_anchor, exit_anchor = exit_anchor, entry_anchor

    if entry_anchor:
        glyph.addAnchorPoint("Join", "entry", entry_anchor[0], entry_anchor[1])
    if exit_anchor:
        glyph.addAnchorPoint("Join", "exit", exit_anchor[0], exit_anchor[1])

    glyph.addReference(reference_glyph.glyphname)

    glyph.transform(compose(transformation["matrix"], transformation2["matrix"]))
    glyph.left_side_bearing = 0
    glyph.right_side_bearing = 0

    (xmin, ymin, xmax, ymax) = glyph.boundingBox()
    if ymin < 0:
        glyph.transform(psMat.translate(0, -ymin - glyph.font.strokewidth))


fontforge.registerMenuItem(
    callback=create_from_reference,
    context="Glyph",
    name=("Create from Reference", "grascii_create_from_reference")
)
