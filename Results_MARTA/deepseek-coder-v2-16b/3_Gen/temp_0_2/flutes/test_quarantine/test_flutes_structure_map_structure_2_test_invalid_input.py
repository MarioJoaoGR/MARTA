
import pytest
from collections.abc import Callable, Collection
from typing import TypeVar

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

def test_invalid_input():
    with pytest.raises(TypeError):
        map_structure(lambda x: x**2, "not a collection")  # Test with non-collection type

    def square(x):
        return x ** 2

    with pytest.raises(TypeError):
        map_structure(square, None)  # Test with None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_structure_map_structure_2_test_invalid_input
flutes/Test4DT_tests/test_flutes_structure_map_structure_2_test_invalid_input.py:16:24: E0602: Undefined variable '_NO_MAP_TYPES' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_2_test_invalid_input.py:16:54: E0602: Undefined variable '_NO_MAP_INSTANCE_ATTR' (undefined-variable)


"""