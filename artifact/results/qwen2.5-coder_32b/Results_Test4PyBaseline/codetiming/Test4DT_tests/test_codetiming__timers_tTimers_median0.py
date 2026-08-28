# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import statistics

def test_median_with_single_value():
    timers = Timers()
    timers._timings['test_timer'].append(1.5)
    assert timers.median('test_timer') == 1.5

def test_median_with_multiple_values():
    timers = Timers()
    timers._timings['test_timer'] = [1.0, 2.0, 3.0]
    assert timers.median('test_timer') == 2.0

def test_median_with_even_number_of_values():
    timers = Timers()
    timers._timings['test_timer'] = [1.0, 2.0, 3.0, 4.0]
    assert timers.median('test_timer') == 2.5

def test_median_with_empty_list():
    timers = Timers()
    timers._timings['test_timer'] = []
    assert timers.median('test_timer') == 0.0

def test_median_with_no_timings():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')

def test_median_with_negative_values():
    timers = Timers()
    timers._timings['test_timer'] = [-1.5, -2.5, -3.5]
    assert timers.median('test_timer') == -2.5

def test_median_with_mixed_positive_and_negative_values():
    timers = Timers()
    timers._timings['test_timer'] = [-1.0, 0.0, 1.0]
    assert timers.median('test_timer') == 0.0
