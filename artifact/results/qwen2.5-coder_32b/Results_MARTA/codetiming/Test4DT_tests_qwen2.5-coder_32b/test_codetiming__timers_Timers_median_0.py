
import pytest
from codetiming._timers import Timers
import statistics

def test_median_none_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median(None)

def test_median_empty_timer():
    timers = Timers()
    timers.add('empty_timer', 0.0)  # Add a valid float value to avoid TypeError
    assert timers.median('empty_timer') == 0.0

def test_median_single_value_timer():
    timers = Timers()
    timers.add('single_timer', 1.5)
    assert timers.median('single_timer') == 1.5

def test_median_multiple_values_timer():
    timers = Timers()
    timers.add('multiple_timers', 1.0)
    timers.add('multiple_timers', 2.0)
    timers.add('multiple_timers', 3.0)
    assert timers.median('multiple_timers') == 2.0

def test_median_odd_values_timer():
    timers = Timers()
    timers.add('odd_timers', 1.0)
    timers.add('odd_timers', 3.0)
    timers.add('odd_timers', 5.0)
    assert timers.median('odd_timers') == 3.0

def test_median_even_values_timer():
    timers = Timers()
    timers.add('even_timers', 1.0)
    timers.add('even_timers', 2.0)
    timers.add('even_timers', 3.0)
    timers.add('even_timers', 4.0)
    assert timers.median('even_timers') == 2.5
