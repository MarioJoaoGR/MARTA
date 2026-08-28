
import pytest
from unittest.mock import patch
import statistics

# Assuming the Timers class and its methods are defined in a module named 'codetiming._timers'
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_valid_input(timers):
    timers._timings['example_timer'] = [1.0, 2.0, 3.0]
    assert timers.median('example_timer') == statistics.median([1.0, 2.0, 3.0])

def test_edge_case(timers):
    timers._timings['example_timer'] = []
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')
    assert timers.median('example_timer') == statistics.median([0])

def test_invalid_input(timers):
    with pytest.raises(KeyError):
        timers.median('non_existent_timer')
