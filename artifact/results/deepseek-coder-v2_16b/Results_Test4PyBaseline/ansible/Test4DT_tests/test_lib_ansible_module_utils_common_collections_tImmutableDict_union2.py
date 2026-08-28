
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization of ImmutableDict with initial key-value pairs
def test_init_with_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test initialization of ImmutableDict with keyword arguments
def test_init_with_kwargs():
    immutable_dict = ImmutableDict(key1='value1', key2='value2')
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test accessing values by key
def test_get():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict.get('key1') == 'value1'