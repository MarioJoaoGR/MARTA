
import pytest
from codetiming import Timers

def test_apply_valid_case():
    timers = Timers()
    timers._timings['operation1'] = [0.1, 0.2, 0.3]
    
    result = timers.apply(lambda x: sum(x), 'operation1')
    assert result == pytest.approx(0.6)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_0_test_valid_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_valid_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""