
import pytest
from codetiming._timers import Timers  # Correctly importing from the module

def test_median_invalid_input():
    timers = Timers()
    
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')
