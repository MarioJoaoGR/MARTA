
import pytest
from dataclasses_json.utils import _is_counter, _get_type_origin
from collections import Counter

def test_invalid_input():
    # Test with None input
    assert not _is_counter(None)
    
    # Test with an integer input
    assert not _is_counter(123)
    
    # Test with a string input
    assert not _is_counter("string")
    
    # Test with a list input
    assert not _is_counter([1, 2, 3])
    
    # Test with a custom class that does not inherit from Counter
    class NotACounter:
        pass
    
    assert not _is_counter(NotACounter)
