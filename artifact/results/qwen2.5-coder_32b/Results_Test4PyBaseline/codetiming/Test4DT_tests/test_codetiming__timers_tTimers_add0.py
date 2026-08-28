
# Test case  

# Module: codetiming._timers
import pytest
from codetiming._timers import Timers
import collections  # Importing the collections module

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, collections.defaultdict)
    assert isinstance(timers.data, dict)

def test_add_single_entry():
    timers = Timers()
    timers.add('load_data', 0.5)
    assert timers._timings['load_data'] == [0.5]
    assert timers.data['load_data'] == 0.5

def test_add_multiple_entries_same_label():
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('load_data', 0.3)
    assert timers._timings['load_data'] == [0.5, 0.3]
    assert timers.data['load_data'] == 0.8

def test_add_multiple_entries_different_labels():
    timers = Timers()
    timers.add('load_data', 0.5)
    timers.add('process_data', 1.2)
    assert timers._timings['load_data'] == [0.5]
    assert timers.data['load_data'] == 0.5
    assert timers._timings['process_data'] == [1.2]
    assert timers.data['process_data'] == 1.2

def test_add_zero_value():
    timers = Timers()
    timers.add('idle', 0.0)
    assert timers._timings['idle'] == [0.0]
    assert timers.data['idle'] == 0.0

def test_add_negative_value():
    timers = Timers()
    # Assuming the function does not raise an error for negative values
    timers.add('error', -0.5)
    assert timers._timings['error'] == [-0.5]
    assert timers.data['error'] == -0.5

def test_add_non_string_label():
    timers = Timers()
    # Assuming the function does not raise an error for non-string labels
    timers.add(123, 0.5)
    assert timers._timings[123] == [0.5]
    assert timers.data[123] == 0.5

def test_add_non_float_value():
    timers = Timers()
    with pytest.raises(TypeError):
        timers.add('load_data', 'not_a_float')
