import sys

import fontforge
import psMat


STROKE_WIDTH = 24
HALF_STROKE_WIDTH = STROKE_WIDTH // 2

font = fontforge.open(sys.argv[1])
font.strokedfont = False

for glyph in font.glyphs():
    if glyph.references:
        glyph.unlinkRef()
    else:
        glyph.unlinkThisGlyph()

    glyph.background = glyph.foreground

    glyph.stroke("circular", STROKE_WIDTH)
    glyph.transform(psMat.translate(0, HALF_STROKE_WIDTH))

    if glyph.glyphname != "space":
        glyph.left_side_bearing = 0
        glyph.right_side_bearing = 0


font.generate(sys.argv[2])
font.save(sys.argv[3])
