
import pytest
from codetiming import Timers

def test_apply_function():
    timers = Timers()
    timers._timings['test_timer'] = [1.0, 2.0, 3.0]
    
    result = timers.apply(lambda x: sum(x), 'test_timer')
    assert result == 6.0

def test_apply_function_missing_timer():
    timers = Timers()
    
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'non_existent_timer')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_0_test_error_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_error_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""