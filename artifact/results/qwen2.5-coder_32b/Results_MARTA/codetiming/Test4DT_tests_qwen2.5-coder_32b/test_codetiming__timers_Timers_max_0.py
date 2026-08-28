
import pytest
from codetiming._timers import Timers

def test_valid_case():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.max('example_timer') == 5.6

def test_edge_case_empty_list():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.max('empty_timer') == 0.0

def test_invalid_case_missing_timer():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.max('non_existent_timer')
