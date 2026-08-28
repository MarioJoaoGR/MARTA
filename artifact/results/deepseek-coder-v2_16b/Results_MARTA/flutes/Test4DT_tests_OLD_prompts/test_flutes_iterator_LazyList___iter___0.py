
import pytest
from flutes.iterator import LazyList

def test_lazy_list_iteration():
    numbers = [1, 2, 3, 4]
    lazy_list = LazyList(numbers)
    result = []
    for item in lazy_list:
        result.append(item)
    assert result == [1, 2, 3, 4]
