
import pytest
from sty.rendertype import EightbitBg

def test_valid_input():
    # Test valid input within the range of 0 to 255
    num = 42
    bg_color = EightbitBg(num)
    assert bg_color.args == [num]
