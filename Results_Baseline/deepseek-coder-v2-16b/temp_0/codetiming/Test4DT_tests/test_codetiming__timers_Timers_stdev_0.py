
import pytest
from unittest.mock import patch, MagicMock
import collections
import statistics
import math
from codetiming._timers import Timers

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings['default'], list)

# Test adding a new timer
def test_add_new_timer():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert 'example_timer' in timers._timings
    assert len(timers._timings['example_timer']) == 3

# Test adding an existing timer
def test_add_existing_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent_timer')

# Test calculating standard deviation with insufficient data
def test_stdev_insufficient_data():
    timers = Timers()
    timers._timings['example_timer'] = [1.2]
    with pytest.raises(ValueError):
        raise ValueError("Insufficient data for calculation")

# Test calculating standard deviation with sufficient data
def test_stdev_sufficient_data():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert math.isclose(timers.stdev('example_timer'), statistics.stdev([1.2, 3.4, 5.6]), abs_tol=0.001)
