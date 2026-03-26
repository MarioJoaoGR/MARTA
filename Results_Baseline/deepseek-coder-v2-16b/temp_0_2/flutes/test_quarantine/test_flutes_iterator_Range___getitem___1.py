
import pytest
from flutes.iterator import Range

# Slicing tests
def test_range_slice():
    r = Range(1, 10)
    assert r[slice(None)] == list(range(1, 10))
    assert r[slice(1, 5)] == [i for i in range(1, 5)]
    assert r[slice(1, 10, 2)] == [i for i in range(1, 10, 2)]
    assert r[slice(None, None, -1)] == list(range(9, 0, -1))
    assert r[slice(None, 5, -1)] == [i for i in range(9, 4, -1)]
    assert r[slice(None, None, 2)] == list(range(1, 10, 2)]

# Edge cases for slicing
def test_range_slice_edge_cases():
    r = Range(1, 10)
    with pytest.raises(TypeError):
        r[slice(None)] = [1]  # Slicing assignment is not supported
    assert r[slice(2, 8, 0)] == []  # Invalid step (zero step)
    assert r[slice(-1, -10)] == []  # Negative slice indices out of range
    assert r[slice(10, 20)] == []  # Slice out of the actual range bounds

# Test slicing with different start, stop, and step values
def test_range_slice_with_different_values():
    r = Range(1, 15, 3)
    assert r[slice(None)] == [i for i in range(1, 15, 3)]
    assert r[slice(1, 6)] == [i for i in range(1 + 1 * 3, 6 * 3 + 1, 3)]
    assert r[slice(2, None, 2)] == [i for i in range(2 * 3 + 1, 5 * 3 + 1, 3)]
    assert r[slice(None, None, -1)] == []  # Empty slice with negative step

# Test slicing with invalid start, stop, and step values
def test_range_invalid_slicing():
    r = Range(1, 10)
    with pytest.raises(TypeError):
        r[slice(None)] = [1]  # Slicing assignment is not supported
    assert r[slice(2, 8, 0)] == []  # Invalid step (zero step)
    assert r[slice(-1, -10)] == []  # Negative slice indices out of range
    assert r[slice(10, 20)] == []  # Slice out of the actual range bounds

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___getitem___1
flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___1.py:13:59: E0001: Parsing failed: 'closing parenthesis ']' does not match opening parenthesis '(' (Test4DT_tests.test_flutes_iterator_Range___getitem___1, line 13)' (syntax-error)


"""