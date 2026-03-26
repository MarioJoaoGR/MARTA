
from typing import Any, Dict, List, Union

import pytest

from isort._vendored.tomli._parser import NestedDict

# Define the type for the keys in the dictionary
Key = List[Union[str, int]]

def test_get_or_create_nest_basic():
    nd = NestedDict()
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert result == {}
    assert nd.dict == {'a': {'b': {'c': {}}}}

def test_get_or_create_nest_create():
    nd = NestedDict()
    result = nd.get_or_create_nest(['x', 'y'])
    assert result == {}