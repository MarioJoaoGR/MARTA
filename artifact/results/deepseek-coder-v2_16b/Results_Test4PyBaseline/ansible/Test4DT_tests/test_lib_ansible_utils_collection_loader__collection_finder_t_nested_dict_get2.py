
import pytest
from ansible.utils.collection_loader._collection_finder import _nested_dict_get

def test_basic_usage():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['a', 'b', 'c'])
    assert result == 1

def test_key_not_found():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['a', 'x', 'y'])
    assert result is None

def test_intermediate_key_not_found():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, ['a', 'b'])
    assert result == {'c': 1}

def test_empty_key_list():
    data = {'a': {'b': {'c': 1}}}
    result = _nested_dict_get(data, [])