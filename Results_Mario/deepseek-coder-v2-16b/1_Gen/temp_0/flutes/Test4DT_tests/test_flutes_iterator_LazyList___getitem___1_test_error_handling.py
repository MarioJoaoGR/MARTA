
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    with pytest.raises(IndexError):
        lazy_list = LazyList([1, 2, 3])
        print(lazy_list[5])  # This should raise an IndexError
