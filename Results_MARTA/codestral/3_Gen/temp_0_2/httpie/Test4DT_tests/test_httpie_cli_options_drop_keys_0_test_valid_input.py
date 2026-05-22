
import pytest
from typing import Dict, Any, Tuple

def drop_keys(configuration: Dict[str, Any], key_blacklist: Tuple[str, ...]) -> Dict[str, Any]:
    return {key: value for key, value in configuration.items() if key not in key_blacklist}

@pytest.mark.parametrize("config, blacklist, expected", [
    ({'a': 1, 'b': 2, 'c': 3}, ('a',), {'b': 2, 'c': 3}),
    ({'x': 4, 'y': 5, 'z': 6}, ('x',), {'y': 5, 'z': 6}),
    ({'foo': 'bar', 'baz': 'qux'}, ('foo',), {'baz': 'qux'}),
    ({"a": "apple", "b": "banana", "c": "cherry"}, ("a",), {"b": "banana", "c": "cherry"}),
])
def test_valid_input(config, blacklist, expected):
    assert drop_keys(config, blacklist) == expected
