
import pytest
from ansible.playbook.base import FieldAttributeBase

def test_extend_value_with_list():
    field = FieldAttributeBase()
    value = [1, 2]
    new_value = [3, 4]
    extended_value = field._extend_value(value, new_value)
    assert isinstance(extended_value, list), "Expected a list"
    assert extended_value == [1, 2, 3, 4], "Extended value should be [1, 2, 3, 4]"

def test_extend_value_with_non_list():
    field = FieldAttributeBase()
    value = 1
    new_value = 2
    extended_value = field._extend_value(value, new_value)
    assert isinstance(extended_value, list), "Expected a list"
    assert extended_value == [1, 2], "Extended value should be [1, 2]"

def test_extend_value_prepend():
    field = FieldAttributeBase()
    value = [1, 2]
    new_value = [3, 4]
    extended_value = field._extend_value(value, new_value, prepend=True)
    assert isinstance(extended_value, list), "Expected a list"
    assert extended_value == [3, 4, 1, 2], "Prepended value should be [3, 4, 1, 2]"

def test_extend_value_removes_duplicates():
    field = FieldAttributeBase()
    value = [1, 2, 2]
    new_value = [3, 4, 4]
    extended_value = field._extend_value(value, new_value)
    assert isinstance(extended_value, list), "Expected a list"
    assert extended_value == [1, 2, 3, 4], "Duplicates should be removed"

def test_extend_value_handles_none():
    field = FieldAttributeBase()
    value = None
    new_value = [1, 2]
    extended_value = field._extend_value(value, new_value)
    assert isinstance(extended_value, list), "Expected a list"
    assert extended_value == [1, 2], "None values should be stripped"
