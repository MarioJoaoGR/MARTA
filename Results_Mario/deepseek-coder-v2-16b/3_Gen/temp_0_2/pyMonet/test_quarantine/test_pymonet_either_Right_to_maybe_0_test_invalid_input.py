
import pytest
from pymonet.either import Right

def test_invalid_input():
    with pytest.raises(TypeError):
        Right().to_maybe()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_to_maybe_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Right_to_maybe_0_test_invalid_input.py:7:8: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""