# Frequently Asked Questions

### Can I do X with the font?

Probably, Grascii is distributed under the permissive [SIL Open Font
License](https://openfontlicense.org/). See also [OFL.txt](../OFL.txt) and
[OFL-FAQ.txt](../OFL-FAQ.txt).

### How is this possible?

Grascii leverages OpenType, the same modern font technology used for an array
of world writing systems. In particular, Grascii makes heavy use of contextual
substitution, ligatures, cursive joining, and mark positioning.

### How does this compare to text2Gregg (steno.tu-clausthal.de)?

**License**

*text2Gregg*: None, closed-source. The tool is served through a web application
which could disappear at any time.

*Grascii*: Open Font License. Anyone can build and modify the font.

**Technology**

*text2Gregg*: METAFONT: A powerful font creation tool which has not gained much
traction.

*Grascii*: OpenType: A modern font format with wide support across operating
systems and applications.

**Input**

*text2Gregg*: English text. The text is converted into Gregg strokes using a
dictionary for briefs and phrases, and pronunciation for all other words.

*Grascii*: Grascii text. The user has full control over the Gregg strokes used
to write a word or phrase.

**Output**

*text2Gregg*: .gif, .djvu, .pdf, and .svg exposed through the online tool.

*Grascii*: Rendered Gregg Shorthand. A variety of programs can be used to output
the rendered font into various image and document formats.

**Modeling**

*text2Gregg*: Standard strokes are defined as curves in METAFONT. Joinings
between strokes are generated mathematically.

*Grascii*: Glyphs use cubic Bezier curves and are manually modeled
based on handwritten forms from the official Gregg Shorthand dictionaries.

**Styling**

*text2Gregg*: The generated shorthand is based on the Centennial (1988) edition
of Gregg Shorthand, one of the newest editions with fewer special joinings and
rules compared to previous editions.

*Grascii*: The rendered shorthand is based on the Preanniversary (1916) edition
of Gregg Shorthand, one of the oldest editions with more special joinings and
rules compared to later editions.

### Why is the font based on Preanniversary?

The Grascii font is based on the Preanniversary (1916) edition of Gregg
Shorthand just like the Grascii language. Using Preanniversary as the foundation
is advantageous when adding support for later editions of Gregg Shorthand.
Preanniversary is essentially a superset of all other editions, so adapting for
them is a matter of subtraction rather than addition.

### How do I write X?

Check the [User Guide](./UserGuide.md) and then
[Discussions](https://github.com/grascii/font/discussions) to see if anyone has
the same question. If you still don't find an answer, start a [new
discussion](https://github.com/grascii/font/discussions/new?category=q-a).

### Why is it so small?

Grascii's glyphs are sized such that the widest glyphs (like Gregg L) are as
wide as the widest glyphs in a typical Latin font (like Latin M). As such, at
12pt, Grascii appears very small. The font size at which Grascii approaches the
actual size of handwritten Gregg Shorthand is 36-48pt.

The default sizing of the font may be changed in the future.

### Why is this stroke overlapping with the previous word?

With the way OpenType handles cursive fonts, a space advances the cursor from
the rightmost edge of the previous glyph. While this behavior works well in most
cases, it can fall short when strokes that end to the left of where they began
(like Gregg B) are involved.

"B" followed by a space is no problem: the cursor advances from the rightmost
edge of the "B", the top. However, "BE" followed by a space has an issue. The
cursor advances from the rightmost edge of the "E" which is not as far right as
the top of the "B". Thus, the cursor may land left of the top of the "B" or
close to it causing the next typed stroke to overlap with the "B"!

Rather than implementing an [expensive
system](https://github.com/dscorbett/duployan-font/blob/master/docs/width-system.md)
in the font to correct this behavior, Grascii leaves it up to the user to insert
additional spaces as needed in these cases.

### Why doesn't this look right?

If the strokes appear next to each other but are not connected, the application
you are using may not support the required OpenType features. See
[Applications](./UserGuide.md#applications).

If the shorthand form is readable but not realistic, see the next FAQ.

If the form is obviously incorrect (overlapping strokes, weird strokes,
misplaced marks) it may be that the particular joining is not modeled. The
initial version of Grascii only modeled joinings that appear in the
Preanniversary or Anniversary Gregg Shorthand dictionaries.

Check if this is a known issue:

1. Type the bad text into the demo site. The demo has the bleeding edge version
of the font and there is a chance the issue may already be fixed. If it looks
better, install the newest version of the font.
2. Check [Issues](https://github.com/grascii/font/issues) and
   [Discussions](https://github.com/grascii/font/discussions) for existing
reports of the same issue.

If this is not a known issue, create a [new
issue](https://github.com/grascii/font/issues/new?template=wrong.yaml).

### What are the core design principles of the font?

**Legibility**

The rendered font should be recognizable and readable Gregg Shorthand.

**Manage Technical Complexity**

The font internals should be relatively easy to understand and modify. There
should not be duplicate or extraneous glyphs.

In practice, this means:

- Avoid consonant variants; leave variants for vowels.
- If consonant variants are necessary, limit variants to only the start or end
of the consonant, not both.
- Exploit symmetry in strokes. Ex. "K" is simply "R" rotated 180 degrees.
- Take advantage of similar strokes. Ex. "F" and "V", and "N" and "M" only
differ in size, so the same "A" glyph can be used in "FAN", "FAM", "VAN", and
"VAM".
- Prefer contextual lookups that look no more than one glyph backward or
forward.
- Apply general lookups early and specific lookups as late as possible.

One of the consequences of managing technical complexity is that while the Gregg
shorthand is legible, it may not always look realistic. Consonants in
handwritten Gregg are not perfectly consistent and may be written with slightly
different angles and lengths depending on their connected strokes.

### Why does Grascii use the Latin character set for Gregg strokes?

The Grascii language is designed to be typable on a standard QWERTY keyboard
without requiring any additional software. Accordingly, the font follows the
same principle.

Fonts for non-Latin scripts typically use the appropriate Unicode code blocks
for their glyphs. Although, Unicode does not have a block for all scripts and
does not have one for Gregg Shorthand. In such cases, fonts sometimes use the
Unicode Private Use Area (PUA). However, adopting the PUA for Grascii would
require defining code points for every Gregg character and would still result in
a non-standard solution. Moreover, those code points would not be directly
typable, and the font would need to be paired with another program or input
method, creating user friction.

Nevertheless, anyone who would like to use the Private Use Area for a Gregg
Shorthand font is welcome to do so. Adapting the Grascii font to use the PUA
would likely be straightforward via substitution rules.

### What if the FAQ didn't answer my question?

Check the [Discussions](https://github.com/grascii/font/discussions) to see if
anyone has the same question. If you still don't find an answer, start a [new
discussion](https://github.com/grascii/font/discussions/new?category=q-a).
