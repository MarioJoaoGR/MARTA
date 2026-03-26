
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test None value
    val_none = Validation(None, ['Error 1'])
    assert len(val_none.errors) == 1
    assert val_none.value is None

    # Test empty list for errors
    val_empty_errors = Validation("Success", [])
    assert not val_empty_errors.errors
    assert val_empty_errors.value == "Success"

    # Test boundary value with no initial errors
    val_no_initial_errors = Validation("Boundary Value", [])
    assert val_no_initial_errors.value == "Boundary Value"
    assert not val_no_initial_errors.errors
