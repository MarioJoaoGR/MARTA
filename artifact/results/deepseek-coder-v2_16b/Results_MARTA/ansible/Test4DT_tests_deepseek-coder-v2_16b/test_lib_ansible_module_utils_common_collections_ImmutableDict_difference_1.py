
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_edge_difference():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    filtered_dict = original_dict.difference(['key1'])
    assert len(filtered_dict) == 2, f"Expected length of 2 but got {len(filtered_dict)}"
    assert 'key1' not in filtered_dict, "Key 'key1' should be removed from the dictionary"
    assert 'key2' in filtered_dict and filtered_dict['key2'] == 'value2', f"Expected value for key 'key2' to be 'value2' but got {filtered_dict['key2']}"
    assert 'key3' in filtered_dict and filtered_dict['key3'] == 'value3', f"Expected value for key 'key3' to be 'value3' but got {filtered_dict['key3']}"

def test_invalid_difference():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    with pytest.raises(TypeError):
        filtered_dict = original_dict.difference(None)
