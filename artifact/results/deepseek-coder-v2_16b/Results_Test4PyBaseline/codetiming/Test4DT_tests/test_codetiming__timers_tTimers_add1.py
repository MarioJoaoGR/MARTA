
import pytest
from codetiming._timers import Timers
import collections

# Test initialization with default arguments
def test_init_default():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert timers._timings == {}

# Test adding a timing value to an existing timer
@pytest.fixture
def setup_timers():
    timers = Timers()
    timers.add("test_timer", 1.0)
    return timers

def test_add(setup_timers):
    assert "test_timer" in setup_timers._timings
    assert len(setup_timers._timings["test_timer"]) == 1
    assert setup_timers._timings["test_timer"][0] == 1.0

# Test adding a timing value to a new timer
def test_add_new_timer():
    timers = Timers()
    timers.add("new_timer", 2.0)
    assert "new_timer" in timers._timings
    assert len(timers._timings["new_timer"]) == 1
    assert timers._timings["new_timer"][0] == 2.0

# Test adding multiple timing values to the same timer
def test_add_multiple_values():
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 3.0)
    assert "test_timer" in timers._timings
    assert len(timers._timings["test_timer"]) == 2
    assert timers._timings["test_timer"] == [1.0, 3.0]

# Test adding a timing value to the data dictionary
def test_add_to_data():
    timers = Timers()
    timers.add("test_timer", 1.0)
    assert "test_timer" in timers.data
    assert timers.data["test_timer"] == 1.0

# Test adding multiple timing values to the data dictionary
def test_add_multiple_to_data():
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 3.0)
    assert "test_timer" in timers.data
    assert timers.data["test_timer"] == 4.0
