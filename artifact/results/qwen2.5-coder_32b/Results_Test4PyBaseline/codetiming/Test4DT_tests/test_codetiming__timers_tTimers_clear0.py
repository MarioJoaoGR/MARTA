
# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections  # Importing the collections module

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert list(timers._timings.keys()) == []

def test_timers_record_times():
    timers = Timers()
    timers._timings['load_data'].append(0.5)
    timers._timings['process_data'].extend([1.2, 0.8])
    
    assert timers._timings['load_data'] == [0.5]
    assert timers._timings['process_data'] == [1.2, 0.8]

def test_timers_clear():
    timers = Timers()
    timers._timings['load_data'].append(0.5)
    timers._timings['process_data'].extend([1.2, 0.8])
    
    timers.clear()
    assert list(timers._timings.keys()) == []

def test_timers_empty_clear():
    timers = Timers()
    timers.clear()  # Clearing an already empty dictionary
    assert list(timers._timings.keys()) == []
