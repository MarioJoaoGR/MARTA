
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_invalid_input():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['invalid'] = 123  # This should raise a TypeError as per the function definition

def test_clear_method():
    timers = Timers()
    timers._timings['task1'] = [1.0, 2.0, 3.0]
    assert len(timers._timings) == 1
    timers.clear()
    assert len(timers._timings) == 0

def test_apply_function():
    def mean_func(values):
        return sum(values) / len(values)

    timers = Timers()
    timers._timings['task1'] = [1.0, 2.0, 3.0]
    result = timers.apply(mean_func, 'task1')
    assert result == 2.0

def test_retrieve_statistics():
    timers = Timers()
    timers._timings['task1'] = [1.0, 2.0, 3.0]
    assert timers.mean('task1') == 2.0
    assert timers.median('task1') == 2.0
    assert timers.min('task1') == 1.0
    assert timers.max('task1') == 3.0
