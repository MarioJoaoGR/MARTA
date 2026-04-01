
import pytest
from dataclasses_json.utils import _isinstance_safe

def test_invalid_inputs():
    # Test with None as input
    assert not _isinstance_safe(None, int), "Expected False for None and int"
    
    # Test with string as input but checking against float type
    assert not _isinstance_safe("hello", float), "Expected False for string and float"
    
    # Test with list as input but checking against tuple type
    assert not _isinstance_safe([1, 2, 3], tuple), "Expected False for list and tuple"
    
    # Additional test cases to ensure robustness
    assert not _isinstance_safe(42, str), "Expected False for int and str"
    assert not _isinstance_safe("world", list), "Expected False for string and list"
