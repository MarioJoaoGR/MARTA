# Module: sty.renderfunc
import pytest
from sty.renderfunc import rgb_fg

def test_rgb_fg_vivid_green():
    assert rgb_fg(0, 255, 0) == '\x1b[38;2;0;255;0m'

def test_rgb_fg_red():
    assert rgb_fg(255, 0, 0) == '\x1b[38;2;255;0;0m'

def test_rgb_fg_blue():
    assert rgb_fg(0, 0, 255) == '\x1b[38;2;0;0;255m'

def test_rgb_fg_grayscale():
    assert rgb_fg(64, 64, 64) == '\x1b[38;2;64;64;64m'

# Add more tests for edge cases and invalid inputs if necessary
