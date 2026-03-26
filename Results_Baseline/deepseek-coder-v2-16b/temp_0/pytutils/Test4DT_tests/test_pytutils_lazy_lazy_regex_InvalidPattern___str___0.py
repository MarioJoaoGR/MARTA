
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

# Test cases for the InvalidPattern class
def test_invalid_pattern_init():
    invalid_pattern = InvalidPattern("The provided pattern does not match any known format.")
    assert invalid_pattern.msg == "The provided pattern does not match any known format."

def test_invalid_pattern_str():
    invalid_pattern = InvalidPattern("Missing required fields in the input data.")
    custom_error_string = invalid_pattern._fmt % {'msg': invalid_pattern.msg}