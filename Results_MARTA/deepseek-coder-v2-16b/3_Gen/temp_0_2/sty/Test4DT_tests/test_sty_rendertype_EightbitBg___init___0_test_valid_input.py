
import pytest
from sty import rendertype

def test_valid_input():
    bg = rendertype.EightbitBg(10)
    assert isinstance(bg, rendertype.EightbitBg)
    assert bg.args == [10]
