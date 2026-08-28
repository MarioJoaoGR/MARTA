# Module: ansible.playbook.base
# test_field_attribute_base.py
from ansible.playbook.base import FieldAttributeBase
import pytest
from copy import deepcopy

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_initialization(field_attribute):
    assert hasattr(field_attribute, '_loader'), "Expected _loader to be initialized"
    assert hasattr(field_attribute, '_variable_manager'), "Expected _variable_manager to be initialized"
    assert not field_attribute._validated, "_validated should initially be False"
    assert not field_attribute._squashed, "_squashed should initially be False"
    assert not field_attribute._finalized, "_finalized should initially be False"
    assert isinstance(field_attribute._uuid, str), "Expected _uuid to be a string"
    assert hasattr(field_attribute, '_attributes'), "Expected _attributes to be initialized"
    assert hasattr(field_attribute, '_attr_defaults'), "Expected _attr_defaults to be initialized"
    assert isinstance(field_attribute.vars, dict), "Expected vars to be a dictionary"

def test_copy_method(field_attribute):
    copied_field = field_attribute.copy()
    assert isinstance(copied_field, FieldAttributeBase), "Copy method should return an instance of FieldAttributeBase"
    assert copied_field._loader == field_attribute._loader, "_loader not correctly copied"
    assert copied_field._variable_manager == field_attribute._variable_manager, "_variable_manager not correctly copied"
    assert copied_field._validated == field_attribute._validated, "_validated not correctly copied"
    assert copied_field._finalized == field_attribute._finalized, "_finalized not correctly copied"
    assert copied_field._uuid == field_attribute._uuid, "_uuid not correctly copied"
    for key in field_attribute._attributes:
        assert field_attribute._attributes[key] == copied_field._attributes[key], f"{key} attribute not correctly copied"
    for key in field_attribute._attr_defaults:
        assert field_attribute._attr_defaults[key] == copied_field._attr_defaults[key], f"{key} default attribute not correctly copied"

def test_copy_method_with_ds(field_attribute):
    # Set a ds value on the original object to ensure it is copied
    field_attribute._ds = "test_ds"
    copied_field = field_attribute.copy()
    assert hasattr(copied_field, '_ds'), "_ds not correctly copied"
    assert copied_field._ds == "test_ds", "_ds value not correctly copied"
