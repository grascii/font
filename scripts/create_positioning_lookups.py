import fontforge

font = fontforge.open(sys.argv[1])

base = 6
digits = 4

last_lookup = "Ing Ing Positioning"

start_glyph = font["_start"]

for exp in range(digits):
    increment = base ** exp
    for i in range(1, base):
        amount = increment * i
        name = f"Right {amount}"
        font.addLookup(name, "gpos_single", None, (), last_lookup)
        font.addLookupSubtable(name, name)
        start_glyph.addPosSub(name, amount, 0, 0, 0)
        last_lookup = name


for exp in range(digits):
    increment = base ** exp
    for i in range(1, base):
        amount = increment * i
        name = f"Up {amount}"
        font.addLookup(name, "gpos_single", None, (), last_lookup)
        font.addLookupSubtable(name, name)
        start_glyph.addPosSub(name, 0, amount, 0, 0)
        last_lookup = name

font.save(sys.argv[1])
