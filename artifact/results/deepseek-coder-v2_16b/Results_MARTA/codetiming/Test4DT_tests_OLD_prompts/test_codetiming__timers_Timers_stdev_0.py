
import pytest
from unittest.mock import patch
import math
import statistics
from codetiming._timers import Timers

# Test Scenario 1: test_valid_input
def test_valid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.23, 4.56, 7.89]
    
    with patch('statistics.stdev', return_value=2.0):
        result = timers.stdev('example_timer')
        assert math.isnan(result) == False

# Test Scenario 2: test_edge_case
def test_edge_case():
    timers = Timers()
    timers._timings['example_timer'] = []
    
    with patch('statistics.stdev', return_value=math.nan):
        result = timers.stdev('example_timer')
        assert math.isnan(result) == True

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    timers = Timers()
    timers._timings['example_timer'] = [1.23, 4.56, 7.89]
    
    with pytest.raises(KeyError):
        timers.stdev('non_existent_timer')
