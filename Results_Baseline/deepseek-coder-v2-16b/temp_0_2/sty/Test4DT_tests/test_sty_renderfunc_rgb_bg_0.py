# Module: sty.renderfunc
# test_renderfunc.py
import pytest
from sty.renderfunc import rgb_bg

def test_rgb_bg():
    # Test case 1: RGB values for bright green (0, 255, 0)
    assert rgb_bg(0, 255, 0) == "\x1b[48;2;0;255;0m"
    
    # Test case 2: RGB values for pure red (255, 0, 0)
    assert rgb_bg(255, 0, 0) == "\x1b[48;2;255;0;0m"
    
    # Test case 3: RGB values for blue (0, 0, 255)
    assert rgb_bg(0, 0, 255) == "\x1b[48;2;0;0;255m"
    
    # Test case 4: RGB values for white (255, 255, 255)
    assert rgb_bg(255, 255, 255) == "\x1b[48;2;255;255;255m"
    
    # Test case 5: RGB values for black (0, 0, 0)
    assert rgb_bg(0, 0, 0) == "\x1b[48;2;0;0;0m"

# Additional test cases can be added to cover more edge cases or different color combinations.
