
import pytest
from your_module import Right  # Replace 'your_module' with the actual module name where Right is defined

def test_valid_input():
    right_instance = Right(42)
    mapped_value = right_instance.bind(lambda x: x * 2)
    assert mapped_value == 84

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_bind_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_0_test_valid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""