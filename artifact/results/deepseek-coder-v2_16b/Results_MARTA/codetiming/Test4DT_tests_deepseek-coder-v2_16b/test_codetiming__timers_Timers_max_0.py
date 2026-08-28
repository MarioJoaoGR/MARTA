
import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

# Scenario 1: Test standard input for max function
def test_valid_input_max(timers):
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.max('example_timer') == 3.0

# Scenario 2: Test edge case with empty list for max function
def test_edge_case_max(timers):
    timers._timings['example_timer'] = []
    assert timers.max('example_timer') == 0

# Scenario 3: Test invalid input by passing non-existent timer name to max function
def test_invalid_input_max(timers):
    with pytest.raises(KeyError):
        timers.max('non_existent_timer')
