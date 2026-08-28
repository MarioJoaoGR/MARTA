
import pytest
from ansible.playbook.base import FieldAttributeBase

def test_get_variable_manager():
    field_attribute = FieldAttributeBase()
    assert hasattr(field_attribute, '_variable_manager'), "FieldAttributeBase should have a _variable_manager attribute"
    assert callable(field_attribute.get_variable_manager), "_variable_manager should be callable"
    variable_manager = field_attribute.get_variable_manager()
    assert isinstance(variable_manager, object), f"_variable_manager should return an instance of {object.__name__}"
