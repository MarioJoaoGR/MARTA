
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test None input
    val_none = Validation(None, [None])
    assert val_none.value is None
    assert len(val_none.errors) == 1
    
    # Test empty list input
    val_empty_list = Validation([], [])
    assert val_empty_list.value == []
    assert len(val_empty_list.errors) == 0
    
    # Test boundary values (e.g., minimum and maximum values for different types)
    val_boundary_int = Validation(0, [])
    assert val_boundary_int.value == 0
    assert len(val_boundary_int.errors) == 0
    
    val_boundary_float = Validation(0.0, [])
    assert val_boundary_float.value == 0.0
    assert len(val_boundary_float.errors) == 0
    
    val_boundary_str = Validation("", [])
    assert val_boundary_str.value == ""
    assert len(val_boundary_str.errors) == 0
