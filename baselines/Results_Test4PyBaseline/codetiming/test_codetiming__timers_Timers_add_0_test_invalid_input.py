
import pytest
from codetiming._timers import Timers

def test_invalid_input():
    timers = Timers()
    
    with pytest.raises(TypeError):
        # Adding a non-float value should raise a TypeError
        timers.add('test', 'not_a_float')
