# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections

# Test initialization with default values
def test_init():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert timers._timings == collections.defaultdict(list)

# Test adding a new timing
def test_add_timing():
    timers = Timers()
    timers._timings["operation1"].append(0.5)
    assert len(timers._timings["operation1"]) == 1
    assert timers._timings["operation1"][0] == 0.5

# Test applying a function to timings
def test_apply():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "operation1")
    timers._timings["operation1"].append(0.5)
    result = timers.apply(lambda x: sum(x), "operation1")
    assert result == 0.5

# Test counting timings
def test_count():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.count("operation1")
    timers._timings["operation1"].append(0.5)
    count = timers.count("operation1")
    assert count == 1
