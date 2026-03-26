
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalidpattern_equality():
    # Create two instances of InvalidPattern with different messages
    invalid_pattern1 = InvalidPattern("First message")
    invalid_pattern2 = InvalidPattern("Second message")
    
    # Check that they are not equal if their messages are different
    assert invalid_pattern1 != invalid_pattern2
    
    # Create another instance of InvalidPattern with the same message
    invalid_pattern3 = InvalidPattern("First message")
    
    # Check that instances with the same message are equal
    assert invalid_pattern1 == invalid_pattern3
