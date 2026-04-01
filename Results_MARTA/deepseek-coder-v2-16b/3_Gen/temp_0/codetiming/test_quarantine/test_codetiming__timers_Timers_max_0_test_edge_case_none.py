
import pytest
from codetiming import Timers

def test_max_edge_case_none():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.max('non_existent_timer')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_max_0_test_edge_case_none
codetiming/Test4DT_tests/test_codetiming__timers_Timers_max_0_test_edge_case_none.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""