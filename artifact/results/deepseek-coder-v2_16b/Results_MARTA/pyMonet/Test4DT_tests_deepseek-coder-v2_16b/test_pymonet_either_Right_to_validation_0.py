
import pytest
from pymonet.either import Right
from pymonet.validation import Validation

# Test valid input where Right is not empty and has a valid value
def test_valid_input():
    right_instance = Right(10)  # Create an instance of Right with a value of 10
    validation_monad = right_instance.to_validation()  # Call the to_validation method
    assert isinstance(validation_monad, Validation)  # Assert that the result is a Validation object
    assert validation_monad.value == 10

# Test invalid input where Right contains an invalid value (string in this case)
def test_invalid_input():
    right_instance = Right('string')  # Create an instance of Right with a string value
    validation_monad = right_instance.to_validation()  # Call the to_validation method
    assert isinstance(validation_monad, Validation)  # Assert that the result is a Validation object
    assert validation_monad.value == 'string'
