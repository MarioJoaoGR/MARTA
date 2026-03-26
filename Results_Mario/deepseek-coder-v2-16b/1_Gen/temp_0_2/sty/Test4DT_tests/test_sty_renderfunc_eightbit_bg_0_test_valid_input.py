
import pytest
from sty import renderfunc

def eightbit_bg(num: int) -> str:
    """
    Create a 8-bit (256-color) background escape sequence.
    """
    return "\033[48;5;" + str(num) + "m"

def test_valid_input():
    # Test valid inputs within the range of 0 to 255
    for num in range(0, 256):
        assert eightbit_bg(num) == "\033[48;5;" + str(num) + "m"
