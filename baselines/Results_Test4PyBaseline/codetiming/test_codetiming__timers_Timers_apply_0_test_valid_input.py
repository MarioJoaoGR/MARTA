
import pytest
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    
    # Add a valid timer with some timestamps
    with pytest.raises(TypeError):
        timers['test_timer'] = [1.0, 2.0, 3.0]
