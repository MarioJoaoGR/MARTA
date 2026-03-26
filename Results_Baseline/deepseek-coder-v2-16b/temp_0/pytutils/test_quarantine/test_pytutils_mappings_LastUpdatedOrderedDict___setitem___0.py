
# Module: pytutils.mappings
import pytest
from collections import OrderedDict
from pytutils.mappings import LastUpdatedOrderedDict

# Test Initialization
def test_initialization():
    ld = LastUpdatedOrderedDict()
    assert isinstance(ld, LastUpdatedOrderedDict), "Initialization should create an instance of LastUpdatedOrderedDict"

# Test Adding a new key-value pair
def test_adding_new_key_value_pair():
    ld = LastUpdatedOrderedDict()
    ld['a'] = 1
    assert list(ld.keys()) == ['a'], "After adding a new key-value pair, the keys should be in the order they were added"

# Test Updating an existing key
def test_updating_existing_key():
    ld = LastUpdatedOrderedDict()
    ld['b'] = 2
    ld['c'] = 3
    ld['a'] = 4
    assert list(ld.keys()) == ['b', 'c', 'a'], "Updating an existing key should move it to the end of the order"

# Test Updating a key that already exists
def test_updating_existing_key():
    ld = LastUpdatedOrderedDict()
    ld['a'] = 1
    ld['b'] = 2
    ld['c'] = 3
    ld['a'] = 4
    assert list(ld.keys()) == ['b', 'c', 'a'], "Updating a key that already exists should move it to the end of the order"

# Test Order after multiple updates
def test_order_after_multiple_updates():
    ld = LastUpdatedOrderedDict()
    ld['a'] = 1
    ld['b'] = 2
    ld['c'] = 3
    ld['a'] = 4
    ld['e'] = 5
    ld['f'] = 6
    ld['g'] = 7
    ld['h'] = 8
    assert list(ld.keys()) == ['b', 'c', 'e', 'f', 'g', 'h', 'a'], "Multiple updates should maintain the order correctly"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_LastUpdatedOrderedDict___setitem___0
pytutils/Test4DT_tests/test_pytutils_mappings_LastUpdatedOrderedDict___setitem___0.py:27:0: E0102: function already defined line 19 (function-redefined)


"""