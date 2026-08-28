
import pytest
from ansible.utils.version import _Alpha

# Scenario 1: Test comparison between two instances of _Alpha with string specifiers
def test_valid_comparison_string_with_string():
    alpha1 = _Alpha('apple')
    alpha2 = _Alpha('banana')
    assert alpha1 < alpha2, "Expected apple to be less than banana"

# Scenario 2: Test comparison between an instance of _Alpha and a string representing an integer
def test_valid_comparison_string_with_integer():
    alpha3 = _Alpha('10')
    str_int = '2'
    assert alpha3 < str_int, "Expected 10 to be less than 2"

# Scenario 3: Test raising ValueError when comparing with a non-comparable type
def test_invalid_comparison_with_non_comparable_type():
    alpha4 = _Alpha('example')
    num = 5
    with pytest.raises(ValueError):
        assert alpha4 < num, "Expected comparison to raise ValueError"
