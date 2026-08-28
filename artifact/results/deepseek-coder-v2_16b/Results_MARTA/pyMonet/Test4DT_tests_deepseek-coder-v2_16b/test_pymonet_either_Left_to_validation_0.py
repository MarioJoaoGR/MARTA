
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    left_instance = Left(value='An error occurred')
    validation_monad = left_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.errors == ['An error occurred']

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case_none():
    left_instance = Left(value=None)
    validation_monad = left_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.errors == [None]

# Test invalid input where Maybe is nothing (is_nothing is True)
def test_invalid_input():
    left_instance = Left(value='Another error occurred')
    validation_monad = left_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.errors == ['Another error occurred']
