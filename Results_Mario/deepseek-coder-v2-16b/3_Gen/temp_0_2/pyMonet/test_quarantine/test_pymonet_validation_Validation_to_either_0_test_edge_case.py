
from pymonet.validation import Validation
from pymonet.either import Left, Right
import pytest

def test_edge_case():
    # Create a Validation instance with a value and no errors
    val = Validation(10, [])
    
    # Convert to Either
    either_val = val.to_either()
    
    # Check if the conversion is correct
    assert isinstance(either_val, Right)
    assert either_val.get_value() == 10

    # Add an error and check again
    val.add_error("An error occurred")
    either_val = val.to_either()
    
    assert isinstance(either_val, Left)
    assert either_val.get_error() == ["An error occurred"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_to_either_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_edge_case.py:15:11: E1101: Instance of 'Left' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_edge_case.py:15:11: E1101: Instance of 'Right' has no 'get_value' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_edge_case.py:18:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_edge_case.py:22:11: E1101: Instance of 'Left' has no 'get_error' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_either_0_test_edge_case.py:22:11: E1101: Instance of 'Right' has no 'get_error' member (no-member)


"""