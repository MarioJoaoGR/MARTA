
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

@pytest.mark.parametrize("r, g, b", [(0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255)])
def test_rgb_bg(r, g, b):
    expected = "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
    assert rgb_bg(r, g, b) == expected
