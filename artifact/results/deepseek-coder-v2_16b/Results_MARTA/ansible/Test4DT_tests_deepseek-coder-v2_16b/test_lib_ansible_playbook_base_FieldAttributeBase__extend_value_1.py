
import pytest
from ansible.playbook.base import FieldAttributeBase

def test_extend_value_with_prepend():
    field = FieldAttributeBase()
    extended_value = field._extend_value([1, 2], [3, 4], prepend=True)
    assert extended_value == [3, 4, 1, 2]

def test_extend_value_without_prepend():
    field = FieldAttributeBase()
    extended_value = field._extend_value([1, 2], [3, 4])
    assert extended_value == [1, 2, 3, 4]

def test_extend_value_with_none():
    field = FieldAttributeBase()
    extended_value = field._extend_value(None, [3, 4])
    assert extended_value == [3, 4]

def test_extend_value_with_sentinel():
    field = FieldAttributeBase()
    extended_value = field._extend_value([1, 2], [3, 4], prepend=True)
    assert extended_value == [3, 4, 1, 2]
