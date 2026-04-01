
import pytest
from math import ceil

def ceil_div(a: int, b: int) -> int:
    """Integer division that rounds up."""
    return (a - 1) // b + 1

def test_invalid_inputs():
    # Test with invalid inputs where a is not an integer or b is zero
    with pytest.raises(TypeError):
        ceil_div("string", 3)
    
    with pytest.raises(TypeError):
        ceil_div(10, "string")
    
    with pytest.raises(ZeroDivisionError):
        ceil_div(10, 0)
