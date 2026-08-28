
import pytest
from ansible.utils.collection_loader._collection_finder import _nested_dict_get

def test_basic_usage():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['a', 'b', 'c'])
    assert result == 1

def test_key_not_found():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['a', 'b', 'd'])
    assert result is None

def test_key_not_present_in_root():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['x', 'y', 'z'])
    assert result is None

def test_empty_key_list():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, [])
    assert result == {'a': {'b': {'c': 1}}}


def test_complex_nested_structure():
    data = {'outer': {'inner': {'deeply': {'nested': 'value'}}}}
    result = _nested_dict_get(data, ['outer', 'inner', 'deeply', 'nested'])
    assert result == 'value'