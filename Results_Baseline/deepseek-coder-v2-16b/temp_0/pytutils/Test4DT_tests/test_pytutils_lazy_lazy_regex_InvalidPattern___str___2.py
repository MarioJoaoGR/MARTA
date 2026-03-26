
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

# Test cases for the InvalidPattern class
def test_invalid_pattern_init():
    invalid_pattern = InvalidPattern("The provided pattern does not match any known format.")
    assert invalid_pattern.msg == "The provided pattern does not match any known format."

def test_invalid_pattern_str():
    invalid_pattern = InvalidPattern("Missing required fields in the input data.")
    expected_output = "Invalid pattern(s) found. Missing required fields in the input data."