
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_non_callable_mapper():
    with pytest.raises(TypeError) as e:
        curried_map(None, [1, 2, 3])
    assert str(e.value) == "'NoneType' object is not callable"
