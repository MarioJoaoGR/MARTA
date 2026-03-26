
import pytest
from codetiming._timers import Timers  # Correctly importing from the specified module

def test_min_valid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.min("non_existent_timer")
