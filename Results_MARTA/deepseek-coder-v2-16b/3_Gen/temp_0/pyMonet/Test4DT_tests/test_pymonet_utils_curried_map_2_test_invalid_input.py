
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_invalid_input():
    with pytest.raises(TypeError):
        # Providing an integer instead of a function as the mapper
        result = curried_map(42, [1, 2, 3])
