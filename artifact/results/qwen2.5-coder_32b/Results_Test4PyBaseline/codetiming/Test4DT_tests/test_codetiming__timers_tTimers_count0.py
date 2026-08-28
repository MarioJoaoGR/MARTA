
# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections  # Importing the collections module

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert list(timers._timings.keys()) == []

def test_count_with_existing_timer():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.count('example_timer') == 3

def test_count_with_nonexistent_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.count('non_existent_timer')

def test_count_after_adding_timings():
    timers = Timers()
    timers._timings['load_data'].append(0.5)
    assert timers.count('load_data') == 1
    timers._timings['load_data'].append(0.3)
    assert timers.count('load_data') == 2

def test_count_with_empty_timings():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.count('empty_timer') == 0
