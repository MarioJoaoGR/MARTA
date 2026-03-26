
import pytest
from pytutils.timers import Timer

def test_invalid_input():
    with pytest.raises(TypeError):
        Timer(name="test", verbose=True, extra="argument")  # Providing an extra argument should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_timers_Timer___enter___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0_test_invalid_input.py:7:8: E1123: Unexpected keyword argument 'extra' in constructor call (unexpected-keyword-arg)


"""