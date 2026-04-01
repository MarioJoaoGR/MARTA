
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val_with_error = Validation('Failure', ['Error occurred'])
    
    assert not val_with_error.is_success(), "Expected validation to fail due to errors"
    assert len(val_with_error.errors) == 1, "Expected one error message in the list"
