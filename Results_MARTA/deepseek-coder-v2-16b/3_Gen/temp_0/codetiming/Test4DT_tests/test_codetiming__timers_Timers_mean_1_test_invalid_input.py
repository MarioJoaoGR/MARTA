
import pytest
from codetiming._timers import Timers  # Corrected import from 'codetiming'
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_invalid_input(timers):
    with pytest.raises(KeyError):
        timers.mean("non_existent_timer")
