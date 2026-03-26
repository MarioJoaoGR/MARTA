
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def test_edge_case_zero():
    expected_output = '\x1b[48;2;0;0;0m'
    assert rgb_bg(0, 0, 0) == expected_output
