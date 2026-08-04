import uharfbuzz as hb


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    glyphs = (font.glyph_to_string(info.codepoint) for info in buf.glyph_infos)
    return list(filter(lambda g: g != "_start" and g != "_end", glyphs))
