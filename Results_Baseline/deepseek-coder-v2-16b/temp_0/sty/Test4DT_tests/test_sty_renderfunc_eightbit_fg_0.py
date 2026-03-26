
import pytest
from sty import renderfunc

# Test cases for eightbit_fg function
def test_eightbit_fg_valid_input():
    assert renderfunc.eightbit_fg(123) == '\033[38;5;123m'
    assert renderfunc.eightbit_fg(0) == '\033[38;5;0m'