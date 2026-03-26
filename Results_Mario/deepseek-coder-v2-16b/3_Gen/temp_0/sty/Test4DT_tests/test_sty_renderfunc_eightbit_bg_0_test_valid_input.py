
import pytest
from sty import renderfunc

def test_valid_input():
    # Test cases for valid inputs between 0 and 255
    assert renderfunc.eightbit_bg(0) == "\033[48;5;0m"
    assert renderfunc.eightbit_bg(15) == "\033[48;5;15m"
    assert renderfunc.eightbit_bg(255) == "\033[48;5;255m"
    assert renderfunc.eightbit_bg(127) == "\033[48;5;127m"  # Midpoint value
