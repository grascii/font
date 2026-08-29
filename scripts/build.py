import math
import sys

from pathlib import Path

import fontforge
import psMat

from calculate_line_of_writing_positions import calculate_line_of_writing_positions


STROKE_WIDTH = 24
HALF_STROKE_WIDTH = STROKE_WIDTH // 2

no_stroke = []

font = fontforge.open(sys.argv[1])
calculate_line_of_writing_positions(font)
font.strokedfont = False

for glyph in font.glyphs():
    if glyph.references:
        glyph.unlinkRef()
    glyph.unlinkThisGlyph()

    glyph.background = glyph.foreground

    if glyph.persistent is not None and glyph.persistent["no_stroke"]:
        no_stroke.append(glyph.glyphname)
    else:
        # With a circular nib, the angle does not matter in theory,
        # but it makes a difference in practice
        glyph.stroke("circular", STROKE_WIDTH, angle=math.pi/4)
        glyph.transform(psMat.translate(0, HALF_STROKE_WIDTH))


    if glyph.anchorPoints:
        glyph.left_side_bearing = 0
        glyph.right_side_bearing = 0


print("Did not stroke", no_stroke)

font_dir = Path(sys.argv[1]).parent
license = font_dir.joinpath("OFL.txt").read_text()
copyright = license[0:license.find("\n")]
font.copyright = copyright
sfnt_names = list(font.sfnt_names)
sfnt_names.append(("English (US)", "License", license))
font.sfnt_names = tuple(sfnt_names)
font.fontlog = font_dir.joinpath("FONTLOG.txt").read_text()

font.generate(sys.argv[2])
font.save(sys.argv[3])
