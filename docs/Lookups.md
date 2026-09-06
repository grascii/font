# Lookups

Grascii makes use of several OpenType lookups.

## Substitution

### Lowercase (RQD)

Substitutes uppercase glyphs for lowercase glyphs to achieve Case-insensitivity.

### Multichar Strokes (rlig)

Creates glyphs represented by multiple characters like `ch`, `sh`, `th`, and
diphthongs. Supports the [canonical
interpretation](https://grascii.readthedocs.io/en/stable/interpretation.html#the-canonical-interpretation).

### Blended Consonants Override (rclt)

Creates glyphs for priority blended consonants according to Rule 4 of the
[canonical
interpretation](https://grascii.readthedocs.io/en/stable/interpretation.html#the-canonical-interpretation).

### Blended Consonants (rlig)

Creates glyphs for all other blended consonants.

### Blended Consonants Decomposition (ccmp)

Splits blended consonants like `mn` and `td` that can be represented by two
separate glyphs.

### Aliases (ccmp)

Substitutes glyphs represented by single characters that are an alias for
another glyph. Ex. `z` is an alias for `s`.

### Boundaries and Jogs (rclt)

Replaces hyphens with a dedicated boundary glyph or a jog glyph when it appears
between two straight horizontal or upward glyphs.

### Wunderbars (rclt)

Replaces underscores after vowels with a wunderbar mark glyph that represents
the w sound.

### Annotated Directions (rclt)

Consumes direction annotations `)`/`(` applied to consonants like `s` and `th`.

### Directions (rclt)

Infers the directions of un-annotated consonants like `s` and `th` based on
their surrounding strokes.

### Aspirate Swap A (rlig)

Replaces apostrophes preceding strokes with intermediate glyphs like
`a.aspirate`. Grascii has aspirates before the strokes they apply to, but
OpenType marks are positioned to the glyphs that precede them. This is the first
lookup in the process of swapping aspirates to be after their stroke.

### Aspirate Swap B (ccmp)

Replaces intermediate glyphs like `a.aspirate` with the stroke followed by an
aspirate mark glyph.

### Ings (rclt)

Replaces other apostrophes with a mark glyph for the ing dot.

### Start and End (ccmp)

Replaces strokes with themselves preceded by a helper `_start` glyph and
followed by a helper `_end` glyph.

### Middle (ccmp)

Replaces an `_end` glyph next to a `_start` glyph with a helper `_middle`
mark glyph. At this point, the first glyph in an outline is preceded by
`_start` glyph and the last glyph in a outline is followed by an `_end` glyph.
The `_middle` glyph has no use at the moment, but may in the future.

### Consonant Joinings (rclt)

Replaces consonants with common variants depending on their context.

### Vowel Between (rclt)

Replaces vowels with variants according to the glyphs they appear between. Not
all vowels may match a rule in this lookup.

### Vowel Before/After (rclt)

Replaces vowels with variants according to the glyph they appear before. If
vowels are at the end of a outline, they are replaced according to the glyph
they appear after.

### Vowel Fallback (rclt)

Replaces vowels like `a&'` and `a&e` that did not match a rule in the last two
lookups with a similar fallback, like `a`. Then, reruns the Vowel Between and
Vowel Before/After lookups.

### Diphthong Decomposition (ccmp)

Splits hook diphthongs that did not match a vowel rule into two separate glyphs.
Handles diphthongs that are written by themselves.

### Consonant Joinings 2 (rclt)

Applies uncommon and specific consonant variants.

### Final Substitutions (rclt)

Applies any final substitutions for glyphs that did not match other rules and
cleans up unneeded glyphs like `_middle`.

## Positioning

### Line of Writing (RQD)

Repositions the `_start` glyph such that the correct glyph appears to rest on
the line of writing. The subtables in this lookup are generated via a script
(`make calculate-line-of-writing`).

### Stroke Adjustment (RQD)

Shifts the `_start` glyph to account for the stroked font stroke width
configured in FontForge which affects the calculations for Line of Writing.

### Cursive Attachment (curs)

Enables cursive positioning for strokes.

### A&' Dot Positioning (mark)

Positions the dot in `a&'` in the middle of `a`.

### Aspirate Positioning (mark)

Positions aspirates above strokes.

### Ing Positioning (mark)

Positions ing dots after strokes.

### Ing Ing Positioning (mkmk)

Positions a dot next to an ing dot for outlines like `th''`.

### Sound Positioning (mark)

Positions wunderbars below vowels.
