
from sty import Style, RgbFg, Sgr
from typing import Iterable
import pytest

class StylingRule:
    pass

@pytest.mark.parametrize("value", [
    "\x1B[38;2;1;5;10m\x1B[1m"  # Correctly escaped ANSI sequence
])
def test_invalid_input(value):
    class MockStylingRule(StylingRule):
        pass
    
    style = Style(*[MockStylingRule() for _ in range(2)], value=value)
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == value
