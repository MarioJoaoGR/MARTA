
import pytest
from codetiming._timers import Timers

def test_invalid_key():
    timers = Timers()
    func = lambda x: sum(x)
    
    with pytest.raises(KeyError):
        timers.apply(func, "non_existing_timer")
