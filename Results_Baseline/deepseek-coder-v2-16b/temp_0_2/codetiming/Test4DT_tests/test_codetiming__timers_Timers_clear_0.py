
import pytest
from collections import defaultdict
import collections

# Import the Timers class from the module codetiming._timers
try:
    from codetiming._timers import Timers
except ImportError:
    # If the module is not found, skip the test
    pytest.skip("Module 'codetiming._timers' not found", allow_module_level=True)

def test_init():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)