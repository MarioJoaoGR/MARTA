
import pytest
from unittest.mock import patch
import math
import statistics
from codetiming._timers import Timers

def test_valid_input():
    timers = Timers()
    with patch('codetiming._timers.statistics.stdev', return_value=1.0):
        timers._timings['example'] = [1.0, 2.0, 3.0]
        assert math.isnan(timers.stdev('example')) == False
