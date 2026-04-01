
import pytest
from pytutils.timers import Timer

def test_timer():
    with Timer(name='test_operation', verbose=True) as t:
        # Simulate a long operation by sleeping for a short period
        import time
        time.sleep(0.1)
    
    assert t.elapsed_time > 0, "Elapsed time should be greater than zero"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_timers_Timer___init___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_timers_Timer___init___0_test_edge_cases.py:11:11: E1101: Instance of 'Timer' has no 'elapsed_time' member (no-member)


"""