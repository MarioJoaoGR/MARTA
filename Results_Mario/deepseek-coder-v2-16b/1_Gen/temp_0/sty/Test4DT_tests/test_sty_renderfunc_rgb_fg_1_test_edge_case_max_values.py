
import pytest
from sty import renderfunc

def test_edge_case_max_values():
    # Test the function with maximum RGB values (255, 255, 255)
    result = renderfunc.rgb_fg(255, 255, 255)
    assert result == '\x1b[38;2;255;255;255m'
