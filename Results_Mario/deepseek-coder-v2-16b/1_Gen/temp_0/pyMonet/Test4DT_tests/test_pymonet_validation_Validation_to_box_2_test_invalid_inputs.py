
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val_invalid_input = Validation('Success', [])
    
    # Check that errors are accumulated correctly
    assert len(val_invalid_input.errors) == 0, f"Expected no errors but got {len(val_invalid_input.errors)} errors."
