import uharfbuzz as hb


def shape(text, font):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    return [font.glyph_to_string(info.codepoint) for info in buf.glyph_infos]
