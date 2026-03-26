
import pytest

from isort._vendored.tomli._parser import NestedDict

# Test cases for NestedDict class methods

def test_get_or_create_nest():
    nd = NestedDict()
    nd.get_or_create_nest(['a', 'b', 'c'])
    assert nd.dict == {'a': {'b': {'c': {}}}}

def test_get_or_create_nest_without_access_lists():
    nd = NestedDict()
    nd.get_or_create_nest(['x', 'y'], access_lists=False)