
import pytest
from codetiming._timers import Timers
import time

# Test initialization of Timers class
def test_init():
    timers = Timers()
    assert isinstance(timers, Timers), "Timers instance should be an instance of Timers"
    assert hasattr(timers, '_timings'), "_timings attribute not found in Timers instance"
    assert isinstance(timers._timings, dict), "_timings should be a dictionary"

# Test max method with no timings available
def test_max_no_timings():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.max("non_existent_name")

# Test max method with existing timings
def test_max_with_timings():
    timers = Timers()
    # Add some timing data
    timers._timings["test_timer"] = [1.0, 2.0, 3.0]
    assert timers.max("test_timer") == 3.0, "Maximal value should be 3.0"

# Test max method with multiple timings
def test_max_multiple_timings():
    timers = Timers()
    # Add some timing data
    timers._timings["test_timer"] = [1.5, 2.5, 3.5]
    assert timers.max("test_timer") == 3.5, "Maximal value should be 3.5"

# Test max method with negative timings
def test_max_negative_timings():
    timers = Timers()
    # Add some timing data
    timers._timings["test_timer"] = [-1.0, -2.0, -3.0]
    assert timers.max("test_timer") == -1.0, "Maximal value should be -1.0"

# Test max method with mixed positive and negative timings
def test_max_mixed_timings():
    timers = Timers()
    # Add some timing data
    timers._timings["test_timer"] = [-1.5, 2.5, -3.5]
    assert timers.max("test_timer") == 2.5, "Maximal value should be 2.5"
