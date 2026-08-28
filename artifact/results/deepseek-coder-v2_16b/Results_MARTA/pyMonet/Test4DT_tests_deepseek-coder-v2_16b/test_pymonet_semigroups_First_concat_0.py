
import pytest
from pymonet.semigroups import First

# Test valid case with default value

# Test error case where input is none

# Test valid case with specific value
def test_valid_case_with_specific_value():
    specific_value = "initial string"
    first_instance = First(specific_value)
    assert first_instance.value == specific_value

# Test combining two instances
def test_combining_two_instances():
    value1 = 42
    value2 = "hello"
    first1 = First(value1)
    first2 = First(value2)
    combined_first = first1.concat(first2)
    assert combined_first.value == value1  # Should return the first value