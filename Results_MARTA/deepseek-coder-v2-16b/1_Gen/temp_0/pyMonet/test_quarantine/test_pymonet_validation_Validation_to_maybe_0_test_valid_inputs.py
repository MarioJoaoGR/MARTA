
import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

def test_valid_inputs():
    # Create a Validation instance with a success value and no errors
    val = Validation("Success", [])
    
    # Convert the Validation to Maybe
    maybe_val = val.to_maybe()
    
    # Check if the Maybe is just (has a value)
    assert maybe_val.is_just(), "Expected Maybe to be just with the success value"
    assert maybe_val.get_value() == "Success", "The value should match the initial success value"

    # Create a Validation instance with an error
    val_with_error = Validation(None, ["Error occurred"])
    
    # Convert the Validation to Maybe
    maybe_val_with_error = val_with_error.to_maybe()
    
    # Check if the Maybe is nothing (has no value)
    assert maybe_val_with_error.is_nothing(), "Expected Maybe to be nothing as there are errors"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:14:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:15:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)


"""