
import pytest
from flutes.iterator import Range

# Slicing tests
def test_range_slice_basic():
    r = Range(1, 10)
    assert list(r[slice(None)]) == list(range(1, 10))
    assert list(r[slice(1, 5)]) == [2, 3, 4, 5]