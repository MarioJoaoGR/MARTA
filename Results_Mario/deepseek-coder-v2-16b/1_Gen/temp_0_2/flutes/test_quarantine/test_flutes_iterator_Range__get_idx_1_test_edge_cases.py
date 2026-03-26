
import pytest
from flutes.iterator import range_replacement as Range  # Importing the Range class from flutes.iterator

def test_edge_cases():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range__get_idx_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_edge_cases.py:3:0: E0611: No name 'range_replacement' in module 'flutes.iterator' (no-name-in-module)


"""