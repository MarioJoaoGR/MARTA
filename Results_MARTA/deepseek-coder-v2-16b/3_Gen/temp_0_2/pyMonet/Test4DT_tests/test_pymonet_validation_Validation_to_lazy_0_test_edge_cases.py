
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test with None value
    val_none = Validation(None, ['Error message'])
    assert val_none.value is None
    assert val_none.errors == ['Error message']
    
    # Test with empty list as errors
    val_empty = Validation('', [])
    assert val_empty.value == ''
    assert val_empty.errors == []
    
    # Test with boundary values (e.g., non-empty strings, lists)
    val_boundary = Validation('test', ['Another error'])
    assert val_boundary.value == 'test'
    assert val_boundary.errors == ['Another error']
