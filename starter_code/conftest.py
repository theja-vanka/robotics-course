"""
Make ``helpers`` importable no matter which DayXX/ folder pytest is launched from.

pytest loads this automatically; the DayXX/ files also add starter_code/ to sys.path
themselves so ``python DayXX/some_file.py`` works without pytest too.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
