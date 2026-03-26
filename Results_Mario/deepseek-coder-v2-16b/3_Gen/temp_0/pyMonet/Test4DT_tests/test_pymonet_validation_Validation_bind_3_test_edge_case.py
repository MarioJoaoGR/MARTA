
import pytest
from pymonet.validation import Validation

def test_edge_case():
    # Test with None value
    val_none = Validation(None, [''])
    assert len(val_none.errors) == 1
    assert val_none.value is None

    # Test with empty list as errors
    val_empty_errors = Validation("Success", [])
    assert not val_empty_errors.errors
    assert val_empty_errors.value == "Success"
