
import pytest
from collections import Mapping, Sequence, Set
from typing import Container, FrozenSet, List, Tuple, Dict, Any

# Assuming ImmutableDict and frozenset are defined elsewhere in your codebase
class ImmutableDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._immutable = False

    def _setitem__(self, key, value):
        raise TypeError("ImmutableDict is immutable")

    def update(self, *args, **kwargs):
        raise TypeError("ImmutableDict is immutable")

def _make_immutable(obj: Any) -> Any:
    if isinstance(obj, (str, bytes)):
        return obj
    elif isinstance(obj, Mapping):
        temp_dict = {}
        for key, value in obj.items():
            if isinstance(value, Container):
                temp_dict[key] = _make_immutable(value)
            else:
                temp_dict[key] = value
        return ImmutableDict((k, v) for k, v in temp_dict.items())
    elif isinstance(obj, Set):
        temp_set = set()
        for value in obj:
            if isinstance(value, Container):
                temp_set.add(_make_immutable(value))
            else:
                temp_set.add(value)
        return frozenset(temp_set)
    elif isinstance(obj, Sequence):
        temp_sequence = []
        for value in obj:
            if isinstance(value, Container):
                temp_sequence.append(_make_immutable(value))
            else:
                temp_sequence.append(value)
        return tuple(temp_sequence)
    return obj

# Test cases
def test_valid_case_1():
    result = _make_immutable({'a': [1, 2, 3], 'b': {4, 5, 6}})
    assert isinstance(result['a'], tuple)
    assert isinstance(result['b'], frozenset)

def test_valid_case_2():
    result = _make_immutable(frozenset([[7, 8], {'x': 'y'}]))
    for item in result:
        assert isinstance(item, (tuple, ImmutableDict))

def test_valid_case_3():
    nested_structure = {
        'outer_dict': {'inner_list': [1, 2, 3], 'inner_set': {4, 5, 6}},
        'outer_list': [[7, 8], {'x': 'y'}],
        'outer_set': {(9,), ('z',)}
    }
    result = _make_immutable(nested_structure)
    assert isinstance(result['outer_dict']['inner_list'], tuple)
    assert isinstance(result['outer_dict']['inner_set'], frozenset)
    assert isinstance(result['outer_list'], tuple)
    assert isinstance(result['outer_set'], frozenset)

def test_edge_case_1():
    result = _make_immutable(None)
    assert result is None

def test_edge_case_2():
    result = _make_immutable([])
    assert isinstance(result, tuple)

def test_error_case_1():
    with pytest.raises(TypeError):
        _make_immutable(42)
