# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections
import statistics
import math

# Test initialization of Timers class with default values
def test_timers_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings['example_timer'], list)

# Test adding a new timing to the Timers instance
def test_add_timing():
    timers = Timers()
    timers._timings['test_timing'] = [10, 20, 30]
    assert len(timers._timings['test_timing']) == 3
    assert timers._timings['test_timing'] == [10, 20, 30]

# Test calculating standard deviation with valid data
def test_stdev_valid():
    timers = Timers()
    timers._timings['example_timer'] = [10, 20, 30]
    assert math.isclose(timers.stdev('example_timer'), statistics.stdev([10, 20, 30]), abs_tol=0.0001)

# Test calculating standard deviation with insufficient data
def test_stdev_insufficient_data():
    timers = Timers()
    timers._timings['example_timer'] = [10]
    assert math.isnan(timers.stdev('example_timer'))

# Test calculating standard deviation with non-existing timer
def test_stdev_non_existing_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('nonexistent_timer')
