
# Module: ansible.playbook.base
# test_fieldattributebase.py
from ansible.playbook.base import FieldAttributeBase
import pytest
import uuid

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_serialize_method(field_attribute):
    serialized_data = field_attribute.serialize()
    assert 'uuid' in serialized_data, "Expected 'uuid' to be in serialized data"
    assert isinstance(serialized_data['uuid'], str), f"Expected {type(str)} but got {type(serialized_data['uuid'])}"
    assert serialized_data['finalized'] == field_attribute._finalized, f"Expected {field_attribute._finalized} but got {serialized_data['finalized']}"
    assert serialized_data['squashed'] == field_attribute._squashed, f"Expected {field_attribute._squashed} but got {serialized_data['squashed']}"
    assert 'finalized' in serialized_data, "Expected 'finalized' to be in serialized data"