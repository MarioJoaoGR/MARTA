
import pytest
from flutes.iterator import Range

# Initialization tests
def test_range_one_argument():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == 10

def test_range_two_arguments():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.val == 1
    assert r.length == 9

def test_range_three_arguments():
    r = Range(1, 11, 2)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2
    assert r.val == 1
    assert r.length == 5

def test_range_invalid_number_of_arguments():
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

# Indexing tests
def test_range_index_access():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9

def test_range_index_access_negative():
    r = Range(1, 11, 2)
    with pytest.raises(IndexError):
        r[-1]  # Should raise IndexError for negative index out of range
    with pytest.raises(IndexError):
        r[-6]  # Should raise IndexError for negative index out of range

def test_range_index_access_out_of_range():
    r = Range(1, 5)
    with pytest.raises(IndexError):
        r[5]  # Should raise IndexError for index out of range

# Slicing tests
def test_range_slicing():
    r = Range(1, 11, 2)
    assert r[0:3] == [1, 3, 5]
    assert r[1:4] == [3, 5, 7]
    assert r[2:] == [5, 7, 9]
    assert r[:3] == [1, 3, 5]

def test_range_slicing_invalid():
    r = Range(1, 5)
    with pytest.raises(TypeError):
        r[0:3:2:1]  # Invalid slicing syntax should raise TypeError

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___getitem___2
flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___2.py:68:16: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_flutes_iterator_Range___getitem___2, line 68)' (syntax-error)


"""