
import pytest
from sty import renderfunc

def test_valid_input():
    # Test valid RGB values
    assert renderfunc.rgb_bg(0, 0, 0) == '\x1b[48;2;0;0;0m'
    assert renderfunc.rgb_bg(255, 255, 255) == '\x1b[48;2;255;255;255m'
    assert renderfunc.rgb_bg(255, 0, 0) == '\x1b[48;2;255;0;0m'
    assert renderfunc.rgb_bg(0, 255, 0) == '\x1b[48;2;0;255;0m'
    assert renderfunc.rgb_bg(0, 0, 255) == '\x1b[48;2;0;0;255m'
