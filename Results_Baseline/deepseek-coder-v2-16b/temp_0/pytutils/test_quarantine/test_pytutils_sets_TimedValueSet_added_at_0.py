
# Module: pytutils.sets
import pytest
from pytutils import TimedValueSet
import time
import attr

# Check if the _meta attribute is initialized correctly
def test_default_initialization():
    timed_value_set = TimedValueSet()
    assert hasattr(timed_value_set, '_meta'), "The TimedValueSet instance should have an attribute `_meta`"
    assert isinstance(timed_value_set._meta, dict), f"Expected _meta to be a dictionary but got {type(timed_value_set._meta)}"

# Check if the added_at method returns the correct metadata
def test_added_at_method():
    timed_value_set = TimedValueSet()
    assert hasattr(timed_value_set, 'added_at'), "The TimedValueSet instance should have an `added_at` method"
    meta_time = time.time()  # Capture the current time for comparison
    assert timed_value_set.added_at() == {'meta_func': lambda value, **kwargs: meta_time}, f"Expected added_at to return {{'meta_func': lambda value, **kwargs: {meta_time}}} but got {timed_value_set.added_at()}"

# Check if the added_at method returns a dictionary with the correct time when initialized without parameters
def test_added_at_method_no_params():
    timed_value_set = TimedValueSet()
    meta_time = time.time()  # Capture the current time for comparison
    assert timed_value_set.added_at() == {'meta_func': lambda value, **kwargs: meta_time}, f"Expected added_at to return {{'meta_func': lambda value, **kwargs: {meta_time}}} but got {timed_value_set.added_at()}"

# Check if the added_at method returns a dictionary with the correct time when initialized with custom arguments
def test_custom_initialization():
    timed_value_set = TimedValueSet(custom_arg=123)  # Instantiate with a custom argument
    meta_time = time.time()  # Capture the current time for comparison
    assert timed_value_set.added_at() == {'meta_func': lambda value, **kwargs: meta_time}, f"Expected added_at to return {{'meta_func': lambda value, **kwargs: {meta_time}}} but got {timed_value_set.added_at()}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_sets_TimedValueSet_added_at_0
pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0.py:4:0: E0611: No name 'TimedValueSet' in module 'pytutils' (no-name-in-module)


"""