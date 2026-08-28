
import pytest

def _nested_dict_get(root_dict, key_list):
    cur_value = root_dict
    for key in key_list:
        cur_value = cur_value.get(key)
        if not cur_value:
            return None

    return cur_value

# Test cases
@pytest.mark.parametrize("data, keys, expected", [
    ({'a': {'b': {'c': 1}}}, ['a', 'b', 'c'], 1),
    ({'a': {'b': {'c': 1}}}, ['a', 'b', 'd'], None),
    ({'a': {'b': {'c': 1}}}, ['x', 'y', 'z'], None)
])
def test_nested_dict_get(data, keys, expected):
    assert _nested_dict_get(data, keys) == expected
