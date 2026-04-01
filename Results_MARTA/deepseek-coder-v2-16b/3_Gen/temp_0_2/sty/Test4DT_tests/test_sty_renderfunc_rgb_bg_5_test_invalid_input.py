
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
        raise TypeError("RGB values must be integers")
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def test_invalid_input():
    with pytest.raises(TypeError):
        rgb_bg("invalid", 0, 0)
