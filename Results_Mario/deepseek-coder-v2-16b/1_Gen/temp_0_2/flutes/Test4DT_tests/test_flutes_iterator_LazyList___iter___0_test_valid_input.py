
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    result = []
    for item in lazy_list:
        result.append(item)
        if item == 3:
            break
    assert result == [1, 2, 3]
