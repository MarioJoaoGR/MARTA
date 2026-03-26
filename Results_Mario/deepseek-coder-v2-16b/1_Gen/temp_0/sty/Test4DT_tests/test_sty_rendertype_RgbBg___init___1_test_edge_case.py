
import pytest
from sty import RgbBg

def test_edge_case():
    # Test with boundary values for each color component
    rgb_bg = RgbBg(0, 0, 0)
    assert rgb_bg.args == [0, 0, 0]
    
    rgb_bg = RgbBg(255, 255, 255)
    assert rgb_bg.args == [255, 255, 255]
    
    # Test with values at the boundary of valid range
    rgb_bg = RgbBg(0, 0, 0)
    assert rgb_bg.args == [0, 0, 0]
    
    rgb_bg = RgbBg(255, 255, 255)
    assert rgb_bg.args == [255, 255, 255]
