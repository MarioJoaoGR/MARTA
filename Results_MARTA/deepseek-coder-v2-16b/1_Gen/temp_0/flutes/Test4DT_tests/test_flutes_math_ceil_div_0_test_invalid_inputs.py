
import pytest
from flutes.math import ceil_div

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert ceil_div(10, 3) == 4
    assert ceil_div(-7, 2) == -3
    with pytest.raises(ZeroDivisionError):
        ceil_div(5, 0)
    with pytest.raises(ZeroDivisionError):
        ceil_div(0, 0)
