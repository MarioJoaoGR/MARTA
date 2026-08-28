
import pytest
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.total('example_timer') == sum([1.0, 2.0, 3.0])

def test_invalid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    with pytest.raises(KeyError):
        assert timers.total('non_existent_timer')

def test_apply_function():
    timers = Timers()
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    result = timers.apply(sum, 'example_timer')
    assert result == sum([1.0, 2.0, 3.0])
