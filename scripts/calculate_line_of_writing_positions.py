import os
import sys
import tempfile
from itertools import product

import fontforge
import uharfbuzz as hb


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
    "l": ["l", "ld.head"],
}

LOOKUP = "Line of Writing"
SUBTABLE_PREFIX = "LoW"


def calculate_line_of_writing_positions(font: fontforge.font):
    _, tmp_path = tempfile.mkstemp(".otf")
    font.generate(tmp_path)
    blob = hb.Blob.from_file_path(tmp_path)
    face = hb.Face(blob)
    hb_font = hb.Font(face)

    os.remove(tmp_path)

    for subtable in font.getLookupSubtables(LOOKUP):
        font.removeLookupSubtable(subtable)

    subtables = [
        # put more specific rules first so they take precedence
        (
            "Vowel S Vowel Downward 1",
            product(VOWELS[:3], S, VOWELS, DOWNWARD_CONSONANTS),
        ),
        (
            "Vowel S Vowel Downward 2",
            product(VOWELS[3:6], S, VOWELS, DOWNWARD_CONSONANTS),
        ),
        (
            "Vowel S Vowel Downward 3",
            product(VOWELS[6:], S, VOWELS, DOWNWARD_CONSONANTS),
        ),
        ("S Vowel Downward", product(S, VOWELS, DOWNWARD_CONSONANTS)),
        ("Vowel S Downward", product(VOWELS, S, DOWNWARD_CONSONANTS)),
        ("S Downward", product(S, DOWNWARD_CONSONANTS)),
        ("Vowel S Vowel", product(VOWELS, S, VOWELS)),
        (
            "S U Circle Downward",
            product(S, ["U"], ["A", "E", "I"], DOWNWARD_CONSONANTS),
        ),
        ("S Vowel", product(S, VOWELS)),
        ("Vowel Downward", product(VOWELS, DOWNWARD_CONSONANTS)),
        ("Vowel Consonant", product(VOWELS, CONSONANTS)),
        ("Consonant", CONSONANTS),
        ("Downward", DOWNWARD_CONSONANTS),
        (
            "U Vowel S Downward",
            product(["U"], ["A", "E", "O", "U", "I"], S, DOWNWARD_CONSONANTS),
        ),
        (
            "U Vowel Downward",
            product(["U"], ["A", "E", "O", "U", "I"], DOWNWARD_CONSONANTS),
        ),
        ("U Circle", product(["U"], ["A", "E", "I"])),
        ("Vowel", VOWELS),
        ("O", ["o("]),
    ]

    rule_count = 0
    last_subtable = None
    for name, rule_seq in subtables:
        subtable = f"{SUBTABLE_PREFIX} {name}"
        rules = []

        for text in ("".join(t) for t in rule_seq):
            shaped = shape(text, hb_font)

            variants = TAIL_VARIANTS.get(shaped[-1], [shaped[-1]])
            glyphs_list = [shaped[:-1] + [variant] for variant in variants]

            for glyphs in glyphs_list:
                x_adjustment, y_adjustment = 0, 0
                exit_x, exit_y = 0, 0
                xmin, ymin = 0, 0
                for glyph_name in glyphs:
                    glyph = font[glyph_name]
                    for anchor in glyph.anchorPoints:
                        if anchor[0] == "Join" and anchor[1] == "entry":
                            entry_x = anchor[2]
                            entry_y = anchor[3]

                    xmin, ymin, _xmax, _ymax = glyph.boundingBox()
                    x_adjustment += max(0, round(entry_x - xmin - exit_x))
                    y_adjustment += max(
                        0, round(entry_y - ymin - exit_y - font.strokewidth)
                    )

                    for anchor in glyph.anchorPoints:
                        if anchor[0] == "Join" and anchor[1] == "exit":
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

                rules.append(f"| _start {' '.join(lookups)} | {' '.join(glyphs)}")
                rule_count += 1

        if last_subtable is not None:
            font.addContextualSubtable(
                LOOKUP,
                subtable,
                "glyph",
                rules,
                afterSubtable=last_subtable,
            )
        else:
            font.addContextualSubtable(LOOKUP, subtable, "glyph", rules)

        print(f"{subtable}: {len(rules)} rules")

        last_subtable = subtable

    font["_start"].addPosSub(
        "Stroke Adjustment", -int(font.strokewidth), -int(font.strokewidth), 0, 0
    )

    print("Created", rule_count, "rules")


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
