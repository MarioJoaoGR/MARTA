
import pytest
from collections import defaultdict
from typing import Any, Callable, Dict, List
import codetiming._timers as timers_module

# Test initialization with no arguments
def test_init_no_args():
    t = timers_module.Timers()
    assert isinstance(t._timings, defaultdict)