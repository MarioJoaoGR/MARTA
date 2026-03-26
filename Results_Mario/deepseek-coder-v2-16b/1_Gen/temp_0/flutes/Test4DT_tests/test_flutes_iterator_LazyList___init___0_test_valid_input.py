
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    
    # Check that the elements are accessed lazily and only up to the point of iteration
    for i in range(len(my_list)):
        assert next(lazy_list.iter) == my_list[i]
