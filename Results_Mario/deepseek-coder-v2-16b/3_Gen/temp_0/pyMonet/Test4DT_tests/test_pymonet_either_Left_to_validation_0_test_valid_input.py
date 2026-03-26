
from pymonet.either import Left  # Correctly import the Left class from the appropriate module
import pytest

def test_valid_input():
    left_instance = Left("some error message")  # Create an instance of Left with a sample error message
    validation_result = left_instance.to_validation()
    
    assert not validation_result.is_success(), "Expected the Validation to be failed"
    assert validation_result.errors == ["some error message"], "Expected the errors list to contain the initial error message"
