
# Module: flutes.structure
import pytest
from typing import Callable, List, Tuple, Dict, Set, Collection
from collections.abc import Iterable

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

# Test cases
def test_map_structure_list():
    def square(x):
        return x ** 2
    
    a = [1, 2, 3, 4, 5]
    expected = [1, 4, 9, 16, 25]
    assert map_structure(square, a) == expected

def test_map_structure_tuple():
    def square(x):
        return x ** 2
    
    b = (1, 2, 3, 4, 5)
    expected = (1, 4, 9, 16, 25)
    assert map_structure(square, b) == expected

def test_map_structure_dict():
    def square(x):
        return x ** 2
    
    c = {'a': 1, 'b': 2, 'c': 3}
    expected = {'a': 1, 'b': 4, 'c': 9}
    assert map_structure(square, c) == expected

def test_map_structure_set():
    def square(x):
        return x ** 2
    
    d = {1, 2, 3, 4, 5}
    expected = {1, 4, 9, 16, 25}
    assert map_structure(square, d) == expected

def test_map_structure_non_collection():
    def square(x):
        return x ** 2
    
    e = 5
    expected = 25
    assert map_structure(square, e) == expected

# Additional edge cases can be added to ensure robustness

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_structure_map_structure_0
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:7:32: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:7:36: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:7:56: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:7:74: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:14:24: E0602: Undefined variable '_NO_MAP_TYPES' (undefined-variable)
flutes/Test4DT_tests/test_flutes_structure_map_structure_0.py:14:54: E0602: Undefined variable '_NO_MAP_INSTANCE_ATTR' (undefined-variable)


"""