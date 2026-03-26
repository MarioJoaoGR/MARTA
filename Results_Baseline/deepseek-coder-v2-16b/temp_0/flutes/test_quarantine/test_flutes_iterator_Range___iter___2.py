
# Module: flutes.iterator
# test_range.py
from flutes.iterator import Range
import pytest

@pytest.fixture
def range_instance():
    return Range(1, 10 + 1)

def test_range_creation():
    r = Range(1, 10 + 1)
    assert isinstance(r, Range), "Range instance should be created successfully"

def test_index_access():
    r = Range(1, 10 + 1)
    assert r[0] == 1, "Indexing at position 0 should return the start value"
    assert r[2] == 3, "Indexing at position 2 should return the third element in the sequence"

# Additional test cases for __iter__ method
def test_range_iteration():
    r = Range(1, 5)
    iterator = iter(r)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    with pytest.raises(StopIteration):
        next(iterator)

def test_range_iteration_with_step():
    r = Range(1, 10, 2)
    iterator = iter(r)
    assert next(iterator) == 1
    assert next(iterator) == 3
    assert next(iterator) == 5
    assert next(iterator) == 7
    assert next(iterator) == 9
    with pytest.raises(StopIteration):
        next(iterator)

def test_range_iteration_negative_step():
    r = Range(10, 1, -1)
    iterator = iter(r)
    assert next(iterator) == 10
    assert next(iterator) == 9
    assert next(iterator) == 8
    assert next(iterator) == 7
    assert next(iterator) == 6
    assert next(iterator) == 5
    assert next(iterator) == 4
    assert next(iterator) == 3
    assert next(iterator) == 2
    with pytest.raises(StopIteration):
        next(iterator)

def test_range_iteration_zero_step():
    with pytest.raises(ValueError):
        Range(1, 5, 0)

def test_range_iteration_invalid_arguments():
    with pytest.raises(TypeError):
        iter(Range())
    with pytest.raises(TypeError):
        iter(Range(step=2))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___iter___2
flutes/Test4DT_tests/test_flutes_iterator_Range___iter___2.py:65:13: E1123: Unexpected keyword argument 'step' in constructor call (unexpected-keyword-arg)


"""