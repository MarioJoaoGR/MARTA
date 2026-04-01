
import pytest
from typing import Callable, Collection, TypeVar
from flutes.structure import _NO_MAP_TYPES, _NO_MAP_INSTANCE_ATTR

T = TypeVar('T')
R = TypeVar('R')

def map_structure(fn: Callable[[T], R], obj: Collection[T]) -> Collection[R]:
    r"""Map a function over all elements in a (possibly nested) collection.

    :param fn: The function to call on elements.
    :param obj: The collection to map function over.
    :return: The collection in the same structure, with elements mapped.
    """
    if obj.__class__ in _NO_MAP_TYPES or hasattr(obj, _NO_MAP_INSTANCE_ATTR):
        return fn(obj)
    if isinstance(obj, list):
        return [map_structure(fn, x) for x in obj]
    if isinstance(obj, tuple):
        if hasattr(obj, '_fields'):  # namedtuple
            return type(obj)(*[map_structure(fn, x) for x in obj])
        else:
            return tuple(map_structure(fn, x) for x in obj)
    if isinstance(obj, dict):
        # could be `OrderedDict`
        return type(obj)((k, map_structure(fn, v)) for k, v in obj.items())
    if isinstance(obj, set):
        return {map_structure(fn, x) for x in obj}
    return fn(obj)

# Example test case to ensure the function works correctly
def test_map_structure():
    def square(x: int) -> int:
        return x ** 2

    # Test with list
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Test with tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Test with dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Test with set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}
