
import pytest
from sty import renderfunc

def test_valid_input():
    # Test cases for valid inputs
    assert renderfunc.eightbit_fg(0) == "\033[38;5;0m"
    assert renderfunc.eightbit_fg(255) == "\033[38;5;255m"
    assert renderfunc.eightbit_fg(127) == "\033[38;5;127m"
    assert renderfunc.eightbit_fg(64) == "\033[38;5;64m"
    assert renderfunc.eightbit_fg(192) == "\033[38;5;192m"
