
import pytest
from codetiming._timers import Timers
import statistics

# Test cases for Timers class
def test_valid_median():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    median_time = timers.median('example_timer')
    assert median_time == 2.0

def test_edge_median():
    timers = Timers()
    timers._timings['example_edge_timer'] = []
    median_time = timers.median('example_edge_timer')
    assert median_time == 0

def test_invalid_median():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')
