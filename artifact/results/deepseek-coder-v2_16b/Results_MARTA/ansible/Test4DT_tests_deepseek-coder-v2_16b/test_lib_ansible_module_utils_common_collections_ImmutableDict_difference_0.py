
import pytest
from ansible.module_utils.common.collections import ImmutableDict


def test_invalid_input():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    
    # Test with a non-iterable type (int)
    with pytest.raises(TypeError):
        filtered_dict_invalid_type = original_dict.difference(42)  # int is not iterable