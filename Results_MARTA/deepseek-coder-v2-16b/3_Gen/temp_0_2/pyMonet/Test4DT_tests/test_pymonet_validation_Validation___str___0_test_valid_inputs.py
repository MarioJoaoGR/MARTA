
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(10, [])
    assert str(val) == 'Validation.success[10]'
    
    val_with_error = Validation(None, ['Error message'])
    assert str(val_with_error) == 'Validation.fail[None, [\'Error message\']]'
