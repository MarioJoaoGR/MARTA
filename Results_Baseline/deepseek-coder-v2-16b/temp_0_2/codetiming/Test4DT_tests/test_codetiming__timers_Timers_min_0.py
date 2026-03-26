# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections

# Test initialization of Timers instance
def test_init():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert hasattr(timers, '_timings')
    assert isinstance(timers._timings, collections.defaultdict)
    assert len(timers._timings) == 0

# Test adding timings to the timers dictionary
def test_add_timing():
    timers = Timers()
    timers._timings['test'].append(1.0)
    assert len(timers._timings['test']) == 1
    assert timers._timings['test'][0] == 1.0

# Test retrieving the minimal value from the timings list
def test_min():
    timers = Timers()
    timers._timings['test'].extend([2.0, 1.0, 3.0])
    assert timers.min('test') == 1.0

# Test applying a function to the timings list
def test_apply():
    timers = Timers()
    timers._timings['test'].extend([2.0, 1.0, 3.0])
    result = timers.apply(lambda values: min(values or [0]), name='test')
    assert result == 1.0

# Test applying a function to non-existing timings list
def test_apply_non_existing():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda values: min(values or [0]), name='nonexistent')
