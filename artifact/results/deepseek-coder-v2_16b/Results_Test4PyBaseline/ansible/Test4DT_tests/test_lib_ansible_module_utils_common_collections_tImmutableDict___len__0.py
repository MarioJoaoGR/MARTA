# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with a dictionary literal
def test_initialization():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert list(immutable_dict.items()) == [('key1', 'value1'), ('key2', 'value2')]

# Test attempting to update the dictionary raises TypeError
def test_update():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'

# Test len method
def test_len():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert len(immutable_dict) == 2

# Test iteration over keys and values
def test_iteration():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    items = list(immutable_dict.items())
    assert ('key1', 'value1') in items
    assert ('key2', 'value2') in items
