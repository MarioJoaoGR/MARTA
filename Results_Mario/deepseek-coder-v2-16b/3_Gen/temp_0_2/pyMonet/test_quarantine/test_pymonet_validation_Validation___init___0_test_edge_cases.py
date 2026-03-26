
import pytest
from pymonet.validation import Validation

def test_apply_function():
    # Test when there are no errors
    val = Validation(10, [])
    mapped_val = val.apply_function(lambda x: x * 2)
    assert mapped_val.value == 20
    assert len(mapped_val.errors) == 0

    # Test when there are errors
    val = Validation(10, ['Error1'])
    mapped_val = val.apply_function(lambda x: x * 2)
    assert mapped_val is None
    assert val.errors == ['Error1']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation___init___0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___init___0_test_edge_cases.py:8:17: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_validation_Validation___init___0_test_edge_cases.py:14:17: E1101: Instance of 'Validation' has no 'apply_function' member (no-member)


"""