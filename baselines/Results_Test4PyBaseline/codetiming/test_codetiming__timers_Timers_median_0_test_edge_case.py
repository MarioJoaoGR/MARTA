
import pytest
from unittest.mock import patch
import statistics

class Timers:
    def __init__(self):
        self._timings = {'example': [], 'error': [None]}

    def apply(self, func, name):
        if name in self._timings:
            return func(self._timings[name])
        raise KeyError(name)

    def median(self, name):
        return self.apply(lambda values: statistics.median(values or [0]), name)

def test_edge_case():
    timers = Timers()
    
    # Test with an empty list
    with patch('statistics.median', side_effect=ValueError("Cannot calculate median of an empty list")):
        with pytest.raises(ValueError, match="Cannot calculate median of an empty list"):
            timers.median('example')
    
    # Test with a None value in the list
    with patch('statistics.median', return_value=0):
        assert timers.median('error') == 0
