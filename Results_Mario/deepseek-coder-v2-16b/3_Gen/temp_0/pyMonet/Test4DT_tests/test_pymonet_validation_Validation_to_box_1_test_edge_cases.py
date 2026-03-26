
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test with None value
    val_none = Validation(None, ['Error 1'])
    assert len(val_none.errors) == 1
    assert val_none.errors[0] == 'Error 1'
    
    # Test with empty list as value
    val_empty = Validation([], [])
    assert isinstance(val_empty.value, list) and not val_empty.value
    assert len(val_empty.errors) == 0
    
    # Test with boundary value
    val_boundary = Validation('Boundary', [])
    assert val_boundary.value == 'Boundary'
    assert len(val_boundary.errors) == 0
