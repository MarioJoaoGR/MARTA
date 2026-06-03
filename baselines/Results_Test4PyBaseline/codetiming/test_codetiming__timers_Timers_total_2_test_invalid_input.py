
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_invalid_input():
    timers = Timers()
    
    with pytest.raises(KeyError):
        timers.total("non_existent_timer")
