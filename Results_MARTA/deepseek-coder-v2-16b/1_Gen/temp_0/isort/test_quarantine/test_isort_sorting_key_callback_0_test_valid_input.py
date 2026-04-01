
from isort.sorting import key_callback  # Assuming this is the correct module path
import pytest

def test_valid_input():
    assert key_callback("example123") == [('e', 0), ('x', 1), ('a', 2), ('m', 3), ('p', 4), ('l', 5), ('e', 6), ('1', 7), ('2', 8), ('3', 9)]
    assert key_callback("abc123xyz") == [('a', 0), ('b', 1), ('c', 2), ('1', 3), ('2', 4), ('3', 5), ('x', 6), ('y', 7), ('z', 8)]
    assert key_callback("123abc") == [('1', 0), ('2', 1), ('3', 2), ('a', 3), ('b', 4), ('c', 5)]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_sorting_key_callback_0_test_valid_input
isort/Test4DT_tests/test_isort_sorting_key_callback_0_test_valid_input.py:2:0: E0611: No name 'key_callback' in module 'isort.sorting' (no-name-in-module)


"""