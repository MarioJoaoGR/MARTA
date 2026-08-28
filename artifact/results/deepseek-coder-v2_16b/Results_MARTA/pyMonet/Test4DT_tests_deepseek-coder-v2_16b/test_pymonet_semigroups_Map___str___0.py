
import pytest
from pymonet.semigroups import Map

# Test valid input where Maybe is not nothing and has a valid value

# Test edge case where Maybe is empty (is_nothing is True)
def test_none_input():
    map = Map(None)
    assert map.value == None  # The value should be None when initialized with None

# Test empty input, which means no arguments are passed to the constructor