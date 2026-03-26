
import pytest
from sty import rendertype  # Assuming 'sty' is the module where RgbBg is defined, adjust accordingly if needed

def test_rgb_bg_init():
    """Test initialization of RgbBg class with valid RGB values."""
    r = 128
    g = 64
    b = 32
    
    rgb_bg = rendertype.RgbBg(r, g, b)
    
    assert isinstance(rgb_bg, rendertype.RgbBg), "The object should be an instance of RgbBg"
    assert rgb_bg.args == [r, g, b], "The RGB values should match the initialized values"
