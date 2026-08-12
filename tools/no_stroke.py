import fontforge


def add_no_stroke(data: None, font: fontforge.font):
    for glyph in font.selection.byGlyphs:
        glyph.persistent = {
            "no_stroke": True,
        }


def remove_no_stroke(data: None, font: fontforge.font):
    for glyph in font.selection.byGlyphs:
        glyph.persistent = None


fontforge.registerMenuItem(
    callback=add_no_stroke,
    context="Font",
    name=("Disable Stroke", "grascii_disable_stroke")
)


fontforge.registerMenuItem(
    callback=remove_no_stroke,
    context="Font",
    name=("Enable Stroke", "grascii_enable_stroke")
)
