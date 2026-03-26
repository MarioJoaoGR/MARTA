
import pytest
from codetiming._timers import Timers
import math
import statistics

def test_edge_case():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent')
