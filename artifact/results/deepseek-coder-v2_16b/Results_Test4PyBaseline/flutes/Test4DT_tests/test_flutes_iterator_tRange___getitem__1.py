
import pytest
from flutes.iterator import Range

# Test case for __getitem__ with a valid positive index
def test_range_getitem_positive_index():
    r = Range(10)
    assert r[0] == 0, f"Expected {0}, but got {r[0]}"
    assert r[5] == 5, f"Expected {5}, but got {r[5]}"
    assert r[9] == 9, f"Expected {9}, but got {r[9]}"

# Test case for __getitem__ with a valid negative index (should be converted to positive index)
def test_range_getitem_negative_index():
    r = Range(10)
    assert r[-1] == 9, f"Expected {9}, but got {r[-1]}"
    assert r[-5] == 5, f"Expected {5}, but got {r[-5]}"