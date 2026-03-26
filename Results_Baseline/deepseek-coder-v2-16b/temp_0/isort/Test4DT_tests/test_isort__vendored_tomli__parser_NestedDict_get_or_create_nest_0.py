
from typing import Any, Dict, List, Union

import pytest

# Assuming the module name is 'isort._vendored.tomli._parser' and the class NestedDict is defined there.
try:
    from isort._vendored.tomli._parser import NestedDict
except ImportError:
    pytest.skip("Module not available", allow_module_level=True)

@pytest.fixture
def nested_dict():
    return NestedDict()

# Test cases for get_or_create_nest method

def test_get_or_create_nest_creates_nested_structure(nested_dict):
    assert nested_dict.get_or_create_nest(['a', 'b', 'c']) == {}
    assert isinstance(nested_dict.dict, dict)
    assert isinstance(nested_dict.dict['a'], dict)
    assert isinstance(nested_dict.dict['a']['b'], dict)

def test_get_or_create_nest_with_access_lists_true(nested_dict):
    nested_dict.dict['a'] = {'b': {}}
    assert nested_dict.get_or_create_nest(['a', 'b', 'c'], access_lists=True) == {}
    assert isinstance(nested_dict.dict['a']['b'], dict)

def test_get_or_create_nest_with_access_lists_false(nested_dict):
    nested_dict.dict['a'] = {'b': [1, 2, 3]}