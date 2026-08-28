
# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test creating a successful Validation instance
def test_successful_validation():
    val_success = Validation(10, [])
    assert val_success.value == 10
    assert not val_success.is_fail()

# Test creating a failed Validation instance with an error message
def test_failed_validation():
    val_failure = Validation(None, ['Error message'])
    assert val_failure.errors == ['Error message']
    assert val_failure.is_fail()

# Test checking if the validation is successful and handling it accordingly
def test_check_success_and_handle():
    val_success = Validation(10, [])
    val_failure = Validation(None, ['Error message'])
    
    if val_success.is_fail():
        pytest.fail("Expected validation to be successful")
    else:
        assert val_success.value == 10
    
    if not val_failure.is_fail():
        pytest.fail("Expected validation to be failed")
    else:
        assert val_failure.errors == ['Error message']

# Test transforming the Validation into different monad types (if applicable)
def test_transform_to_maybe():
    val_success = Validation(10, [])
    maybe_val = val_success.to_maybe()