
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_edge_case():
    timers = Timers()
    with patch('codetiming._timers.collections', {'defaultdict': lambda: {}}):
        timers._timings['example'] = []
        assert timers.min('example') == 0
