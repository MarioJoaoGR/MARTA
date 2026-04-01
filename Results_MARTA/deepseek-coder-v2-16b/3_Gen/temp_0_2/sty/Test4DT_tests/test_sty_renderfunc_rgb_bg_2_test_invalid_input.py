
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be in the range 0 to 255")
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def test_invalid_input():
    # Test case for invalid RGB values that should raise a ValueError
    with pytest.raises(ValueError):
        rgb_bg(-1, 256, 0)
    
    # Test case for valid RGB values
    assert rgb_bg(0, 0, 0) == "\x1b[48;2;0;0;0m"
