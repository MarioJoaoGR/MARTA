
import pytest
from sty.renderfunc import eightbit_bg

def test_eightbit_bg_valid_input():
    assert eightbit_bg(15) == "\033[48;5;15m"
    assert eightbit_bg(0) == "\033[48;5;0m"