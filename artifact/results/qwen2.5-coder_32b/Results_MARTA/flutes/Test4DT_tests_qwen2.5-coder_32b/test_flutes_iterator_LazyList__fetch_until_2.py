
import pytest
from flutes.iterator import LazyList

def test_LazyList__fetch_until_basic():
    def my_generator():
        for i in range(5):
            yield i * i

    lazy_list = LazyList(my_generator())
    
    # Accessing the first element should fetch only that element
    assert lazy_list[0] == 0
    
    # Accessing the third element should fetch up to that element
    assert lazy_list[2] == 4
