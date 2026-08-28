
import pytest
from ansible.utils.vars import merge_hash

# Test case 1: Basic Merge
def test_merge_basic():
    merged = merge_hash({'a': 1}, {'b': 2})
    assert merged == {'a': 1, 'b': 2}

# Test case 2: Merge with Recursive False
def test_merge_recursive_false():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': 3}}, recursive=False)
    assert merged == {'a': {'b': 3}}

# Test case 3: Merge with List Merge 'append'

# Test case 4: Merge with List Merge 'prepend'

# Test case 5: Merge with List Merge 'append_rp'

# Test case 6: Merge with List Merge 'prepend_rp'
def test_merge_list_prepend_rp():
    merged = merge_hash({'a': [1, 2]}, {'a': {'b': [2, 3]}}, list_merge='prepend_rp')
    assert merged == {'a': {'b': [2, 3]}}