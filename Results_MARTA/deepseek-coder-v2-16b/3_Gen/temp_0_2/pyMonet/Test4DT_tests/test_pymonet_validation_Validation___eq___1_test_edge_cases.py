
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test with None value
    val_none = Validation(None, ['Initial error'])
    assert val_none.value is None
    assert val_none.errors == ['Initial error']
    
    # Test with empty list as errors
    val_empty = Validation('', [])
    assert val_empty.value == ''
    assert val_empty.errors == []
    
    # Test with boundary value (100) and no initial errors
    val_boundary = Validation(100, [])
    assert val_boundary.value == 100
    assert val_boundary.errors == []
