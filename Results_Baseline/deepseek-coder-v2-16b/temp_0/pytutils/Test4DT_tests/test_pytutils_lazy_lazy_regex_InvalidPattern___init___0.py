
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

# Test 1: Creating an instance with a specific message
def test_invalid_pattern_with_specific_message():
    msg = "The provided pattern does not match any known format."
    invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern.msg == msg

# Test 2: Using the class in an exception scenario
def test_invalid_pattern_exception():
    msg = "Missing required fields in the input data."
    with pytest.raises(InvalidPattern):
        raise InvalidPattern(msg)

# Test 3: Creating an instance with a different message
def test_invalid_pattern_with_different_message():
    msg = "Missing required fields in the input data."
    invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern._fmt % {'msg': invalid_pattern.msg} == "Invalid pattern(s) found. Missing required fields in the input data."
