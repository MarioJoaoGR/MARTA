
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_invalid_input():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['key1'] = 'new_value'
