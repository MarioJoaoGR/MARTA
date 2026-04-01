
import pytest
from sty import RgbBg

def test_valid_input():
    rgb_bg = RgbBg(255, 0, 0)
    assert rgb_bg.args == [255, 0, 0]
