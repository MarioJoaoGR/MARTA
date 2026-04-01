
import pytest
from sty import RgbBg

def test_edge_case():
    rgb_bg = RgbBg(255, 255, 255)
    assert rgb_bg.args == [255, 255, 255]
