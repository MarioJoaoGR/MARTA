
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    
    assert isinstance(iterator, LazyList.LazyListIterator)
    
    items = []
    try:
        while True:
            item = next(iterator)
            items.append(item)
    except StopIteration:
        pass
    
    assert items == [1, 2, 3, 4]
