
import pytest
from math import ceil as real_ceil

def ceil_div(a: int, b: int) -> int:
    """Integer division that rounds up."""
    return (a - 1) // b + 1

def test_invalid_input_non_integer():
    with pytest.raises(TypeError):
        ceil_div("string", 3)
        ceil_div(3, "string")
        ceil_div(None, 3)
        ceil_div(3, None)
        ceil_div([], 3)
        ceil_div(3, [])
        ceil_div({}, 3)
        ceil_div(3, {})
