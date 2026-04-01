
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_invalid_inputs():
    # Test case 1: Invalid mapper (not a function)
    with pytest.raises(TypeError):
        curried_map("not_a_function", [1, 2, 3])

    # Test case 2: Invalid collection (not iterable)
    with pytest.raises(TypeError):
        curried_map(lambda x: x * 2, 12345)

    # Test case 3: Empty collection
    assert curried_map(lambda x: x ** 2, []) == []

    # Test case 4: Collection with None elements (should raise TypeError if not handled properly)
    with pytest.raises(TypeError):
        curried_map(lambda x: x * 2, [None])
