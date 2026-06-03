# Module: codetiming._timers
import pytest
from collections import defaultdict
from typing import List, Dict, Callable, Any
import codetiming._timers as timers_module  # Replace with actual module name where Timers is defined

# Test the __init__ method of the Timers class
def test_timers_init():
    t = timers_module.Timers()
    assert isinstance(t._timings, defaultdict)
    assert isinstance(t._timings['default'], list)

# Test the apply method with an existing name
def test_apply_existing_name():
    t = timers_module.Timers()
    t._timings['example_timer'] = [1.0, 2.0, 3.0]
    result = t.apply(lambda x: sum(x), 'example_timer')
    assert result == 6.0

# Test the apply method with a non-existing name
def test_apply_non_existing_name():
    t = timers_module.Timers()
    with pytest.raises(KeyError):
        t.apply(lambda x: sum(x), 'nonexistent_timer')

# Test the count method with an existing name
def test_count_existing_name():
    t = timers_module.Timers()
    t._timings['example_timer'] = [1.0, 2.0, 3.0]
    count = t.count('example_timer')
    assert count == 3.0

# Test the count method with a non-existing name
def test_count_non_existing_name():
    t = timers_module.Timers()
    with pytest.raises(KeyError):
        t.count('nonexistent_timer')
