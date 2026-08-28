
import pytest
from ansible.utils.version import _Numeric

# Test scenario 1: Initializing with an integer
def test_numeric_init_with_int():
    num = _Numeric(10)
    assert num.specifier == 10

# Test scenario 2: Initializing with a string representing an integer
def test_numeric_init_with_str_int():
    num = _Numeric('10')
    assert num.specifier == 10

# Test scenario 3: Attempting to initialize with None, which should raise a TypeError
def test_numeric_init_with_none():
    with pytest.raises(TypeError):
        _Numeric(None)
