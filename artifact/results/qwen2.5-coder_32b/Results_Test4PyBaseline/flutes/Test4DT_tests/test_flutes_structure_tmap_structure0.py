# Module: flutes.structure
import pytest
from flutes.structure import map_structure
from collections import namedtuple

def test_map_structure_simple_list():
    result = map_structure(lambda x: x * 2, [1, 2, 3, 4])
    assert result == [2, 4, 6, 8]

def test_map_structure_nested_list():
    result = map_structure(lambda x: x + 1, [1, [2, 3], [4, [5, 6]]])
    assert result == [2, [3, 4], [5, [6, 7]]]

def test_map_structure_dict():
    result = map_structure(str.upper, {'a': 'apple', 'b': 'banana'})
    assert result == {'a': 'APPLE', 'b': 'BANANA'}

def test_map_structure_nested_dict():
    result = map_structure(lambda x: x * 3 if isinstance(x, int) else str.upper(x),
                          {'numbers': [1, 2, 3], 'text': ['hello', 'world']})
    assert result == {'numbers': [3, 6, 9], 'text': ['HELLO', 'WORLD']}

def test_map_structure_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    result = map_structure(lambda n: n * 2, Point(1, 2))
    assert result == Point(x=2, y=4)

def test_map_structure_set():
    result = map_structure(lambda x: -x, {1, 2, 3})
    assert result == {-1, -2, -3}

def test_map_structure_mixed_types():
    Mixed = namedtuple('Mixed', ['num', 'text'])
    data = [Mixed(1, 'a'), {'key': (2, 'b')}, [3, 'c']]
    result = map_structure(lambda x: x * 2 if isinstance(x, int) else str.upper(x), data)
    expected = [Mixed(num=2, text='A'), {'key': (4, 'B')}, [6, 'C']]
    assert result == expected

def test_map_structure_empty_structures():
    assert map_structure(lambda x: x, []) == []
    assert map_structure(lambda x: x, {}) == {}
    assert map_structure(lambda x: x, ()) == ()
    assert map_structure(lambda x: x, set()) == set()

def test_map_structure_no_change():
    result = map_structure(lambda x: x, [1, 2, {'a': 3}])
    assert result == [1, 2, {'a': 3}]
