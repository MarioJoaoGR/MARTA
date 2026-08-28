
import pytest
from codetiming._timers import Timers
import statistics

def test_edge_case():
    timers = Timers()
    timers._timings['example_timer'] = []
    with pytest.raises(statistics.StatisticsError):
        statistics.median(timers._timings['example_timer'])
