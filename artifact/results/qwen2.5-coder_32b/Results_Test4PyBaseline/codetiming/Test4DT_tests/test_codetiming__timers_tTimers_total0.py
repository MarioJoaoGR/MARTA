
# Module: codetiming._timers
import pytest
from collections import defaultdict
from codetiming._timers import Timers

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert list(timers._timings.keys()) == []

def test_total_with_existing_timer():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.total('example_timer') == pytest.approx(10.2)

def test_total_with_non_existent_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.total('non_existent_timer')

def test_total_with_empty_timer_list():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.total('empty_timer') == 0.0

def test_total_with_single_entry():
    timers = Timers()
    timers._timings['single_entry_timer'] = [2.5]
    assert timers.total('single_entry_timer') == pytest.approx(2.5)

def test_total_with_multiple_timers():
    timers = Timers()
    timers._timings['timer1'] = [1.0, 2.0]
    timers._timings['timer2'] = [3.0, 4.0]
    assert timers.total('timer1') == pytest.approx(3.0)
    assert timers.total('timer2') == pytest.approx(7.0)

def test_total_with_negative_times():
    timers = Timers()
    timers._timings['negative_timer'] = [-1.5, -2.5]
    assert timers.total('negative_timer') == pytest.approx(-4.0)
