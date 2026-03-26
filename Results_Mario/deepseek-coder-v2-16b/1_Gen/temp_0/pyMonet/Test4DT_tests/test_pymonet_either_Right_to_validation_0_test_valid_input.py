
import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_valid_input():
    right = Right(value=42)  # Assuming some value is passed to Right constructor
    validation_monad = right.to_validation()
    
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value == 42
