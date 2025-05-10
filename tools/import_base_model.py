import fontforge
import psMat
from svgpathtools import Document, SVG_GROUP_TAG, SVG_NAMESPACE, Line, CubicBezier, QuadraticBezier


MODEL_ID = "model"


def bbox(paths):
    bbs = [path.bbox() for path in paths]
    xmins, xmaxs, ymins, ymaxs = list(zip(*bbs))
    xmin = min(xmins)
    xmax = max(xmaxs)
    ymin = min(ymins)
    ymax = max(ymaxs)
    return xmin, -ymax, xmax, -ymin


def import_base_model(data, glyph):
    filename = fontforge.openFilename("Select a base model file", "", "*.svg")
    if not filename:
        return

    doc = Document(filename)
    groups = doc.root.findall(f".//{SVG_GROUP_TAG}[@id='{MODEL_ID}']", SVG_NAMESPACE)
    assert len(groups) == 1
    paths = doc.paths_from_group(groups[0])

    transformed = []
    pen = glyph.glyphPen()
    start = paths[0].start
    for path in paths:
        path = path.translated(-start)
        path = path.scaled(60, 60)
        transformed.append(path)

    contour = fontforge.contour()
    contour.moveTo(0, 0)
    for path in transformed:
        for segment in path:
            if isinstance(segment, Line):
                contour.lineTo((segment.end.real, -segment.end.imag))
            elif isinstance(segment, CubicBezier):
                contour.cubicTo(
                    (segment.control1.real, -segment.control1.imag),
                    (segment.control2.real, -segment.control2.imag),
                    (segment.end.real, -segment.end.imag),
                )
            else:
                raise Exception(f"Base model contains an unsupported path segment of type {type(segment)}")

    contour.draw(pen)

    (xmin, ymin, xmax, ymax) = bbox(transformed)

    glyph.addAnchorPoint("Join", "entry", contour[0].x, contour[0].y)
    glyph.addAnchorPoint("Join", "exit", contour[-1].x, contour[-1].y)

    if contour[0].y <= 0 and contour[-1].y <= 0 and ymin < -0.001:
        glyph.transform(psMat.translate(0, ymax - ymin))

    glyph.right_side_bearing = 0
    glyph.left_side_bearing = 0

    glyph.round()


fontforge.registerMenuItem(
    callback=import_base_model,
    context="Glyph",
    name=("Import Grascii Base Model", "grascii_import_base_model")
)
