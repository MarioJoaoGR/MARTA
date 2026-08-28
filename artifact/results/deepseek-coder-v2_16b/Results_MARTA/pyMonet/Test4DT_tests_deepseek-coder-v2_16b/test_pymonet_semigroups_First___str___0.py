
import pytest
from pymonet.semigroups import First

# Test valid input where Maybe is not nothing and has a valid value

# Test edge case where Maybe is empty (is_nothing is True)

# Test invalid input where an exception should be raised
def test_invalid_input():
    with pytest.raises(TypeError):
        First()