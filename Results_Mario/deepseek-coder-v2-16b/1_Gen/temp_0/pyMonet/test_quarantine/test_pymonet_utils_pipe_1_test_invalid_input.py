
import pytest
from pymonet.utils import pipe
from functools import reduce

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where value is not provided
        pipe()
        
    with pytest.raises(TypeError):
        # Test case where functions are not provided
        pipe(5)
        
    with pytest.raises(TypeError):
        # Test case where both value and functions are not provided
        pipe()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_pipe_1_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_utils_pipe_1_test_invalid_input.py:9:8: E1120: No value for argument 'value' in function call (no-value-for-parameter)
pyMonet/Test4DT_tests/test_pymonet_utils_pipe_1_test_invalid_input.py:17:8: E1120: No value for argument 'value' in function call (no-value-for-parameter)


"""