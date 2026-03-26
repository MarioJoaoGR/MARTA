
import pytest
from sty.rendertype import RgbFg

# Test initialization with valid RGB values
def test_rgb_fg_initialization():
    rgb = RgbFg(255, 0, 0)
    assert rgb.args == [255, 0, 0]

# Test initialization with different RGB values
def test_rgb_fg_different_values():
    rgb = RgbFg(0, 255, 0)
    assert rgb.args == [0, 255, 0]

# Test initialization with edge case values (all zeros)
def test_rgb_fg_edge_case_zeros():
    rgb = RgbFg(0, 0, 0)
    assert rgb.args == [0, 0, 0]

# Test initialization with edge case values (all maximums)
def test_rgb_fg_edge_case_maximums():
    rgb = RgbFg(255, 255, 255)