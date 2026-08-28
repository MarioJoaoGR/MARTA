
import pytest
from ansible.playbook.base import FieldAttributeBase

def test_get_variable_manager():
    field_attribute = FieldAttributeBase()
    assert field_attribute.get_variable_manager() is None, "Expected _variable_manager to be initially set to None"
