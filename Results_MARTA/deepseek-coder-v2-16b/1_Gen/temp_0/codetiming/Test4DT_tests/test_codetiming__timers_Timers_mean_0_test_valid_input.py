
import pytest
from codetiming._timers import Timers  # Correctly importing from the specified module
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_with_valid_input(timers):
    # Adding some timings to simulate valid input
    timers._timings['example_timer'].extend([10, 20, 30])
    
    # Calculating the mean of the timings
    result = timers.mean('example_timer')
    
    # Asserting that the mean is calculated correctly
    assert result == statistics.mean([10, 20, 30])
