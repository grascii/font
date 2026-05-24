import fontforge

def view_reference_tree(data: None, font: fontforge.font):
    try:
        selected = next(iter(font.selection.byGlyphs))
    except StopIteration:
        return

    builder = []

    def traverse(node: fontforge.glyph, depth: int):
        builder.append("    " * depth)
        builder.append(node.glyphname)
        builder.append("\n")
        for ref in node.references:
            child = font[ref[0]]
            traverse(child, depth + 1)

    traverse(selected, 0)
    builder.append("--")
    fontforge.postNotice(f"{selected.glyphname} Reference Tree", "".join(builder))


fontforge.registerMenuItem(
    callback=view_reference_tree,
    context="Font",
    name=("View Reference Tree", "grascii_view_reference_tree")
)
