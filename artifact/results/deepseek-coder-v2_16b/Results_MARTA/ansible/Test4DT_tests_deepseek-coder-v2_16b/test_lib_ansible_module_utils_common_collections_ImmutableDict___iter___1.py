
import pytest
from ansible.module_utils.common.collections import ImmutableDict


def test_accessing_value():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1', f"Expected value for key 'key1' to be 'value1' but got {immutable_dict['key1']}"
