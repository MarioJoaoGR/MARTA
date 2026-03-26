
import pytest
from collections import defaultdict
import statistics
from codetiming._timers import Timers

def test_invalid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median("non_existent_key")
