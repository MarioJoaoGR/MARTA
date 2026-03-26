
# Module: codetiming._timers
import pytest
from codetiming import Timers  # Corrected import statement
import collections

# Test initialization of Timers class
def test_timers_init():
    timers = Timers()  # Corrected instantiation
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers.data, dict)

# Test adding a timing value to a new timer
def test_add_new_timer():
    timers = Timers()  # Corrected instantiation
    timers.add('test_timer', 1.0)  # Corrected method call
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 1
    assert timers.data['test_timer'] == 1.0

# Test adding a timing value to an existing timer
def test_add_existing_timer():
    timers = Timers()  # Corrected instantiation
    timers.add('test_timer', 1.0)  # Corrected method call
    timers.add('test_timer', 2.0)  # Corrected method call
    assert len(timers._timings['test_timer']) == 2
    assert timers.data['test_timer'] == 3.0

# Test adding a timing value with invalid name (non-string type)
def test_add_invalid_name():
    timers = Timers()  # Corrected instantiation
    with pytest.raises(TypeError):
        timers.add(123, 1.0)  # Invalid name type

# Test adding a timing value with invalid value (non-float type)
def test_add_invalid_value():
    timers = Timers()  # Corrected instantiation
    with pytest.raises(TypeError):
        timers.add('test_timer', 'not_a_float')  # Invalid value type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0.py:4:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""