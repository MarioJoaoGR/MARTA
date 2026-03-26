
import pytest
from sty import renderfunc

def test_valid_input():
    # Test case 1: Valid RGB values (0, 0, 0) should return '\x1b[38;2;0;0;0m'
    assert renderfunc.rgb_fg(0, 0, 0) == '\x1b[38;2;0;0;0m'
    
    # Test case 2: Valid RGB values (255, 255, 255) should return '\x1b[38;2;255;255;255m'
    assert renderfunc.rgb_fg(255, 255, 255) == '\x1b[38;2;255;255;255m'
    
    # Test case 3: Valid RGB values (255, 0, 0) should return '\x1b[38;2;255;0;0m'
    assert renderfunc.rgb_fg(255, 0, 0) == '\x1b[38;2;255;0;0m'
    
    # Test case 4: Valid RGB values (0, 255, 0) should return '\x1b[38;2;0;255;0m'
    assert renderfunc.rgb_fg(0, 255, 0) == '\x1b[38;2;0;255;0m'
    
    # Test case 5: Valid RGB values (0, 0, 255) should return '\x1b[38;2;0;0;255m'
    assert renderfunc.rgb_fg(0, 0, 255) == '\x1b[38;2;0;0;255m'
