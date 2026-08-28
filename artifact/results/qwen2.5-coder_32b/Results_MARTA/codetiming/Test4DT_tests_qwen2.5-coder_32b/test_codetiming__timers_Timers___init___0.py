
import pytest
from codetiming._timers import Timers


def test_add_single_time_entry():
    """Test adding a single time entry to a timer."""
    timers = Timers()
    timers.add('load_data', 0.5)
    assert timers._timings['load_data'] == [0.5]

def test_add_multiple_time_entries():
    """Test adding multiple time entries to the same timer."""
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 1.0)
    assert timers._timings['load_data'] == [0.5, 1.0]

def test_total_time():
    """Test calculating total time for a timer."""
    timers = Timers()
    timers.add('process_data', 1.2)
    timers.add('process_data', 0.8)
    assert timers.total('process_data') == 2.0

def test_count_entries():
    """Test counting the number of entries for a timer."""
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 1.0)
    assert timers.count('load_data') == 2

def test_mean_time():
    """Test calculating mean time for a timer."""
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 1.0)
    assert timers.mean('load_data') == pytest.approx(0.75)

def test_median_time():
    """Test calculating median time for a timer."""
    timers = Timers()
    timers.add('process_data', 1.2)
    timers.add('process_data', 0.8)
    assert timers.median('process_data') == pytest.approx(1.0)


def test_clear_timings():
    """Test clearing all stored timings."""
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.clear()
    assert not timers._timings