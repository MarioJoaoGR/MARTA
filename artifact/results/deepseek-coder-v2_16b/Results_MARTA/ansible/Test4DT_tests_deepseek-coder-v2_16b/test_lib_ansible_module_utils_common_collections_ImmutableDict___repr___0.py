
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_error_case_1():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'
