
import pytest
from dataclasses_json.utils import _is_new_type

def test_invalid_input():
    # Test with an integer (not a type)
    assert not _is_new_type(42)
    
    # Test with a string (not a type)
    assert not _is_new_type("test")
    
    # Test with a list (not a type)
    assert not _is_new_type([1, 2, 3])
    
    # Test with a dictionary (not a type)
    assert not _is_new_type({})
    
    # Test with None (not a type)
    assert not _is_new_type(None)
