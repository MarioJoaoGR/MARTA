
import pytest
from copy import deepcopy

def dict_merge(a, b):
    '''Recursively merges two dictionaries. If both `a` and `b` have a key whose value is a dictionary, the function will recursively merge these nested dictionaries. The function returns a new dictionary that represents the result of merging `a` and `b`.

    Parameters:
        a (dict): The first dictionary to be merged.
        b (dict): The second dictionary to be merged.

    Returns:
        dict: A new dictionary that is the result of recursively merging `a` and `b`.

    Examples:
        >>> a = {'a': 1, 'b': {'c': 2}}
        >>> b = {'b': {'d': 3}, 'e': 4}
        >>> dict_merge(a, b)
        {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    '''
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result

# Test cases
def test_valid_merge():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    merged = dict_merge(a, b)
    assert merged == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}

def test_merge_with_non_dict():
    a = {'a': 1}
    b = 5
    merged = dict_merge(a, b)
    assert merged == 5

def test_invalid_input():
    a = None
    b = {'b': {'d': 3}, 'e': 4}
    with pytest.raises(TypeError):
        dict_merge(a, b)
