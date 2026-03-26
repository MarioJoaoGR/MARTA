
import pytest
from flutes.iterator import Range

# Test cases for the __getitem__ method
def test_range_getitem_integer_index():
    r = Range(10)
    assert r[0] == 0