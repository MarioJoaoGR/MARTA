
import pytest
from codetiming import Timers
import statistics

def test_edge_case():
    timers = Timers()
    
    # Test mean on non-existing timer
    with pytest.raises(KeyError):
        timers.mean("non_existing_timer")
    
    # Test apply on non-existing timer
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "non_existing_timer")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_1_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_1_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""