import os
import re
import tempfile
import fontforge
import uharfbuzz as hb
from itertools import chain, product


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    glyphs = [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]
    assert glyphs[0] == "_start" and glyphs[-1] == "_end"
    return glyphs[1:-1]


VOWELS = [
    "a",
    "e",
    "o",
    "u",
    "i",
    # covered by a
    # "a&'",
    "a&e",
    "oe",
    "au",
    "eu",
]

DOWNWARD_CONSONANTS = [
    "pr",
    "pl",
    "br",
    "bl",
    # "fr",
    # "fl",
    # "vr",
    # "vl",
    "p",
    "b",
    "f",
    "v",
    "sh",
    "ch",
    "j",
    "ng",
    "nk",
    "s)",
    "s(",
    "jnt",
]

CONSONANTS = [
    "k",
    "g",
    "r",
    "l",
    "n",
    "m",
    "t",
    "d",
    "th(",
    "th)",
    "tn",
    "tm",
    "nt",
    "md",
    "df",
]

S = ["s)", "s("]

TAIL_VARIANTS = {
    "k": ["k", "k.cut"],
    "g": ["g", "g.cut"],
    "p": ["p", "p.cut"],
    "b": ["b", "b.cut"],
    "s.left": ["s.left", "s.left.cut"],
    "th.under": ["th.under", "th.under.angled", "th.under.skew30", "th.under.skew45"],
    "nt": ["nt", "nt.angled", "nt.skew30", "nt.skew45"],
    "mt": ["mt", "mt.angled", "mt.skew30", "mt.skew45"],
    "jnt": ["jnt", "jnt.angled", "jnt.skew30", "jnt.skew45"],
    "u.fu": ["u.fu", "u.cut"],
    "u": ["u", "u.cut"],
}

LOOKUP = "Line of Writing"


def calculate_line_of_writing_positions(font: fontforge.font):
    _, tmp_path = tempfile.mkstemp(".otf")
    font.generate(tmp_path)
    blob = hb.Blob.from_file_path(tmp_path)
    face = hb.Face(blob)
    hb_font = hb.Font(face)

    os.remove(tmp_path)

    rules = {}
    texts = map(
        lambda t: "".join(t),
        chain(
            # put more specific rules first so they take precedence
            product(VOWELS, S, VOWELS, DOWNWARD_CONSONANTS),
            product(S, VOWELS, DOWNWARD_CONSONANTS),
            product(VOWELS, S, DOWNWARD_CONSONANTS),
            product(S, DOWNWARD_CONSONANTS),
            product(VOWELS, S, VOWELS),
            product(S, ["U"], ["A", "E", "I"], DOWNWARD_CONSONANTS),
            product(S, VOWELS),
            product(VOWELS, DOWNWARD_CONSONANTS),
            product(VOWELS, CONSONANTS),
            CONSONANTS,
            DOWNWARD_CONSONANTS,
            product(["U"], ["A", "E", "I"], DOWNWARD_CONSONANTS),
            product(["U"], ["A", "E", "I"]),
            VOWELS,
        ),
    )

    for text in texts:
        shaped = shape(text, hb_font)

        variants = TAIL_VARIANTS.get(shaped[-1], [shaped[-1]])
        glyphs_list = [shaped[:-1] + [variant] for variant in variants]

        for glyphs in glyphs_list:
            key = " ".join(glyphs)
            if key in rules:
                continue

            x_adjustment, y_adjustment = 0, 0
            exit_x, exit_y = 0, 0
            xmin, ymin = 0, 0
            for glyph_name in glyphs:
                glyph = font[glyph_name]
                for anchor in glyph.anchorPoints:
                    if anchor[0] == "Join":
                        if anchor[1] == "entry":
                            entry_x = anchor[2]
                            entry_y = anchor[3]

                xmin, ymin, xmax, ymax = glyph.boundingBox()
                x_adjustment += max(0, round(entry_x - xmin - exit_x))
                y_adjustment += max(
                    0, round(entry_y - ymin - exit_y - font.strokewidth)
                )

                for anchor in glyph.anchorPoints:
                    if anchor[0] == "Join":
                        if anchor[1] == "exit":
                            exit_x = anchor[2]
                            exit_y = anchor[3]

            x_adjustment -= font.strokewidth
            assert x_adjustment >= 0 and y_adjustment >= 0
            if x_adjustment == 0 and y_adjustment == 0:
                continue

            x_adjustments = decomose_adjustments(x_adjustment)
            y_adjustments = decomose_adjustments(y_adjustment)

            lookups = []
            for adjustment in x_adjustments:
                lookups.append(f"@<Right {adjustment}>")
            for adjustment in y_adjustments:
                lookups.append(f"@<Up {adjustment}>")

            rules[key] = f"| _start {' '.join(lookups)} | {key}"

    subtables = font.getLookupSubtables(LOOKUP)
    for subtable in subtables:
        font.removeLookupSubtable(subtable)

    # limit the number of rules per subtable to keep them under 64 KB
    RULES_PER_SUBTABLE = 1024
    rules_list = list(rules.values())
    last_subtable = None
    for i in range(0, len(rules_list), RULES_PER_SUBTABLE):
        subtable = f"{LOOKUP} {i}"
        if i > 0:
            font.addContextualSubtable(
                LOOKUP,
                subtable,
                "glyph",
                rules_list[i : i + RULES_PER_SUBTABLE],
                afterSubtable=last_subtable,
            )
        else:
            font.addContextualSubtable(
                LOOKUP, subtable, "glyph", rules_list[i : i + RULES_PER_SUBTABLE]
            )
        last_subtable = subtable

    font["_start"].addPosSub(
        "Stroke Adjustment", -int(font.strokewidth), -int(font.strokewidth), 0, 0
    )

    print("Created", len(rules), "rules")


def decomose_adjustments(value):
    BASE = 6
    DIGITS = 4
    increment = BASE ** (DIGITS - 1)
    adjustments = []

    while increment >= 1:
        count, value = divmod(value, increment)
        adjustment = int(count * increment)
        if adjustment > 0:
            adjustments.append(adjustment)
        increment /= BASE

    return adjustments


if __name__ == "__main__":
    font = fontforge.open(sys.argv[1])
    calculate_line_of_writing_positions(font)
    font.save(sys.argv[1])
