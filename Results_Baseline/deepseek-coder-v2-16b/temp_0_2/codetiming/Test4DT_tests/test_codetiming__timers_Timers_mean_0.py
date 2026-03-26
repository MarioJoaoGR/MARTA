# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections
import statistics

# Fixture to create an instance of Timers for each test
@pytest.fixture
def timers():
    return Timers()

def test_init(timers):
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers._timings['default'], list)

def test_mean_no_data(timers):
    with pytest.raises(KeyError):
        timers.mean("non_existent")

def test_mean_with_data(timers):
    timers._timings["operation1"].append(0.5)
    assert timers.mean("operation1") == 0.5

def test_mean_empty_list(timers):
    timers._timings["empty_op"] = []
    assert timers.mean("empty_op") == 0

def test_mean_multiple_values(timers):
    timers._timings["multi_op"].extend([1, 2, 3])
    assert timers.mean("multi_op") == 2

if __name__ == "__main__":
    pytest.main()
