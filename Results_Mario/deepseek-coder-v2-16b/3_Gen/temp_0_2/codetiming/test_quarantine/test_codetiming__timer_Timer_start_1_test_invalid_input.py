
import pytest
from codetiming import Timer
import time

def test_invalid_input():
    timer = Timer()
    with pytest.raises(TypeError):  # Since start does not take any parameters, passing a parameter will raise TypeError
        timer.start(1)  # This should raise an error because the method does not accept arguments

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_start_1_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_invalid_input.py:9:8: E1121: Too many positional arguments for method call (too-many-function-args)


"""