
import pytest
from isort.sorting import key_callback  # Assuming this is the correct module path

def test_key_callback():
    assert key_callback("example123abc") == [('a', 97), ('b', 98), ('c', 99), ('e', 101), ('l', 108), ('m', 109), ('n', 110), ('p', 112), ('r', 114), ('t', 116), ('x', 120)]
    assert key_callback("test456") == [('e', 101), ('s', 115), ('t', 116), ('u', 117), ('w', 119)]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_sorting_key_callback_0_test_edge_case
isort/Test4DT_tests/test_isort_sorting_key_callback_0_test_edge_case.py:3:0: E0611: No name 'key_callback' in module 'isort.sorting' (no-name-in-module)


"""