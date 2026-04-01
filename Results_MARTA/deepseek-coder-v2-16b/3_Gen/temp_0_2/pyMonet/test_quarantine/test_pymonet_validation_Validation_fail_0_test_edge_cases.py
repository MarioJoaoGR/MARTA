
import pytest
from pymonet.validation import Validation

def test_add_error():
    val = Validation(10, [])
    assert val.value == 10
    assert len(val.errors) == 0
    
    val.add_error("Value is too high")
    assert len(val.errors) == 1
    assert val.errors[0] == "Value is too high"

def test_fail():
    failed_val = Validation.fail(["Error 1", "Error 2"])
    assert failed_val.value is None
    assert failed_val.errors == ["Error 1", "Error 2"]

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_validation_Validation_fail_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_validation_Validation_fail_0_test_edge_cases.py:10:4: E1101: Instance of 'Validation' has no 'add_error' member (no-member)


"""