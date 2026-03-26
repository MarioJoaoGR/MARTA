
import pytest
from sty import renderfunc

def test_valid_input():
    assert renderfunc.rgb_fg(0, 255, 0) == '\x1b[38;2;0;255;0m'
