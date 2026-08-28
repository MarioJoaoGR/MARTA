
import pytest
from pymonet.semigroups import Last

# Test scenario 1: test_valid_concat - Standard concatenation of two Last instances with different values
def test_valid_concat():
    last1 = Last(10)
    last2 = Last(20)
    combined_last = last1.concat(last2)
    assert combined_last.value == 20, f"Expected value to be 20 but got {combined_last.value}"

# Test scenario 2: test_edge_case_none - Concatenating None with a Last instance
def test_edge_case_none():
    last_with_none = Last(None)
    none_concat = Last(None).concat(last_with_none)
    assert none_concat.value is None, f"Expected value to be None but got {none_concat.value}"

# Test scenario 3: test_invalid_input - Concatenating an invalid type with a Last instance
def test_invalid_input():
    invalid_type_concat = Last('string').concat(Last(10))
    assert isinstance(invalid_type_concat.value, int), f"Expected value to be of type int but got {type(invalid_type_concat.value)}"
