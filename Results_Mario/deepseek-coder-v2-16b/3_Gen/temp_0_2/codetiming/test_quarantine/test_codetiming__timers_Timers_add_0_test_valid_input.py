
from codetiming import Timers
import pytest
from collections import defaultdict

def test_valid_input():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert isinstance(timers.data, dict)
    
    # Adding a valid timing value
    timers.add('test_timer', 1.23)
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 1
    assert timers._timings['test_timer'][0] == 1.23
    
    # Adding another timing value to the same timer
    timers.add('test_timer', 4.56)
    assert len(timers._timings['test_timer']) == 2
    assert timers._timings['test_timer'] == [1.23, 4.56]
    
    # Adding a timing value to a new timer
    timers.add('new_timer', 7.89)
    assert 'new_timer' in timers._timings
    assert len(timers._timings['new_timer']) == 1
    assert timers._timings['new_timer'][0] == 7.89
    
    # Ensuring the data dictionary is updated correctly
    assert timers.data['test_timer'] == pytest.approx(5.79)
    assert timers.data['new_timer'] == pytest.approx(7.89)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_valid_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""