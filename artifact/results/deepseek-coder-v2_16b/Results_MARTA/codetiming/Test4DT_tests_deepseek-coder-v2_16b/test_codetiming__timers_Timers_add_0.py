
import pytest
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    timers.add('task1', 1.23)
    assert 'task1' in timers._timings
    assert len(timers._timings['task1']) == 1
    assert timers._timings['task1'][0] == 1.23
    assert timers.data['task1'] == 1.23

def test_edge_case():
    timers = Timers()
    with pytest.raises(TypeError):
        timers.add('', None)

def test_invalid_input():
    timers = Timers()
    with pytest.raises(TypeError):
        timers.add('task1', 'not a float')
