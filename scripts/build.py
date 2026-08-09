import sys

import fontforge
import psMat

from calculate_line_of_writing_positions import calculate_line_of_writing_positions


STROKE_WIDTH = 24
HALF_STROKE_WIDTH = STROKE_WIDTH // 2

NO_STROKE = {
    "eadot",
    "aspirate",
    "an",
    "ing",
    "inging",
}

font = fontforge.open(sys.argv[1])
calculate_line_of_writing_positions(font)
font.strokedfont = False

for glyph in font.glyphs():
    if glyph.references:
        glyph.unlinkRef()
    glyph.unlinkThisGlyph()

    glyph.background = glyph.foreground

    if glyph.glyphname not in NO_STROKE:
        glyph.stroke("circular", STROKE_WIDTH)
        glyph.transform(psMat.translate(0, HALF_STROKE_WIDTH))

    if glyph.anchorPoints:
        glyph.left_side_bearing = 0
        glyph.right_side_bearing = 0


font.generate(sys.argv[2])
font.save(sys.argv[3])
