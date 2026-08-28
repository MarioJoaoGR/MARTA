
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

# Test case for the constructor of InvalidPattern class
def test_invalid_pattern_constructor():
    msg = "Incorrect format of the input."
    invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern.msg == msg

# Test case to check the string representation of InvalidPattern instance
def test_invalid_pattern_str_representation():
    msg = "You have entered an invalid pattern."
    invalid_pattern = InvalidPattern(msg)
    expected_output = 'Invalid pattern(s) found. You have entered an invalid pattern.'