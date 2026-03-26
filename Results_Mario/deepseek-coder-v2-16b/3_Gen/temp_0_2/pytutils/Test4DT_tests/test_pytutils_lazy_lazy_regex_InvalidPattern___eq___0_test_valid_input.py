
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    msg = "The provided pattern does not match any expected format."
    invalid_pattern = InvalidPattern(msg)
    
    # Create another instance of InvalidPattern with the same message for comparison
    another_invalid_pattern = InvalidPattern(msg)
    
    # Check if both instances are equal
    assert invalid_pattern == another_invalid_pattern
