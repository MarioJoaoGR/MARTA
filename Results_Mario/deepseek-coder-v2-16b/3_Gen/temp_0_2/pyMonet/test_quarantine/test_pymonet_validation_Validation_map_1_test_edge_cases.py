
from pymonet.validation import Validation
import pytest

def test_map():
    # Create a Validation instance with an initial value and empty list of errors
    val = Validation(10, [])
    
    # Applying a mapping function that squares the value
    mapped_val = val.map(lambda x: x * x)
    assert mapped_val.value == 100
    assert len(mapped_val.errors) == 0
    
    # Adding an error to the Validation instance
    val.add_error("Value is too high")
    
    # Applying a mapping function that does not change the value but adds an error message
    mapped_val = val.map(lambda x: x)
    assert mapped_val.value is None
    assert len(mapped_val.errors) == 1
    assert mapped_val.errors[0] == "Value is too high"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_map_1_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_map_1_test_edge_cases.py:15:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""