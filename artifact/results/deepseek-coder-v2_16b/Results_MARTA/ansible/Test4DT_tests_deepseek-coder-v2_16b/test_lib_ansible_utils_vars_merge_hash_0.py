
import pytest
from ansible.utils.vars import merge_hash

def test_merge_hash_basic():
    merged = merge_hash({'a': 1}, {'b': 2})
    assert merged == {'a': 1, 'b': 2}

def test_merge_hash_recursive_false():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': 3}}, recursive=False)
    assert merged == {'a': {'b': 3}}




def test_merge_hash_list_merge_prepend_rp():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [2, 3]}}, list_merge='prepend_rp')
    assert merged == {'a': {'b': [2, 3]}}