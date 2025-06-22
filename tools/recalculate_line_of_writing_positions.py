import re
import fontforge


POSITION_BEFORE_REGEX = re.compile(r"Position Before ([.\w]+)")


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
                        exit_x = anchor[2]
                        exit_y = anchor[3]

            for anchor in following_glyph.anchorPoints:
                if anchor[0] == "Join":
                    if anchor[1] == "entry":
                        entry_x = anchor[2]

            left = glyph.boundingBox()[0]

            dx = max(0, round(entry_x - xmin - (exit_x - left)))
            dy = round(height - exit_y)
            glyph.addPosSub(subtable, dx, dy, 0, 0)


fontforge.registerMenuItem(
    callback=recalculate_line_of_writing_positions,
    context="Font",
    name=("Recalculate Line of Writing Positions", "grascii_recalculate_line_of_writing_positions")
)
