# Module: codetiming._timers
import pytest
from collections import defaultdict
import codetiming._timers as timers_module

# Test initialization of Timers class
def test_init():
    t = timers_module.Timers()
    assert isinstance(t, timers_module.Timers)
    assert isinstance(t._timings, defaultdict)
    assert isinstance(t.data, dict)

# Test adding a timing value to a new timer
def test_add_new_timer():
    t = timers_module.Timers()
    t.add('task1', 0.5)
    assert 'task1' in t._timings
    assert t._timings['task1'] == [0.5]
    assert 'task1' in t.data
    assert t.data['task1'] == 0.5

# Test adding a timing value to an existing timer
def test_add_existing_timer():
    t = timers_module.Timers()
    t.add('task1', 0.5)
    t.add('task1', 0.3)
    assert 'task1' in t._timings
    assert t._timings['task1'] == [0.5, 0.3]
    assert 'task1' in t.data
    assert t.data['task1'] == 0.8

# Test adding a timing value to multiple timers
def test_add_multiple_timers():
    t = timers_module.Timers()
    t.add('task1', 0.5)
    t.add('task2', 0.3)
    assert 'task1' in t._timings
    assert t._timings['task1'] == [0.5]
    assert 'task2' in t._timings
    assert t._timings['task2'] == [0.3]
    assert 'task1' in t.data
    assert t.data['task1'] == 0.5
    assert 'task2' in t.data
    assert t.data['task2'] == 0.3
