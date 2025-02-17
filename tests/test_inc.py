import sys
import os

# Add the parent directory to sys.path so Python can find 'inc.py'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from inc import inc

def test_inc():
    assert inc(1) == 2  # 1 + 1 should be 2
    assert inc(0) == 1  # 0 + 1 should be 1
    assert inc(-1) == 0  # -1 + 1 should be 0
    assert inc(99) == 100  # 99 + 1 should be 100

# run 'pytest' to run the tests (all files starting with 'test_').