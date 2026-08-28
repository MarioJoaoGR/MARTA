
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_valid_input():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'
