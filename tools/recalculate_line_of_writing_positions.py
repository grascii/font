import re
import fontforge


POSITION_BEFORE_REGEX = re.compile(r"Position Before (\w+)")


def recalculate_line_of_writing_positions(data, font):
    for glyph in font.glyphs():
        for pos in glyph.getPosSub("*"):
            subtable, kind, *others = pos

            if kind != "Position":
                continue

            match = POSITION_BEFORE_REGEX.fullmatch(subtable)
            if not match:
                continue

            following_glyph = font[match.group(1)]
            xmin, ymin, xmax, ymax = following_glyph.boundingBox()
            height = ymax - ymin

            for anchor in glyph.anchorPoints:
                if anchor[0] == "Join":
                    if anchor[1] == "exit":
                        exit_y = anchor[3]

            glyph.addPosSub(subtable, 0, round(height - exit_y), 0, 0)


fontforge.registerMenuItem(
    callback=recalculate_line_of_writing_positions,
    context="Font",
    name=("Recalculate Line of Writing Positions", "grascii_recalculate_line_of_writing_positions")
)
