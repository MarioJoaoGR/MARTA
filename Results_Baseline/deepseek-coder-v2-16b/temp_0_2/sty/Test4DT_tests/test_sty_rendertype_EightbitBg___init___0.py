
import pytest
from sty import rendertype

# Test initialization with valid 8-bit color number
def test_eightbitbg_valid_color():
    bg = rendertype.EightbitBg(10)
    assert isinstance(bg, rendertype.EightbitBg)