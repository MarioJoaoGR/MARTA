
import pytest
from codetiming import Timers

def test_valid_input():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['timer_name'] = 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___setitem___0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers___setitem___0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""