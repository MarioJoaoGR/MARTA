
import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics

def test_invalid_inputs():
    timers = Timers()
    
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x) / len(x), "nonexistent_timer")
        
    with pytest.raises(KeyError):
        timers.mean("nonexistent_timer")
