
import pytest
from sty import RgbFg

def test_valid_inputs():
    # Test valid green color
    green = RgbFg(0, 255, 0)
    assert green.args == [0, 255, 0]
    
    # Test valid blue color
    blue = RgbFg(0, 0, 255)
    assert blue.args == [0, 0, 255]
    
    # Additional test for a different valid RGB combination
    yellow = RgbFg(255, 255, 0)
    assert yellow.args == [255, 255, 0]
