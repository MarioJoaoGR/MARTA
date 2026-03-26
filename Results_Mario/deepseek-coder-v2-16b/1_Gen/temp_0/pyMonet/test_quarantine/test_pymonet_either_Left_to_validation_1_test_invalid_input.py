
from pymonet.validation import Left

def test_invalid_input():
    left_instance = Left()
    validation_result = left_instance.to_validation()
    assert not validation_result.is_success()
    assert validation_result.errors == [left_instance.value]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_to_validation_1_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Left_to_validation_1_test_invalid_input.py:2:0: E0611: No name 'Left' in module 'pymonet.validation' (no-name-in-module)


"""