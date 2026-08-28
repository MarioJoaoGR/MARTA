
import pytest
from copy import deepcopy
from unittest.mock import patch, MagicMock

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

    Notes:
        - If `b` is not a dictionary, it will be returned as-is.
        - The function uses deepcopy to ensure that nested dictionaries are copied correctly during the merge process.
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
def test_valid_case_basic():
    a = {'a': 1, 'b': 2}
    b = {'c': 3, 'd': 4}
    merged_dict = dict_merge(a, b)
    assert merged_dict == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_valid_case_nested():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    merged_dict = dict_merge(a, b)
    assert merged_dict == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}

def test_error_case_non_dict():
    a = {'a': 1}
    b = 5  # Not a dictionary
    merged_dict = dict_merge(a, b)
    assert merged_dict == 5
