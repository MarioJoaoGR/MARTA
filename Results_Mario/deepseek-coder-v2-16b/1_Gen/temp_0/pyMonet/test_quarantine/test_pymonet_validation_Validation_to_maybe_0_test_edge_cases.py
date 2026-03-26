
import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

def test_to_maybe_success():
    val = Validation("Success", [])
    maybe_val = val.to_maybe()
    assert maybe_val.is_just(), "Expected a Just value"
    assert maybe_val.get_value() == "Success", "Expected the success value to be 'Success'"

def test_to_maybe_failure():
    val = Validation(None, ["Error occurred"])
    maybe_val = val.to_maybe()
    assert maybe_val.is_nothing(), "Expected a Nothing value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_maybe_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:9:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_edge_cases.py:10:11: E1101: Instance of 'Maybe' has no 'get_value' member (no-member)


"""