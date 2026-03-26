
# Module: codetiming._timers
import pytest
from codetiming import Timers

# Test initialization with default arguments
def test_init_default():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert timers._timings == {}

# Test initialization with custom logger function
def test_init_custom_logger():
    def custom_logger(message):
        print(f"LOG: {message}")
    timers = Timers(logger=custom_logger)
    assert isinstance(timers._timings, dict)
    assert timers._timings == {}

# Test adding a timing value to a new timer
def test_add_new_timer():
    timers = Timers()
    timers.add('test_timer', 1.0)
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 1
    assert timers._timings['test_timer'][0] == 1.0

# Test adding a timing value to an existing timer
def test_add_existing_timer():
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 2
    assert sum(timers._timings['test_timer']) == 3.0

# Test adding a timing value to multiple timers
def test_add_multiple_timers():
    timers = Timers()
    timers.add('timer1', 1.0)
    timers.add('timer2', 2.0)
    assert 'timer1' in timers._timings
    assert 'timer2' in timers._timings
    assert len(timers._timings['timer1']) == 1
    assert len(timers._timings['timer2']) == 1
    assert timers._timings['timer1'][0] == 1.0
    assert timers._timings['timer2'][0] == 2.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0.py:4:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""