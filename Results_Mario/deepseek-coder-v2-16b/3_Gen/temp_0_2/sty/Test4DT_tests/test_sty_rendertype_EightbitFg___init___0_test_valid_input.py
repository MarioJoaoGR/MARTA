
import pytest
from sty import rendertype

def test_valid_input():
    # Test creating an instance of EightbitFg with a valid 8-bit color number
    fg = rendertype.EightbitFg(16)
    
    # Check that the instance was created correctly
    assert isinstance(fg, rendertype.EightbitFg), "Instance should be of type EightbitFg"
    
    # Check that the color number is stored correctly
    assert fg.args[0] == 16, "Color number should be 16"
