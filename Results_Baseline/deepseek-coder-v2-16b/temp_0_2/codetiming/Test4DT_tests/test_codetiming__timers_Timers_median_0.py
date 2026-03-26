
import pytest
from codetiming._timers import Timers
import time
import statistics
import collections

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert len(timers._timings) == 0

# Test apply method with a lambda function to sum the timings
def test_apply():
    timers = Timers()
    timers._timings["test"].append(1.0)
    result = timers.apply(lambda x: sum(x), "test")
    assert result == 1.0

# Test median method to check if it computes the median correctly
def test_median():
    timers = Timers()
    timers._timings["test"].extend([1.0, 2.0, 3.0])
    median_value = timers.median("test")