
import pytest
from flutes.iterator import Range

# Test for basic functionality of the Range class with positive indexing

# Test for slicing functionality of the Range class
def test_Range___getitem___slice():
    r = Range(1, 11, 2)
    assert [i for i in r[1:5]] == [3, 5, 7, 9], f"Expected slice to be [3, 5, 7, 9] but got {r[1:5]}"

# Test for negative indexing functionality of the Range class
def test_Range___getitem___negative():
    r = Range(10)
    assert r[-1] == 9, f"Expected r[-1] to be 9 but got {r[-1]}"
    assert r[-3] == 7, f"Expected r[-3] to be 7 but got {r[-3]}"