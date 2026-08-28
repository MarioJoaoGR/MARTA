
import pytest
from codetiming._timers import Timers

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert not timers._timings

def test_add_timing():
    timers = Timers()
    timers.add('load_data', 0.5)
    assert 'load_data' in timers._timings
    assert timers._timings['load_data'] == [0.5]

def test_add_multiple_timings():
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 0.3)
    assert timers._timings['load_data'] == [0.5, 0.3]

def test_total_time():
    timers = Timers()
    timers.add('process_data', 1.2)
    timers.add('process_data', 0.8)
    assert timers.total('process_data') == pytest.approx(2.0)

def test_count_timings():
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 0.3)
    assert timers.count('load_data') == 2

def test_mean_time():
    timers = Timers()
    timers.add('process_data', 1.2)
    timers.add('process_data', 0.8)
    assert timers.mean('process_data') == pytest.approx(1.0)

def test_mean_no_timings():
    timers = Timers()