
import pytest
from codetiming._timers import Timers  # Corrected import path
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_with_empty_timings(timers):
    with pytest.raises(KeyError):
        timers.mean("non_existent_timer")

def test_mean_with_single_timing(timers):
    timers._timings["example_timer"] = [10]
    assert timers.mean("example_timer") == 10

def test_mean_with_multiple_timings(timers):
    timers._timings["example_timer"] = [10, 20, 30]
    assert timers.mean("example_timer") == statistics.mean([10, 20, 30])
