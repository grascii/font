import sys

import fontforge
import psMat

font = fontforge.open(sys.argv[1])
font.strokedfont = False

for glyph in font.glyphs():
    if glyph.references:
        glyph.unlinkRef()
    else:
        glyph.unlinkThisGlyph()

    glyph.background = glyph.foreground

    glyph.stroke("circular", 24)
    glyph.transform(psMat.translate(0, 12))

    if glyph.glyphname != "space":
        glyph.left_side_bearing = 0
        glyph.right_side_bearing = 0

font.generate(sys.argv[2])
font.save(sys.argv[3])
