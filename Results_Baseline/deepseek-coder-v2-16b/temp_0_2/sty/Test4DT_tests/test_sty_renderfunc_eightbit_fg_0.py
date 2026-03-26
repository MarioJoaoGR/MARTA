
import pytest
from sty import renderfunc

# Test cases for eightbit_fg function
def test_eightbit_fg_valid_range():
    # Valid range should return the correct escape sequence
    assert renderfunc.eightbit_fg(196) == '\033[38;5;196m'
    assert renderfunc.eightbit_fg(0) == '\033[38;5;0m'