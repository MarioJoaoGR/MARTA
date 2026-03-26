
import pytest
from sty import renderfunc

def test_valid_input():
    # Test range of valid inputs (0 to 255)
    for num in range(256):
        assert renderfunc.eightbit_fg(num) == "\033[38;5;" + str(num) + "m"
