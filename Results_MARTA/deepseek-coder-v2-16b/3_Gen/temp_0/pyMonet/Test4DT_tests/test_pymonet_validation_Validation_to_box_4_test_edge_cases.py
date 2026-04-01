
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test with None value
    val_none = Validation(None, ['Error 1'])
    assert len(val_none.errors) == 1
    
    # Test with empty list value
    val_empty = Validation('', [])
    assert len(val_empty.errors) == 0
    
    # Test with boundary value
    val_boundary = Validation('Boundary', [])
    assert val_boundary.value == 'Boundary'
