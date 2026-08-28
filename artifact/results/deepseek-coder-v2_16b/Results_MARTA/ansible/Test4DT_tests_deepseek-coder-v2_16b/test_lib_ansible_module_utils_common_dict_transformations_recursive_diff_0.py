
import pytest
from collections import MutableMapping

def recursive_diff(dict1, dict2):
    """Recursively diff two dictionaries

    Raises ``TypeError`` for incorrect argument type.

    :arg dict1: Dictionary to compare against.
    :arg dict2: Dictionary to compare with ``dict1``.
    :return: Tuple of dictionaries of differences or ``None`` if there are no differences.
    """

    if not all((isinstance(item, MutableMapping) for item in (dict1, dict2))):
        raise TypeError("Unable to diff 'dict1' %s and 'dict2' %s. "
                        "Both must be a dictionary." % (type(dict1), type(dict2)))

    left = dict((k, v) for (k, v) in dict1.items() if k not in dict2)
    right = dict((k, v) for (k, v) in dict2.items() if k not in dict1)
    for k in (set(dict1.keys()) & set(dict2.keys())):
        if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            result = recursive_diff(dict1[k], dict2[k])
            if result:
                left[k] = result[0]
                right[k] = result[1]
        elif dict1[k] != dict2[k]:
            left[k] = dict1[k]
            right[k] = dict2[k]
    if left or right:
        return left, right
    return None

# Test cases
def test_valid_case():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 4, 'e': 5}}
    result = recursive_diff(dict1, dict2)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Tuple should contain two dictionaries"
    assert set(result[0].keys()) == {'b'}, "Differences should only be in 'b'"
    assert result[0]['b'] == {'c': 2, 'd': 3}, "'b' dictionary in dict1 is incorrect"
    assert set(result[1].keys()) == {'b'}, "Differences should only be in 'b'"
    assert result[1]['b'] == {'c': 4, 'e': 5}, "'b' dictionary in dict2 is incorrect"

def test_edge_case():
    dict1 = None
    dict2 = None
    with pytest.raises(TypeError):
        recursive_diff(dict1, dict2)

def test_invalid_input():
    dict1 = {}
    dict2 = 'not a dictionary'
    with pytest.raises(TypeError):
        recursive_diff(dict1, dict2)
