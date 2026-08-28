
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_edge_difference():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    filtered_dict = original_dict.difference(['key1'])
    assert isinstance(filtered_dict, ImmutableDict)
    assert len(filtered_dict) == 2
    assert list(filtered_dict.keys()) == ['key2', 'key3']

def test_invalid_difference():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    with pytest.raises(TypeError):
        filtered_dict = original_dict.difference(None)
