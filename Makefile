PYTHON = pypy

all:
	CFLAGS='-Wall' $(PYTHON) setup.py build
	$(PYTHON) test.py
