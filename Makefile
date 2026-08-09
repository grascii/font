FONT_FORGE = $(shell (command -v fontforge && echo fontforge) || echo ./FontForge.AppImage)
CWD = $(shell pwd)

.PHONY: install test run install-tools calculate-line-of-writing

build: scripts/build.py Grascii.sfdir
	mkdir -p build
	$(FONT_FORGE) --quiet -script $(CWD)/scripts/build.py $(CWD)/Grascii.sfdir $(CWD)/build/Grascii.otf $(CWD)/build/Grascii.sfd

calculate-line-of-writing: scripts/calculate_line_of_writing_positions.py Grascii.sfdir
	$(FONT_FORGE) --quiet -script $(CWD)/scripts/calculate_line_of_writing_positions.py $(CWD)/Grascii.sfdir

install: build
	mkdir -p ~/.local/share/fonts/grascii
	cp build/Grascii.otf ~/.local/share/fonts/grascii

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
