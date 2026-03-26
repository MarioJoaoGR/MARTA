
import pytest
from flutes.iterator import range_replacement as Range

def test_get_idx_positive():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

def test_get_idx_negative():
    r = Range(10)
    assert r[-1] == 9
    assert r[-3] == 7
    assert r[-5] == 5

def test_get_idx_out_of_range_positive():
    r = Range(10)
    with pytest.raises(IndexError):
        r[10]

def test_get_idx_out_of_range_negative():
    r = Range(10)
    with pytest.raises(IndexError):
        r[-11]

def test_get_idx_zero_step():
    with pytest.raises(ValueError):
        r = Range(1, 2, 0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range__get_idx_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_0_test_edge_cases.py:3:0: E0611: No name 'range_replacement' in module 'flutes.iterator' (no-name-in-module)


"""