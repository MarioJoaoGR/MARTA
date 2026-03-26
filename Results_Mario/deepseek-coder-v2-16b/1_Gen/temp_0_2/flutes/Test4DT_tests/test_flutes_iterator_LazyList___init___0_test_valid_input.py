
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    items = []
    for item in lazy_list:
        items.append(item)
        if item == 3:
            break
    assert items == [1, 2, 3]
