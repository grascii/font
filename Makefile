FONT_FORGE = $(shell (command -v fontforge && echo fontforge) || echo ./FontForge.AppImage)
CWD = $(shell pwd)

.PHONY: install-tools run

run:
	$(FONT_FORGE) $(CWD)/Grascii.sfdir

test:
	$(FONT_FORGE) --quiet -script $(CWD)/tests/main.py

install-tools: tools/load.py | env
	$(eval FF_INIT_DIR := $(shell $(FONT_FORGE) --quiet -c 'print(fontforge.scriptPath()[-1])'))
	sed "s|REPLACE|$(CWD)|" ./tools/load.py > $(FF_INIT_DIR)/load_grascii_tools.py

env: requirements.txt
	if [ ! -d env ]; then \
		python -m venv env; \
	fi
	./env/bin/python -m pip install -U pip
	./env/bin/python -m pip install -r requirements.txt
