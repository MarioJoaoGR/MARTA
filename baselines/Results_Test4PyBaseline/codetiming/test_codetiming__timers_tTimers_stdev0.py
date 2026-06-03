
import pytest
from codetiming._timers import Timers
import collections
import statistics
import math

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings['default'], list)

# Test stdev method with valid data
def test_stdev_valid():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0, 4.0]
    assert math.isnan(timers.stdev('example_timer')) is False
