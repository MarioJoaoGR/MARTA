
import pytest
from flutes.iterator import LazyList

def test_invalid_inputs():
    # Test that LazyList handles invalid inputs gracefully by raising a TypeError
    with pytest.raises(TypeError):
        my_list = None  # This should raise a TypeError as LazyList expects an iterable
        lazy_list = LazyList(my_list)  # Passing None instead of an iterable
