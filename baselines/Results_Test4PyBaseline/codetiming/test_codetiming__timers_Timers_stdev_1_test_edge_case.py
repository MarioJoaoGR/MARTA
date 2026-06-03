
import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics
import math

def test_edge_case():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent')
