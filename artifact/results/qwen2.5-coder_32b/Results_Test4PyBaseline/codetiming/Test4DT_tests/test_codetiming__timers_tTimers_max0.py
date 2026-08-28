# Module: codetiming._timers
import pytest
from codetiming._timers import Timers

def test_max_with_predefined_timings():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.max('example_timer') == 5.6

def test_max_with_empty_list_of_timings():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.max('empty_timer') == 0.0

def test_max_with_multiple_timers():
    timers = Timers()
    timers._timings['timer1'] = [2.5, 4.8]
    timers._timings['timer2'] = [1.1, 6.7, 3.3]
    
    assert timers.max('timer1') == 4.8
    assert timers.max('timer2') == 6.7

def test_max_with_single_timing():
    timers = Timers()
    timers._timings['single_timer'] = [0.9]
    assert timers.max('single_timer') == 0.9

def test_max_with_negative_timings():
    timers = Timers()
    timers._timings['negative_timer'] = [-1.2, -3.4, -5.6]
    assert timers.max('negative_timer') == -1.2

def test_max_raises_key_error_for_nonexistent_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.max('non_existent_timer')
