#!/usr/bin/env python3
"""Build this course's decks. The engine and the page template are shared by all
courses: see tools/build_slides.py and tools/slides/template.html.
Usage: python3 build.py   (from any directory)
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.exit(subprocess.call([sys.executable, str(ROOT / "tools" / "build_slides.py"), "4"]))
