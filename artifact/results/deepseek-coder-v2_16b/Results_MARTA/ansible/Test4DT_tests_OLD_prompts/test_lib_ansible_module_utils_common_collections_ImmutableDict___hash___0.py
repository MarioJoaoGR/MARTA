
import pytest
from ansible.module_utils.common.collections import ImmutableDict



def test_initialization_with_valid_input():
    immutable_dict = ImmutableDict({'key1': 'value1'})
    assert len(immutable_dict) == 1
    assert immutable_dict['key1'] == 'value1'

def test_hash_functionality():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    expected_hash = hash(frozenset(immutable_dict.items()))
    assert hash(immutable_dict) == expected_hash

def test_equality():
    dict1 = ImmutableDict({'key1': 'value1'})
    dict2 = ImmutableDict({'key1': 'value1'})
    dict3 = ImmutableDict({'key1': 'different_value'})
    
    assert dict1 == dict2
    assert not (dict1 == dict3)