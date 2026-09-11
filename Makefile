FONT_FORGE = $(shell (command -v fontforge && echo fontforge) || echo ./FontForge.AppImage)
CWD = $(shell pwd)

.PHONY: all clean install test run install-tools calculate-line-of-writing

all: build/Grascii-Regular.otf build/Grascii-Regular.woff2 build/Grascii-Regular.sfd

build/%: scripts/build.py Grascii.sfdir
	mkdir -p build
	$(FONT_FORGE) --quiet -script $(CWD)/scripts/build.py $(CWD)/Grascii.sfdir

pages: build/Grascii-Regular.woff2
	cp build/Grascii-Regular.woff2 pages/assets/fonts
	git rev-parse HEAD > pages/demo/commit.txt

serve: pages
	python -m http.server --bind 127.0.0.1 --directory pages

clean:
	rm -rf build/
	rm -f pages/assets/fonts/Grascii*
	rm -f pages/demo/commit.txt

calculate-line-of-writing: scripts/calculate_line_of_writing_positions.py Grascii.sfdir
	$(FONT_FORGE) --quiet -script $(CWD)/scripts/calculate_line_of_writing_positions.py $(CWD)/Grascii.sfdir

install: build
	mkdir -p ~/.local/share/fonts/grascii
	cp build/Grascii-Regular.otf ~/.local/share/fonts/grascii

run:
	$(FONT_FORGE) $(CWD)/Grascii.sfdir

test: | env
	$(FONT_FORGE) --quiet -script $(CWD)/tests/main.py

install-tools: tools/load.py | env
	$(eval FF_INIT_DIR := $(shell $(FONT_FORGE) --quiet -skippyfile -c 'print(fontforge.scriptPath()[-1])'))
	sed "s|REPLACE|$(CWD)|" ./tools/load.py > $(FF_INIT_DIR)/load_grascii_tools.py

env: requirements.txt
	if [ ! -d env ]; then \
		python -m venv env; \
	fi
	./env/bin/python -m pip install -U pip
	./env/bin/python -m pip install -r requirements.txt
	touch env
