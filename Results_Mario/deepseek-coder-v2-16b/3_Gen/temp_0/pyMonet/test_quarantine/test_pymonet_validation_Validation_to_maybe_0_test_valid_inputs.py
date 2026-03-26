
from pymonet.validation import Validation
from pymonet.maybe import Maybe
import pytest

def test_valid_inputs():
    # Create a Validation instance with a success value and no errors
    val = Validation("Success", [])
    
    # Convert the Validation to Maybe
    maybe_val = val.to_maybe()
    
    # Check if the Maybe is just (has a value)
    assert maybe_val.is_just(), "Expected Maybe to be just"
    
    # Get the value from the Maybe and check it
    assert maybe_val.get_value() == "Success", "Expected value 'Success' but got something else"

def test_invalid_inputs():
    # Create a Validation instance with an error
    val = Validation(None, ["Error occurred"])
    
    # Convert the Validation to Maybe
    maybe_val = val.to_maybe()
    
    # Check if the Maybe is nothing (has no value)
    assert maybe_val.is_nothing(), "Expected Maybe to be nothing"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:14:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_valid_inputs.py:17:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)


"""