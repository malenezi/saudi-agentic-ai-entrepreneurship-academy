.PHONY: check links test

# Everything CI runs. Python 3.9 or newer, standard library only.
check: links test

links:
	python3 tools/check_repo.py

test:
	python3 -m unittest discover -s tests
