
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test None input
    val_none = Validation(None, ['Error 1'])
    assert len(val_none.errors) == 1
    assert val_none.value is None

    # Test empty list for errors
    val_empty_errors = Validation("Success", [])
    assert not val_empty_errors.errors
    assert val_empty_errors.value == "Success"

    # Test boundary values
    val_boundary = Validation(1, ['Error 2'])
    assert val_boundary.value == 1
    assert len(val_boundary.errors) == 1
