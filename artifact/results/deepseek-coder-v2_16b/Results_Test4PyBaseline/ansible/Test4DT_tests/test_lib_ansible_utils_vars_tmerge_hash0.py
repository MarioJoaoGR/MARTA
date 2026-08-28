
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

def test_basic_merge():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': [4], 'c': 5}
    merged = merge_hash(x, y)
    assert merged == {'a': 1, 'b': [4], 'c': 5}

def test_non_recursive_merge():
    x = {'a': 1, 'b': [2, 3]}
    y = {'b': [4], 'c': 5}
    merged_non_recursive = merge_hash(x, y, recursive=False)