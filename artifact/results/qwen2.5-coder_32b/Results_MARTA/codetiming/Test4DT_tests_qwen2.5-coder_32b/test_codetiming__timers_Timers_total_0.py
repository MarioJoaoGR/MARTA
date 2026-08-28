
import pytest
from codetiming._timers import Timers

def test_valid_case():
    timers = Timers()
    timers._timings['example_timer'] = [1.2, 3.4, 5.6]
    assert timers.total('example_timer') == 10.2

def test_edge_case_empty_list():
    timers = Timers()
    timers._timings['empty_timer'] = []
    assert timers.total('empty_timer') == 0.0

def test_error_case_missing_key():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.total('non_existent_timer')
