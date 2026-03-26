
import pytest
from sty import renderfunc

def test_valid_input():
    # Test valid input for sgr function
    assert renderfunc.sgr(1) == '\033[1m'
    assert renderfunc.sgr(31) == '\033[31m'
    assert renderfunc.sgr(42) == '\033[42m'
