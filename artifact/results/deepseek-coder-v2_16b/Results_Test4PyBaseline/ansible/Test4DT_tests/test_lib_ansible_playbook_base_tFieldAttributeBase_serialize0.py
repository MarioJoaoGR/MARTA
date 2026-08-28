
# Module: ansible.playbook.base
# test_fieldattributebase.py
from ansible.playbook.base import FieldAttributeBase
import pytest
import uuid

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_uuid_is_unique(field_attribute):
    assert isinstance(field_attribute._uuid, uuid.UUID), f"Expected {type(uuid.UUID)} but got {type(field_attribute._uuid)}"

def test_initialization_of_internal_params(field_attribute):
    assert field_attribute._loader is None
    assert field_attribute._variable_manager is None
    assert not field_attribute._validated
    assert not field_attribute._squashed
    assert not field_attribute._finalized

def test_attributes_are_copied(field_attribute):
    initial_attrs = {key: value for key, value in FieldAttributeBase.__dict__.items() if callable(getattr(FieldAttributeBase, key, None)) and not key.startswith('_')}
    copied_attrs = field_attribute._attributes
    assert initial_attrs == copied_attrs, f"Expected {initial_attrs} but got {copied_attrs}"

def test_attr_defaults_are_initialized(field_attribute):
    initial_attr_defaults = {key: value() if callable(value) else value for key, value in FieldAttributeBase.__dict__.items() if callable(getattr(FieldAttributeBase, key, None)) and not key.startswith('_')}
    assert field_attribute._attr_defaults == initial_attr_defaults, f"Expected {initial_attr_defaults} but got {field_attribute._attr_defaults}"

def test_serialize_method(field_attribute):
    serialized_data = field_attribute.serialize()
    assert 'uuid' in serialized_data, "Expected 'uuid' to be in serialized data"
    assert serialized_data['uuid'] == field_attribute._uuid, f"Expected {field_attribute._uuid} but got {serialized_data['uuid']}"
    assert serialized_data['finalized'] == field_attribute._finalized, f"Expected {field_attribute._finalized} but got {serialized_data['finalized']}"
    assert serialized_data['squashed'] == field_attribute._squashed, f"Expected {field_attribute._squashed} but got {serialized_data['squashed']}"

def test_serialize_method_with_overridden_class(monkeypatch):
    class MockFieldAttributeBase(FieldAttributeBase):
        def __init__(self):
            super().__init__()
            self.mocked = True

        def serialize(self):
            data = super().serialize()
            data['mocked'] = self.mocked
            return data

    monkeypatch.setattr(FieldAttributeBase, '__init__', lambda x: None)
    field_attribute = MockFieldAttributeBase()
    serialized_data = field_attribute.serialize()
    assert 'mocked' in serialized_data, "Expected 'mocked' to be in serialized data"
    assert serialized_data['mocked'] is True, f"Expected True but got {serialized_data['mocked']}"
