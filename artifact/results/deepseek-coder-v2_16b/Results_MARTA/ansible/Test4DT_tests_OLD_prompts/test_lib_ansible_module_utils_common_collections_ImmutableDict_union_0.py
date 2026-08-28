
import pytest
from ansible.module_utils.common.collections import ImmutableDict


def test_invalid_union():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    another_dict = {'key3': 'value3'}
    combined_dict = immutable_dict.union(another_dict)
    assert isinstance(combined_dict, ImmutableDict), "The result should be an instance of ImmutableDict"
    assert combined_dict != {'key1': 'value1', 'key2': 'value2'}, "Combined dictionary should not match expected values"