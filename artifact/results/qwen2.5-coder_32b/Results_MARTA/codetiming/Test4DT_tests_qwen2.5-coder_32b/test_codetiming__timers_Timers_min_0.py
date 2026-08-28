
import pytest
from codetiming._timers import Timers


def test_min_with_single_valid_time():
    timers = Timers()
    timers._timings['valid_timer'] = [1.5]
    assert timers.min('valid_timer') == 1.5

def test_min_with_multiple_times():
    timers = Timers()
    timers._timings['multiple_timers'] = [2.0, 3.5, 1.0, 4.0]
    assert timers.min('multiple_timers') == 1.0

def test_min_with_empty_list():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.min('empty_timer') == 0.0
