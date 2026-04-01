
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_none_input():
    # Create an instance of InvalidPattern with None input
    invalid_pattern = InvalidPattern(None)
    
    # Check that the instance is equal to another instance created with None input
    assert invalid_pattern == InvalidPattern(None)
