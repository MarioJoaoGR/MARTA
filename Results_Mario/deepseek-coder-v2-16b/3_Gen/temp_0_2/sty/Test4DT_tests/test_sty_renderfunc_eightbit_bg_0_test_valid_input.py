
import pytest
from sty import renderfunc

def test_valid_input():
    assert renderfunc.eightbit_bg(0) == "\033[48;5;0m"
    assert renderfunc.eightbit_bg(255) == "\033[48;5;255m"
    assert renderfunc.eightbit_bg(100) == "\033[48;5;100m"
