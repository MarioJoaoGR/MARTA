
import pytest
from codetiming._timers import Timers
import collections

# Test initialization with default parameters
def test_init_default():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert hasattr(timers, '_timings')
    assert isinstance(timers._timings, collections.defaultdict)

# Test clear method
def test_clear():
    timers = Timers()
    # Initially, the _timings dictionary should be empty
    assert len(timers._timings) == 0
    
    # After adding some data, calling clear should remove it
    timers.data = {'example': [1, 2, 3]}
    timers._timings = {'example': [4, 5, 6]}
    timers.clear()
    assert len(timers.data) == 0
    assert len(timers._timings) == 0

# Test clear method with no data initially
def test_clear_no_initial_data():
    timers = Timers()
    # Initially, the _timings dictionary should be empty
    assert len(timers.data) == 0
    assert len(timers._timings) == 0
    
    # Calling clear when there's no data should not raise an error or change anything
    timers.clear()
    assert len(timers.data) == 0
    assert len(timers._timings) == 0
