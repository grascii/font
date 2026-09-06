# Modeling

Modeling is the process of creating and editing the appearance of glyphs.

Glyphs are modeled as cubic Bezier curves in SVG files. Those SVG files are then
imported into FontForge using a Grascii tool that will also automatically set
anchor points for cursive positioning. During the build process, the curves will
be run through FontForge's Expand Stroke functionality to produce an outlined
font.

## Example Workflow

Suppose you want to add a glyph for "a" when it appears between "k" and "t".

1. Find a reference image for a word containing "kat". [Grascii
   Search](https://huggingface.co/spaces/grascii/search) is helpful for this
step.
2. Try to reuse an existing glyph.
    1. Look for an existing glyph for "a" that might work (unchanged or
       transformed). In this case, "kat" is similar to "tar" just upside down.
    2. Create a new glyph in FontForge named "a.kat" and open it.
    3. Use Tools > Create From Reference. Enter "a.tar" as the glyph and select
       "R to K" for the transformation and leave the second transformation as
       "Identity".
    4. Click "OK". The tool will create a reference to the existing the glyph in
       FontForge and create Join entry and exit anchors for cursive positioning.
3. Define a lookup rule for the new glyph.
    1. Open Element > Font Info.
    2. Click on "Lookups".
    3. Expand "Between k t" and double-click the "Between k t" subtable.
    4. Add an entry for "a" as the base glyph and "a.kat" as the replacement.
       Click "OK".
    5. Click "OK" on the Font info dialog and save the project.
4. Check the appearance of the glyph in context.
    1. Open Metrics > New Metrics Window.
    2. Enter "kat" in the text field.
    3. See how the form looks in the view window. If satisfied, you are done.
       For the purposes of this example, suppose it doesn't look quite right and
       that "tar" and "kat" are not as similar as originally thought.
5. Create a new base model.
    1. Start a new file in Inkscape.
    2. Import the reference image from step 1.
    3. Import the base models for the relevant glyphs from `base_models/`.
        - `k.svg`
        - `a.svg`
        - `t.svg`
    4. Make sure the reference image is behind the base models and resize it to
       match the size of the "k" and "t" based models as closely as possible.
    5. Edit the "a" model with the Node Tool to match the reference image as
       closely as possible.
    6. When satisfied, open the XML Editor and locate the lowest group ("g"
       element) that contains the "a" path. Set the "id" attribute on the group
       to "model".
    7. Clean up the file by deleting the reference image and any other
       intermediate work. Only "k", "a", and "t" should be left.
    8. Go to File > Save As. Save the file in `base_models/a/` with the name
       `kat.svg` and "Optimized SVG" as the file type. In the optimization
       dialog, accept the default settings by clicking "OK".
6. Import the new model.
    1. In FontForge, open the "a.kat" glyph.
    2. Select Tools > Import Grascii Base Model.
    3. Select the `kat.svg` file you just saved.
    4. In the following dialog, leave "model" as the ID and press "OK". The tool
       will draw the glyph in FontForge and create Join entry and exit anchors
       for cursive positioning.
7. Check the appearance of the new glyph.
    1. Open the Metrics window like before and see how "kat" looks.
    2. Also double-check the similar forms: "kad", "gat", and "gad".
8. Add tests for the new glyph.
    1. Open `tests/substitution/test_a.py`.
    2. Add test cases under `test_k_a` and `test_g_a` for "kat", "kad", "gat",
       and "gad".
9. Run the tests.
    1. Run `make test` and make sure all the tests pass.

## Inkscape Practices

When modeling glyphs in Inkscape, there are certain guidelines to follow:

- Keep models simple. For the most part, they do not need more than three nodes.
- Use Inkscape's snapping feature when editing control points which snaps
  their angles to 15-degree increments.
- Nodes should be smooth or symmetric, not corner nodes.
- When a model should join smoothly with the next stroke, make sure the end of
  the model is tangent to the next stroke. For instance, if "a" is being modeled
  before "t", the control point at the end of the "a" should be at a 30-degree
  angle to match the angle of the "t".
- When a circle vowel is at a non-smooth joining with another stroke, it should
  touch it at a 90-degree angle (+/- 30 degrees based on the reference image).
  So, if modeling "a" in "at", the control point of start of the "a" should be
  perpendicular to the "t".
- Save the model along with its contextual strokes, but nothing else.
- Save files in "Optimized SVG" format with the default settings.
