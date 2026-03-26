
import pytest
from string_utils import validation

def test_invalid_type():
    # Test with None (not a string)
    assert not validation.is_string(None)
    
    # Test with list (not a string)
    assert not validation.is_string([1, 2, 3])
    
    # Add more invalid type tests if necessary
