
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

# Scenario 3: Test max function with single value
def test_single_value_max(timers):
    timers._timings['single_timer'] = [42.0]
    assert timers.max('single_timer') == 42.0

# Scenario 4: Test max function with multiple values including negative numbers
def test_multiple_values_with_negatives_max(timers):
    timers._timings['negative_timer'] = [-1.0, -2.0, -3.0]
    assert timers.max('negative_timer') == -1.0

# Scenario 5: Test max function with non-numeric values raises TypeError