
import pytest
from lib.ansible.module_utils.common.collections import ImmutableDict


def test_access_value():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'

def test_length_of_immutable_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert len(immutable_dict) == 2

def test_union_method():
    initial_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    another_dict = {'key3': 'value3'}
    combined_dict = initial_dict.union(another_dict)
    assert isinstance(combined_dict, ImmutableDict)
    assert combined_dict == ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})

def test_difference_method():
    initial_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    keys_to_exclude = ['key1']
    filtered_dict = initial_dict.difference(keys_to_exclude)
    assert isinstance(filtered_dict, ImmutableDict)
    assert filtered_dict == ImmutableDict({'key2': 'value2', 'key3': 'value3'})