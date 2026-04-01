
import pytest

def curried_filter(filterer, collection):
    return [item for item in collection if filterer(item)]

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where filterer is not a callable
        curried_filter(123, [1, 2, 3])
    
    with pytest.raises(TypeError):
        # Test case where collection is not an iterable
        curried_filter(lambda x: x % 2 == 0, 123)
