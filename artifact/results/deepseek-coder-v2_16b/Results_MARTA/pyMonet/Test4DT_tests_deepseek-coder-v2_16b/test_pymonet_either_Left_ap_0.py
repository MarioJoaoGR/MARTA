
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    left_instance = Left("An error occurred")
    validation_monad = left_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.errors == ['An error occurred']

# Test invalid input to ensure it raises TypeError