
import pytest
from httpie.context import Environment

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        # Providing invalid keyword arguments should raise AssertionError
        Environment(invalid_arg='invalid_value')
