
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def test_valid_input():
    assert rgb_bg(0, 0, 0) == '\x1b[48;2;0;0;0m'
    assert rgb_bg(255, 255, 255) == '\x1b[48;2;255;255;255m'
    assert rgb_bg(255, 0, 0) == '\x1b[48;2;255;0;0m'
    assert rgb_bg(0, 255, 0) == '\x1b[48;2;0;255;0m'
    assert rgb_bg(0, 0, 255) == '\x1b[48;2;0;0;255m'
