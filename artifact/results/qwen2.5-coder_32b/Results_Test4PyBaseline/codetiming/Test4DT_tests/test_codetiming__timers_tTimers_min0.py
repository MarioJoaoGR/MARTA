
import pytest
from codetiming._timers import Timers

def test_min_with_existing_timings():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.min('example_timer') == 1.2

def test_min_with_single_timing():
    timers = Timers()
    timers._timings['example_timer'] = [0.7]
    assert timers.min('example_timer') == 0.7

def test_min_with_no_timings():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.min('empty_timer') == 0.0

def test_min_with_non_existent_key():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.min('non_existent_timer')

def test_min_with_negative_timings():
    timers = Timers()
    timers._timings['negative_timer'] = [-1.2, -3.4, -5.6]
    assert timers.min('negative_timer') == -5.6

def test_min_with_mixed_positive_and_negative_timings():
    timers = Timers()
    timers._timings['mixed_timer'] = [1.2, -3.4, 0.0]
    assert timers.min('mixed_timer') == -3.4
