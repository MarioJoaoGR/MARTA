
import pytest
from ansible.utils.vars import merge_hash
from collections.abc import MutableMapping, MutableSequence
from ansible.errors import AnsibleError

# Helper function to simulate iteritems for Python 3 compatibility
try:
    from collections import abc as collections_abc
except ImportError:
    import collections as collections_abc

def iteritems(d):
    return ((k, d[k]) for k in d)

# Test cases for merge_hash function

def test_invalid_list_merge():
    x = {'a': 1}
    y = {'b': [4]}
    with pytest.raises(AnsibleError):
        merge_hash(x, y, list_merge='invalid')

def _validate_mutable_mappings(x, y):
    if not isinstance(x, MutableMapping) or not isinstance(y, MutableMapping):
        raise TypeError("Both inputs must be mutable mappings")

def test_validate_mutable_mappings():
    x = None
    y = {}
    with pytest.raises(TypeError):
        _validate_mutable_mappings(x, y)

def test_empty_dict_merge():
    x = {}
    y = {'a': 1}
    merged = merge_hash(x, y)
    assert merged == {'a': 1}

def test_equal_dict_merge():
    x = {'a': 1}
    y = {'a': 1}
    merged = merge_hash(x, y)
    assert merged == {'a': 1}

def test_non_recursive_merge():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': [4], 'c': 5}
    merged_non_recursive = merge_hash(x, y, recursive=False)
    assert merged_non_recursive == {'a': 1, 'b': [4], 'c': 5}

def test_recursive_merge():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': {'d': 4}, 'c': 5}
    merged_recursive = merge_hash(x, y)
    assert merged_recursive == {'a': 1, 'b': {'d': 4}, 'c': 5}

def test_list_replace():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': [4], 'c': 5}
    merged_replace = merge_hash(x, y, list_merge='replace')
    assert merged_replace == {'a': 1, 'b': [4], 'c': 5}

def test_list_append():
    x = {'a': 1, 'b': [2]}
    y = {'b': [3, 4], 'c': 5}
    merged_append = merge_hash(x, y, list_merge='append')
    assert merged_append == {'a': 1, 'b': [2, 3, 4], 'c': 5}

def test_list_prepend():
    x = {'a': 1, 'b': [2]}
    y = {'b': [3, 4], 'c': 5}
    merged_prepend = merge_hash(x, y, list_merge='prepend')
    assert merged_prepend == {'a': 1, 'b': [3, 4, 2], 'c': 5}

def test_list_append_rp():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': [4, 5], 'c': 5}
    merged_append_rp = merge_hash(x, y, list_merge='append_rp')