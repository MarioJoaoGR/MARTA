
import pytest
from codetiming._timers import Timers

def test_none_value():
    timers = Timers()
    with pytest.raises(TypeError):
        timers.add('task2', None)
