
import pytest
from codetiming._timers import Timers

def test_clear_with_data():
    # Setup: Create a Timers instance and add some timing data
    timers = Timers()
    timers._timings['load_data'] = [0.5, 1.2]
    timers._timings['process_data'] = [0.3]

    # Exercise: Clear the timings
    timers.clear()

    # Verify: Check that _timings is empty
    assert not timers._timings

def test_clear_empty_timings():
    # Setup: Create a Timers instance with no timing data
    timers = Timers()

    # Exercise: Clear the (already) empty timings
    timers.clear()

    # Verify: Check that _timings remains empty
    assert not timers._timings

def test_clear_with_invalid_data():
    # Setup: Create a Timers instance and add invalid data to _timings
    timers = Timers()
    timers._timings['load_data'] = "invalid_string"
    timers._timings['process_data'] = 12345

    # Exercise: Clear the timings with invalid data
    timers.clear()

    # Verify: Check that _timings is empty
    assert not timers._timings
