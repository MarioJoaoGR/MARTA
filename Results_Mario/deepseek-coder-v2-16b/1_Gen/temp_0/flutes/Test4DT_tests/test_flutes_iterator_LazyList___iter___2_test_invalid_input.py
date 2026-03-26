
import pytest
from flutes.iterator import LazyList

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy_list = LazyList(iterable=None)  # Passing None should raise a TypeError
