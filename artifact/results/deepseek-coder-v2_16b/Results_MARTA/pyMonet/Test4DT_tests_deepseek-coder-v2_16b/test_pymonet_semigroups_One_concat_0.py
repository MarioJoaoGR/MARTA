
import pytest
from pymonet.semigroups import One

# Test valid input where Maybe is not nothing and has a valid value

# Test edge case where Maybe is empty (is_nothing is True)
def test_invalid_input():
    with pytest.raises(TypeError):
        One()  # Attempt to create an instance without a value should raise TypeError