
import pytest
from codetiming._timers import Timers  # Corrected import path
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean(timers):
    # Adding some timings to the timer
    timers._timings['example_timer'].extend([1, 2, 3, 4])
    
    # Calculating mean for 'example_timer'
    result = timers.mean('example_timer')
    
    # Expected mean value is (1+2+3+4)/4 = 2.5
    assert pytest.approx(result, 0.0001) == 2.5
