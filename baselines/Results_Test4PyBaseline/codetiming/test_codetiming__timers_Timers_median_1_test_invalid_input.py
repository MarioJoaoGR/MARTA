
import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics

def test_invalid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median('non_existent')
